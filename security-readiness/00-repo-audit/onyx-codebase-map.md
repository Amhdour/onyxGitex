# Onyx Codebase Map (Phase 1 Repository Audit)

Date: 2026-05-11 (UTC)
Scope: static repository audit only; no runtime validation.

## High-level subsystem map

- **AuthN/AuthZ**: `backend/onyx/auth/`, `backend/onyx/server/auth/`, and permission enforcement in route dependencies. Confidence: **Confirmed**.
- **Core API routing**: `backend/onyx/server/` with feature routers and `query_and_chat` entrypoints. Confidence: **Confirmed**.
- **Data models**: `backend/onyx/db/models.py` includes `User`, `UserGroup`, `Document`, `DocumentSet`, `ChatSession`, `Tool`, `MCP*` entities. Confidence: **Confirmed**.
- **RAG and retrieval**: `backend/onyx/context/search/`, `backend/onyx/server/query_and_chat/`, `backend/onyx/document_index/`. Confidence: **Partially Confirmed** (query pipeline entrypoints confirmed; all downstream index backends not exhaustively traced).
- **Tooling + MCP**: `backend/onyx/tools/`, `backend/onyx/server/features/tool/`, `backend/onyx/server/features/mcp/`. Confidence: **Confirmed**.
- **Observability**: `backend/onyx/server/metrics/`, `backend/onyx/utils/logger.py`, `backend/onyx/tracing/`. Confidence: **Partially Confirmed**.
- **Connector ingestion**: `backend/onyx/connectors/`, background tasks/redis orchestration in `backend/onyx/redis/` and celery layers. Confidence: **Partially Confirmed**.
- **Deployment**: `deployment/docker_compose/`, `deployment/helm/`, `deployment/terraform/`, backend Dockerfiles. Confidence: **Confirmed**.

## Primary entrypoint files (quick index)

- Chat runtime endpoints: `backend/onyx/server/query_and_chat/chat_backend.py`
- Query/retrieval API: `backend/onyx/server/query_and_chat/query_backend.py`
- Access filtering logic: `backend/onyx/db/document_access.py`
- Permissions dependency: `backend/onyx/auth/permissions.py`
- Tool admin/user APIs: `backend/onyx/server/features/tool/api.py`
- MCP server + auth/tool discovery APIs: `backend/onyx/server/features/mcp/api.py`
- Data model hub: `backend/onyx/db/models.py`

## Coverage statement

This map is intentionally phase-scoped and does **not** assert production security properties. It identifies where controls likely live and where Phase 2 should verify behavior with tests and runtime evidence.
