| Artifact | Required | Present | Status | Notes |
|---|---|---|---|---|
| pytest-output.txt | Yes | Yes | BLOCKED | Pytest attempted; import failed with missing `fastapi_users` dependency. |
| backend-logs.txt | Yes | No | MISSING | Backend runtime logs were not captured in this execution attempt. |
| docker-compose-ps.txt | Yes | Yes | NOT_AVAILABLE | Docker CLI unavailable; file records `DOCKER_NOT_AVAILABLE`. |
| env-manifest-redacted.txt | Yes | Yes | PRESENT | Redacted environment manifest captured with secret-like keys masked. |
| git-commit.txt | Yes | Yes | PRESENT | Commit captured at runtime attempt. |
| test-command.txt | Yes | Yes | PRESENT | Exact executed pytest command captured. |
| timestamp.txt | Yes | Yes | PRESENT | UTC execution timestamp captured. |
| runtime-status.txt | Yes | Yes | BLOCKED | Status recorded as `DEPENDENCY_FAILURE`. |
| execution-precheck.md | Yes | Yes | PARTIAL | Precheck completed; Docker/Compose unavailable in environment. |
| final-run-status.json | Yes | Yes | BLOCKED | Updated to BLOCKED with `blocker_type=DEPENDENCY_FAILURE`. |
