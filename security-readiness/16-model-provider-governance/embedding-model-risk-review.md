# 97. Embedding Model Risk Review

Date: 2026-05-11
Status: **Partially Confirmed**

## Embedding governance observations

| Topic | Observation | Risk | Status |
|---|---|---|---|
| Embedding provider persistence | Cloud embedding provider is upserted by provider type in DB | Misconfiguration can silently replace prior provider config | Verified |
| Metrics observability | Embedding metrics tag provider label; `None` maps to local path | Provider usage metadata leakage (operational intelligence risk) | Verified |
| Query embedding cache | Cache behavior is environment-configurable | Stale embeddings or unintended data retention if TTL policy is weak | Partially Confirmed |
| Outage behavior | No complete end-to-end evidence collected here for embedding provider failure behavior | Unknown fail-open/fail-closed characteristics | Unknown |

## Data exposure risk
- Embedding calls can transmit document/query text to external providers when cloud embeddings are enabled.
- Local embedding path reduces third-party exposure but must still be evaluated for host-level data access controls.

## Logging risk
- Provider labels in metrics are useful for operations but can expose architecture details.
- Payload/body logging for embedding text is **Unknown** from this review and requires log-sink verification.

## Evidence required
1. Runtime trace showing embedding request path for each enabled provider.
2. Log-sink sampling proving text payload redaction/non-retention.
3. Failure test showing behavior when embedding provider is unreachable.
4. Mapping of embedding models to data classification tiers.

## Launch gate effect
- If payload logging controls are unverified or outage behavior is unknown, embedding governance remains **No-Go** for sensitive data classes.
