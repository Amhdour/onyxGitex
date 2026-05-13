#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
S=Path('agent-security-readiness/23-langgraph-agent-lab/final-run-status.json');LAB=S.parent
def fail(m): print(f'FAIL: {m}'); raise SystemExit(1)
d=json.loads(S.read_text()); sd=d.get('status_dimensions',{})
for k in ['real_langgraph_status','compatibility_runtime_status','sandboxed_tool_status','ci_workflow_status','ci_artifact_status']:
    if k not in sd: fail(f'missing status field {k}')
for sec in ['memory_evidence','sandboxed_tool_evidence','incident_trace_evidence','ci_evidence']:
    if sec not in d: fail(f'missing section {sec}')
if sd.get('ci_artifact_status')=='CI_ARTIFACT_VERIFIED' and sd.get('ci_workflow_status') not in {'CI_PASS','CI_ARTIFACT_VERIFIED'}: fail('ci status mismatch')
if sd.get('launch_gate_status')=='GO' and sd.get('evidence_status') in {'PARTIAL_EVIDENCE','NOT_ENOUGH_EVIDENCE'}: fail('GO requires stronger evidence')
if sd.get('real_langgraph_status')=='NOT_AVAILABLE' and any('production LangGraph runtime verified' in c for c in d.get('claims_allowed',[])): fail('overclaim')
if ('PARTIAL' in sd.get('sandboxed_tool_status','') or 'VERIFIED' in sd.get('sandboxed_tool_status','')) and not (LAB/'graph-runtime-artifacts/graph-sandboxed-tool-results.json').exists(): fail('missing sandbox artifact')
if ('PARTIAL' in sd.get('memory_boundary_status','') or 'VERIFIED' in sd.get('memory_boundary_status','')) and not (LAB/'graph-runtime-artifacts/graph-memory-boundary-log.json').exists(): fail('missing memory artifact')
if sd.get('incident_trace_status')=='RUNTIME_ARTIFACTS_PRESENT' and not (LAB/'graph-runtime-artifacts/graph-incident-timeline.json').exists(): fail('missing incident artifact')
print('PASS: final-run-status.json consistency checks passed')
