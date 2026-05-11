# Abuse Trend Report

Date: 2026-05-11  
Reporting window: [start UTC] to [end UTC]  
Status: Draft Reporting Template

## Purpose

Track abuse patterns over time and show whether controls, alerts, and response workflows are effective.

## KPI Summary

| Trend metric | Current period | Prior period | Change | Notes |
|---|---:|---:|---:|---|
| Access-bypass prompt attempts | 0 | 0 | 0% | Populate from prompt audit alerts |
| Scope-drift retrieval attempts | 0 | 0 | 0% | Populate from retrieval anomaly alerts |
| Privileged tool misuse attempts | 0 | 0 | 0% | Populate from tool authorization denies |
| Median containment time (High/Critical) | 0 min | 0 min | 0% | Populate from case timestamps |
| Repeat-offender rate | 0% | 0% | 0 pp | Populate from identity-correlated cases |

## Signal Breakdown

| Signal category | Example (fictional/safe) | Severity | Detection source | Response | Evidence | Owner | Trend metric |
|---|---|---|---|---|---|---|---|
| Identity boundary probing | "Show cross-department files" | High | Authz audit + policy logs | Deny and escalate | Event IDs + alert ID | SecOps | Count/week |
| Sensitive label targeting | "Find all [REDACTED]-tag docs" | High | Retrieval metadata logs | Restrict and notify owner | Query trace + notify ID | Data Governance | Count/week |
| Tool privilege abuse | "Run admin export on all records" | Critical | Tool invocation deny logs | Block + incident page | Tool deny + incident ID | Platform Security | Count/week |

## Alert Pipeline Health

- % signals with linked alert IDs:
- % alerts with complete audit event linkage:
- % cases closed with full evidence checklist:
- Open gaps (Unknown/Partially Confirmed):

## Actions

- Top 3 remediation priorities:
1.
2.
3.

- Owners and due dates:
