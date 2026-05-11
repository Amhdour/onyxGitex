# 98. Model Routing Policy

Date: 2026-05-11
Status: **Draft Policy (needs implementation verification)**

## Policy objective
Define deterministic, auditable, least-privilege model routing for chat, persona flows, and build-mode tasks.

## Routing order (intended + code-aligned)
1. **Explicit runtime override** (provider+model) when approved for caller context.
2. **Persona default model configuration** when present and authorized.
3. **Tenant default provider/model**.
4. **Fail-closed for protected personas** (policy target), or documented fallback for low-risk personas.

## Mandatory controls
- Provider must be on approved allowlist for environment and data tier.
- `can_user_access_llm_provider` authorization must pass before provider invocation.
- If authorization fails for high-sensitivity persona, block response generation unless an approved fallback exception exists.
- Build-mode routing must pin to `build-mode-{provider}` records for deterministic governance; fallback-to-any-provider-type requires explicit waiver.

## Routing assumptions (mark explicitly)
- Assumption A1 (**Partially Confirmed**): default LLM exists and is governed in DB.
- Assumption A2 (**Unknown**): all override paths are captured in audit logs with actor/context.
- Assumption A3 (**Partially Confirmed**): unauthorized provider fallback is acceptable only for non-sensitive flows.

## Evidence required
- Provider decision log per request: requested provider/model, resolved provider/model, reason code.
- Access-control test matrix across personas/groups/public providers.
- Negative test showing fail-closed behavior for protected personas.

## Launch gate effect
- Missing routing decision logs or missing protected-persona fail-closed tests => **No-Go**.
