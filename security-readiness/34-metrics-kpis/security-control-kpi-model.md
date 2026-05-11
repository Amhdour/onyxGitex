# Security Control KPI Model

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Control Implementation Coverage | (Implemented required controls / Total required controls) × 100 | Control inventory and implementation map in `security-readiness/05-controls-and-retrofit/` | 100% | 95% to < 100% | < 95% | `security_controls.implementation_coverage_pct` | **Block launch** unless 100% or formally accepted exception |
| Control Test Pass Rate | (Controls passing verification tests / Controls tested) × 100 | Test logs in `security-readiness/07-testing-and-verification/` | >= 95% | 85% to < 95% | < 85% | `security_controls.test_pass_rate_pct` | **Block launch** if Critical |
| Fail-Closed Enforcement Rate | (Controls proven fail-closed / Controls requiring fail-closed behavior) × 100 | Design review + negative test cases | 100% | 95% to < 100% | < 95% | `security_controls.fail_closed_enforcement_pct` | **Immediate launch block** if < 100% without approved exception |
| Policy Decision Logging Completeness | (Authorization decisions logged with required fields / Total authorization decisions) × 100 | Policy engine logs and audit schema validation | >= 99% | 95% to < 99% | < 95% | `security_controls.policy_logging_completeness_pct` | **Block launch** if Critical |
| Control Ownership Assignment Rate | (Controls with named owner / Total controls) × 100 | Control ownership matrix | 100% | 95% to < 100% | < 95% | `security_controls.ownership_assignment_pct` | **Escalate governance review** if Warning; **block** if Critical |

## Dependencies and Availability Notes

- Policy log schema validator may be a **dependency** if not yet automated.
- Ownership matrix centralization (e.g., GRC system sync) may be a **dependency**.
- If required-field logging cannot be measured reliably, mark metric status **Partially Confirmed**.

## Measurement Notes

- Treat control exceptions as separate denominator line items with explicit approval IDs.
- Do not count untested controls as passed.
- Recalculate after every control-change release, minimum weekly cadence.
