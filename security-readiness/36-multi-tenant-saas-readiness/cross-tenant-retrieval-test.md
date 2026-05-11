# Cross-Tenant Retrieval Test

Date: 2026-05-11  
Status: **Unknown**

## Objective
Validate explicit denial of cross-tenant retrieval.

## Criticality
Cross-tenant leakage is **Critical** and must fail launch gate.

## Test Case Matrix
1. **Header/Identity mismatch test**
   - Auth as tenant A user; send `X-Onyx-Tenant-ID: tenant_b`.
   - Expect reject/deny if identity binding is enforced.
2. **Sentinel retrieval test**
   - Query tenant A for tenant B unique content fingerprint.
   - Expect no retrieval results from tenant B corpus.
3. **API token tenancy test**
   - Reuse token from tenant A against tenant B namespace route patterns (if present).
   - Expect deny.

## Required Evidence
- Command transcript.
- HTTP status codes.
- Response payload excerpts (redacted).
- Server logs/audit entries proving denial path.

## Current Result
- Not executed in this phase; result remains **Unknown**.
