# AI System Ownership Matrix

_Date: 2026-05-11_
_Status: Draft for Security Readiness (Build Priority 32)_

## Ownership Matrix

| Asset Name | Type | Primary Owner | Security Owner | Backup Owner Role | Dependency | Data Touched | Risk Level | Lifecycle Status | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|---|---|
| Onyx Backend Server | Core AI Service | Platform Engineering Manager | AppSec Lead | Senior Backend Engineer | LLM APIs, Vector Store, AuthN/Z | Prompts, retrieval context, auth context | High | Active | Backend service directories and deployment manifests | Bi-weekly |
| Onyx Web App | User Interaction Layer | Frontend Engineering Lead | Product Security Partner | Senior Frontend Engineer | Backend API, SSO | User inputs, session metadata | Medium | Active | Web source tree and API client integration | Monthly |
| Retrieval & Ranking Stack | AI Retrieval Subsystem | Search/AI Engineering Lead | AI Security Architect | Retrieval Engineer | Connector ingestion, embeddings, vector DB | Internal document chunks and metadata | High | Active | Retrieval/indexing modules and retrieval config | Bi-weekly |
| Connector Ingestion Stack | Data Ingestion Subsystem | Integrations Engineering Lead | Security Architect | Integration Engineer | Third-party SaaS APIs, worker orchestration | External enterprise docs, ACL metadata | High | Active | Connector/sync modules and scheduling workflows | Monthly |
| Identity & Access Controls | Security Control Plane | Security Engineering Manager | IAM Lead | Platform Engineer | IdP/SSO, role mapping, policy checks | Identity claims, group mappings, policy decisions | High | Active | Auth and authorization integration code | Monthly |
| Observability and Audit Events | Assurance Subsystem | SRE Manager | Security Operations Lead | Reliability Engineer | Logging backends, SIEM pipeline | Audit event logs, trace IDs, error context | Medium | Active | Logging hooks and observability configs | Monthly |

## RACI Guidance
- **Responsible**: Primary Owner executes updates/remediation.
- **Accountable**: Security Owner approves control posture.
- **Consulted**: Backup Owner Role and dependent subsystem owners.
- **Informed**: Governance and launch-gate stakeholders.
