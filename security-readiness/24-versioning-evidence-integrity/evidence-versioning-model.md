# Evidence Versioning Model

## Objective
Define a deterministic, auditable versioning model for security-readiness evidence artifacts used in launch-gate decisions.

Date: 2026-05-11
Status: Draft for review

## Scope
Applies to evidence artifacts stored under `security-readiness/` (documents, logs, screenshots, manifests, and structured test outputs).

## Version Identifier
Use a monotonic semantic format:

`EVID-<domain>-<artifact>-v<major>.<minor>.<patch>`

Example: `EVID-authz-retrieval-policy-tests-v1.2.0`

## Change Semantics
- **Major**: Evidence meaning or acceptance criteria changes (e.g., control objective updated).
- **Minor**: New validated evidence added without invalidating prior interpretation.
- **Patch**: Metadata corrections, formatting, or reference/link fixes only.

## Required Metadata
Each evidence artifact version MUST include:
- Evidence ID
- Version
- Author/reviewer
- UTC timestamp
- Related control IDs
- Source command(s)
- Git commit SHA
- Verification status (`Verified`, `Partially Confirmed`, `Unknown`)

## Integrity and Immutability Rules
- Evidence must be content-addressed by SHA-256 hash.
- Hashes must be generated only from existing files.
- Superseded versions are retained (no destructive overwrite).
- Evidence validity statements must link to reproducible commands.

## Approval and Promotion
- Draft evidence: contributor-owned.
- Accepted evidence: reviewer-approved and linked to launch-gate criteria.
- Deprecated evidence: retained with deprecation reason and replacement pointer.

## Known Gaps (as of 2026-05-11)
- Cryptographic signing workflow is planned but not yet enforced in repository CI (**Partially Confirmed**).
