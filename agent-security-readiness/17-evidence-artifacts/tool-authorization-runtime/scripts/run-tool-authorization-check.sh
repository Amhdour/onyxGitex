#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
OUT_DIR="$ROOT_DIR/agent-security-readiness/17-evidence-artifacts/tool-authorization-runtime"
STATUS_FILE="$OUT_DIR/runtime-status.txt"
POLICY_FILE="$ROOT_DIR/agent-security-readiness/05-policy-as-code/tool-authorization-policy.rego"
TEST_FILE="$ROOT_DIR/agent-security-readiness/05-policy-as-code/tool-authorization-policy_test.rego"

mkdir -p "$OUT_DIR"
echo "RUNNING" > "$STATUS_FILE"
date -u +"%Y-%m-%dT%H:%M:%SZ" > "$OUT_DIR/timestamp.txt"
git -C "$ROOT_DIR" rev-parse HEAD > "$OUT_DIR/git-commit.txt"
echo "opa test agent-security-readiness/05-policy-as-code -v" > "$OUT_DIR/test-command.txt"

if ! command -v opa >/dev/null 2>&1; then
  echo "OPA_NOT_AVAILABLE" | tee "$OUT_DIR/policy-test-output.txt"
  echo "BLOCKED" > "$STATUS_FILE"
  exit 1
fi

if [[ ! -f "$POLICY_FILE" || ! -f "$TEST_FILE" ]]; then
  echo "TESTS_NOT_FOUND" | tee "$OUT_DIR/policy-test-output.txt"
  echo "TESTS_NOT_FOUND" > "$STATUS_FILE"
  exit 1
fi

opa test "$ROOT_DIR/agent-security-readiness/05-policy-as-code" -v 2>&1 | \
  sed -E 's#((api[_-]?key|token|password|secret|client[_-]?secret|private[_-]?key|cookie|bearer)[[:space:]]*[:=][[:space:]]*)[^[:space:]]+#\1[REDACTED]#Ig' | \
  tee "$OUT_DIR/policy-test-output.txt"

echo "COMPLETED" > "$STATUS_FILE"
