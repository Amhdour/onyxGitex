# Onyx Observability Paths

## Logging

- Broad logger pattern: `from onyx.utils.logger import setup_logger` across auth/chat/tool/MCP/search modules.
- Example files: `chat_backend.py`, `query_backend.py`, `auth/permissions.py`, `tools/built_in_tools.py`.
- Confidence: **Confirmed**.

## Tracing

- Chat backend references tracing bootstrap: `onyx.tracing.framework.create.ensure_trace`.
- Additional span usage observed in tool flows (e.g., research agent uses function spans).
- Confidence: **Partially Confirmed**.

## Metrics

- Metrics subsystem under `backend/onyx/server/metrics/` with unit tests for collectors and pipelines.
- Includes specific surfaces: indexing pipeline, opensearch search, celery tasks, permission sync.
- Confidence: **Confirmed**.

## Unknowns / gaps

- Trace propagation completeness across async task boundaries (API -> celery -> index) is **Unknown**.
- Audit-event schema completeness for policy decisions is **Unknown**.
