# Test Result Versioning Model

## Objective
Make security test outcomes reproducible, diffable, and tied to specific code and evidence states.

Date: 2026-05-11
Status: Draft for review

## Test Result Identifier
`TEST-<suite>-<case>-<YYYYMMDD>-<run-seq>`

Example: `TEST-authz-negative-cross-tenant-20260511-01`

## Version Trigger
A new test-result version is required when any of the following changes:
- Source code commit
- Test command/options
- Environment profile
- Input dataset/fixtures
- Expected assertion criteria

## Required Metadata
- Test result ID/version
- UTC execution timestamp
- Executor identity (user or CI actor)
- Git commit SHA
- Full command used
- Exit code
- Pass/fail/skip status
- Artifact hash(es) for captured output files
- Related control and evidence IDs

## Retention Rules
- Raw outputs and normalized summaries are both retained.
- Failed/negative tests are preserved (no selective deletion).
- Re-runs do not overwrite prior versions.

## Confidence Labels
- **Verified**: command and output captured; hashes present.
- **Partially Confirmed**: partial output or missing artifact hashes.
- **Unknown**: no reliable test record.
