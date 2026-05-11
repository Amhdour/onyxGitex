# Retrieval Denial Alerting

Date: 2026-05-11  
Status: Draft (Documentation-Only)

## Alert Definition
- **Signal**: abnormal growth in authorization-based retrieval denials.
- **Severity**: Medium by default; High if correlated with identity/ACL drift.
- **Threshold**: Denial ratio >15% and >2x rolling baseline for 30 minutes.
- **Owner**: Retrieval Security Owner.
- **Evidence Source**: Retrieval authorization audit logs, identity mapping change logs, request trace IDs.
- **Response Action**: Investigate role-mapping changes, validate index-level ACLs, and apply scoped rollback if drift confirmed.
- **Launch Gate Impact**: Conditional launch hold when denial anomaly is unexplained or coupled with access-control changes.

## Event Mapping Requirements
- Required event types: `retrieval_request`, `retrieval_authz_decision`, `retrieval_authz_denied`.
- Correlation key: `request_id` + `principal_id` + `index_id`.

## Evidence Notes
- Documentation-only baseline; no live integrations introduced.
