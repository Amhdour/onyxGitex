# Bypass ACL Contract Dependency-Light Evidence Summary

- Date: 2026-05-12
- Scope: Dependency-light contract tests for `enforce_bypass_acl_contract` only.
- Target: `backend/onyx/security_readiness/retrieval_guard_adapter.py::enforce_bypass_acl_contract`
- Harness: Direct pytest module under `security-readiness/evidence-artifacts/` without importing `backend/tests` conftest.

## Command Executed

```bash
PYTHONPATH=backend pytest -q security-readiness/evidence-artifacts/bypass-acl-contract/test_bypass_acl_contract.py
```

## Result

- Dependency-light test result: **PASS** (7 passed).
- Backend harness result: **BLOCKED** (unchanged from previous machine-readable status due to missing `fastapi_users`).

## Coverage in This Evidence Set

Verified via passing tests:
1. `bypass_acl=False` returns without audit event.
2. `bypass_acl=True` and `trusted_system_context=False` fails closed with `OnyxError`.
3. Denied bypass emits `retrieval.bypass_acl.deny` audit event.
4. `bypass_acl=True` and `trusted_system_context=True` is allowed.
5. Approved bypass emits `retrieval.bypass_acl.allow` audit event.
6. `actor_id` is preserved in audit event.
7. Normal user-style request cannot enable bypass without trusted context.

## Limits / Non-Claims

- This does **not** establish full runtime proof across the full backend test harness.
- Launch gate remains **NOT_ENOUGH_EVIDENCE**.
- Overall status remains bounded by partial confirmation at system level, with dependency-light evidence now passing.
