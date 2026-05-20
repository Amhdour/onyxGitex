# Gap Remediation Plan (Tier 4 Closure)

Date (UTC): 2026-05-20
Owner: AI Trust & Security Readiness Engineering
Status: In Progress

## Purpose
Close the highest-impact readiness gaps that currently block GO by producing validator-consumable Tier 4 runtime evidence.

## Current Blocking Gaps

1. **RetrievalAuthorizationGuard runtime proof gap**
   - Current state: Runtime-adjacent evidence exists; full runtime PASS remains blocked.
   - Required closure evidence: Passing full backend/runtime test artifact accepted by launch-gate validators.

2. **CitationSourceLeakageFilter runtime proof gap**
   - Current state: Dependency-light PASS exists; full runtime citation leakage evidence remains blocked.
   - Required closure evidence: Full runtime citation leakage PASS artifact accepted by validator.

3. **PromptInjectionBoundary runtime proof gap**
   - Current state: Dependency-light boundary tests pass; integrated runtime/red-team PASS missing.
   - Required closure evidence: Runtime prompt-injection test and adversarial run artifacts with PASS status.

4. **Tool authorization/runtime wiring Tier 4 evidence gap**
   - Current state: Runtime context wiring exists in `backend/onyx/chat/llm_loop.py` via runtime adapter path; full runtime validator-consumable PASS evidence not yet attached.
   - Required closure evidence: Full runtime execution artifacts proving enforcement and deny-before-dispatch behavior under RAG+TOOLS mode.

## Remediation Work Plan (Ordered)

1. Run narrow Tier 4 retrieval guard runtime tests first.
2. Run runtime citation leakage tests.
3. Run runtime prompt-injection and abuse-case tests.
4. Run runtime tool authorization + MCP deny-before-dispatch tests in RAG+TOOLS mode.
5. Publish all outputs to `security-readiness/evidence-artifacts/test-results/` in validator-consumable format.
6. Re-run launch gate and evidence completeness validator.
7. Update canonical control status and residual risk register with exact pass/fail deltas.

## Evidence Acceptance Criteria

- Each closure item includes:
  - exact test command,
  - raw test output,
  - timestamp (UTC),
  - git commit SHA,
  - normalized JSON result artifact consumed by launch gate.
- Any failed or skipped test is labeled **Unknown** or **Partially Confirmed** with explicit blocker reason.
- No production readiness claim is made unless launch gate returns GO and critical controls are Tier 4 PASS.

## Immediate Next Commands (Planned)

- `pytest -q backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py`
- Runtime citation leakage suite command (environment-specific)
- Runtime prompt-injection suite command (environment-specific)
- Runtime tool authorization + MCP deny-before-dispatch suite command (environment-specific)

## Risk if Unresolved

- Continued **NOT_ENOUGH_EVIDENCE** decision at launch gate.
- RAG+TOOLS launch remains blocked due to unproven runtime enforcement.
