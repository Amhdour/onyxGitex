# AI Trust & Security Readiness Lab for RAG and Autonomous Agents

This repository is a portfolio and readiness-engineering lab. It is not a production certification and does not claim that Onyx or any derived system is production-secure.

## Version 2.1 — Artifact-Aware Evidence Validator + P0 Runtime Proof Pack
- Adds artifact-aware evidence consistency validation.
- Adds P0 runtime boundary proof structure for seven controls.
- Keeps conservative claim boundaries and explicit NO_GO blockers.

### Inspect V2.1
- `security-readiness/meta/canonical-version-status.json`
- `security-readiness/evidence-artifacts/canonical-evidence-manifest.json`
- `security-readiness/evidence-artifacts/p0-runtime-boundary-proof/`
- `security-readiness/launch-gates/canonical-launch-gate-decision.json`

### Run validator
`python3 security-readiness/scripts/validate_readiness_evidence.py`

### Current P0 status
`NOT_EXECUTED` (structure-only, no runtime pass evidence yet).

### Current launch gate
`NO_GO`.

### Next step after V2.1
V2.2 — Execute P0 Runtime Boundary Proof.
