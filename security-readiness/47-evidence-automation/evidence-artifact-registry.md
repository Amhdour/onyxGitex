# Evidence Artifact Registry

Date: 2026-05-11  
Status: Partially Confirmed

## Objective
Track required readiness artifacts and their verification expectations.

## Baseline Registry Fields
- `artifact_id`
- `artifact_path`
- `required` (`true`/`false`)
- `owner`
- `expected_status` (`Verified`)

## Registry Storage
Recommended file: `security-readiness/evidence-artifacts/required-artifacts.json`.

## Sample Entry
```json
{
  "artifact_id": "evidence_pipeline_doc",
  "artifact_path": "security-readiness/47-evidence-automation/evidence-collection-pipeline.md",
  "required": true,
  "owner": "AI Trust & Security",
  "expected_status": "Verified"
}
```

## Gap
Registry governance workflow (approvals/SLAs) is not yet automated (**Unknown**).
