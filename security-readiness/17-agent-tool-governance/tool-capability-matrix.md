# Tool Capability Matrix

Date: 2026-05-11
Status: **Partially Confirmed**

| Tool Name | Purpose | Input Risk | Output Risk | Authorization Requirement | Human Approval Requirement | Audit Event Requirement | Kill-Switch Method | Abuse Cases | Evidence Needed | Control Mapping |
|---|---|---|---|---|---|---|---|---|---|---|
| `internal_search` | Query internal corpus | Prompt-injected query expansion | Unauthorized snippet disclosure | Authenticated user + basic access | Required for sensitive collections (policy requirement; implementation unknown) | Query, actor, filters, result IDs | Disable tool and/or collection access | Cross-tenant probing | Denied access tests + result-filter logs | AC-1, RA-1, FC-1 |
| `web_search` | Search external web | Malicious query payloads | Hallucinated/unsafe synthesis source | Authenticated user (tool exposure path) | Required for regulated workflows | Query + provider + domains + actor | Disable tool | Data exfiltration via external prompt channel | Domain policy tests + invocation logs | TG-2, TG-4, AU-1 |
| `open_url` | Fetch page content | SSRF-style target selection attempts | Injection of malicious content into context | Authenticated user (tool exposure path) | Required for non-allowlisted domains | URL + response metadata + actor | Disable tool | Accessing disallowed domains | Allow/denylist evidence | TG-2, FC-2, AU-1 |
| `python` | Run generated code | Arbitrary code payloads | Filesystem/network side effects | Tool-level availability checks | Mandatory explicit human confirmation | Code hash + runtime env + actor + decision | Disable tool; stop sandbox workers | Secret scraping, lateral movement | Unauthorized/approval-missing block tests | TG-1, TG-3, AU-2 |
| `memory` | Persist user memory | Sensitive data ingestion | Future leakage from memory recall | Session/user scoped use expected | Required for PII writes (policy) | Memory write/read actor + key + policy decision | Disable memory tool | PII retention without notice | Logs proving retention controls | DP-1, AU-3 |
| MCP tools | External server actions | Untrusted tool schemas | Third-party action side effects | MCP connection ownership + role checks | Mandatory for high-impact actions | Server/tool/call IDs + token scope + actor | Disable MCP server connection | Over-broad OAuth scopes, tool abuse | Authorization and denied-call tests | TP-1, TG-1, AU-2 |

## Control Legend
- TG-* = Tool Governance controls
- AU-* = Auditability controls
- FC-* = Fail-Closed controls
- TP-* = Third-party controls
- DP-* = Data protection controls

## Gaps
- Centralized runtime classification and policy-decision engine for tool calls is **Unknown**.
- Uniform audit event schema for all tool calls is **Partially Confirmed**.
