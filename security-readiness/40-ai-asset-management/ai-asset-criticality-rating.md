# AI Asset Criticality Rating

_Date: 2026-05-11_
_Status: Draft for Security Readiness (Build Priority 32)_

## Rating Scale
- **Critical**: Failure can cause sensitive data exposure, broad authorization bypass, or unbounded unsafe responses.
- **High**: Failure materially impacts confidentiality/integrity/availability of AI service outcomes.
- **Medium**: Failure has bounded blast radius with compensating controls.
- **Low**: Failure has minimal security and business impact.

## Criticality Matrix

| Asset Name | Type | Owner | Dependency | Data Touched | Risk Level | Criticality Rating | Lifecycle Status | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|---|
| Authorization Filter Path | Security Enforcement Component | Security Engineering | IdP claims, retrieval engine | Access control context, document ACL metadata | High | Critical | Active | Authorization integration and policy checks in backend | Bi-weekly |
| Retrieval Engine | AI Retrieval | Search/AI Engineering | Vector store, auth filters | Internal document snippets | High | Critical | Active | Retrieval code paths and config | Bi-weekly |
| LLM Inference Integration | External AI Integration | AI Platform Engineering | Model provider APIs | Prompts, context, generated outputs | High | Critical | Active | Model integration code and runtime configuration | Weekly |
| Connector Framework | Data Ingestion | Integrations Engineering | SaaS APIs, schedulers | Enterprise source documents | High | High | Active | Connector modules and synchronization configs | Monthly |
| Web Chat Interface | User Interface | Frontend Engineering | Backend response APIs | User input, rendered responses | Medium | Medium | Active | Web application source | Monthly |
| Observability/Audit Pipeline | Detection & Assurance | SRE / SecOps | Log pipeline and SIEM | Audit events, request traces | Medium | High | Active | Logging and audit hooks in repository | Monthly |

## Criticality Notes
- **Unknown**: Final criticality validation pending abuse-case testing and control verification outputs.
- Ratings should be re-baselined if architecture or model providers change.
