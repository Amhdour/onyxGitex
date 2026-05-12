#!/usr/bin/env python3
"""Generate evidence-based launch gate decision artifacts.

This script fail-closes: missing/unknown critical evidence blocks GO.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DECISIONS = {"GO", "CONDITIONAL_GO", "NO_GO", "NOT_ENOUGH_EVIDENCE"}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run launch gate from evidence inputs")
    p.add_argument("--evidence-registry", default="security-readiness/47-evidence-automation/evidence-artifact-registry.json")
    p.add_argument("--evidence-validation", default="security-readiness/evidence-artifacts/evidence-validation/validation-result.json")
    p.add_argument("--control-test-results", default="security-readiness/evidence-artifacts/control-layer-unit-tests/control-layer-summary.md")
    p.add_argument("--red-team-results", default="security-readiness/09-evidence/onyx-red-team-results.md")
    p.add_argument("--residual-risk-register", default="security-readiness/10-decision/onyx-residual-risk-register.md")
    p.add_argument("--critical-findings", default="security-readiness/01-assessment/onyx-initial-risk-register.md")
    p.add_argument("--evidence-pack", default="security-readiness/evidence-artifacts/evidence-pack.json")
    p.add_argument("--output-dir", default="security-readiness/evidence-artifacts/launch-gate")
    return p.parse_args()


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def exists_nonempty(path: Path) -> bool:
    return path.exists() and path.stat().st_size > 0


def contains_any(path: Path, needles: list[str]) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return any(n.lower() in text for n in needles)


def main() -> int:
    args = parse_args()
    root = Path.cwd()
    out_dir = root / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()

    paths = {
        "evidence_registry": root / args.evidence_registry,
        "evidence_validation": root / args.evidence_validation,
        "control_test_results": root / args.control_test_results,
        "red_team_results": root / args.red_team_results,
        "residual_risk_register": root / args.residual_risk_register,
        "critical_findings": root / args.critical_findings,
        "evidence_pack": root / args.evidence_pack,
    }

    reasons: list[str] = []
    missing_inputs: list[str] = []
    unknown_inputs: list[str] = []

    for key, p in paths.items():
        if not exists_nonempty(p):
            missing_inputs.append(key)

    validation_status = "UNKNOWN"
    allow_go = False
    missing_evidence_ids: list[str] = []
    if paths["evidence_validation"].exists():
        v = read_json(paths["evidence_validation"])
        validation_status = str(v.get("status", "UNKNOWN"))
        allow_go = bool(v.get("allow_go", False))
        missing_evidence_ids = [m.get("id", "unknown") for m in v.get("missing", [])]
    else:
        unknown_inputs.append("evidence_validation")

    missing_identity_fail_closed_test = any("retrieval_authorization" in x or "identity" in x for x in missing_evidence_ids)
    runtime_integration_unknown = any("runtime_traces_generated" in x for x in missing_evidence_ids)

    critical_retrieval_leak = contains_any(paths["critical_findings"], ["critical retrieval leak", "cross-tenant leakage", "retrieval leak"]) and contains_any(paths["critical_findings"], ["open", "unresolved", "pending"])
    critical_open_risk = contains_any(paths["residual_risk_register"], ["critical"]) and contains_any(paths["residual_risk_register"], ["open", "unresolved", "not remediated"])
    medium_residual_risk = contains_any(paths["residual_risk_register"], ["medium"]) and not critical_open_risk

    evidence_pack_missing = "evidence_pack" in missing_inputs

    decision = "NOT_ENOUGH_EVIDENCE"

    if critical_retrieval_leak:
        decision = "NO_GO"
        reasons.append("Critical retrieval leak identified in findings.")
    elif missing_identity_fail_closed_test:
        decision = "NOT_ENOUGH_EVIDENCE"
        reasons.append("Missing fail-closed identity/retrieval authorization evidence.")
    elif evidence_pack_missing:
        decision = "NOT_ENOUGH_EVIDENCE"
        reasons.append("Missing evidence pack artifact.")
    elif critical_open_risk:
        decision = "NO_GO"
        reasons.append("Critical open residual risk without remediation evidence.")
    elif runtime_integration_unknown:
        decision = "NOT_ENOUGH_EVIDENCE"
        reasons.append("Runtime integration evidence is unknown/incomplete.")
    elif validation_status != "COMPLETE" or not allow_go:
        decision = "NOT_ENOUGH_EVIDENCE"
        reasons.append("Evidence completeness validator does not allow GO.")
    elif medium_residual_risk:
        decision = "CONDITIONAL_GO"
        reasons.append("Core evidence passes, but medium residual risks remain.")
    else:
        decision = "GO"
        reasons.append("All required evidence present and no critical open risk detected.")

    if missing_inputs:
        reasons.append(f"Missing inputs: {', '.join(missing_inputs)}")
    if unknown_inputs:
        reasons.append(f"Unknown inputs: {', '.join(unknown_inputs)}")

    assert decision in DECISIONS

    decision_inputs = {
        "generated_at": now,
        "git_commit": commit,
        "inputs": {k: str(v.relative_to(root)) for k, v in paths.items()},
        "input_exists": {k: exists_nonempty(v) for k, v in paths.items()},
        "validation_status": validation_status,
        "validation_allow_go": allow_go,
        "missing_evidence_ids": missing_evidence_ids,
        "derived_flags": {
            "critical_retrieval_leak": critical_retrieval_leak,
            "missing_identity_fail_closed_test": missing_identity_fail_closed_test,
            "evidence_pack_missing": evidence_pack_missing,
            "critical_open_risk": critical_open_risk,
            "medium_residual_risk": medium_residual_risk,
            "runtime_integration_unknown": runtime_integration_unknown,
        },
    }

    result = {
        "generated_at": now,
        "git_commit": commit,
        "decision": decision,
        "reasons": reasons,
        "uncertainty_preserved": decision != "GO",
        "validation_status": validation_status,
    }

    (out_dir / "decision-inputs.json").write_text(json.dumps(decision_inputs, indent=2) + "\n", encoding="utf-8")
    (out_dir / "launch-gate-result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    (out_dir / "timestamp.txt").write_text(now + "\n", encoding="utf-8")
    (out_dir / "git-commit.txt").write_text(commit + "\n", encoding="utf-8")

    summary = [
        "# Launch Gate Summary",
        "",
        f"- Generated at (UTC): `{now}`",
        f"- Git commit: `{commit}`",
        f"- Decision: **{decision}**",
        "",
        "## Decision Reasons",
    ]
    summary.extend([f"- {r}" for r in reasons])
    summary.extend([
        "",
        "## Rule Mapping",
        f"- Rule 1 (critical retrieval leak): `{critical_retrieval_leak}`",
        f"- Rule 2 (missing identity fail-closed test): `{missing_identity_fail_closed_test}`",
        f"- Rule 3 (missing evidence pack): `{evidence_pack_missing}`",
        f"- Rule 4 (critical open risk): `{critical_open_risk}`",
        f"- Rule 5 (medium residual risk): `{medium_residual_risk}`",
        f"- Rule 6 (all required evidence + no critical risk): `{validation_status == 'COMPLETE' and allow_go and not critical_open_risk}`",
        f"- Rule 7 (unknown runtime integration): `{runtime_integration_unknown}`",
    ])
    (out_dir / "launch-gate-summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
