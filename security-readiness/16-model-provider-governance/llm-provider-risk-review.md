# 96. LLM Provider Risk Review

Date: 2026-05-11
Status: **Partially Confirmed**

## Risk review matrix

| Provider Area | Data Exposure Risk | Logging Risk | Fallback / Routing Risk | Evidence Status |
|---|---|---|---|---|
| Default provider provisioning (OpenAI/Anthropic/Vertex) | High: prompts/context may leave trust boundary | Medium: provider choice may appear in logs/metrics; payload logging needs separate confirmation | Medium: missing env values skip provisioning, may change effective default provider availability | **Verified** for provisioning conditions; **Unknown** for payload logging behavior |
| Persona and group access gating | Medium: misconfigured provider visibility can expose stronger/external models | Low-Medium: access denials logged with identifiers | Medium: denied provider access falls back to default model, which may still be external | **Verified** for access-check + fallback behavior |
| Build-mode provider selection (`build-mode-{type}`) | Medium: can route build sessions to unintended provider if naming conventions drift | Low: selection logic observable in code, runtime logging depth unknown | Medium: second-stage fallback to any provider type can reduce deterministic routing | **Partially Confirmed** |
| Dynamic/custom providers | High: unknown vendor chain and handling practices | Medium-High: unclear default logging and retention terms per vendor | High: model list and behavior may shift externally without pinned policy | **Unknown** |

## Key findings
1. Provider provisioning is conditional on env keys/credentials and skips silently (logged) if defaults are absent.
2. User access to a provider is constrained by persona/group/public settings, but runtime can still fall back to system default provider when access fails.
3. Build-mode routing prefers a specially named provider but will fall back to any matching provider type.
4. Dynamic provider behavior is not fully confirmable from current static evidence.

## Required compensating controls
- Enforce explicit allowlist of production-approved provider types.
- Require provider data-processing agreements and retention policy attestation per vendor.
- Add policy-decision logs that capture provider routing decision inputs/outputs (without sensitive prompt bodies).
- Fail-closed rule for unauthorized provider: block response generation for protected personas instead of broad fallback (unless explicitly approved).

## Launch gate effect
- **Conditional No-Go** until dynamic/custom provider controls and logging-retention attestations are verified.
