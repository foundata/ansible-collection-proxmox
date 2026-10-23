"""Keep native activation failures visible without touching host storage."""

import pytest
from _pve_tasks import assertion, run_play, select


def mount_task(arguments):
    task = select("storage", "Mount encrypted volumes after key load")
    assert task["ansible.builtin.command"]["argv"][:2] == ["zfs", "mount"]
    task["ansible.builtin.command"]["argv"] = ["/usr/bin/printf", *arguments]
    task["register"] = "fixture_mount_result"
    return task


def key_observation(status="unavailable", skipped=False):
    return {
        "__pve_zfs_dataset_keystatus": {
            "results": [
                {
                    "stdout": status,
                    "skipped": skipped,
                    "__pve_proxmox_keystatus_item": {"name": "fixture/data"},
                }
            ]
        }
    }


def test_encrypted_mount_failure_stops_following_tasks(tmp_path):
    run_play(
        tmp_path,
        [
            mount_task(["%"]),
            {
                "name": "Reject continuation after failed native activation",
                "ansible.builtin.fail": {"msg": "activation incorrectly continued"},
            },
        ],
        key_observation(),
        expected_failure="non-zero return code",
    )
    assert (
        "activation incorrectly continued" not in (tmp_path / "output.log").read_text()
    )


def test_successful_encrypted_mount_keeps_change_reporting(tmp_path):
    run_play(
        tmp_path,
        [
            mount_task(["%s", ""]),
            assertion("fixture_mount_result['results'][0]['rc'] == 0"),
            assertion("fixture_mount_result['changed']"),
        ],
        key_observation(),
    )


def test_encrypted_mount_does_not_execute_in_check_mode(tmp_path):
    run_play(
        tmp_path,
        [
            mount_task(["%"]),
            assertion("fixture_mount_result['skipped']"),
            assertion("not fixture_mount_result['changed']"),
        ],
        key_observation(),
        check=True,
    )


@pytest.mark.parametrize(
    "status, skipped", [("available", False), ("unavailable", True)]
)
def test_nonselected_encrypted_mount_keeps_existing_skip(tmp_path, status, skipped):
    run_play(
        tmp_path,
        [
            mount_task(["%"]),
            assertion("fixture_mount_result['skipped']"),
            assertion("not fixture_mount_result['changed']"),
        ],
        key_observation(status, skipped),
    )
