# Runtime Integration Point Review: RetrievalAuthorizationGuard

Date: 2026-05-11
Scope: Runtime-path analysis only (no behavior changes)

## 1) Chat request entrypoint
- **Claim:** Primary chat runtime entrypoint is `POST /chat/send-chat-message` in `handle_send_chat_message`, which invokes `handle_stream_message_objects(...)` for both streaming and non-streaming execution paths.
- **File / Symbol:** `backend/onyx/server/query_and_chat/chat_backend.py` / `handle_send_chat_message`
- **Confidence:** **Confirmed**
- **Evidence:** Endpoint decorator `@router.post("/send-chat-message")`; function directly calls `handle_stream_message_objects(...)` in both stream and non-stream branches.

## 2) User identity source
- **Claim:** User identity is injected via FastAPI dependency (`user: User = Depends(current_chat_accessible_user)`) and propagated into chat processing and search tool construction.
- **File / Symbol:** `backend/onyx/server/query_and_chat/chat_backend.py` / `handle_send_chat_message`; `backend/onyx/chat/process_message.py` / `handle_stream_message_objects`, `_stream_chat_turn`, `construct_tools`
- **Confidence:** **Confirmed**
- **Evidence:** `handle_send_chat_message(... user: User = Depends(current_chat_accessible_user) ...)`; downstream calls pass `user=user`; `construct_tools(... user=user ...)`.

## 3) Document set or collection selection path
- **Claim:** Document set scoping comes from user-provided `internal_search_filters.document_set` and/or persona-configured document sets (`persona_search_info.document_set_names`). User-provided values override persona defaults.
- **File / Symbol:** `backend/onyx/server/query_and_chat/models.py` / `SendMessageRequest.internal_search_filters`; `backend/onyx/context/search/pipeline.py` / `_build_index_filters`
- **Confidence:** **Confirmed**
- **Evidence:** `internal_search_filters: BaseFilters | None`; in `_build_index_filters`, `document_set_filter = base_filters.document_set if ... else persona_document_sets`.

## 4) Retrieval/search function path
- **Claim:** Chat retrieval route is: chat endpoint -> `handle_stream_message_objects` -> tool construction -> search tool `_run_search_for_query` -> `search_pipeline(...)` -> `search_chunks(...)` -> index retrieval methods.
- **File / Symbol:** `backend/onyx/chat/process_message.py`; `backend/onyx/tools/tool_implementations/search/search_tool.py` / `_run_search_for_query`; `backend/onyx/context/search/pipeline.py` / `search_pipeline`; `backend/onyx/context/search/retrieval/search_runner.py` / `search_chunks`
- **Confidence:** **Confirmed**
- **Evidence:** `construct_tools(... SearchToolConfig ...)`; `_run_search_for_query` returns `search_pipeline(...)`; `search_pipeline` calls `search_chunks(...)`.

## 5) Metadata filtering path
- **Claim:** Retrieval metadata filters are assembled centrally in `_build_index_filters`, including source, time, tags, document sets, ACL filters, tenant ID, and assistant knowledge filters.
- **File / Symbol:** `backend/onyx/context/search/pipeline.py` / `_build_index_filters`
- **Confidence:** **Confirmed**
- **Evidence:** `IndexFilters(...)` populated with `source_type`, `document_set`, `time_cutoff`, `tags`, `access_control_list`, `tenant_id`, `attached_document_ids`, `hierarchy_node_ids`.

## 6) Citation/source construction path
- **Claim:** Citation mapping is built in search tool output conversion (`convert_inference_sections_to_llm_string`) and returned as `SearchDocsResponse.citation_mapping`; then persisted and re-hydrated for chat history.
- **File / Symbol:** `backend/onyx/tools/tool_implementations/search/search_tool.py` / `run`; `backend/onyx/context/search/models.py` / `SearchDocsResponse`; `backend/onyx/db/chat.py` / `translate_db_message_to_chat_message_detail`
- **Confidence:** **Confirmed**
- **Evidence:** Search tool returns `ToolResponse(rich_response=SearchDocsResponse(... citation_mapping=...))`; DB translation converts `{citation_num: db_doc_id}` to `{citation_num: document_id}` for response.

## 7) Existing authorization checks
- **Claim A:** Document-set access checks exist in retrieval filter construction via `filter_document_set_names_by_user_access`, raising `INSUFFICIENT_PERMISSIONS` for unauthorized names.
- **File / Symbol:** `backend/onyx/context/search/pipeline.py` / `_build_index_filters`; `backend/onyx/db/document_set.py` / `filter_document_set_names_by_user_access`
- **Confidence:** **Confirmed**
- **Evidence:** Unauthorized set names are computed and cause `OnyxError(OnyxErrorCode.INSUFFICIENT_PERMISSIONS, ...)`.

- **Claim B:** ACL filters are applied to retrieval via `build_access_filters_for_user` -> `IndexFilters.access_control_list`.
- **File / Symbol:** `backend/onyx/context/search/preprocessing/access_filters.py` / `build_access_filters_for_user`; `backend/onyx/context/search/pipeline.py` / `_build_index_filters`
- **Confidence:** **Confirmed**
- **Evidence:** `user_acl_filters = build_access_filters_for_user(...)`; assigned to `IndexFilters(access_control_list=user_acl_filters)`.

