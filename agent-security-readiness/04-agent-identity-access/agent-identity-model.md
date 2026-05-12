# Agent Identity Model

- User identity: authenticated principal with role, department, and session claims.
- Agent identity: non-human principal bound to request/session context.
- Service account: minimal privilege account for tool connectors.
- Delegated authorization: agent acts only within user-approved scope plus policy constraints.
- Session binding: every tool call tied to request ID and user/session identity.
- Tenant/department boundary: enforced on retrieval and record operations.
- Privilege escalation risks: forged tokens, stale sessions, implicit trust in planner output.
- Evidence required: identity binding logs, denied escalation tests, token/claim validation traces.
