# LLM Cost Risk Review

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Objective
Establish abuse-linked LLM spend risks and define fail-closed cost controls before launch.

## Current Implementation Evidence (Code Inspection)
- Tenant-level LLM spend accounting exists via `llm_cost_cents` persistence and increment logic.
- Provider-side cost limit checks are wired into query/chat backend paths.
- Model usage includes token usage capture and cost computation hooks.

## Cost Risk Register
| Cost risk | Abuse scenario | Monitoring source | Threshold | Alert | Control | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| Runaway model spend per tenant | Automated prompt flooding to force expensive completions | Tenant usage table (`llm_cost_cents`), request traces | Daily spend > approved tenant budget | High-priority SOC + platform alert | Enforce provider budget check (fail-closed on exceed) | `backend/onyx/db/usage.py`, `backend/ee/onyx/server/query_and_chat/search_backend.py`, `backend/onyx/llm/multi_llm.py` | Platform Engineering + FinOps |
| Prompt-injection cost amplification | User coerces agent into repeated long-chain responses | LLM span usage metrics (`prompt_tokens`, `completion_tokens`, `total_tokens`) | 3x baseline token growth/session | Security monitoring alert + abuse case ticket | Per-session token caps + anomaly detection | `backend/onyx/llm/model_response.py`, tracing tests | AppSec + AI Security |
| Silent cost drift from model routing changes | Undocumented routing to higher-price model tiers | Model/provider logs + release change records | Any routing policy change without review | Governance review alert | Change-control gate on routing rules | `security-readiness/16-model-provider-governance/model-routing-policy.md` + this phase artifacts | AI Governance Council |

## Verification Status
- **Verified**: Cost tracking code path exists and includes cost increment capability.
- **Partially Confirmed**: Alert transport and dashboards for spend anomaly escalation require operational confirmation.
- **Unknown**: Real billing reconciliation workflow in production finance systems (out of scope; no billing data used).
