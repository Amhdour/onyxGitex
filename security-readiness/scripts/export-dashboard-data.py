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


def item_status(validation, item_id):
    if not validation:
        return "Missing"
    for grp in ("checked", "missing", "failed", "skipped"):
        for item in validation.get(grp, []):
            if item.get("id") == item_id:
                if grp == "checked":
                    return "Passed"
                if grp == "skipped":
                    return "Skipped"
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
        "retrieval_authorization": item_status(validation, "retrieval_authorization_tests"),
        "citation_leakage": item_status(validation, "citation_leakage_tests"),
        "prompt_injection": item_status(validation, "prompt_injection_boundary_tests"),
        "tool_authorization": item_status(validation, "tool_authorization_tests"),
    },
    "audit_logging_status": item_status(validation, "audit_events_generated"),
    "runtime_tracing_status": item_status(validation, "runtime_traces_generated"),
    "open_critical_risks": "Missing" if item_status(validation, "no_critical_open_risks") != "Passed" else "Verified",
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
