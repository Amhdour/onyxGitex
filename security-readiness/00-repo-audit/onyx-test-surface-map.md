# Onyx Test Surface Map (Security-Relevant)

## Backend tests root

- `backend/tests/` with unit + daily suites. Confidence: **Confirmed**.

## Auth / access control tests

- `backend/tests/unit/onyx/auth/test_permissions.py`
- `backend/tests/unit/onyx/server/scim/test_auth.py`
- `backend/tests/unit/onyx/server/manage/test_users_directory_visibility.py`
- Confidence: **Partially Confirmed** (presence confirmed; full assertion quality not yet reviewed).

## Retrieval / document / connector tests

- Connector daily tests: `backend/tests/daily/connectors/*`
- File/doc processing tests: `backend/tests/unit/onyx/file_processing/*`
- Hierarchy/access info test: `backend/tests/unit/onyx/server/features/hierarchy/test_user_access_info.py`
- Confidence: **Partially Confirmed**.

## Chat / tools / MCP tests

- Tool packets: `backend/tests/unit/tools/test_memory_tool_packets.py`
- MCP: `backend/tests/unit/onyx/server/features/mcp/test_oauth_credentials_resolver.py`
- Confidence: **Partially Confirmed**.

## Observability tests

- Metrics tests in `backend/tests/unit/server/metrics/`.
- Prometheus instrumentation test: `backend/tests/unit/onyx/server/test_prometheus_instrumentation.py`.
- Confidence: **Confirmed**.

## Phase 2 test-depth tasks

1. Build matrix mapping controls -> exact tests -> missing scenarios.
2. Add explicit retrieval-authorization integration tests for document sets and mixed ACL sources.
3. Add chat+tool abuse-case tests for permission bypass attempts.
