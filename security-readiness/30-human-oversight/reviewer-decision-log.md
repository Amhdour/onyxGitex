# Build Priority 22 — Reviewer Decision Log

Date: 2026-05-11
Status: Active Template

## Logging Standard
Use one row per decision event. Do not overwrite historical entries; append updates as new rows.

## Decision Log Table
| Decision ID | Date/Time (UTC) | Request ID | Action | Risk Tier | Reviewers (Role) | Decision | Evidence Links | Rationale | Conditions / Expiry | Escalated (Y/N) |
|---|---|---|---|---|---|---|---|---|---|---|
| HO-DEC-001 | [REDACTED] | [REDACTED] | Example: High-risk connector sync enablement | High | [REDACTED] (Primary), [REDACTED] (Security) | Deferred | [REDACTED] | Missing abuse-case test evidence | N/A | Y |

## Evidence Requirements per Entry
- At least one concrete evidence reference (file path, test command output, ticket, or run log).
- Named reviewer roles must match the approval matrix.
- Decision status must match allowed states from control model.

## Data Quality Rules
- If reviewer identity is unavailable, decision is invalid.
- If evidence link is empty, decision is invalid.
- If timestamp is missing, decision is invalid.

## Note
This template does not claim any real approval occurred; all sample values are redacted placeholders.
