# Version 2.2.1 — Fix P0 Execution Environment and Failure Classification

## 1. Purpose
Correct P0 failure classification so setup/import blockers are not mislabeled as security-control failures.

## 2. Why V2.2.1 exists
V2.2 marked seven controls as failed even though pytest failed during import/collection.

## 3. What went wrong in V2.2
Pytest exited before meaningful assertions due to missing dependency `fastapi_users`.

## 4. Correct interpretation of the previous result
P0 execution was attempted, but controls were blocked before assertions.

## 5. Difference between assertion failure and execution blocker
Assertion failure means assertions were reached and failed. Execution blocker means assertions were never reached.

## 6. Updated result taxonomy
PASSED, FAILED_ASSERTION, FAILED_TEST_RUNTIME, BLOCKED_IMPORT_DEPENDENCY, BLOCKED_TEST_COLLECTION, BLOCKED_ENVIRONMENT, BLOCKED_COMMAND_MISSING, NOT_EXECUTED.

## 7. Expected files affected
Scripts, per-control evidence files, canonical manifests, launch-gate and status files, runbook, backlog, claims.

## 8. Acceptance criteria
Classification logic updated, evidence regenerated, validator updated, NO_GO preserved.

## 9. Launch-gate impact
Launch remains NO_GO.

## 10. Allowed claims
Classification corrected; import/setup blockers no longer mislabeled; missing dependency documented; NO_GO preserved.

## 11. Blocked claims
No claims of passed controls, functional control failure, production/client/staging readiness, compliance certification, or safe launch.

## 12. Next milestone: V2.2.2 Pass Lightweight Local Harness Tests
After dependency/test isolation correction, run lightweight harness tests and collect meaningful assertion evidence.
