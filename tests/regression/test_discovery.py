"""Reject ambiguous dataset discovery before any creation decision."""

import pytest
from _pve_tasks import assertion, run_play, select


def declaration(name="fixture/data"):
    return {
        "name": name,
        "type": "zfs_dataset",
        "attributes": {"zfs_properties": {"encryption": "off"}},
    }


def observed(returncode=0, stdout="fixture/data\tfilesystem\n", stderr=""):
    return {
        "rc": returncode,
        "stdout": stdout,
        "stderr": stderr,
        "__pve_proxmox_dataset_facts_item": declaration(),
    }


@pytest.mark.parametrize(
    "name",
    [
        "fixture",
        "fixture/data",
        "fixture/data space",
        "fixture/data%temporary",
        "fixture/data:-_1",
        "pool space/data",
        "fixture/" + "d" * 247,
    ],
)
def test_native_dataset_names_are_preserved(tmp_path, name):
    run_play(
        tmp_path,
        [select("storage", "Validate ZFS dataset selectors")],
        {"__pve_storage_sanitized": [declaration(name)]},
    )


@pytest.mark.parametrize(
    "name",
    [
        "",
        "-a",
        "/mnt/data",
        "fixture/",
        "fixture//data",
        "fixture/../data",
        "fixture/./data",
        "fixture/data@snapshot",
        "fixture/data#bookmark",
        "fixture/$HOME",
        "fixture/data\n",
        "fixture/data\tother",
        "fixture/data\x00other",
        "mirror/data",
        None,
        "fixture/" + "d" * 248,
    ],
)
def test_invalid_selectors_are_rejected_before_discovery(tmp_path, name):
    run_play(
        tmp_path,
        [select("storage", "Validate ZFS dataset selectors")],
        {"__pve_storage_sanitized": [declaration(name)]},
        expected_failure="ZFS dataset selector must be an exact filesystem or volume name",
    )


@pytest.mark.parametrize(
    "result",
    [
        observed(stdout=""),
        observed(stdout="fixture/data\tfilesystem"),
        observed(stdout="fixture/data\tfilesystem\n\n"),
        observed(stdout="fixture/data\tfilesystem\nother/data\tfilesystem\n"),
        observed(stdout="other/data\tfilesystem\n"),
        observed(stdout="fixture/data\tsnapshot\n"),
        observed(stderr="warning\n"),
        observed(1, "", "cannot open 'fixture/data': permission denied\n"),
        observed(1, "", "cannot open 'other/data': dataset does not exist\n"),
        observed(127, "", "cannot open 'fixture/data': dataset does not exist\n"),
        observed(1, "", "cannot open 'fixture/data': dataset does not exist"),
        observed(False),
        observed("0"),
        observed(stdout=[]),
        observed(stderr=None),
        {**observed(), "skipped": True},
    ],
)
def test_failed_or_malformed_discovery_never_becomes_absence(tmp_path, result):
    run_play(
        tmp_path,
        [select("storage", "Validate dataset discovery results")],
        {"__pve_zfs_dataset_facts": {"results": [result]}},
        expected_failure="Cannot establish ZFS dataset presence",
    )


@pytest.mark.parametrize("kind", ["filesystem", "volume"])
def test_exact_discovery_records_presence(tmp_path, kind):
    run_play(
        tmp_path,
        [
            select("storage", "Validate dataset discovery results"),
            select("storage", "Build zfs_dataset existence map"),
            assertion("__pve_zfs_dataset_exists['fixture/data']"),
        ],
        {
            "__pve_zfs_dataset_facts": {
                "results": [observed(stdout=f"fixture/data\t{kind}\n")]
            }
        },
    )


@pytest.mark.parametrize("check", [False, True])
def test_exact_missing_child_requires_imported_root_before_absence(tmp_path, check):
    root = select("storage", "Verify imported root for absent datasets")
    root["ansible.builtin.command"]["argv"] = [
        "/usr/bin/printf",
        "%s",
        "fixture\tfilesystem\n",
    ]
    run_play(
        tmp_path,
        [
            select("storage", "Validate dataset discovery results"),
            root,
            select("storage", "Validate imported root discovery coverage"),
            select("storage", "Validate imported dataset roots"),
            select("storage", "Build zfs_dataset existence map"),
            assertion("not __pve_zfs_dataset_exists['fixture/data']"),
            assertion(
                "not __pve_zfs_dataset_roots['results'][0]['skipped'] | default(false)"
            ),
        ],
        {
            "__pve_zfs_dataset_facts": {
                "results": [
                    observed(
                        1, "", "cannot open 'fixture/data': dataset does not exist\n"
                    )
                ]
            }
        },
        check=check,
    )


