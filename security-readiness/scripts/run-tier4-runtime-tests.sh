#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="security-readiness/evidence-artifacts/tier4-runtime-runner"
RUNS_DIR="${BASE_DIR}/runs"
TS="$(date -u +"%Y%m%dT%H%M%SZ")"
RUN_DIR="${RUNS_DIR}/${TS}"
LOG_FILE="${RUN_DIR}/runner.log"
SUMMARY_FILE="${RUN_DIR}/summary.md"

mkdir -p "${RUN_DIR}" "security-readiness/evidence-artifacts/test-results"

log() {
  echo "[$(date -u +"%Y-%m-%dT%H:%M:%SZ")] $*" | tee -a "${LOG_FILE}"
}

run_and_capture() {
  local name="$1"
  local command="$2"
  local stdout_file="${RUN_DIR}/${name}.stdout.txt"
  local stderr_file="${RUN_DIR}/${name}.stderr.txt"

  log "COMMAND ${name}: ${command}"
  set +e
  bash -lc "${command}" >"${stdout_file}" 2>"${stderr_file}"
  local exit_code=$?
  set -e
  log "EXIT ${name}: ${exit_code}"
  return ${exit_code}
}

status_preflight="BLOCKED"
status_retrieval="BLOCKED"
status_citation="BLOCKED"
status_prompt="BLOCKED"

{
  echo "# Tier 4 Runtime Runner Summary"
  echo ""
  echo "- UTC Timestamp: ${TS}"
  echo "- Git commit: $(git rev-parse HEAD 2>/dev/null || echo UNKNOWN)"
  echo "- Launch posture: NOT_ENOUGH_EVIDENCE (preserved)"
  echo ""
} > "${SUMMARY_FILE}"

log "Checking Python/backend environment"
if command -v python3 >/dev/null 2>&1 || command -v python >/dev/null 2>&1; then
  py_cmd="python3"
  command -v python3 >/dev/null 2>&1 || py_cmd="python"
  run_and_capture "python_version" "${py_cmd} --version" || true
  if [[ -f "pyproject.toml" && -f "uv.lock" ]]; then
    status_preflight="PARTIALLY_CONFIRMED"
    log "Found root pyproject.toml and uv.lock"
  else
    log "Missing root pyproject.toml or uv.lock"
  fi
else
  log "Python not found"
fi

log "Checking required services (docker compose if available)"
if command -v docker >/dev/null 2>&1; then
  run_and_capture "docker_version" "docker --version" || true
  if docker compose version >/dev/null 2>&1; then
    run_and_capture "docker_compose_ps" "docker compose -f deployment/docker_compose/docker-compose.yml -f deployment/docker_compose/docker-compose.dev.yml ps" || true
  else
    log "docker compose plugin unavailable"
  fi
else
  log "Docker not available"
fi

log "Checking writable evidence artifact paths"
for path in \
  "security-readiness/evidence-artifacts/test-results" \
  "security-readiness/evidence-artifacts/tier4-runtime-runner" \
  "${RUN_DIR}"; do
  if [[ -d "${path}" && -w "${path}" ]]; then
    echo "writable: ${path}" >> "${RUN_DIR}/path-checks.txt"
  else
    echo "not-writable: ${path}" >> "${RUN_DIR}/path-checks.txt"
    status_preflight="BLOCKED"
  fi
done

# Candidate commands can be overridden by env vars
RETRIEVAL_CMD="${RETRIEVAL_CMD:-python -m dotenv -f .vscode/.env run -- pytest backend/tests/integration/tests/permissions -k retrieval -xv}"
CITATION_CMD="${CITATION_CMD:-python -m dotenv -f .vscode/.env run -- pytest backend/tests/integration -k citation -xv}"
PROMPT_INJECTION_CMD="${PROMPT_INJECTION_CMD:-python -m dotenv -f .vscode/.env run -- pytest backend/tests/integration -k 'prompt and injection' -xv}"

if run_and_capture "retrieval_authorization" "${RETRIEVAL_CMD}"; then
  status_retrieval="PASS"
else
  status_retrieval="BLOCKED"
fi

if run_and_capture "citation_leakage" "${CITATION_CMD}"; then
  status_citation="PASS"
else
  status_citation="BLOCKED"
fi

if run_and_capture "prompt_injection_boundary" "${PROMPT_INJECTION_CMD}"; then
  status_prompt="PASS"
else
  status_prompt="BLOCKED"
fi

{
  echo "## Suite outcomes"
  echo "- retrieval_authorization_tests: ${status_retrieval}"
  echo "- citation_leakage_tests: ${status_citation}"
  echo "- prompt_injection_boundary_tests: ${status_prompt}"
  echo ""
  echo "## Guardrail"
  echo "- Runner never upgrades launch posture by itself."
  echo "- If any suite is blocked/failing, posture remains NOT_ENOUGH_EVIDENCE."
} >> "${SUMMARY_FILE}"

cat "${SUMMARY_FILE}"
