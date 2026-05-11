#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<USAGE
Usage: $0 --output <raw_json> --command <command_text> <artifact_path> [artifact_path...]
USAGE
}

OUTPUT=""
COMMAND_TEXT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output)
      OUTPUT="$2"; shift 2 ;;
    --command)
      COMMAND_TEXT="$2"; shift 2 ;;
    -h|--help)
      usage; exit 0 ;;
    --)
      shift; break ;;
    -* )
      echo "Unknown option: $1" >&2; usage; exit 2 ;;
    *)
      break ;;
  esac
done

if [[ -z "$OUTPUT" || -z "$COMMAND_TEXT" || $# -lt 1 ]]; then
  usage
  exit 2
fi

commit="$(git rev-parse HEAD)"
ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

mkdir -p "$(dirname "$OUTPUT")"

python3 - "$OUTPUT" "$COMMAND_TEXT" "$commit" "$ts" "$@" <<'PY'
import hashlib
import json
import pathlib
import sys

output, command, commit, ts, *paths = sys.argv[1:]
records = []
for p in paths:
    path = pathlib.Path(p)
    if path.exists() and path.is_file():
        h = hashlib.sha256(path.read_bytes()).hexdigest()
        status = "Verified"
    else:
        h = None
        status = "Missing"
    records.append({
        "artifact_path": p,
        "artifact_hash_sha256": h,
        "timestamp_utc": ts,
        "git_commit": commit,
        "command": command,
        "status": status,
    })

pathlib.Path(output).write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
print(f"wrote {len(records)} raw evidence records to {output}")
PY
