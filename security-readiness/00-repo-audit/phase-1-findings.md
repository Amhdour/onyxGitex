# Phase 1 Findings: Repository Audit

Date: 2026-05-11 (UTC)
Assessment Type: static codebase/documentation map only.

## What is confirmed in-repo

- Onyx has explicit authorization dependency patterns via `require_permission(...)` and multiple role-aware route dependencies.
- Document-level ACL filtering logic exists in a centralized helper (`db/document_access.py`) with public/email/group conditions.
- Chat and retrieval entrypoints are structurally separated and identifiable (`chat_backend.py`, `query_backend.py`).
- Tool and MCP management have dedicated API modules and model/db integration points.
- Deployment options include compose, helm, and terraform, with MCP-specific deployment artifacts.

## High-risk areas (for Phase 2)

1. **Access-control consistency across all retrieval modalities**
   - Risk: ACL applied in some retrieval paths but not others.
   - Status: **Partially Confirmed**.

2. **Chat + tool invocation boundary enforcement**
   - Risk: tool execution context might permit data exfiltration or implicit privilege expansion.
   - Status: **Needs Verification**.

3. **MCP OAuth and credential lifecycle robustness**
   - Risk: stale credentials, mask-handling bugs, token misuse.
   - Status: **Partially Confirmed**.

4. **Policy decision logging / audit completeness**
   - Risk: security-relevant allow/deny decisions may be hard to reconstruct.
   - Status: **Unknown**.

## Blockers encountered in Phase 1

- No runtime environment execution performed in this phase by design.
- Large-module depth (e.g., `auth/users.py`) requires scenario testing to move from partial to confirmed assertions.

## Recommended Phase 2 tasks

1. Create control-to-test matrix for AuthN/AuthZ/RAG ACL/tool/MCP controls.
2. Execute targeted integration tests for:
   - document set visibility across users/groups,
   - connector-ingested ACL propagation,
   - chat retrieval with mixed permissioned sources,
   - tool and MCP abuse-case denial behavior.
3. Validate logging/tracing for policy decisions (allow/deny, tool invocation, citation source selection).
4. Produce evidence artifacts with commands + outputs + residual risk labels (Verified / Partially Confirmed / Unknown).

## Non-claims (explicit)

- This phase does **not** claim production readiness.
- This phase does **not** assert that any control is effective at runtime without test evidence.
