# Audit Finding Tracker

## Purpose
Track audit findings from identification through remediation and closure with severity-driven prioritization.

## Status Definitions
- `Open`: Newly logged finding.
- `In Progress`: Remediation work underway.
- `Pending Validation`: Awaiting reviewer verification.
- `Closed`: Remediation validated and accepted.
- `Risk Accepted`: Not remediated; explicitly accepted by authority.

## Finding Tracker

| Finding ID | Review Criteria | Evidence Required | Reviewer | Status | Finding Severity | Remediation | Sign-off |
|---|---|---|---|---|---|---|---|
| AF-001 | Finding statement is specific and reproducible. | Reproduction steps, affected component reference. | Audit Reviewer | Open | Medium | Define precise repro and validation path. | Pending |
| AF-002 | Severity rating reflects realistic impact and likelihood. | Severity rationale, impact notes, threat linkage. | Risk Reviewer | Open | Medium | Reassess severity with threat model owner. | Pending |
| AF-003 | Remediation plan has owner and due date. | Task link, accountable owner, target completion date. | Control Owner | Open | High | Assign named owner and commit due date. | Pending |
| AF-004 | Closure requires verification evidence, not assertion. | Retest command + output, updated artifacts. | Validation Reviewer | Open | High | Perform retest and attach output evidence. | Pending |

## Detailed Finding Record Template
- Finding ID:
- Date Identified (YYYY-MM-DD):
- Source (internal audit, external review, test, red team, etc.):
- Description:
- Affected Control(s):
- Severity: `Critical` / `High` / `Medium` / `Low`
- Reviewer:
- Remediation Owner:
- Remediation Plan:
- Target Date:
- Validation Evidence:
- Final Status:
- Sign-off:
