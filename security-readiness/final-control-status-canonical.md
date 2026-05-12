# Final Control Status Canonical

Date (UTC): 2026-05-12

## RAG Evidence Maturity Tier Legend

- **Tier 0** — Documentation only
- **Tier 1** — Control code exists
- **Tier 2** — Dependency-light tests pass
- **Tier 3** — Runtime-adjacent tests pass
- **Tier 4** — Full backend/runtime tests pass
- **Tier 5** — Client-specific production evidence exists

## Control Status and Maturity

| Control | Tier achieved | Code path | Runtime wired | Test exists | Test passes | Evidence artifact exists | Evidence recognized by validator | Launch gate impact | Exact next action |
|---|---:|---|---|---|---|---|---|---|---|
| RetrievalAuthorizationGuard | 3 | `backend/onyx/context/search/pipeline.py` | Yes | Yes | Blocked | Yes | No | Blocks GO as fail-closed retrieval evidence is not passing | Run `pytest -q backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py` in supported backend env and publish PASS JSON artifact. |
| RetrievalGuardAdapter | 3 | `backend/onyx/context/search/pipeline.py` | Partial | Yes | PASS (adapter/path evidence) | Yes | Partial | Adapter/path evidence improves confidence but does not satisfy full runtime proof | Execute full backend runtime retrieval path test and publish validator-consumable PASS artifact. |
| BypassACLContract | 2 | `security-readiness/evidence-artifacts/pure-control-unit-tests/test_pure_control_layer.py` | No (dependency-light) | Yes | PASS | Yes | Yes (dependency-light only) | Partial evidence only; GO remains blocked pending runtime evidence | Add runtime-adjacent + full runtime ACL bypass enforcement evidence. |
| TrustedSystemContextInputBoundary | 2 | `backend/onyx/security/trusted_system_context.py` + schema test artifact | No (dependency-light) | Yes | PASS | Yes | Yes (dependency-light only) | Partial evidence only; runtime boundary still unproven | Add runtime invocation evidence for schema boundary under live prompt construction path. |
| CitationSourceLeakageFilter | 2 | `security-readiness/evidence-artifacts/citation-source-leakage/test_citation_source_leakage.py` + `backend/onyx/context/search/citation_filter.py` | No (dependency-light only) | Yes | PASS (dependency-light), Full runtime: NOT_PASS_BLOCKED | Yes | Yes (dependency-light only) | Partial positive evidence only; full runtime citation leakage remains blocking for GO | Preserve strict launch gate: keep `citation_leakage_tests` fail-closed until full runtime citation leakage evidence is PASS. |
| PromptInjectionBoundary | 2 | `backend/onyx/security_readiness/prompt_injection_boundary.py` + `security-readiness/evidence-artifacts/prompt-injection-boundary/test_prompt_injection_boundary.py` | No (dependency-light boundary only) | Yes | PASS (8/8), Full runtime: NOT_PASS_BLOCKED | Yes | Yes (dependency-light only) | Partial positive evidence only; full runtime prompt-injection/red-team remains blocking for GO | Keep boundary tests strict and blocked until integrated runtime prompt-injection and red-team evidence is PASS. |
| ToolRuntimeWiringAdapter | 3 | `backend/onyx/security_readiness/tool_runtime_wiring_adapter.py` + `security-readiness/evidence-artifacts/test-results/tool-runtime-wiring-adjacent-tests.json` | No (runtime-adjacent adapter only) | Yes | PASS (runtime-adjacent adapter) + PASS (main llm_loop.py runtime-adjacent) + PASS (research-agent runtime-adjacent) + PASS (MCP deny-before-dispatch runtime-adjacent), Full runtime: NOT_PASS, MCP hardening: NOT_PASS | Yes | Yes (non-critical runtime-adjacent only) | Adds Tier 3 runtime-adjacent confidence signal only; RAG_PLUS_TOOLS remains NOT_READY and GO stays blocked | Keep adapter evidence recognized as non-critical; require full production wiring proof in `llm_loop.py` + research-agent paths before promoting runtime wiring control. |
| ToolRuntimeContextGuard | 2 | `backend/onyx/security_readiness/tool_runtime_context_guard.py` + `security-readiness/evidence-artifacts/test-results/tool-runtime-context-guard-tests.json` | No (dependency-light only) | Yes | PASS (dependency-light), Runtime wiring: NOT_PASS | Yes | Yes (dependency-light only) | Partial positive signal only; RAG_PLUS_TOOLS remains blocked until runtime wiring is proven in llm_loop.py and research-agent runtime | Preserve dependency-light PASS as a non-critical positive signal and keep runtime wiring checks fail-closed for RAG_PLUS_TOOLS mode. |
| ToolAuthorizationRouter | 2 | `backend/onyx/tools/tool_runner.py` + `security-readiness/evidence-artifacts/test-results/tool-authorization-dependency-light-tests.json` | Partial | Yes | PASS (dependency-light), Runtime wiring: NOT_PASS | Yes | Yes (dependency-light only) | Partial positive signal only; RAG_PLUS_TOOLS remains blocked until runtime wiring and full tool authorization pass | Pass authorization context from `backend/onyx/chat/llm_loop.py` into `run_tool_calls` and execute runtime tool authorization + wiring tests in supported env. |
| AuditLogger | 3 | `backend/onyx/context/search/pipeline.py`, `backend/onyx/tools/tool_runner.py` | Yes | Yes | PASS (runtime-adjacent) | Yes | Yes | Supports traceability, but launch still blocked by critical runtime gaps | Add passing full runtime execution proof that generated audit events were created in-run. |
| RuntimeTracer | 3 | `backend/onyx/context/search/pipeline.py`, `backend/onyx/tools/tool_runner.py` | Yes | Yes | PASS (runtime-adjacent) | Yes | Yes | Improves observability confidence; GO still blocked by critical runtime gaps | Add passing full runtime run showing traces generated in tested runtime path. |
| LaunchGateEngine | 3 | `security-readiness/scripts/run-launch-gate.py` | Yes | N/A | N/A | Yes | Partial | Produces NOT_ENOUGH_EVIDENCE fail-closed decision | Preserve strict fail-closed decision logic and consume updated validator artifacts only. |

## Runtime enforcement note

Tool authorization is **Not Fully Enforced** for the main chat runtime because `backend/onyx/chat/llm_loop.py` currently calls `run_tool_calls` without `authorization_router`, `user_id`, and `tool_policy` inputs.

## Launch decision

- Active launch mode: **RAG_ONLY** (default)
- Tool authorization evidence in RAG_ONLY: **Dependency-light PASS is recognized; runtime wiring/full-runtime enforcement still not passing and remains visible as skipped/blocked by mode**
- RAG_PLUS_TOOLS policy: **Missing tool authorization/runtime wiring evidence blocks GO**
- Current launch decision: **NOT_ENOUGH_EVIDENCE**
- GO decision: **Blocked** pending Tier 4 evidence for critical runtime controls.
