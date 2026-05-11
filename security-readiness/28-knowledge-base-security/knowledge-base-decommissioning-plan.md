# Build Priority 20 - Knowledge Base Decommissioning Plan

Date: 2026-05-11

## Scope
Define secure decommissioning steps for knowledge bases, connectors, indexes, and derived artifacts.

## Decommission workflow
1. Inventory target knowledge base assets (documents, chunks, vectors, caches, backups).
2. Freeze new ingestion and retrieval for target scope.
3. Revoke connector credentials and upstream access grants.
4. Delete indexed artifacts (document store, chunk store, vector namespaces).
5. Purge related caches/snapshots according to retention policy.
6. Verify non-retrievability using negative retrieval tests.
7. Record audit evidence and residual risks.

## Required verification tests
| Test | Purpose | Status |
|---|---|---|
| Cross-department vector retrieval test (post-decommission) | Confirm no residual vectors leak data | **Planned** |
| Stale document retrieval test (post-delete) | Confirm deleted docs are not returned | **Planned** |
| Poisoned document retrieval test (post-delete) | Confirm adversarial docs removed from retrieval set | **Planned** |

## Evidence requirements
- Deletion commands/jobs + timestamps.
- Retrieval negative test outputs after decommission.
- Audit event records linking actor, scope, and completion status.

## Open items
- Recovery window and backup purge SLA are **Unknown** until retention controls are validated.
- Any inability to prove non-retrievability must block readiness sign-off.
