# Onyx RAG Entrypoints

## Confirmed entrypoints

1. `backend/onyx/server/query_and_chat/chat_backend.py`
   - Functionality: `/chat` router, request validation/dependencies, streaming + session lifecycle.
   - Evidence: imports of `handle_multi_model_stream`, `handle_stream_message_objects`, `create_chat_session_from_request`, and chat/session DB APIs.
   - Confidence: **Confirmed**.

2. `backend/onyx/server/query_and_chat/query_backend.py`
   - Functionality: `/query` and `/admin/search` retrieval APIs.
   - Evidence: `build_access_filters_for_user`, vector-db retrieval path (`admin_retrieval`, `random_retrieval`).
   - Confidence: **Confirmed**.

3. `backend/onyx/context/search/` (referenced by query backend)
   - Functionality: filter models, preprocessing, search documents shaping.
   - Evidence: imports `IndexFilters`, `SearchDoc`, `build_access_filters_for_user` in query API.
   - Confidence: **Partially Confirmed** (full call graph not exhaustively followed).

## Gaps / needs verification

- How each index backend (OpenSearch/Vespa/etc.) applies ACL filters at query time: **Needs Verification**.
- Whether all chat paths (including tool-augmented and deep-research branches) share identical access control semantics: **Needs Verification**.
