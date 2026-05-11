# Build Priority 20 - Document Permission Inheritance Review

Date: 2026-05-11

## Scope
Assess whether document-level permissions from upstream systems are inherited and preserved through indexing and retrieval.

## Review matrix
| Control point | Security objective | Test / evidence method | Status |
|---|---|---|---|
| Source ACL capture during ingestion | Preserve source permission semantics | Inspect ingestion mapping + fixture documents with distinct ACLs | **Unknown** |
| ACL propagation to document records | Persist permissions in storage layer | DB/schema inspection + integration tests | **Unknown** |
| ACL propagation to chunk/index metadata | Ensure downstream chunk and vector access checks can evaluate ACL | Chunk/index metadata inspection + retrieval tests | **Unknown** |
| Permission updates on source-side access revocation | Fail closed after access is revoked | Revocation test (before/after retrieval attempt) | **Unknown** |

## Planned tests
1. **Document permission inheritance test**
   - Setup: ingest two docs with department-scoped ACLs (Dept-A, Dept-B).
   - Check: Dept-A user retrieves only Dept-A doc; Dept-B doc denied.
   - Evidence: test command, assertion logs, relevant query metadata.
2. **Permission revocation propagation test**
   - Setup: ingest doc with access for User-X, then revoke upstream permission.
   - Check: User-X retrieval is denied after next sync/index cycle.
   - Evidence: sync timestamp + denied retrieval trace.

## Risks
- If inheritance is incomplete at any stage, retrieval leakage is **Critical**.
- Until tested, inheritance guarantees remain **Unknown** and cannot be treated as implemented.
