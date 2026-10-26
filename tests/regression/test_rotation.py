# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Exercise role rotation framing and a synthetic native-command state machine."""

import hashlib
import json
import subprocess

import pytest
from _pve_tasks import assertion, run_play, select

CURRENT = "SYNTHETIC_CURRENT_78094a"
PREVIOUS = "SYNTHETIC_PREVIOUS_77bcf1"
WRONG = "SYNTHETIC_WRONG_5eef0b"


def storage(current=CURRENT, previous=PREVIOUS):
    return {
        "name": "fixture/private",
        "type": "zfs_dataset",
        "attributes": {
            "zfs_properties": {
                "encryption": "aes-256-gcm",
                "keyformat": "passphrase",
                "keylocation": "prompt",
                "passphrase": current,
                "passphrase_old": previous,
            }
        },
    }


def variables(declaration):
    return {
        "pve_proxmox_storage": [declaration],
        "__pve_zfs_dataset_exists": {declaration["name"]: True},
    }


def test_rotation_credentials_do_not_enter_task_environment():
    rotation = select("storage", "Manage encryption key changes")
    assert "__PVE_ZFS_PASS_NEW" not in rotation.get("environment", {})
    assert "__PVE_ZFS_PASSES_OLD" not in rotation.get("environment", {})
    assert "stdin" in rotation["ansible.builtin.shell"]


@pytest.mark.parametrize("previous", [PREVIOUS, [WRONG, PREVIOUS], []])
def test_rotation_stdin_transports_current_then_ordered_candidates(tmp_path, previous):
    rotation = select("storage", "Manage encryption key changes")
    stdin = rotation.pop("ansible.builtin.shell")["stdin"]
    rotation["ansible.builtin.command"] = {
        "argv": ["/usr/bin/sha256sum"],
        "stdin": stdin,
    }
    rotation["changed_when"] = False
    candidates = [previous] if isinstance(previous, str) else previous
    expected = hashlib.sha256(
        ("\n".join([CURRENT, *candidates]) + "\n").encode()
    ).hexdigest()
    output = run_play(
        tmp_path,
        [
            select("storage", "Validate rotation passphrase framing"),
            rotation,
            assertion(
                "__pve_zfs_passphrase_change['results'][0]['stdout'].split()[0] == fixture_digest"
            ),
        ],
        {**variables(storage(previous=previous)), "fixture_digest": expected},
    )
    for sentinel in (CURRENT, PREVIOUS, WRONG):
        assert sentinel not in output


@pytest.mark.parametrize("suffix", ["\nsecond", "\rsecond", "\x00second"])
@pytest.mark.parametrize("field", ["passphrase", "passphrase_old"])
def test_rotation_rejects_ambiguous_framing_without_logging_secrets(
    tmp_path, suffix, field
):
    declaration = storage()
    declaration["attributes"]["zfs_properties"][field] = CURRENT + suffix
    validation = select("storage", "Validate rotation passphrase framing")
    validation["register"] = "fixture_validation"
    validation["ignore_errors"] = True
    output = run_play(
        tmp_path,
        [
            validation,
            assertion("fixture_validation is failed"),
            assertion(
                "fixture_validation['results'][0]['msg'] == 'ZFS rotation passphrases must be single-line strings without NUL bytes.'"
            ),
        ],
        variables(declaration),
    )
    for sentinel in (CURRENT, PREVIOUS):
        assert sentinel not in output


FAKE_ZFS = r"""#!/usr/bin/python3
import hashlib
import json
import os
import pathlib
import sys

state_path = pathlib.Path(os.environ["FIXTURE_STATE"])
state = json.loads(state_path.read_text())
state["invocations"] += 1
state_path.write_text(json.dumps(state))
arguments = sys.argv[1:]
assert arguments[-1] == "fixture/private"
if arguments[0] == "get":
    assert arguments[:4] == ["get", "-H", "-o", "value"]
    assert arguments[4] in ("keyformat", "keylocation", "encryptionroot")
    state["observations"].append(arguments[4])
    state_path.write_text(json.dumps(state))
    if state.get("failed_observation") == arguments[4]:
        sys.exit(1)
    print(state[arguments[4]])
    sys.exit(0)
assert arguments[:-1] in (["load-key", "-n", "-L", "prompt"], ["load-key", "-L", "prompt"], ["change-key"])
arguments = [value for value in arguments if value not in ("-L", "prompt")]
supplied = sys.stdin.readline().rstrip("\n")
parent = pathlib.Path("/proc") / str(os.getppid())
parent_argv = (parent / "cmdline").read_bytes()
parent_environment = (parent / "environ").read_bytes()
sentinels = [value.encode() for value in state["sentinels"]]
record = {
    "operation": arguments[:-1],
    "digest": hashlib.sha256(supplied.encode()).hexdigest(),
    "argv_secret": any(value in parent_argv for value in sentinels),
    "environment_secret": any(value in parent_environment for value in sentinels),
    "native_environment_secret": any(value.decode() in item for value in sentinels for item in os.environ.values()),
}
state["events"].append(record)
returncode = 0
if arguments[0] == "load-key":
    if "-n" in arguments and supplied == state.get("uncertain_candidate"):
        print(state.get("uncertain_error", "Key load error: Permission denied."), file=sys.stderr)
        print("0 / 1 key(s) successfully verified")
        returncode = 255
    elif "-n" not in arguments and state["loaded"]:
        print("Key load error: Key already loaded for 'fixture/private'.", file=sys.stderr)
        returncode = 255
    elif supplied != state["key"]:
        print("Key load error: Incorrect key provided for 'fixture/private'.", file=sys.stderr)
        print("0 / 1 key(s) successfully verified")
        returncode = 255
    elif "-n" not in arguments:
        state["loaded"] = True
    else:
        print("1 / 1 key(s) successfully verified")
else:
    assert state["loaded"]
    state["key"] = supplied
    if state.get("fail_after_change"):
        returncode = 1
state_path.write_text(json.dumps(state))
sys.exit(returncode)
"""


