# Red-Team Metrics

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Red-Team Scenario Pass Rate | (Scenarios resisted successfully / Total executed scenarios) × 100 | Red-team execution logs in `security-readiness/07-testing-and-verification/` | >= 95% | 85% to < 95% | < 85% | `red_team.scenario_pass_rate_pct` | **Block launch** if Critical |
| Critical Finding Density | Critical findings / 100 executed scenarios | Red-team findings register | 0 | > 0 to 1 | > 1 | `red_team.critical_finding_density` | **Immediate launch block** when > 0 until remediated |
| Regressed Scenario Rate | (Previously passed scenarios now failing / Previously passed scenarios re-run) × 100 | Historical test baselines + current run | 0.0% | > 0.0% to 2.0% | > 2.0% | `red_team.regressed_scenario_rate_pct` | **Block launch** at any non-zero unresolved regression |
| Mean Time to Red-Team Remediation | Sum(time to remediate red-team findings) / Count(remediated findings) | Issue tracker + finding closure dates (dependency) | <= 14 days | > 14 to 30 days | > 30 days | `red_team.mttr_days` | **Escalate gate review** at Warning; **block** if Critical |
| Abuse-Case Coverage | (Abuse cases tested in cycle / Total prioritized abuse cases) × 100 | Abuse-case catalog + test run manifest | 100% | 90% to < 100% | < 90% | `red_team.abuse_case_coverage_pct` | **Block launch** if < 100% for P0/P1 abuse cases |

## Dependencies and Availability Notes

- Integration with issue tracker for MTTR is a **dependency** where manual capture is current state.
- Scenario history retention is a **dependency** for regression calculations.
- If abuse-case prioritization tiers are incomplete, coverage metric is **Partially Confirmed**.

## Measurement Notes

- Version-control each red-team scenario to preserve reproducibility.
- Run a fixed mandatory P0/P1 scenario set for every release candidate.
- Do not collapse “blocked by environment” into “pass.”
