import json

from tests.integration.tests.chat.tier4_artifact_writer import (
    build_result_envelope,
    mark_blocked,
    mark_failed,
    mark_passed_only_if_assertions_executed,
    write_tier4_result_artifact,
)


def test_mark_blocked_sets_expected_defaults() -> None:
    result = mark_blocked("tier4_artifact_writer", ["backend blocked"])

    assert result["status"] == "BLOCKED"
    assert result["tests_run"] == 0
    assert result["launch_posture"] == "NOT_ENOUGH_EVIDENCE"


def test_mark_failed_sets_expected_counts() -> None:
    result = mark_failed("tier4_artifact_writer", tests_run=5, tests_failed=2)

    assert result["status"] == "FAILED"
    assert result["tests_passed"] == 3
    assert result["tests_failed"] == 2


def test_mark_passed_requires_assertions_execution_when_false() -> None:
    result = mark_passed_only_if_assertions_executed(
        suite_id="tier4_artifact_writer",
        assertions_executed=False,
        tests_run=4,
        forbidden_markers_checked=["NO_ASSERTIONS_EXECUTED"],
        forbidden_markers_found=[],
    )

    assert result["status"] == "BLOCKED"


def test_mark_passed_requires_assertions_execution_when_true() -> None:
    result = mark_passed_only_if_assertions_executed(
        suite_id="tier4_artifact_writer",
        assertions_executed=True,
        tests_run=4,
        forbidden_markers_checked=["NO_ASSERTIONS_EXECUTED"],
        forbidden_markers_found=[],
    )

    assert result["status"] == "PASSED"


def test_build_result_envelope_has_required_schema_fields() -> None:
    result = build_result_envelope(
        suite_id="tier4_artifact_writer",
        status="FAILED",
        tests_run=3,
        tests_passed=2,
        tests_failed=1,
    )

    required_fields = {
        "suite_id",
        "status",
        "runtime_level",
        "launch_posture",
        "tests_run",
        "tests_passed",
        "tests_failed",
        "blockers",
        "audit_events",
        "runtime_traces",
        "forbidden_markers_checked",
        "forbidden_markers_found",
        "generated_at_utc",
        "git_commit",
    }

    assert required_fields.issubset(result.keys())


def test_write_tier4_result_artifact_writes_valid_json(tmp_path) -> None:
    result = mark_blocked("tier4_artifact_writer", ["backend blocked"])
    output_file = tmp_path / "tier4-result.json"

    written = write_tier4_result_artifact(output_file, result)

    assert written == output_file
    loaded = json.loads(output_file.read_text())
    assert loaded == result
