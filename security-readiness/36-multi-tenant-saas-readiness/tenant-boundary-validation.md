# Tenant Boundary Validation

Date: 2026-05-11  
Status: **Partially Confirmed**

## Objective
Validate whether Onyx implements tenant boundary controls for SaaS multi-tenancy.

## Evidence Reviewed
- `MULTI_TENANT` feature flag is present and controls multi-tenant mode enablement from environment configuration.
- Tenant context is propagated via `CURRENT_TENANT_ID_CONTEXTVAR` and enforced through tenant-aware session helpers.
- DB sessions use `schema_translate_map` keyed by tenant id, with tenant id schema-name validation.
- API middleware accepts tenant context from `X-Onyx-Tenant-ID` request header.

## Findings
1. **Tenant-aware DB routing exists (Verified).**
   - `get_session_with_tenant()` validates tenant id and routes SQLAlchemy queries through schema translation for tenant schema targeting.
2. **Async tenant-aware DB routing exists (Verified).**
   - `get_async_session()` applies the same schema-translation strategy.
3. **Tenant context source is header-based (Partially Confirmed).**
   - Middleware sets tenant context from `X-Onyx-Tenant-ID` header.
   - This document does not confirm all upstream authentication/binding controls that prevent caller-controlled spoofing in all routes.
4. **Fail behavior when tenant context missing in multi-tenant mode (Verified).**
   - `get_current_tenant_id()` raises runtime error if tenant id is unset and `MULTI_TENANT=true`.

## Gaps / Unknowns
- Unknown whether all ingress paths cryptographically or authorization-bind user identity to tenant id before middleware consumption.
- Unknown whether all routes consistently depend on tenant-aware session helpers.

## Risk
- If caller-provided tenant headers are not strongly bound to identity, cross-tenant access risk is **Critical**.

## Conclusion
Tenant boundary mechanisms exist at configuration, context, and DB schema layers, but full boundary assurance remains **Partially Confirmed** pending end-to-end authorization verification.
