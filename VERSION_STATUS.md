# onyxGitex Version Status

## Executive Summary
Current repo status:
- V1 strong.
- V1.5 evidence-consistency achieved.
- V2-alpha started.
- V2.1 is the next technical milestone.
- V3 staging not verified.
- V4 client production template only.
- Production readiness not claimed.
- Client readiness not claimed.
- Global launch gate remains NO_GO.

## Version 2.1 — Artifact-Aware Evidence Validator + P0 Runtime Proof Pack
- **Status:** In progress / next milestone.
- **Purpose:** Upgrade from metadata-only consistency to artifact-aware validation discipline.
- **What it adds:** P0 runtime proof-pack structure, per-control evidence schema, and validator checks for artifact existence and claim-boundary enforcement.
- **Allowed claims:** V2.1 defines artifact-aware validation and P0 proof structure.
- **Blocked claims:** GO, production-ready, client-ready, staging-verified, compliance-certified.
- **Required evidence:** Executed P0 tests + runtime logs + pytest output + populated evidence-result files.
- **Why NO_GO remains:** P0 runtime boundary proofs are structured but not executed/passed.


## Version 2.2 — Execute P0 Runtime Boundary Proof
- **Status:** PARTIAL
- V2.2 is partially achieved: P0 proof execution was attempted and evidence was collected for available checks, but remaining failed/blocked controls keep the launch gate at NO_GO.
- **Execution summary:** 0 passed, 7 failed, 0 blocked, 0 not executed.
- **Launch-gate impact:** NO_GO remains.
- **Next milestone:** V2.3 CI Evidence Replay.
