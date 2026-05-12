# Runtime Control Points Update (Priority 2)

**Date:** 2026-05-11

## Control Points (Scaffold)
1. **Policy evaluation point**: `PolicyDecisionEngine.evaluate()` before any protected retrieval/tool action.
2. **Retrieval authorization point**: `RetrievalAuthorizationGuard.authorize_document()` before returning document content.
3. **Tool authorization point**: `ToolAuthorizationRouter.authorize_tool()` before tool invocation.
4. **Audit event point**: `AuditLogger.emit()` on authorization decisions and denied actions.
5. **Trace event point**: `RuntimeTracer.emit()` at retrieval/tool policy checkpoints.
6. **Fail-closed point**: `FailClosedError` raised on missing required auth/policy context.
7. **Evidence point**: `EvidencePackGenerator.generate_manifest()` after control test executions.
8. **Launch decision point**: `LaunchGateEngine.evaluate()` post-score calculation.
9. **Readiness score point**: `ReadinessScoringEngine.calculate()` from weighted control results.
10. **Dashboard export point**: `DashboardDataExporter.export_json/export_csv()` for reporting artifacts.

## Integration Note
These points are implemented as adapters/scaffolds and are not wired into all production runtime paths yet.


## Diagram Reference
- `security-readiness/04-controls/diagrams/control-coverage-map.mmd`
- `security-readiness/04-controls/diagrams/retrieval-authorization-flow.mmd`
- `security-readiness/04-controls/diagrams/tool-authorization-flow.mmd`
