# Evidence Export Script

Date: 2026-05-11  
Status: Verified (script implemented)

## Objective
Export selected normalized evidence records into a reviewable evidence pack.

## Behavior
- Preserves existing status values (`Verified`, `Missing`, `Incomplete`).
- Includes export metadata: export timestamp, git commit, command.
- Does not modify original artifact files.

## Example
```bash
python3 security-readiness/scripts/export-evidence-pack.py \
  --input security-readiness/evidence-artifacts/normalized-evidence.json \
  --output security-readiness/evidence-artifacts/evidence-pack.json
```
