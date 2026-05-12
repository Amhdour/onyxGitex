| Control Claim | Evidence Required | Current Evidence | Status | Launch Implication |
|---|---|---|---|---|
| Document-set retrieval boundary is enforced. | Runtime test logs showing allowed and denied retrieval by identity/document set. | Structure only; no runtime logs committed. | NOT_ENOUGH_EVIDENCE | Cannot claim control enforcement. |
| Restricted documents are not exposed to unauthorized users. | Unauthorized retrieval denial output and citation-safe responses. | No executed denial artifacts in this package. | NOT_ENOUGH_EVIDENCE | Launch remains NO-GO. |
| Prompt-injected retrieved content cannot override access policy. | Injection scenario outputs with policy-deny evidence. | No runtime prompt-injection execution artifacts in this package. | NOT_ENOUGH_EVIDENCE | No runtime override-resistance claim permitted. |
| Responses are grounded in authorized sources only. | Runtime outputs with source attribution and authorization checks. | No grounded runtime response artifact committed. | NOT_ENOUGH_EVIDENCE | Cannot claim source-grounding enforcement. |
| Unauthorized retrieval attempts are logged. | Backend/audit logs with denied retrieval events. | backend-logs.txt absent. | NOT_ENOUGH_EVIDENCE | Audit completeness unverified. |
| Fail-closed behavior occurs when authorization state is uncertain. | Runtime logs showing deny-on-uncertainty behavior. | No fail-closed runtime artifact in this package. | NOT_ENOUGH_EVIDENCE | Fail-closed enforcement unverified. |
