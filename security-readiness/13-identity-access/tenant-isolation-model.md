# Tenant Isolation Model

## Relevant code paths
- `backend/onyx/auth/users.py` (tenant-context session usage and tenant context var handling).
- `backend/onyx/db/engine/sql_engine.py` and async engine session helpers.
- `backend/onyx/db/document_access.py` (document ACL filtering by user email and external group ids).

## Current observed behavior
- Auth flows set tenant context and use tenant-scoped sessions for user operations in multi-tenant paths.
- Document access filtering applies ACLs via connector access type, document public flags, user email match, and external group overlap.

## Unknowns
- Full cross-tenant negative test coverage for every sensitive endpoint.
- Assurance that all background jobs inherit/reset tenant context correctly across asynchronous boundaries.

## Expected control
- No request should read/write data outside current tenant context.
- Document retrieval must stay constrained by ACL predicates tied to current user identity/groups.

## Test cases
- Wrong-department (non-overlapping external group) access denied to scoped documents.
- Cross-tenant user cannot access another tenant’s data (integration scenario).

## Evidence needed
- SQL/log evidence showing tenant-scoped queries.
- Multitenant negative tests for representative endpoints and document retrieval.

## Launch gate impact
- **Critical**: tenant isolation gaps are launch blockers for enterprise internal knowledge assistants.
