# AI Service Availability Review

Date: 2026-05-11  
Status: Partially Confirmed

## Scope
Review current repository evidence for availability controls affecting model calls, retrieval services, connector-dependent data paths, tool execution, tracing/logging, policy checks, and evidence generation.

## Observed Availability Behaviors (Code-Backed)

1. **Model/API provider failure signaling exists**
   - Standard error codes include `SERVICE_UNAVAILABLE`, `BAD_GATEWAY`, `LLM_PROVIDER_ERROR`, and `GATEWAY_TIMEOUT`, which supports consistent outage propagation.  
   - Evidence: `backend/onyx/error_handling/error_codes.py`.

2. **Vector/index startup retries are implemented**
   - Index setup retries each index several times, sleeps between attempts, and returns `False` after attempt exhaustion (explicit non-ready state instead of silent success).  
   - Evidence: `backend/onyx/setup.py` (`setup_document_indices`).

3. **Retrieval tool endpoint returns structured degraded responses**
   - MCP search catches upstream errors and returns empty results + error field, avoiding process crashes.
   - CE retrieval path is an explicit fallback to chat endpoint with longer timeout (`300s`), indicating degraded but available behavior.
   - Evidence: `backend/onyx/mcp_server/tools/search.py`.

4. **Redis-based tenant gating intentionally fails open**
   - If active-tenant Redis read fails, API returns `None` and callers are directed to dispatch to all tenants, preserving availability at the cost of efficiency.
   - Evidence: `backend/onyx/redis/redis_tenant_work_gating.py`.

5. **Policy enforcement utilities default fail-closed**
   - Missing identity/policy/map entries raise `FailClosedError` in readiness control components.
   - Evidence: `backend/onyx/security_readiness/control_layer.py`.

## Gaps / Unknowns
- No completed resilience test evidence found in this phase folder yet (fault-injection runs, SLO impact, MTTR metrics): **Unknown**.
- Runtime production behavior for all chat/retrieval paths (outside sampled modules) during model/vector outages: **Partially Confirmed**.
- Observability backend outage handling (tracer sink unavailable while request continues): **Unknown**.

## Availability Posture Summary
- **Fail-Closed:** policy identity/policy preconditions.
- **Graceful Degradation:** retrieval returns empty/error payloads, CE search fallback path.
- **Fail-Open (explicit):** tenant-work gating on Redis-read failure to avoid starvation.

This review is **not** launch-readiness evidence by itself; it is a code-inspection baseline pending executed resilience tests.
