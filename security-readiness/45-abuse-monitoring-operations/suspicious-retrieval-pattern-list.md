# Suspicious Retrieval Pattern List

Date: 2026-05-11  
Status: Draft (Detection Content)

All examples are fictional and safe.

| Signal category | Example | Severity | Detection source | Response | Evidence | Owner | Trend metric |
|---|---|---|---|---|---|---|---|
| Scope-drift retrieval | Sequence pivots from "team handbook" to "all finance legal docs" | High | Retrieval query-chain analytics | Block out-of-scope hops, require re-authorization | Query trace IDs, deny decision ID | RAG Platform + IAM | Scope-drift events/user/week |
| Connector hopping anomaly | Multiple unrelated connectors queried in rapid succession | Medium | Connector access logs + anomaly model | Step-up auth; temporary retrieval throttle | Connector audit events, anomaly score | Search Infrastructure Owner | Cross-connector hop frequency |
| Sensitive label targeting | Repeated queries for "confidential", "M&A", "payroll" tags | High | Metadata filter logs + label abuse detector | Restrict sensitive-label retrieval, notify data owner | Retrieval filter decisions, owner notification ID | Data Governance Owner | Sensitive-tag targeting trend |
| Repeated denied retrieval | Same denied query retried with minor wording changes | Medium | Deny-retry correlation rule | Escalate severity tier; user risk score increase | Deny chain IDs, risk score change event | Security Operations | Deny-retry loop count |
| Injection-bearing source chunks | Retrieved chunk includes instruction override text | High | Retrieval content scanner | Quarantine source chunk, exclude from context, alert detection engineer | Chunk fingerprint, quarantine event ID | Detection Engineering | Injection chunk prevalence by source |
