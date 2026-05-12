# RAG Boundary 002 Evidence Summary

Date: 2026-05-12

## Scope
Added a repository-native RAG boundary enforcement test that uses the fictional dataset at `security-readiness/test-data/rag-boundary/` and validates authorization denial behavior, fail-closed behavior, prompt injection resistance, and leakage checks across answer/citation outputs.

## Commands Run
- `pytest backend/tests/unit/onyx/security_readiness/test_control_layer.py -q`
- `rg 'LEAK_MARKER_' security-readiness/evidence-artifacts/rag-boundary-002/pytest-output.txt`

## Result
- **Partially Confirmed**.
- Test implementation exists and encodes all 10 requested scenarios.
- Runtime execution in this container is blocked by missing dependency: `fastapi_users`.
- Leak marker scan over captured pytest output found no leak markers.

## Limitation
Full test execution evidence is incomplete until the backend test environment includes required dependencies.
