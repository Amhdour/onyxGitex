# Tier 4 Test Execution Order

Date (UTC): 2026-05-12

## Purpose
Provide strict, dependency-aware ordering to move from runtime-adjacent evidence to full backend/runtime evidence.

## Ordered steps
1. **Environment readiness gate**
   - Confirm backend test environment prerequisites from `backend-test-environment-plan.md`.
   - Output artifact: run preflight checklist record.

2. **Retrieval authorization runtime suite**
   - Execute full backend/runtime retrieval authorization tests.
   - Output artifact: `security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json`.

3. **Citation leakage runtime suite**
   - Execute full backend/runtime citation leakage tests.
   - Output artifact: `security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`.

4. **Prompt-injection boundary + runtime red-team suite**
   - Execute full backend/runtime adversarial boundary tests.
   - Output artifact: `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`.

5. **Critical risk refresh**
   - Reconcile runtime results with risk register.
   - Output artifact: `security-readiness/evidence-artifacts/risk/open-risk-summary.json`.

6. **Evidence pack refresh**
   - Ingest produced artifacts and update completeness status.
   - Output artifact: `security-readiness/evidence-artifacts/evidence-pack/evidence-pack-status.json`.

7. **Validator rerun**
   - Command: `python security-readiness/scripts/run-evidence-validation.py`.
   - Output artifact: refreshed evidence-validation results.

## Stop conditions
- If any runtime suite errors or is blocked, stop and record blocker state as unresolved.
- Do not infer PASS from partial data.

## Guardrails
- Keep launch gate as **NOT_ENOUGH_EVIDENCE** until validator criteria are objectively met.
