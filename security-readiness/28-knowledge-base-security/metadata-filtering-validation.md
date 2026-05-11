# Build Priority 20 - Metadata Filtering Validation

Date: 2026-05-11

## Scope
Validate that metadata filters enforce access boundaries for retrieval requests.

## Validation checklist
| Check | Expected behavior | Test mapping | Status |
|---|---|---|---|
| Identity-bound filter construction | User/group/department attributes are attached to retrieval query | Metadata filtering test | **Unknown** |
| Mandatory filter enforcement | Retrieval fails closed if required filters missing | Metadata filtering test (negative) | **Unknown** |
| Filter behavior under ambiguous terms | Semantic overlap does not bypass metadata boundaries | Cross-department retrieval test | **Unknown** |
| Filter behavior in fallback modes | Alternate retrieval paths preserve same filter requirements | Integration trace review | **Unknown** |

## Planned tests
1. **Metadata filtering test (positive/negative)**
   - Positive: authorized metadata returns expected chunks.
   - Negative: same query with unauthorized metadata returns no restricted chunks.
2. **Mandatory-filter fail-closed test**
   - Remove required metadata fields in test harness.
   - Expect explicit deny / empty result behavior.

## Acceptance alignment
- Unknown controls remain labeled **Unknown** until tests run.
- Any metadata bypass that enables leakage is classified **Critical**.
