=================================================
foundata.proxmox Ansible collection Release Notes
=================================================

.. contents:: Topics

v1.3.0
======

Minor Changes
-------------

- pve role - Add pve_proxmox_update_grub, pve_proxmox_reload_network and pve_proxmox_restart_firewall handler topics. Retain the previous update grub, reload network, restart pve-firewall and reload pve-firewall topics as migration aliases until version 2.0.0.

Security Fixes
--------------

- pve role - exclude current and previous ZFS passphrases from key-status loop results and verbose callbacks; resolve prompt credentials only within the protected key-loading task.
- pve role - pass current and previous ZFS rotation credentials through module stdin instead of task environment variables that can appear in remote shell process arguments; reject line breaks and NUL bytes before framing credentials.
- pve role - require freshly observed prompt-based passphrase keys on the declared encryption root before rotation, refusing file-key and inherited-root rotation rather than verifying the wrong credential.
- pve role - stop rotation on indeterminate credential verification instead of treating every native failure as an incorrect key; only the exact C-locale incorrect-key result permits trying previous credentials.

Bugfixes
--------

- Check the minimum ansible-core version before gathering role facts so unsupported versions fail with the intended diagnostic.
- Limit automatic fact gathering to each role's declared subsets while retaining missing-fact recovery and reuse of cached facts.
- The declared ansible-core minimum is corrected from 2.16 to 2.19. The roles write Jinja's own filters and tests as ``ansible.builtin.<name>``, which ansible-core resolves from 2.19 only; on 2.16 to 2.18 every run failed at the first such expression, so no working installation is affected.
- pve role - Gather the hostname and timestamp facts used by configuration and backup tasks explicitly, without relying on injected fact variables.
- pve role - Pass managed guest firewall options, aliases, IP sets and rules into the configuration template instead of leaving its section inputs unset.
- pve role - Read existing ZFS pools from the registered module result so disabling fact injection does not misclassify existing pools as missing.
- pve role - Reject invalid template inputs without depending on an ambient undefined variable, and identify invalid network interfaces in diagnostics.
- pve role - derive observed NFS mount status from command return codes, skip skipped verification results, and stop describing a mountpoint check as proof of server accessibility.
- pve role - propagate failures when mounting encrypted datasets after loading their keys instead of reporting success and continuing after failed activation.
- pve role - reject existing dataset encryption mismatches before dataset changes; accept the native encryption=on alias for encrypted ciphers.
- pve role - reject missing or failed network validators and unknown diagnostics while retaining the specific bridge-fd zero warning.
- pve role - reset storage discovery maps on each invocation instead of reusing previous disks and resource state.
- pve role - route new datasets with explicit encryption=off through ordinary creation while preserving that property, instead of selecting an encrypted creation task that requires key credentials. Reject contradictory key properties or passphrases with encryption=off before storage changes.
- pve role - skip key-status loading and encryption notices for existing datasets explicitly declared with encryption=off.
- pve role - stop on failed or malformed key-status reads before loading keys, including read-only discovery in check mode.
- pve role - treat failed firewall validation as a rollback condition, capture cluster policy only on its selected writer, and refuse unreadable rollback sources instead of treating them as absent.
- pve role - use bounded exact-name dataset discovery with strict native result validation instead of treating failed or empty facts as absence; require an independently observed imported pool root before creating an absent child.
- pve role - validate dataset selectors before native operations and allow existing encryption=off declarations through the passphrase-presence check.

v1.2.0
======

Release Summary
---------------

Release Date: 2026-08-28

Maintenance release.

Minor Changes
-------------

- ``pve`` - Improve Ansible compatibility for roles and collections used in the wild by giving every loop in the role a private, purpose-specific loop variable derived from the role's public variable prefix (``__pve_proxmox_*_item``) instead of ``item``. This avoids rebinding a caller's ``item`` when role parameters reference it, such as when the role itself is included from a loop, and makes the role behave more robustly across common Ansible usage patterns.

v1.1.1
======

Release Summary
---------------

Release Date: 2026-08-13

Bugfix release.

Minor Changes
-------------

- ``pve`` - existing ``pvesm`` storage IDs are no longer accepted by name alone: the type and backing (``path`` or ``pool``) of an existing storage have to match the declaration before any settings are reconciled onto it.
- ``pve`` - new option ``pve_proxmox_cluster_writer`` to pin the node that writes the cluster-wide pmxcfs files (per cluster, e.g. via group_vars), for rolling plays with ``serial`` batching or the ``free`` strategy where automatic writer selection cannot work.

Security Fixes
--------------

- ``pve`` - ZFS passphrases could appear in normal callback output: many storage tasks looped over the complete storage items, so loop labels and skipped-item lines printed ``passphrase``/``passphrase_old`` values. Storage loops now iterate a sanitized copy of ``pve_proxmox_storage`` with the secret keys stripped; only the tasks that genuinely need the passphrase (encrypted dataset creation, key loading, key rotation) read the original data and each of them is protected by ``no_log`` or a sanitized loop label.
- ``pve`` - ZFS passphrases were embedded in the text of the executed shell commands, making them world-readable in the process list of the managed host while the commands ran. They are now passed via stdin respectively the process environment, and the ``zfs_properties`` dictionary is marked ``no_log`` so Ansible logs and argument-validation output cannot leak the ``passphrase``/``passphrase_old`` values.

