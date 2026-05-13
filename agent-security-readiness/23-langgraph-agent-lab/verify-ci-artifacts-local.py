#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

LAB = Path(__file__).resolve().parent
OUT = LAB / "ci-artifact-verification-output.json"
DEFAULT_ARTIFACT_DIR = LAB / "ci-downloaded-artifact"
REQ = [
"final-run-status.json",
"runtime-execution-report.md",
"evidence-manifest.md",
"runtime-artifacts/langgraph-dependency-check.json",
"graph-runtime-artifacts/graph-runtime-summary.json",
"graph-runtime-artifacts/graph-runtime-trace.json",
"graph-runtime-artifacts/graph-policy-decision-log.json",
"graph-runtime-artifacts/graph-audit-events.json",
"graph-runtime-artifacts/graph-memory-boundary-log.json",
"graph-runtime-artifacts/graph-sandboxed-tool-results.json",
"graph-runtime-artifacts/graph-incident-timeline.json",
]
JSON_REQ = [p for p in REQ if p.endswith('.json')]

def now():
    return datetime.now(timezone.utc).isoformat()

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact-dir", default=str(DEFAULT_ARTIFACT_DIR))
    args = ap.parse_args()
    artifact_dir = Path(args.artifact_dir)
    if not artifact_dir.is_absolute():
        artifact_dir = (Path.cwd() / artifact_dir).resolve()

    exists = artifact_dir.exists() and artifact_dir.is_dir()
    present, missing, json_validation = [], [], {}
    status = "CI_ARTIFACT_NOT_AVAILABLE"

    if exists:
        for rel in REQ:
            p = artifact_dir / rel
            if p.exists():
                present.append(rel)
            else:
                missing.append(rel)
        for rel in JSON_REQ:
            p = artifact_dir / rel
            if p.exists():
                try:
                    json.loads(p.read_text())
                    json_validation[rel] = "VALID"
                except Exception as e:
                    json_validation[rel] = f"INVALID: {e}"
        if missing:
            status = "CI_ARTIFACT_INCOMPLETE"
        elif any(v != "VALID" for v in json_validation.values()):
            status = "CI_ARTIFACT_INCOMPLETE"
        else:
            status = "CI_ARTIFACT_VERIFIED"

    out = {
        "artifact_dir": str(artifact_dir),
        "artifact_dir_exists": exists,
        "required_files_total": len(REQ),
        "required_files_present": present,
        "required_files_missing": missing,
        "json_validation": json_validation,
        "verification_status": status,
        "evidence_implication": "Direct CI artifact verification is present." if status == "CI_ARTIFACT_VERIFIED" else "CI artifact proof is not yet verified from downloaded artifacts.",
        "launch_gate_implication": "NO_GO",
        "checked_at_utc": now(),
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    if status == "CI_ARTIFACT_INCOMPLETE":
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
