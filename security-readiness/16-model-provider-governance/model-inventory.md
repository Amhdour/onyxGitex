# 95. Model Inventory

Date: 2026-05-11
Status: **Partially Confirmed**

## Scope
Inventory LLM and embedding model/provider governance-relevant paths in Onyx code/config without using live API keys.

## Observed provider/model inventory (code-path evidence)

| Provider | Model Type | Usage Purpose | Routing Assumption | Fallback Behavior | Confidence |
|---|---|---|---|---|---|
| OpenAI | Chat/completion models (`model_configurations`) | Default chat provider when `OPENAI_DEFAULT_API_KEY` is set during tenant provisioning | Chosen by default provider + model config; can be overridden by persona/override | If missing default config or access denied, runtime falls back to default LLM resolution path | Partially Confirmed |
| Anthropic | Chat/completion models | Alternate default provider when `ANTHROPIC_DEFAULT_API_KEY` is set | Same provider/model resolution and access control pipeline as above | Same default fallback semantics via `get_default_llm()` | Partially Confirmed |
| Vertex AI | Chat/completion models | Alternate default provider when `VERTEXAI_DEFAULT_CREDENTIALS` is set | Provisioned with credentials+location custom config | If default creds absent, provider provisioning skipped | Partially Confirmed |
| OpenRouter / dynamic providers | Dynamic model catalog | Optional provider via stored provider records and model configs | Provider-level custom config and display-name handling for dynamic model lists | Unknown at runtime without deployed tenant/provider records | Unknown |
| Cloud Embedding Provider (DB-backed) | Embedding model config | Embeddings for indexing/query paths via cloud embedding provider record | Single provider-type upserted in DB and later invoked by embedding pipelines | Unknown behavior if provider unavailable from this evidence set | Unknown |
| Local embedding path (`provider=None` metrics label) | Local embedding model path | Embedding operations tracked even when no cloud provider label is set | Metrics path supports explicit local/no-provider labeling | Not a model fallback control by itself; only observability evidence | Partially Confirmed |

## Data exposure and logging notes
- Provider API keys are configured via environment-backed config and DB provider records; inventory here does not use any live credentials.
- Embedding metrics include provider labels; this can reveal provider usage patterns even if payload content is not logged.

## Evidence required before launch gate
1. Exported tenant-level provider list and active model configs (admin API + DB read) with redaction.
2. Confirmed default and persona-specific model routing matrix for production personas.
3. Confirmed embedding provider configuration and failure-mode behavior under provider outage.
4. Audit evidence for model/provider change approvals.

## Launch gate effect
- If inventory remains incomplete, governance status for model boundary assurance is **No-Go** (insufficient evidence).
