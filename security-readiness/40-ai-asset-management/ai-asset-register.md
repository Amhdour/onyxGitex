# AI Asset Register

_Date: 2026-05-11_
_Status: Draft for Security Readiness (Build Priority 32)_

## Purpose
Canonical register of Onyx AI system assets for trust, security, ownership, and review tracking.

## AI Asset Register

| Asset Name | Type | Owner | Dependency | Data Touched | Risk Level | Lifecycle Status | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|
| Onyx Web App (`web/`) | Application UI | Application Engineering | Backend API, Auth provider, Search APIs | User queries, chat history metadata, session identifiers | Medium | Active | Repository structure and source tree (`web/`) | Monthly |
| Onyx Backend Server (`backend/onyx/server/`) | Core AI Orchestration Service | Platform Engineering | LLM provider APIs, vector DB, relational DB, connectors | Prompts, retrieval context, document snippets, auth context | High | Active | Repository structure and source tree (`backend/onyx/server/`) | Bi-weekly |
| Retrieval Pipeline | AI Processing Component | Search/AI Engineering | Document indexing workers, embeddings provider, vector store | Internal documents, extracted chunks, embedding vectors | High | Active | Backend retrieval/indexing code paths and runtime config | Bi-weekly |
| Connector Framework | Ingestion Component | Integrations Engineering | SaaS APIs, enterprise content stores, scheduler/worker stack | Source documents, ACL metadata, sync logs | High | Active | Connector modules and sync configurations in backend | Monthly |
| LLM Inference Integration | External AI Dependency Integration | AI Platform Engineering | Model provider endpoints, API credentials, network egress controls | User prompts, retrieved context, model responses | High | Active | LLM integration code and environment-dependent configuration | Weekly |
| Vector Store | Data Platform Component | Data Platform Team | Embedding generator, retrieval service | Embeddings, document chunk references, metadata filters | High | Active | Vector retrieval/index configuration references | Monthly |
| Authentication & Authorization Integration | Identity/Security Component | Security Engineering | SSO/IdP, role/group mapping, policy middleware | User identity claims, authorization context | High | Active | Auth middleware and access control integration in backend | Monthly |
| Observability & Audit Logging | Monitoring Component | SRE / Security Operations | Logging pipeline, metrics backend, alerting stack | Audit events, operational metadata, trace identifiers | Medium | Active | Logging and observability configuration/code references | Monthly |

## Notes
- Risk levels are readiness placeholders and require validation during formal threat modeling and control verification.
- Unknowns must remain marked until explicit test evidence is recorded.
