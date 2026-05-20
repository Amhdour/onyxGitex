# Readiness Gaps and Suggestions (2026-05-20)

## Scope

This artifact captures the currently observed launch-readiness gaps and recommended remediation actions, based on the current repository evidence and decision artifacts.

## Current Status Summary

- Launch posture remains **NO_GO / NOT_ENOUGH_EVIDENCE**.
- Existing documentation confirms partial positive evidence for some controls, but critical runtime proof remains incomplete.

## Observed Gaps

### Gap 1 — Runtime evidence remains incomplete for launch-critical controls

**Status:** Partially Confirmed  
**Evidence:** Final readiness report marks runtime telemetry, red-team execution logs, and live policy decision logs as not collected/pending.

**Impact:** Launch decision cannot move to GO without runtime-grade evidence.

### Gap 2 — Tier mismatch between control confidence and launch requirement

**Status:** Verified  
**Evidence:** Canonical control status shows multiple controls at Tier 2/Tier 3 with dependency-light or runtime-adjacent PASS, while Tier 4 runtime evidence remains blocked for key controls.

**Impact:** Confidence signal exists, but does not satisfy full runtime launch criteria.

### Gap 3 — Information architecture drift versus canonical phase model

**Status:** Partially Confirmed  
**Evidence:** Repository guidance recommends a 01–09 lifecycle structure, while the active `security-readiness/` tree includes many additional tracks and supporting folders.

**Impact:** Audit and reviewer navigation cost is higher unless phase crosswalk mapping is explicit.

### Gap 4 — Evidence freshness and artifact dating can be more explicit

**Status:** Partially Confirmed  
**Evidence:** Key decision documents include dates, but a consistent per-artifact “last validated on” stamp is not uniformly enforced across all launch-critical artifacts.

**Impact:** Reviewers may misread stale evidence as current.

### Gap 5 — Launch-gate contract is distributed, not singularly operationalized

**Status:** Partially Confirmed  
**Evidence:** Required tests/actions are present across multiple files, but no single compact contract file defines exact command → artifact → pass criteria → owner for each critical control.

**Impact:** Execution tracking and accountability can drift across teams.

## Recommended Actions (Prioritized)

### Priority 0 — Create a single launch-gate minimum evidence contract

Create one authoritative artifact (e.g., `security-readiness/10-decision/launch-gate-minimum-evidence-contract.md`) that lists, per P0/P1 control:

- exact test command,
- required artifact file path,
- required pass criteria,
- control owner,
- due date,
- current status (Verified / Partially Confirmed / Unknown).

**Expected result:** Removes ambiguity and creates executable accountability.

### Priority 1 — Focus execution on three blocking runtime proofs

Run and publish validator-consumable Tier 4 evidence for:

1. Retrieval authorization fail-closed runtime behavior,
2. Prompt-injection runtime boundary behavior,
3. Tool authorization/runtime wiring enforcement.

**Expected result:** Directly addresses the controls currently blocking GO.

### Priority 2 — Add a canonical lifecycle crosswalk index

Create an index mapping current folders/artifacts to canonical lifecycle phases for reviewers and auditors.

**Expected result:** Faster external review and lower interpretation risk.

### Priority 3 — Standardize freshness stamping on launch-critical artifacts

Add a required metadata block at top of each launch-critical artifact:

- `artifact_owner`,
- `last_validated_on_utc`,
- `evidence_window_start_utc`,
- `evidence_window_end_utc`,
- `confidence_state`.

**Expected result:** Prevents stale-evidence ambiguity.

### Priority 4 — Preserve fail-closed launch discipline until Tier 4 proof is complete

Continue enforcing **NOT_ENOUGH_EVIDENCE** and **NO_GO** until Tier 4 runtime artifacts for critical controls are passing and validator-recognized.

**Expected result:** Prevents unsupported readiness claims and aligns with stated safety rules.

## Tracking Format for Immediate Use

Use the checklist below to track execution progress:

- [ ] Launch-gate minimum evidence contract created and approved.
- [ ] Retrieval authorization Tier 4 runtime artifact published and validator-recognized.
- [ ] Prompt-injection Tier 4 runtime artifact published and validator-recognized.
- [ ] Tool authorization/runtime wiring Tier 4 runtime artifact published and validator-recognized.
- [ ] Phase crosswalk index created and linked from `security-readiness/README.md`.
- [ ] Freshness metadata block added to all launch-critical artifacts.
- [ ] Launch decision re-run with updated evidence package.

## Notes

- This document does not assert production readiness.
- Any control not proven by code/config/test output remains **Partially Confirmed** or **Unknown**.
