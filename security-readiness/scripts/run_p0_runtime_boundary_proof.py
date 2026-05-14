#!/usr/bin/env python3
from __future__ import annotations
import json, shlex, subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "security-readiness/evidence-artifacts/p0-runtime-boundary-proof"

@dataclass(frozen=True)
class Control:
    control_id: str
    control_name: str
    folder: str

CONTROLS = [
    Control("P0-RA-001", "Retrieval Authorization", "01-retrieval-authorization"),
    Control("P0-CL-001", "Citation Leakage Boundary", "02-citation-leakage-boundary"),
    Control("P0-PI-001", "Prompt-Injection Retrieval Boundary", "03-prompt-injection-retrieval-boundary"),
    Control("P0-TA-001", "Tool Authorization", "04-tool-authorization"),
    Control("P0-FC-001", "Fail-Closed Behavior", "05-fail-closed-behavior"),
    Control("P0-AL-001", "Audit Logging", "06-audit-logging"),
    Control("P0-TT-001", "Telemetry Tracing", "07-telemetry-tracing"),
]

def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()

def write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")

def classify_result(cmd: str, exit_code: int | None, output: str) -> dict:
    lower = output.lower()
    if not cmd or "COMMAND_PLACEHOLDER_NOT_EXECUTED" in cmd:
        return dict(status="BLOCKED_COMMAND_MISSING", evidence_level="BLOCKED_NO_RUNTIME", test_executed=False, assertions_reached=False, failure_classification="missing_command", root_cause_summary="No executable test command exists for this control.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=["TEST_COMMAND_MISSING"], recommended_fix="Provide an executable pytest command in test-command.txt.")
    if "modulenotfounderror" in lower and "fastapi_users" in lower:
        return dict(status="BLOCKED_IMPORT_DEPENDENCY", evidence_level="BLOCKED_IMPORT_DEPENDENCY", test_executed=True, assertions_reached=False, failure_classification="missing_python_dependency", root_cause_summary="Pytest import/collection failed before assertions because required dependency fastapi_users is missing.", dependency_blockers=["fastapi_users"], environment_blockers=[], test_collection_blockers=["ModuleNotFoundError"], blockers=["MISSING_PYTHON_DEPENDENCY: fastapi_users"], recommended_fix="Install/resolve fastapi-users dependency per repository dependency workflow and rerun.")
    if any(x in lower for x in ["importerror while loading conftest", "error collecting", "interrupted:"]) or exit_code == 4:
        return dict(status="BLOCKED_TEST_COLLECTION", evidence_level="BLOCKED_TEST_COLLECTION", test_executed=True, assertions_reached=False, failure_classification="pytest_collection_failure", root_cause_summary="Pytest could not collect tests before assertions.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=["pytest_collection_failure"], blockers=["PYTEST_COLLECTION_FAILED"], recommended_fix="Resolve collection/import/conftest/config errors and rerun.")
    if "no tests ran" in lower:
        return dict(status="BLOCKED_TEST_COLLECTION", evidence_level="BLOCKED_TEST_COLLECTION", test_executed=True, assertions_reached=False, failure_classification="no_tests_collected", root_cause_summary="Pytest executed but did not run any tests.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=["no_tests_ran"], blockers=["NO_TESTS_COLLECTED"], recommended_fix="Verify test path and pytest discovery configuration.")
    if exit_code == 0:
        evidence = "LOCAL_HARNESS" if "tests/security_readiness/" in cmd else "LOCAL_RUNTIME"
        return dict(status="PASSED", evidence_level=evidence, test_executed=True, assertions_reached=True, failure_classification="none", root_cause_summary="Assertions executed and passed.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=[], recommended_fix="Replay in CI to strengthen evidence.")
    return dict(status="FAILED_ASSERTION", evidence_level="LOCAL_TEST_ASSERTION_FAILED", test_executed=True, assertions_reached=True, failure_classification="assertion_failure_or_runtime_nonzero", root_cause_summary="Command executed and returned non-zero after test execution.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=["TEST_ASSERTION_OR_RUNTIME_FAILURE"], recommended_fix="Inspect pytest output and fix failing assertions/runtime paths.")

results = []
for c in CONTROLS:
    folder = BASE / c.folder
    cmd_path = folder / "test-command.txt"
    pytest_out = folder / "pytest-output.txt"
    runtime_log = folder / "runtime-log.txt"
    raw = cmd_path.read_text(encoding="utf-8").strip() if cmd_path.exists() else ""
    if not raw or "COMMAND_PLACEHOLDER_NOT_EXECUTED" in raw:
        cls = classify_result(raw, None, "")
        exit_code = None
    else:
        cp = subprocess.run(shlex.split(raw), cwd=ROOT, capture_output=True, text=True)
        combined = (cp.stdout or "") + "\n\n=== STDERR ===\n" + (cp.stderr or "")
        pytest_out.write_text(combined, encoding="utf-8")
        runtime_log.write_text("NO_RUNTIME_LOG_CAPTURED — command executed but no separate runtime log source was configured.\n", encoding="utf-8")
        cls = classify_result(raw, cp.returncode, combined)
        exit_code = cp.returncode
    passed = cls["status"] == "PASSED"
    result = {
        "control_id": c.control_id, "control_name": c.control_name,
        "status": cls["status"], "evidence_level": cls["evidence_level"],
        "test_executed": cls["test_executed"], "assertions_reached": cls["assertions_reached"],
        "test_command": raw or "COMMAND_PLACEHOLDER_NOT_EXECUTED", "exit_code": exit_code,
        "pytest_output_path": str(pytest_out.relative_to(ROOT)), "runtime_log_path": str(runtime_log.relative_to(ROOT)),
        "failure_classification": cls["failure_classification"], "root_cause_summary": cls["root_cause_summary"],
        "dependency_blockers": cls["dependency_blockers"], "environment_blockers": cls["environment_blockers"],
        "test_collection_blockers": cls["test_collection_blockers"],
        "supports_local_harness_claim": passed and cls["evidence_level"] == "LOCAL_HARNESS",
        "supports_local_runtime_claim": passed,
        "supports_go_claim": False, "supports_production_claim": False, "supports_client_claim": False, "supports_staging_claim": False,
        "limitations": [] if passed else [cls["root_cause_summary"]], "blockers": cls["blockers"],
        "recommended_fix": cls["recommended_fix"], "next_required_action": cls["recommended_fix"], "timestamp_utc": now(),
    }
    write_json(folder / "evidence-result.json", result)
    results.append(result)

counts = {
    "controls_passed": sum(1 for r in results if r["status"] == "PASSED"),
    "controls_failed_assertion": sum(1 for r in results if r["status"] == "FAILED_ASSERTION"),
    "controls_failed_test_runtime": sum(1 for r in results if r["status"] == "FAILED_TEST_RUNTIME"),
    "controls_blocked_import_dependency": sum(1 for r in results if r["status"] == "BLOCKED_IMPORT_DEPENDENCY"),
    "controls_blocked_test_collection": sum(1 for r in results if r["status"] == "BLOCKED_TEST_COLLECTION"),
    "controls_blocked_environment": sum(1 for r in results if r["status"] == "BLOCKED_ENVIRONMENT"),
    "controls_blocked_command_missing": sum(1 for r in results if r["status"] == "BLOCKED_COMMAND_MISSING"),
    "controls_not_executed": sum(1 for r in results if r["status"] == "NOT_EXECUTED"),
}
all_passed = counts["controls_passed"] == len(CONTROLS)
overall = "BLOCKED_IMPORT_DEPENDENCY" if counts["controls_blocked_import_dependency"] else ("PASSED" if all_passed else "PARTIAL")
final = {
    "milestone": "V2.2.1 — Fix P0 Execution Environment and Failure Classification",
    "p0_runtime_boundary_proof_status": overall,
    "all_p0_controls_passed": all_passed,
    "any_assertion_failures": counts["controls_failed_assertion"] > 0,
    "supports_launch_go": False, "supports_production_ready": False, "supports_client_verified": False, "supports_staging_verified": False,
    "controls_total": len(CONTROLS), **counts, "control_results": results,
    "blocking_reason": "P0 commands were attempted but pytest collection/import failed because required dependency fastapi_users is missing." if counts["controls_blocked_import_dependency"] else "One or more controls are not PASSED.",
    "corrected_interpretation": "No P0 control is proven passed and no P0 control is functionally proven failed; execution is blocked before meaningful security assertions.",
    "next_required_action": "Install/resolve required test dependencies or isolate lightweight harness tests from heavy backend conftest, then rerun P0 proof.",
    "timestamp_utc": now(),
}
write_json(BASE / "final-status.json", final)
print(json.dumps({"overall": overall, **counts}, indent=2))
