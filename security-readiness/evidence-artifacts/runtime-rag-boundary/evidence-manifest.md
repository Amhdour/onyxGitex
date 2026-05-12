| Artifact | Required | Present | Status | Notes |
|---|---|---|---|---|
| python-runtime-precheck.md | Yes | Yes | PRESENT | Python compatibility precheck completed. |
| runtime-environment.md | Yes | Yes | PRESENT | Selected Python runtime and commands documented. |
| python-version.txt | Yes | Yes | PRESENT | Runner captured active interpreter details. |
| python-runtime-sync-output.txt | Yes | Yes | BLOCKED | `uv sync --python 3.12` failed downloading `numpy==2.4.1` (tunnel error). |
| dependency-precheck.md | Yes | Yes | PRESENT | Dependency declaration/import precheck retained. |
| dependency-resolution.md | Yes | Yes | PARTIAL | Updated with Python runtime follow-up. |
| dependency-install-output.txt | Yes | Yes | BLOCKED_PACKAGE_RESOLUTION | Prior cp314 blocker evidence retained. |
| pytest-output.txt | Yes | Yes | BLOCKED | Pytest still blocked at import (`fastapi_users` missing). |
| backend-logs.txt | Yes | No | MISSING | Test did not execute. |
| docker-compose-ps.txt | Yes | Yes | NOT_AVAILABLE | Docker unavailable in this environment. |
| env-manifest-redacted.txt | Yes | Yes | PRESENT | Redacted env manifest captured. |
| git-commit.txt | Yes | Yes | PRESENT | Current commit captured at run time. |
| test-command.txt | Yes | Yes | PRESENT | Exact command captured. |
| timestamp.txt | Yes | Yes | PRESENT | UTC timestamp captured. |
| runtime-status.txt | Yes | Yes | BLOCKED | Current status `DEPENDENCY_FAILURE`. |
| execution-precheck.md | Yes | Yes | PARTIAL | Precheck exists; runtime still blocked. |
| runtime-execution-report.md | Yes | Yes | PARTIAL | Includes Python runtime compatibility attempt. |
| final-run-status.json | Yes | Yes | BLOCKED | Valid JSON, evidence still blocked. |
