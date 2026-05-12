# Recommended Next Runtime Tests

Date (UTC): 2026-05-12

This sequence is ordered to close launch-gate-critical runtime gaps first.

1. **Retrieval Authorization Full Runtime Test (highest priority)**
   - Goal: prove fail-closed retrieval authorization in full backend runtime.
   - Evidence target: PASS artifact consumable by validator and launch-gate scripts.

2. **Citation Leakage Full Runtime Test**
   - Goal: validate citation/source leakage protections in live retrieval + citation pipeline.
   - Evidence target: runtime PASS output + updated evidence artifact.

3. **Prompt Injection Full Runtime + Red Team Test**
   - Goal: validate prompt-injection boundary in runtime with adversarial prompts.
   - Evidence target: runtime PASS output + red-team evidence entry.

4. **Tool Authorization Runtime Wiring and Enforcement Test**
   - Goal: verify tool authorization context is wired in main runtime path and enforced fail-closed.
   - Evidence target: runtime PASS output proving denied/allowed behavior by policy.

5. **Launch-Gate Revalidation Run**
   - Goal: re-run evidence completeness validator and launch gate after the above artifacts are present.
   - Evidence target: updated `launch-gate-summary.md` and dashboard export still reflecting strict fail-closed logic.

## Guardrails

- Do not set launch decision to GO without Tier 4 evidence for blocked critical controls.
- Keep unknowns and partial confirmations explicit in all updated artifacts.
