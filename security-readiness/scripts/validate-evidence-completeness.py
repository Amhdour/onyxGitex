#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate evidence completeness")
    parser.add_argument("--normalized-input", required=True)
    parser.add_argument("--required-artifacts", required=True)
    parser.add_argument("--summary-output", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = json.loads(Path(args.normalized_input).read_text(encoding="utf-8"))
    registry = json.loads(Path(args.required_artifacts).read_text(encoding="utf-8"))

    by_path = {r.get("artifact_path"): r for r in records}
    failures = []

    for req in registry:
        if not req.get("required", True):
            continue
        p = req["artifact_path"]
        rec = by_path.get(p)
        if not rec:
            failures.append({"artifact_path": p, "status": "Missing", "reason": "No record found"})
            continue
        if rec.get("status") != "Verified":
            failures.append({"artifact_path": p, "status": rec.get("status", "Incomplete"), "reason": "Not Verified"})

    summary = {
        "total_required": sum(1 for r in registry if r.get("required", True)),
        "failures": failures,
        "result": "PASS" if not failures else "INCOMPLETE",
    }
    out = Path(args.summary_output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
