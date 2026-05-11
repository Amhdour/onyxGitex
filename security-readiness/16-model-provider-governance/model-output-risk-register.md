# 99. Model Output Risk Register

Date: 2026-05-11
Status: **Initial Register**

| Risk ID | Output Risk | Trigger | Impact | Current Control Evidence | Residual Status | Evidence Required | Launch Gate Effect |
|---|---|---|---|---|---|---|---|
| MOR-01 | Hallucinated policy/compliance statements | Weak retrieval grounding or unsupported completion | Incorrect business/legal guidance | General RAG controls exist elsewhere; provider-specific output guard evidence not in scope here | Partially Confirmed | Prompt+response red-team set with pass/fail criteria | Block regulated-domain launch if unresolved |
| MOR-02 | Sensitive data leakage in responses | Prompt injection / retrieval overexposure / weak auth boundaries | Confidentiality breach | Provider access gating exists; no complete output DLP evidence in this phase | Unknown | Output DLP tests + canary secret tests | No-Go for confidential data tiers |
| MOR-03 | Unsafe tool/action suggestion | Model suggests harmful or unauthorized actions | Operational/security misuse | Tool authorization controls reviewed in other phases; model-specific suppression unknown | Partially Confirmed | Abuse-case tests for prohibited actions | Conditional Go only with tested guardrails |
| MOR-04 | Provider-specific behavior drift | Upstream model updates alter behavior silently | Regressed safety/quality controls | Recommendations/model metadata exists; change governance not yet proven | Unknown | Scheduled regression harness and change checkpoint evidence | No-Go without drift detection |
| MOR-05 | Fallback output quality/safety regression | Automatic fallback to default model on denial/error | Lower-quality or less safe output | Fallback path confirmed in code; risk acceptance not documented | Partially Confirmed | Fallback equivalence/safety test results | No-Go for protected personas |

## Notes
- Unknown items are intentionally preserved as **Unknown** pending direct test or log evidence.
- This register should be linked to abuse-case testing in Phase 07 artifacts before final readiness scoring.
