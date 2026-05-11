# AI Component Dependency Map

_Date: 2026-05-11_
_Status: Draft for Security Readiness (Build Priority 32)_

## Dependency Mapping Table

| Asset Name | Type | Owner | Upstream Dependency | Downstream Dependency | Data Touched | Risk Level | Lifecycle Status | Evidence | Review Cadence |
|---|---|---|---|---|---|---|---|---|---|
| Connector Framework | Ingestion | Integrations Engineering | External SaaS/content APIs | Indexing pipeline | Raw docs, ACL metadata | High | Active | Connector module structure in backend | Monthly |
| Document Indexing Workers | Processing | Search/AI Engineering | Connector framework | Embedding generation | Parsed text chunks, metadata | High | Active | Worker/indexing implementation references | Bi-weekly |
| Embedding Generator | Model Integration | AI Platform Engineering | Indexing workers | Vector store writes | Text chunks, embedding vectors | High | Active | Embedding-related integration points | Bi-weekly |
| Vector Store | Data Store | Data Platform Team | Embedding generator | Retrieval engine | Vectors, metadata filters | High | Active | Vector access and retrieval integration code | Monthly |
| Retrieval Engine | AI Runtime Component | Search/AI Engineering | Vector store, auth filters | LLM prompt assembler | Retrieved chunks, access-scoped context | High | Active | Retrieval/ranking integration paths | Bi-weekly |
| LLM Prompt Assembly + Inference | AI Runtime Component | Platform Engineering | Retrieval engine, policy filters | Response service to UI | User prompt + selected context + model output | High | Active | LLM request/response orchestration code | Weekly |
| Web UI Chat Client | User Interface | Frontend Engineering | Response service API | End user | User prompts, response display metadata | Medium | Active | Web chat interface source code | Monthly |

## Dependency Notes
- Critical trust boundary: retrieval output to LLM context assembly.
- Critical enforcement point: authorization filtering before retrieval material is injected into prompts.
- Third-party dependencies should be reviewed through supply-chain risk workflow before readiness sign-off.
