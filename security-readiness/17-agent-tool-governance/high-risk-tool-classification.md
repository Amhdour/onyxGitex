# High-Risk Tool Classification

Date: 2026-05-11
Status: **Partially Confirmed**

## Classification Criteria
A tool is High-Risk if it can:
- Execute code or shell commands.
- Write/modify external systems.
- Access sensitive internal or third-party data at scale.
- Egress data to external destinations.
- Operate with privileged credentials.

## Current Tool Classification

| Tool Name | Risk Level | Rationale | Required Controls |
|---|---|---|---|
| `python` | High | Code execution with runtime side effects | Human approval, sandbox restriction, full audit, kill-switch |
| coding agent tool | High | Autonomous code+tool orchestration | Human approval at high-impact steps, budget/step limits, full audit |
| MCP tools (write-capable) | High | Third-party side effects via external APIs | Scope-constrained OAuth, approval gate, tenant boundary checks |
| `open_url` | Medium-High | External content retrieval and possible unsafe targets | Domain policy, content sanitization, audit logs |
| `web_search` | Medium | External retrieval with misinformation/exfil channel | Query policy, domain controls, audit logs |
| `internal_search` | Medium | Internal data access risk | ACL enforcement, result filtering, audit logs |
| `memory` | Medium | Persistent storage of sensitive user context | Consent/PII controls, retention controls, audit logs |

## Unknowns
- Formal runtime classification engine dispatching policy by risk level: **Unknown**.
- Evidence of consistent enforcement across all tool implementations: **Partially Confirmed**.
