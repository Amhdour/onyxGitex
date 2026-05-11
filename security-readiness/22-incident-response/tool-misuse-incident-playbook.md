# Tool Misuse Incident Playbook (Priority 14)

Date: 2026-05-11
Status: Operational Draft (Client-Facing)

## Severity mapping
Classify with `ai-incident-classification-model.md`; treat unauthorized state-changing tool actions as Sev-1.

## Detection signals
- Tool events show unauthorized caller, out-of-policy arguments, or denied actions followed by retries.
- Audit logs indicate privilege escalation or unusual service-account behavior.
- Trace shows unexpected tool routing from benign prompts.
- Rate anomalies in high-risk tool categories.

## Immediate containment steps
1. Disable impacted tool(s) or switch to read-only mode.
2. Revoke/rotate associated service credentials.
3. Enforce allowlist-only tool execution and stricter parameter validation.
4. Isolate affected sessions/users while preserving evidence.

## Evidence to preserve
- Tool event logs: caller ID, tool name, arguments (redacted), policy decision, execution result.
- Authorization and identity audit logs for implicated principals.
- Runtime traces connecting prompt -> policy -> tool call.
- Tool backend activity logs and downstream API transaction IDs.
- Configuration diffs for tool policy and permission scopes.

## Escalation path
- Security On-call -> Platform/Tool Owner -> Incident Commander -> Legal/Compliance (if regulated impact) -> Client Success.

## Client communication notes
- State impacted tool capabilities and any temporary disablement.
- Explain whether actions were blocked or executed.
- Share compensating controls and expected service implications.

## Remediation
- Tighten RBAC and capability-based tool authorization.
- Add pre-execution policy simulation and deny-by-default checks.
- Implement anomaly thresholds and auto-disable safeguards.
- Add regression tests for tool policy boundaries.

## Post-incident review requirements
- Verify no orphaned permissions remain.
- Confirm improved deny rates for abusive patterns.
- Document owner-approved re-enable criteria.
