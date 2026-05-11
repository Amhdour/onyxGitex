# Evidence Completeness Validator

Date: 2026-05-11  
Status: Verified (script implemented)

## Objective
Fail validation when required evidence is missing or incomplete.

## Rule
For each required artifact in registry:
- Pass only if a normalized record exists with `status=Verified`.
- Fail if missing record, `Missing`, or `Incomplete`.

## Output
- Machine-readable JSON summary.
- Human-readable missing/incomplete list.
- Exit code `1` on incomplete evidence.
