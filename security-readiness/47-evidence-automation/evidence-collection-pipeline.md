# Evidence Collection Pipeline

Date: 2026-05-11  
Status: Verified (baseline scripts)

## Objective
Define an auditable local pipeline for collecting and preparing evidence artifacts for readiness review.

## Pipeline Steps
1. **Collect**: `collect-evidence.sh` builds a raw manifest from explicit artifact paths.
2. **Normalize**: `normalize-evidence.py` transforms raw records into normalized schema records.
3. **Freshness Check**: `check-evidence-freshness.py` detects stale evidence older than policy threshold.
4. **Completeness Validation**: `validate-evidence-completeness.py` fails if required artifacts are missing/incomplete.
5. **Export**: `export-evidence-pack.py` packages normalized evidence for review.

## Execution Example
```bash
security-readiness/scripts/collect-evidence.sh \
  --output security-readiness/evidence-artifacts/raw-evidence.json \
  --command "manual collection" \
  security-readiness/47-evidence-automation/evidence-collection-pipeline.md

python3 security-readiness/scripts/normalize-evidence.py \
  --input security-readiness/evidence-artifacts/raw-evidence.json \
  --output security-readiness/evidence-artifacts/normalized-evidence.json
```

## Fail-Closed Behavior
The pipeline never converts missing data into pass states. Missing artifacts are marked `Missing` and remain visible to validators.
