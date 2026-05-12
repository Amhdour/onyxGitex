# MCP Hardening Review

Date (UTC): 2026-05-12
Status: **Present**

## Scope
Review of Onyx MCP server implementation for agent identity, tool authorization, and hardening controls.

## Evidence Reviewed
- `backend/onyx/mcp_server_main.py` (entrypoint + enable flag)
- `backend/onyx/mcp_server/api.py` (server creation, auth hook, app middleware)
- `backend/onyx/mcp_server/auth.py` (token verification)
- `backend/onyx/mcp_server/utils.py` (access-token requirement)
- `backend/onyx/mcp_server/tools/search.py` (tool registration and execution)
- Existing tests under `backend/tests/integration/tests/mcp/`

## Findings

### 1) Server Entrypoint
**Verified**: MCP server entrypoint exists at `python -m onyx.mcp_server_main`, gated by `MCP_SERVER_ENABLED` and served by uvicorn.

### 2) Authentication Behavior
**Verified**:
- FastMCP instance is configured with `auth=OnyxTokenVerifier()`.
- `OnyxTokenVerifier.verify_token()` delegates bearer-token verification to Onyx API `/me` endpoint.
- Non-200 from `/me` returns `None` (auth reject path).

**Partially Confirmed**:
- Scope is set to `mcp:use` in returned `AccessToken`, but no additional per-tool authorization policy is enforced in MCP tool bodies.

### 3) Tool Registration
**Verified**: MCP tools are registered via decorators in `backend/onyx/mcp_server/tools/search.py`:
- `search_indexed_documents`
- `search_web`
- `open_urls`

### 4) Tool Execution Path
**Verified**:
- Tools call `require_access_token()` and fail if token missing.
- Tools proxy to internal Onyx API endpoints with bearer auth.
- Failure responses are normalized into structured `error` payloads.

### 5) Allowed Tools
**Verified**: Only the three tools above are registered in this MCP server module set currently imported from `onyx.mcp_server.tools.search`.

### 6) Dangerous Tools
**Verified/Assessment**:
- No direct shell/OS execution tools in MCP server module.
- `open_urls` is higher risk (external URL retrieval / possible data exfiltration vector if upstream controls are weak).
- `search_web` is medium risk (external content ingress into agent context).

### 7) Logging
**Verified**:
- Informational logs for startup/shutdown and tool invocation intent.
- Warning logs for token rejection and malformed time filter.
- Error logs include stack traces for backend/request failures.

**Partially Confirmed**:
- No explicit immutable audit event schema (actor/tool/decision/outcome/reason) identified in MCP module itself.

### 8) Error Handling
**Verified**:
- Auth failure returns `None` from verifier (reject).
- Backend failures caught and mapped to stable error payloads.
- `require_access_token()` enforces fail-closed requirement for missing identity at tool call path.

## Control Gaps / Unknowns
1. **Unknown**: Dedicated “high-risk tool approval required” policy in MCP runtime path.
2. **Unknown**: Prompt-injection-specific policy enforcement at MCP tool boundary.
3. **Partially Confirmed**: Audit events exist as logs, but dedicated security-audit event contract not confirmed from MCP code alone.

## Hardening Recommendations
1. Add explicit per-tool authorization policy gate (deny-by-default for unapproved high-risk tools).
2. Add structured audit events for every tool decision:
   - actor identity
   - tool name
   - policy decision (allow/deny)
   - reason code
   - correlation/request id
3. Add prompt-injection guardrail checks before high-risk outbound tools (`open_urls`, future external tools).
4. Add mandatory identity checks + fail-closed test coverage for all tool handlers.
