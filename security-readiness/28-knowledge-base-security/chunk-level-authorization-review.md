# Build Priority 20 - Chunk-Level Authorization Review

Date: 2026-05-11

## Scope
Evaluate whether authorization is enforced at chunk retrieval time, not only at source-document ingest time.

## Review matrix
| Control point | Security objective | Test / evidence method | Status |
|---|---|---|---|
| Chunk metadata contains access attributes | Support auth decisions per chunk | Schema and persisted chunk sample inspection | **Unknown** |
| Retrieval pipeline applies chunk auth filter | Prevent unauthorized chunk return | Unit/integration tests around retriever filters | **Unknown** |
| Reranker/context assembly preserves auth | Prevent post-filter leakage in context window | End-to-end query trace with denied chunks | **Unknown** |

## Planned tests
1. **Chunk-level authorization test**
   - Setup: one mixed document split into chunks with differing allowed groups.
   - Check: requester only receives allowed chunks; denied chunks absent from context.
2. **Cross-department vector retrieval negative test**
   - Setup: Dept-A and Dept-B corpora with overlapping terms.
   - Check: Dept-A query should never retrieve Dept-B chunks, even when semantically similar.

## Risk statement
- Missing chunk-level checks can bypass document-level controls and enable silent leakage.
- Retrieval leakage at chunk granularity is classified as **Critical**.
