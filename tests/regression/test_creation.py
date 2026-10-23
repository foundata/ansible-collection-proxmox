"""Preserve explicit plaintext intent when selecting dataset creation tasks."""

import copy

import pytest
from _pve_tasks import assertion, run_play, select

CREATE_TASKS = (
    ("prompt", "Create encrypted ZFS volumes with prompt-based passphrase"),
    ("file", "Create encrypted ZFS volumes with non-prompt-based key (like file://)"),
    ("plain", "Create non-encrypted ZFS volumes"),
)


def storage_item(properties):
    return {
        "name": "fixture/data",
        "type": "zfs_dataset",
        "attributes": {"zfs_properties": properties},
    }


def variables(properties, exists=False):
    sanitized = {
        key: value
        for key, value in properties.items()
        if key not in {"passphrase", "passphrase_old"}
    }
    return {
        "pve_proxmox_storage": [storage_item(properties)],
        "__pve_storage_sanitized": [storage_item(sanitized)],
        "__pve_zfs_dataset_exists": {"fixture/data": exists},
        "__pve_creation_branch": "none",
        "__pve_creation_branches": [],
    }


def captured_creation_tasks():
    tasks = []
    for branch, suffix in CREATE_TASKS:
        task = select("storage", suffix)
        actions = [
            key
            for key in task
            if key
            in {
                "ansible.builtin.command",
                "ansible.builtin.shell",
                "community.general.zfs",
            }
        ]
        assert len(actions) == 1
        parameters = task.pop(actions[0])
        task.pop("args", None)
        task["ansible.builtin.set_fact"] = {
            "__pve_creation_branch": branch,
            "__pve_creation_branches": "{{ __pve_creation_branches + ['"
            + branch
            + "'] }}",
            "__pve_creation_parameters": parameters,
        }
        tasks.append(task)
    return tasks


@pytest.mark.parametrize("check", [False, True])
@pytest.mark.parametrize("exists", [False, True])
@pytest.mark.parametrize(
    ("encryption", "key_source", "branch"),
    [
        (None, None, "plain"),
        ("off", None, "plain"),
        ("on", "prompt", "prompt"),
        ("aes-256-gcm", "prompt", "prompt"),
        ("on", "file", "file"),
        ("aes-256-gcm", "file", "file"),
    ],
)
def test_creation_routes_preserve_declared_properties(
    tmp_path, check, exists, encryption, key_source, branch
):
    properties = {"compression": "lz4", "mountpoint": "none"}
    if encryption is not None:
        properties["encryption"] = encryption
    if key_source:
        properties["keyformat"] = "passphrase" if key_source == "prompt" else "raw"
        properties["keylocation"] = (
            "prompt" if key_source == "prompt" else "file:///fixture/key"
        )
    if key_source == "prompt":
        properties["passphrase"] = "synthetic-creation-sentinel"
    task_variables = variables(properties, exists)
    tasks = [
        select("storage", "Validate the declared storage items"),
        *captured_creation_tasks(),
    ]
    tasks.append(
        assertion(f"__pve_creation_branch == '{'none' if exists else branch}'")
    )
    tasks.append(assertion(f"__pve_creation_branches == {[] if exists else [branch]}"))
    if not exists:
        if branch == "plain":
            task_variables["expected_parameters"] = {
                "name": "fixture/data",
                "state": "present",
                "extra_zfs_properties": copy.deepcopy(properties),
            }
            tasks.append(assertion("__pve_creation_parameters == expected_parameters"))
        elif branch == "prompt":
            task_variables["expected_parameters"] = {
                "argv": [
                    "zfs",
                    "create",
                    "-o",
                    f"encryption={encryption}",
                    "-o",
                    "keyformat=passphrase",
                    "-o",
                    "keylocation=prompt",
                    "-o",
                    "compression=lz4",
                    "-o",
                    "mountpoint=none",
                    "fixture/data",
                ],
                "stdin": "synthetic-creation-sentinel",
            }
            tasks.append(assertion("__pve_creation_parameters == expected_parameters"))
        else:
            for argument in (
                f"encryption={encryption}",
                "keyformat=raw",
                "keylocation=file:///fixture/key",
                "compression=lz4",
                "mountpoint=none",
                "fixture/data",
            ):
                tasks.append(assertion(f"'{argument}' in __pve_creation_parameters"))
    output = run_play(tmp_path, tasks, task_variables, check=check)
    assert "synthetic-creation-sentinel" not in output


@pytest.mark.parametrize("check", [False, True])
@pytest.mark.parametrize("exists", [False, True])
@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("keyformat", "passphrase"),
        ("keylocation", "prompt"),
        ("keylocation", "file:///fixture/key"),
        ("pbkdf2iters", 350000),
        ("passphrase", "synthetic-off-envelope-sentinel"),
        ("passphrase_old", ["synthetic-off-envelope-sentinel"]),
    ],
)
def test_explicit_off_rejects_contradictory_key_envelope(
    tmp_path, check, exists, key, value
):
    output = run_play(
        tmp_path,
        [select("storage", "Validate the declared storage items")],
        variables({"encryption": "off", key: value}, exists),
        check=check,
        expected_failure="Storage item 'fixture/data' is invalid",
    )
    assert "synthetic-off-envelope-sentinel" not in output


@pytest.mark.parametrize("check", [False, True])
@pytest.mark.parametrize("encryption", [False, None, "unknown"])
def test_other_encryption_values_do_not_select_plain_creation(
    tmp_path, check, encryption
):
    tasks = captured_creation_tasks()
    for task in tasks:
        task["ansible.builtin.set_fact"].pop("__pve_creation_parameters")
    tasks.append(assertion("__pve_creation_branch == 'prompt'"))
    run_play(tmp_path, tasks, variables({"encryption": encryption}), check=check)
