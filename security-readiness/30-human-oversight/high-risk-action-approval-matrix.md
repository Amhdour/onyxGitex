# Build Priority 22 — High-Risk Action Approval Matrix

Date: 2026-05-11
Status: Proposed

## Risk Tiers
- **Low**: No sensitive data impact; reversible; no external side effects.
- **Moderate**: Limited operational impact; no policy exceptions.
- **High**: Sensitive-data or high-impact tool action.
- **Critical**: Potential boundary bypass, broad data exposure, or launch-gate blocker.

## Approval Matrix
| Action Type | Risk Tier | Required Approvers | Required Evidence | Escalation Required |
|---|---|---|---|---|
| Non-sensitive prompt/config update | Low | Primary Reviewer | Change diff + targeted test result | No |
| Tool permission expansion (internal systems) | Moderate | Primary Reviewer + Security Reviewer | Risk assessment + control mapping + test evidence | If disagreement |
| High-risk tool execution (write/delete/admin) | High | Primary Reviewer + Security Reviewer | Abuse-case test evidence + rollback plan + runtime traceability proof | Yes if evidence gap |
| Sensitive-data response exception handling | High | Security Reviewer + Incident Commander | Data classification reference + justification + containment controls | Yes |
| Launch with unresolved critical finding | Critical | Launch Gate Approver + Security Reviewer + Incident Commander | Explicit risk acceptance + time-bound mitigation plan + executive owner | Mandatory |
| Manual override affecting launch gate | Critical | Incident Commander + Security Reviewer + Launch Gate Approver | Override record + compensating controls + expiry | Mandatory |

## Enforcement Rule
If required approvers or evidence are absent, decision outcome is automatically **Rejected** or **Deferred** (fail-closed).
