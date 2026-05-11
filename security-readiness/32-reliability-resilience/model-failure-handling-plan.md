# Model Failure Handling Plan

Date: 2026-05-11  
Status: Draft (Pending Validation)

## Failure Mode
Model unavailable (provider outage, timeout, auth failure, quota/rate failure).

## Detection Signals
- Upstream non-2xx responses mapped to standardized service/provider error codes.
- Exceptions in model invocation path with request correlation id.

## Required Behavior
1. **Fail-Closed Conditions**
   - If policy/identity context is missing, do not attempt model response composition.
   - If model response cannot be trusted as policy-compliant, block answer and return controlled error.

2. **Graceful Degradation Conditions**
   - Return explicit user-safe failure message (no fabricated answer).
   - If retrieval-only evidence is available, provide citations/snippets only with “generation unavailable” notice.

## Controls
- Use standardized codes (`LLM_PROVIDER_ERROR`, `BAD_GATEWAY`, `GATEWAY_TIMEOUT`, `SERVICE_UNAVAILABLE`) for consistent downstream handling.
- Emit audit event with: request id, tenant, model name, failure class, fallback path used/not used.
- Apply bounded retry with jitter for transient provider/network errors (no infinite retry loops).

## Evidence Status
- Error-code taxonomy: **Verified** (code inspection).
- End-to-end model outage fallback test: **Unknown** (not executed in this task).
