# Evidence Artifacts Reproducibility Guide

## Purpose
`security-readiness/evidence-artifacts/` stores execution-linked artifacts used to support auditable AI trust and security readiness claims.

## Evidence integrity rules
- Never fabricate logs, traces, screenshots, timestamps, or PASS states.
- Record exact commands and environment constraints.
- Preserve missing evidence as explicit gaps.

## No-fabrication rule
A status may not be changed to PASS without real executed artifacts committed in-repo or attached from CI artifact outputs.

## How to add a new evidence package
1. Create a dedicated folder.
2. Add package README with scope and status.
3. Add `final-run-status.json`.
4. Add evidence manifest and claim mapping.
5. Add runtime collection script when execution is expected.
6. Record missing artifacts as `NOT_ENOUGH_EVIDENCE` until collected.

## Required files for each evidence package
- README.md
- final-run-status.json
- evidence-manifest.md
- control-claim-evidence.md
- test-command.txt (or test plan where script is not yet available)

## Status vocabulary
- NOT_RUN
- RUNNING
- PASS
- FAIL
- BLOCKED
- PARTIAL
- NOT_ENOUGH_EVIDENCE
- QUEUED
- QUEUED_NO_COLLECTION
- COLLECTION_ONLY
- NO_RUNTIME_COLLECTION
