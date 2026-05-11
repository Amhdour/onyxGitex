#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

REQUIRED_KEYS = [
    "artifact_path",
    "artifact_hash_sha256",
    "timestamp_utc",
    "git_commit",
    "command",
    "status",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize evidence records")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    normalized = []

    for record in records:
        item = {key: record.get(key) for key in REQUIRED_KEYS}
        if item["status"] not in {"Verified", "Missing", "Incomplete"}:
            item["status"] = "Incomplete"

        if item["status"] == "Verified" and any(item.get(k) in (None, "") for k in REQUIRED_KEYS):
            item["status"] = "Incomplete"

        normalized.append(item)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(normalized, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(normalized)} normalized records to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
