# Evidence Freshness Checker

Date: 2026-05-11  
Status: Verified (script implemented)

## Objective
Detect stale evidence artifacts based on timestamp age.

## Inputs
- Normalized evidence JSON.
- Maximum age threshold (days).

## Output Behavior
- Emits per-record freshness status.
- Returns non-zero when stale evidence exists.
- Marks entries as `Missing` unchanged when artifacts are absent.

## Example
```bash
python3 security-readiness/scripts/check-evidence-freshness.py \
  --input security-readiness/evidence-artifacts/normalized-evidence.json \
  --max-age-days 30
```
