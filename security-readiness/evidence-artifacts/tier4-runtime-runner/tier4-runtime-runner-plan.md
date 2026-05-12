# Tier 4 Runtime Runner Plan

Date (UTC): 2026-05-12  
Launch posture: **NOT_ENOUGH_EVIDENCE** (preserved)

## Scope
Build a reproducible backend/runtime execution path for the three Tier 4 blocker suites:
1. retrieval_authorization_tests
2. citation_leakage_tests
3. prompt_injection_boundary_tests

## Inputs inspected
- Docker Compose definitions under `deployment/docker_compose/`
- Backend dependency lock files (`pyproject.toml`, `uv.lock`)
- Existing backend test guidance (`backend/tests/README.md`)
- Runtime unblocking artifacts in `security-readiness/evidence-artifacts/runtime-unblocking/`
- Existing readiness scripts in `security-readiness/scripts/`

## Execution model
1. Preflight checks: python, lock/config files, docker/docker compose availability, writable artifact paths.
2. Service readiness checks: `docker compose ... ps` for runtime dependency visibility.
3. Suite execution attempts:
   - Retrieval authorization runtime command
   - Citation leakage runtime command
   - Prompt-injection boundary runtime/red-team command
4. Persist stdout/stderr per suite in timestamped run folder.
5. Record blocked conditions exactly; do not infer PASS from partial data.

## Guardrails
- No fake PASS artifacts.
- No blocker closure from runner-only evidence.
- No launch gate change to GO.
- If Docker/devcontainer unavailable, mark blocker as blocked and capture exact reason.
