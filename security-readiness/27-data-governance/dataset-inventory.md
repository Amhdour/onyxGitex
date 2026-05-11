# Dataset Inventory
Date: 2026-05-11 (UTC)
Scope: Retrieval corpus governance for Onyx RAG flows (not model pretraining)
Status: Partial inventory (code-observed + assumptions)

## Inventory Table

| Dataset / Store | Source system | Owner | Classification | Freshness | Provenance | Deletion requirement | Retention assumption | Quality risk | Evidence needed |
|---|---|---|---|---|---|---|---|---|---|
| Connector-ingested documents (`DocumentSource` set) | External systems integrated through connectors/federated connectors | Data owner in originating system; platform owner for ingestion service | Mixed (Unknown per-source until tagged) | Connector/job dependent (Unknown global SLA) | Connector identity + source type + ingestion pipeline metadata | Must support source-driven delete/update propagation | Retained until source delete or admin policy; exact TTL Unknown | Stale copies, mis-tagged ACL/owner metadata, parser extraction errors | Per-connector inventory export, ingestion job logs, and sampled metadata validation |
| Indexed retrieval chunks + vector/keyword representations | Derived from ingested documents during indexing | Platform owner (search/index ops) + originating data owners | Inherits source classification | Rebuilt by indexing jobs; lag Unknown | Derived artifact linked to source doc id/chunk metadata | Must be deleted when source docs are deleted or access revoked | Retention tied to document lifecycle; explicit TTL Unknown | Orphaned chunks, embedding drift, inconsistent chunk metadata | Reindex/deletion job evidence and orphan-chunk checks |
| Retrieval metadata (`search_doc`) for replay/debug | Runtime retrieval events | Platform owner / security operations | Operational metadata (may reference sensitive docs) | Near real-time per query | Query-time write path in app DB | Must be deletable per policy and tenant requirement | See existing retention baseline assumptions; explicit window not confirmed | Over-retention of sensitive references, incomplete trace linkage | DB schema refs + retention job/setting evidence |

## Notes
- The available connector source taxonomy is explicitly enumerated in code (`DocumentSource`, `FederatedConnectorSource`) but does not by itself provide classification/owner values; those are operational governance inputs. 
- Inventory is retrieval-first; no code evidence in this phase confirms an internal model training corpus managed by this repository.

## Verification Labels
- **Verified:** Connector source types exist in code.
- **Partially Confirmed:** Retrieval metadata persistence surfaces documented.
- **Unknown:** End-to-end owner/classification registry and lifecycle SLAs.
