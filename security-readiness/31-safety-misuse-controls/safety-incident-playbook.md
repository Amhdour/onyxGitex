# Safety Incident Playbook

## Purpose
Define response workflow for detected assistant misuse or safety control failures.

## Incident Types
- IT-01 Private document extraction attempt.
- IT-02 Employee data misuse attempt.
- IT-03 Legal/financial overreliance risk event.
- IT-04 Prompt injection campaign.
- IT-05 Policy bypass/jailbreak pattern.
- IT-06 Tool misuse or exfiltration attempt.
- IT-07 Sensitive operational data exposure attempt.
- IT-08 Policy decision logging failure.

## Monitoring Signal Linkage

| Incident Type | Primary Signals | Secondary Signals |
|---|---|---|
| IT-01 | AMS-01 | AMS-05, AMS-08 |
| IT-02 | AMS-02 | AMS-01, AMS-08 |
| IT-03 | AMS-03 | AMS-08 |
| IT-04 | AMS-04 | AMS-01, AMS-07 |
| IT-05 | AMS-05 | AMS-04, AMS-08 |
| IT-06 | AMS-06 | AMS-05, AMS-08 |
| IT-07 | AMS-07 | AMS-04, AMS-08 |
| IT-08 | AMS-08 | Any concurrent AMS-* |

## Response Workflow
1. **Detect**: Alert generated from AMS signal thresholds.
2. **Triage**: Confirm true positive, classify incident type and severity.
3. **Contain**: Disable affected tool routes/policies/session tokens as needed.
4. **Eradicate**: Remove root cause (rule gaps, policy misconfig, connector mis-scope).
5. **Recover**: Re-enable capabilities after control verification.
6. **Review**: Conduct post-incident analysis with evidence and control improvement actions.

## Required Evidence Per Incident
- Event timeline with UTC timestamps.
- Request/response identifiers and user/session metadata.
- Triggered control IDs and rule IDs.
- Containment actions taken and approver.
- Residual risk and follow-up owners.

## Escalation Matrix
- High severity (data exposure risk/tool exfiltration): immediate security on-call + leadership notify.
- Medium severity (overreliance/policy bypass attempts with no exposure): security queue within business day.
- Observability defect (IT-08): platform owner and security engineering notify; treat as control integrity risk.

## Communications
- Internal notification uses redacted incident summary.
- External communication requires legal/comms approval.

## Verification Status
- **Verified**: Playbook and signal linkage documented.
- **Partially Confirmed**: Drill execution evidence not included in this artifact.
