| Artifact | Required | Present | Status | Notes |
|---|---|---|---|---|
| policy-test-output.txt | Yes | No | NOT_ENOUGH_EVIDENCE | OPA runtime output missing. |
| allowed-tool-call-log.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Allow path runtime log missing. |
| denied-tool-call-log.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Deny path runtime log missing. |
| human-confirmation-log.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Human approval evidence missing. |
| fail-closed-log.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Fail-closed runtime evidence missing. |
| runtime-trace.json | Yes | No | NOT_ENOUGH_EVIDENCE | Trace evidence missing. |
| git-commit.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Execution commit capture missing. |
| test-command.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Executed command capture missing. |
| timestamp.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Execution timestamp missing. |
| final-run-status.json | Yes | Yes | COLLECTION_ONLY | Status intentionally NOT_RUN. |
