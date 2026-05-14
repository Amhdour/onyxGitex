# onyxGitex Version Status

## Version 2.2.2-hotfix — Correct Mixed-Result P0 Status Wording
- **Purpose:** Correct stale V2.2.1-style aggregate wording while preserving actual V2.2.2 evidence.
- **Status:** ACHIEVED
- **Corrected interpretation:** V2.2.2-hotfix corrects stale aggregate wording from the earlier blocked state. The current V2.2.2 evidence shows four P0 controls passed at LOCAL_HARNESS level, while three controls remain BLOCKED_IMPORT_DEPENDENCY. This does not prove full Onyx runtime enforcement, CI replay, staging verification, production readiness, client readiness, compliance certification, or launch GO. The canonical launch gate remains NO_GO.
- **What changed:** aggregate wording, runner wording logic, validator contradiction checks, and canonical docs were aligned to mixed results.
- **What did not change:** 4 pass / 3 blocked split, zero LOCAL_RUNTIME passes, NO_GO, and false production/client/staging claims.

### P0 result table
- P0-RA-001 Retrieval Authorization: BLOCKED_IMPORT_DEPENDENCY
- P0-CL-001 Citation Leakage Boundary: PASSED / LOCAL_HARNESS
- P0-PI-001 Prompt-Injection Retrieval Boundary: PASSED / LOCAL_HARNESS
- P0-TA-001 Tool Authorization: PASSED / LOCAL_HARNESS
- P0-FC-001 Fail-Closed Behavior: PASSED / LOCAL_HARNESS
- P0-AL-001 Audit Logging: BLOCKED_IMPORT_DEPENDENCY
- P0-TT-001 Telemetry Tracing: BLOCKED_IMPORT_DEPENDENCY

### Allowed claims
- Four selected P0 controls have LOCAL_HARNESS evidence with assertions reached.
- Three P0 controls remain blocked by import dependency setup.
- Launch remains NO_GO.

### Blocked claims
- All seven P0 controls passed.
- Full runtime/CI/staging/production/client/compliance proof.
- Launch GO.

### Launch-gate impact
- Decision remains **NO_GO**.

### Next milestone
- **V2.2.3 — Real Onyx Runtime / Integration P0 Tests**.
