# Client Remediation Tracker

## Purpose
Track finding remediation from identification through verification and closure.

## Usage Notes
- One row per finding.
- Update weekly or upon material status change.
- Keep evidence links current and auditable.

## Tracker Template
| Finding ID | Title | Severity | Owner | Target Date | Current Status | Mitigation Plan | Verification Method | Evidence Link | Residual Risk | Client Decision |
|---|---|---|---|---|---|---|---|---|---|---|
| FR-001 | Example: Cross-project retrieval gap | High | [Client Owner] | YYYY-MM-DD | In Progress | Add project-level filter and deny on mismatch | Retest with negative/positive access cases | [Link/Ref] | Medium until retest | Pending |

## Status Definitions
- Open: identified, no remediation started.
- In Progress: remediation underway.
- Ready for Verification: implementation complete, awaiting test.
- Verified Closed: remediation validated by evidence.
- Accepted Risk: not remediated before launch; formally accepted.

## Evidence Limitation Language (Client-Facing)
A remediation item is not considered closed until verification evidence is reviewed. Planned or claimed fixes without validation remain open risk.

## Launch Gate Decision Language (Client-Facing)
Launch gate recommendation must reflect open items in this tracker. Critical/High items that are unresolved require either closure evidence or explicit risk acceptance by authorized stakeholders.
