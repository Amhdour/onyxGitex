# Adapter Path Coverage Evidence Summary

Date: 2026-05-12

## Scope
This artifact captures dependency-light, runtime-adjacent path coverage for:
- `backend/onyx/security_readiness/retrieval_guard_adapter.py`
- Test file: `security-readiness/evidence-artifacts/retrieval-path-coverage/test_retrieval_guard_adapter_path_cases.py`

## Adapter Path Tests (Dependency-Light)
Command:
- `PYTHONPATH=backend pytest -q security-readiness/evidence-artifacts/retrieval-path-coverage/test_retrieval_guard_adapter_path_cases.py`

Result:
- PASS (`7 passed in 1.15s`)

Covered adapter cases:
1. multiple document sets with one unauthorized set
2. access filter function returning partial access
3. mixed allow + deny audit events for mixed document sets
4. mixed allow + deny runtime traces for mixed document sets
5. `authorize_document_fn` raising `FailClosedError` converted to `OnyxError`
6. missing identity fails closed
7. missing permission context fails closed

## Blocked Backend-Harness Tests (Retained Evidence)
The full backend test path remains blocked due to missing dependency in this environment:
- Target: `backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Blocker: `ModuleNotFoundError: No module named 'fastapi_users'`

This blocker evidence is intentionally retained and not overwritten.

## Full Runtime Test Status
- Full runtime retrieval proof remains **NOT_PASS_BLOCKED**.
- Retrieval authorization overall remains **NOT_PASS**.
- Launch gate remains **NOT_ENOUGH_EVIDENCE**.

## Evidence Files
- `security-readiness/evidence-artifacts/retrieval-path-coverage/adapter-path-test-command.txt`
- `security-readiness/evidence-artifacts/retrieval-path-coverage/adapter-path-test-output.txt`
- `security-readiness/evidence-artifacts/test-results/retrieval-path-coverage-tests.json`