@pytest.mark.parametrize(
    "returncode, stdout, stderr",
    [
        (1, "", "cannot open 'fixture': dataset does not exist\n"),
        (127, "", "command unavailable\n"),
        (0, "", ""),
        (0, "fixture\tfilesystem", ""),
        (0, "fixture\tfilesystem\n\n", ""),
        (0, "other\tfilesystem\n", ""),
        (0, "fixture\tvolume\n", ""),
        (0, "fixture\tfilesystem\n", "warning\n"),
        (False, "fixture\tfilesystem\n", ""),
        (0, "fixture\tfilesystem\n", None),
    ],
)
def test_unknown_or_absent_imported_root_refuses_creation(
    tmp_path, returncode, stdout, stderr
):
    result = {
        "rc": returncode,
        "stdout": stdout,
        "stderr": stderr,
        "__pve_zfs_root_probe_item": observed(
            1, "", "cannot open 'fixture/data': dataset does not exist\n"
        ),
    }
    run_play(
        tmp_path,
        [select("storage", "Validate imported dataset roots")],
        {"__pve_zfs_dataset_roots": {"results": [result]}},
        expected_failure="Cannot verify the imported pool root",
    )


@pytest.mark.parametrize("check", [False, True])
def test_dataset_probe_keeps_raw_framing_in_check_mode(tmp_path, check):
    probe = select("storage", "Gather existing ZFS datasets")
    command = probe["ansible.builtin.command"]
    assert command["argv"][:-1] == [
        "zfs",
        "list",
        "-H",
        "-p",
        "-o",
        "name,type",
        "-t",
        "filesystem,volume",
        "--",
    ]
    assert command["expand_argument_vars"] is False
    assert command["strip_empty_ends"] is False
    assert probe["environment"] == {"LC_ALL": "C"}
    command["argv"] = ["/usr/bin/printf", "%s", "fixture/data\tfilesystem\n"]
    run_play(
        tmp_path,
        [
            probe,
            select("storage", "Validate dataset discovery results"),
            assertion("not __pve_zfs_dataset_facts['results'][0]['changed']"),
        ],
        {
            "pve_proxmox_storage": [declaration()],
            "__pve_storage_sanitized": [declaration()],
        },
        check=check,
    )


def test_existing_off_declaration_passes_top_level_validation(tmp_path):
    run_play(
        tmp_path,
        [select("storage", "Validate the declared storage items")],
        {
            "pve_proxmox_storage": [declaration()],
            "__pve_storage_sanitized": [declaration()],
        },
    )


@pytest.mark.parametrize(
    "target_returncode, failure",
    [(0, None), (1, "Cannot verify the imported pool root")],
)
def test_only_existing_targets_may_skip_imported_root_probe(
    tmp_path, target_returncode, failure
):
    result = {"skipped": True, "__pve_zfs_root_probe_item": observed(target_returncode)}
    run_play(
        tmp_path,
        [select("storage", "Validate imported dataset roots")],
        {"__pve_zfs_dataset_roots": {"results": [result]}},
        expected_failure=failure,
    )


@pytest.mark.parametrize(
    "results, names, failure",
    [
        ([], ["fixture/data"], "Incomplete ZFS dataset discovery"),
        ([], [], None),
        (
            [observed(), observed()],
            ["fixture/data"],
            "Incomplete ZFS dataset discovery",
        ),
        ([observed()], ["fixture/other"], "Incomplete ZFS dataset discovery"),
        ({}, ["fixture/data"], "Incomplete ZFS dataset discovery"),
        ("", ["fixture/data"], "Incomplete ZFS dataset discovery"),
    ],
)
def test_dataset_results_cover_all_declared_names(tmp_path, results, names, failure):
    run_play(
        tmp_path,
        [select("storage", "Validate dataset discovery coverage")],
        {
            "__pve_storage_sanitized": [declaration(name) for name in names],
            "__pve_zfs_dataset_facts": {"results": results},
        },
        expected_failure=failure,
    )


@pytest.mark.parametrize(
    "results",
    [
        [],
        [{"__pve_zfs_root_probe_item": observed()}],
        [
            {
                "__pve_zfs_root_probe_item": {
                    **observed(1),
                    "__pve_proxmox_dataset_facts_item": declaration("other/data"),
                }
            }
        ],
        [
            {"__pve_zfs_root_probe_item": observed(1)},
            {"__pve_zfs_root_probe_item": observed(1)},
        ],
    ],
)
def test_root_results_cover_the_original_target_reads(tmp_path, results):
    run_play(
        tmp_path,
        [select("storage", "Validate imported root discovery coverage")],
        {
            "__pve_zfs_dataset_facts": {"results": [observed(1)]},
            "__pve_zfs_dataset_roots": {"results": results},
        },
        expected_failure="Incomplete imported-root discovery",
    )
