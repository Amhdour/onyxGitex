# Evidence Integrity Manifest

## Objective
Define manifest requirements and implementation notes for integrity tracking of evidence files.

Date: 2026-05-11
Status: Implemented baseline generator

## Required Manifest Fields
Each manifest entry includes:
- `file_path`
- `hash_sha256`
- `timestamp_utc`
- `git_commit`
- `command_used`
- `test_status`
- `evidence_type`

## Baseline Generator
Repository includes a generator script:

- `security-readiness/24-versioning-evidence-integrity/generate_evidence_manifest.py`

The script:
1. Validates each provided path exists and is a regular file.
2. Computes SHA-256 from real file bytes.
3. Captures current UTC timestamp.
4. Reads current repository Git commit SHA.
5. Writes JSON manifest entries with command/test/evidence metadata.

## Example Command
```bash
python3 security-readiness/24-versioning-evidence-integrity/generate_evidence_manifest.py \
  --output security-readiness/24-versioning-evidence-integrity/evidence-manifest.json \
  --command "python3 security-readiness/24-versioning-evidence-integrity/generate_evidence_manifest.py ..." \
  --test-status pass \
  --evidence-type documentation \
  security-readiness/24-versioning-evidence-integrity/*.md
```

## Safety Constraint
No manifest entry is created for missing paths. The generator exits non-zero if any input path is absent or non-file.
