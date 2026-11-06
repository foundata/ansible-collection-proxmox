# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Regressions for secret handling and truthful NFS observations."""

import copy
import hashlib

import pytest
import yaml
from _pve_tasks import ROLE, assertion, flatten, run_play, select

SECRET = "SYNTHETIC_CURRENT_SECRET_712d"
OLD_SECRET = "SYNTHETIC_OLD_SECRET_84ce"


def encrypted_storage():
    return {
        "name": "fixture/private",
        "type": "zfs_dataset",
        "attributes": {
            "zfs_properties": {
                "encryption": "aes-256-gcm",
                "keyformat": "passphrase",
                "keylocation": "prompt",
                "passphrase": SECRET,
                "passphrase_old": [OLD_SECRET],
            }
        },
    }


@pytest.mark.parametrize("keystatus", ["available", "unavailable"])
def test_keystatus_results_and_verbose_callbacks_exclude_secrets(tmp_path, keystatus):
    storage = encrypted_storage()
    role_vars = yaml.safe_load((ROLE / "vars/main.yml").read_text())
    probe = select("storage", "Check if encryption keys are loaded")
    probe["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%s", keystatus]
    output = run_play(
        tmp_path,
        [
            probe,
            {
                "name": "Expose only the public probe result",
                "ansible.builtin.debug": {"var": "__pve_zfs_dataset_keystatus"},
            },
        ],
        {
            "pve_proxmox_storage": [storage],
            "__pve_storage_sanitized": role_vars["__pve_storage_sanitized"],
            "__pve_zfs_dataset_exists": {storage["name"]: True},
        },
    )
    assert SECRET not in output
    assert OLD_SECRET not in output
    assert keystatus in output


def test_prompt_key_load_resolves_only_the_matching_credential(tmp_path):
    storage = encrypted_storage()
    sanitized = copy.deepcopy(storage)
    sanitized["attributes"]["zfs_properties"].pop("passphrase")
    sanitized["attributes"]["zfs_properties"].pop("passphrase_old")
    other = encrypted_storage()
    other["name"] = "fixture/other"
    other["attributes"]["zfs_properties"]["passphrase"] = "WRONG_DATASET_SECRET"
    load = select(
        "storage", "Load encryption keys for volumes with prompt-based passphrase"
    )
    load["ansible.builtin.command"]["argv"] = ["/usr/bin/sha256sum"]
    load["register"] = "fixture_load"
    output = run_play(
        tmp_path,
        [
            load,
            assertion(
                "fixture_load['results'][0]['stdout'].split()[0] == fixture_expected"
            ),
        ],
        {
            "pve_proxmox_storage": [other, storage],
            "fixture_expected": hashlib.sha256((SECRET + "\n").encode()).hexdigest(),
            "__pve_zfs_dataset_keystatus": {
                "results": [
                    {
                        "stdout": "unavailable",
                        "__pve_proxmox_keystatus_item": sanitized,
                        "__pve_zfs_dataset_index": 1,
                    }
                ]
            },
        },
    )
    assert SECRET not in output
    assert OLD_SECRET not in output
    assert "WRONG_DATASET_SECRET" not in output


def test_duplicate_dataset_names_keep_credential_positions(tmp_path):
    first = encrypted_storage()
    second = encrypted_storage()
    second["attributes"]["zfs_properties"]["passphrase"] = (
        "SYNTHETIC_SECOND_SECRET_a84e"
    )
    role_vars = yaml.safe_load((ROLE / "vars/main.yml").read_text())
    probe = select("storage", "Check if encryption keys are loaded")
    probe["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%s", "unavailable"]
    load = select(
        "storage", "Load encryption keys for volumes with prompt-based passphrase"
    )
    load["ansible.builtin.command"]["argv"] = ["/usr/bin/sha256sum"]
    load["register"] = "fixture_load"
    output = run_play(
        tmp_path,
        [
            probe,
            load,
            assertion(
                "fixture_load['results'][0]['stdout'].split()[0] == fixture_first"
            ),
            assertion(
                "fixture_load['results'][1]['stdout'].split()[0] == fixture_second"
            ),
        ],
        {
            "pve_proxmox_storage": [first, second],
            "__pve_storage_sanitized": role_vars["__pve_storage_sanitized"],
            "__pve_zfs_dataset_exists": {first["name"]: True},
            "fixture_first": hashlib.sha256((SECRET + "\n").encode()).hexdigest(),
            "fixture_second": hashlib.sha256(
                (second["attributes"]["zfs_properties"]["passphrase"] + "\n").encode()
            ).hexdigest(),
        },
    )
    assert SECRET not in output
    assert OLD_SECRET not in output
    assert "SYNTHETIC_SECOND_SECRET_a84e" not in output


