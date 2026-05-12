# Tier 4 Runtime Command Discovery

Date (UTC): 2026-05-12
Launch gate posture: **NOT_ENOUGH_EVIDENCE**

## Scope inspected
- `backend/tests/`
- `backend/tests/integration/`
- `backend/tests/unit/`
- `security-readiness/evidence-artifacts/test-results/`
- `security-readiness/evidence-artifacts/runtime-unblocking/`
- `security-readiness/scripts/run-tier4-runtime-tests.sh`

## Findings

### 1) retrieval_authorization_tests
- Suite ID: `retrieval_authorization_tests`
- Exact test path (exists): `backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Exact pytest command: `pytest -q backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Required services: none (unit level)
- Required fixtures: pytest unit fixtures from `backend/tests/conftest.py` and local module fixtures in the test file
- Expected output artifact: `security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json`
- Current test exists: `true`
- Reason it cannot be run yet: Tier 4 runtime environment prerequisites (containerized backend/runtime dependencies) are currently unavailable in this host; this command is retained as a dependency-light control check, not full runtime proof.

### 2) citation_leakage_tests
- Suite ID: `citation_leakage_tests`
- Exact test path (full runtime): **missing**
- TODO pytest command (when created): `pytest -q backend/tests/integration/tests/chat/test_citation_leakage_runtime.py`
- Required services: docker + docker compose, Postgres, Redis, Vespa/OpenSearch, backend API stack
- Required fixtures: integration environment fixtures from `backend/tests/integration/conftest.py` plus seeded docs/users with mixed authorization
- Expected output artifact: `security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`
- Current test exists: `false`
- Test file that must be created: `backend/tests/integration/tests/chat/test_citation_leakage_runtime.py`
- Reason it cannot be run yet: no exact Tier 4 runtime integration test file exists for citation leakage in `backend/tests/integration/tests/`; existing dependency-light evidence test under `security-readiness/evidence-artifacts/citation-source-leakage/test_citation_source_leakage.py` is not full runtime coverage.

### 3) prompt_injection_boundary_tests
- Suite ID: `prompt_injection_boundary_tests`
- Exact test path (full runtime): **missing**
- TODO pytest command (when created): `pytest -q backend/tests/integration/tests/chat/test_prompt_injection_boundary_runtime.py`
- Required services: docker + docker compose, Postgres, Redis, Vespa/OpenSearch, backend API stack, prompt-routing/runtime pipeline
- Required fixtures: integration fixtures from `backend/tests/integration/conftest.py`, adversarial prompt corpus, retrieval ACL fixtures, audit log capture fixture
- Expected output artifact: `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`
- Current test exists: `false`
- Test file that must be created: `backend/tests/integration/tests/chat/test_prompt_injection_boundary_runtime.py`
- Reason it cannot be run yet: no exact Tier 4 runtime integration test file exists for prompt-injection boundary in `backend/tests/integration/tests/`; existing dependency-light policy test under `security-readiness/evidence-artifacts/prompt-injection-boundary/test_prompt_injection_boundary.py` is not full runtime/red-team evidence.
