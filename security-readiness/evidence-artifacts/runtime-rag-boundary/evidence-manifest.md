| Artifact | Required | Present | Status | Notes |
|---|---|---|---|---|
| dependency-precheck.md | Yes | Yes | PRESENT | Dependency declaration/import precheck completed from command evidence. |
| dependency-resolution.md | Yes | Yes | PRESENT | Root cause and resolution attempt documented. |
| dependency-install-output.txt | Yes | Yes | BLOCKED | `uv sync` failed on CPython 3.14 due to `onnxruntime` wheel incompatibility. |
| pytest-output.txt | Yes | Yes | BLOCKED | Pytest attempted; import failed with missing `fastapi_users`. |
| backend-logs.txt | Yes | No | MISSING | Backend runtime logs not captured because test did not execute. |
| docker-compose-ps.txt | Yes | Yes | NOT_AVAILABLE | Docker CLI unavailable; file records `DOCKER_NOT_AVAILABLE`. |
| env-manifest-redacted.txt | Yes | Yes | PRESENT | Redacted environment manifest captured. |
| git-commit.txt | Yes | Yes | PRESENT | Commit captured at runtime attempt. |
| test-command.txt | Yes | Yes | PRESENT | Exact pytest command captured. |
| timestamp.txt | Yes | Yes | PRESENT | UTC timestamp captured. |
| runtime-status.txt | Yes | Yes | BLOCKED | Status remains `DEPENDENCY_FAILURE` from script output. |
| execution-precheck.md | Yes | Yes | PARTIAL | Precheck completed; runtime environment remains limited. |
| runtime-execution-report.md | Yes | Yes | PARTIAL | Includes dependency resolution attempt and current blocker state. |
| final-run-status.json | Yes | Yes | BLOCKED | Valid JSON updated to `BLOCKED_PACKAGE_RESOLUTION`. |
