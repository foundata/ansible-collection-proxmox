# Ansible role: `foundata.proxmox.pve`

The `foundata.proxmox.pve` Ansible role (part of the `foundata.proxmox` Ansible collection).



## Table of contents<a id="toc"></a>

- [Features](#features)<!-- ANSIBLE DOCSMITH TOC START -->
- [Role variables](#variables)
<!-- ANSIBLE DOCSMITH TOC END -->
- [Example playbooks, using this role](#examples)
- [Supported tags](#tags)
- [Dependencies](#dependencies)
- [Compatibility](#compatibility)
- [External requirements](#requirements)



## Features<a id="features"></a>

Main features:

- **Network Configuration**
  - Interface alternative names: Assign predictable names to NICs via systemd link files (preserves kernel names, avoids udev conflicts)
  - Flexible interface definitions: Separate host-specific and shared configurations for bonds, VLANs, bridges, and management interfaces
- **Firewall Management**
  - Manage datacenter-level options, policies, and rules (`/etc/pve/firewall/cluster.fw`), define reusable address references for cleaner rule management etc. pp.
  - nftables support: modern firewall backend
- **Storage Management**
  - ZFS: pool creation (Automated pool provisioning with mirror, RAIDZ1/2/3 support and extensive disk validation); Create datasets with optional native encryption (AES-256-GCM), passphrase rotation support
  - NFS mounts: Network storage integration with reachability checks
  - Register storage backends for use in PVE web UI (`dir`, `zfspool` types)
- **Operating system configuration**
  - IOMMU/PCI passthrough: Automatic detection and GRUB configuration for Intel/AMD IOMMU


<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

See [`meta/argument_specs.yml`](./meta/argument_specs.yml) for all available role parameters and their description. [`vars/main.yml`](./vars/main.yml) contains internal variables you should not override (but their description might be interesting).

Additionally, there are variables read from other roles and/or the global scope (for example, host or group vars) as follows:

- None right now.
<!-- ANSIBLE DOCSMITH MAIN END -->


## Example playbooks, using this role<a id="examples"></a>

Configure Proxmox Virtual Environment Servers (PVE)

```yaml
---

- name: "Initialize the foundata.proxmox.pve role"
  hosts: pve_cluster
  gather_facts: false
  tasks:

    - name: "Trigger invocation of the foundata.proxmox.pve role"
      ansible.builtin.include_role:
        name: "foundata.proxmox.pve"
      vars:

        ## It makes moste sense to put these variables into host vars.
        ## This is just done here inline as an example.

        # Storage configuration
        pve_proxmox_storage:
          # Local SSD mirror (low-latency, high-IOPS, SAS)
          - name: "pool1"
            type: "zpool"
            attributes:
              mountpoint: "none"
              vdevs:
                - type: "mirror"
                  disks:
                    - "/dev/disk/by-id/scsi-123"
                    - "/dev/disk/by-id/scsi-234"
              pool_properties:
                ashift: "12"  # 4K sectors (default)

          - name: "pool1/pve-guest-crypt"
            type: "zfs_dataset"
            attributes:
              zfs_properties:
                mountpoint: "/mnt/pool1/pve-guest-crypt" # VMs use zvols, but containers require a mountpoint
                compression: "on"
                atime: "off"
                xattr: "sa"
                acltype: "off"
                encryption: "aes-256-gcm"
                keyformat: "passphrase"
                passphrase: "{{ vault_pwd_pve1_storage }}"
                passphrase_old: [] # List of old passphrases, only needed when changing passphrase
                keylocation: "prompt"

        # Storage Manager (pvesm) configuration
        pve_proxmox_sm:
          # Local SSD mirror (low-latency, high-IOPS, SAS)
          - name: "pve1-guest1"
            type: "zfspool"
            storage_properties:
              pool: "pool1/pve-guest-crypt"
              content:
                - "images" # Virtual machine disks
                - "rootdir" # Container data
              sparse: true # Enable thin provisioning (saves space for unused blocks)
              nodes:
                - "pve1"

        # Network configuration for this specific host
        pve_proxmox_net_ifaces_host_specific:
          sections:

            - title: "Proxmox VE (PVE) main connection (LACP, trunk)"
              interfaces:
                - name: "main1"
                  method: "manual"
                  auto: true
                  iface_properties:
                    mtu: 1500

                - name: "main2"
                  method: "manual"
                  auto: true
                  iface_properties:
                    mtu: 1500

                - name: "bond_main"
                  method: "manual"
                  auto: true
                  iface_properties:
                    bond-slaves: "main1 main2"
                    bond-mode: "802.3ad"
                    bond-miimon: 100
                    bond-lacp-rate: "fast"
                    bond-xmit-hash-policy: "layer2"
                    mtu: 1500


            - title: "Proxmox VE (PVE) management interfaces"
              interfaces:
                - name: "bond_main.0123"
                  method: "manual"
                  auto: true
                  iface_properties:
                    comment: "0123_virt"

                - name: "br0123"
                  method: "static"
                  auto: true
                  comment: |
                    If attaching VMs to this interface is needed some day, the br0020
                    definition has to be moved into /etc/network/interfaces to make it
                    available for the PVE GUI and should be named vmbr0020. Use
                    pve_proxmox_net_ifaces_workload_specific or
                    pve_proxmox_net_ifaces_workload_shared to do so.
                  iface_properties:
                    address: "10.201.20.110/24"
                    gateway: "10.201.20.1"
                    bridge-ports: "bond_main.0020"
                    bridge-stp: "off"
                    bridge-fd: 0
                    comment: "0020_virt (host bridge)"

        pve_proxmox_net_ifaces_workload_specific:
          sections:
            - title: "Corosync link"
              interfaces:
                - name: "sync1"
                  method: "static"
                  auto: true
                  iface_properties:
                    address: "192.168.20.110/24"
                    comment: "Corosync link1 (quad-port NIC, third port)"



        ## It makes moste sense to put these variables into group vars.
        ## This is just done here inline as an example.

        # Network configuration for all PVE hosts (shared data)
        pve_proxmox_net_ifaces_host_shared:
          sections:
            - title: "Proxmox VE (PVE) VLAN interfaces"
              interfaces:
                - name: "bond_main.0001"
                  method: "manual"
                  auto: true
                  iface_properties:
                    comment: "0001_net"

        pve_proxmox_net_ifaces_workload_shared:
          options_before: |
            source /etc/network/interfaces.d/*

          sections:
            - title: "Proxmox VE (PVE) workload bridge interfaces"
              interfaces:
                - name: "vmbr0001"
                  method: "manual"
                  auto: true
                  iface_properties:
                    bridge-ports: "bond_main.0001"
                    bridge-stp: off
                    bridge-fd: 0
                    comment: "0001_net"
```


## Supported tags<a id="tags"></a>

It might be useful and faster to only call parts of the role by using tags:

- `pve_proxmox_os`: Manage basic operating system configuration influencing Proxmox Virtual Environment (PVE) (like IOMMU support)
- `pve_proxmox_network`: Manage network and network interface configuration.
- `pve_proxmox_firewall`: Manage firewall configuration.
- `pve_proxmox_storage`: Manage storage configuration.
- `pve_proxmox_datacenter`: Manage the Proxmox Virtual Environment (PVE) datacenter configuration

There are also tags usually not meant to be called directly but listed for the sake of completeness** and edge cases:

- `pve_proxmox_always`, `always`: Tasks needed by the role itself for internal role setup and the Ansible environment.



## Dependencies<a id="dependencies"></a>

See `dependencies` in [`meta/main.yml`](./meta/main.yml).



## Compatibility<a id="compatibility"></a>

See `min_ansible_version` in [`meta/main.yml`](./meta/main.yml) and `__pve_proxmox_supported_platforms` in [`vars/main.yml`](./vars/main.yml).



## External requirements<a id="requirements"></a>

There are no special requirements not covered by Ansible itself.
