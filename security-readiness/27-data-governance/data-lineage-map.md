# Data Lineage Map
Date: 2026-05-11 (UTC)
Scope: Retrieval corpus lineage
Status: Draft lineage with evidence gaps called out

## Retrieval Lineage (High-Level)
1. Source records originate in enterprise systems (e.g., SaaS/file/wiki/code connectors).
2. Connector/federated connector reads source records and normalizes into Onyx document structures.
3. Indexing pipeline transforms documents into searchable chunks/representations.
4. Query runtime retrieves candidate chunks and stores retrieval metadata (`search_doc`).
5. Response layer returns cited snippets/content to end user under authorization constraints.

## Lineage Controls Needed Per Hop
- **Source -> Ingestion:** source owner id, source object id, collection/workspace id, ingest timestamp.
- **Ingestion -> Index:** immutable document id linkage, chunk derivation version, parser/hash fingerprint.
- **Index -> Retrieval Event:** query id, user id/group claims, retrieved doc ids, policy decision id.
- **Retrieval Event -> Response:** response id, shown citation ids, redaction/deny markers.

## Evidence Status
- **Verified:** Source types for connector and federated connector paths are codified.
- **Partially Confirmed:** Retrieval metadata table surface (`search_doc`) documented in readiness artifacts.
- **Unknown:** Full runtime lineage traceability across all hops with immutable correlation ids.

## Evidence Needed
- Sample lineage trace from one query showing source doc id through response citations.
- Policy decision log joins proving retrieval authorization at query time.
- Deletion propagation trace proving source delete removes derived index artifacts.
