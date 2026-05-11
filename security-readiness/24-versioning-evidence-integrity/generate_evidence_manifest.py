#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def git_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate evidence integrity manifest")
    parser.add_argument("files", nargs="+", help="Evidence file paths to hash")
    parser.add_argument("--output", required=True, help="Output JSON manifest path")
    parser.add_argument("--command", required=True, help="Command used to produce evidence")
    parser.add_argument("--test-status", required=True, help="Test status (e.g. pass/fail/skip/na)")
    parser.add_argument("--evidence-type", required=True, help="Evidence type label")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    commit = git_commit()
    timestamp = dt.datetime.now(dt.timezone.utc).isoformat()

    entries = []
    for raw_path in args.files:
        path = Path(raw_path)
        if not path.exists() or not path.is_file():
            print(f"error: path is missing or not a file: {raw_path}", file=sys.stderr)
            return 2

        entries.append(
            {
                "file_path": str(path.as_posix()),
                "hash_sha256": sha256_file(path),
                "timestamp_utc": timestamp,
                "git_commit": commit,
                "command_used": args.command,
                "test_status": args.test_status,
                "evidence_type": args.evidence_type,
            }
        )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)
        f.write("\n")

    print(f"wrote manifest with {len(entries)} entries to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
