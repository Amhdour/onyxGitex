# Agent System Scope

- Agent purpose: assist internal operations via approved tools only.
- Allowed actions: scoped retrieval, draft generation, ticket creation, approved updates.
- Disallowed actions: destructive operations, unsanctioned exports, unknown tools.
- User roles: requester, reviewer, approver, admin.
- Tool roles: read-only, write-with-approval, denied-by-default.
- Human approver roles: manager, compliance approver, incident commander.
- In-scope tools: listed in tool capability matrix.
- Out-of-scope tools: external unsanctioned SaaS, unmanaged scripts, direct DB admin tools.
- Assumptions: identity provider and policy engine are available unless proven otherwise.
- Limitations: no runtime verification artifacts yet.
- Evidence required before launch: policy tests, runtime logs, approval logs, audit completeness checks.
