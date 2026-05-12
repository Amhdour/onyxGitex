#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATION = ROOT / "security-readiness/evidence-artifacts/evidence-validation/validation-result.json"
LAUNCH_GATE = ROOT / "security-readiness/evidence-artifacts/launch-gate/launch-gate-result.json"
DECISION_MD = ROOT / "security-readiness/10-decision/onyx-launch-decision.md"
RESIDUAL_RISK_MD = ROOT / "security-readiness/10-decision/onyx-residual-risk-register.md"
OUT = ROOT / "security-readiness/dashboard/dashboard-data.json"


def load_json(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text())


def get_git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip()
    except Exception:
        return "UNKNOWN"


def extract_bullets(path: Path, heading: str):
    if not path.exists():
        return []
    lines = path.read_text().splitlines()
    out = []
    in_section = False
    for line in lines:
        if line.startswith("## "):
            in_section = line.strip() == f"## {heading}"
            continue
        if in_section:
            if line.startswith("## "):
                break
            if line.strip().startswith(("- ", "1. ", "2. ", "3. ")):
                out.append(line.strip())
    return out


def map_failed_item_status(item: dict) -> str:
    evidence_file = item.get("expected_file")
    if evidence_file and not (ROOT / evidence_file).exists():
        return "Missing"

    observed = str(item.get("observed", "")).strip().upper()
    if observed == "BLOCKED":
        return "Blocked"
    if item.get("id") == "prompt_injection_boundary_tests" and observed in {"", "NONE", "NULL"}:
        return "Blocked"
    if observed == "FAILED" or item.get("status") == "FAILED":
        return "Failed"
    if observed == "PARTIAL":
        return "Partial"
    return "Failed"


def item_status(validation, item_id):
    if not validation:
        return "Missing"

    for item in validation.get("checked", []):
        if item.get("id") == item_id:
            return "Passed"

    for item in validation.get("skipped", []):
        if item.get("id") == item_id:
            return "Skipped"

    for item in validation.get("failed", []):
        if item.get("id") == item_id:
            return map_failed_item_status(item)

    for item in validation.get("missing", []):
        if item.get("id") == item_id:
            return "Missing"

    return "Missing"


validation = load_json(VALIDATION)
launch = load_json(LAUNCH_GATE)

counts = (validation or {}).get("counts", {})
required_total = counts.get("required_total", 0)
complete = counts.get("complete", 0)
completeness_pct = round((complete / required_total) * 100, 1) if required_total else 0

missing = set((launch or {}).get("reasons", []))
unknowns = extract_bullets(RESIDUAL_RISK_MD, "Open Unknowns")
next_steps = extract_bullets(DECISION_MD, "Required Actions Before Re-evaluation")

payload = {
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "overall_launch_gate_decision": (launch or {}).get("decision", "NOT_ENOUGH_EVIDENCE"),
    "active_launch_mode": (validation or {}).get("active_launch_mode", "RAG_ONLY"),
    "readiness_score": completeness_pct,
    "evidence_completeness": {
        "status": (validation or {}).get("status", "INCOMPLETE"),
        "allow_go": (validation or {}).get("allow_go", False),
        "complete": complete,
        "required_total": required_total,
        "percent": completeness_pct,
    },
    "control_status": "Missing" if completeness_pct < 100 else "Verified",
    "tests": {
        "pure_control_layer": item_status(validation, "pure_control_unit_tests"),
        "citation_source_leakage_dependency_light": item_status(validation, "citation_source_leakage_dependency_light"),
        "retrieval_authorization": item_status(validation, "retrieval_authorization_tests"),
        "citation_leakage": item_status(validation, "citation_leakage_tests"),
        "prompt_injection_dependency_light_boundary": item_status(validation, "prompt_injection_boundary_dependency_light"),
        "prompt_injection_full_runtime_red_team": item_status(validation, "prompt_injection_boundary_tests"),
        "tool_authorization_dependency_light": item_status(validation, "tool_authorization_dependency_light"),
        "tool_authorization": item_status(validation, "tool_authorization_tests"),
        "tool_runtime_wiring": item_status(validation, "tool_runtime_wiring_verified"),
        "mcp_tool_hardening": item_status(validation, "mcp_tool_hardening_verified"),
    },
    "tooling_skip_visibility": [
        item for item in (validation or {}).get("skipped", [])
        if item.get("id") in {"tool_authorization_tests", "tool_runtime_wiring_verified", "mcp_tool_hardening_verified"}
    ],
    "evidence_scope": {
        "pure_control_layer": {
            "status": item_status(validation, "pure_control_unit_tests"),
            "evidence_type": "limited unit evidence",
            "runtime_proof": "No",
            "launch_gate_effect": "Improves confidence but does not unblock GO",
        },
        "runtime_retrieval_authorization": item_status(validation, "retrieval_authorization_tests"),
        "citation_source_leakage_dependency_light": {
            "status": item_status(validation, "citation_source_leakage_dependency_light"),
            "evidence_type": "dependency-light test evidence",
            "runtime_proof": "No",
            "launch_gate_effect": "Partial positive evidence only; GO remains blocked without full runtime citation leakage PASS",
        },
        "full_runtime_citation_leakage": item_status(validation, "citation_leakage_tests"),
        "prompt_injection_dependency_light_boundary": {
            "status": item_status(validation, "prompt_injection_boundary_dependency_light"),
            "evidence_type": "dependency-light boundary test evidence",
            "runtime_proof": "No",
            "launch_gate_effect": "Partial positive evidence only; GO remains blocked until full runtime prompt-injection/red-team evidence is PASS",
        },
        "full_runtime_prompt_injection_red_team": item_status(validation, "prompt_injection_boundary_tests"),
        "tool_authorization_dependency_light": {
            "status": item_status(validation, "tool_authorization_dependency_light"),
            "evidence_type": "dependency-light tool authorization test evidence",
            "runtime_proof": "No",
            "launch_gate_effect": "Partial positive evidence only; RAG_PLUS_TOOLS remains blocked until full tool authorization and runtime wiring evidence are PASS",
        },
        "tool_runtime_wiring": item_status(validation, "tool_runtime_wiring_verified"),
    },
    "audit_logging_status": item_status(validation, "audit_events_generated"),
    "runtime_tracing_status": item_status(validation, "runtime_traces_generated"),
    "open_critical_risks": "Verified" if item_status(validation, "no_critical_open_risks") == "Passed" else "Open",
    "residual_risks": {
        "status": item_status(validation, "residual_risk_documented"),
        "open_unknowns": unknowns,
    },
    "last_evidence_timestamp": (validation or {}).get("generated_at", "UNKNOWN"),
    "git_commit": get_git_commit(),
    "explanation": {
        "status": (launch or {}).get("decision", "NOT_ENOUGH_EVIDENCE"),
        "summary": "NOT ENOUGH EVIDENCE: launch is blocked until missing critical evidence is produced.",
        "reasons": (launch or {}).get("reasons", []) + list(missing),
        "required_actions": next_steps,
    },
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(payload, indent=2) + "\n")
print(f"Wrote {OUT}")
