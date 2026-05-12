| Artifact | Required | Present | Status | Notes |
|---|---|---|---|---|
| pytest-output.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Runtime pytest output not collected yet. |
| backend-logs.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Backend runtime logs not collected yet. |
| docker-compose-ps.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Runtime environment service status missing. |
| env-manifest-redacted.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Redacted env manifest not collected yet. |
| git-commit.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Runtime execution commit capture not collected yet. |
| test-command.txt | Yes | Yes | COLLECTION_ONLY | Reproduction command documented, not executed. |
| timestamp.txt | Yes | No | NOT_ENOUGH_EVIDENCE | Runtime execution timestamp not collected yet. |
| final-run-status.json | Yes | Yes | COLLECTION_ONLY | Status intentionally set to NOT_RUN. |
