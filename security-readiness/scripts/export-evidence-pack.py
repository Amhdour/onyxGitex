#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path


def git_commit() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export evidence pack")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--command", default="python3 security-readiness/scripts/export-evidence-pack.py")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    payload = {
        "export_timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "git_commit": git_commit(),
        "command": args.command,
        "records": records,
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"exported {len(records)} records to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
