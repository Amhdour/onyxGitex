# Runtime-Adjacent Retrieval Guard Isolated Test Evidence

- Date (UTC): 2026-05-12
- Scope: Runtime-adjacent evidence only for `_build_index_filters` retrieval guard behavior.
- Harness strategy: Test file placed outside `backend/tests` to avoid loading `backend/tests/conftest.py`.

## Verification of Original Blocker Context

- Inspected `backend/tests/conftest.py` and observed it does **not** import `fastapi_users` directly.
- New isolated run confirmed a **narrower blocker** occurs earlier in backend module imports: `fastapi_users_db_sqlalchemy` from `backend/onyx/db/models.py`.

## Command Executed

See `isolated-test-command.txt`.

## Output

See `isolated-test-output.txt`.

## Result Classification

- runtime_adjacent_evidence: `BLOCKED` (not PASS)
- blocker_status: `NARROWER_BLOCKER_IDENTIFIED`
- blocking_dependency: `fastapi_users_db_sqlalchemy`
- full_runtime_evidence: `NOT_PASS`
- launch_gate_status: `NOT_ENOUGH_EVIDENCE`

## Evidence Confidence

- Verified: isolated path avoids `backend/tests/conftest.py` loading.
- Verified: import fails during module collection due to missing `fastapi_users_db_sqlalchemy`.
- Unknown: runtime-adjacent behavior assertions for allow/deny/fail-closed/audit until dependency stubbing is added before backend imports.
