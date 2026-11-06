# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Exercise the delivered network validation command with an owned fake ifup."""

import json
import os
import shlex
import subprocess

import pytest
from _pve_tasks import select


@pytest.mark.parametrize(
    "suffix",
    ["Render /etc/network/interfaces", "Render /etc/network/interfaces.d/10-host"],
)
@pytest.mark.parametrize(
    "returncode, output, accepted",
    [
        (0, "", True),
        (127, "missing command", False),
        (1, "", False),
        (1, "warning: unqualified warning", False),
        (0, "error: invalid interface", False),
        (
            1,
            'warning: vmbr0: bridge-fd: value of out range "0": valid attribute range: 2-255',
            True,
        ),
    ],
)
def test_network_validator_rejects_unknown_failure(
    tmp_path, suffix, returncode, output, accepted
):
    validator = select("network", suffix)["ansible.builtin.template"]["validate"]
    fixture = tmp_path / "ifup"
    fixture.write_text(
        f"#!/bin/sh\nprintf '%s\\n' {shlex.quote(output)}\nexit {returncode}\n"
    )
    fixture.chmod(0o700)
    validator = validator.replace("/usr/sbin/ifup", str(fixture))
    result = subprocess.run(
        shlex.split(validator % str(tmp_path / "interfaces")),
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    (tmp_path / "result.json").write_text(
        json.dumps(
            {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }
        )
    )
    assert (result.returncode == 0) == accepted


@pytest.mark.parametrize("grep_status", [2, 127])
def test_network_validator_rejects_failed_diagnostic_filter(tmp_path, grep_status):
    validator = select("network", "Render /etc/network/interfaces")[
        "ansible.builtin.template"
    ]["validate"]
    fixture = tmp_path / "ifup"
    fixture.write_text(
        "#!/bin/sh\nprintf '%s\\n' 'warning: vmbr0: bridge-fd: value of out range \"0\": valid attribute range: 2-255'\nexit 1\n"
    )
    fixture.chmod(0o700)
    grep = tmp_path / "grep"
    grep.write_text(f"#!/bin/sh\nexit {grep_status}\n")
    grep.chmod(0o700)
    validator = validator.replace("/usr/sbin/ifup", str(fixture))
    result = subprocess.run(
        shlex.split(validator % str(tmp_path / "interfaces")),
        env=dict(os.environ, PATH=str(tmp_path)),
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    assert result.returncode != 0
