# Tool Runtime Integration Point Review (Onyx)

Date: 2026-05-12
Scope: runtime inspection only (no behavior changes)
Status labels: **Verified**, **Partially Confirmed**, **Unknown**

## 1) Tool inventory

### Built-in and runtime-constructed tools (**Verified**)
- `SearchTool` (internal indexed retrieval).
- `WebSearchTool` (external web search provider-backed).
- `OpenURLTool` (URL fetch/open path).
- `PythonTool` (code execution / file-generating interpreter behavior).
- `CodingAgentTool` (agentic coding flow).
- `FileReaderTool` (reads user/chat attached files).
- `ImageGenerationTool` (image generation provider-backed).
- `MemoryTool` (user memory persistence path).
- `MCPTool` (proxy/execution wrapper for external MCP servers/tools).
- Custom OpenAPI-derived tools from `openapi_schema` database entries.

Evidence:
- Tool construction and branching logic in `construct_tools` / `_construct_tools_impl`.
- Runtime runner and tool interface definitions.

## 2) MCP server inventory if present

### MCP capability is present (**Verified**)
- MCP server API exists in `backend/onyx/mcp_server/api.py` with FastMCP bootstrapping.
- MCP server exposes at least one tool module (`mcp_server/tools/search.py`) and resource modules (`resources/indexed_sources.py`, `resources/document_sets.py`).
- Runtime MCP client path exists (`tool_implementations/mcp/mcp_client.py`) and MCP tool wrapper exists (`tool_implementations/mcp/mcp_tool.py`).

### MCP auth modes observed in runtime constructor (**Verified**)
- `NONE`, `PT_OAUTH`, `API_TOKEN`, `OAUTH` handling paths via DB-backed MCP server config.
- Per-user and admin performer paths are differentiated before tool instance creation.

## 3) Tool execution entrypoint

### Primary runtime execution entrypoint (**Verified**)
- `backend/onyx/tools/tool_runner.py::run_tool_calls(...)` is the centralized batch executor.
- Per-tool execution is routed through `_safe_run_single_tool(...)`, which invokes `tool.run(...)` and emits `SectionEnd` packets regardless of success/failure.
- `backend/onyx/chat/llm_loop.py` imports and calls `run_tool_calls(...)` as part of chat LLM tool-call loops.

## 4) Tool permission context

### Current permission context source (**Partially Confirmed**)
- Persona tool association + optional `allowed_tool_ids` gate in constructor.
- Search filters and document constraints are applied when constructing search/file tools.
- Anonymous-user blocking exists for certain OAuth/passthrough custom and MCP paths.
- MCP auth prerequisites are checked in `MCPTool.run` before remote invocation.

### Gap
- No single centralized authorization decision object (allow/deny/conditions) is applied immediately before all `tool.run(...)` calls.

## 5) User identity context

### Identity context observed (**Verified**)
- Chat setup creates `LLMUserIdentity` and carries user/session context through chat runtime.
- Tool construction passes `user`, `user_id`, `user_email`, OAuth tokens, and MCP headers/context where needed.
- MCP tool wrapper receives `user_email`, `user_id`, and potential user OAuth token.

## 6) Human approval support if present

### Status (**Partially Confirmed**)
- Explicit human-approval enforcement hook in runtime tool runner path was **not** found.
- Governance test file exists with `xfail` tests describing expected future behavior for approval/authorization/audit hooks.

Interpretation:
- Human approval support appears **planned/test-specified** but not centrally enforced in current runtime path.

## 7) High-risk tool classification

### High-risk tools (recommended classification)
Treat as **High Risk** due to external action, remote execution, or write side effects:
- `PythonTool` (code execution, generated artifacts).
- `CodingAgentTool` (agentic execution/actions).
- `MCPTool` (external server action surface; depends on remote tool capabilities).
- Custom OpenAPI tools (may call mutating third-party/internal APIs).
- `OpenURLTool` / `WebSearchTool` as medium-to-high depending on egress policy; keep high in restricted environments.

### Current enforcement status (**Partially Confirmed**)
- No centralized high-risk classification gate in `run_tool_calls` before execution.

## 8) Existing audit logging

### Observed logging/trace evidence (**Partially Confirmed**)
- Tool execution errors and exceptions are logged in `tool_runner.py` and attached to tracing spans.
- MCP tool path logs successful execution and authentication/config issues.
- Chat state tracks tool call info for persistence/response flows.

### Gap
- A dedicated, structured audit event for authorization decision (allow/deny/why/policy id/approval id) was not confirmed in the centralized runtime path.

## 9) Recommended ToolAuthorizationRouter integration point

### Recommended primary integration point (**Recommended**)
Insert `ToolAuthorizationRouter` decision call in `backend/onyx/tools/tool_runner.py` immediately before each tool invocation in `_safe_run_single_tool(...)` (or in `run_tool_calls(...)` while preparing per-call execution tuples).

Why here:
- This is the narrowest centralized choke point used by chat runtime for all tool executions.
- Enables fail-closed deny before side effects.
- Supports consistent decision logging and policy evaluation regardless of tool type.
- Avoids fragmented policy checks across individual tool implementations.

### Secondary integration (context assembly)
- In `backend/onyx/chat/llm_loop.py`, ensure router context payload is assembled (user identity, persona/tool allow-list, session/message ids, placement, risk class, approval token) and passed to tool runner.
- In `backend/onyx/tools/tool_constructor.py`, preserve current construction filters but do not rely on constructor-only filtering as final authorization.

## 10) Test files to modify

### Highest-value test targets
- `backend/tests/unit/onyx/tools/test_tool_governance_controls.py` (already present `xfail` governance expectations).
- `backend/tests/unit/onyx/tools/test_tool_runner.py` (central runner behavior).
- `backend/tests/integration/tests/llm_workflows/test_tool_policy_enforcement.py` (integration coverage for deny/allow path).
- `backend/tests/external_dependency_unit/tools/test_mcp_passthrough_oauth.py` (MCP auth + governance interaction).
- `backend/tests/integration/tests/mcp/test_mcp_client_no_auth_flow.py` (MCP no-auth flow with authorization router outcomes).

## 11) Missing context

Marking unresolved items explicitly:
- **Unknown**: canonical policy source for tool-level allow/deny rules (DB table, config, or external PDP).
- **Unknown**: required UX/API contract for human approval token/challenge and replay protection.
- **Unknown**: final audit sink schema for governance decisions (event bus, DB table, SIEM format).
- **Partially Confirmed**: whether non-chat tool execution paths bypass `tool_runner.run_tool_calls`.
- **Unknown**: tenant-specific high-risk overrides and break-glass semantics.

## 12) Risk rating

### Current-state risk rating: **High**
Rationale:
- Central execution path exists, but centralized authorization + approval gate is not confirmed as enforced at runtime prior to tool side effects.
- High-risk tools with external action/execution surfaces are present.
- Governance/audit expectations are visible in tests but currently marked `xfail`, indicating known readiness gap.

## Clear next implementation path (non-breaking plan)
1. Add `ToolAuthorizationRouter` pre-execution decision hook in `tool_runner` (fail-closed default on undecidable state).
2. Pass explicit decision context from `llm_loop` (identity, session, tool args hash, approval artifact, risk class).
3. Emit structured audit event for every decision (allow/deny/error) with correlation ids.
4. Convert current governance `xfail` tests into active pass/fail assertions incrementally.
