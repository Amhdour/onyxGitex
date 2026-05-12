# Tier 4 Artifact Writer Plan

## Objective
Define standardized artifact outputs for executable Tier 4 runtime tests so validator inputs are machine-readable and auditable.

## Artifact targets
Per test run, produce:
- `retrieval_authorization.runtime.json`
- `citation_leakage.runtime.json`
- `prompt_injection_boundary.runtime.json`
- `tier4-summary.json`

## Output envelope
Each artifact should include:
- `schema_version`
- `test_id`
- `run_id`
- `timestamp`
- `environment` (runtime profile, model profile, tenant/test namespace)
- `fixture_refs`
- `assertions`
- `results`
- `audit_event_refs`
- `runtime_trace_refs`
- `status` (`PASS|FAIL|ERROR`)
- `notes` (unknowns / partial confirmation)

## Assertion encoding pattern
Each assertion entry:
- `assertion_id`
- `description`
- `expected`
- `observed`
- `outcome` (`PASS|FAIL|ERROR`)
- `evidence_refs` (event IDs, trace IDs, response offsets)

## Schema governance
- Version schemas with semantic versioning.
- Reject write on schema mismatch unless explicit migration flag is enabled.
- Include validation result block:
  - `schema_valid`
  - `missing_fields`
  - `normalization_warnings`

## Integrity requirements
- Include deterministic hash of raw response + citation payload for replay confidence.
- Include capture completeness booleans:
  - `audit_capture_complete`
  - `trace_capture_complete`
  - `citation_capture_complete`
- Any `false` completeness flag forces non-PASS outcome.

## Tier4 summary behavior
`tier4-summary.json` aggregates:
- per-test status
- blocker mapping
- unknown/partial counts
- explicit launch posture field

Required summary posture rule:
- `launch_posture` remains `NOT_ENOUGH_EVIDENCE` until all blocker criteria are met by executed evidence.
- This plan does not authorize changing posture.
