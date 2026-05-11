# Agent Kill-Switch Runbook

Date: 2026-05-11
Status: **Operational Draft**

## Objective
Rapidly stop unsafe agent/tool execution while preserving forensic evidence.

## Trigger Conditions
- Suspected unauthorized tool execution.
- Data exfiltration indicator.
- High-risk tool execution without required human approval.
- MCP credential abuse or third-party side-effect incident.

## Kill-Switch Actions (Order)
1. Disable affected tools via admin status endpoint/path (`/admin/tool/status`) or DB-level disable controls.
2. Remove tool bindings from active assistants.
3. Disable/revoke affected MCP server connections and OAuth credentials.
4. Quarantine/stop code-execution workers or sandbox managers.
5. Preserve logs/traces and capture incident timestamp + actor scope.

## Minimum Audit Evidence to Capture
- Trigger source and timestamp.
- Tool names and call IDs involved.
- Requesting actor, tenant, assistant IDs.
- Policy decision state (approved/denied/missing).
- Kill-switch operator and exact actions taken.

## Recovery Criteria
- Root cause identified and documented.
- Required controls implemented or validated.
- Control tests pass:
  - unauthorized call blocked,
  - missing approval blocked,
  - high-risk call blocked,
  - audit event emitted.
- Security sign-off recorded.

## Unknowns / Gaps
- No single documented operational command set for all runtime components was confirmed in this pass.
- Environment-specific stop procedures (k8s vs local) must be attached before production readiness claim.
