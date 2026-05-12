#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<USAGE
Usage: $0 --registry <registry_json> --output <raw_json>
USAGE
}

REGISTRY=""
OUTPUT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --registry) REGISTRY="$2"; shift 2 ;;
    --output) OUTPUT="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
done

if [[ -z "$REGISTRY" || -z "$OUTPUT" ]]; then
  usage
  exit 2
fi

commit="$(git rev-parse HEAD)"
ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

mkdir -p "$(dirname "$OUTPUT")"

python3 - "$REGISTRY" "$OUTPUT" "$commit" "$ts" <<'PY'
import hashlib
import json
import pathlib
import sys

registry_path, output_path, commit, ts = sys.argv[1:]
registry = json.loads(pathlib.Path(registry_path).read_text(encoding="utf-8"))
records = []

for item in registry:
    path = pathlib.Path(item["artifact_path"])
    status = "Missing"
    sha = None

    if path.exists() and path.is_file():
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        status = "Failed" if "fail" in path.name.lower() else "Present"

    record = {
        "artifact_id": item["artifact_id"],
        "control_id": item["control_id"],
        "artifact_path": item["artifact_path"],
        "artifact_type": item["artifact_type"],
        "generated_by_command": item.get("generated_by_command", ""),
        "timestamp": ts,
        "git_commit": commit,
        "hash_sha256": sha,
        "status": status,
        "related_test": item.get("related_test", ""),
        "related_control": item.get("related_control", ""),
        "launch_gate_relevance": item.get("launch_gate_relevance", "Informational"),
    }
    records.append(record)

pathlib.Path(output_path).write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
print(f"wrote {len(records)} records to {output_path}")
PY
