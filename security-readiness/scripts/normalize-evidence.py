#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
from pathlib import Path

REQUIRED_FIELDS = [
    "artifact_id", "control_id", "artifact_path", "artifact_type", "generated_by_command",
    "timestamp", "git_commit", "hash_sha256", "status", "related_test", "related_control",
    "launch_gate_relevance",
]

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*[^\s,]+"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Normalize and sanitize evidence records")
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    return p.parse_args()


def stale(ts: str) -> bool:
    try:
        d = dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return True
    return (dt.datetime.now(dt.timezone.utc) - d) > dt.timedelta(days=30)


def redact(value: str) -> str:
    out = value
    for pattern in SECRET_PATTERNS:
        out = pattern.sub("[REDACTED]", out)
    return out


def main() -> int:
    args = parse_args()
    records = json.loads(Path(args.input).read_text(encoding="utf-8"))
    normalized = []

    for rec in records:
        item = {k: rec.get(k) for k in REQUIRED_FIELDS}
        for field in ("generated_by_command", "related_test", "related_control"):
            item[field] = redact(item.get(field) or "")

        status = item.get("status")
        if status == "Present" and stale(item.get("timestamp") or ""):
            status = "Stale"

        path = Path(item.get("artifact_path") or "")
        if status == "Present" and path.exists() and path.is_file() and item.get("artifact_type", "").endswith("_output"):
            text = path.read_text(encoding="utf-8", errors="ignore").lower()
            if "failed" in text or "error" in text:
                status = "Failed"

        if status not in {"Present", "Missing", "Failed", "Stale"}:
            status = "Missing"

        if status == "Present" and any(not item.get(k) for k in REQUIRED_FIELDS if k != "hash_sha256"):
            status = "Missing"

        item["status"] = status
        normalized.append(item)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(normalized, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(normalized)} normalized records to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
