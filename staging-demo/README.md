# Version 3 — Staging Demo

Current status:
NOT_STARTED

Purpose:
Prove runtime behavior in a staged environment.

Minimum staging stack:
- Keycloak or mock OIDC
- OPA policy checks
- Vault/OpenBao or substitute
- Onyx RAG test environment
- LangGraph agent test environment
- Qdrant or pgvector retrieval
- Langfuse/Phoenix/OpenTelemetry traces
- GitHub Actions artifacts
- Grafana/Superset dashboard if practical

Entry condition:
Do not start serious staging work until Version 2A RAG Runtime Evidence and Version 2B CI Artifact Proof are complete.
