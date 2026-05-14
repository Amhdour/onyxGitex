#!/usr/bin/env python3
from __future__ import annotations
import json, os, subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "security-readiness/evidence-artifacts/p0-runtime-boundary-proof"
TIMEOUT_SECONDS = int(os.environ.get("P0_TEST_TIMEOUT_SECONDS", "120"))

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

def is_runtime_cmd(cmd: str) -> bool:
    return "backend/tests/integration" in cmd or "backend/tests/" in cmd

def classify_result(cmd: str, exit_code: int | None, output: str, timed_out: bool) -> dict:
    lower = output.lower()
    if timed_out:
        return dict(status="BLOCKED_TEST_RUNTIME_TIMEOUT" if is_runtime_cmd(cmd) else "BLOCKED_TIMEOUT", evidence_level="BLOCKED_TIMEOUT", test_executed=True, assertions_reached=False, failure_classification="timeout", root_cause_summary="Command exceeded timeout before producing conclusive evidence.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=["TEST_TIMEOUT"], recommended_fix="Inspect command dependencies, runtime services, and test isolation; rerun with configured environment or adjusted timeout only if justified.")
    if "modulenotfounderror" in lower and "fastapi_users" in lower:
        return dict(status="BLOCKED_IMPORT_DEPENDENCY", evidence_level="BLOCKED_IMPORT_DEPENDENCY", test_executed=True, assertions_reached=False, failure_classification="missing_python_dependency", root_cause_summary="Pytest import/collection failed before assertions because required dependency fastapi_users is missing.", dependency_blockers=["fastapi_users"], environment_blockers=[], test_collection_blockers=["ModuleNotFoundError"], blockers=["MISSING_PYTHON_DEPENDENCY: fastapi_users"], recommended_fix="Install/resolve fastapi-users dependency per repository dependency workflow and rerun.")
    if any(x in lower for x in ["importerror while loading conftest", "error collecting", "interrupted:"]) or exit_code == 4:
        return dict(status="BLOCKED_TEST_COLLECTION", evidence_level="BLOCKED_TEST_COLLECTION", test_executed=True, assertions_reached=False, failure_classification="pytest_collection_failure", root_cause_summary="Pytest could not collect tests before assertions.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=["pytest_collection_failure"], blockers=["PYTEST_COLLECTION_FAILED"], recommended_fix="Resolve collection/import/conftest/config errors and rerun.")
    if exit_code == 0:
        evidence = "LOCAL_HARNESS" if "tests/security_readiness/" in cmd else ("LOCAL_INTEGRATION" if "backend/tests/integration" in cmd else "LOCAL_RUNTIME")
        return dict(status="PASSED", evidence_level=evidence, test_executed=True, assertions_reached=True, failure_classification="none", root_cause_summary="Assertions executed and passed.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=[], recommended_fix="Replay in CI to strengthen evidence.")
    return dict(status="FAILED_ASSERTION", evidence_level="LOCAL_HARNESS_ASSERTION_FAILED" if "tests/security_readiness/" in cmd else "LOCAL_TEST_ASSERTION_FAILED", test_executed=True, assertions_reached=True, failure_classification="assertion_failure_or_runtime_nonzero", root_cause_summary="Command executed and returned non-zero after test execution.", dependency_blockers=[], environment_blockers=[], test_collection_blockers=[], blockers=["TEST_ASSERTION_OR_RUNTIME_FAILURE"], recommended_fix="Inspect pytest output and fix failing assertions/runtime paths.")

results=[]
for c in CONTROLS:
    folder=BASE/c.folder
    raw=(folder/"test-command.txt").read_text(encoding="utf-8").strip()
    pytest_out=folder/"pytest-output.txt"
    runtime_log=folder/"runtime-log.txt"
    exit_code=None; output=""; timed_out=False
    try:
        cp=subprocess.run(raw, cwd=ROOT, capture_output=True, text=True, shell=True, timeout=TIMEOUT_SECONDS)
        output=(cp.stdout or "")+"\n\n=== STDERR ===\n"+(cp.stderr or "")
        exit_code=cp.returncode
    except subprocess.TimeoutExpired as e:
        timed_out=True
        output=(e.stdout or "")+"\n\n=== STDERR ===\n"+(e.stderr or "")+f"\n\nTIMEOUT: command exceeded {TIMEOUT_SECONDS} seconds."
    pytest_out.write_text(output, encoding="utf-8")
    runtime_log.write_text("TIMEOUT_OCCURRED\n" if timed_out else "NO_RUNTIME_LOG_CAPTURED — command executed but no separate runtime log source was configured.\n", encoding="utf-8")
    cls=classify_result(raw, exit_code, output, timed_out)
    passed=cls["status"]=="PASSED"
    result={"control_id":c.control_id,"control_name":c.control_name,"status":cls["status"],"evidence_level":cls["evidence_level"],"test_executed":True,"assertions_reached":cls["assertions_reached"],"test_command":raw,"exit_code":exit_code,"timeout_seconds":TIMEOUT_SECONDS,"timed_out":timed_out,"pytest_output_path":str(pytest_out.relative_to(ROOT)),"runtime_log_path":str(runtime_log.relative_to(ROOT)),"failure_classification":cls["failure_classification"],"root_cause_summary":cls["root_cause_summary"],"dependency_blockers":cls["dependency_blockers"],"environment_blockers":cls["environment_blockers"],"test_collection_blockers":cls["test_collection_blockers"],"supports_local_harness_claim":passed and cls["evidence_level"]=="LOCAL_HARNESS","supports_local_runtime_claim":passed and cls["evidence_level"] in {"LOCAL_RUNTIME","LOCAL_INTEGRATION"},"supports_go_claim":False,"supports_production_claim":False,"supports_client_claim":False,"supports_staging_claim":False,"limitations":[] if passed else [cls["root_cause_summary"]],"blockers":cls["blockers"],"recommended_fix":cls["recommended_fix"],"next_required_action":cls["recommended_fix"],"timestamp_utc":now()}
    write_json(folder/"evidence-result.json", result)
    results.append(result)

counts={k:sum(1 for r in results if r['status']==v) for k,v in {'controls_passed':'PASSED','controls_failed_assertion':'FAILED_ASSERTION','controls_failed_test_runtime':'FAILED_TEST_RUNTIME','controls_blocked_import_dependency':'BLOCKED_IMPORT_DEPENDENCY','controls_blocked_test_collection':'BLOCKED_TEST_COLLECTION','controls_blocked_environment':'BLOCKED_ENVIRONMENT','controls_blocked_command_missing':'BLOCKED_COMMAND_MISSING','controls_blocked_timeout':'BLOCKED_TIMEOUT','controls_blocked_test_runtime_timeout':'BLOCKED_TEST_RUNTIME_TIMEOUT','controls_not_executed':'NOT_EXECUTED'}.items()}
final={"milestone":"V2.2.3 — Real Onyx Runtime / Integration P0 Tests","p0_runtime_boundary_proof_status":"PARTIAL_OR_FAILED","all_p0_controls_passed":counts['controls_passed']==len(CONTROLS),"any_assertion_failures":counts['controls_failed_assertion']>0,"supports_launch_go":False,"supports_production_ready":False,"supports_client_verified":False,"supports_staging_verified":False,"controls_total":len(CONTROLS),**counts,"controls_local_harness_passed":sum(1 for r in results if r['status']=='PASSED' and r['evidence_level']=='LOCAL_HARNESS'),"controls_local_runtime_passed":sum(1 for r in results if r['status']=='PASSED' and r['evidence_level']=='LOCAL_RUNTIME'),"controls_local_integration_passed":sum(1 for r in results if r['status']=='PASSED' and r['evidence_level']=='LOCAL_INTEGRATION'),"assertions_reached":sum(1 for r in results if r['assertions_reached']),"control_results":results,"blocking_reason":"Local evidence only; unresolved blocked/timeout controls keep NO_GO.","corrected_interpretation":"LOCAL_HARNESS and any LOCAL_RUNTIME/LOCAL_INTEGRATION evidence do not support production/client/staging claims.","next_required_action":"Resolve blockers and replay in CI (V2.3).","timestamp_utc":now()}
write_json(BASE/"final-status.json", final)
print(json.dumps({"overall":final['p0_runtime_boundary_proof_status'], **counts}, indent=2))
