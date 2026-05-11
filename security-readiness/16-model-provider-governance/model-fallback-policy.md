# 101. Model Fallback Policy

Date: 2026-05-11
Status: **Draft Policy with Known Gaps**

## Policy intent
Fallback must preserve security boundaries and should not silently downgrade to a less-governed model for sensitive personas.

## Fallback classes
1. **Authorization failure** (user/persona not permitted for selected provider)
2. **Provider unavailable** (timeout/outage/rate limit)
3. **Model config missing/invalid**

## Required behavior by sensitivity tier

| Tier | Authorization Failure | Provider Outage | Missing Config |
|---|---|---|---|
| Restricted / Confidential | **Fail-closed** (return controlled error) | Fail to approved same-tier backup only; else fail-closed | Fail-closed |
| Internal | Fallback allowed only to pre-approved provider/model pair with equal-or-better controls | Controlled fallback allowed with audit event | Controlled fallback allowed |
| Public | Fallback allowed with telemetry and user-visible notice | Fallback allowed | Fallback allowed |

## Observed current behavior (from code)
- Persona/provider resolution may fall back to default LLM when overrides are invalid, model configs missing, or provider access is denied.
- Build-mode provider lookup falls back from named `build-mode-{type}` provider to any provider of same type.

## Control requirements
- Emit structured fallback audit events with reason code and resolved provider/model.
- Block fallback for protected personas unless explicit approved exception exists.
- Maintain approved fallback map (source provider/model -> allowed fallback provider/model).
- Periodically test fallback paths for quality and safety regression.

## Unknowns
- Whether all fallback branches currently emit auditable decision logs: **Unknown**.
- Whether fallback branches are differentiated by data sensitivity tiers at runtime: **Unknown**.

## Launch gate effect
- Without tier-aware fail-closed enforcement and fallback audit logs, readiness status is **No-Go** for sensitive enterprise launch.
