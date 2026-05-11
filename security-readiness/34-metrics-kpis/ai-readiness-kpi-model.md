# AI Readiness KPI Model

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Readiness Control Pass Rate | (Verified controls passed in current cycle / Total in-scope controls) × 100 | Control verification logs in `security-readiness/07-testing-and-verification/` and test reports | >= 95% | 85% to < 95% | < 85% | `ai_readiness.control_pass_rate_pct` | **Block launch** if Critical; require remediation plan if Warning |
| Evidence Coverage Rate | (Controls with linked evidence artifacts / Total in-scope controls) × 100 | Evidence index and references in `security-readiness/08-evidence-pack-and-readiness-decision/` | >= 98% | 90% to < 98% | < 90% | `ai_readiness.evidence_coverage_pct` | **Block launch** if Critical |
| Unsupported Answer Rate | (Unsupported responses detected / Total sampled responses) × 100 | Eval/red-team sample output logs; citation validation scripts | <= 2.0% | > 2.0% to 5.0% | > 5.0% | `ai_readiness.unsupported_answer_rate_pct` | **Block launch** if Critical; conditional launch review if Warning |
| Identity Boundary Violation Rate | (Cross-boundary access violations / Total authorization checks) × 100 | Authz audit logs and policy decision logs | 0.00% | > 0.00% to 0.10% | > 0.10% | `ai_readiness.identity_boundary_violation_rate_pct` | **Immediate launch block** at Warning or Critical |
| Mean Time to Security Finding Closure (MTTR-Sec) | Sum(time-to-close for security findings) / Count(closed findings) | Ticketing system + risk register (dependency) | <= 14 days | > 14 to 30 days | > 30 days | `ai_readiness.mttr_security_days` | **Escalate launch review** if Warning; **block** if Critical |

## Dependencies and Availability Notes

- Ticketing-system export for MTTR-Sec is a **dependency** if not yet integrated into readiness dashboards.
- Citation validation automation is a **dependency** if currently done manually.
- Any metric that cannot be computed from available logs must be marked **Unknown** in the reporting cycle rather than estimated.

## Measurement Notes

- Compute all rates for a fixed reporting window (recommended: trailing 30 days).
- Freeze numerator/denominator definitions per release candidate to avoid metric drift.
- Use fail-closed handling for missing denominator data: emit `Unknown`, not `0`.
