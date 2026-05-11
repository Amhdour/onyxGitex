# Build Priority 20 - Knowledge Base Inventory

Date: 2026-05-11

## Scope
Inventory knowledge-base security surfaces that affect retrieval authorization, data integrity, and lifecycle risk.

## Inventory summary
| Asset / surface | Security relevance | Evidence source needed | Current status |
|---|---|---|---|
| Connector-synced source documents | May contain cross-department confidential content | Connector + source system mapping, document ACL metadata samples | **Partially Confirmed** |
| Parsed chunks in document/chunk stores | Authorization must hold after document splitting | Chunk schema review + retrieval auth tests | **Unknown** |
| Vector index entries | Embeddings can leak semantic access if filters fail | Index isolation review + cross-tenant retrieval tests | **Unknown** |
| Metadata filter fields (dept/team/source/access) | Primary retrieval enforcement boundary in filtered search | Filter config review + negative tests | **Partially Confirmed** |
| Re-indexing and stale deletion jobs | Stale content may remain retrievable after source revocation | Sync/delete job evidence + stale retrieval tests | **Unknown** |
| Document trust signals / ingestion validation | Poisoned content can manipulate retrieved answers | Provenance controls + poisoning tests | **Unknown** |

## Key findings
- Retrieval leakage across department boundaries is a **Critical** risk until verified tests demonstrate fail-closed behavior.
- Knowledge-base security controls cannot be marked **Verified** without code/config evidence and executable tests.
- Current maturity in this artifact is inventory-only; implementation confirmation remains pending.

## Next evidence steps
1. Complete document permission inheritance review and chunk-level authorization review.
2. Execute negative retrieval tests for cross-department boundaries.
3. Validate stale and poisoned document controls in controlled test data.
