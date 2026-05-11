# Retrieval Authorization Readiness Case Study

## Scenario
A fictional investment research firm, **Northbridge Analytics**, deploys an internal RAG assistant so equity analysts can query policy documents, deal memos, and team knowledge bases.

## Business Risk
If retrieval authorization fails, users may access documents outside their entitlement boundary (e.g., M&A draft materials or restricted compliance notes), creating confidentiality, regulatory, and reputational exposure.

## System Components Involved
- Identity provider (SSO + group claims)
- Onyx user/session layer
- Document ingestion and metadata tagging pipeline
- Vector index and retrieval service
- Authorization policy engine (document ACL + group mapping)
- Application audit log sink and dashboard

## Threat Model Summary
- **Primary asset:** restricted internal documents.
- **Adversary profile:** authenticated insider with valid account but insufficient clearance.
- **Trust boundary:** identity and group claims crossing into retrieval service.
- **Failure mode:** fail-open retrieval when ACL metadata is missing, stale, or bypassed.

## Abuse Case
A user in the "General Research" group asks a broad question crafted to retrieve results from a "Confidential Deals" collection and receives unauthorized snippets because ACL checks are skipped for one retrieval path.

## Control Design
- Enforce retrieval-time ACL checks on every candidate document before ranking output.
- Require deny-by-default behavior when ACL metadata is missing or unparsable.
- Bind query execution to immutable user identity and group claims captured at request start.
- Emit structured audit events for authorized and denied retrieval attempts.

## Test Design
- Positive test: authorized user retrieves only in-scope documents.
- Negative test: unauthorized user attempts same query and receives denial/no restricted content.
- Metadata integrity test: remove ACL field and verify fail-closed behavior.
- Regression test: multi-turn chat cannot inherit elevated context from prior authorized session.

## Evidence Required
**Planned Evidence**
- Retrieval authorization integration test commands and outputs.
- Sample redacted audit events proving deny decisions.
- Configuration references for ACL enforcement defaults.
- Trace IDs linking user request to retrieval decision logs.

## Expected Dashboard Signal
- Non-zero denied retrieval count for unauthorized test cases.
- Zero restricted document disclosures to out-of-scope users during test window.
- Alert when ACL metadata missing-rate exceeds threshold.

## Residual Risk
Group claim drift between IdP and retrieval policy cache may cause temporary over/under-enforcement if synchronization lags.

## Launch Gate Impact
No production launch approval for confidential datasets unless deny-path tests and audit evidence are collected and reviewed.

## Client-Facing Explanation
"We tested whether your assistant can prevent users from retrieving documents outside their role. The release should only proceed once denial behavior and audit traceability are verified with evidence."

## Portfolio Summary
This case study demonstrates readiness methodology for least-privilege retrieval in enterprise RAG systems, emphasizing fail-closed authorization and auditable policy decisions.
