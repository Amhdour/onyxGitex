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


## Tier 4 Runtime Environment Repair (2026-05-12)
- Backend auth modules (`fastapi-users`, `fastapi-users-db-sqlalchemy`) are provided by root `pyproject.toml` backend dependency group.
- Repo-supported dependency setup command identified from `backend/requirements/README.md`: `uv sync --no-default-groups --group backend --group dev`.
- In this host, dependency sync remained blocked (cp314 wheel mismatch for `onnxruntime`, and follow-up `--python 3.11` runtime download tunnel failure).
- Collection-only command remained pre-collection blocked due missing `dotenv` in system interpreter environment.
- Launch gate remains **NOT_ENOUGH_EVIDENCE**; no Tier 4 suite PASS claim.
