"""Regressions for secret handling and truthful NFS observations."""

import copy

import pytest
import yaml
from _pve_tasks import ROLE, assertion, run_play, select

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
    load["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "accepted"]
    load["register"] = "fixture_load"
    output = run_play(
        tmp_path,
        [
            load,
            assertion(
                "fixture_load['results'][0]['invocation']['module_args']['stdin'] == fixture_expected"
            ),
        ],
        {
            "pve_proxmox_storage": [other, storage],
            "fixture_expected": SECRET,
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
    load["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", "accepted"]
    load["register"] = "fixture_load"
    output = run_play(
        tmp_path,
        [
            probe,
            load,
            assertion(
                "fixture_load['results'][0]['invocation']['module_args']['stdin'] == fixture_first"
            ),
            assertion(
                "fixture_load['results'][1]['invocation']['module_args']['stdin'] == fixture_second"
            ),
        ],
        {
            "pve_proxmox_storage": [first, second],
            "__pve_storage_sanitized": role_vars["__pve_storage_sanitized"],
            "__pve_zfs_dataset_exists": {first["name"]: True},
            "fixture_first": SECRET,
            "fixture_second": second["attributes"]["zfs_properties"]["passphrase"],
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
