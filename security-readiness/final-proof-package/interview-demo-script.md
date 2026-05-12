# Interview Demo Script

**Audience:** Hiring panels, staff+ engineers, security architects  
**Duration:** 20–30 minutes

## Opening (2 minutes)
"This is an AI Trust & Security Readiness case study for an internal company knowledge assistant. The pattern is Morgan Stanley-style as inspiration only, with no affiliation claim. The key outcome is not feature hype; it is disciplined launch gating based on evidence."

## Problem Statement (3 minutes)
- Internal assistants fail when they leak data, ignore identity boundaries, or overclaim confidence.
- I framed the project around fail-closed controls and auditable release decisions.
- Success criterion: can we prove enough to launch safely?

## Scope and Build (5 minutes)
- Built readiness artifacts around two launch modes:
  - `RAG_ONLY`
  - `RAG_PLUS_TOOLS`
- Mapped and implemented core controls:
  - `RetrievalAuthorizationGuard`, `RetrievalGuardAdapter`, `BypassACLContract`
  - `TrustedSystemContextInputBoundary`, `PromptInjectionBoundary`
  - `CitationSourceLeakageFilter`
  - `AuditLogger`, `RuntimeTracer`, `LaunchGateEngine`

## Evidence Maturity Model (4 minutes)
- Tier 1: design intent
- Tier 2: static/config confirmation
- Tier 3: test/validator outputs
- Tier 4: runtime adversarial proof
- Tier 5: launch-grade closure

"The key professional behavior is refusing to call Tier 3/4 evidence 'launch ready' when Tier 5 conditions are unmet."

## Results (4 minutes)
**Passed evidence categories:**
- dependency-light tests,
- runtime-adjacent tests,
- validator/dashboard generation.

**Blocked categories:**
- full backend runtime retrieval authorization,
- full runtime citation leakage,
- full runtime prompt-injection/red-team,
- complete evidence pack,
- complete `RAG_PLUS_TOOLS` tool authorization wiring evidence.

## Decision Discipline (3 minutes)
- Launch gate output: `NOT_ENOUGH_EVIDENCE`.
- This is the correct decision under fail-closed policy.
- I intentionally avoid false-positive launch decisions.

## Close (2 minutes)
"This work demonstrates how to retrofit AI controls into real systems and make launch decisions from evidence rather than optimism."
