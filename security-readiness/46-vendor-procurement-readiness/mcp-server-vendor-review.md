# MCP Server Vendor Review (Priority 38 / Scope 313)

## Purpose
Review third-party MCP server vendors/providers for tool safety, authorization boundaries, and data handling risk.

## Critical Constraint
- MCP vendor remains **Not Approved** unless tool authorization, logging, and data deletion controls are verified.

## Security Review Questions
| Domain | Questions | Evidence Required | Status |
|---|---|---|---|
| Data access | How does MCP server enforce requester identity and least privilege for tool actions? | AuthZ model docs, policy enforcement examples | Unknown |
| Retention | Does server store prompts, tool parameters, or outputs? If yes, for how long? | Data lifecycle/retention documentation | Unknown |
| Logging | Are all tool calls, denials, and privilege changes logged with actor and request ID? | Audit log schema + sample records | Unknown |
| Encryption | Are tool payloads encrypted in transit and sensitive stores encrypted at rest? | TLS/storage encryption docs | Unknown |
| Incident notification | What incident SLA applies to unauthorized tool execution or data leakage? | IR policy and contractual timelines | Unknown |
| Subcontractors | Are third parties involved in hosting or processing MCP requests? | Subprocessor inventory and notice process | Unknown |
| Audit rights | Can customer obtain audit reports and perform targeted control validation? | Audit package and customer assessment terms | Unknown |
| Exit/deletion | Can session/tool data be exported and deleted with proof of deletion? | Export/deletion SOP and attestation format | Unknown |

## Tool Misuse and Abuse-Case Checks
- Confirm default deny behavior for unknown tools/actions.
- Confirm policy decision logging for allow/deny outcomes.
- Confirm human approval workflow for high-risk tools.
- Confirm rate limiting and abuse detection controls.

## Procurement Decision
- Vendor:
- High-risk tool categories in scope:
- Blocking issues:
- Decision: **Pending / Conditionally Acceptable / Rejected / Approved with Evidence**
