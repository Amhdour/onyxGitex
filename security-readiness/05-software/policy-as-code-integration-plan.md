# Policy-as-Code Integration Plan

Date: 2026-05-12
Status: Draft for software retrofit phase

## Objective
Introduce retrieval and tool authorization policy decisions as explicit policy-as-code controls without weakening existing Onyx controls.

## Current baseline
- YAML policy definitions with JSON Schema validation.
- Local Python evaluator with fail-closed default deny behavior.
- Unit tests for retrieval/tool allow/deny edge cases.

## Integration sequence
1. **Read-only shadow mode**
   - Invoke evaluator at retrieval/tool decision points.
   - Log structured decision output alongside existing control outcomes.
   - No enforcement changes yet.
2. **Drift review**
   - Compare policy decisions with current behavior.
   - Document mismatches, root causes, and required policy updates.
3. **Enforcement gate enablement**
   - Add deny enforcement path only after drift is understood.
   - Keep fail-closed for missing identity/classification/tool context.
4. **Observability and evidence**
   - Emit policy id, reason, and missing fields in audit events.
   - Track deny-rate and missing-context metrics.
5. **OPA migration (future)**
   - Replace YAML evaluator with OPA sidecar/embedded evaluation.
   - Reuse same input contract and decision schema.

## Constraints
- Default deny must remain true in all environments.
- Missing context must deny (fail-closed).
- External services are optional; local evaluation remains supported.
- No claim of OPA runtime integration until implemented and verified.

## Unknowns / Partially Confirmed
- **Unknown**: exact Onyx modules where retrieval/tool checks should be hooked first.
- **Partially Confirmed**: policy semantics validated by local unit tests; not yet validated against live Onyx request traces.
