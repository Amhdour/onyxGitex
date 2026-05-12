#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
OUT_DIR="$ROOT_DIR/security-readiness/evidence-artifacts/runtime-rag-boundary"
STATUS_FILE="$OUT_DIR/runtime-status.txt"
PYTEST_OUT="$OUT_DIR/pytest-output.txt"
DOCKER_PS_OUT="$OUT_DIR/docker-compose-ps.txt"
ENV_OUT="$OUT_DIR/env-manifest-redacted.txt"
PYTHON_VERSION_OUT="$OUT_DIR/python-version.txt"
SELECTED_PYTHON="3.12"
SYNC_STATUS_FILE="$OUT_DIR/dependency-sync-status.txt"

mkdir -p "$OUT_DIR"

date -u +"%Y-%m-%dT%H:%M:%SZ" > "$OUT_DIR/timestamp.txt"
git -C "$ROOT_DIR" rev-parse HEAD > "$OUT_DIR/git-commit.txt"
echo "NOT_RUN" > "$STATUS_FILE"

TARGET_TEST="backend/tests/integration/tests/chat/test_chat_document_set_access.py"
TEST_CMD_UV="cd backend && uv run --python 3.12 python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k \"rag or boundary or document_set or access\""
TEST_CMD_PY="cd backend && python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k \"rag or boundary or document_set or access\""

echo "$TEST_CMD_UV" > "$OUT_DIR/test-command.txt"

if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
  docker compose -f "$ROOT_DIR/docker-compose.yml" ps > "$DOCKER_PS_OUT" 2>&1 || echo "DOCKER_COMPOSE_PS_FAILED" > "$DOCKER_PS_OUT"
else
  echo "DOCKER_NOT_AVAILABLE" > "$DOCKER_PS_OUT"
fi

printenv | sort | awk -F= 'BEGIN { IGNORECASE=1 } { key=$1; val=substr($0, length(key)+2); if (key ~ /(SECRET|TOKEN|PASSWORD|PASS|API_KEY|OPENAI|ANTHROPIC|COHERE|JWT|COOKIE|SESSION|PRIVATE|CREDENTIAL|AUTH|BEARER|CLIENT_SECRET)/) print key"=[REDACTED]"; else print key"="val }' > "$ENV_OUT"

python --version > "$PYTHON_VERSION_OUT" 2>&1 || true
python -c 'import sys; print(sys.version); print(sys.executable)' >> "$PYTHON_VERSION_OUT" 2>&1 || true

python_major_minor="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
if [[ "$python_major_minor" != "$SELECTED_PYTHON" ]]; then
  echo "UNSUPPORTED_PYTHON_VERSION" > "$STATUS_FILE"
  echo "UNSUPPORTED_PYTHON_VERSION: selected=$SELECTED_PYTHON detected=$python_major_minor" > "$PYTEST_OUT"
  exit 1
fi

if [[ ! -f "$ROOT_DIR/$TARGET_TEST" ]]; then
  echo "PATH_NOT_FOUND" > "$STATUS_FILE"
  echo "PATH_NOT_FOUND: $TARGET_TEST" > "$PYTEST_OUT"
  exit 1
fi

if [[ -f "$SYNC_STATUS_FILE" ]]; then
  sync_status="$(cat "$SYNC_STATUS_FILE")"
  if [[ "$sync_status" == "BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD" ]]; then
    echo "BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD" > "$STATUS_FILE"
    echo "Dependency sync status indicates network download blocker." > "$PYTEST_OUT"
    exit 1
  elif [[ "$sync_status" =~ ^(BLOCKED_PACKAGE_RESOLUTION|BLOCKED_PACKAGE_INDEX|BLOCKED_DEPENDENCY_UNKNOWN)$ ]]; then
    echo "DEPENDENCY_SYNC_REQUIRED" > "$STATUS_FILE"
    echo "Dependency sync not complete: $sync_status" > "$PYTEST_OUT"
    exit 1
  fi
fi

RUN_WITH_UV=false
if command -v uv >/dev/null 2>&1 && [[ -f "$ROOT_DIR/.python-version" ]]; then
  RUN_WITH_UV=true
fi

set +e
if [[ "$RUN_WITH_UV" == true ]]; then
  (
    cd "$ROOT_DIR/backend"
    uv run --python "$SELECTED_PYTHON" python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k "rag or boundary or document_set or access"
  ) 2>&1 | tee "$PYTEST_OUT"
else
  echo "$TEST_CMD_PY" > "$OUT_DIR/test-command.txt"
  (
    cd "$ROOT_DIR/backend"
    python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k "rag or boundary or document_set or access"
  ) 2>&1 | tee "$PYTEST_OUT"
fi
pytest_rc=${PIPESTATUS[0]}
set -e

if [[ $pytest_rc -eq 0 ]]; then
  echo "PASS" > "$STATUS_FILE"
  exit 0
fi

if rg -q "ModuleNotFoundError: No module named 'fastapi_users'" "$PYTEST_OUT"; then
  echo "DEPENDENCY_FAILURE" > "$STATUS_FILE"
elif rg -q "ModuleNotFoundError: No module named" "$PYTEST_OUT"; then
  echo "DEPENDENCY_FAILURE" > "$STATUS_FILE"
elif rg -qi "tunnel error|failed to fetch|download failed|connection|timeout|dns|tls|proxy|network" "$PYTEST_OUT"; then
  echo "BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD" > "$STATUS_FILE"
else
  echo "FAIL" > "$STATUS_FILE"
fi

exit 1
