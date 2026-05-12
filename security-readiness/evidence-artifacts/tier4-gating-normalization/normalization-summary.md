# Tier 4 Gating Normalization Summary

Date (UTC): 2026-05-12

## Scope
Normalized fail-closed PASS gating logic in the three Tier 4 runtime suites:
- retrieval authorization runtime
- citation leakage runtime
- prompt-injection boundary runtime

## Changes Applied
- Removed reliance on `ASSERTIONS_EXECUTED` global state.
- Standardized partial-execution detection to `any(ASSERTION_COMPLETION.values())`.
- Preserved PASS requirement of `all(ASSERTION_COMPLETION.values())` via `_all_required_assertions_completed()`.
- Standardized partial-completion behavior to write `FAILED` artifacts using `mark_failed(...)` with missing assertion keys listed.
- Added explicit fail-closed `BLOCKED` artifact write when no assertions execute at all.
- Preserved suite-specific required assertion keys.
- Preserved `launch_posture=NOT_ENOUGH_EVIDENCE` through existing artifact writer defaults.

## Non-goals Preserved
- No blocker converted to PASS.
- No evidence-pack completion claims added.
- No critical-risk closure claims added.
