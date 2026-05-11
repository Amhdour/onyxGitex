# Build Priority 7 - External Data Ingestion Risk Review

Date: 2026-05-11

## Data ingestion path (verified architecture)
1. Source type selected from `DocumentSource`.
2. Connector class resolved through `CONNECTOR_CLASS_MAP`.
3. Connector instantiated by factory with credential loading.
4. Connector executes load/poll/checkpoint workflows and emits documents.

## Risk register
| Risk | Description | Existing control | Evidence required |
|---|---|---|---|
| Credential overreach | Token has broader permissions than required | Credential storage abstraction + connector validation hooks | Scope review per connector + auth test logs |
| Data poisoning | Malicious content injected from web/file/API sources | No universal content trust gate observed in inspected files | Content validation/red-team test outputs |
| Stale ingestion | Poll/checkpoint gaps leave old/incorrect docs | Poll/checkpoint interfaces + indexing status pipeline | Freshness SLO checks + stale-doc detection report |
| Cross-tenant leakage | Mis-scoped retrieval or cc-pair visibility | Tenant-aware credential provider and user/group filter logic | Tenant isolation tests on connector docs |
| Misconfigured deletion/quarantine | Unsafe connector remains active after issue | Status transitions (`PAUSED`/`DELETING`/`INVALID`) and deletion workflow | Runbook execution evidence + audit logs |

## No-external-credential handling
This review used code inspection only. No external connector credentials were created, loaded, or tested.
