#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

S = Path('agent-security-readiness/23-langgraph-agent-lab/final-run-status.json')
LAB = S.parent


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


d = json.loads(S.read_text())
sd = d.get('status_dimensions', {})
required = ['runtime_status','graph_runtime_status','runtime_mode','real_langgraph_status','real_langgraph_attempt_status','compatibility_runtime_status','tool_authorization_status','human_approval_status','sandboxed_tool_status','memory_boundary_status','prompt_injection_status','fail_closed_status','audit_status','incident_trace_status','telemetry_mapping_status','ci_workflow_status','ci_artifact_status','evidence_status','launch_gate_status']
for key in required:
    if key not in sd:
        fail(f'missing status field {key}')

if sd['launch_gate_status'] == 'GO':
    fail('launch gate must not be GO')

ci_out = json.loads((LAB / 'ci-artifact-verification-output.json').read_text()) if (LAB / 'ci-artifact-verification-output.json').exists() else {}
if sd['ci_artifact_status'] == 'CI_ARTIFACT_VERIFIED' and ci_out.get('verification_status') != 'CI_ARTIFACT_VERIFIED':
    fail('ci artifact verified mismatch with local verifier output')
if sd['ci_artifact_status'] == 'CI_ARTIFACT_NOT_VERIFIED' and any('ci artifact' in c.lower() and 'verified' in c.lower() for c in d.get('claims_allowed', [])):
    fail('claims_allowed overclaims CI artifact proof')

real_out = json.loads((LAB / 'real-langgraph-attempt-output.json').read_text()) if (LAB / 'real-langgraph-attempt-output.json').exists() else {}
if sd['real_langgraph_status'] == 'PASS' and real_out.get('real_runtime_status') != 'REAL_LANGGRAPH_RUNTIME_PASS':
    fail('real langgraph pass without pass attempt evidence')
if sd['real_langgraph_status'] == 'NOT_AVAILABLE' and any('real langgraph runtime' in c.lower() and 'verified' in c.lower() for c in d.get('claims_allowed', [])):
    fail('claims_allowed overclaims real langgraph runtime')

if sd['evidence_status'] == 'PARTIAL_EVIDENCE' and sd['launch_gate_status'] not in {'NO_GO', 'CONDITIONAL_GO'}:
    fail('partial evidence requires NO_GO or CONDITIONAL_GO')

summary = json.loads((LAB / 'graph-runtime-artifacts/graph-runtime-summary.json').read_text())
if sd['runtime_status'] == 'PASS' and summary.get('total_cases') != summary.get('passed_cases'):
    fail('runtime pass requires total_cases == passed_cases')

sandbox = json.loads((LAB / 'graph-runtime-artifacts/graph-sandboxed-tool-results.json').read_text())
if any(item.get('external_side_effect') is not False for item in sandbox):
    fail('sandboxed tool result has external_side_effect != false')

if sd['telemetry_mapping_status'] == 'LOCAL_SCHEMA_MAPPED_NOT_INTEGRATED' and not (LAB / 'telemetry-field-map.json').exists():
    fail('telemetry-field-map.json missing for mapped status')

print('PASS: final-run-status.json consistency checks passed')
