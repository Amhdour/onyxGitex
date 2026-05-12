# Tier 4 Runtime Fixture Design and Implementation Plan

## Scope and posture
- Date: 2026-05-12.
- Objective: convert Tier 4 skeleton tests into executable full-runtime tests for three launch blockers:
  - `retrieval_authorization_tests`
  - `citation_leakage_tests`
  - `prompt_injection_boundary_tests`
- Current launch posture remains: **NOT_ENOUGH_EVIDENCE**.
- This document is a design and implementation plan only; it is not execution evidence and does not mark any test as PASS.

## Blocker alignment
The three executable Tier 4 tests defined by this plan target the validator-failing items that depend on full-runtime signals:
1. Retrieval authorization behavior at runtime.
2. Citation leakage resistance at runtime.
3. Prompt-injection boundary enforcement at runtime.

These tests are expected to produce artifacts that contribute evidence toward (but do not automatically satisfy):
- `no_critical_open_risks`
- `evidence_pack_complete`

## Implementation phases
1. **Fixture implementation**
   - Build deterministic fixtures for identities, documents, sessions, requests, and capture hooks.
2. **Runtime harness wiring**
   - Wire fixture setup into Tier 4 runner to call real runtime path (chat/retrieval pipeline) with no mocked authorization decision.
3. **Assertion enforcement**
   - Add explicit assertions for allow/deny output, leakage markers, audit events, and runtime traces.
4. **Artifact writer integration**
   - Emit per-test JSON artifacts using defined schema and include run metadata.
5. **CI collection update (if needed)**
   - Ensure collection picks up new artifact files and retains fail-closed behavior on schema/trace gaps.

## Global constraints for all three tests
- Fail closed if required capture channels (audit or trace) are missing.
- Use deterministic fixture IDs and seeded content to avoid flaky matching.
- Keep adversarial payload corpus versioned and immutable per run.
- Record unknowns explicitly rather than downgrading severity.
- Do not infer PASS from partial signals.

## Full fixture inventory
The required fixtures are implemented once and re-used across all three tests:
1. `authorized_user`
2. `unauthorized_user`
3. `allowed_document`
4. `restricted_document`
5. `allowed_document_set`
6. `restricted_document_set`
7. `chat_session`
8. `retrieval_request`
9. `citation_capture`
10. `audit_event_capture`
11. `runtime_trace_capture`
12. `adversarial_prompt_corpus`

Refer to `fixture-map.json` for authoritative fixture contract definitions.

## Runtime call path requirement
Each Tier 4 test must exercise the **actual runtime request path** used in production-equivalent retrieval chat execution:
- Authenticated user context
- Retrieval + ranking path
- LLM answer generation with citations
- Audit and trace instrumentation path

The test harness should not bypass policy checks via direct helper invocation when evaluating blocker controls.

## Deliverables produced by this plan
- `fixture-map.json` (fixture contract and reuse matrix)
- `retrieval-runtime-assertions.md`
- `citation-leakage-runtime-assertions.md`
- `prompt-injection-runtime-assertions.md`
- `audit-trace-capture-plan.md`
- `artifact-writer-plan.md`

## Expected result state after implementation (not execution)
- Tier 4 skeletons become executable with deterministic fixtures and explicit assertions.
- Launch posture stays **NOT_ENOUGH_EVIDENCE** until runtime tests execute and evidence is reviewed.