- **Claim C:** Post-query censoring hook exists (`fetch_ee_implementation_or_noop(... _post_query_chunk_censoring)`), enabling field-level pruning for some sources.
- **File / Symbol:** `backend/onyx/context/search/pipeline.py` / `search_pipeline`
- **Confidence:** **Partially Confirmed** (hook exists; active behavior depends on EE implementation/runtime)
- **Evidence:** `censored_chunks = fetch_ee_implementation_or_noop(...)(chunks=retrieved_chunks, user=user)`.

- **Claim D:** There is an extra/duplicative pre-check in chat processing for `internal_search_filters.document_set` before build.
- **File / Symbol:** `backend/onyx/chat/process_message.py` / `_stream_chat_turn`
- **Confidence:** **Confirmed**
- **Evidence:** Inline comment says doc set access check was added in SearchTool and this instance should be removed in follow-up; code still performs check.

## 8) Missing or unclear authorization checks
- **Claim A:** Single canonical guard location is not yet enforced across all retrieval callsites; document-set validation appears in both `_stream_chat_turn` and `_build_index_filters`.
- **Confidence:** **Confirmed**
- **Impact:** Divergence risk and inconsistent failure semantics.

- **Claim B:** Whether all non-chat retrieval paths consistently pass through `_build_index_filters` with identical semantics is not fully established in this review.
- **Confidence:** **Unknown**
- **Impact:** Potential bypass risk if any path builds raw `IndexFilters` without guard.

- **Claim C:** `bypass_acl=True` intentionally disables ACL/document-set checks in some contexts (e.g., Slack/system callers); security assumptions for each caller need explicit policy logging.
- **Confidence:** **Partially Confirmed**
- **Evidence:** `_build_index_filters` branches on `bypass_acl`; `_stream_chat_turn` has `bypass_acl` argument and conditionally skips check.
- **Impact:** **Critical** if misused for user-originated traffic (retrieval leakage).

## 9) Recommended integration point (exact candidate)
- **Recommendation:** Integrate `RetrievalAuthorizationGuard` at **`backend/onyx/context/search/pipeline.py::_build_index_filters`**, immediately before constructing `IndexFilters` and before `search_chunks(...)` is called.
- **Why safest:**
  1. It is the narrow choke point where user identity, document set selections (user + persona), ACL state, and metadata filters converge.
  2. It is tool-agnostic for internal search paths that use `search_pipeline`.
  3. It fails closed before retrieval executes.
- **Confidence:** **Confirmed** (as best runtime convergence point in inspected paths).

## 10) Alternative integration points rejected and why
1. **`/chat/send-chat-message` endpoint (`handle_send_chat_message`)**
   - Rejected: too early; lacks finalized retrieval filter state and would duplicate logic per entrypoint (chat, APIs, tools).
2. **`process_message._stream_chat_turn` pre-check block**
   - Rejected: chat-specific and already marked as duplicative in code comment; does not cover non-chat search invocations.
3. **`search_chunks` / document index retrieval layer**
   - Rejected: later in flow; harder to reason about high-level request semantics (persona/user overrides) and error messages.
4. **Citation construction layer (`search_tool` / `db.chat`)**
   - Rejected: too late; leakage may have already happened during retrieval.

## 11) Risk of breaking existing behavior
- **Low-to-Moderate** if guard preserves current `_build_index_filters` semantics and error codes.
- **Moderate** risk for callers using `bypass_acl=True`; must preserve explicit system-only behavior.
- **High (Critical) security risk** if integration accidentally becomes fail-open or diverges from current document-set + ACL checks.

## 12) Test files to modify or extend
- `backend/tests/integration/tests/chat/test_chat_document_set_access.py`
  - Extend to assert guard behavior remains enforced via chat path and no regression on authorized/public/nonexistent sets.
- `backend/tests/integration/tests/mcp/test_mcp_server_search.py`
  - Add/extend case validating authorization behavior for search tool invocations outside chat-style flow.
- Potentially add focused unit tests near search filter assembly:
  - `backend/onyx/context/search/` test module for `_build_index_filters` guard behavior (if existing unit test pattern permits).

## 13) Minimal implementation plan
1. Introduce `RetrievalAuthorizationGuard` callable used by `_build_index_filters` (no semantic changes initially).
2. Move/centralize document-set authorization decision there; keep failure mode `OnyxErrorCode.INSUFFICIENT_PERMISSIONS`.
3. Preserve `bypass_acl` semantics explicitly and document intended callers.
4. Remove chat-layer duplicate pre-check only after parity tests pass.
5. Add/extend tests listed above to prevent bypass regressions.
6. Record evidence in `security-readiness/07-testing-and-verification/evidence.md` during implementation phase.

---

### Notes on confidence discipline
- Any claim not directly proven from inspected code is marked **Unknown** or **Partially Confirmed**.
- Retrieval leakage should be treated as **Critical** in implementation and test prioritization.
