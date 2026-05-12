#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
OUT_DIR="$ROOT_DIR/security-readiness/evidence-artifacts/runtime-rag-boundary"
STATUS_FILE="$OUT_DIR/runtime-status.txt"
PYTEST_PATH="tests/integration/tests/chat/test_chat_document_set_access.py"
CMD="python -m pytest -xv ${PYTEST_PATH} -k 'rag or boundary or document_set'"

mkdir -p "$OUT_DIR"
echo "RUNNING" > "$STATUS_FILE"

date -u +"%Y-%m-%dT%H:%M:%SZ" > "$OUT_DIR/timestamp.txt"
git -C "$ROOT_DIR" rev-parse HEAD > "$OUT_DIR/git-commit.txt"
echo "$CMD" > "$OUT_DIR/test-command.txt"

if command -v docker >/dev/null 2>&1; then
  if docker compose version >/dev/null 2>&1; then
    docker compose -f "$ROOT_DIR/docker-compose.yml" ps > "$OUT_DIR/docker-compose-ps.txt" 2>&1 || echo "DOCKER_COMPOSE_PS_FAILED" > "$OUT_DIR/docker-compose-ps.txt"
  else
    echo "DOCKER_COMPOSE_NOT_AVAILABLE" > "$OUT_DIR/docker-compose-ps.txt"
  fi
else
  echo "DOCKER_NOT_AVAILABLE" > "$OUT_DIR/docker-compose-ps.txt"
fi

{
  find "$ROOT_DIR" -maxdepth 3 -type f \( -name '.env' -o -name '.env.*' -o -name '*.env' \) -print 2>/dev/null | while read -r envf; do
    echo "### ${envf#$ROOT_DIR/}"
    sed -E 's#((api[_-]?key|token|password|secret|client[_-]?secret|private[_-]?key|cookie|bearer)[[:space:]]*[:=][[:space:]]*).*#\1[REDACTED]#Ig' "$envf"
  done
} > "$OUT_DIR/env-manifest-redacted.txt" || true

if [[ -f "$ROOT_DIR/backend/$PYTEST_PATH" ]]; then
  (
    cd "$ROOT_DIR/backend"
    eval "$CMD"
  ) 2>&1 | tee "$OUT_DIR/pytest-output.txt"
  echo "PASS_OR_FAIL_CHECK_OUTPUT" > "$STATUS_FILE"
else
  echo "PATH_NOT_FOUND: backend/$PYTEST_PATH" | tee "$OUT_DIR/pytest-output.txt"
  echo "PATH_NOT_FOUND" > "$STATUS_FILE"
  exit 1
fi
