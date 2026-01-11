# Ansible role: `foundata.proxmox.pve`

The `foundata.proxmox.pve` Ansible role (part of the `foundata.proxmox` Ansible collection).



## Table of contents<a id="toc"></a>

- [Features](#features)
- [Example playbooks, using this role](#examples)
- [Supported tags](#tags)<!-- ANSIBLE DOCSMITH TOC START -->
- [Role variables](#variables)
  - [`pve_proxmox_tmpbackupfiles`](#variable-pve_proxmox_tmpbackupfiles)
  - [`pve_proxmox_iommu_manage`](#variable-pve_proxmox_iommu_manage)
  - [`pve_proxmox_net_altnames`](#variable-pve_proxmox_net_altnames)
    - [`pve_proxmox_net_altnames['type']`](#variable-pve_proxmox_net_altnames-sub-type)
    - [`pve_proxmox_net_altnames['mac_address']`](#variable-pve_proxmox_net_altnames-sub-mac_address)
    - [`pve_proxmox_net_altnames['desc']`](#variable-pve_proxmox_net_altnames-sub-desc)
    - [`pve_proxmox_net_altnames['altnames']`](#variable-pve_proxmox_net_altnames-sub-altnames)
  - [`pve_proxmox_net_ifaces_host_shared`](#variable-pve_proxmox_net_ifaces_host_shared)
    - [`pve_proxmox_net_ifaces_host_shared['options_before']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-options_before)
    - [`pve_proxmox_net_ifaces_host_shared['sections']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections)
      - [`pve_proxmox_net_ifaces_host_shared['sections']['title']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-title)
      - [`pve_proxmox_net_ifaces_host_shared['sections']['comment']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-comment)
      - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['name']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-name)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['method']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-method)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['auto']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-auto)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['comment']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-comment)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['iface_properties']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-iface_properties)
    - [`pve_proxmox_net_ifaces_host_shared['options_after']`](#variable-pve_proxmox_net_ifaces_host_shared-sub-options_after)
  - [`pve_proxmox_net_ifaces_host_specific`](#variable-pve_proxmox_net_ifaces_host_specific)
    - [`pve_proxmox_net_ifaces_host_specific['options_before']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-options_before)
    - [`pve_proxmox_net_ifaces_host_specific['sections']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections)
      - [`pve_proxmox_net_ifaces_host_specific['sections']['title']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-title)
      - [`pve_proxmox_net_ifaces_host_specific['sections']['comment']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-comment)
      - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['name']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-name)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['method']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-method)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['auto']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-auto)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['comment']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-comment)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['iface_properties']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-iface_properties)
    - [`pve_proxmox_net_ifaces_host_specific['options_after']`](#variable-pve_proxmox_net_ifaces_host_specific-sub-options_after)
  - [`pve_proxmox_net_ifaces_workload_shared`](#variable-pve_proxmox_net_ifaces_workload_shared)
    - [`pve_proxmox_net_ifaces_workload_shared['options_before']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-options_before)
    - [`pve_proxmox_net_ifaces_workload_shared['sections']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections)
      - [`pve_proxmox_net_ifaces_workload_shared['sections']['title']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-title)
      - [`pve_proxmox_net_ifaces_workload_shared['sections']['comment']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-comment)
      - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['name']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-name)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['method']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-method)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['auto']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-auto)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['comment']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-comment)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['iface_properties']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-iface_properties)
    - [`pve_proxmox_net_ifaces_workload_shared['options_after']`](#variable-pve_proxmox_net_ifaces_workload_shared-sub-options_after)
  - [`pve_proxmox_net_ifaces_workload_specific`](#variable-pve_proxmox_net_ifaces_workload_specific)
    - [`pve_proxmox_net_ifaces_workload_specific['options_before']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-options_before)
    - [`pve_proxmox_net_ifaces_workload_specific['sections']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections)
      - [`pve_proxmox_net_ifaces_workload_specific['sections']['title']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-title)
      - [`pve_proxmox_net_ifaces_workload_specific['sections']['comment']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-comment)
      - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['name']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-name)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['method']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-method)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['auto']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-auto)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['comment']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-comment)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['iface_properties']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-iface_properties)
    - [`pve_proxmox_net_ifaces_workload_specific['options_after']`](#variable-pve_proxmox_net_ifaces_workload_specific-sub-options_after)
  - [`pve_proxmox_fw_cluster_options`](#variable-pve_proxmox_fw_cluster_options)
  - [`pve_proxmox_fw_cluster_aliases`](#variable-pve_proxmox_fw_cluster_aliases)
    - [`pve_proxmox_fw_cluster_aliases['name']`](#variable-pve_proxmox_fw_cluster_aliases-sub-name)
    - [`pve_proxmox_fw_cluster_aliases['ip']`](#variable-pve_proxmox_fw_cluster_aliases-sub-ip)
    - [`pve_proxmox_fw_cluster_aliases['comment']`](#variable-pve_proxmox_fw_cluster_aliases-sub-comment)
  - [`pve_proxmox_fw_cluster_ipsets`](#variable-pve_proxmox_fw_cluster_ipsets)
    - [`pve_proxmox_fw_cluster_ipsets['name']`](#variable-pve_proxmox_fw_cluster_ipsets-sub-name)
    - [`pve_proxmox_fw_cluster_ipsets['comment']`](#variable-pve_proxmox_fw_cluster_ipsets-sub-comment)
    - [`pve_proxmox_fw_cluster_ipsets['entries']`](#variable-pve_proxmox_fw_cluster_ipsets-sub-entries)
      - [`pve_proxmox_fw_cluster_ipsets['entries']['ip']`](#variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-ip)
      - [`pve_proxmox_fw_cluster_ipsets['entries']['comment']`](#variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-comment)
      - [`pve_proxmox_fw_cluster_ipsets['entries']['nomatch']`](#variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-nomatch)
  - [`pve_proxmox_fw_cluster_securitygroups`](#variable-pve_proxmox_fw_cluster_securitygroups)
    - [`pve_proxmox_fw_cluster_securitygroups['name']`](#variable-pve_proxmox_fw_cluster_securitygroups-sub-name)
    - [`pve_proxmox_fw_cluster_securitygroups['comment']`](#variable-pve_proxmox_fw_cluster_securitygroups-sub-comment)
    - [`pve_proxmox_fw_cluster_securitygroups['rules']`](#variable-pve_proxmox_fw_cluster_securitygroups-sub-rules)
  - [`pve_proxmox_fw_cluster_rules`](#variable-pve_proxmox_fw_cluster_rules)
    - [`pve_proxmox_fw_cluster_rules['direction']`](#variable-pve_proxmox_fw_cluster_rules-sub-direction)
    - [`pve_proxmox_fw_cluster_rules['action']`](#variable-pve_proxmox_fw_cluster_rules-sub-action)
    - [`pve_proxmox_fw_cluster_rules['security_group']`](#variable-pve_proxmox_fw_cluster_rules-sub-security_group)
    - [`pve_proxmox_fw_cluster_rules['proto']`](#variable-pve_proxmox_fw_cluster_rules-sub-proto)
    - [`pve_proxmox_fw_cluster_rules['iface']`](#variable-pve_proxmox_fw_cluster_rules-sub-iface)
    - [`pve_proxmox_fw_cluster_rules['source']`](#variable-pve_proxmox_fw_cluster_rules-sub-source)
    - [`pve_proxmox_fw_cluster_rules['sport']`](#variable-pve_proxmox_fw_cluster_rules-sub-sport)
    - [`pve_proxmox_fw_cluster_rules['dest']`](#variable-pve_proxmox_fw_cluster_rules-sub-dest)
    - [`pve_proxmox_fw_cluster_rules['dport']`](#variable-pve_proxmox_fw_cluster_rules-sub-dport)
    - [`pve_proxmox_fw_cluster_rules['log']`](#variable-pve_proxmox_fw_cluster_rules-sub-log)
    - [`pve_proxmox_fw_cluster_rules['comment']`](#variable-pve_proxmox_fw_cluster_rules-sub-comment)
  - [`pve_proxmox_fw_node_options`](#variable-pve_proxmox_fw_node_options)
  - [`pve_proxmox_fw_node_rules`](#variable-pve_proxmox_fw_node_rules)
    - [`pve_proxmox_fw_node_rules['direction']`](#variable-pve_proxmox_fw_node_rules-sub-direction)
    - [`pve_proxmox_fw_node_rules['action']`](#variable-pve_proxmox_fw_node_rules-sub-action)
    - [`pve_proxmox_fw_node_rules['security_group']`](#variable-pve_proxmox_fw_node_rules-sub-security_group)
    - [`pve_proxmox_fw_node_rules['proto']`](#variable-pve_proxmox_fw_node_rules-sub-proto)
    - [`pve_proxmox_fw_node_rules['iface']`](#variable-pve_proxmox_fw_node_rules-sub-iface)
    - [`pve_proxmox_fw_node_rules['source']`](#variable-pve_proxmox_fw_node_rules-sub-source)
    - [`pve_proxmox_fw_node_rules['sport']`](#variable-pve_proxmox_fw_node_rules-sub-sport)
    - [`pve_proxmox_fw_node_rules['dest']`](#variable-pve_proxmox_fw_node_rules-sub-dest)
    - [`pve_proxmox_fw_node_rules['dport']`](#variable-pve_proxmox_fw_node_rules-sub-dport)
    - [`pve_proxmox_fw_node_rules['log']`](#variable-pve_proxmox_fw_node_rules-sub-log)
    - [`pve_proxmox_fw_node_rules['comment']`](#variable-pve_proxmox_fw_node_rules-sub-comment)
  - [`pve_proxmox_datacentercfg`](#variable-pve_proxmox_datacentercfg)
  - [`pve_proxmox_storage`](#variable-pve_proxmox_storage)
    - [`pve_proxmox_storage['name']`](#variable-pve_proxmox_storage-sub-name)
    - [`pve_proxmox_storage['type']`](#variable-pve_proxmox_storage-sub-type)
    - [`pve_proxmox_storage['attributes']`](#variable-pve_proxmox_storage-sub-attributes)
      - [`pve_proxmox_storage['attributes']['mountpoint']`](#variable-pve_proxmox_storage-sub-attributes-sub-mountpoint)
      - [`pve_proxmox_storage['attributes']['vdevs']`](#variable-pve_proxmox_storage-sub-attributes-sub-vdevs)
        - [`pve_proxmox_storage['attributes']['vdevs']['type']`](#variable-pve_proxmox_storage-sub-attributes-sub-vdevs-sub-type)
        - [`pve_proxmox_storage['attributes']['vdevs']['disks']`](#variable-pve_proxmox_storage-sub-attributes-sub-vdevs-sub-disks)
      - [`pve_proxmox_storage['attributes']['pool_properties']`](#variable-pve_proxmox_storage-sub-attributes-sub-pool_properties)
      - [`pve_proxmox_storage['attributes']['filesystem_properties']`](#variable-pve_proxmox_storage-sub-attributes-sub-filesystem_properties)
      - [`pve_proxmox_storage['attributes']['zfs_properties']`](#variable-pve_proxmox_storage-sub-attributes-sub-zfs_properties)
      - [`pve_proxmox_storage['attributes']['storage_properties']`](#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties)
        - [`pve_proxmox_storage['attributes']['storage_properties']['src']`](#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-src)
        - [`pve_proxmox_storage['attributes']['storage_properties']['path']`](#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-path)
        - [`pve_proxmox_storage['attributes']['storage_properties']['opts']`](#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-opts)
        - [`pve_proxmox_storage['attributes']['storage_properties']['state']`](#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-state)
  - [`pve_proxmox_storage_force_cleanup`](#variable-pve_proxmox_storage_force_cleanup)
  - [`pve_proxmox_sm`](#variable-pve_proxmox_sm)
    - [`pve_proxmox_sm['name']`](#variable-pve_proxmox_sm-sub-name)
    - [`pve_proxmox_sm['type']`](#variable-pve_proxmox_sm-sub-type)
    - [`pve_proxmox_sm['storage_properties']`](#variable-pve_proxmox_sm-sub-storage_properties)
      - [`pve_proxmox_sm['storage_properties']['content']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-content)
      - [`pve_proxmox_sm['storage_properties']['nodes']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-nodes)
      - [`pve_proxmox_sm['storage_properties']['is_mountpoint']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-is_mountpoint)
      - [`pve_proxmox_sm['storage_properties']['path']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-path)
      - [`pve_proxmox_sm['storage_properties']['pool']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-pool)
      - [`pve_proxmox_sm['storage_properties']['sparse']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-sparse)
      - [`pve_proxmox_sm['storage_properties']['blocksize']`](#variable-pve_proxmox_sm-sub-storage_properties-sub-blocksize)
<!-- ANSIBLE DOCSMITH TOC END -->
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



<!-- ANSIBLE DOCSMITH MAIN START -->

## Role variables<a id="variables"></a>

The following variables can be configured for this role:

| Variable | Type | Required | Default | Description (abstract) |
|----------|------|----------|---------|------------------------|
| `pve_proxmox_tmpbackupfiles` | `bool` | No | `true` | Switch to control whether temporary disaster-safeguard backups of important configuration files should be created before re-writing them via Ansible.<br><br>When set to `true` (which is the default), the role will:<br><br>1. Create a temporary […](#variable-pve_proxmox_tmpbackupfiles) |
| `pve_proxmox_iommu_manage` | `bool` | No | `true` | Switch to control if the role should manage input–output memory management unit (IOMMU) related operating system configuration. IOMMU support is needed for PCI and/or GPU passthrough.<br><br>When set to `true` (which is the default), the role […](#variable-pve_proxmox_iommu_manage) |
| `pve_proxmox_net_altnames` | `list` | No | `[]` | List of network interface alternative name definitions for systemd link files (`/etc/systemd/network/10-*.link`).<br><br>Instead of renaming kernel network devices, this approach assigns alternative names (altnames). This preserves the original […](#variable-pve_proxmox_net_altnames) |
| `pve_proxmox_net_ifaces_host_shared` | `dict` | No | `{}` | Network interface definitions for `/etc/network/interfaces.d/10-host` shared across all hosts in the inventory group.<br><br>These interfaces are NOT visible in the PVE web UI and are intended for backend networking configurations. Use this variable […](#variable-pve_proxmox_net_ifaces_host_shared) |
| `pve_proxmox_net_ifaces_host_specific` | `dict` | No | `{}` | Network interface definitions for `/etc/network/interfaces.d/10-host` specific to individual hosts.<br><br>These interfaces are NOT visible in the PVE web UI and are intended for backend networking configurations. Use this variable for host-specific […](#variable-pve_proxmox_net_ifaces_host_specific) |
| `pve_proxmox_net_ifaces_workload_shared` | `dict` | No | `{}` | Network interface definitions for `/etc/network/interfaces` shared across all hosts in the inventory group.<br><br>These interfaces ARE visible in the PVE web UI and available for assignment to virtual machines and containers. Use this variable for […](#variable-pve_proxmox_net_ifaces_workload_shared) |
| `pve_proxmox_net_ifaces_workload_specific` | `dict` | No | `{}` | Network interface definitions for `/etc/network/interfaces` specific to individual hosts.<br><br>These interfaces ARE visible in the PVE web UI and available for assignment to virtual machines and containers. Use this variable for host-specific […](#variable-pve_proxmox_net_ifaces_workload_specific) |
| `pve_proxmox_fw_cluster_options` | `dict` | No | `{}` | Cluster-wide (datacenter) firewall options applied to all PVE hosts.<br><br>This is a passthrough of original Proxmox VE firewall options. Keys and values are rendered directly into the `[OPTIONS]` section of […](#variable-pve_proxmox_fw_cluster_options) |
| `pve_proxmox_fw_cluster_aliases` | `list` | No | `[]` | Cluster-wide IP aliases for use in firewall rules.<br><br>Aliases provide speakable, stable names for IP addresses and networks. Once defined, aliases can be referenced in rules, IP sets, and other aliases using the `dc/` syntax.<br><br>Each alias […](#variable-pve_proxmox_fw_cluster_aliases) |
| `pve_proxmox_fw_cluster_ipsets` | `list` | No | `[]` | Cluster-wide IP sets for use in firewall rules.<br><br>IP sets are reusable collections of IP addresses, networks, and aliases. They simplify rule management by allowing a single rule to match multiple addresses.<br><br>Each IP set generates an […](#variable-pve_proxmox_fw_cluster_ipsets) |
| `pve_proxmox_fw_cluster_securitygroups` | `list` | No | `[]` | Cluster-wide security groups (reusable rule collections).<br><br>Security groups bundle multiple firewall rules under a single name, allowing them to be applied as a unit to hosts, VMs, or containers. This promotes rule reuse and simplifies […](#variable-pve_proxmox_fw_cluster_securitygroups) |
| `pve_proxmox_fw_cluster_rules` | `list` | No | `[]` | Cluster-wide firewall rules applied to all PVE hosts.<br><br>Rules define traffic filtering policies. Each rule generates a line in the `[RULES]` section of `/etc/pve/firewall/cluster.fw`.<br><br>Rules can reference aliases (`dc/`), IP sets (`+dc/`), […](#variable-pve_proxmox_fw_cluster_rules) |
| `pve_proxmox_fw_node_options` | `dict` | No | `{}` | Node-specific firewall options for this PVE host.<br><br>This is a passthrough of original Proxmox VE firewall options. Keys and values are rendered directly into the `[OPTIONS]` section of `/etc/pve/nodes//host.fw`.<br><br>These options only affect […](#variable-pve_proxmox_fw_node_options) |
| `pve_proxmox_fw_node_rules` | `list` | No | `[]` | Node-specific firewall rules for this PVE host.<br><br>Rules defined here only apply to this specific node, not the entire cluster. Each rule generates a line in the `[RULES]` section of `/etc/pve/nodes//host.fw`.<br><br>The data structure is […](#variable-pve_proxmox_fw_node_rules) |
| `pve_proxmox_datacentercfg` | `dict` | No | `{}` | Proxmox VE datacenter-wide configuration settings.<br><br>This variable defines cluster-wide defaults rendered to `/etc/pve/datacenter.cfg`. Since this file resides on pmxcfs (the FUSE-backed cluster filesystem synchronized via Corosync), settings […](#variable-pve_proxmox_datacentercfg) |
| `pve_proxmox_storage` | `list` | No | `[]` | List of storage definitions for the PVE host.<br><br>This variable manages operating system-level storage configuration including ZFS pools, ZFS datasets, and NFS mounts. Each entry defines a storage resource with its type-specific […](#variable-pve_proxmox_storage) |
| `pve_proxmox_storage_force_cleanup` | `bool` | No | `false` | Allow automatic cleanup of existing data on disks for ZFS pool creation.<br><br>DESTRUCTIVE OPERATION WARNING: When set to `true`, the role will automatically wipe filesystem signatures and ZFS labels from disks that have existing data but whose […](#variable-pve_proxmox_storage_force_cleanup) |
| `pve_proxmox_sm` | `list` | No | `[]` | Proxmox VE Storage Manager (pvesm) configuration.<br><br>This variable defines storage resources visible in the PVE web UI and available for VM/container disk allocation, backups, ISO storage, and container templates.<br><br>These entries configure […](#variable-pve_proxmox_sm) |

### `pve_proxmox_tmpbackupfiles`<a id="variable-pve_proxmox_tmpbackupfiles"></a>

[*⇑ Back to ToC ⇑*](#toc)

Switch to control whether temporary disaster-safeguard backups of
important configuration files should be created before re-writing them
via Ansible.

When set to `true` (which is the default), the role will:

1. Create a temporary directory with the `ansible_pve_backup_` prefix.
2. Copy important configuration files there before editing them.

This is only a disaster safeguard. If the automatic configuration
causes an error, you can log in to the machine and restore the
original configuration files from that backup. The role outputs where
the backups are copied to.

There is no role-based cleanup of these backup files, but the
temporary directory is usually cleaned up by the operating system
during boot. The backup files are typically just a few kilobytes in
size, so keeping them around until the next reboot should not be an
issue.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`



### `pve_proxmox_iommu_manage`<a id="variable-pve_proxmox_iommu_manage"></a>

[*⇑ Back to ToC ⇑*](#toc)

Switch to control if the role should manage input–output memory
management unit (IOMMU) related operating system configuration.
IOMMU support is needed for PCI and/or GPU passthrough.

When set to `true` (which is the default), the role will:

1. Check for CPU vendor based IOMMU support.
2. Add or remove needed GRUB parameters based on CPU vendor and IOMMU
   support.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`



### `pve_proxmox_net_altnames`<a id="variable-pve_proxmox_net_altnames"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of network interface alternative name definitions for systemd
link files (`/etc/systemd/network/10-*.link`).

Instead of renaming kernel network devices, this approach assigns
alternative names (altnames). This preserves the original device name
assigned by the kernel and avoids potential kernel/udev conflicts
during boot or device hotplug.

Each entry generates a separate `.link` file named after the first
altname (e.g., `10-main1.link`). The systemd-networkd service uses
these files to match interfaces by MAC address and type, then applies
the specified alternative names.

Use `ip -br link show` to display current interface names and their
altnames after configuration.

References:
  - https://www.freedesktop.org/software/systemd/man/latest/systemd.link.html
  - https://manpages.debian.org/trixie/udev/systemd.link.5.en.html
  - https://pve.proxmox.com/wiki/Network_Configuration#_manual_method

Example:

```yaml
pve_proxmox_net_altnames:
  - type: "en"
    desc: "enp134s0f0np0 (dual-port NIC, upper port)"
    mac_address: "aa:bb:11:44:77:38"
    altnames:
      - "main1"

  - type: "en"
    desc: "enp134s0f1np1 (dual-port NIC, lower port)"
    mac_address: "aa:bb:22:55:88:39"
    altnames:
      - "main2"

  - type: "en"
    desc: "eno3np0 (quad-port NIC, first port)"
    mac_address: "aa:bb:33:66:99:b1"
    altnames:
      - "admfb"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_net_altnames['type']`<a id="variable-pve_proxmox_net_altnames-sub-type"></a>

[*⇑ Back to ToC ⇑*](#toc)

Interface type identifier used for matching in the `[Match]`
section of the generated systemd link file.

This value is mapped to the corresponding systemd `Type=` value:

- `en`: Ethernet (`ether`)
- `lo`: Loopback (`loopback`)
- `wl`: Wireless LAN (`wlan`)
- `ww`: Wireless WAN (`wwan`)
- `ib`: InfiniBand (`infiniband`)

The type ensures the link file only matches interfaces of the
correct hardware type, preventing accidental mismatches when
MAC addresses are reused or spoofed.

- **Type**: `str`
- **Required**: Yes
- **Choices**: `en`, `lo`, `wl`, `ww`, `ib`

#### `pve_proxmox_net_altnames['mac_address']`<a id="variable-pve_proxmox_net_altnames-sub-mac_address"></a>

[*⇑ Back to ToC ⇑*](#toc)

MAC address of the network interface in colon-separated format.

Used in the `[Match]` section to uniquely identify the physical
interface. The MAC address must match exactly for the link file
to apply.

Format: `XX:XX:XX:XX:XX:XX` (case-insensitive)

Example: `3c:fd:fe:de:97:38`

Use `ip link show` or `cat /sys/class/net/*/address` to find
the MAC addresses of installed interfaces.

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_net_altnames['desc']`<a id="variable-pve_proxmox_net_altnames-sub-desc"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional human-readable description of the interface.

Rendered as the `Description=` directive in the `[Link]` section.
Use this to document the physical location, purpose, or original
kernel name of the interface for easier identification.

Example: `enp134s0f0np0 (dual-port NIC, upper port farther from
the mainboard)`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_net_altnames['altnames']`<a id="variable-pve_proxmox_net_altnames-sub-altnames"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of alternative names to assign to the interface.

Each name is rendered as a separate `AlternativeName=` directive
in the `[Link]` section. The first entry is also used as the
filename for the generated link file (e.g., `10-main1.link`).

Alternative names allow referencing the interface by a
human-friendly, predictable name while preserving the original
kernel-assigned name. Multiple altnames can be specified if the
interface should be reachable under different names.

Naming conventions:
  - `main1`, `main2`: Primary workload interfaces (bond members)
  - `admfb`: Admin fallback interface (emergency access)
  - `sync1`, `sync2`: Corosync cluster communication links

The altnames defined here should match the interface names used
in `network_interfaces_host_specific` and related variables.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `str`



### `pve_proxmox_net_ifaces_host_shared`<a id="variable-pve_proxmox_net_ifaces_host_shared"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network interface definitions for `/etc/network/interfaces.d/10-host`
shared across all hosts in the inventory group.

These interfaces are NOT visible in the PVE web UI and are intended
for backend networking configurations. Use this variable for VLAN
devices, bond members, or configurations that should remain hidden
from VMs and administrators.

Typically defined in `group_vars/` and merged with
`pve_proxmox_net_ifaces_host_specific` during template rendering. The
shared definitions are processed after host-specific ones.

See `pve_proxmox_net_ifaces_host_specific` for the data structure
documentation.

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`

#### `pve_proxmox_net_ifaces_host_shared['options_before']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-options_before"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed before all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_net_ifaces_host_shared['sections']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of logical sections grouping related interfaces.

Each section generates a highlighted comment header (using the
`title` value) for improved human readability when inspecting the
generated configuration file.

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`

##### `pve_proxmox_net_ifaces_host_shared['sections']['title']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-title"></a>

[*⇑ Back to ToC ⇑*](#toc)

Section title rendered as a highlighted comment header above
the interface definitions.

Example output: `### Proxmox VE (PVE) VLAN interfaces`

- **Type**: `str`
- **Required**: Yes

##### `pve_proxmox_net_ifaces_host_shared['sections']['comment']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional comment block rendered below the title and above the
interface definitions.

Each line is automatically prefixed with `# ` in the output.
Use this for explanatory text about the section's purpose.

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_net_ifaces_host_shared['sections']['interfaces']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of network interface definitions within this section.

Each interface generates an `auto` directive (if enabled) and
an `iface` stanza with the specified method and properties.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`

###### `pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['name']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Interface name as recognized by the kernel.

Examples: `bond_main.0001`, `br0020`, `main1`

- **Type**: `str`
- **Required**: Yes

###### `pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['method']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-method"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address assignment method for the interface as defined in
interfaces(5).

Common values:

- `manual`: No automatic IP configuration. Used for bridge
  members, bond slaves, or interfaces managed elsewhere.
- `static`: Fixed IP address specified via `iface_properties`.
- `dhcp`: Obtain address via DHCP client.
- `loopback`: Loopback interface (typically only for `lo`).

- **Type**: `str`
- **Required**: Yes
- **Choices**: `manual`, `static`, `dhcp`, `loopback`

###### `pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['auto']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-auto"></a>

[*⇑ Back to ToC ⇑*](#toc)

Whether to automatically bring up the interface at boot.

When `true`, renders an `auto <name>` directive before the
`iface` stanza.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`

###### `pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['comment']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional multi-line comment rendered above the interface
definition (before the `auto` directive).

Use this for lengthy explanations about the interface's
purpose or configuration rationale. Each line is prefixed
with `# `.

For short inline comments within the `iface` block, use
`iface_properties.comment` instead.

- **Type**: `str`
- **Required**: No

###### `pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['iface_properties']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-iface_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

Key-value pairs for interfaces(5) options rendered within
the `iface` stanza.

All keys are rendered as `    <key> <value>` lines with
proper indentation, except for the special `comment` key
which renders as `    # <value>`.

Common properties by interface type:

Static addressing:
  - `address`: IP address with CIDR notation (e.g., `10.0.0.1/24`)
  - `gateway`: Default gateway IP address

Bonding:
  - `bond-slaves`: Space-separated list of member interfaces
  - `bond-mode`: Bonding mode (e.g., `802.3ad` for LACP)
  - `bond-miimon`: Link monitoring interval in milliseconds
  - `bond-lacp-rate`: LACP rate (`slow` or `fast`)
  - `bond-xmit-hash-policy`: Transmit hash policy

Bridging:
  - `bridge-ports`: Space-separated list of member interfaces
  - `bridge-stp`: Spanning tree protocol (`on` or `off`)
  - `bridge-fd`: Forwarding delay in seconds

General:
  - `mtu`: Maximum transmission unit size
  - `comment`: Inline comment within the interface block

- **Type**: `dict`
- **Required**: No



#### `pve_proxmox_net_ifaces_host_shared['options_after']`<a id="variable-pve_proxmox_net_ifaces_host_shared-sub-options_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed after all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_net_ifaces_host_specific`<a id="variable-pve_proxmox_net_ifaces_host_specific"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network interface definitions for `/etc/network/interfaces.d/10-host`
specific to individual hosts.

These interfaces are NOT visible in the PVE web UI and are intended
for backend networking configurations. Use this variable for
host-specific physical interfaces, bonds, management bridges, or VLAN
subinterfaces that should remain hidden from VMs.

Typically defined in `host_vars/` and merged with
`pve_proxmox_net_ifaces_host_shared` during template rendering. The
host-specific definitions are processed before shared ones.

Data structure (identical for all `pve_proxmox_net_ifaces_*` variables):

```yaml
pve_proxmox_net_ifaces_host_specific:
  options_before: |
    # Optional header lines using interfaces(5) syntax
    source /etc/network/interfaces.d/*

  sections:
    - title: "Section title for human readability"
      comment: |
        Optional multi-line comment explaining this section.
        Rendered with '# ' prefix on each line.

      interfaces:
        - name: "bond_main"
          method: "manual"
          auto: true
          comment: |
            Optional multi-line comment above the interface.
          iface_properties:
            bond-slaves: "eth0 eth1"
            bond-mode: "802.3ad"
            mtu: 1500
            comment: "Inline comment within iface block"

        - name: "bond_main.0020"
          method: "static"
          auto: true
          iface_properties:
            address: "10.0.20.1/24"
            gateway: "10.0.20.254"
            comment: "0020_management"

  options_after: |
    # Optional footer lines using interfaces(5) syntax
```

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`

#### `pve_proxmox_net_ifaces_host_specific['options_before']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-options_before"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed before all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_net_ifaces_host_specific['sections']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of logical sections grouping related interfaces.

Each section generates a highlighted comment header (using the
`title` value) for improved human readability when inspecting the
generated configuration file.

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`

##### `pve_proxmox_net_ifaces_host_specific['sections']['title']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-title"></a>

[*⇑ Back to ToC ⇑*](#toc)

Section title rendered as a highlighted comment header above
the interface definitions.

Example output: `### Proxmox VE (PVE) main connection (LACP, trunk)`

- **Type**: `str`
- **Required**: Yes

##### `pve_proxmox_net_ifaces_host_specific['sections']['comment']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional comment block rendered below the title and above the
interface definitions.

Each line is automatically prefixed with `# ` in the output.
Use this for explanatory text about the section's purpose.

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_net_ifaces_host_specific['sections']['interfaces']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of network interface definitions within this section.

Each interface generates an `auto` directive (if enabled) and
an `iface` stanza with the specified method and properties.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`

###### `pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['name']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Interface name as recognized by the kernel.

Examples: `main1`, `main2`, `bond_main`, `bond_main.0020`,
`br0020`, `admfb`

- **Type**: `str`
- **Required**: Yes

###### `pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['method']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-method"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address assignment method for the interface as defined in
interfaces(5).

Common values:

- `manual`: No automatic IP configuration. Used for bridge
  members, bond slaves, or interfaces managed elsewhere.
- `static`: Fixed IP address specified via `iface_properties`.
- `dhcp`: Obtain address via DHCP client.
- `loopback`: Loopback interface (typically only for `lo`).

- **Type**: `str`
- **Required**: Yes
- **Choices**: `manual`, `static`, `dhcp`, `loopback`

###### `pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['auto']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-auto"></a>

[*⇑ Back to ToC ⇑*](#toc)

Whether to automatically bring up the interface at boot.

When `true`, renders an `auto <name>` directive before the
`iface` stanza.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`

###### `pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['comment']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional multi-line comment rendered above the interface
definition (before the `auto` directive).

Use this for lengthy explanations about the interface's
purpose or configuration rationale. Each line is prefixed
with `# `.

For short inline comments within the `iface` block, use
`iface_properties.comment` instead.

- **Type**: `str`
- **Required**: No

###### `pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['iface_properties']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-iface_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

Key-value pairs for interfaces(5) options rendered within
the `iface` stanza.

All keys are rendered as `    <key> <value>` lines with
proper indentation, except for the special `comment` key
which renders as `    # <value>`.

See `pve_proxmox_net_ifaces_host_shared` for common properties.

- **Type**: `dict`
- **Required**: No



#### `pve_proxmox_net_ifaces_host_specific['options_after']`<a id="variable-pve_proxmox_net_ifaces_host_specific-sub-options_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed after all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_net_ifaces_workload_shared`<a id="variable-pve_proxmox_net_ifaces_workload_shared"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network interface definitions for `/etc/network/interfaces` shared
across all hosts in the inventory group.

These interfaces ARE visible in the PVE web UI and available for
assignment to virtual machines and containers. Use this variable for
workload bridge interfaces (typically named `vmbr<VLAN_ID>`) that VMs
and containers attach to.

Typically defined in `group_vars/` and merged with
`pve_proxmox_net_ifaces_workload_specific` during template rendering. The
shared definitions are processed after host-specific ones.

The `options_before` value typically includes
`source /etc/network/interfaces.d/*` to include host-specific
configurations.

See `pve_proxmox_net_ifaces_host_specific` for the data structure
documentation.

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`

#### `pve_proxmox_net_ifaces_workload_shared['options_before']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-options_before"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed before all sections in the generated file.
Uses interfaces(5) syntax.

For workload interfaces, this typically includes:
```
source /etc/network/interfaces.d/*
```

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_net_ifaces_workload_shared['sections']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of logical sections grouping related interfaces.

Each section generates a highlighted comment header (using the
`title` value) for improved human readability when inspecting the
generated configuration file.

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`

##### `pve_proxmox_net_ifaces_workload_shared['sections']['title']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-title"></a>

[*⇑ Back to ToC ⇑*](#toc)

Section title rendered as a highlighted comment header above
the interface definitions.

Example output: `### Proxmox VE (PVE) workload bridge interfaces`

- **Type**: `str`
- **Required**: Yes

##### `pve_proxmox_net_ifaces_workload_shared['sections']['comment']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional comment block rendered below the title and above the
interface definitions.

Each line is automatically prefixed with `# ` in the output.
Use this for explanatory text about the section's purpose.

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of network interface definitions within this section.

Each interface generates an `auto` directive (if enabled) and
an `iface` stanza with the specified method and properties.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`

###### `pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['name']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Interface name as recognized by the kernel.

PVE convention uses `vmbr<VLAN_ID>` for workload bridges.

Examples: `vmbr0001`, `vmbr0020`, `vmbr0254`

- **Type**: `str`
- **Required**: Yes

###### `pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['method']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-method"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address assignment method for the interface as defined in
interfaces(5).

Common values:

- `manual`: No automatic IP configuration. Used for bridge
  members, bond slaves, or interfaces managed elsewhere.
- `static`: Fixed IP address specified via `iface_properties`.
- `dhcp`: Obtain address via DHCP client.
- `loopback`: Loopback interface (typically only for `lo`).

- **Type**: `str`
- **Required**: Yes
- **Choices**: `manual`, `static`, `dhcp`, `loopback`

###### `pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['auto']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-auto"></a>

[*⇑ Back to ToC ⇑*](#toc)

Whether to automatically bring up the interface at boot.

When `true`, renders an `auto <name>` directive before the
`iface` stanza.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`

###### `pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['comment']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional multi-line comment rendered above the interface
definition (before the `auto` directive).

Use this for lengthy explanations about the interface's
purpose or configuration rationale. Each line is prefixed
with `# `.

For short inline comments within the `iface` block, use
`iface_properties.comment` instead.

- **Type**: `str`
- **Required**: No

###### `pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['iface_properties']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-iface_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

Key-value pairs for interfaces(5) options rendered within
the `iface` stanza.

All keys are rendered as `    <key> <value>` lines with
proper indentation, except for the special `comment` key
which renders as `    # <value>`.

Common properties for workload bridges:

- `bridge-ports`: Member interface (e.g., `bond_main.0001`)
- `bridge-stp`: Spanning tree protocol (`on` or `off`)
- `bridge-fd`: Forwarding delay (typically `0`)
- `comment`: VLAN name or description

See `pve_proxmox_net_ifaces_host_shared` for additional common
properties.

- **Type**: `dict`
- **Required**: No



#### `pve_proxmox_net_ifaces_workload_shared['options_after']`<a id="variable-pve_proxmox_net_ifaces_workload_shared-sub-options_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed after all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_net_ifaces_workload_specific`<a id="variable-pve_proxmox_net_ifaces_workload_specific"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network interface definitions for `/etc/network/interfaces` specific
to individual hosts.

These interfaces ARE visible in the PVE web UI and available for
assignment to virtual machines and containers. Use this variable for
host-specific workload interfaces such as Corosync cluster links,
special-purpose bridges, or interfaces unique to a particular node.

Typically defined in `host_vars/` and merged with
`pve_proxmox_net_ifaces_workload_shared` during template rendering. The
host-specific definitions are processed before shared ones.

See `pve_proxmox_net_ifaces_host_specific` for the data structure
documentation.

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`

#### `pve_proxmox_net_ifaces_workload_specific['options_before']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-options_before"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed before all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_net_ifaces_workload_specific['sections']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of logical sections grouping related interfaces.

Each section generates a highlighted comment header (using the
`title` value) for improved human readability when inspecting the
generated configuration file.

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`

##### `pve_proxmox_net_ifaces_workload_specific['sections']['title']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-title"></a>

[*⇑ Back to ToC ⇑*](#toc)

Section title rendered as a highlighted comment header above
the interface definitions.

Example output: `### Corosync links`

- **Type**: `str`
- **Required**: Yes

##### `pve_proxmox_net_ifaces_workload_specific['sections']['comment']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional comment block rendered below the title and above the
interface definitions.

Each line is automatically prefixed with `# ` in the output.
Use this for explanatory text about the section's purpose.

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of network interface definitions within this section.

Each interface generates an `auto` directive (if enabled) and
an `iface` stanza with the specified method and properties.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`

###### `pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['name']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Interface name as recognized by the kernel.

Examples: `sync1`, `sync2` (for Corosync links)

- **Type**: `str`
- **Required**: Yes

###### `pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['method']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-method"></a>

[*⇑ Back to ToC ⇑*](#toc)

Address assignment method for the interface as defined in
interfaces(5).

Common values:

- `manual`: No automatic IP configuration. Used for bridge
  members, bond slaves, or interfaces managed elsewhere.
- `static`: Fixed IP address specified via `iface_properties`.
- `dhcp`: Obtain address via DHCP client.
- `loopback`: Loopback interface (typically only for `lo`).

- **Type**: `str`
- **Required**: Yes
- **Choices**: `manual`, `static`, `dhcp`, `loopback`

###### `pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['auto']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-auto"></a>

[*⇑ Back to ToC ⇑*](#toc)

Whether to automatically bring up the interface at boot.

When `true`, renders an `auto <name>` directive before the
`iface` stanza.

- **Type**: `bool`
- **Required**: No
- **Default**: `true`

###### `pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['comment']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional multi-line comment rendered above the interface
definition (before the `auto` directive).

Use this for lengthy explanations about the interface's
purpose or configuration rationale. Each line is prefixed
with `# `.

For short inline comments within the `iface` block, use
`iface_properties.comment` instead.

- **Type**: `str`
- **Required**: No

###### `pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['iface_properties']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-iface_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

Key-value pairs for interfaces(5) options rendered within
the `iface` stanza.

All keys are rendered as `    <key> <value>` lines with
proper indentation, except for the special `comment` key
which renders as `    # <value>`.

See `pve_proxmox_net_ifaces_host_shared` for common properties.

- **Type**: `dict`
- **Required**: No



#### `pve_proxmox_net_ifaces_workload_specific['options_after']`<a id="variable-pve_proxmox_net_ifaces_workload_specific-sub-options_after"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional lines placed after all sections in the generated file.
Uses interfaces(5) syntax.

Duplicate lines across merged datasets are automatically
deduplicated during rendering.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_fw_cluster_options`<a id="variable-pve_proxmox_fw_cluster_options"></a>

[*⇑ Back to ToC ⇑*](#toc)

Cluster-wide (datacenter) firewall options applied to all PVE hosts.

This is a passthrough of original Proxmox VE firewall options. Keys
and values are rendered directly into the `[OPTIONS]` section of
`/etc/pve/firewall/cluster.fw`.

Nested dictionaries are automatically converted to the PVE
`key=value,key2=value2` format (e.g., for `log_ratelimit`).

Common options:

- `enable`: Enable/disable the cluster firewall (`0` or `1`,
  default: `0`)
- `ebtables`: Enable ebtables rules cluster-wide (`0` or `1`,
  default: `1`)
- `policy_in`: Default policy for incoming traffic (`ACCEPT`,
  `DROP`, `REJECT`, default: `DROP`)
- `policy_out`: Default policy for outgoing traffic (`ACCEPT`,
  `DROP`, `REJECT`, default: `ACCEPT`)
- `policy_forward`: Default policy for forwarded traffic (`ACCEPT`,
  `DROP`, `REJECT`, default: `ACCEPT`, PVE 8.3+)
- `log_ratelimit`: Rate limiting for firewall log messages (dict with
  `enable`, `rate`, `burst` keys)

Reference:
  https://pve.proxmox.com/wiki/Firewall#pve_firewall_cluster_wide_setup

Example:
```yaml
pve_proxmox_fw_cluster_options:
  enable: 1
  ebtables: 1
  log_ratelimit:
    burst: 5
    enable: 1
    rate: "1/second"
  policy_in: "DROP"
  policy_out: "ACCEPT"
  policy_forward: "ACCEPT"
```

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`



### `pve_proxmox_fw_cluster_aliases`<a id="variable-pve_proxmox_fw_cluster_aliases"></a>

[*⇑ Back to ToC ⇑*](#toc)

Cluster-wide IP aliases for use in firewall rules.

Aliases provide speakable, stable names for IP addresses and networks.
Once defined, aliases can be referenced in rules, IP sets, and other
aliases using the `dc/<alias_name>` syntax.

Each alias generates a line in the `[ALIASES]` section of
`/etc/pve/firewall/cluster.fw`.

Reference:
  https://pve.proxmox.com/wiki/Firewall#pve_firewall_ip_aliases

Example:
```yaml
pve_proxmox_fw_cluster_aliases:
  - name: "gateway-main"
    ip: "10.1.1.254"
    comment: "Main gateway router"

  - name: "pve-node1"
    ip: "10.1.1.10"
    comment: "PVE node 1 management IP"

  - name: "admin-network"
    ip: "10.123.0.0/24"
    comment: "Admin VLAN"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_fw_cluster_aliases['name']`<a id="variable-pve_proxmox_fw_cluster_aliases-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Alias name used to reference this IP address or network.

Must start with a letter and contain only alphanumeric characters,
underscores, or hyphens (`^[A-Za-z][A-Za-z0-9_-]*$`).

Reference in rules and IP sets using `dc/<name>` prefix.

Example: `gateway-main` (referenced as `dc/gateway-main`)

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_fw_cluster_aliases['ip']`<a id="variable-pve_proxmox_fw_cluster_aliases-sub-ip"></a>

[*⇑ Back to ToC ⇑*](#toc)

IP address or network in IPv4 or IPv6 format.

Supports CIDR notation for networks (e.g., `10.0.0.0/24`).

Examples:
  - `10.1.1.2` (single host)
  - `10.1.2.0/24` (network)
  - `2001:db8::1` (IPv6 host)
  - `2001:db8::/32` (IPv6 network)

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_fw_cluster_aliases['comment']`<a id="variable-pve_proxmox_fw_cluster_aliases-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional human-readable description of the alias.

Rendered as a comment after the alias definition.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_fw_cluster_ipsets`<a id="variable-pve_proxmox_fw_cluster_ipsets"></a>

[*⇑ Back to ToC ⇑*](#toc)

Cluster-wide IP sets for use in firewall rules.

IP sets are reusable collections of IP addresses, networks, and
aliases. They simplify rule management by allowing a single rule to
match multiple addresses.

Each IP set generates an `[IPSET <name>]` section in
`/etc/pve/firewall/cluster.fw`.

Reference IP sets in rules using the `+dc/<ipset_name>` syntax
(note the `+` prefix).

Reference:
  https://pve.proxmox.com/wiki/Firewall#pve_firewall_ip_sets

Example:
```yaml
pve_proxmox_fw_cluster_ipsets:
  - name: "trusted_networks"
    comment: "Networks allowed to access management"
    entries:
      - ip: "10.1.20.0/24"
        comment: "Management VLAN"
      - ip: "10.1.2.0/24"
        comment: "Admin VLAN"

  - name: "pve_nodes"
    comment: "All PVE cluster nodes"
    entries:
      - ip: "dc/pve-node1"
        comment: "Node 1"
      - ip: "dc/pve-node2"
        comment: "Node 2"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_fw_cluster_ipsets['name']`<a id="variable-pve_proxmox_fw_cluster_ipsets-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

IP set name used to reference this collection.

Must start with a letter and contain only alphanumeric characters,
underscores, or hyphens (`^[A-Za-z][A-Za-z0-9_-]*$`).

Reference in rules using `+dc/<name>` prefix (note the `+`).

Example: `trusted_networks` (referenced as `+dc/trusted_networks`)

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_fw_cluster_ipsets['comment']`<a id="variable-pve_proxmox_fw_cluster_ipsets-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional human-readable description of the IP set.

Rendered as a comment after the `[IPSET <name>]` header.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_ipsets['entries']`<a id="variable-pve_proxmox_fw_cluster_ipsets-sub-entries"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of IP addresses, networks, or alias references in this set.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`

##### `pve_proxmox_fw_cluster_ipsets['entries']['ip']`<a id="variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-ip"></a>

[*⇑ Back to ToC ⇑*](#toc)

IP address, network (CIDR), or alias reference.

Supported formats:
  - IPv4 address: `10.1.20.110`
  - IPv4 network: `10.1.20.0/24`
  - IPv6 address: `2001:db8::1`
  - IPv6 network: `2001:db8::/32`
  - Cluster alias: `dc/<alias_name>`
  - Guest alias: `guest/<alias_name>`

- **Type**: `str`
- **Required**: Yes

##### `pve_proxmox_fw_cluster_ipsets['entries']['comment']`<a id="variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional human-readable description of this entry.

Rendered as a comment after the entry.

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_fw_cluster_ipsets['entries']['nomatch']`<a id="variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-nomatch"></a>

[*⇑ Back to ToC ⇑*](#toc)

Exclude this entry from the IP set (negation).

When `true`, the entry is prefixed with `!` in the output,
meaning traffic matching this entry will NOT match the IP set.
Useful for creating exceptions within a broader network range.

Example: Allow `10.0.0.0/24` except `10.0.0.1`:
```yaml
entries:
  - ip: "10.0.0.0/24"
  - ip: "10.0.0.1"
    nomatch: true
```

- **Type**: `bool`
- **Required**: No
- **Default**: `false`




### `pve_proxmox_fw_cluster_securitygroups`<a id="variable-pve_proxmox_fw_cluster_securitygroups"></a>

[*⇑ Back to ToC ⇑*](#toc)

Cluster-wide security groups (reusable rule collections).

Security groups bundle multiple firewall rules under a single name,
allowing them to be applied as a unit to hosts, VMs, or containers.
This promotes rule reuse and simplifies management.

Each security group generates a `[group <name>]` section in
`/etc/pve/firewall/cluster.fw`.

Reference security groups in the `[RULES]` section using:
`GROUP <group_name>`

Reference:
  https://pve.proxmox.com/wiki/Firewall#pve_firewall_security_groups

Example:
```yaml
pve_proxmox_fw_cluster_securitygroups:
  - name: "allow_web_out"
    comment: "Allow HTTP/HTTPS outbound"
    rules:
      - direction: "OUT"
        action: "ACCEPT"
        proto: "tcp"
        dport: "80,443"
        comment: "HTTP(S) outbound"

  - name: "allow_ssh_in"
    comment: "Allow SSH from trusted networks"
    rules:
      - direction: "IN"
        action: "SSH(ACCEPT)"
        source: "+dc/trusted_networks"
        comment: "SSH inbound"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_fw_cluster_securitygroups['name']`<a id="variable-pve_proxmox_fw_cluster_securitygroups-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Security group name.

Must start with a letter and contain only alphanumeric characters,
underscores, or hyphens (`^[A-Za-z][A-Za-z0-9_-]*$`).

Reference in rules using `GROUP <name>`.

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_fw_cluster_securitygroups['comment']`<a id="variable-pve_proxmox_fw_cluster_securitygroups-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Optional human-readable description of the security group.

Rendered as a comment after the `[group <name>]` header.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_securitygroups['rules']`<a id="variable-pve_proxmox_fw_cluster_securitygroups-sub-rules"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of firewall rules within this security group.

See `pve_proxmox_fw_cluster_rules` for the rule data structure.

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `dict`



### `pve_proxmox_fw_cluster_rules`<a id="variable-pve_proxmox_fw_cluster_rules"></a>

[*⇑ Back to ToC ⇑*](#toc)

Cluster-wide firewall rules applied to all PVE hosts.

Rules define traffic filtering policies. Each rule generates a line
in the `[RULES]` section of `/etc/pve/firewall/cluster.fw`.

Rules can reference aliases (`dc/<name>`), IP sets (`+dc/<name>`),
security groups (`GROUP <name>`), and PVE macros (`MACRO(ACTION)`).

Reference:
  https://pve.proxmox.com/wiki/Firewall#_firewall_rules

Example:
```yaml
pve_proxmox_fw_cluster_rules:
  # Apply a security group
  - action: "GROUP"
    security_group: "allow_pve_mgmt_in"

  # Direct rule with macro
  - direction: "IN"
    action: "SSH(ACCEPT)"
    source: "+dc/trusted_networks"
    comment: "SSH from trusted networks"

  # Direct rule with protocol and port
  - direction: "IN"
    action: "ACCEPT"
    proto: "tcp"
    dport: 8006
    source: "+dc/trusted_networks"
    comment: "PVE Web UI"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_fw_cluster_rules['direction']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-direction"></a>

[*⇑ Back to ToC ⇑*](#toc)

Traffic direction for the rule.

Required for all rules except `GROUP` actions.

- `IN`: Incoming traffic (towards the host/VM)
- `OUT`: Outgoing traffic (from the host/VM)

- **Type**: `str`
- **Required**: No
- **Choices**: `IN`, `OUT`

#### `pve_proxmox_fw_cluster_rules['action']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-action"></a>

[*⇑ Back to ToC ⇑*](#toc)

Action to take when the rule matches.

Supported values:

- `ACCEPT`: Allow the traffic
- `DROP`: Silently discard the traffic
- `REJECT`: Discard and send ICMP error response
- `MACRO(ACTION)`: Use a predefined PVE macro (e.g., `SSH(ACCEPT)`,
  `Ping(ACCEPT)`, `DNS(ACCEPT)`, `HTTP(ACCEPT)`, `HTTPS(ACCEPT)`)
- `GROUP`: Reference a security group (requires `security_group`)

PVE provides many predefined macros for common services. Macros
automatically set the appropriate protocol and port.

Reference:
  https://pve.proxmox.com/wiki/Firewall#_standard_macros

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_fw_cluster_rules['security_group']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-security_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Security group name to apply.

Required when `action` is `GROUP`. References a security group
defined in `pve_proxmox_fw_cluster_securitygroups`.

Example: `allow_pve_mgmt_in`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['proto']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-proto"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network protocol to match.

Not needed when using macros (they define their own protocol).

Common values: `tcp`, `udp`, `icmp`, `icmpv6`, `sctp`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['iface']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-iface"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network interface to match.

Limits the rule to traffic on a specific interface.

Example: `vmbr0`, `eth0`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['source']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-source"></a>

[*⇑ Back to ToC ⇑*](#toc)

Source address filter.

Supported formats:
  - IPv4/IPv6 address: `10.0.0.1`, `2001:db8::1`
  - Network (CIDR): `10.0.0.0/24`
  - Alias reference: `dc/<alias_name>`
  - IP set reference: `+dc/<ipset_name>` (note the `+` prefix)

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['sport']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-sport"></a>

[*⇑ Back to ToC ⇑*](#toc)

Source port filter.

Supports single port, comma-separated list, or range.

Examples: `22`, `80,443`, `1024:65535`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['dest']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-dest"></a>

[*⇑ Back to ToC ⇑*](#toc)

Destination address filter.

Supported formats (same as `source`):
  - IPv4/IPv6 address: `10.0.0.1`, `2001:db8::1`
  - Network (CIDR): `10.0.0.0/24`
  - Alias reference: `dc/<alias_name>`
  - IP set reference: `+dc/<ipset_name>` (note the `+` prefix)

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['dport']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-dport"></a>

[*⇑ Back to ToC ⇑*](#toc)

Destination port filter.

Not needed when using macros (they define their own port).

Supports single port, comma-separated list, or range.

Examples: `22`, `80,443`, `1024:65535`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['log']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-log"></a>

[*⇑ Back to ToC ⇑*](#toc)

Log level for matched traffic.

Logs matching packets to syslog at the specified level.

Values: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`,
`info`, `debug`, `nolog`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_cluster_rules['comment']`<a id="variable-pve_proxmox_fw_cluster_rules-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Human-readable description of the rule.

Rendered as a comment after the rule definition.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_fw_node_options`<a id="variable-pve_proxmox_fw_node_options"></a>

[*⇑ Back to ToC ⇑*](#toc)

Node-specific firewall options for this PVE host.

This is a passthrough of original Proxmox VE firewall options. Keys
and values are rendered directly into the `[OPTIONS]` section of
`/etc/pve/nodes/<hostname>/host.fw`.

These options only affect the specific node, not the entire cluster.

Common options:

- `enable`: Enable/disable the host firewall (`0` or `1`)
- `log_level_in`: Log level for incoming traffic
- `log_level_out`: Log level for outgoing traffic
- `log_nf_conntrack`: Log nf_conntrack messages (`0` or `1`)
- `ndp`: Allow NDP (Neighbor Discovery Protocol) for IPv6 (`0` or `1`,
  default: `0`)
- `nf_conntrack_allow_invalid`: Allow invalid conntrack states
  (`0` or `1`, default: `0`)
- `nf_conntrack_helpers`: Enable conntrack helpers (`0` or `1`)
- `nf_conntrack_max`: Maximum conntrack table entries
- `nf_conntrack_tcp_timeout_established`: TCP established timeout
- `nf_conntrack_tcp_timeout_syn_recv`: TCP SYN received timeout
- `nftables`: Use nftables instead of iptables (`0` or `1`,
  default: `0`)
- `nosmurfs`: Enable smurf attack protection (`0` or `1`)
- `protection_synflood`: Enable SYN flood protection (`0` or `1`)
- `protection_synflood_burst`: SYN flood burst limit
- `protection_synflood_rate`: SYN flood rate limit
- `smurf_log_level`: Log level for smurf attack attempts
- `tcp_flags_log_level`: Log level for TCP flag violations
- `tcpflags`: Enable TCP flag checks (`0` or `1`)

Reference:
  https://pve.proxmox.com/wiki/Firewall#pve_firewall_host_specific_configuration

Example:
```yaml
pve_proxmox_fw_node_options:
  nftables: 1
  ndp: 1
  log_level_in: "warning"
  log_level_out: "warning"
```

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`



### `pve_proxmox_fw_node_rules`<a id="variable-pve_proxmox_fw_node_rules"></a>

[*⇑ Back to ToC ⇑*](#toc)

Node-specific firewall rules for this PVE host.

Rules defined here only apply to this specific node, not the entire
cluster. Each rule generates a line in the `[RULES]` section of
`/etc/pve/nodes/<hostname>/host.fw`.

The data structure is identical to `pve_proxmox_fw_cluster_rules`.
Rules can reference cluster-wide aliases (`dc/<name>`) and IP sets
(`+dc/<name>`), as well as security groups.

Reference:
  https://pve.proxmox.com/wiki/Firewall#_firewall_rules

Example:
```yaml
pve_proxmox_fw_node_rules:
  # Allow ICMP from monitoring server
  - direction: "IN"
    action: "Ping(ACCEPT)"
    source: "dc/monitoring-server"
    comment: "Monitoring health checks"

  # Allow backup traffic from specific network
  - direction: "IN"
    action: "ACCEPT"
    proto: "tcp"
    dport: "8007"
    source: "+dc/backup_networks"
    comment: "PBS backup traffic"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_fw_node_rules['direction']`<a id="variable-pve_proxmox_fw_node_rules-sub-direction"></a>

[*⇑ Back to ToC ⇑*](#toc)

Traffic direction for the rule.

Required for all rules except `GROUP` actions.

- `IN`: Incoming traffic (towards the host)
- `OUT`: Outgoing traffic (from the host)

- **Type**: `str`
- **Required**: No
- **Choices**: `IN`, `OUT`

#### `pve_proxmox_fw_node_rules['action']`<a id="variable-pve_proxmox_fw_node_rules-sub-action"></a>

[*⇑ Back to ToC ⇑*](#toc)

Action to take when the rule matches.

See `pve_proxmox_fw_cluster_rules` for detailed documentation.

Supported values: `ACCEPT`, `DROP`, `REJECT`, `MACRO(ACTION)`,
`GROUP`

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_fw_node_rules['security_group']`<a id="variable-pve_proxmox_fw_node_rules-sub-security_group"></a>

[*⇑ Back to ToC ⇑*](#toc)

Security group name to apply.

Required when `action` is `GROUP`.

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['proto']`<a id="variable-pve_proxmox_fw_node_rules-sub-proto"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network protocol to match.

Common values: `tcp`, `udp`, `icmp`, `icmpv6`, `sctp`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['iface']`<a id="variable-pve_proxmox_fw_node_rules-sub-iface"></a>

[*⇑ Back to ToC ⇑*](#toc)

Network interface to match.

Example: `vmbr0`, `eth0`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['source']`<a id="variable-pve_proxmox_fw_node_rules-sub-source"></a>

[*⇑ Back to ToC ⇑*](#toc)

Source address filter.

Supports IPv4/IPv6, CIDR, aliases (`dc/<name>`), and IP sets
(`+dc/<name>`).

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['sport']`<a id="variable-pve_proxmox_fw_node_rules-sub-sport"></a>

[*⇑ Back to ToC ⇑*](#toc)

Source port filter.

Examples: `22`, `80,443`, `1024:65535`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['dest']`<a id="variable-pve_proxmox_fw_node_rules-sub-dest"></a>

[*⇑ Back to ToC ⇑*](#toc)

Destination address filter.

Supports IPv4/IPv6, CIDR, aliases (`dc/<name>`), and IP sets
(`+dc/<name>`).

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['dport']`<a id="variable-pve_proxmox_fw_node_rules-sub-dport"></a>

[*⇑ Back to ToC ⇑*](#toc)

Destination port filter.

Examples: `22`, `80,443`, `1024:65535`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['log']`<a id="variable-pve_proxmox_fw_node_rules-sub-log"></a>

[*⇑ Back to ToC ⇑*](#toc)

Log level for matched traffic.

Values: `emerg`, `alert`, `crit`, `err`, `warning`, `notice`,
`info`, `debug`, `nolog`

- **Type**: `str`
- **Required**: No

#### `pve_proxmox_fw_node_rules['comment']`<a id="variable-pve_proxmox_fw_node_rules-sub-comment"></a>

[*⇑ Back to ToC ⇑*](#toc)

Human-readable description of the rule.

- **Type**: `str`
- **Required**: No



### `pve_proxmox_datacentercfg`<a id="variable-pve_proxmox_datacentercfg"></a>

[*⇑ Back to ToC ⇑*](#toc)

Proxmox VE datacenter-wide configuration settings.

This variable defines cluster-wide defaults rendered to
`/etc/pve/datacenter.cfg`. Since this file resides on pmxcfs (the
FUSE-backed cluster filesystem synchronized via Corosync), settings
apply to all nodes in the cluster.

This is a passthrough of original Proxmox VE datacenter options. Keys
and values are rendered directly as `key: value` lines into
/etc/pve/datacenter.cfg. Nested dictionaries are automatically converted to the PVE
`key=value,key2=value2` format.

Reference:
  https://pve.proxmox.com/wiki/Manual:_datacenter.cfg
  https://pve.proxmox.com/pve-docs/datacenter.cfg.5.html

Example:
```yaml
pve_proxmox_datacentercfg:
  language: "en"
  keyboard: "en-us"
  console: "html5"
  next-id:
    lower: 100
    upper: 1000000
  migration:
    type: "secure"
    network: "10.1.2.0/24"
```

- **Type**: `dict`
- **Required**: No
- **Default**: `{}`



### `pve_proxmox_storage`<a id="variable-pve_proxmox_storage"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of storage definitions for the PVE host.

This variable manages operating system-level storage configuration
including ZFS pools, ZFS datasets, and NFS mounts. Each entry defines
a storage resource with its type-specific attributes.

Supported storage types:

- `zpool`: ZFS storage pool (creates new pools from raw disks)
- `zfs_dataset`: ZFS dataset/filesystem (creates datasets within
  existing pools, supports encryption)
- `nfs`: NFS network mount

The role performs extensive validation before creating storage:
- Verifies disk existence and accessibility
- Checks for existing data on disks (safety check)
- Validates vdev disk counts match RAID requirements
- Detects disks belonging to different pools

For ZFS pools, the role will NOT automatically destroy existing data.
Set `storage_force_cleanup: true` to allow automatic disk wiping
(DESTRUCTIVE - use with extreme caution).

Example:
```yaml
pve_proxmox_storage:
  # ZFS mirror pool on SSDs
  - name: "pool1"
    type: "zpool"
    attributes:
      mountpoint: "none"
      vdevs:
        - type: "mirror"
          disks:
            - "/dev/disk/by-id/scsi-SATA_SSD1"
            - "/dev/disk/by-id/scsi-SATA_SSD2"
      pool_properties:
        ashift: "12"

  # Encrypted dataset for VM storage
  - name: "pool1/vms-encrypted"
    type: "zfs_dataset"
    attributes:
      zfs_properties:
        mountpoint: "/mnt/pool1/vms"
        compression: "on"
        encryption: "aes-256-gcm"
        keyformat: "passphrase"
        keylocation: "prompt"
        passphrase: "{{ vault_zfs_passphrase }}"

  # NFS backup storage
  - name: "nfs-backup"
    type: "nfs"
    attributes:
      storage_properties:
        src: "nas.example.com:/exports/backup"
        path: "/mnt/nfs-backup"
        opts: "defaults,noatime"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_storage['name']`<a id="variable-pve_proxmox_storage-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Storage resource name.

For ZFS pools: The pool name (e.g., `pool1`)
For ZFS datasets: The full dataset path (e.g., `pool1/vms`)
For NFS: A descriptive identifier (e.g., `nfs-backup`)

ZFS naming rules:
  - Must start with a letter
  - Can contain alphanumeric characters, underscores, hyphens
  - Dataset names use `/` to denote hierarchy

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_storage['type']`<a id="variable-pve_proxmox_storage-sub-type"></a>

[*⇑ Back to ToC ⇑*](#toc)

Storage type identifier.

- `zpool`: Create a new ZFS storage pool from raw disks
- `zfs_dataset`: Create a ZFS dataset within an existing pool
- `nfs`: Mount an NFS export from a network server

- **Type**: `str`
- **Required**: Yes
- **Choices**: `zpool`, `zfs_dataset`, `nfs`

#### `pve_proxmox_storage['attributes']`<a id="variable-pve_proxmox_storage-sub-attributes"></a>

[*⇑ Back to ToC ⇑*](#toc)

Type-specific storage attributes.

The structure varies based on the `type` value. See the nested
options documentation for each storage type.

- **Type**: `dict`
- **Required**: Yes

##### `pve_proxmox_storage['attributes']['mountpoint']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-mountpoint"></a>

[*⇑ Back to ToC ⇑*](#toc)

ZFS pool mountpoint (for `zpool` type).

Use `none` to prevent automatic mounting of the pool root.
Child datasets can still have their own mountpoints.

Example: `none`, `/mnt/mypool`

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_storage['attributes']['vdevs']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-vdevs"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of virtual devices (vdevs) for the ZFS pool.

Only applicable for `type: zpool`.

Each vdev defines a RAID configuration with its member disks.
Multiple vdevs can be combined for additional capacity (striped
across vdevs).

Example:
```yaml
vdevs:
  - type: "mirror"
    disks:
      - "/dev/disk/by-id/scsi-SATA_SSD1"
      - "/dev/disk/by-id/scsi-SATA_SSD2"
```

- **Type**: `list`
- **Required**: No
- **List Elements**: `dict`

###### `pve_proxmox_storage['attributes']['vdevs']['type']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-vdevs-sub-type"></a>

[*⇑ Back to ToC ⇑*](#toc)

Vdev RAID type.

- `stripe`: Single disk, no redundancy (NOT recommended for
  important data)
- `mirror`: Two or more disks mirrored (can lose n-1 disks)
- `raidz1`: RAID-Z with single parity (can lose 1 disk,
  requires 2+ disks)
- `raidz2`: RAID-Z with double parity (can lose 2 disks,
  requires 3+ disks)
- `raidz3`: RAID-Z with triple parity (can lose 3 disks,
  requires 4+ disks)

Disk count requirements:
  - `stripe`: exactly 1 disk
  - `mirror`: at least 2 disks
  - `raidz1`: at least 2 disks
  - `raidz2`: at least 3 disks
  - `raidz3`: at least 4 disks

- **Type**: `str`
- **Required**: Yes
- **Choices**: `stripe`, `mirror`, `raidz1`, `raidz2`, `raidz3`

###### `pve_proxmox_storage['attributes']['vdevs']['disks']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-vdevs-sub-disks"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of disk device paths for this vdev.

Always use persistent device paths from `/dev/disk/by-id/`
to ensure consistent identification across reboots.

The role validates that:
  - All disks exist on the system
  - Disks don't contain existing data (unless
    `storage_force_cleanup: true`)
  - Disks aren't already part of a different pool

Example:
```yaml
disks:
  - "/dev/disk/by-id/scsi-SATA_Samsung_SSD_123"
  - "/dev/disk/by-id/scsi-SATA_Samsung_SSD_456"
```

- **Type**: `list`
- **Required**: Yes
- **List Elements**: `str`


##### `pve_proxmox_storage['attributes']['pool_properties']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-pool_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

ZFS pool properties (for `zpool` type).

These are pool-level properties set at creation time. This is
a passthrough of original ZFS pool properties.

Common properties:
  - `ashift`: Sector size exponent (9=512B, 12=4K, 13=8K).
    Use `12` for modern drives with 4K sectors.
  - `autoexpand`: Auto-expand pool when larger disks added
    (`on`/`off`)
  - `autoreplace`: Auto-replace failed disks (`on`/`off`)
  - `failmode`: Behavior on write failure
    (`wait`/`continue`/`panic`)

Example:
```yaml
pool_properties:
  ashift: "12"
  autoexpand: "on"
```

- **Type**: `dict`
- **Required**: No

##### `pve_proxmox_storage['attributes']['filesystem_properties']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-filesystem_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

ZFS filesystem properties for the pool root (for `zpool` type).

These properties are inherited by child datasets unless
overridden. This is a passthrough of original ZFS filesystem
properties.

Common properties: `compression`, `atime`, `xattr`, `acltype`,
`recordsize`

See `zfs_properties` under `zfs_dataset` for detailed property
descriptions.

- **Type**: `dict`
- **Required**: No

##### `pve_proxmox_storage['attributes']['zfs_properties']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-zfs_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

ZFS dataset properties (for `zfs_dataset` type).

These properties configure the dataset's behavior, performance
characteristics, and optional encryption. This is a passthrough
of original ZFS dataset properties.

Common properties:

Storage behavior:
  - `mountpoint`: Where to mount the dataset (e.g., `/mnt/data`)
    Use `none` for unmounted datasets (e.g., zvol parents)
  - `compression`: Compression algorithm (`on`, `off`, `lz4`,
    `zstd`, `gzip-N`)
  - `atime`: Update access time on read (`on`/`off`). Disable
    for performance.
  - `recordsize`: Maximum block size (`128K` default, `1M` for
    large files)
  - `quota`: Maximum size limit (e.g., `100G`)
  - `reservation`: Guaranteed minimum space (e.g., `50G`)

Metadata handling:
  - `xattr`: Extended attribute handling (`on`, `off`, `sa`).
    Use `sa` (system attribute) for performance.
  - `acltype`: ACL type (`off`, `posix`, `nfsv4`)
  - `dnodesize`: Dnode size (`legacy`, `auto`, `1k`-`16k`)

Encryption (native ZFS encryption):
  - `encryption`: Encryption algorithm (`aes-256-gcm`
    recommended)
  - `keyformat`: Key format (`passphrase`, `raw`, `hex`)
  - `keylocation`: Key source (`prompt`, `file:///path/to/key`)
  - `passphrase`: The encryption passphrase (for
    `keylocation: prompt`)
  - `passphrase_old`: Previous passphrase(s) for key rotation
    (string or list)

Note: `passphrase` and `passphrase_old` are special keys
handled by the role and not passed directly to ZFS.

Example (encrypted dataset):
```yaml
zfs_properties:
  mountpoint: "/mnt/secure-data"
  compression: "on"
  atime: "off"
  xattr: "sa"
  encryption: "aes-256-gcm"
  keyformat: "passphrase"
  keylocation: "prompt"
  passphrase: "{{ vault_passphrase }}"
  passphrase_old:
    - "12345aaaaarrrrRR"
    - "456789bbbbbbbTTT"
```

Example (high-performance dataset):
```yaml
zfs_properties:
  mountpoint: "/mnt/vms"
  compression: "lz4"
  atime: "off"
  recordsize: "64K"
  xattr: "sa"
  acltype: "off"
```

- **Type**: `dict`
- **Required**: No

##### `pve_proxmox_storage['attributes']['storage_properties']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-storage_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

NFS mount properties (for `nfs` type).

Configures NFS client mounts. The role validates server
reachability before attempting to mount.

- **Type**: `dict`
- **Required**: No

###### `pve_proxmox_storage['attributes']['storage_properties']['src']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-src"></a>

[*⇑ Back to ToC ⇑*](#toc)

NFS server and export path.

Format: `<server>:<export_path>`

Example: `nas.example.com:/exports/backup`

- **Type**: `str`
- **Required**: Yes

###### `pve_proxmox_storage['attributes']['storage_properties']['path']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-path"></a>

[*⇑ Back to ToC ⇑*](#toc)

Local mountpoint directory.

The directory will be created if it doesn't exist.

Example: `/mnt/nfs-backup`

- **Type**: `str`
- **Required**: Yes

###### `pve_proxmox_storage['attributes']['storage_properties']['opts']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-opts"></a>

[*⇑ Back to ToC ⇑*](#toc)

NFS mount options. This is a passthrough of the original
mount options.

Common options:
  - `defaults`: Standard mount options
  - `noatime`: Don't update access times (performance)
  - `nfsvers=4`: Force NFSv4
  - `soft`: Return errors on timeout (vs. `hard`)
  - `timeo=N`: Timeout in deciseconds
  - `retrans=N`: Number of retries

Example: `defaults,noatime,nfsvers=4`

- **Type**: `str`
- **Required**: No
- **Default**: `"defaults"`

###### `pve_proxmox_storage['attributes']['storage_properties']['state']`<a id="variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-state"></a>

[*⇑ Back to ToC ⇑*](#toc)

Desired mount state.

- `mounted`: Mount and add to fstab
- `present`: Add to fstab but don't mount
- `unmounted`: Unmount but keep in fstab
- `absent`: Unmount and remove from fstab

- **Type**: `str`
- **Required**: No
- **Default**: `"mounted"`
- **Choices**: `mounted`, `present`, `unmounted`, `absent`





### `pve_proxmox_storage_force_cleanup`<a id="variable-pve_proxmox_storage_force_cleanup"></a>

[*⇑ Back to ToC ⇑*](#toc)

Allow automatic cleanup of existing data on disks for ZFS pool
creation.

DESTRUCTIVE OPERATION WARNING: When set to `true`, the role will
automatically wipe filesystem signatures and ZFS labels from disks
that have existing data but whose target pool does not exist.

This is a safety mechanism. By default (`false`), the role will fail
with detailed instructions if it encounters disks with existing data,
allowing you to manually verify and clean the disks.

Use cases for enabling:
  - Fresh installations where disks are known to be empty or
    recyclable
  - Automated provisioning where disk contents are irrelevant
  - Rebuilding pools after intentional destruction

The role will NEVER automatically clean disks that:
  - Belong to a different existing ZFS pool (requires manual
    intervention)
  - Are part of an existing pool that matches the configuration

Example:
```yaml
# Enable automatic disk cleanup (DANGEROUS)
pve_proxmox_storage_force_cleanup: true
```

- **Type**: `bool`
- **Required**: No
- **Default**: `false`



### `pve_proxmox_sm`<a id="variable-pve_proxmox_sm"></a>

[*⇑ Back to ToC ⇑*](#toc)

Proxmox VE Storage Manager (pvesm) configuration.

This variable defines storage resources visible in the PVE web UI and
available for VM/container disk allocation, backups, ISO storage, and
container templates.

These entries configure PVE's storage layer (`/etc/pve/storage.cfg`),
which is separate from the underlying filesystem/pool creation handled
by `pve_proxmox_storage`. Typically, you first create the storage
backend (ZFS pool, NFS mount, etc.) via `pve_proxmox_storage`, then
register it with PVE via `pve_proxmox_sm`.

Supported storage types:

- `dir`: Directory-based storage (any mounted filesystem)
- `zfspool`: ZFS pool/dataset storage (for zvols and datasets)

Where:
- `nodename|shared`: Node-local or cluster-shared storage
- `guest`: VM/container disk storage (usually encrypted)
- `assets`: ISOs, templates, snippets (usually not encrypted)
- `backup`: Backup target for vzdump (usually encrypted)
- `N`: Priority index (lower = preferred for workload type)

Example:
```yaml
pve_proxmox_sm:
  # ZFS storage for VMs/containers
  - name: "pve1-guest1"
    type: "zfspool"
    storage_properties:
      pool: "pool123/vms"
      content:
        - "images"
        - "rootdir"
      sparse: true
      nodes:
        - "pve1"

  # Directory storage for ISOs and templates
  - name: "pve1-assets1"
    type: "dir"
    storage_properties:
      path: "/mnt/assets"
      is_mountpoint: true
      content:
        - "iso"
        - "vztmpl"
        - "snippets"
      nodes:
        - "pve1"

  # Directory storage for backups
  - name: "pve1-backup1"
    type: "dir"
    storage_properties:
      path: "/mnt/backup"
      is_mountpoint: true
      content:
        - "backup"
      nodes:
        - "pve1"
```

- **Type**: `list`
- **Required**: No
- **Default**: `[]`
- **List Elements**: `dict`

#### `pve_proxmox_sm['name']`<a id="variable-pve_proxmox_sm-sub-name"></a>

[*⇑ Back to ToC ⇑*](#toc)

Storage identifier as shown in the PVE web UI.

Must be unique across the cluster. This name is used to reference
the storage in VM/container configurations and backup jobs.

Naming convention: `<node|shared>-<purpose><index>`

Examples:
  - `pve1-guest1`: Primary guest storage on node pve1
  - `pve1-backup1`: Backup storage on node pve1
  - `shared-assets1`: Shared asset storage (cluster-wide)

- **Type**: `str`
- **Required**: Yes

#### `pve_proxmox_sm['type']`<a id="variable-pve_proxmox_sm-sub-type"></a>

[*⇑ Back to ToC ⇑*](#toc)

PVE storage type.

Determines how PVE interacts with the underlying storage backend.

- `dir`: Directory-based storage. Uses a filesystem path for
  storing disk images as files (qcow2, raw, vmdk). Suitable for
  any mounted filesystem (local, NFS, CIFS, etc.).

- `zfspool`: Native ZFS storage. Uses ZFS zvols for VM disks and
  ZFS datasets for container storage. Provides better performance
  and snapshot capabilities than directory storage on ZFS.

Note: The underlying storage (ZFS pool, NFS mount, etc.) must
already exist. Use `pve_proxmox_storage` to create it first.

- **Type**: `str`
- **Required**: Yes
- **Choices**: `dir`, `zfspool`

#### `pve_proxmox_sm['storage_properties']`<a id="variable-pve_proxmox_sm-sub-storage_properties"></a>

[*⇑ Back to ToC ⇑*](#toc)

Type-specific storage configuration properties.

The available options depend on the `type` value.

- **Type**: `dict`
- **Required**: Yes

##### `pve_proxmox_sm['storage_properties']['content']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-content"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of content types this storage can hold.

Determines what PVE allows to be stored here. A storage can
support multiple content types.

Available content types:

- `images`: Virtual machine disk images (qcow2, raw, vmdk)
- `rootdir`: Container root directories (for LXC containers)
- `backup`: Backup archives from vzdump
- `iso`: ISO images for VM installation
- `vztmpl`: Container templates (.tar.gz, .tar.xz)
- `snippets`: Configuration snippets (hookscripts, cloud-init)

Typical combinations:
  - Guest storage: `[images, rootdir]`
  - Asset storage: `[iso, vztmpl, snippets]`
  - Backup storage: `[backup]`

Example:
```yaml
content:
  - "images"
  - "rootdir"
```

- **Type**: `list`
- **Required**: No
- **Choices**: `images`, `rootdir`, `backup`, `iso`, `vztmpl`, `snippets`
- **List Elements**: `str`

##### `pve_proxmox_sm['storage_properties']['nodes']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-nodes"></a>

[*⇑ Back to ToC ⇑*](#toc)

List of cluster nodes where this storage is available.

Limits storage visibility to specific nodes. Useful for
node-local storage that shouldn't appear on other nodes.

If omitted, the storage is available on all cluster nodes
(appropriate for shared/network storage).

Example:
```yaml
nodes:
  - "pve1"
  - "pve2"
```

- **Type**: `list`
- **Required**: No
- **List Elements**: `str`

##### `pve_proxmox_sm['storage_properties']['is_mountpoint']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-is_mountpoint"></a>

[*⇑ Back to ToC ⇑*](#toc)

Indicates the storage path is an external mountpoint.

When `true`, PVE will:
  - Check that the path is actually mounted before use
  - Prevent operations if the mountpoint is not available
  - Display appropriate warnings in the UI

Set to `true` for:
  - NFS/CIFS mounts
  - ZFS datasets with dedicated mountpoints
  - Any storage on a separately mounted filesystem

Set to `false` (or omit) for:
  - Subdirectories on the root filesystem
  - Paths that are always available

- **Type**: `bool`
- **Required**: No
- **Default**: `false`

##### `pve_proxmox_sm['storage_properties']['path']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-path"></a>

[*⇑ Back to ToC ⇑*](#toc)

Filesystem path for directory storage (for `type: dir`).

The directory must exist and be writable. For ZFS datasets,
this is typically the dataset's mountpoint.

The role will create the directory if it doesn't exist.

Example: `/mnt/pool123/assets`

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_sm['storage_properties']['pool']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-pool"></a>

[*⇑ Back to ToC ⇑*](#toc)

ZFS pool or dataset name (for `type: zfspool`).

This is the ZFS dataset path, not a filesystem path. PVE will
create zvols and child datasets under this location.

The pool/dataset must already exist. Use `pve_proxmox_storage`
with `type: zpool` or `type: zfs_dataset` to create it.

Example: `pool123/vms` or `tank/proxmox/guests`

- **Type**: `str`
- **Required**: No

##### `pve_proxmox_sm['storage_properties']['sparse']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-sparse"></a>

[*⇑ Back to ToC ⇑*](#toc)

Enable thin provisioning for ZFS zvols (for `type: zfspool`).

When `true`:
  - Zvols only consume space for written data
  - VM disks appear full-sized but use less actual space
  - Risk of overcommitment if total allocated exceeds pool

When `false`:
  - Zvols pre-allocate their full size immediately
  - Guaranteed space availability
  - No overcommitment risk

Thin provisioning is generally recommended for efficiency but
requires monitoring pool usage to avoid space exhaustion.

- **Type**: `bool`
- **Required**: No
- **Default**: `false`

##### `pve_proxmox_sm['storage_properties']['blocksize']`<a id="variable-pve_proxmox_sm-sub-storage_properties-sub-blocksize"></a>

[*⇑ Back to ToC ⇑*](#toc)

ZFS block size (volblocksize) for new zvols
(for `type: zfspool`).

Determines the minimum allocation unit for VM disk writes.
Optimal value depends on workload:

- `4k`/`8k`: Database workloads, random I/O
- `16k`: General purpose (good default)
- `32k`/`64k`: Sequential workloads, large files
- `128k`: Maximum, for mostly sequential large-file access

If omitted, uses the pool's default recordsize.

Example: `16k`

- **Type**: `str`
- **Required**: No





<!-- ANSIBLE DOCSMITH MAIN END -->


## Dependencies<a id="dependencies"></a>

See `dependencies` in [`meta/main.yml`](./meta/main.yml).



## Compatibility<a id="compatibility"></a>

See `min_ansible_version` in [`meta/main.yml`](./meta/main.yml) and `__pve_proxmox_supported_platforms` in [`vars/main.yml`](./vars/main.yml).



## External requirements<a id="requirements"></a>

There are no special requirements not covered by Ansible itself.
