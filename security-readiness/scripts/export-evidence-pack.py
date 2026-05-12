#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

SECRET_NAME_RE = re.compile(r"(KEY|TOKEN|SECRET|PASSWORD|PWD)", re.IGNORECASE)


def git_commit() -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Export normalized evidence into structured evidence pack")
    p.add_argument("--input", required=True, help="Normalized evidence JSON")
    p.add_argument("--output-dir", required=True, help="Output directory for evidence pack")
    p.add_argument("--manifest-name", default="evidence-pack-manifest.json")
    return p.parse_args()


def redact_environment() -> dict:
    redacted = {}
    for k, v in os.environ.items():
        redacted[k] = "[REDACTED]" if SECRET_NAME_RE.search(k) else v
    return redacted


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    args = parse_args()
    records = json.loads(Path(args.input).read_text(encoding="utf-8"))

    out_dir = Path(args.output_dir)
    artifacts_dir = out_dir / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    exported = []
    for rec in records:
        rec_copy = dict(rec)
        src = Path(rec["artifact_path"])
        if rec.get("status") == "Present" and src.exists() and src.is_file():
            dst = artifacts_dir / src.name
            shutil.copy2(src, dst)
            rec_copy["exported_artifact_path"] = str(dst)
        else:
            rec_copy["exported_artifact_path"] = None
        exported.append(rec_copy)

    env_manifest = out_dir / "environment-manifest-redacted.json"
    env_manifest.write_text(json.dumps(redact_environment(), indent=2) + "\n", encoding="utf-8")

    manifest = {
        "created_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "git_commit": git_commit(),
        "input_normalized": args.input,
        "environment_manifest": str(env_manifest),
        "environment_manifest_sha256": sha256(env_manifest),
        "records": exported,
    }

    manifest_path = out_dir / args.manifest_name
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"exported evidence pack to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
