# Launch Gate Drift Alerting

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Alert Definition
- **Signal**: post-approval control drift, readiness score regression, or newly failed critical controls.
- **Severity**: High (Critical if any previously passed critical control regresses).
- **Threshold**: Readiness score below approved minimum in two consecutive runs, or any critical control regression.
- **Owner**: Launch Governance Board Delegate.
- **Evidence Source**: Readiness scoring job output, control verification records, audit trail diffs.
- **Response Action**: Freeze release promotion, convene launch gate review, issue remediation deadlines.
- **Launch Gate Impact**: Enforced hold until drift is resolved and re-verified.

## Event Mapping Requirements
- Required event types: `readiness_evaluation_completed`, `control_regression_detected`, `launch_gate_status_changed`.
- Required fields: `readiness_score`, `critical_control_count_failed`, `baseline_version`, `current_version`.

## Evidence Notes
- No net-new operational integration performed in this step.
