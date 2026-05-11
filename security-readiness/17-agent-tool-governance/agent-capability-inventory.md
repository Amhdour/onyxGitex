# Agent Capability Inventory

Date: 2026-05-11
Status: **Partially Confirmed**

## Scope
Inventory of agent-exposed capabilities from repository-observed tool paths and MCP integration points.

## Capability Inventory

| Agent/Runtime Capability | Tool Name(s) | Purpose | Input/Output Risk | Authorization Requirement | Human Approval Requirement | Audit Event Requirement | Kill-Switch Method | Abuse Cases | Evidence Needed | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Internal retrieval | `internal_search` | Retrieve indexed internal content | Prompt injection into retrieval terms; over-broad result exposure | `Permission.BASIC_ACCESS` for tool listing/API exposure | Not explicit in code | Trace span + tool invocation log required | Disable tool via `/admin/tool/status`; remove from assistant config | Unauthorized data discovery via crafted queries | Runtime logs showing user-bound filters and denied results | Partially Confirmed |
| External web retrieval | `web_search`, `open_url` | Internet search and URL fetch | Data exfiltration channel, malicious content ingestion | No explicit per-call high-risk gate observed in tool runner | Not explicit | Per-call invocation + URL domain logged | Disable in tool status and assistant config | Data exfiltration or untrusted content laundering | Block/allowlist test evidence by domain and policy enforcement logs | Partially Confirmed |
| Code execution | `python`, coding agent tool | Evaluate/generated code execution | Arbitrary code execution and data exfil from runtime | Tool availability checks exist, but central high-risk approval gate not confirmed | Not explicit | Execution request, actor, inputs hash, output summary | Disable tool; sandbox teardown; worker stop | File/network misuse, hidden persistence | Tests for denial without approval + blocked high-risk call + audit trail | Partially Confirmed |
| Memory write/read | `memory` | Persist and retrieve conversational memory | Unauthorized persistence of sensitive content | User/session scoping expected; explicit policy assertions not fully verified | Not explicit | Memory write/read event with actor and scope | Disable memory tool + clear memory path | PII persistence without consent | Tests/logs proving scope and redaction policy | Unknown |
| MCP federated tools | MCP discovered tools | Invoke external servers via MCP | Third-party action risk, OAuth token misuse | MCP connection and tool visibility enforcement exists in API layer | Not explicit | MCP call event with server/tool/tenant/user IDs | Disable MCP server/tool connection; revoke OAuth credentials | Privilege escalation through over-permissive MCP tool | Evidence of per-tenant isolation and denied unauthorized calls | Partially Confirmed |

## Notes
- Human confirmation policy and high-risk classification are not currently enforced by a single central policy gate in inspected tool execution path.
- Unknowns are carried into control and testing artifacts; no readiness claim is made.