def run_rotation(
    directory,
    current,
    previous,
    *,
    initial=None,
    fail_read=False,
    export_seed=None,
    dataset_name="fixture/private",
    shell_options=None,
):
    directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    binary_directory = directory / "bin"
    binary_directory.mkdir(exist_ok=True)
    fake_zfs = binary_directory / "zfs"
    fake_zfs.write_text(FAKE_ZFS)
    fake_zfs.chmod(0o700)
    for command in ("cat", "grep"):
        link = binary_directory / command
        if not link.exists():
            link.symlink_to(
                "/usr/bin/false"
                if fail_read and command == "cat"
                else f"/usr/bin/{command}"
            )
    state_path = directory / "state.json"
    if initial is not None:
        state_path.write_text(
            json.dumps(
                {
                    "events": [],
                    "invocations": 0,
                    "observations": [],
                    "keyformat": "passphrase",
                    "keylocation": "prompt",
                    "encryptionroot": "fixture/private",
                    "sentinels": [CURRENT, PREVIOUS, WRONG],
                    **initial,
                }
            )
        )
    script = select("storage", "Manage encryption key changes")[
        "ansible.builtin.shell"
    ]["cmd"]
    result = subprocess.run(
        ["/bin/bash", "-c", script],
        input="\n".join([current, *previous]) + "\n",
        env={
            "PATH": str(binary_directory),
            "FIXTURE_STATE": str(state_path),
            "__PVE_ZFS_DATASET": dataset_name,
            "LC_ALL": "C",
            **dict.fromkeys(export_seed or [], "inherited-export-marker"),
            **({"SHELLOPTS": shell_options} if shell_options else {}),
        },
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    state = json.loads(state_path.read_text())
    for event in state["events"]:
        assert not event["argv_secret"]
        assert not event["environment_secret"]
        assert not event["native_environment_secret"]
    for sentinel in (CURRENT, PREVIOUS, WRONG):
        assert sentinel not in result.stdout + result.stderr
    (directory / "result.json").write_text(
        json.dumps(
            {
                "rc": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "events": state["events"],
            },
            indent=2,
        )
    )
    return result, state


@pytest.mark.parametrize("loaded", [True, False])
def test_rotation_current_first_is_idempotent(tmp_path, loaded):
    result, state = run_rotation(
        tmp_path, CURRENT, [WRONG, PREVIOUS], initial={"key": CURRENT, "loaded": loaded}
    )
    assert result.returncode == 0
    assert result.stdout == ""
    assert [event["operation"] for event in state["events"]] == [["load-key", "-n"]]
    assert state["loaded"] == loaded


@pytest.mark.parametrize("loaded", [True, False])
def test_rotation_tries_previous_candidates_in_order_then_repeats_safely(
    tmp_path, loaded
):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [WRONG, PREVIOUS],
        initial={"key": PREVIOUS, "loaded": loaded},
    )
    assert result.returncode == 0, result.stderr
    assert "SUCCESS" in result.stdout
    assert state["key"] == CURRENT
    assert [event["operation"] for event in state["events"]] == [
        ["load-key", "-n"],
        ["load-key", "-n"],
        ["load-key", "-n"],
        ["load-key"],
        ["change-key"],
        ["load-key", "-n"],
    ]
    assert [event["digest"] for event in state["events"][:3]] == [
        hashlib.sha256(value.encode()).hexdigest()
        for value in (CURRENT, WRONG, PREVIOUS)
    ]
    repeat, repeated_state = run_rotation(tmp_path, CURRENT, [WRONG, PREVIOUS])
    assert repeat.returncode == 0
    assert repeat.stdout == ""
    assert len(repeated_state["events"]) == len(state["events"]) + 1
    assert repeated_state["events"][-1]["operation"] == ["load-key", "-n"]