@pytest.mark.parametrize(
    "returncode, expected", [(0, True), (1, False), (127, False), (None, False)]
)
def test_nfs_status_uses_return_code(tmp_path, returncode, expected):
    result = {
        "failed": False,
        "stdout": "",
        "__pve_proxmox_nfs_mount_item": {"name": "fixture"},
    }
    if returncode is not None:
        result["rc"] = returncode
    run_play(
        tmp_path,
        [
            select("storage", "Build mount status dictionary"),
            assertion(
                "__pve_nfs_mount_status['fixture']['is_mounted'] == fixture_expected"
            ),
        ],
        {
            "__pve_nfs_current_mounts": {"results": [result]},
            "fixture_expected": expected,
        },
    )


@pytest.mark.parametrize("returncode", [1, 127, None])
def test_nfs_report_does_not_claim_failed_or_skipped_probes_are_accessible(
    tmp_path, returncode
):
    result = {
        "failed": False,
        "__pve_proxmox_nfs_verify_item": {
            "name": "fixture",
            "attributes": {"storage_properties": {"path": "/synthetic"}},
        },
    }
    if returncode is not None:
        result["rc"] = returncode
    else:
        result["skipped"] = True
    output = run_play(
        tmp_path,
        [select("storage", "Report mount verification results")],
        {"__pve_nfs_mount_verify": {"results": [result]}},
    )
    assert "is mounted and accessible" not in output


def optional_storage_task(suffix):
    tasks = yaml.safe_load((ROLE / "tasks/storage/default.yml").read_text())
    return [
        copy.deepcopy(task)
        for task in flatten(tasks)
        if task.get("name", "").endswith(suffix)
    ]


def test_repeated_storage_invocations_forget_previous_disks(tmp_path):
    resets = optional_storage_task("Reset invocation-local discovery state")
    storage = {
        "name": "current",
        "type": "zpool",
        "attributes": {
            "vdevs": [{"type": "mirror", "disks": ["/dev/first", "/dev/second"]}]
        },
    }
    extract = select("storage", "Extract all disks from vdevs")
    build = select("storage", "Build disk check list")
    run_play(
        tmp_path,
        [
            *resets,
            extract,
            build,
            *copy.deepcopy(resets),
            copy.deepcopy(extract),
            copy.deepcopy(build),
            assertion("__pve_zpool_all_disks.keys() | list == ['current']"),
            assertion("__pve_disk_check_list | length == 2"),
            assertion(
                "__pve_disk_check_list | map(attribute='pool') | unique | list == ['current']"
            ),
        ],
        {
            "__pve_zpool_all_disks": {"retired": ["/dev/old"]},
            "__pve_disk_check_list": [{"pool": "retired", "disk": "/dev/old"}],
            "pve_proxmox_storage": [storage],
            "__pve_storage_sanitized": [storage],
        },
    )


@pytest.mark.parametrize(
    "value, failure",
    [
        ("available", None),
        ("unavailable", None),
        ("", "Cannot verify ZFS key availability"),
        ("unavail", "Cannot verify ZFS key availability"),
        ("available extra", "Cannot verify ZFS key availability"),
    ],
)
@pytest.mark.parametrize("check", [False, True])
def test_key_status_is_verified_before_loading(tmp_path, value, failure, check):
    storage = encrypted_storage()
    role_vars = yaml.safe_load((ROLE / "vars/main.yml").read_text())
    probe = select("storage", "Check if encryption keys are loaded")
    probe["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%s", value]
    run_play(
        tmp_path,
        [
            probe,
            *optional_storage_task("Validate encryption key status"),
            assertion(
                "not (__pve_zfs_dataset_keystatus['results'][0]['skipped'] | default(false))"
            ),
        ],
        {
            "pve_proxmox_storage": [storage],
            "__pve_storage_sanitized": role_vars["__pve_storage_sanitized"],
            "__pve_zfs_dataset_exists": {storage["name"]: True},
        },
        check=check,
        expected_failure=failure,
    )


