#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
S=Path('agent-security-readiness/23-langgraph-agent-lab/final-run-status.json');LAB=S.parent

def fail(m): print(f'FAIL: {m}'); raise SystemExit(1)
d=json.loads(S.read_text()); sd=d.get('status_dimensions',{})
for k in ['real_langgraph_status','real_langgraph_attempt_status','compatibility_runtime_status','sandboxed_tool_status','ci_workflow_status','ci_artifact_status','telemetry_mapping_status']:
    if k not in sd: fail(f'missing status field {k}')
if sd.get('launch_gate_status')=='GO': fail('launch gate must not be GO')
if sd.get('ci_artifact_status')=='CI_ARTIFACT_VERIFIED' and not d.get('ci_evidence',{}).get('artifact_verified',False): fail('ci artifact verified mismatch')
if sd.get('ci_artifact_status')=='CI_ARTIFACT_NOT_VERIFIED' and any('CI artifact verified' in c for c in d.get('claims_allowed',[])): fail('overclaim ci artifact')
if sd.get('telemetry_mapping_status')=='LOCAL_SCHEMA_MAPPED_NOT_INTEGRATED' and not any('production telemetry' in c.lower() for c in d.get('claims_not_allowed',[])): fail('missing telemetry non-claim')
if sd.get('real_langgraph_status')=='NOT_AVAILABLE' and any('real langgraph runtime verified' in c.lower() for c in d.get('claims_allowed',[])): fail('overclaim real runtime')
if sd.get('graph_runtime_status')=='COMPATIBILITY_GRAPH_PASS' and sd.get('runtime_mode')!='DETERMINISTIC_GRAPH_COMPATIBILITY_MODE': fail('runtime mode mismatch')
if ('PARTIAL' in sd.get('sandboxed_tool_status','') or 'VERIFIED' in sd.get('sandboxed_tool_status','')):
    p=LAB/'graph-runtime-artifacts/graph-sandboxed-tool-results.json'
    if not p.exists(): fail('missing sandbox artifact')
    arr=json.loads(p.read_text())
    if any(x.get('external_side_effect') is not False for x in arr): fail('external side effect not false')
if ('PARTIAL' in sd.get('memory_boundary_status','') or 'VERIFIED' in sd.get('memory_boundary_status','')) and not (LAB/'graph-runtime-artifacts/graph-memory-boundary-log.json').exists(): fail('missing memory artifact')
if sd.get('incident_trace_status')=='RUNTIME_ARTIFACTS_PRESENT' and not (LAB/'graph-runtime-artifacts/graph-incident-timeline.json').exists(): fail('missing incident artifact')
if sd.get('telemetry_mapping_status') and not (LAB/'telemetry-field-map.json').exists(): fail('missing telemetry field map')
if sd.get('runtime_status')=='PASS':
    s=json.loads((LAB/'graph-runtime-artifacts/graph-runtime-summary.json').read_text())
    if s.get('total_cases')!=s.get('passed_cases'): fail('runtime pass but not all passed')
print('PASS: final-run-status.json consistency checks passed')
