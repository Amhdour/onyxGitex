# Governance Maturity Metrics

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Policy Coverage Ratio | (Required AI governance policies published and approved / Total required policies) × 100 | Governance policy register in `security-readiness/09-governance-and-continuous-review/` | 100% | 90% to < 100% | < 90% | `governance.policy_coverage_ratio_pct` | **Block launch** if Critical |
| Exception Aging Risk | (Open policy/security exceptions older than SLA / Total open exceptions) × 100 | Exception register + aging report | <= 5% | > 5% to 15% | > 15% | `governance.exception_aging_risk_pct` | **Escalate governance board** at Warning; **block** if Critical |
| Control Review Cadence Compliance | (Controls reviewed on schedule / Controls due for review) × 100 | Control review calendar + logs | >= 95% | 85% to < 95% | < 85% | `governance.review_cadence_compliance_pct` | **Conditional launch** at Warning; **block** if Critical |
| Training Completion for Key Roles | (Assigned personnel completing required training / Assigned personnel) × 100 | LMS/export report (dependency) | 100% | 90% to < 100% | < 90% | `governance.training_completion_pct` | **Block launch** if Critical |
| Risk Acceptance Documentation Completeness | (Accepted risks with rationale, approver, expiry / Total accepted risks) × 100 | Risk register and acceptance forms | 100% | 95% to < 100% | < 95% | `governance.risk_acceptance_doc_completeness_pct` | **Block launch** if Critical |

## Dependencies and Availability Notes

- LMS export availability is a **dependency** for training completion metric.
- Exception register normalization may be a **dependency** if multiple trackers are used.
- If approver/expiry fields are missing in legacy risk records, status is **Partially Confirmed**.

## Measurement Notes

- Governance metrics should be reviewed monthly and before each launch gate.
- Treat missing approval metadata as non-compliant, not null-safe pass.
- Align policy inventory with framework control mapping to avoid duplicate counts.
