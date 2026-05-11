# Retrieval Failure Handling Plan

Date: 2026-05-11  
Status: Draft (Pending Validation)

## Failure Modes
- Vector DB/index unavailable.
- Partial retrieval failure (subset of sources/timeouts).
- Connector-backed source unavailable.

## Detection Signals
- Index setup exhaustion / startup failure return.
- Retrieval endpoint non-success or parsing error.
- Zero-source condition detected by indexed-source precheck.

## Required Behavior
1. **Fail-Closed Conditions**
   - If authorization policy map or user identity is missing for retrieval decisions, deny access.
   - If policy engine errors for entitlement check, return deny/error (no document release).

2. **Graceful Degradation Conditions**
   - If retrieval backend temporarily unavailable: return empty results + explicit error field.
   - If no sources are indexed: return instructional message (no synthetic content).
   - If partial retrieval across sources: return available authorized subset + partial-results indicator.

## Controls
- Preserve structured error payloads in MCP search tool (documents array + error/message).
- Keep CE fallback route explicit and traceable when dedicated search is unavailable.
- Record per-source success/failure counts for connector-backed retrieval calls.

## Evidence Status
- Structured degraded retrieval responses: **Verified** (code inspection).
- Vector DB outage drill with measured behavior: **Unknown**.
- Partial retrieval marker behavior in production endpoint: **Partially Confirmed**.
