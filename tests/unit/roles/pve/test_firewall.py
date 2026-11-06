# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Regressions for firewall validation and rollback snapshot ownership."""

import os

import pytest
import yaml
from _pve_tasks import ROLE, assertion, run_play, select


@pytest.mark.parametrize(
    "returncode, lines, expected",
    [
        (0, [], False),
        (127, ["command not found"], True),
        (1, [], True),
        (0, ["/etc/pve/firewall/cluster.fw (line 4): invalid entry"], True),
    ],
)
def test_firewall_validator_failure_is_not_accepted(
    tmp_path, returncode, lines, expected
):
    run_play(
        tmp_path,
        [
            select(
                "firewall", "Determine parse problems in the managed firewall files"
            ),
            assertion("(__pve_fw_compile_problems | length > 0) == fixture_expected"),
        ],
        {
            "__pve_fw_compile": {
                "rc": returncode,
                "stdout_lines": [],
                "stderr_lines": lines,
                "failed": False,
            },
            "__pve_fw_previous": {
                "results": [
                    {"__pve_proxmox_fw_capture_item": "/etc/pve/firewall/cluster.fw"}
                ]
            },
            "fixture_expected": expected,
        },
    )


@pytest.mark.parametrize("writer", ["localhost", "another-node"])
def test_firewall_rollback_only_captures_owned_cluster_policy(tmp_path, writer):
    tasks = yaml.safe_load((ROLE / "tasks/firewall/default.yml").read_text())
    capture = next(
        task for task in tasks if "__pve_fw_managed_files" in task.get("vars", {})
    )
    run_play(
        tmp_path,
        [
            {
                "name": "Evaluate actual rollback ownership",
                "ansible.builtin.set_fact": {
                    "fixture_paths": capture["vars"]["__pve_fw_managed_files"]
                },
            },
            assertion(
                "('/etc/pve/firewall/cluster.fw' in fixture_paths) == (inventory_hostname == __pve_cluster_writer)"
            ),
            assertion("'/etc/pve/nodes/fixture/host.fw' in fixture_paths"),
        ],
        {"__pve_cluster_writer": writer, "ansible_facts": {"hostname": "fixture"}},
    )


def test_firewall_unreadable_rollback_source_stops_before_writes(tmp_path):
    if os.geteuid() == 0:
        pytest.skip("This permission-denial regression needs an unprivileged user")
    source = tmp_path / "unreadable.fw"
    source.write_text("foreign policy\n")
    source.chmod(0)
    capture = select(
        "firewall",
        "Capture the current managed configuration files (for the validation rollback)",
    )
    capture["ansible.builtin.slurp"]["src"] = str(source)
    capture["loop"] = [str(source)]
    try:
        run_play(
            tmp_path,
            [capture],
            {"__pve_fw_file_status": {"results": [{"stat": {"exists": True}}]}},
            expected_failure="Permission denied",
        )
    finally:
        source.chmod(0o600)


def test_firewall_absent_rollback_source_is_not_a_read_failure(tmp_path):
    source = tmp_path / "absent.fw"
    capture = select(
        "firewall",
        "Capture the current managed configuration files (for the validation rollback)",
    )
    capture["ansible.builtin.slurp"]["src"] = str(source)
    capture["loop"] = [str(source)]
    run_play(
        tmp_path,
        [
            capture,
            assertion("__pve_fw_previous['results'][0]['content'] is not defined"),
        ],
        {"__pve_fw_file_status": {"results": [{"stat": {"exists": False}}]}},
    )
