# Version 2.2.2-hotfix — Correct Mixed-Result P0 Status Wording

## 1. Purpose
Correct stale aggregate wording so V2.2.2 reflects the actual mixed P0 result without overclaiming.

## 2. Why this hotfix exists
Stale V2.2.1-style language remained in aggregate status metadata even after four P0 controls passed at LOCAL_HARNESS level.

## 3. What was stale or misleading
Legacy wording implied that no P0 controls were proven passed, which contradicted current counters and per-control evidence files.

## 4. Correct V2.2.2 interpretation
“This hotfix corrects stale V2.2.1-style aggregate wording that incorrectly implied no P0 controls were proven passed. The V2.2.2 evidence shows four controls passed at LOCAL_HARNESS level and three controls remain blocked by import dependency setup. This does not prove full Onyx runtime enforcement, CI evidence, staging verification, production readiness, client readiness, or launch GO.”

## 5. What this hotfix changes
- Corrects aggregate wording in P0 final status.
- Updates runner wording logic for mixed outcomes.
- Aligns canonical status, launch-gate, manifest, claim, control, backlog, and README documents with mixed-result evidence.

## 6. What this hotfix does not change
- Does not convert blocked controls into passed controls.
- Does not add full runtime, CI, staging, production, or client proof.
- Does not change launch decision from NO_GO.

## 7. Launch-gate impact
Launch decision remains **NO_GO** because three required P0 controls are still blocked and full runtime evidence is missing.

## 8. Allowed claims after hotfix
- V2.2.2 produced LOCAL_HARNESS evidence for four P0 controls.
- Four P0 controls reached assertions and passed at helper-level.
- Three P0 controls remain blocked by import dependency setup.
- Launch remains NO_GO.

## 9. Blocked claims after hotfix
- All seven P0 controls passed.
- Full Onyx runtime proof exists.
- CI proof exists.
- Staging verification exists.
- Production readiness exists.
- Client readiness exists.
- Compliance certification exists.
- Safe launch is supported.

## 10. Next milestone: V2.2.3 Real Onyx Runtime / Integration P0 Tests
Resolve backend dependency/runtime blockers and execute real runtime/integration evidence for the remaining blocked controls.
