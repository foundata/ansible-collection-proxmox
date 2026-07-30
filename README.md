# Ansible collection: `foundata.proxmox`

This repository contains the `foundata.proxmox` Ansible Collection.

It provides resources to manage and different Proxmox products:

* [Proxmox Virtual Environment (PVE)](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview)
* [Proxmox Backup Server (PBS)](https://www.proxmox.com/en/products/proxmox-backup-server/overview)
* [Proxmox Datacenter Manager (PDM)](https://www.proxmox.com/en/products/proxmox-datacenter-manager/overview)
* [Proxmox Mail Gateway (PMG)](https://www.proxmox.com/en/products/proxmox-mail-gateway/overview)

⚠ Please note: The features, roles, and modules in this collection are stable and tested, but the **collection is still evolving and not yet fully feature-complete**. We recommend checking that the features and products you need are currently supported before use.<br> We decided to release this collection earlier than usual because we think the available functionality is already useful and worth sharing with the community.


<div align="center" id="project-readme-header">
<br>
<br>

**⭐ Found this useful? Support open-source and star this project:**

[![GitHub repository](https://img.shields.io/github/stars/foundata/ansible-collection-proxmox.svg)](https://github.com/foundata/ansible-collection-proxmox)

<br>
</div>


## Table of contents<a id="toc"></a>

- [Included content](#content)
  - [Role: `foundata.proxmox.pve` (Proxmox Virtual Environment)](#content-role-pve)
  - [Role: `foundata.proxmox.pbs` (Proxmox Backup Server)](#content-role-pbs)
  - [Role: `foundata.proxmox.pdm` (Proxmox Datacenter Manager)](#content-role-pdm)
  - [Role: `foundata.proxmox.pmg` (Proxmox Mail Gateway)](#content-role-pmg)
- [Dependencies](#dependencies)
- [Licensing, copyright](#licensing-copyright)
- [Author information](#author-information)



## Included content<a id="content"></a>

### Role: `foundata.proxmox.pve` (Proxmox Virtual Environment)<a id="content-role-pve"></a>

The resource in this collection to configure and maintain Proxmox Virtual Environment (PVE) nodes, including network, firewall, storage, and related settings. [Its `README.md`](./roles/pve/README.md) covers configuration, usage examples, and more:

<!-- ANSIBLE DOCSMITH TOC-FULL pve START -->
- [Ansible role: `foundata.proxmox.pve`](roles/pve/README.md#ansible-role-foundataproxmoxpve)
  - [Table of contents](roles/pve/README.md#toc)
  - [Features](roles/pve/README.md#features)
  - [Example playbooks, using this role](roles/pve/README.md#examples)
  - [Supported tags](roles/pve/README.md#tags)
  - [Role variables](roles/pve/README.md#variables)
    - [`pve_proxmox_state`](roles/pve/README.md#variable-pve_proxmox_state)
    - [`pve_proxmox_tmpbackupfiles`](roles/pve/README.md#variable-pve_proxmox_tmpbackupfiles)
    - [`pve_proxmox_iommu_manage`](roles/pve/README.md#variable-pve_proxmox_iommu_manage)
    - [`pve_proxmox_net_altnames`](roles/pve/README.md#variable-pve_proxmox_net_altnames)
      - [`pve_proxmox_net_altnames['type']`](roles/pve/README.md#variable-pve_proxmox_net_altnames-sub-type)
      - [`pve_proxmox_net_altnames['mac_address']`](roles/pve/README.md#variable-pve_proxmox_net_altnames-sub-mac_address)
      - [`pve_proxmox_net_altnames['desc']`](roles/pve/README.md#variable-pve_proxmox_net_altnames-sub-desc)
      - [`pve_proxmox_net_altnames['altnames']`](roles/pve/README.md#variable-pve_proxmox_net_altnames-sub-altnames)
    - [`pve_proxmox_net_ifaces_host_shared`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared)
      - [`pve_proxmox_net_ifaces_host_shared['options_before']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-options_before)
      - [`pve_proxmox_net_ifaces_host_shared['sections']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['title']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-title)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-comment)
        - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces)
          - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['name']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-name)
          - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['method']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-method)
          - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['auto']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-auto)
          - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-comment)
          - [`pve_proxmox_net_ifaces_host_shared['sections']['interfaces']['iface_properties']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-sections-sub-interfaces-sub-iface_properties)
      - [`pve_proxmox_net_ifaces_host_shared['options_after']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_shared-sub-options_after)
    - [`pve_proxmox_net_ifaces_host_specific`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific)
      - [`pve_proxmox_net_ifaces_host_specific['options_before']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-options_before)
      - [`pve_proxmox_net_ifaces_host_specific['sections']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['title']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-title)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-comment)
        - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces)
          - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['name']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-name)
          - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['method']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-method)
          - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['auto']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-auto)
          - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-comment)
          - [`pve_proxmox_net_ifaces_host_specific['sections']['interfaces']['iface_properties']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-sections-sub-interfaces-sub-iface_properties)
      - [`pve_proxmox_net_ifaces_host_specific['options_after']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_host_specific-sub-options_after)
    - [`pve_proxmox_net_ifaces_workload_shared`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared)
      - [`pve_proxmox_net_ifaces_workload_shared['options_before']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-options_before)
      - [`pve_proxmox_net_ifaces_workload_shared['sections']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['title']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-title)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-comment)
        - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces)
          - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['name']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-name)
          - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['method']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-method)
          - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['auto']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-auto)
          - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-comment)
          - [`pve_proxmox_net_ifaces_workload_shared['sections']['interfaces']['iface_properties']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-sections-sub-interfaces-sub-iface_properties)
      - [`pve_proxmox_net_ifaces_workload_shared['options_after']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_shared-sub-options_after)
    - [`pve_proxmox_net_ifaces_workload_specific`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific)
      - [`pve_proxmox_net_ifaces_workload_specific['options_before']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-options_before)
      - [`pve_proxmox_net_ifaces_workload_specific['sections']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['title']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-title)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-comment)
        - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces)
          - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['name']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-name)
          - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['method']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-method)
          - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['auto']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-auto)
          - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['comment']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-comment)
          - [`pve_proxmox_net_ifaces_workload_specific['sections']['interfaces']['iface_properties']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-sections-sub-interfaces-sub-iface_properties)
      - [`pve_proxmox_net_ifaces_workload_specific['options_after']`](roles/pve/README.md#variable-pve_proxmox_net_ifaces_workload_specific-sub-options_after)
    - [`pve_proxmox_fw_cluster_options`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_options)
    - [`pve_proxmox_fw_cluster_aliases`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_aliases)
      - [`pve_proxmox_fw_cluster_aliases['name']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_aliases-sub-name)
      - [`pve_proxmox_fw_cluster_aliases['ip']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_aliases-sub-ip)
      - [`pve_proxmox_fw_cluster_aliases['comment']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_aliases-sub-comment)
    - [`pve_proxmox_fw_cluster_ipsets`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets)
      - [`pve_proxmox_fw_cluster_ipsets['name']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets-sub-name)
      - [`pve_proxmox_fw_cluster_ipsets['comment']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets-sub-comment)
      - [`pve_proxmox_fw_cluster_ipsets['entries']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets-sub-entries)
        - [`pve_proxmox_fw_cluster_ipsets['entries']['ip']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-ip)
        - [`pve_proxmox_fw_cluster_ipsets['entries']['comment']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-comment)
        - [`pve_proxmox_fw_cluster_ipsets['entries']['nomatch']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_ipsets-sub-entries-sub-nomatch)
    - [`pve_proxmox_fw_cluster_securitygroups`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_securitygroups)
      - [`pve_proxmox_fw_cluster_securitygroups['name']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_securitygroups-sub-name)
      - [`pve_proxmox_fw_cluster_securitygroups['comment']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_securitygroups-sub-comment)
      - [`pve_proxmox_fw_cluster_securitygroups['rules']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_securitygroups-sub-rules)
    - [`pve_proxmox_fw_cluster_rules`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules)
      - [`pve_proxmox_fw_cluster_rules['direction']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-direction)
      - [`pve_proxmox_fw_cluster_rules['action']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-action)
      - [`pve_proxmox_fw_cluster_rules['security_group']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-security_group)
      - [`pve_proxmox_fw_cluster_rules['proto']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-proto)
      - [`pve_proxmox_fw_cluster_rules['iface']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-iface)
      - [`pve_proxmox_fw_cluster_rules['source']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-source)
      - [`pve_proxmox_fw_cluster_rules['sport']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-sport)
      - [`pve_proxmox_fw_cluster_rules['dest']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-dest)
      - [`pve_proxmox_fw_cluster_rules['dport']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-dport)
      - [`pve_proxmox_fw_cluster_rules['log']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-log)
      - [`pve_proxmox_fw_cluster_rules['comment']`](roles/pve/README.md#variable-pve_proxmox_fw_cluster_rules-sub-comment)
    - [`pve_proxmox_fw_node_options`](roles/pve/README.md#variable-pve_proxmox_fw_node_options)
    - [`pve_proxmox_fw_node_rules`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules)
      - [`pve_proxmox_fw_node_rules['direction']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-direction)
      - [`pve_proxmox_fw_node_rules['action']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-action)
      - [`pve_proxmox_fw_node_rules['security_group']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-security_group)
      - [`pve_proxmox_fw_node_rules['proto']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-proto)
      - [`pve_proxmox_fw_node_rules['iface']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-iface)
      - [`pve_proxmox_fw_node_rules['source']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-source)
      - [`pve_proxmox_fw_node_rules['sport']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-sport)
      - [`pve_proxmox_fw_node_rules['dest']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-dest)
      - [`pve_proxmox_fw_node_rules['dport']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-dport)
      - [`pve_proxmox_fw_node_rules['log']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-log)
      - [`pve_proxmox_fw_node_rules['comment']`](roles/pve/README.md#variable-pve_proxmox_fw_node_rules-sub-comment)
    - [`pve_proxmox_datacentercfg`](roles/pve/README.md#variable-pve_proxmox_datacentercfg)
    - [`pve_proxmox_storage`](roles/pve/README.md#variable-pve_proxmox_storage)
      - [`pve_proxmox_storage['name']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-name)
      - [`pve_proxmox_storage['type']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-type)
      - [`pve_proxmox_storage['attributes']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes)
        - [`pve_proxmox_storage['attributes']['mountpoint']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-mountpoint)
        - [`pve_proxmox_storage['attributes']['vdevs']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-vdevs)
          - [`pve_proxmox_storage['attributes']['vdevs']['type']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-vdevs-sub-type)
          - [`pve_proxmox_storage['attributes']['vdevs']['disks']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-vdevs-sub-disks)
        - [`pve_proxmox_storage['attributes']['pool_properties']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-pool_properties)
        - [`pve_proxmox_storage['attributes']['filesystem_properties']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-filesystem_properties)
        - [`pve_proxmox_storage['attributes']['zfs_properties']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-zfs_properties)
        - [`pve_proxmox_storage['attributes']['storage_properties']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties)
          - [`pve_proxmox_storage['attributes']['storage_properties']['src']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-src)
          - [`pve_proxmox_storage['attributes']['storage_properties']['path']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-path)
          - [`pve_proxmox_storage['attributes']['storage_properties']['opts']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-opts)
          - [`pve_proxmox_storage['attributes']['storage_properties']['state']`](roles/pve/README.md#variable-pve_proxmox_storage-sub-attributes-sub-storage_properties-sub-state)
    - [`pve_proxmox_storage_force_cleanup`](roles/pve/README.md#variable-pve_proxmox_storage_force_cleanup)
    - [`pve_proxmox_sm`](roles/pve/README.md#variable-pve_proxmox_sm)
      - [`pve_proxmox_sm['name']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-name)
      - [`pve_proxmox_sm['type']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-type)
      - [`pve_proxmox_sm['storage_properties']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties)
        - [`pve_proxmox_sm['storage_properties']['content']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-content)
        - [`pve_proxmox_sm['storage_properties']['nodes']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-nodes)
        - [`pve_proxmox_sm['storage_properties']['is_mountpoint']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-is_mountpoint)
        - [`pve_proxmox_sm['storage_properties']['path']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-path)
        - [`pve_proxmox_sm['storage_properties']['pool']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-pool)
        - [`pve_proxmox_sm['storage_properties']['sparse']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-sparse)
        - [`pve_proxmox_sm['storage_properties']['blocksize']`](roles/pve/README.md#variable-pve_proxmox_sm-sub-storage_properties-sub-blocksize)
  - [Dependencies](roles/pve/README.md#dependencies)
  - [Compatibility](roles/pve/README.md#compatibility)
  - [External requirements](roles/pve/README.md#requirements)
<!-- ANSIBLE DOCSMITH TOC-FULL pve END -->



### Role: `foundata.proxmox.pbs` (Proxmox Backup Server)<a id="content-role-pbs"></a>

To be done / not released yet.



### Role: `foundata.proxmox.pdm` (Proxmox Datacenter Manager)<a id="content-role-pdm"></a>

To be done / not released yet.



### Role: `foundata.proxmox.pmg` (Proxmox Mail Gateway)<a id="content-role-pmg"></a>

To be done / not released yet.



## Dependencies<a id="dependencies"></a>

See `dependencies` in [`galaxy.yml`](./galaxy.yml).



## Licensing, copyright<a id="licensing-copyright"></a>

<!--REUSE-IgnoreStart-->
Copyright (c) 2025, 2026 [foundata GmbH](https://foundata.com/) (https://foundata.com)

This project is licensed under the GNU General Public License v3.0 or later (SPDX-License-Identifier: `GPL-3.0-or-later`), see [`LICENSES/GPL-3.0-or-later.txt`](LICENSES/GPL-3.0-or-later.txt) for the full text.

The [`REUSE.toml`](REUSE.toml) file provides detailed licensing and copyright information in a human- and machine-readable format. This includes parts that may be subject to different licensing or usage terms, such as third-party components. The repository conforms to the [REUSE specification](https://reuse.software/spec/). You can use [`reuse spdx`](https://reuse.readthedocs.io/en/latest/readme.html#cli) to create a [SPDX software bill of materials (SBOM)](https://en.wikipedia.org/wiki/Software_Package_Data_Exchange).
<!--REUSE-IgnoreEnd-->

[![REUSE status](https://api.reuse.software/badge/github.com/foundata/ansible-collection-proxmox)](https://api.reuse.software/info/github.com/foundata/ansible-collection-proxmox)



## Author information<a id="author-information"></a>

This [project](https://foundata.com/en/projects/) was created and is maintained by [foundata](https://foundata.com/).

Initially based on an [Ansible skeleton](https://foundata.com/en/projects/ansible-skeletons/) developed by [foundata](https://foundata.com/).
