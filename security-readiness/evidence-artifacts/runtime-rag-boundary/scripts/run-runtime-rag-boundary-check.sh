#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../../.." && pwd)"
OUT_DIR="$ROOT_DIR/security-readiness/evidence-artifacts/runtime-rag-boundary"
STATUS_FILE="$OUT_DIR/runtime-status.txt"
PYTEST_OUT="$OUT_DIR/pytest-output.txt"
DOCKER_PS_OUT="$OUT_DIR/docker-compose-ps.txt"
ENV_OUT="$OUT_DIR/env-manifest-redacted.txt"

mkdir -p "$OUT_DIR"

date -u +"%Y-%m-%dT%H:%M:%SZ" > "$OUT_DIR/timestamp.txt"
git -C "$ROOT_DIR" rev-parse HEAD > "$OUT_DIR/git-commit.txt"

echo "NOT_RUN" > "$STATUS_FILE"

TARGET_TEST="backend/tests/integration/tests/chat/test_chat_document_set_access.py"
TEST_CMD="cd backend && python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k \"rag or boundary or document_set or access\""
echo "$TEST_CMD" > "$OUT_DIR/test-command.txt"

if command -v docker >/dev/null 2>&1; then
  if docker compose version >/dev/null 2>&1; then
    docker compose -f "$ROOT_DIR/docker-compose.yml" ps > "$DOCKER_PS_OUT" 2>&1 || echo "DOCKER_COMPOSE_PS_FAILED" > "$DOCKER_PS_OUT"
  else
    echo "DOCKER_COMPOSE_NOT_AVAILABLE" > "$DOCKER_PS_OUT"
  fi
else
  echo "DOCKER_NOT_AVAILABLE" > "$DOCKER_PS_OUT"
fi

printenv | sort | awk -F= '
BEGIN { IGNORECASE=1 }
{
  key=$1
  val=substr($0, length(key)+2)
  if (key ~ /(SECRET|TOKEN|PASSWORD|PASS|API_KEY|OPENAI|ANTHROPIC|COHERE|JWT|COOKIE|SESSION|PRIVATE|CREDENTIAL|AUTH|BEARER|CLIENT_SECRET)/) {
    print key"=[REDACTED]"
  } else {
    print key"="val
  }
}' > "$ENV_OUT"

if ! command -v python >/dev/null 2>&1; then
  echo "PYTHON_NOT_AVAILABLE" > "$STATUS_FILE"
  echo "python command not available" > "$PYTEST_OUT"
  exit 1
fi

if ! python -m pytest --version >/dev/null 2>&1; then
  echo "PYTEST_NOT_AVAILABLE" > "$STATUS_FILE"
  echo "python -m pytest --version failed" > "$PYTEST_OUT"
  exit 1
fi

if [[ ! -f "$ROOT_DIR/$TARGET_TEST" ]]; then
  {
    echo "PATH_NOT_FOUND: $TARGET_TEST"
    echo "Candidate tests:"
    find "$ROOT_DIR/backend/tests" -type f \( -iname '*document*access*.py' -o -iname '*document_set*.py' -o -iname '*chat*access*.py' -o -iname '*retrieval*access*.py' -o -iname '*rag*boundary*.py' \) | sed "s#$ROOT_DIR/##" | sort
  } > "$PYTEST_OUT"
  echo "PATH_NOT_FOUND" > "$STATUS_FILE"
  exit 1
fi

set +e
(
  cd "$ROOT_DIR/backend"
  python -m pytest -xv tests/integration/tests/chat/test_chat_document_set_access.py -k "rag or boundary or document_set or access"
) 2>&1 | tee "$PYTEST_OUT"
pytest_rc=${PIPESTATUS[0]}
set -e

if [[ $pytest_rc -eq 0 ]]; then
  echo "PASS" > "$STATUS_FILE"
  exit 0
fi

if rg -q "ModuleNotFoundError|ImportError|No module named|ERROR collecting|fixture .* not found" "$PYTEST_OUT"; then
  echo "DEPENDENCY_FAILURE" > "$STATUS_FILE"
else
  echo "FAIL" > "$STATUS_FILE"
fi

exit 1
