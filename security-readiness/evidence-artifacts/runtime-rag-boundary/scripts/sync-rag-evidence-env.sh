#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
OUT_DIR="$ROOT_DIR/security-readiness/evidence-artifacts/runtime-rag-boundary"
OUT_FILE="$OUT_DIR/dependency-sync-output.txt"
STATUS_FILE="$OUT_DIR/dependency-sync-status.txt"
IMPORT_FILE="$OUT_DIR/dependency-import-check.txt"
SELECTED_PYTHON="3.12"
SYNC_CMD="uv sync --python 3.12 --group backend --group dev"

mkdir -p "$OUT_DIR"
: > "$OUT_FILE"

{
  echo "timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "git_commit=$(git -C "$ROOT_DIR" rev-parse HEAD)"
  echo "uv_version=$(uv --version 2>&1 || echo UV_NOT_AVAILABLE)"
  echo "python_version=$(python --version 2>&1 || echo PYTHON_NOT_AVAILABLE)"
  echo "selected_python_version=$SELECTED_PYTHON"
  echo "command_attempted=$SYNC_CMD"
  echo
} >> "$OUT_FILE"

set +e
(
  cd "$ROOT_DIR"
  eval "$SYNC_CMD"
) >> "$OUT_FILE" 2>&1
sync_rc=$?
set -e

if [[ $sync_rc -ne 0 ]]; then
  sync_text="$(tr '[:upper:]' '[:lower:]' < "$OUT_FILE")"
  status="BLOCKED_DEPENDENCY_UNKNOWN"

  if [[ "$sync_text" =~ (tunnel|timeout|timed\ out|connection|dns|tls|proxy|network|download\ failed|failed\ to\ fetch) ]]; then
    status="BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD"
  elif [[ "$sync_text" =~ (401|403|not\ authorized|forbidden|private\ index|authentication) ]]; then
    status="BLOCKED_PACKAGE_INDEX"
  elif [[ "$sync_text" =~ (no\ matching\ distribution|incompatible|resolution\ failed|solver\ failed) ]]; then
    status="BLOCKED_PACKAGE_RESOLUTION"
  fi

  echo "$status" > "$STATUS_FILE"
  exit 1
fi

echo "SYNC_PASS" > "$STATUS_FILE"

{
  echo "timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  uv run --python "$SELECTED_PYTHON" python - <<'PY'
import importlib.util
import sys
mods = ["fastapi_users", "numpy", "onnxruntime", "pytest"]
print("python_executable=", sys.executable)
print("python_version=", sys.version)
for mod in mods:
    print(f"{mod}_available=", importlib.util.find_spec(mod) is not None)
PY
} > "$IMPORT_FILE" 2>&1

{
  echo
  echo "# Import checks"
  cat "$IMPORT_FILE"
} >> "$OUT_FILE"
