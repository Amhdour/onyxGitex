"""Tier 4 runtime artifact scaffolding.

This module must never emit PASS for blocked scaffolding-only runtime tests.
"""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_RUNTIME_LEVEL = "TIER_4"
DEFAULT_LAUNCH_POSTURE = "NOT_ENOUGH_EVIDENCE"


def _git_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except Exception:
        return "UNKNOWN"


def build_result_envelope(
    suite_id: str,
    status: str,
    tests_run: int,
    tests_passed: int,
    tests_failed: int,
    blockers: list[str] | None = None,
    audit_events: list[dict[str, Any]] | None = None,
    runtime_traces: list[dict[str, Any]] | None = None,
    forbidden_markers_checked: list[str] | None = None,
    forbidden_markers_found: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "suite_id": suite_id,
        "status": status,
        "runtime_level": DEFAULT_RUNTIME_LEVEL,
        "launch_posture": DEFAULT_LAUNCH_POSTURE,
        "tests_run": tests_run,
        "tests_passed": tests_passed,
        "tests_failed": tests_failed,
        "blockers": blockers or [],
        "audit_events": audit_events or [],
        "runtime_traces": runtime_traces or [],
        "forbidden_markers_checked": forbidden_markers_checked or [],
        "forbidden_markers_found": forbidden_markers_found or [],
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": _git_commit(),
    }


def mark_blocked(suite_id: str, blockers: list[str]) -> dict[str, Any]:
    return build_result_envelope(
        suite_id=suite_id,
        status="BLOCKED",
        tests_run=0,
        tests_passed=0,
        tests_failed=0,
        blockers=blockers,
    )


def mark_failed(
    suite_id: str,
    tests_run: int,
    tests_failed: int,
    blockers: list[str] | None = None,
) -> dict[str, Any]:
    return build_result_envelope(
        suite_id=suite_id,
        status="FAILED",
        tests_run=tests_run,
        tests_passed=max(tests_run - tests_failed, 0),
        tests_failed=tests_failed,
        blockers=blockers,
    )


def mark_passed_only_if_assertions_executed(
    suite_id: str,
    assertions_executed: bool,
    tests_run: int,
    forbidden_markers_checked: list[str],
    forbidden_markers_found: list[str],
) -> dict[str, Any]:
    if not assertions_executed:
        return mark_blocked(
            suite_id=suite_id,
            blockers=["Assertions were not executed; PASS is prohibited."],
        )

    return build_result_envelope(
        suite_id=suite_id,
        status="PASSED",
        tests_run=tests_run,
        tests_passed=tests_run,
        tests_failed=0,
        blockers=[],
        forbidden_markers_checked=forbidden_markers_checked,
        forbidden_markers_found=forbidden_markers_found,
    )


def write_tier4_result_artifact(
    artifact_path: str | Path,
    result_envelope: dict[str, Any],
) -> Path:
    output_path = Path(artifact_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result_envelope, indent=2, sort_keys=True) + "\n")
    return output_path
