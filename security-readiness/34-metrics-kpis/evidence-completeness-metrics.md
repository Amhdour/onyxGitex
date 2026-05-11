# Evidence Completeness Metrics

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Requirement-to-Evidence Traceability | (Requirements with linked evidence / Total in-scope requirements) × 100 | Evidence map in `security-readiness/08-evidence-pack-and-readiness-decision/` | 100% | 95% to < 100% | < 95% | `evidence.traceability_pct` | **Block launch** if below 100% without approved exception |
| Evidence Freshness Compliance | (Evidence artifacts updated within SLA / Total required artifacts) × 100 | Artifact metadata timestamps | >= 98% | 90% to < 98% | < 90% | `evidence.freshness_compliance_pct` | **Gate review required** at Warning; **block** if Critical |
| Reproducible Test Evidence Rate | (Tests with command + output + environment metadata / Total required tests) × 100 | Test evidence logs in `security-readiness/07-testing-and-verification/` | 100% | 95% to < 100% | < 95% | `evidence.reproducible_test_evidence_pct` | **Block launch** if Critical |
| Unknown Control Status Rate | (Controls marked Unknown / Total controls) × 100 | Control status register | <= 2.0% | > 2.0% to 5.0% | > 5.0% | `evidence.unknown_control_status_rate_pct` | **Block launch** if Critical; formal risk acceptance if Warning |
| Evidence Review Completion Rate | (Required evidence reviews completed / Total required evidence reviews) × 100 | Review sign-off tracker (dependency) | 100% | 90% to < 100% | < 90% | `evidence.review_completion_pct` | **Block launch** if Critical |

## Dependencies and Availability Notes

- Review workflow tracker integration is a **dependency** if approvals are currently email-based.
- Artifact metadata collection may require repository automation (**dependency**).
- If environment metadata for historical tests is missing, mark reproducibility as **Partially Confirmed**.

## Measurement Notes

- SLA for freshness should be explicitly set per artifact type (e.g., 30 days for control tests).
- Unknowns must remain visible; do not auto-reclassify without new evidence.
- Audit trail should preserve reviewer identity and decision date.
