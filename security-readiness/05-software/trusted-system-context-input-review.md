# trusted_system_context Input Origin Review

Date: 2026-05-12  
Status: **Launch gate remains NOT_ENOUGH_EVIDENCE**

## Scope
Review of whether external users/API callers can set `trusted_system_context=True` and thereby authorize `bypass_acl=True`.

Inspected categories:
- all `ChunkSearchRequest` construction sites
- all `search_pipeline` callers
- chat request conversion paths
- API request schemas/routes for chat/search
- tool/search paths that build `ChunkSearchRequest`
- tests that set `bypass_acl` / `trusted_system_context`

## Findings by construction/call site

| File path | Function/Class | How `ChunkSearchRequest` is created/called | `bypass_acl` | `trusted_system_context` | External user/API input origin? | Trusted internal caller? | Existing guard | Risk | Required fix |
|---|---|---|---|---|---|---|---|---|---|
| `backend/onyx/tools/tool_implementations/search/search_tool.py` | `SearchTool._run_search_for_query` | Constructs `ChunkSearchRequest(...)` for tool-driven retrieval; calls `search_pipeline(...)` | Set from `self.bypass_acl` | **Not set** (defaults to `False`) | Indirectly influenced by chat/search flows that configure `SearchToolConfig`; in normal API search route hard-coded `False` | Yes, internal tool execution path | `search_pipeline -> _build_index_filters -> enforce_bypass_acl_contract(...)` fail-closed | **Low (current)** because missing `trusted_system_context=True` means any future `bypass_acl=True` here is denied | If a trusted system flow truly needs bypass through this path, explicitly plumb `trusted_system_context=True` only from vetted internal caller and keep deny-by-default |
| `backend/ee/onyx/search/process_search_query.py` | `_run_single_search` | Constructs `ChunkSearchRequest(...)` from `SendSearchQueryRequest` and calls `search_pipeline(...)` | Not set (default `False`) | Not set (default `False`) | Request fields are external (`/api/search/send-search-message`), but these flags are **not** in schema | Mixed: endpoint-backed, but no trust elevation input | Contract guard in pipeline; schema omits trust flags | **Low** for this specific control | Keep request schema free of these fields; add regression test that unrecognized trust fields are rejected/ignored |
| `backend/onyx/context/search/pipeline.py` | `search_pipeline` | Accepts `ChunkSearchRequest` and passes both flags into `_build_index_filters(...)` | Forwarded from request | Forwarded from request | Depends on upstream constructor | Internal core retrieval | `enforce_bypass_acl_contract(bypass_acl, trusted_system_context)` with deny/audit on untrusted bypass | **Medium** (security-critical aggregator) | Keep centralized enforcement here; add integration tests for each upstream entrypoint |
| `backend/onyx/server/features/search/api.py` | `search` route (`POST /api/search`) | Does **not** build `ChunkSearchRequest` directly; builds `SearchTool(... bypass_acl=False)` then tool builds request | Hard-coded `False` | Not exposed | External API route; user controls query/filters but not bypass/trust flags | No (user API) | Hard-coded `bypass_acl=False` + downstream contract | **Low** | Keep hard-coded false; add explicit comment/test asserting API cannot enable bypass via payload |
| `backend/ee/onyx/server/query_and_chat/search_backend.py` + `backend/ee/onyx/server/query_and_chat/models.py` | `handle_send_search_message` + `SendSearchQueryRequest` | Route passes request to `_run_single_search` builder above | Not present in request schema | Not present in request schema | External API route, but no trust/bypass fields in schema | No (user API) | Omitted from schema + downstream contract | **Low** | Add schema-level regression test attempting `trusted_system_context` injection |
| `backend/onyx/server/query_and_chat/models.py` + `backend/onyx/chat/process_message.py` | `SendMessageRequest` conversion into `_stream_chat_turn` / `handle_stream_message_objects` | Chat path constructs `SearchToolConfig(... bypass_acl=bypass_acl)` internally; user chat schema has no bypass/trust fields | Param exists in internal function signatures (`bypass_acl: bool=False`) | No explicit trusted context plumbed in this path | User-facing chat request cannot directly set bypass/trust based on inspected schema; internal callers could set `bypass_acl` | Mixed (internal and external call stack) | Downstream contract denies bypass unless trusted context also true | **High (until fully proven across all internal route wrappers)** | Audit all invocations of `handle_stream_message_objects` / `_stream_chat_turn` in non-user channels (Slack/Discord/system jobs) and explicitly document which are trusted; add tests for each wrapper |
| `backend/onyx/onyxbot/slack/handlers/handle_regular_answer.py` | Slack handler tool construction | Constructs `SearchToolConfig(... bypass_acl=False)` for Slack bot path | Hard-coded `False` | Not set | Not directly user payload field at this call site | Internal integration path | Downstream contract | **Low (current)** | If Slack/system needs bypass in future, require explicit trusted context plumbing and signed identity check |

## Tests that set bypass/trusted flags

| File path | Test scope | Flags set | Input origin confidence | Risk label | Note |
|---|---|---|---|---|---|
| `backend/tests/unit/onyx/security_readiness/test_bypass_acl_contract.py` | Unit tests for `enforce_bypass_acl_contract` | Sets both combinations of `bypass_acl` and `trusted_system_context` | Internal test-only | Low | Verifies fail-closed deny + allow path with audit events |
| `security-readiness/evidence-artifacts/bypass-acl-contract/test_bypass_acl_contract.py` | Dependency-light evidence tests | Sets both combinations | Internal test-only | Low | Duplicates core contract evidence |
| `backend/tests/unit/onyx/chat/test_multi_model_streaming.py` | Chat state setup | `setup.bypass_acl=False` | Internal test-only | Low | No trust elevation |

## Assessment answer (current evidence)

1. **No confirmed externally user-controlled path was found that can set `trusted_system_context=True` via the inspected chat/search API schemas.**  
2. `trusted_system_context` is currently only present on internal `ChunkSearchRequest` model and is not exposed in inspected request schemas.  
3. The retrieval core now enforces `bypass_acl => trusted_system_context` fail-closed, reducing exploitability if an internal path accidentally sets bypass without trust.  
4. **Residual gap:** complete provenance of internal/system callers that can thread `bypass_acl=True` is still not fully proven end-to-end in backend harness/integration tests; keep decision **NOT_ENOUGH_EVIDENCE**.

## Risk decision

- External user control of `trusted_system_context`: **Not Verified / Unknown** globally (no positive evidence found in inspected paths).  
- If any external route is later found to map user input into `trusted_system_context=True`, classify immediately as **Critical** per policy.  
- Current launch gate: **NOT_ENOUGH_EVIDENCE** (unchanged).

## Next minimal code fix to prioritize

1. Add integration tests at API boundaries (chat + search routes) that send payloads containing `trusted_system_context` / `bypass_acl` and assert they are rejected or ignored.  
2. Add explicit trusted-caller contract helper at chat wrapper boundaries: only vetted system entrypoints may request bypass, and must set `trusted_system_context=True` in one narrow place.  
3. Extend backend harness to exercise full route -> tool -> `search_pipeline` chain and capture authorization audit events.
