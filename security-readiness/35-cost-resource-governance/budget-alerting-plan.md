# Budget Alerting Plan

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Alerting Levels
- **Info (70%)**: budget burn approaching limit.
- **Warn (85%)**: intervention recommended.
- **Critical (100%)**: enforce hard stop/fail-closed behavior where configured.

## Budget Alert Table
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| Monthly budget exhaustion | Burst abuse consumes quota early | Tenant usage counters (`llm_cost_cents`) | 70/85/100% of period budget | Info/Warn/Critical notifications | Automated throttle/deny at critical | `backend/onyx/db/usage.py`, `backend/ee/onyx/server/usage_limits.py` | FinOps |
| Budget starvation of legitimate users | One actor monopolizes shared quota | Per-user + group token limits | Any actor >30% tenant budget/day | Abuse + fairness alert | Actor-level caps + group budgets | `backend/ee/onyx/server/query_and_chat/token_limit.py` | Tenant Admin |
| Hidden post-limit traffic attempts | Attackers continue calls after limit exceeded | Budget exceeded errors in logs | >10 blocked requests/actor/hour | Security alert | Temporary account hold + IR review | `backend/onyx/llm/utils.py` | SOC + IAM |

## Implementation Notes
- Alert transport integration target: existing monitoring/alerting controls in Priority 33 artifacts.
- This plan intentionally excludes real billing exports; synthetic and internal counters only.
