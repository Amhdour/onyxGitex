# Graceful Degradation Rules

Date: 2026-05-11  
Status: Draft (Pending Validation)

## Decision Matrix (Mandatory)

| Scenario | Primary Action | Mode | User/API Response Requirement |
|---|---|---|---|
| Model unavailable | Skip generation; return controlled error or retrieval-only output | Graceful degradation | Explicitly state generation unavailable; no fabricated answer |
| Vector DB/index unavailable | Return no retrieval results | Graceful degradation | Empty results + machine-readable error |
| Connector failure | Exclude failed connector data | Graceful degradation | Partial-results notice + failed source identifier |
| Tool failure | Abort tool call, keep session alive | Graceful degradation | Structured tool error; no silent success |
| Tracing/logging failure | Continue core request path with local fallback logging | Graceful degradation | Internal warning event; no user data leakage |
| Partial retrieval failure | Return authorized subset only | Graceful degradation | Mark response as partial |
| Policy engine failure / missing policy | Block data/tool action | **Fail-closed** | Deny/error response; zero protected data release |
| Evidence generation failure | Block readiness sign-off artifact publication | **Fail-closed** for governance | Mark evidence artifact as incomplete/invalid |

## Non-Negotiable Rules
1. Authorization uncertainty always fails closed.
2. Availability degradations must be explicit (never silent).
3. Degraded responses must not invent unsupported content.
4. Fallback paths require auditable event logging.
