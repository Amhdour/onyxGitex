# Version 2.2.2 — Pass Lightweight Local Harness Tests

## 1. Purpose
Isolate selected P0 tests from heavy backend pytest setup and produce real LOCAL_HARNESS evidence.
## 2. Why V2.2.2 exists
V2.2.1 showed collection/import blockers before assertions.
## 3. Relationship to V2.2.1
V2.2.1 corrected failure classification; V2.2.2 adds assertion-reaching harness execution.
## 4. What lightweight local harness evidence means
Helper-level tests run locally with `PYTHONPATH=backend`, assertions reached, outputs captured.
## 5. What lightweight local harness evidence does not mean
Not full runtime, CI, staging, production, or client proof.
## 6. Controls targeted for LOCAL_HARNESS
P0-CL-001, P0-PI-001, P0-TA-001, P0-FC-001.
## 7. Controls expected to remain blocked until full runtime
P0-RA-001, P0-AL-001, P0-TT-001.
## 8. Execution model
Run direct harness tests, run P0 controller, run validator, then update canonical artifacts.
## 9. Evidence outputs
Per-control pytest output, runtime-log note, evidence-result.json, and p0 final-status.json.
## 10. Pass/fail/block rules
Pass requires exit 0 and assertions reached. Import/collection blockers stay blocked.
## 11. Launch-gate impact
NO_GO remains unless all required P0 criteria are satisfied.
## 12. Allowed claims
LOCAL_HARNESS evidence for passing controls; explicit blockers for remaining controls.
## 13. Blocked claims
No claims of full runtime, CI, staging, production, client readiness, compliance, or safe launch.
## 14. Next milestone: V2.2.3 Real Onyx Runtime / Integration P0 Tests
Execute integration/runtime boundary tests on real Onyx paths.
