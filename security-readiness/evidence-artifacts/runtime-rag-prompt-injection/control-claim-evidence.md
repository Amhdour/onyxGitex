| Control Claim | Evidence Required | Current Evidence | Status | Launch Implication |
|---|---|---|---|---|
| Retrieved malicious instructions cannot override authorization controls. | Runtime logs showing deny behavior under injected instructions. | Scenario plan only. | NOT_ENOUGH_EVIDENCE | No runtime safety claim allowed. |
| Unauthorized cross-department retrieval is blocked. | Denial outputs and policy logs for cross-department requests. | No runtime denial artifact committed. | NOT_ENOUGH_EVIDENCE | Launch remains NO-GO. |
| Citation laundering is prevented. | Output proving citations are constrained to authorized sources. | No runtime citation laundering artifacts. | NOT_ENOUGH_EVIDENCE | Cannot claim citation integrity at runtime. |
| Hidden source chunks are not disclosed. | Runtime outputs showing refusal for hidden-chunk disclosure attempts. | No executed output attached. | NOT_ENOUGH_EVIDENCE | Confidentiality control remains unverified. |
| Tool/retrieval escalation via prompt injection is denied. | Runtime traces showing deny on escalation attempts. | No runtime trace committed. | NOT_ENOUGH_EVIDENCE | Escalation resistance unverified. |
