#!/usr/bin/env python3
import argparse
import datetime as dt
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check evidence freshness")
    parser.add_argument("--input", required=True)
    parser.add_argument("--max-age-days", type=int, default=30)
    return parser.parse_args()


def parse_ts(v: str) -> dt.datetime:
    return dt.datetime.fromisoformat(v.replace("Z", "+00:00"))


def main() -> int:
    args = parse_args()
    now = dt.datetime.now(dt.timezone.utc)
    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    stale_count = 0
    for rec in records:
        status = rec.get("status")
        ts = rec.get("timestamp_utc")
        if status != "Verified" or not ts:
            print(f"{rec.get('artifact_path')}: skipped freshness check (status={status})")
            continue
        age_days = (now - parse_ts(ts)).total_seconds() / 86400
        if age_days > args.max_age_days:
            stale_count += 1
            print(f"{rec.get('artifact_path')}: Stale ({age_days:.1f} days)")
        else:
            print(f"{rec.get('artifact_path')}: Fresh ({age_days:.1f} days)")

    if stale_count:
        print(f"stale evidence found: {stale_count}")
        return 1
    print("all verified evidence is fresh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
