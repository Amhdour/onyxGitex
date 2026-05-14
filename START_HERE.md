# START HERE

This repository is an AI Trust & Security Readiness portfolio lab and production-readiness starter kit. It is not production proof, not client verification, and not a compliance certification.

## Current status
- Current status: V1.5 / V2-alpha moving toward V2.1.
- Current launch-gate decision: NO_GO.

## Safe claims
This repository demonstrates a structured method for assessing RAG and agent readiness through architecture mapping, threat modeling, control design, evidence manifests, validation scripts, and launch-gate decisions.

## Blocked claims
This repository does not prove production security, client deployment readiness, staging runtime verification, or regulatory certification.

## Folder map
- `security-readiness/` canonical readiness workspace
- `production-readiness/` production-track starter kit artifacts
- `security-readiness/evidence-artifacts/` evidence manifests, validation outputs, and proof-pack folders
- `security-readiness/scripts/` readiness validation utilities

## How to review evidence
1. Read `VERSION_STATUS.md` and `security-readiness/meta/canonical-version-status.json`.
2. Read launch gate decision JSON/MD.
3. Review canonical evidence manifest JSON/MD.
4. Inspect `security-readiness/evidence-artifacts/p0-runtime-boundary-proof/`.

## Run validator
`python3 security-readiness/scripts/validate_readiness_evidence.py`

## What validator proves
The validator checks evidence metadata and artifact consistency. It does not prove that the full system is production secure.

## What validator does not prove
- Production readiness
- Client verification
- Staging verification
- Compliance certification
- Safe-to-launch outcome

## What V2.1 adds
- Artifact-aware evidence-path checks
- P0 runtime proof-pack structure for seven critical controls
- Explicit blocker tracking for launch-gate NO_GO

## Next technical milestone
- V2.2 — Execute P0 Runtime Boundary Proof.
