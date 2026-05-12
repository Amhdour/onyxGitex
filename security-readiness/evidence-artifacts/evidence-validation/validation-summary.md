# Launch Evidence Validation Summary

- Generated at: `2026-05-12T16:47:50+00:00`
- Overall status: **FAILED**
- Allow GO: **False**
- Pre-launch status: **FAILED**
- Post-launch status: **COMPLETE**
- Draft decision only: **True**
- Active launch mode: **RAG_ONLY**
- Tools enabled: **False**

## Counts
- Complete: 14
- Missing: 0
- Failed: 6
- Skipped: 3
## Failed Evidence
- `retrieval_authorization_tests`: Evidence artifact does not meet pass criteria (`security-readiness/evidence-artifacts/test-results/retrieval-authorization-tests.json`)
- `citation_leakage_tests`: Evidence artifact does not meet pass criteria (`security-readiness/evidence-artifacts/test-results/citation-leakage-tests.json`)
- `prompt_injection_boundary_tests`: Evidence artifact does not meet pass criteria (`security-readiness/evidence-artifacts/test-results/prompt-injection-boundary-tests.json`)
- `mcp_deny_before_dispatch_adjacent`: Evidence artifact does not meet pass criteria (`security-readiness/evidence-artifacts/test-results/mcp-deny-before-dispatch-tests.json`)
- `no_critical_open_risks`: Evidence artifact does not meet pass criteria (`security-readiness/evidence-artifacts/risk/open-risk-summary.json`)
- `evidence_pack_complete`: Evidence artifact does not meet pass criteria (`security-readiness/evidence-artifacts/evidence-pack/evidence-pack-status.json`)

## Skipped Evidence
- `tool_authorization_tests`: Skipped because launch mode is RAG_ONLY
- `tool_runtime_wiring_verified`: Skipped because launch mode is RAG_ONLY
- `mcp_tool_hardening_verified`: Skipped because tools are disabled
