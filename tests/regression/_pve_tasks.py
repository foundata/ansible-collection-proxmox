# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Run selected role tasks without native storage, network or firewall operations."""

from __future__ import annotations

import copy
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

COLLECTION = Path(os.environ.get("PVE_TEST_COLLECTION", Path(__file__).parents[2]))
ROLE = COLLECTION / "roles/pve"


def flatten(tasks):
    for task in tasks:
        yield task
        for section in ("block", "rescue", "always"):
            yield from flatten(task.get(section, []))


def select(subsystem, suffix):
    tasks = yaml.safe_load((ROLE / f"tasks/{subsystem}/default.yml").read_text())
    matches = [task for task in flatten(tasks) if task.get("name", "").endswith(suffix)]
    assert len(matches) == 1, (suffix, len(matches))
    return copy.deepcopy(matches[0])


def assertion(expression):
    return {
        "name": "Check the regression postcondition",
        "ansible.builtin.assert": {"that": [expression]},
    }


def run_play(directory, tasks, variables=None, check=False, expected_failure=None):
    directory.mkdir(parents=True, exist_ok=True)
    allowed = {
        "ansible.builtin.assert",
        "ansible.builtin.command",
        "ansible.builtin.debug",
        "ansible.builtin.fail",
        "ansible.builtin.set_fact",
        "ansible.builtin.slurp",
        "ansible.builtin.stat",
    }
    for task in tasks:
        actions = {key for key in task if key.startswith("ansible.builtin.")}
        assert len(actions) == 1 and actions <= allowed, actions
        if "ansible.builtin.command" in task:
            argv = task["ansible.builtin.command"]["argv"]
            assert argv[0] == "/usr/bin/printf" or argv == ["/usr/bin/sha256sum"]
        for action in ("ansible.builtin.slurp", "ansible.builtin.stat"):
            if action in task:
                field = "src" if action.endswith("slurp") else "path"
                assert (
                    Path(task[action][field])
                    .resolve()
                    .is_relative_to(directory.resolve())
                )
    play = directory / "play.yml"
    play.write_text(
        yaml.safe_dump(
            [
                {
                    "name": "Run isolated role behavior regression",
                    "hosts": "localhost",
                    "connection": "local",
                    "gather_facts": False,
                    "become": False,
                    "vars": {
                        "ansible_python_interpreter": sys.executable,
                        **(variables or {}),
                    },
                    "tasks": tasks,
                }
            ],
            sort_keys=False,
        )
    )
    config = directory / "ansible.cfg"
    config.write_text("[defaults]\nretry_files_enabled = False\n")
    environment = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(("ANSIBLE_", "PYTHON", "PYTEST_"))
    }
    environment.update(
        ANSIBLE_CONFIG=str(config),
        ANSIBLE_HOME=str(directory / "home"),
        ANSIBLE_LOCAL_TEMP=str(directory / "local"),
        ANSIBLE_REMOTE_TEMP=str(directory / "remote"),
        ANSIBLE_COLLECTIONS_PATH=str(directory / "collections"),
        ANSIBLE_COLLECTIONS_SCAN_SYS_PATH="false",
        XDG_CACHE_HOME=str(directory / "cache"),
        PYTHONDONTWRITEBYTECODE="1",
    )
    executable = os.environ.get("PVE_TEST_ANSIBLE_PLAYBOOK") or shutil.which(
        "ansible-playbook"
    )
    assert executable, "ansible-playbook is required for the task regressions"
    command = [executable, "-i", "localhost,", str(play), "-vvv"]
    if check:
        command.append("--check")
    result = subprocess.run(
        command,
        cwd=directory,
        env=environment,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=45,
        check=False,
    )
    output = result.stdout + result.stderr
    (directory / "output.log").write_text(output)
    assert "PLAY RECAP" in output, output
    assert (result.returncode != 0) == bool(expected_failure), output
    if expected_failure:
        assert expected_failure in output, output
    return output