def test_failed_candidates_do_not_change_the_key(tmp_path):
    result, state = run_rotation(
        tmp_path, CURRENT, [WRONG], initial={"key": PREVIOUS, "loaded": True}
    )
    assert result.returncode == 1
    assert "None of the old passphrases" in result.stderr
    assert state["key"] == PREVIOUS
    assert all(event["operation"] == ["load-key", "-n"] for event in state["events"])


def test_failed_change_does_not_blindly_retry(tmp_path):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [PREVIOUS],
        initial={"key": PREVIOUS, "loaded": True, "fail_after_change": True},
    )
    assert result.returncode == 1
    assert "Failed to change passphrase" in result.stderr
    assert state["key"] == CURRENT
    assert sum(event["operation"] == ["change-key"] for event in state["events"]) == 1
    repeat, repeated_state = run_rotation(tmp_path, CURRENT, [PREVIOUS])
    assert repeat.returncode == 0
    assert len(repeated_state["events"]) == len(state["events"]) + 1
    assert repeated_state["events"][-1]["operation"] == ["load-key", "-n"]


def test_failed_stdin_read_is_not_an_empty_candidate_success(tmp_path):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [PREVIOUS],
        initial={"key": PREVIOUS, "loaded": True},
        fail_read=True,
    )
    assert result.returncode == 1
    assert state["key"] == PREVIOUS
    assert state["events"] == []


@pytest.mark.parametrize(
    "property_name, value, diagnostic",
    [
        ("keyformat", "hex", "Rotation requires a declared encryption root"),
        (
            "keylocation",
            "file:///synthetic/key",
            "Rotation requires a declared encryption root",
        ),
        ("encryptionroot", "fixture", "Rotation requires a declared encryption root"),
        ("failed_observation", "keylocation", "Cannot verify encryption properties"),
    ],
)
def test_rotation_refuses_unverified_or_unsupported_key_sources(
    tmp_path, property_name, value, diagnostic
):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [PREVIOUS],
        initial={"key": PREVIOUS, "loaded": True, property_name: value},
    )
    assert result.returncode == 1
    assert diagnostic in result.stderr
    assert state["key"] == PREVIOUS
    assert state["events"] == []


def test_empty_candidates_preserve_existing_noop_behavior(tmp_path):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [],
        initial={
            "key": PREVIOUS,
            "loaded": True,
            "keylocation": "file:///synthetic/key",
        },
    )
    assert result.returncode == 0
    assert state["key"] == PREVIOUS
    assert state["events"] == []
    assert state["observations"] == []


@pytest.mark.parametrize("candidate", [CURRENT, WRONG])
@pytest.mark.parametrize(
    "diagnostic",
    [
        "Key load error: Permission denied.",
        "Key load error: Incorrect key provided for 'other/root'.",
        "unrecognized diagnostic",
    ],
)
def test_unknown_verification_failures_never_authorize_rotation(
    tmp_path, candidate, diagnostic
):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [WRONG, PREVIOUS],
        initial={
            "key": PREVIOUS,
            "loaded": True,
            "uncertain_candidate": candidate,
            "uncertain_error": diagnostic,
        },
    )
    assert result.returncode == 1
    assert "verification is indeterminate" in result.stderr
    assert state["key"] == PREVIOUS
    assert all(event["operation"] == ["load-key", "-n"] for event in state["events"])


@pytest.mark.parametrize(
    "variable",
    [
        "__PVE_ZFS_PASS_NEW",
        "__PVE_ZFS_PASSES_OLD",
        "__pve_pass",
        "__pve_old_pass_working",
    ],
)
def test_inherited_export_attributes_do_not_expose_credentials(tmp_path, variable):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [PREVIOUS],
        initial={"key": PREVIOUS, "loaded": True},
        export_seed=[variable],
    )
    assert result.returncode == 0
    assert state["key"] == CURRENT


@pytest.mark.parametrize(
    "dataset_name", ["", "-a", "-r", "fixture/private\nother", "fixture/private\rother"]
)
def test_invalid_dataset_identity_stops_before_native_invocation(
    tmp_path, dataset_name
):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [PREVIOUS],
        initial={"key": PREVIOUS, "loaded": True},
        dataset_name=dataset_name,
    )
    assert result.returncode == 1
    assert "Invalid dataset identity" in result.stderr
    assert state["invocations"] == 0


@pytest.mark.parametrize("shell_options", ["allexport", "xtrace", "allexport:xtrace"])
def test_inherited_shell_options_do_not_expose_credentials(tmp_path, shell_options):
    result, state = run_rotation(
        tmp_path,
        CURRENT,
        [PREVIOUS],
        initial={"key": PREVIOUS, "loaded": True},
        shell_options=shell_options,
    )
    assert result.returncode == 0
    assert state["key"] == CURRENT
