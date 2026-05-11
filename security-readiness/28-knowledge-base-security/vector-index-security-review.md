# Build Priority 20 - Vector Index Security Review

Date: 2026-05-11

## Scope
Review vector index isolation, authorization dependencies, and misuse paths affecting retrieval confidentiality.

## Review matrix
| Area | Security requirement | Evidence needed | Status |
|---|---|---|---|
| Index namespace/isolation model | Prevent cross-tenant/cross-department retrieval bleed | Index configuration and tenancy model review | **Unknown** |
| Filter binding at query time | Enforce identity/department constraints before result return | Retriever query construction and test traces | **Unknown** |
| Backfill/reindex correctness | Maintain auth metadata across reindex jobs | Reindex logs + metadata comparison tests | **Unknown** |
| Debug/admin query safeguards | Prevent privileged bypass in normal user paths | Route/mode gating validation | **Partially Confirmed** |

## Planned tests
1. **Cross-department vector retrieval test** (negative)
   - Validate no Dept-B vectors returned to Dept-A identity under similarity pressure.
2. **Metadata-required retrieval test**
   - Force query path to fail closed when mandatory auth metadata is absent.

## Risk statement
- Vector retrieval without strong filter coupling is a **Critical** confidentiality risk.
- No index control should be marked present without executable evidence.
