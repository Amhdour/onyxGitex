| Control Claim | Evidence Required | Current Evidence | Status | Launch Implication |
|---|---|---|---|---|
| Agent tools are inventoried. | Tool inventory with mapped controls. | Policy file exists; runtime execution absent. | NOT_ENOUGH_EVIDENCE | Inventory runtime linkage unverified. |
| Tools are mapped to risk levels. | Risk-tier mapping and enforcement outputs. | No runtime risk-tier evidence in package. | NOT_ENOUGH_EVIDENCE | Risk enforcement claims not allowed. |
| Tool calls are authorized before execution. | Allow/deny runtime traces and policy test logs. | No runtime traces committed. | NOT_ENOUGH_EVIDENCE | Authorization enforcement unverified. |
| Sensitive tools require human approval. | Approval-required and approval-present logs. | No human-confirmation logs. | NOT_ENOUGH_EVIDENCE | Sensitive gating unverified. |
| Unknown tools fail closed. | Denied unknown tool runtime output. | No denied-tool runtime log attached. | NOT_ENOUGH_EVIDENCE | Fail-closed unknown-tool claim not allowed. |
| Missing identity fails closed. | Deny logs for missing identity path. | No runtime deny artifact attached. | NOT_ENOUGH_EVIDENCE | Identity fail-closed unverified. |
| Policy decisions are logged. | Runtime decision log with policy outcome. | No runtime decision logs attached. | NOT_ENOUGH_EVIDENCE | Auditability incomplete. |
| Runtime traces support auditability. | Trace artifacts with timestamps and commit references. | runtime-trace.json missing. | NOT_ENOUGH_EVIDENCE | Launch gate remains NO-GO. |
