# Onyx Retrieval Paths

## Document and permission models

- `backend/onyx/db/models.py`
  - Classes: `Document`, `DocumentSet`, `ConnectorCredentialPair`, `ChatSession`.
  - Appears to define storage-layer entities used by retrieval and access control.
  - Confidence: **Confirmed**.

- `backend/onyx/db/document_access.py`
  - Applies connector access type + document public + external user/group ACL filters.
  - Confidence: **Confirmed**.

## Retrieval/search paths

- `backend/onyx/server/query_and_chat/query_backend.py`
  - Builds `IndexFilters` including ACL and tenant filters; invokes index retrieval.
  - Confidence: **Confirmed**.

- `backend/onyx/server/features/search/api.py` and `backend/onyx/context/search/*`
  - Likely alternate/extended search surfaces.
  - Confidence: **Partially Confirmed**.

## Citation/source generation

- Chat/tool flows reference citation processing in `backend/onyx/chat/citation_*` and tool flows (`backend/onyx/tools/fake_tools/research_agent.py`).
- Evidence: imports of `DynamicCitationProcessor`, `collapse_citations`, citation mapping handling.
- Confidence: **Partially Confirmed**.

## Connector ingestion paths

- Connectors live under `backend/onyx/connectors/`.
- Permission sync & ingestion orchestration indicators: `backend/onyx/redis/redis_connector_doc_perm_sync.py`, `redis_connector_prune.py`, `redis_connector_delete.py`.
- Confidence: **Partially Confirmed**.

## Gaps

- End-to-end ingestion -> indexing -> retrieval ACL consistency is **Unknown** until integration tests and sampled documents are validated.
