"""Tier 4 runtime integration structure for citation leakage launch blocker.

Fail-closed behavior is required:
- If runtime fixtures are unavailable, tests skip and the Tier 4 artifact is BLOCKED.
- PASS artifacts are only allowed when all required runtime assertions execute.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from .tier4_artifact_writer import (
    mark_blocked,
    mark_passed_only_if_assertions_executed,
    write_tier4_result_artifact,
)
from .tier4_runtime_fixtures import (
    allowed_document,
    authorized_user,
    build_runtime_context,
    restricted_document,
    unauthorized_user,
)

CITATION_LEAKAGE_ARTIFACT = Path(
    "security-readiness/evidence-artifacts/test-results/"
    "citation-leakage-tests.json"
)
FORBIDDEN_MARKERS = ["[RESTRICTED]", "restricted://", "acl:restricted"]
ASSERTIONS_EXECUTED = False
REQUIRED_ASSERTION_KEYS = {
    "allowed_citation_present",
    "restricted_citation_absent",
    "restricted_source_id_absent",
    "restricted_document_title_absent",
    "restricted_url_absent",
    "restricted_metadata_absent",
    "restricted_marker_absent_from_answer",
    "audit_event_captured",
    "runtime_trace_captured",
}
ASSERTION_COMPLETION = {key: False for key in REQUIRED_ASSERTION_KEYS}


def _mark_assertion_complete(assertion_key: str) -> None:
    if assertion_key not in ASSERTION_COMPLETION:
        raise ValueError(f"Unknown Tier 4 assertion key: {assertion_key}")
    ASSERTION_COMPLETION[assertion_key] = True


def _all_required_assertions_completed() -> bool:
    return all(ASSERTION_COMPLETION.values())


def _any_blocked(fixtures: dict[str, Any]) -> list[str]:
    blockers: list[str] = []
    for name, value in fixtures.items():
        if isinstance(value, dict) and value.get("status") == "BLOCKED":
            blockers.append(f"{name}: {value.get('reason', 'Unknown blocker')}")
    return blockers


@pytest.fixture(scope="module")
def tier4_runtime_context() -> dict[str, Any]:
    fixtures = {
        "authorized_user": authorized_user(),
        "unauthorized_user": unauthorized_user(),
        "allowed_document": allowed_document(),
        "restricted_document": restricted_document(),
    }

    blockers = _any_blocked(fixtures)
    if blockers:
        artifact = mark_blocked(
            suite_id="citation_leakage_tests",
            blockers=blockers,
        )
        write_tier4_result_artifact(CITATION_LEAKAGE_ARTIFACT, artifact)
        pytest.skip(
            "Tier 4 runtime fixtures unavailable; fail-closed BLOCKED artifact written."
        )

    context = build_runtime_context(fixtures)
    if not context.get("runtime_ready", False):
        artifact = mark_blocked(
            suite_id="citation_leakage_tests",
            blockers=["Runtime context not executable in current environment."],
        )
        write_tier4_result_artifact(CITATION_LEAKAGE_ARTIFACT, artifact)
        pytest.skip("Tier 4 runtime context is not executable in current environment.")

    return context


def test_allowed_citation_present(tier4_runtime_context: dict[str, Any]) -> None:
    global ASSERTIONS_EXECUTED
    citations = tier4_runtime_context["capture_citation_metadata"]()
    assert len(citations) > 0
    assert citations[0].get("authorized") is True
    ASSERTIONS_EXECUTED = True
    _mark_assertion_complete("allowed_citation_present")


def test_restricted_citation_absent(tier4_runtime_context: dict[str, Any]) -> None:
    citations = tier4_runtime_context["capture_citation_metadata"]()
    assert all(not c.get("restricted", False) for c in citations)
    _mark_assertion_complete("restricted_citation_absent")


def test_restricted_source_id_absent(tier4_runtime_context: dict[str, Any]) -> None:
    citations = tier4_runtime_context["capture_citation_metadata"]()
    assert all("restricted_source_id" not in c for c in citations)
    _mark_assertion_complete("restricted_source_id_absent")


def test_restricted_document_title_absent(tier4_runtime_context: dict[str, Any]) -> None:
    citations = tier4_runtime_context["capture_citation_metadata"]()
    assert all("restricted_document_title" not in c for c in citations)
    _mark_assertion_complete("restricted_document_title_absent")


def test_restricted_url_absent(tier4_runtime_context: dict[str, Any]) -> None:
    citations = tier4_runtime_context["capture_citation_metadata"]()
    assert all("restricted_url" not in c for c in citations)
    _mark_assertion_complete("restricted_url_absent")


def test_restricted_metadata_absent(tier4_runtime_context: dict[str, Any]) -> None:
    citations = tier4_runtime_context["capture_citation_metadata"]()
    assert all("restricted_metadata" not in c for c in citations)
    _mark_assertion_complete("restricted_metadata_absent")


def test_restricted_marker_absent_from_answer(
    tier4_runtime_context: dict[str, Any],
) -> None:
    answer_text = tier4_runtime_context["capture_answer_text"]()
    for marker in FORBIDDEN_MARKERS:
        assert marker not in answer_text
    _mark_assertion_complete("restricted_marker_absent_from_answer")


def test_audit_event_captured(tier4_runtime_context: dict[str, Any]) -> None:
    event = tier4_runtime_context["capture_audit_event"]()
    assert event.get("status") == "captured"
    _mark_assertion_complete("audit_event_captured")


def test_runtime_trace_captured(tier4_runtime_context: dict[str, Any]) -> None:
    trace = tier4_runtime_context["capture_runtime_trace"]()
    assert trace.get("status") == "captured"
    _mark_assertion_complete("runtime_trace_captured")


@pytest.fixture(scope="module", autouse=True)
def _write_pass_artifact_only_if_assertions_executed() -> None:
    yield
    completed_assertions = sorted(
        [key for key, completed in ASSERTION_COMPLETION.items() if completed]
    )
    missing_assertions = sorted(REQUIRED_ASSERTION_KEYS - set(completed_assertions))

    if _all_required_assertions_completed():
        artifact = mark_passed_only_if_assertions_executed(
            suite_id="citation_leakage_tests",
            assertions_executed=True,
            tests_run=len(REQUIRED_ASSERTION_KEYS),
            forbidden_markers_checked=FORBIDDEN_MARKERS,
            forbidden_markers_found=[],
        )
        write_tier4_result_artifact(CITATION_LEAKAGE_ARTIFACT, artifact)
        return

    if ASSERTIONS_EXECUTED:
        write_tier4_result_artifact(
            CITATION_LEAKAGE_ARTIFACT,
            {
                **mark_blocked(
                    suite_id="citation_leakage_tests",
                    blockers=[
                        "Tier 4 PASS prohibited: not all required citation leakage assertions completed."
                    ],
                ),
                "status": "FAILED",
                "tests_run": len(completed_assertions),
                "tests_passed": len(completed_assertions),
                "tests_failed": len(missing_assertions),
                "blockers": [
                    "Tier 4 PASS prohibited: not all required citation leakage assertions completed.",
                    f"Missing assertions: {', '.join(missing_assertions)}",
                ],
            },
        )
