# Retrieval Source Change Approval Workflow

## Scope
Controls for adding/removing/modifying connectors, corpora, sync scopes, or indexing rules.

## Workflow
1. Submit `AI Change Request` with **Change Type = Retrieval Source**.
2. Perform risk assessment on data classification, tenancy boundaries, ACL inheritance, and connector trust.
3. Execute required tests:
   - authorization boundary tests,
   - document visibility tests by role,
   - ingestion and indexing integrity checks,
   - connector failure and quarantine behavior checks.
4. Update evidence with source inventory changes, test results, and access-control verification.
5. Secure approvals (data owner + security + service owner).
6. Roll out with staged sync and rollback path.
7. Validate launch gate impact, especially on confidentiality controls.

## Required Control Fields
- **Change Type:** Retrieval Source
- **Risk Assessment:** Mandatory
- **Required Tests:** Mandatory
- **Evidence Update:** Mandatory
- **Approval Owner:** Data Governance Owner
- **Rollback:** Required (disable connector/revert index scope)
- **Launch Gate Impact:** Required

## Minimum Approval Criteria
- Access controls confirmed as **Verified** for sampled roles.
- High-classification data handling explicitly approved.
- Quarantine/disable procedure validated.
