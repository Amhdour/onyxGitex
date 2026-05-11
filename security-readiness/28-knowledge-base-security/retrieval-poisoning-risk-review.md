# Build Priority 20 - Retrieval Poisoning Risk Review

Date: 2026-05-11

## Scope
Assess risk that poisoned or adversarially crafted documents manipulate retrieval ranking and downstream answers.

## Risk scenarios
| Scenario | Abuse path | Control expectation | Status |
|---|---|---|---|
| Instruction injection in indexed docs | Malicious doc is highly ranked and overrides policy | Provenance controls + content risk checks + runtime guardrails | **Unknown** |
| Citation poisoning | Fake authority document outranks trusted sources | Source trust weighting + citation verification | **Unknown** |
| Keyword stuffing / embedding manipulation | Adversarial chunk dominates semantic search | Anomaly detection + ranking constraints | **Unknown** |

## Planned test
1. **Poisoned document retrieval test**
   - Setup: inject marked poisoned doc with high lexical/semantic overlap.
   - Check: retrieval stack flags/suppresses poisoned candidate or routes to safe handling.
   - Evidence: retrieval trace, ranking output, policy/audit events.

## Risk statement
- Poisoning remains high risk until prevention/detection controls are verified.
- If poisoning can alter responses across trust boundaries, severity is **Critical**.
