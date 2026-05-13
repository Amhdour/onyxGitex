#!/usr/bin/env python3
import json
import sys
from pathlib import Path

fp = Path('security-readiness/evidence-artifacts/runtime-rag-boundary/final-run-status.json')

data = json.loads(fp.read_text())
errors = []
required = [
    'schema_version','status_dimensions','primary_workflow','external_ci_signal','local_runtime','evidence_conclusion','launch_gate'
]
for k in required:
    if k not in data:
        errors.append(f"Missing required field: {k}")

sd = data.get('status_dimensions', {})
ci = sd.get('ci_workflow_status','')
local = sd.get('local_runtime_status','')
exts = sd.get('external_ci_signal_status','')
ev = sd.get('evidence_status','')
lg = sd.get('launch_gate_status','')

allowed_evidence = {'NOT_ENOUGH_EVIDENCE','EVIDENCE_COLLECTED_PASS','EVIDENCE_COLLECTED_FAIL','PARTIAL_EVIDENCE','STRUCTURE_ONLY','EXTERNAL_SIGNAL_ONLY'}
allowed_lg = {'NO_GO','CONDITIONAL_GO','GO','NOT_ENOUGH_EVIDENCE'}

if not ci.startswith('CI_'): errors.append('ci_workflow_status must start with CI_')
if local.startswith('CI_'): errors.append('local_runtime_status must not start with CI_')
if not exts.startswith('EXTERNAL_SIGNAL_'): errors.append('external_ci_signal_status must start with EXTERNAL_SIGNAL_')
if ev not in allowed_evidence: errors.append('evidence_status is not in allowed list')
if lg not in allowed_lg: errors.append('launch_gate_status is not in allowed list')

pw = data.get('primary_workflow',{})
if pw.get('artifact_verified') is False and ci == 'CI_ARTIFACT_VERIFIED':
    errors.append('artifact_verified false conflicts with CI_ARTIFACT_VERIFIED')
if pw.get('workflow_run_verified') is False and ci == 'CI_PASS':
    errors.append('workflow_run_verified false conflicts with CI_PASS')

ext = data.get('external_ci_signal',{})
if ext.get('classification') == 'EXTERNAL_SIGNAL_INSUFFICIENT' and ev == 'EVIDENCE_COLLECTED_PASS':
    errors.append('EXTERNAL_SIGNAL_INSUFFICIENT cannot support EVIDENCE_COLLECTED_PASS')

conc = data.get('evidence_conclusion',{})
if conc.get('runtime_verified') is False and lg == 'GO':
    errors.append('runtime_verified false cannot have GO launch_gate_status')

if errors:
    print('RAG boundary status consistency check: FAIL')
    for e in errors:
        print(f'- {e}')
    sys.exit(1)

print('RAG boundary status consistency check: PASS')
