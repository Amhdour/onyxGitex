#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED_CATEGORIES = {
    "unit_test_output",
    "integration_test_output",
    "audit_log",
    "runtime_trace",
    "policy_decision_log",
    "leak_marker_scan",
    "dashboard_export",
    "launch_gate_result",
    "environment_manifest_redacted",
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Validate evidence completeness")
    p.add_argument("--normalized-input", required=True)
    p.add_argument("--required-artifacts", required=True)
    p.add_argument("--summary-output", required=True)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    records = json.loads(Path(args.normalized_input).read_text(encoding="utf-8"))
    registry = json.loads(Path(args.required_artifacts).read_text(encoding="utf-8"))

    by_id = {r["artifact_id"]: r for r in records}
    failures = []

    for item in registry:
        record = by_id.get(item["artifact_id"])
        if not record:
            failures.append({"artifact_id": item["artifact_id"], "status": "Missing", "reason": "No record found"})
            continue
        if record.get("status") != "Present":
            failures.append({"artifact_id": item["artifact_id"], "status": record.get("status"), "reason": "Artifact not present"})

    present_categories = {r.get("artifact_type") for r in records}
    missing_categories = sorted(REQUIRED_CATEGORIES - present_categories)
    for cat in missing_categories:
        failures.append({"artifact_id": f"CATEGORY::{cat}", "status": "Missing", "reason": "Required category absent from records"})

    result = "PASS" if not failures else "INCOMPLETE"
    summary = {
        "total_required_artifacts": len(registry),
        "total_records": len(records),
        "missing_categories": missing_categories,
        "failures": failures,
        "result": result,
    }

    out = Path(args.summary_output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
