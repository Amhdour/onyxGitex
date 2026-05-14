#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess
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
    return dict(status="FAILED_ASSERTION", evidence_level="LOCAL_HARNESS_ASSERTION_FAILED" if "tests/security_readiness/" in cmd else "LOCAL_TEST_ASSERTION_FAILED", test_executed=True, assertions_reached=True, failure_classification="assertion_failure_or_runtime_nonzero", root_cause_summary="Command executed and returned non-zero after test execution.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=["TEST_ASSERTION_OR_RUNTIME_FAILURE"], recommended_fix="Inspect pytest output and fix failing assertions/runtime paths.")

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
        cp = subprocess.run(raw, cwd=ROOT, capture_output=True, text=True, shell=True)
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
        "supports_local_runtime_claim": passed and cls["evidence_level"] == "LOCAL_RUNTIME",
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

total = len(CONTROLS)
passed = counts["controls_passed"]
blocked_import_dependency = counts["controls_blocked_import_dependency"]
controls_local_harness_passed = sum(1 for r in results if r["status"]=="PASSED" and r["evidence_level"]=="LOCAL_HARNESS")
controls_local_runtime_passed = sum(1 for r in results if r["status"]=="PASSED" and r["evidence_level"]=="LOCAL_RUNTIME")
assertions_reached = sum(1 for r in results if r["assertions_reached"])

if controls_local_harness_passed > 0 and blocked_import_dependency > 0:
    overall = "PARTIAL_LOCAL_HARNESS"
    blocking_reason = "Some P0 controls passed at LOCAL_HARNESS level while others remain blocked by import/dependency setup."
    corrected_interpretation = f"{controls_local_harness_passed} P0 controls have LOCAL_HARNESS evidence with assertions reached and passed. {blocked_import_dependency} P0 controls remain blocked by import/dependency setup. No full runtime, CI, staging, production, client, compliance, or launch-GO claim is supported."
    next_required_action = "Resolve blockers for remaining controls and execute real runtime/integration evidence in V2.2.3."
elif controls_local_harness_passed == 0 and blocked_import_dependency > 0:
    overall = "BLOCKED_IMPORT_DEPENDENCY"
    blocking_reason = "Pytest collection/import is blocked by missing dependency fastapi_users."
    corrected_interpretation = "No P0 control is proven passed and no P0 control is functionally proven failed; execution is blocked before meaningful security assertions."
    next_required_action = "Install/resolve dependency blockers, rerun P0 proof, then execute validator."
elif controls_local_runtime_passed == total:
    overall = "LOCAL_RUNTIME_COMPLETE"
    blocking_reason = "All P0 controls reached assertions and passed at LOCAL_RUNTIME level."
    corrected_interpretation = "All seven P0 controls have LOCAL_RUNTIME evidence, but CI/staging/production/client claims remain blocked unless those environments produce evidence."
    next_required_action = "Replay P0 proof in CI and staging before readiness claims can increase."
elif controls_local_harness_passed == total:
    overall = "LOCAL_HARNESS_COMPLETE"
    blocking_reason = "All P0 controls reached assertions and passed at LOCAL_HARNESS level."
    corrected_interpretation = "All seven P0 controls have LOCAL_HARNESS evidence, but full runtime, CI, staging, production, client, compliance, and launch-GO claims remain blocked."
    next_required_action = "Convert LOCAL_HARNESS evidence to LOCAL_RUNTIME and CI/staging evidence before readiness claims can increase."
else:
    overall = "PARTIAL_OR_FAILED"
    blocking_reason = "Some controls passed while others failed or remained blocked."
    corrected_interpretation = "Mixed control outcomes detected; launch remains NO_GO until all required P0 controls pass with appropriate evidence level."
    next_required_action = "Resolve failures/blockers, rerun P0 proof, and validate canonical artifacts."

final = {
    "milestone": "V2.2.2-hotfix — Correct Mixed-Result P0 Status Wording",
    "p0_runtime_boundary_proof_status": overall,
    "all_p0_controls_passed": all_passed,
    "any_assertion_failures": counts["controls_failed_assertion"] > 0,
    "supports_launch_go": False,
    "supports_production_ready": False,
    "supports_client_verified": False,
    "supports_staging_verified": False,
    "controls_total": total,
    **counts,
    "controls_local_harness_passed": controls_local_harness_passed,
    "controls_local_runtime_passed": controls_local_runtime_passed,
    "assertions_reached": assertions_reached,
    "control_results": results,
    "blocking_reason": blocking_reason,
    "corrected_interpretation": corrected_interpretation,
    "next_required_action": next_required_action,
    "timestamp_utc": now(),
}
write_json(BASE / "final-status.json", final)
print(json.dumps({"overall": overall, **counts}, indent=2))
