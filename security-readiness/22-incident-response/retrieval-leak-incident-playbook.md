# Retrieval Leak Incident Playbook (Priority 14)

Date: 2026-05-11
Status: Operational Draft (Client-Facing)

## Severity mapping
Use `ai-incident-classification-model.md` to assign Sev-1 through Sev-4. Default to Sev-1 until exposure scope is bounded.

## Detection signals
- Audit logs show access decisions inconsistent with user/tenant policy.
- Retrieval events show document IDs from unauthorized connector or tenant scope.
- Trace shows retrieval authorization fallback, bypass, or unexpected allow path.
- User/client report of seeing restricted content in answer.

## Immediate containment steps
1. Activate incident bridge; assign Incident Commander.
2. Fail closed for affected retrieval paths:
   - disable affected connector(s),
   - enforce strict ACL gating,
   - block high-risk query classes if needed.
3. Preserve volatile evidence before cleanup.
4. Rotate any related credentials/tokens if compromise suspected.

## Evidence to preserve
- Audit log entries for authN/authZ and policy decisions (with timestamps).
- Retrieval events: query text hash, document IDs, access decision reason, source connector.
- Runtime traces with trace IDs spanning request -> retrieval -> response.
- Response artifacts returned to user (redacted) and session metadata.
- Change history for retrieval policy/config around incident window.

## Escalation path
- Security On-call -> Incident Commander -> Data Protection/Privacy -> Legal -> Client Success -> Executive Sponsor.

## Client communication notes
- Acknowledge incident and time first detected.
- State what is known vs unknown; avoid unverified impact claims.
- Provide immediate containment actions completed.
- Commit next update interval (e.g., every 4 hours for Sev-1/Sev-2).
- Include guidance for client-side monitoring actions if relevant.

## Remediation
- Fix authorization logic or policy mapping root cause.
- Add regression tests for tenant/document boundary enforcement.
- Add detection rules for cross-tenant retrieval anomalies.
- Re-validate least-privilege connector permissions.

## Post-incident review requirements
- Root cause, blast radius, MTTD/MTTR, evidence completeness.
- Control gaps mapped to owners and due dates.
- Readiness impact: Verified / Partially Confirmed / Unknown controls.