def test_failed_key_status_read_stops_before_loading(tmp_path):
    storage = encrypted_storage()
    role_vars = yaml.safe_load((ROLE / "vars/main.yml").read_text())
    probe = select("storage", "Check if encryption keys are loaded")
    probe["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%"]
    run_play(
        tmp_path,
        [probe, *optional_storage_task("Validate encryption key status")],
        {
            "pve_proxmox_storage": [storage],
            "__pve_storage_sanitized": role_vars["__pve_storage_sanitized"],
            "__pve_zfs_dataset_exists": {storage["name"]: True},
        },
        expected_failure="non-zero return code",
    )


@pytest.mark.parametrize(
    "desired, actual, failure",
    [
        ("aes-256-gcm", "off", "Existing dataset encryption does not match"),
        ("aes-256-gcm", "aes-128-gcm", "Existing dataset encryption does not match"),
        ("on", "aes-256-gcm", None),
        ("aes-256-gcm", "aes-256-gcm", None),
        ("aes-256-gcm", "", "Existing dataset encryption does not match"),
        ("invalid", "invalid", "Existing dataset encryption does not match"),
    ],
)
def test_existing_encryption_mismatch_is_rejected(tmp_path, desired, actual, failure):
    storage = encrypted_storage()
    storage["attributes"]["zfs_properties"]["encryption"] = desired
    role_vars = yaml.safe_load((ROLE / "vars/main.yml").read_text())
    probe = select("storage", "Check encryption status of existing volumes")
    probe["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%s", actual]
    run_play(
        tmp_path,
        [probe, *optional_storage_task("Validate existing dataset encryption")],
        {
            "pve_proxmox_storage": [storage],
            "__pve_storage_sanitized": role_vars["__pve_storage_sanitized"],
            "__pve_zfs_dataset_exists": {storage["name"]: True},
        },
        expected_failure=failure,
    )


def test_encryption_preflight_precedes_dataset_mutation():
    tasks = list(
        flatten(yaml.safe_load((ROLE / "tasks/storage/default.yml").read_text()))
    )
    names = [task["name"] for task in tasks]
    validation = next(
        index
        for index, name in enumerate(names)
        if name.endswith("Validate existing dataset encryption")
    )
    for suffix in (
        "Create encrypted ZFS volumes with prompt-based passphrase",
        "Ensure mountpoint directories",
        "Update properties on existing non-encrypted ZFS volumes",
    ):
        mutation = next(
            index
            for index, name in enumerate(names)
            if "zfs_dataset" in name and name.endswith(suffix)
        )
        assert validation < mutation


def test_existing_plaintext_declaration_skips_key_operations(tmp_path):
    storage = {
        "name": "fixture/plaintext",
        "type": "zfs_dataset",
        "attributes": {"zfs_properties": {"encryption": "off"}},
    }
    encryption = select("storage", "Check encryption status of existing volumes")
    encryption["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%s", "off"]
    probe = select("storage", "Check if encryption keys are loaded")
    probe["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "%s", "-"]
    load = select(
        "storage", "Load encryption keys for volumes with prompt-based passphrase"
    )
    load["ansible.builtin.command"]["argv"] = ["/usr/bin/sha256sum"]
    load["register"] = "fixture_load"
    rotation = select("storage", "Manage encryption key changes")
    stdin = rotation.pop("ansible.builtin.shell")["stdin"]
    rotation["ansible.builtin.command"] = {
        "argv": ["/usr/bin/sha256sum"],
        "stdin": stdin,
    }
    notice = select("storage", "Encryption key notice")
    notice["register"] = "fixture_notice"
    run_play(
        tmp_path,
        [
            encryption,
            select("storage", "Validate existing dataset encryption"),
            probe,
            select("storage", "Validate encryption key status"),
            load,
            rotation,
            notice,
            assertion("__pve_zfs_dataset_keystatus['results'][0]['skipped']"),
            assertion("fixture_load['results'][0]['skipped']"),
            assertion("__pve_zfs_passphrase_change['results'][0]['skipped']"),
            assertion("fixture_notice['results'][0]['skipped']"),
        ],
        {
            "pve_proxmox_storage": [storage],
            "__pve_storage_sanitized": [storage],
            "__pve_zfs_dataset_exists": {storage["name"]: True},
        },
    )
