# Deprecated AI Asset Review

_Date: 2026-05-11_
_Status: Initial Review Template for Security Readiness (Build Priority 32)_

## Purpose
Track AI assets that should be deprecated to reduce attack surface, stale integrations, and unmanaged model risk.

## Deprecation Review Table

| Asset Name | Type | Owner | Dependency | Data Touched | Risk Level | Current Lifecycle Status | Deprecation Trigger | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|---|
| Unused Connector Integrations | Data Ingestion | Integrations Engineering | Third-party SaaS APIs | Enterprise docs, metadata | Medium | Maintenance | No business owner or no successful sync over defined period | Connector telemetry and ownership verification records | Quarterly |
| Legacy Model Provider Integration | External AI Integration | AI Platform Engineering | Model API + credentials | Prompts, context, generated output | High | Maintenance | Provider no longer approved or fails control requirements | Provider assessment and policy approvals | Monthly |
| Superseded Retrieval Strategy | Retrieval Component | Search/AI Engineering | Vector store, ranking logic | Retrieved document chunks | High | Maintenance | New retrieval controls outperform and old path increases risk | A/B test results and control test outcomes | Quarterly |

## Required Review Questions
1. Is there a named owner accountable for shutdown?
2. Is there evidence that dependencies and credentials can be removed safely?
3. Are audit and evidence retention requirements documented before retirement?
4. Is there a rollback/contingency plan if deprecation causes service regression?
5. Has security sign-off been recorded?

## Status Labels
- **Verified**: Retirement prerequisites and evidence confirmed.
- **Partially Confirmed**: Some prerequisites confirmed; blockers remain.
- **Unknown**: Insufficient evidence to approve deprecation.
