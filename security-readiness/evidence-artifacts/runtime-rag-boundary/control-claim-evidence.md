| Claim | Required runtime evidence | Latest observed evidence | Status | Notes |
|---|---|---|---|---|
| Document-set retrieval boundary is enforced. | Passing runtime boundary pytest execution. | Runtime test execution blocked before collection. | BLOCKED_NETWORK_DEPENDENCY_DOWNLOAD | No runtime PASS evidence. |
| Restricted documents are not exposed to unauthorized users. | Unauthorized retrieval deny evidence from executed test/logs. | Not executed due dependency sync blocker. | NOT_ENOUGH_EVIDENCE | Unverified. |
| Prompt-injected retrieved content cannot override access policy. | Prompt-injection runtime test evidence. | Not in scope for this PR. | NOT_ENOUGH_EVIDENCE | Unverified. |
| Responses are grounded in authorized sources only. | Runtime/source assertions from executed tests. | Not executed due blocker. | NOT_ENOUGH_EVIDENCE | Unverified. |
| Unauthorized retrieval attempts are logged. | Backend audit/runtime denied retrieval logs. | backend-logs artifact missing. | NOT_ENOUGH_EVIDENCE | Unverified. |
| Fail-closed behavior occurs when authorization state is uncertain. | Runtime deny-on-uncertainty evidence. | Not executed due blocker. | NOT_ENOUGH_EVIDENCE | Unverified. |
