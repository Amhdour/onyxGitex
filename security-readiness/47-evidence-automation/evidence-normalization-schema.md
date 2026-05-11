# Evidence Normalization Schema

Date: 2026-05-11  
Status: Verified (design + local implementation)

## Objective
Define a normalized schema for evidence records consumed by the readiness workflow.

## Required Fields
Each normalized record MUST include:

- `artifact_path`: Relative path to evidence artifact.
- `artifact_hash_sha256`: SHA-256 hash computed from artifact bytes.
- `timestamp_utc`: Collection timestamp in UTC ISO-8601 format.
- `git_commit`: Git commit SHA captured at collection time.
- `command`: Command used to produce or collect the artifact.
- `status`: `Verified`, `Missing`, or `Incomplete`.

## Optional Fields
- `evidence_type`: Category such as `test-output`, `configuration`, or `documentation`.
- `owner`: Evidence owner.
- `notes`: Free-form context.

## Status Semantics
- `Verified`: Artifact exists and mandatory metadata is present.
- `Missing`: Artifact path not found.
- `Incomplete`: Artifact exists but required metadata is missing.

## Safety Constraints
- Schema is metadata-only and does not assert readiness by itself.
- Missing or incomplete evidence is preserved as explicit status values.
