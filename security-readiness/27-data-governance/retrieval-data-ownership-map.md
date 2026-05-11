# Retrieval Data Ownership Map
Date: 2026-05-11 (UTC)
Scope: Ownership clarity for retrieval data lifecycle
Status: Ownership model defined; implementation evidence partially confirmed

## Ownership Matrix

| Data object | System owner | Business/data owner | Security owner | Decision authority |
|---|---|---|---|---|
| Source documents in external systems | Source platform admins | Producing business unit | Enterprise security + compliance | Source owner approves access and retention baseline |
| Connector credentials/configuration | Onyx platform operations | N/A (service config) | Security engineering | Platform/security jointly approve connector enablement |
| Ingested/indexed retrieval artifacts | Onyx platform operations | Inherits source data owner | Security readiness owner | Source owner + security approve access model and deletion propagation |
| Retrieval metadata/events (`search_doc`, audit traces) | Onyx platform operations | Product owner for assistant | Security operations | Security defines retention + audit requirements |

## Required Governance Rule
No dataset is onboarded for retrieval unless all four ownership dimensions are filled and versioned.

## Known Gaps
- Named owners are not yet recorded per-connector/per-dataset in repository artifacts.
- Classification and retention are not enforced from a single source-of-truth catalog.

## Acceptance-Criteria Mapping
- Retrieval data ownership clarity: **Partially Confirmed** (role model defined, per-dataset assignments pending evidence).
