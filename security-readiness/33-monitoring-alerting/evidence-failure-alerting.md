# Evidence Failure Alerting

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Alert Definition
- **Signal**: missing/invalid control evidence, failed manifest generation, stale verification artifacts.
- **Severity**: High.
- **Threshold**: Any mandatory evidence artifact missing at checkpoint, or manifest validation failure.
- **Owner**: GRC Program Owner + Security PMO.
- **Evidence Source**: Evidence pipeline logs, manifest validators, signed artifact inventory.
- **Response Action**: Mark control status as **Unknown** or **Partially Confirmed**, block sign-off packet publication, assign remediation owner.
- **Launch Gate Impact**: No readiness declaration permitted for controls without valid evidence.

## Event Mapping Requirements
- Required event types: `evidence_job_started`, `evidence_job_failed`, `manifest_validation_failed`, `evidence_staleness_detected`.
- Required fields: `control_id`, `artifact_id`, `validation_error`, `run_id`, `owner`.

## Evidence Notes
- This artifact does not introduce live notifications; it defines policy for alert conditions and outcomes.
