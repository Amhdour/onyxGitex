# Tier 4 Runtime Command Discovery

Date (UTC): 2026-05-12
Launch gate posture: **NOT_ENOUGH_EVIDENCE**

## Scope inspected
- `backend/tests/integration/tests/chat/`
- `security-readiness/evidence-artifacts/test-results/`
- `security-readiness/evidence-artifacts/runtime-unblocking/`
- `security-readiness/scripts/run-tier4-runtime-tests.sh`

## Findings

### 1) retrieval_authorization_tests
- Suite ID: `retrieval_authorization_tests`
- Exact test path (exists): `backend/tests/integration/tests/chat/test_retrieval_authorization_runtime.py`
- Exact pytest command: `pytest -q backend/tests/integration/tests/chat/test_retrieval_authorization_runtime.py`
- Required services: docker + docker compose, Postgres, Redis, Vespa/OpenSearch, backend API stack
- Required fixtures: integration environment fixtures from `backend/tests/integration/conftest.py` plus seeded docs/users with mixed authorization
- Expected output artifact: `security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json`
- Current test exists: `true`
- Runtime status: **BLOCKED/SKIPPED** until Tier 4 runtime environment/fixtures are provisioned.

### 2) citation_leakage_tests
- Suite ID: `citation_leakage_tests`
- Exact test path (exists): `backend/tests/integration/tests/chat/test_citation_leakage_runtime.py`
- Exact pytest command: `pytest -q backend/tests/integration/tests/chat/test_citation_leakage_runtime.py`
- Required services: docker + docker compose, Postgres, Redis, Vespa/OpenSearch, backend API stack
- Required fixtures: integration environment fixtures from `backend/tests/integration/conftest.py` plus seeded docs/users with mixed authorization
- Expected output artifact: `security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`
- Current test exists: `true`
- Runtime status: **BLOCKED/SKIPPED** until Tier 4 runtime environment/fixtures are provisioned.

### 3) prompt_injection_boundary_tests
- Suite ID: `prompt_injection_boundary_tests`
- Exact test path (exists): `backend/tests/integration/tests/chat/test_prompt_injection_boundary_runtime.py`
- Exact pytest command: `pytest -q backend/tests/integration/tests/chat/test_prompt_injection_boundary_runtime.py`
- Required services: docker + docker compose, Postgres, Redis, Vespa/OpenSearch, backend API stack, prompt-routing/runtime pipeline
- Required fixtures: integration fixtures from `backend/tests/integration/conftest.py`, adversarial prompt corpus, retrieval ACL fixtures, audit log capture fixture
- Expected output artifact: `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`
- Current test exists: `true`
- Runtime status: **BLOCKED/SKIPPED** until Tier 4 runtime environment/fixtures are provisioned.

## Launch Gate Guardrail
- Validator blockers are not closed by these skeletons.
- Launch gate remains **NOT_ENOUGH_EVIDENCE**.
- Status is not upgraded to GO without real runtime assertions and evidence artifacts.
