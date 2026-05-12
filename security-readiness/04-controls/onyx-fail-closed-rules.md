# Fail-Closed Rules (Retrieval Path Update)

Date: 2026-05-11
Status: Partially Confirmed

## Enforced Retrieval Rules
1. If `document_set` is requested and `user.id` is missing, retrieval authorization fails closed.
2. If `document_set` is requested and `db_session` is missing (while `bypass_acl=False`), retrieval authorization fails closed.
3. If a requested document set has no allow policy in guard policy map, authorization fails closed.
4. Denied authorization decisions stop filter construction with `OnyxErrorCode.INSUFFICIENT_PERMISSIONS`.

## Scope Notes
- Rules are enforced in `_build_index_filters` for the internal search pipeline path.
- `bypass_acl=True` callers are unchanged and out-of-scope for this control proof.

## Evidence
- Implementation: `backend/onyx/context/search/pipeline.py`
- Tests: `backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Artifacts: `security-readiness/evidence-artifacts/rag-boundary-001/`

## Remaining Gaps
- End-to-end runtime verification is pending due to environment dependency failure (`fastapi_users` missing during pytest import).
- Launch posture remains **Not Approved** until verification completes.
