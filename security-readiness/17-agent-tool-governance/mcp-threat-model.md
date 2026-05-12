# MCP Threat Model (Agent Identity / Tool Authorization)

Date (UTC): 2026-05-12
MCP Status: **Present**

## Assets
- Internal indexed documents retrievable via `search_indexed_documents`.
- User bearer tokens used to authorize MCP access.
- Agent context receiving tool outputs.

## Trust Boundaries
1. External MCP client -> Onyx MCP server (`/mcp` path).
2. MCP server -> internal Onyx API (`/me`, `/search`, `/web-search`, `/manage`).
3. Agent/tool output -> model context.

## Entry Points
- MCP streamable HTTP endpoint (`/?transportType=streamable-http` once routed).
- MCP health check endpoint (`/health`, intentionally unauthenticated).

## Abuse Cases
1. **Unauthenticated tool invocation** (missing/invalid bearer).
   - Expected control: deny (401 / auth reject).
2. **Unknown tool invocation**.
   - Expected control: protocol-level tool-not-found reject.
3. **Prompt-injected outbound fetch** using `open_urls` to attacker-controlled domains.
   - Current status: **Partially Confirmed**; no explicit MCP-local policy gate detected.
4. **Cross-identity data access** through indexed document search.
   - Expected control: backend ACL enforcement via token identity.
5. **Silent policy bypass without audit evidence**.
   - Current status: **Unknown/Partial** for dedicated security audit contract.

## High-Risk Tool Classification
- `open_urls`: High risk (external content retrieval / potential exfiltration bridge).
- `search_web`: Medium risk (untrusted content ingestion).
- `search_indexed_documents`: High sensitivity impact (internal data access), but expected to be identity-bound by backend ACL.

## Existing Mitigations
- Token verification through backend `/me`.
- Tool handlers call `require_access_token()` (fail closed on missing token).
- Error handling and logging for failure modes.

## Residual Risks
- No explicit “approval workflow” for high-risk tools in reviewed MCP path.
- No explicit prompt-injection detection/denial gate at MCP tool boundary.
- Audit logging may be insufficient for launch-gate evidence without structured events.

## Security Requirements (Next Phase)
1. Add policy engine hook for per-tool allow/deny with reason codes.
2. Require approval or policy precondition for high-risk tools.
3. Add structured audit event emission on every tool call decision.
4. Add deny rules for unsafe prompt-to-tool patterns (fail closed).
