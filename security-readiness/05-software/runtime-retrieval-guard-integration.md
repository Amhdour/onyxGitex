# Runtime Retrieval Guard Integration

Date: 2026-05-11
Status: Partially Confirmed

## Integration Point
- `backend/onyx/context/search/pipeline.py::_build_index_filters`

## Implemented Adapter
- Added a minimal adapter that invokes `RetrievalAuthorizationGuard.authorize_document(...)` for each requested `document_set` value before `IndexFilters` is built.
- Authorization context is derived from `user.id` (`AuthContext(user_id=...)`).
- Policy map is derived from `filter_document_set_names_by_user_access(...)` results.
- Missing identity (`user.id is None`) fails closed with `OnyxErrorCode.INSUFFICIENT_PERMISSIONS`.
- Missing document permission context (`db_session is None` while document sets are requested and ACLs are not bypassed) fails closed with `OnyxErrorCode.INSUFFICIENT_PERMISSIONS`.

## Audit / Trace
- Guard allow/deny decisions emit:
  - `AuditLogger.emit("retrieval_authorization_decision", ...)`
  - `RuntimeTracer.emit("retrieval.authorization", ...)`

## Behavior Notes
- Authorized users preserve retrieval behavior.
- Unauthorized document-set requests are denied before retrieval executes.
- `bypass_acl=True` behavior remains unchanged and skips the guard path.

## Evidence
- Targeted unit tests added:
  - `backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Test run artifact:
  - `security-readiness/evidence-artifacts/rag-boundary-001/pytest-output.txt`
- Current runtime status:
  - **Partially Confirmed** due to missing dependency (`fastapi_users`) in this execution environment.

## Launch Gate Note
- Launch decision remains **Not Approved** pending successful runtime/integration test execution with full test dependencies.
