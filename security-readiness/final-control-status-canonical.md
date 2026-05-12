# Final Control Status Canonical

Date (UTC): 2026-05-12

| Control | Code path | Runtime wired | Test exists | Test passes | Evidence artifact exists | Evidence recognized by validator | Launch gate impact | Exact next action |
|---|---|---|---|---|---|---|---|---|
| RetrievalAuthorizationGuard | `backend/onyx/context/search/pipeline.py` | Yes | Yes | Blocked | Yes | No | Blocks GO as fail-closed retrieval evidence is not passing | Run `pytest -q backend/tests/unit/onyx/context/search/test_pipeline_retrieval_guard.py` in supported backend env and publish PASS JSON artifact. |
| PureControlLayerUnitTests | `security-readiness/evidence-artifacts/pure-control-unit-tests/test_pure_control_layer.py` | No (unit only) | Yes | PASS | Yes | Yes | Improves confidence only; does not unblock GO and does not prove runtime enforcement | Keep as limited unit evidence and pair with runtime retrieval/tool-path integration tests before GO. |
| CitationSourceLeakageDependencyLight | `security-readiness/evidence-artifacts/citation-source-leakage/test_citation_source_leakage.py` + `backend/onyx/context/search/citation_filter.py` | No (dependency-light only) | Yes | PASS (dependency-light), Full runtime: NOT_PASS_BLOCKED | Yes | Yes (dependency-light only) | Partial positive evidence only; full runtime citation leakage remains blocking for GO | Preserve strict launch gate: keep `citation_leakage_tests` fail-closed until full runtime citation leakage evidence is PASS. |
| ToolAuthorizationRouter | `backend/onyx/tools/tool_runner.py` | Partial | Yes | Blocked | Yes | No | Not fully enforced in main runtime path and not validator-passing | Pass authorization context from `backend/onyx/chat/llm_loop.py` into `run_tool_calls` and execute tool runtime tests in supported env. |
| Policy-as-Code evaluator | `onyx/security_readiness/control_layer` + policy tests artifact | Partial | Yes | Blocked | Yes | No | Cannot claim full policy enforcement readiness | Add runtime invocation evidence from retrieval + tool paths and re-run policy-related suites. |
| AuditLogger | `backend/onyx/context/search/pipeline.py`, `backend/onyx/tools/tool_runner.py` | Yes | Yes | Blocked | Yes | Yes | Still blocked by other critical evidence failures | Keep artifacts; add passing test execution proof that generated events were created in run. |
| RuntimeTracer | `backend/onyx/context/search/pipeline.py`, `backend/onyx/tools/tool_runner.py` | Yes | Yes | Blocked | Yes | Yes | Still blocked by other critical evidence failures | Add passing run showing traces generated in tested runtime path. |
| Evidence validator | `security-readiness/scripts/validate-launch-evidence.py` | Yes | N/A | N/A | Yes | N/A | Current status remains INCOMPLETE/FAILED for GO | Keep strict checks; do not downgrade failure rules. |
| LaunchGateEngine | `security-readiness/scripts/run-launch-gate.py` | Yes | N/A | N/A | Yes | Partial | Produces NOT_ENOUGH_EVIDENCE | Preserve strict fail-closed decision logic and consume updated validator artifacts only. |
| DashboardDataExporter | `security-readiness/scripts/export-dashboard-data.py` | Yes | N/A | N/A | Yes | Partial | Dashboard must mirror validator and launch-gate blockers | Regenerate dashboard after validator + launch gate and keep maturity label below Level 4 while tests blocked. |

## Runtime enforcement note

Tool authorization is **Not Fully Enforced** for the main chat runtime because `backend/onyx/chat/llm_loop.py` currently calls `run_tool_calls` without `authorization_router`, `user_id`, and `tool_policy` inputs.

## Limited unit evidence note

- Pure control-layer unit tests: **PASS**
- Evidence type: **limited unit evidence**
- Runtime proof: **No**
- Launch gate effect: **improves confidence but does not unblock GO**

## Citation/source leakage dependency-light evidence note

- Dependency-light citation/source leakage tests: **PASS**
- Full runtime citation leakage status: **NOT_PASS_BLOCKED**
- Evidence type: **dependency-light test evidence**
- Runtime proof: **No**
- Launch gate effect: **partial positive evidence only; GO remains blocked until full runtime citation leakage tests pass**
