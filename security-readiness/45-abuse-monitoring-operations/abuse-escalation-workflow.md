# Abuse Escalation Workflow

Date: 2026-05-11  
Status: Draft (Operations Workflow)

## Objective

Define the end-to-end workflow from abuse signal detection to closure, with explicit audit log and alert integration.

## Workflow Steps

1. **Detect**  
   - Source: prompt/retrieval/tool audit streams and detector rules.  
   - Output: normalized abuse signal with severity and confidence.

2. **Correlate**  
   - Join signal with identity/session, authorization decisions, and related events.  
   - Generate correlation ID.

3. **Alert**  
   - Route to alerting platform based on severity:  
     - Critical/High -> immediate on-call page  
     - Medium/Low -> queue + digest.

4. **Contain (Fail Closed)**  
   - For High/Critical: deny risky action, constrain retrieval/tool permissions, optionally terminate session.

5. **Triage**  
   - Analyst reviews evidence package and classifies: Verified, Partially Confirmed, Unknown.

6. **Escalate**  
   - Criteria: repeated attempts, sensitive data target, privileged tool misuse, or policy tampering.  
   - Create abuse case and assign owner.

7. **Remediate**  
   - Apply policy updates, blocklists, connector restrictions, or monitoring thresholds.

8. **Review & Close**  
   - Abuse Case Review Board validates closure evidence and residual risk.

## Severity SLA Targets

- Critical: acknowledge <= 15 minutes; containment <= 30 minutes.
- High: acknowledge <= 30 minutes; containment <= 4 hours.
- Medium: acknowledge <= 4 hours; action <= 2 business days.
- Low: review in weekly backlog.

## Required Evidence for Escalation

- Audit event IDs (prompt, retrieval, tool, policy decision)
- Alert IDs and timestamps (UTC)
- Analyst notes and confidence label
- User/session identifiers (redacted when exported)
- Final disposition and owner sign-off
