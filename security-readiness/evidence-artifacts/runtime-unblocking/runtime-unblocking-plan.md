# Runtime Evidence Unblocking Plan (Final 5 Launch Blockers)

Date (UTC): 2026-05-12  
Decision posture: **NOT_ENOUGH_EVIDENCE** (unchanged)  
Scope: Planning/evidence-readiness only (no runtime control changes)

## 1) Backend environment blocker

### Problem statement
Tier 4 full backend/runtime evidence is blocked by environment readiness for integration and red-team execution paths.

### Current state
- Validator-complete checks: **15**.
- Critical blockers still failing: retrieval authorization, citation leakage, prompt-injection runtime PASS, zero critical open risks, complete evidence pack.

### Root cause summary
- Existing evidence is Tier 2/Tier 3 (dependency-light/runtime-adjacent).
- Required full-runtime test harness inputs (runtime services, seeded data, identity contexts, red-team execution channel, and artifact writing path) are not yet consistently available in one reproducible backend test environment.

### Unblocking objective
Provision a reproducible backend test environment that can execute and persist full-runtime outputs for:
1. Retrieval authorization runtime tests.
2. Citation leakage runtime tests.
3. Prompt-injection boundary/red-team runtime tests.

## 2) Retrieval authorization runtime test plan

- **Current observed value:** `BLOCKED`.
- **Expected value:** `PASS` / `PASSED`.
- **Current evidence file:** `security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json`.
- **Root cause:** dependency-light and runtime-adjacent signals exist, but no validated full backend/runtime PASS artifact yet.
- **Exact command/test needed:**
  - `python security-readiness/scripts/run-evidence-validation.py`
  - Runtime execution command to produce `retrieval-authorization-tests.json` with full backend integration (canonical command to be finalized by environment plan; see `backend-test-environment-plan.md`).
- **Dependencies:** backend service stack up, test identity fixtures, authorized/unauthorized corpus fixtures, artifact write permissions, deterministic test seed.
- **Artifact to generate:**
  - `security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json` (full-runtime PASS evidence),
  - supporting command/output log in a run folder under `security-readiness/evidence-artifacts/runtime-unblocking/runs/`.
- **Can close without full backend runtime?** **No**.
- **Risk if unresolved:** access-boundary enforcement remains unproven at runtime; launch must remain fail-closed.

## 3) Citation leakage runtime test plan

- **Current observed value:** `BLOCKED`.
- **Expected value:** `PASS` / `PASSED`.
- **Current evidence file:** `security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`.
- **Root cause:** current citation leakage evidence is dependency-light/partial and does not prove full-runtime behavior.
- **Exact command/test needed:**
  - `python security-readiness/scripts/run-evidence-validation.py`
  - Runtime citation leakage suite command to emit full-runtime `citation-leakage-tests.json` (defined in execution runbook).
- **Dependencies:** full backend runtime, citation-generating retrieval scenarios, sensitive-source fixture corpus, leakage assertions in integrated response path.
- **Artifact to generate:**
  - `security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`,
  - run log + stdout/stderr snapshot in runtime-unblocking run folder.
- **Can close without full backend runtime?** **No**.
- **Risk if unresolved:** source leakage control remains unproven in end-to-end responses.

## 4) Prompt-injection runtime/red-team test plan

- **Current observed value:** `null` (missing full-runtime PASS).
- **Expected value:** `PASS` / `PASSED`.
- **Current evidence file:** `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`.
- **Root cause:** dependency-light boundary checks exist, but full-runtime prompt-injection/red-team execution evidence is missing.
- **Exact command/test needed:**
  - `python security-readiness/scripts/run-evidence-validation.py`
  - Full-runtime prompt-injection/red-team test command to produce updated `prompt-injection-boundary-tests.json`.
- **Dependencies:** backend runtime environment, adversarial prompt suite, policy decision logging enabled, deterministic scenario IDs for audit traceability.
- **Artifact to generate:**
  - `security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`,
  - scenario-level runtime logs and summarized findings in runtime-unblocking run folder.
- **Can close without full backend runtime?** **No**.
- **Risk if unresolved:** inability to prove runtime prompt-boundary resilience; launch gate must remain NOT_ENOUGH_EVIDENCE.

## 5) Critical risk closure plan

- **Current observed value:** `1` open critical risk.
- **Expected value:** `0`.
- **Current evidence file:** `security-readiness/evidence-artifacts/risk/open-risk-summary.json`.
- **Root cause:** at least one critical risk remains open because the linked runtime evidence blockers are unresolved.
- **Exact command/test needed:**
  - Re-run runtime blocker suites above,
  - regenerate open-risk summary,
  - `python security-readiness/scripts/run-evidence-validation.py`.
- **Dependencies:** closure or downgrade of critical risk with evidence-backed justification; updated risk register references.
- **Artifact to generate:** updated `open-risk-summary.json` showing zero critical open risks, plus risk decision note in runtime-unblocking folder.
- **Can close without full backend runtime?** **Generally no** for this current blocker set, because risk is evidence-driven.
- **Risk if unresolved:** launch gate fails critical risk criterion regardless of other partial evidence.

## 6) Evidence pack completion plan

- **Current observed value:** `false`.
- **Expected value:** `true`.
- **Current evidence file:** `security-readiness/evidence-artifacts/evidence-pack/evidence-pack-status.json`.
- **Root cause:** evidence pack missing required full-runtime artifacts and/or completeness markers tied to the five blockers.
- **Exact command/test needed:**
  - Collect artifacts generated by sections 2–5,
  - regenerate pack status,
  - `python security-readiness/scripts/run-evidence-validation.py`.
- **Dependencies:** successful upstream runtime artifact generation, consistent metadata fields, and validator-compatible file paths.
- **Artifact to generate:** updated `evidence-pack-status.json` and completeness checklist.
- **Can close without full backend runtime?** **No** for this final stage.
- **Risk if unresolved:** validator remains fail-closed at evidence-pack gate.

## 7) Recommended execution order

1. Confirm backend environment readiness (hard prerequisite).
2. Execute retrieval authorization runtime suite.
3. Execute citation leakage runtime suite.
4. Execute prompt-injection/red-team runtime suite.
5. Refresh critical risk summary from new results.
6. Refresh evidence-pack completeness.
7. Run validator and launch-gate scripts; expect decision to remain fail-closed until all checks are PASS.

## 8) Do-not-overclaim rules

1. Do **not** mark any blocker closed in this plan.
2. Do **not** set launch gate to **GO** in planning artifacts.
3. Do **not** infer runtime PASS from dependency-light or runtime-adjacent results.
4. Label unresolved controls as **Unknown** or **Partially Confirmed** until full-runtime artifacts are produced.
5. Keep all assertions traceable to generated artifacts and command output.
