# SPDX-FileCopyrightText: foundata GmbH <https://foundata.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Let the tests import their task harness under every runner."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