Bugfixes
--------

- ``pve`` - ``pve_proxmox_iommu_manage`` was accepted but never evaluated: even with the switch set to ``false`` the role probed IOMMU support, rewrote ``GRUB_CMDLINE_LINUX_DEFAULT`` and triggered ``update-grub``. The whole IOMMU block is now gated on the option, leaving existing kernel command line parameters untouched when it is disabled.
- ``pve`` - a mixed ``pve_proxmox_storage`` declaration of ZFS and NFS items failed: the type check inside the ZFS section looped over the whole list and rejected every ``nfs`` item as soon as any ZFS item existed. The validation now runs once for all items, checks the full supported type set and also enforces the attributes each type dereferences unconditionally (``vdevs`` for ``zpool``, ``src``/``path`` for ``nfs``, a ``passphrase`` for prompt-encrypted datasets, ``path``/``pool`` for the ``pve_proxmox_sm`` types).
- ``pve`` - property reconciliation for existing ZFS pools was dead code: it was gated on the NFS-only ``storage_properties`` field which zpool items never carry. It now triggers on ``zfs_properties`` and excludes the creation-only encryption keys that ``zfs set`` cannot change.
- ``pve`` - the cluster-wide pmxcfs files (``/etc/pve/datacenter.cfg``, ``/etc/pve/firewall/cluster.fw``) were written independently by every play host; with differing host variables the last writer silently won. One deterministically selected node per cluster now writes them and the role fails when the cluster-scoped inputs differ between nodes of the same cluster (standalone nodes are unaffected). Automatic selection is refused in plays where it would be wrong (``serial`` batching, the ``free`` strategy or hosts lost before the selection); use the new ``pve_proxmox_cluster_writer`` option there.
- ``pve`` - the disaster-safeguard backup directory (``pve_proxmox_tmpbackupfiles``) reported a change on every run (breaking idempotence) and made ``--check`` runs fail on the missing path. It no longer counts as a change and is created in check mode too; the backups themselves still honor check mode.
- ``pve`` - the firewall configuration is now checked with ``pve-firewall compile`` after rendering. The PVE parser deliberately skips broken entries with a message only (exit code 0), silently changing the effective policy; parse problems in the managed files now restore the previous file contents and fail the run before the firewall service is restarted.
- ``pve`` - the rendered network interface files are now validated with the ifupdown2 parser before installation (parse errors reject the candidate, the live configuration stays untouched) and applied via a configuration reload (``ifreload`` delta semantics) instead of a full networking restart. A malformed value could previously replace a working configuration and disconnect the host on the next restart or boot.
- boolean role arguments are now coerced with ``ansible.builtin.bool`` in every conditional. String values, as delivered by ``-e var=false`` command line extra-vars, were evaluated by truthiness before, so ``"false"`` enabled the gated behavior instead of disabling it.

v1.1.0
======

Release Summary
---------------

Release Date: 2026-07-30

Maintenance and bugfix release.

Minor Changes
-------------

- ``pve`` - properties of already configured ``pvesm`` storages (content, nodes, is_mountpoint, sparse, blocksize) are now compared and updated via ``pvesm set``. Previously a matching storage ID was considered complete and property changes were silently never applied.

Bugfixes
--------

- ``pve`` - ``pve_proxmox_net_altnames`` entries were gated on the first list entry instead of the entry at hand, so a defective first entry skipped all remaining (valid) ones.
- ``pve`` - ``pve_proxmox_state`` gated every configuration section but was neither defined nor documented, so the role failed with an undefined variable unless the caller invented it. It is now a documented role argument defaulting to ``present``.
- ``pve`` - cluster-wide firewall rules were rendered from a misspelled, nonexistent variable, so ``pve_proxmox_fw_cluster_rules`` entries were silently omitted from ``/etc/pve/firewall/cluster.fw``.
- ``pve`` - only the first vdev of a ZFS pool was validated, so invalid disk counts in later vdevs reached pool creation.
- ``pve`` - the NFS reachability warning was shown for every server (including reachable ones) instead of only when ``showmount`` failed.
- ``pve`` - the interfaces template failed on datasets without a ``sections`` key and ignored ``auto: false`` (an ``auto`` directive was rendered for every interface).
- ``pve`` - the role no longer renders ``/etc/network/interfaces`` and ``/etc/network/interfaces.d/10-host`` when the respective ``pve_proxmox_net_ifaces_*`` datasets are empty (the default). Replacing a working network configuration with an effectively empty file and restarting the network would have locked the host out.
- ``pve`` role - Platform-specific task files are now guaranteed to run before the shared default tasks. The former single include loop did not preserve that order with several platforms in one play: Ansible batches the includes across hosts and the insertion order depends on when results arrive (non-deterministic), so default tasks could run before platform-specific ones. The includes are now two sequential tasks, which is a hard ordering barrier.
- the collection now declares its ``community.general`` dependency (ZFS pool, dataset and facts modules).

v1.0.0
======

Release Summary
---------------

Release Date: 2025-12-09

First public release, providing all functionality and files.
