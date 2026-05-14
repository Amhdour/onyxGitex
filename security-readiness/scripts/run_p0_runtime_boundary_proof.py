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


def now(): return datetime.now(timezone.utc).isoformat()

def write_json(p: Path, obj: dict): p.write_text(json.dumps(obj, indent=2) + "\n")

results=[]
for c in CONTROLS:
    folder = BASE / c.folder
    cmd_path = folder / "test-command.txt"
    pytest_out = folder / "pytest-output.txt"
    runtime_log = folder / "runtime-log.txt"
    raw = cmd_path.read_text(encoding="utf-8").strip() if cmd_path.exists() else ""
    placeholder = (not raw) or ("COMMAND_PLACEHOLDER_NOT_EXECUTED" in raw)
    result = {
        "control_id": c.control_id, "control_name": c.control_name,
        "supports_go_claim": False, "supports_production_claim": False, "supports_client_claim": False,
        "runtime_log_path": str(runtime_log.relative_to(ROOT)), "pytest_output_path": str(pytest_out.relative_to(ROOT)),
        "test_command": raw or "COMMAND_PLACEHOLDER_NOT_EXECUTED", "timestamp_utc": now(),
    }
    if placeholder:
        result |= {"status":"BLOCKED","evidence_level":"TEST_COMMAND_MISSING","test_executed":False,"exit_code":None,
                   "supports_local_runtime_claim":False,"limitations":["Missing executable test command."],
                   "blockers":["TEST_COMMAND_MISSING"],"next_required_action":"Define a real test command and rerun V2.2 proof."}
    else:
        cp = subprocess.run(shlex.split(raw), cwd=ROOT, capture_output=True, text=True)
        pytest_out.write_text((cp.stdout or "") + "\n\n=== STDERR ===\n" + (cp.stderr or ""), encoding="utf-8")
        runtime_log.write_text("NO_RUNTIME_LOG_CAPTURED — command executed but no separate runtime log source was configured.\n", encoding="utf-8")
        passed = cp.returncode == 0 and pytest_out.exists() and runtime_log.exists()
        result |= {
            "status":"PASSED" if passed else "FAILED",
            "evidence_level":"LOCAL_RUNTIME" if passed else "LOCAL_TEST_FAILED",
            "test_executed":True,"exit_code":cp.returncode,
            "supports_local_runtime_claim": passed,
            "limitations": [] if passed else ["Test command returned non-zero exit code."],
            "blockers": [] if passed else ["TEST_FAILURE"],
            "next_required_action": "Replay in CI (V2.3)." if passed else "Fix failing test/control and rerun V2.2 proof.",
        }
    write_json(folder / "evidence-result.json", result)
    results.append(result)

counts = {"PASSED":0,"FAILED":0,"BLOCKED":0,"NOT_EXECUTED":0}
for r in results: counts[r["status"]]+=1
all_passed = counts["PASSED"] == len(CONTROLS)
if counts["BLOCKED"] == len(CONTROLS): overall = "BLOCKED"
elif all_passed: overall = "PASSED"
elif counts["FAILED"] > 0 or counts["BLOCKED"] > 0: overall = "PARTIAL"
else: overall = "FAILED"
final = {
    "milestone":"V2.2 — Execute P0 Runtime Boundary Proof",
    "p0_runtime_boundary_proof_status":overall,
    "all_p0_controls_passed":all_passed,
    "supports_launch_go":False,"supports_production_ready":False,"supports_client_verified":False,"supports_staging_verified":False,
    "controls_total":len(CONTROLS),"controls_passed":counts["PASSED"],"controls_failed":counts["FAILED"],"controls_blocked":counts["BLOCKED"],"controls_not_executed":counts["NOT_EXECUTED"],
    "control_results":results,
    "blocking_reason":"One or more P0 controls are failed/blocked or only local runtime evidence exists.",
    "next_required_action":"Resolve failed/blocked controls and replay in CI (V2.3).",
    "timestamp_utc":now(),
}
write_json(BASE / "final-status.json", final)
print(json.dumps({"overall":overall, **counts}, indent=2))
