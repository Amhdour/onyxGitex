# Model Abuse Incident Playbook (Priority 14)

Date: 2026-05-11
Status: Operational Draft (Client-Facing)

## Severity mapping
Use `ai-incident-classification-model.md`; elevate to Sev-1/Sev-2 for sustained abuse, policy bypass, or external harm risk.

## Detection signals
- Elevated harmful/jailbreak attempt rates across tenants or specific accounts.
- Repeated generation-policy violations in audit and moderation logs.
- Runtime traces show repeated fallback to less restrictive pathways.
- Abuse reports from client administrators.

## Immediate containment steps
1. Apply account/session-level throttling or suspension.
2. Increase moderation strictness and block high-risk prompt classes.
3. Disable vulnerable model features or downgrade capability tier.
4. Coordinate with abuse/security teams for active monitoring.

## Evidence to preserve
- Moderation/audit logs with policy categories and outcomes.
- Prompt/response samples (redacted) tied to trace IDs.
- Session/account metadata, rate-limits, and enforcement actions.
- Model version/config and safety-policy snapshots during incident.
- Tool/retrieval events if abuse attempted lateral movement.

## Escalation path
- Security Operations -> Abuse Response Lead -> Incident Commander -> Legal/Policy -> Client Success.

## Client communication notes
- Summarize abuse pattern and account scope.
- Provide protective controls applied and expected access impacts.
- Give recommendations for client-side governance follow-up.

## Remediation
- Tune abuse heuristics and detection thresholds.
- Add tenant-specific abuse controls where contractually required.
- Expand safety evaluation scenarios with observed abuse patterns.
- Improve administrator alerts and self-service enforcement controls.

## Post-incident review requirements
- Confirm recurrence prevention controls are tested.
- Record false-positive/false-negative analysis.
- Track residual abuse risk and governance actions.
