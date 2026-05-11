# Abuse Cost Detection

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Detection Objective
Identify cost anomalies that indicate abuse, misuse, or policy bypass attempts.

## Detection Signals
- Sudden increases in token consumption per actor/session.
- Elevated denied-tool-call rates followed by model cost spikes.
- Frequent retries after budget-exceeded errors.

## Detection Controls
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| Stealth low-and-slow cost abuse | Distributed actors each stay below single-user thresholds | Aggregated tenant usage + actor cohort analysis | Tenant spend trend >2σ weekly baseline | FinOps anomaly alert | Multi-actor anomaly rule + tenant throttle | `backend/onyx/db/usage.py` | FinOps + Security Analytics |
| Budget-bypass probing | Repeated retries after token/cost denial | API error logs (`budget exceeded`) + session traces | >10 retries/actor/15 min | Abuse investigation alert | Progressive backoff + temporary account restrictions | `backend/onyx/llm/utils.py`, `backend/ee/onyx/server/query_and_chat/token_limit.py` | Platform Security |
| Prompt-injection induced spend | Tool denial + high token usage in same session | Correlated tool/LLM traces | 3 correlated events/session | High-priority SOC alert | Session quarantine + incident workflow | `security-readiness/33-monitoring-alerting/tool-misuse-alerting.md` | SOC |

## Evidence Classification
- **Verified**: Budget-exceeded error pathways and token-limit enforcement logic are present in code.
- **Partially Confirmed**: Cross-signal correlation rules require SIEM implementation validation.
- **Unknown**: Final production thresholds pending baseline tuning exercise.
