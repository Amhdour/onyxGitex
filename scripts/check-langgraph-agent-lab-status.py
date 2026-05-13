#!/usr/bin/env python3
from __future__ import annotations
import json,sys
from pathlib import Path
S=Path('agent-security-readiness/23-langgraph-agent-lab/final-run-status.json');LAB=S.parent

def fail(m): print(f'FAIL: {m}'); raise SystemExit(1)

d=json.loads(S.read_text()); sd=d.get('status_dimensions',{}); ap=set(d.get('artifacts_present',[]))
for k in ['graph_runtime_status','runtime_mode']: 
    if k not in sd: fail(f'missing status field {k}')
if sd.get('evidence_status')=='PARTIAL_EVIDENCE' and sd.get('launch_gate_status')=='GO': fail('PARTIAL_EVIDENCE cannot be GO')
if sd.get('runtime_mode')=='DETERMINISTIC_GRAPH_COMPATIBILITY_MODE':
    if 'Production LangGraph deployment is verified.' not in d.get('claims_not_allowed',[]): fail('missing production deployment non-claim')
req=['graph-runtime-summary.json','graph-runtime-trace.json','graph-policy-decision-log.json','graph-audit-events.json','graph-memory-boundary-log.json','graph-prompt-injection-log.json','graph-incident-timeline.json']
if any(f'graph-runtime-artifacts/{r}' in ap for r in req):
    for r in req:
        if not (LAB/'graph-runtime-artifacts'/r).exists(): fail(f'missing graph artifact file: {r}')
if sd.get('incident_trace_status')=='RUNTIME_ARTIFACTS_PRESENT' and not (LAB/'graph-runtime-artifacts/graph-incident-timeline.json').exists(): fail('incident trace file missing')
if 'PARTIAL' in sd.get('memory_boundary_status','') and not (LAB/'graph-runtime-artifacts/graph-memory-boundary-log.json').exists(): fail('memory log missing')
if 'PARTIAL' in sd.get('prompt_injection_status','') and not (LAB/'graph-runtime-artifacts/graph-prompt-injection-log.json').exists(): fail('prompt injection log missing')
print('PASS: final-run-status.json consistency checks passed')
