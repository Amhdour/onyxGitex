# Retrieval Risk Metrics

Date: 2026-05-11  
Status: Draft for Build Priority 26  
Classification: Internal

## Metric Catalog

| Metric Name | Calculation | Data Source | Target Threshold | Warning Threshold | Critical Threshold | Dashboard Field | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| Unauthorized Retrieval Attempt Rate | (Denied retrieval attempts due to authz / Total retrieval attempts) × 100 | Retrieval gateway logs + authz decisions | <= 1.0% (stable baseline) | > 1.0% to 3.0% | > 3.0% | `retrieval.unauthorized_attempt_rate_pct` | **Investigate** at Warning; **block launch** if Critical trend persists |
| Retrieval Policy Bypass Incidents | Count of confirmed bypass incidents per reporting window | Incident records + red-team findings | 0 | 1 | >= 2 | `retrieval.policy_bypass_incidents` | **Immediate launch block** at >= 1 unless disproven false positive |
| Sensitive Document Exposure Rate | (Responses containing unauthorized sensitive content / Total sampled responses) × 100 | DLP/classification scan of response samples | 0.00% | > 0.00% to 0.10% | > 0.10% | `retrieval.sensitive_exposure_rate_pct` | **Immediate launch block** at Warning or Critical |
| Retrieval Citation Match Rate | (Response claims with valid source grounding / Total sampled claims) × 100 | Citation validation pipeline (dependency) | >= 98% | 90% to < 98% | < 90% | `retrieval.citation_match_rate_pct` | **Block launch** if Critical |
| Stale Index Risk Rate | (Queries served with stale/out-of-SLA index / Total queries) × 100 | Index freshness telemetry | <= 1.0% | > 1.0% to 5.0% | > 5.0% | `retrieval.stale_index_risk_rate_pct` | **Require risk acceptance** at Warning; **block** if Critical |

## Dependencies and Availability Notes

- Citation validation pipeline is a **dependency** where automation does not yet exist.
- DLP scanning of model outputs may require additional integration (**dependency**).
- Index freshness telemetry must expose per-query index timestamp to support measurement.

## Measurement Notes

- Separate malicious probing from legitimate denied attempts to avoid false interpretation.
- Track both absolute counts and percentages for low-volume windows.
- Enforce consistent sensitive-data taxonomy across classifier and policy layers.
