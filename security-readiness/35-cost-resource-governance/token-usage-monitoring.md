# Token Usage Monitoring

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Monitoring Design
Token usage monitoring is treated as an abuse-prevention signal, not only a performance metric.

## Observed Sources
- LLM response usage model captures `prompt_tokens`, `completion_tokens`, and `total_tokens`.
- Tracing-related tests validate usage fields are written into spans.
- Admin token-rate-limit surfaces exist for user/group budgeting.

## Control Matrix
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| Token burn spikes | Bot/script repeatedly submits oversized prompts | LLM span usage telemetry | >250k tokens per user/hour (initial policy value) | Medium alert to platform on-call | User token rate limits; deny on budget exceed | `backend/ee/onyx/server/query_and_chat/token_limit.py`, `web/src/app/admin/token-rate-limits/` | Platform Ops |
| Output token inflation | Prompting to force verbose or looped generations | `completion_tokens` + answer-length metrics | Completion/input ratio > 8 for 20 requests | Abuse-cost alert | Response-length guardrails + tool-use constraints | `backend/onyx/llm/model_response.py` | AI Safety |
| Group-level quota drain | Coordinated low-volume abuse across many users | Group token budget counters | Group budget > 85% before period end | Proactive budget warning | Group token budget policy and temporary throttling | `backend/ee/onyx/server/query_and_chat/token_limit.py` | Tenant Admin + Platform |

## Notes
- Thresholds are initial governance defaults and require calibration from non-production test telemetry.
- No production billing exports or real invoice data are referenced in this artifact.
