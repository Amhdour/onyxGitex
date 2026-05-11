# AI System Decommissioning Plan (Priority 36 / Scope 295)

## Purpose
Define a controlled, auditable shutdown process for the internal AI system so decommissioning does not leave retrievable data, active connectors, tool privileges, model access, or evidence gaps.

## Decommissioning Trigger
- **Trigger type:** Planned retirement, risk-based emergency shutdown, or platform migration cutover.
- **Trigger decision owner:** AI Service Owner with Security Lead concurrence.
- **Required trigger artifact:** Signed change request / incident directive ID and effective date.

## Responsible Owners
- **Primary owner:** AI Service Owner.
- **Security owner:** Security Readiness Lead.
- **Data owner:** Data Governance / Privacy Owner.
- **Platform owner:** Onyx Platform Engineering.
- **Evidence owner:** GRC / Audit Readiness Owner.

## Scope of Decommissioning
1. Retrieval indexes and cached embeddings.
2. Connectors and ingestion schedules.
3. Tool identities, permissions, and runtime allowlists.
4. Model provider credentials and API keys.
5. Runtime logs, audit traces, and decision artifacts for archive.

## Execution Sequence (Fail-Closed)
1. Freeze new ingestion and disable autonomous tool execution.
2. Capture final evidence snapshot (config, access state, pending jobs).
3. Delete retrieval indexes and verify non-retrievability.
4. Disable connectors and scheduled sync jobs.
5. Remove tool access and revoke service principals.
6. Revoke model/API keys and confirm authentication failure.
7. Archive decommissioning evidence package.
8. Run post-decommission risk review and sign-off.

## Mandatory Control Requirements
- **Data deletion:** Verified deletion workflow for indexes, vector stores, and temporary caches.
- **Connector disablement:** Confirm connectors cannot pull new data after cutoff.
- **Key revocation:** Confirm revoked keys/tokens are rejected by providers.
- **Evidence archive:** Store immutable evidence with retention and access controls.
- **Residual risk:** Record remaining risk items and business owners.
- **Final sign-off:** Security, platform, and business owner approval required.

## Verification Status Model
- **Verified:** Supported by command output, logs, or configuration evidence.
- **Partially Confirmed:** Some evidence exists; coverage is incomplete.
- **Unknown:** No reliable evidence yet.

## Exit Criteria
Decommissioning is complete only when all related checklists are closed, residual risks are accepted or remediated, and final sign-off is recorded.
