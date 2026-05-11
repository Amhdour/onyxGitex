# Build Priority 20 - Stale Document Risk Review

Date: 2026-05-11

## Scope
Review stale-document risks where outdated, revoked, or superseded content remains retrievable.

## Risk matrix
| Risk | Security/operational impact | Expected control | Status |
|---|---|---|---|
| Revoked document remains indexed | Unauthorized disclosure after access removal | Timely delete/re-index with fail-closed retrieval | **Unknown** |
| Superseded policy docs still retrieved | Unsafe or non-compliant guidance | Versioning and freshness-aware ranking | **Unknown** |
| Connector sync lag not surfaced | False confidence in current state | Freshness telemetry + user-visible staleness indicators | **Partially Confirmed** |

## Planned test
1. **Stale document retrieval test**
   - Setup: ingest doc, then revoke/delete at source.
   - Check: retrieval denies/omits stale doc after defined SLA window.
   - Evidence: sync job output, retrieval result snapshots before/after.

## Residual risk guidance
- Treat stale retrieval of revoked private content as **Critical** leakage risk.
- Mark readiness as blocked if stale-deletion evidence is missing.
