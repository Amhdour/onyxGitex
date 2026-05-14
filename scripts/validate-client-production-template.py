#!/usr/bin/env python3
import json, sys
from pathlib import Path
E=Path('security-readiness/evidence-artifacts/version-4-client-production-template')
T=Path('client-production-template')
errs=[]
req_art=['version-4-client-production-template-status.json','client-production-template-evidence-summary.md','client-template-completeness-checks.json','client-required-evidence-matrix.json','client-launch-gate-template-result.json','client-claim-safety-scan.json','client-placeholder-field-index.json','client-approval-gate-model.json','client-residual-risk-model.json','client-production-template-manifest.json','validation-result.txt','blockers.md']
req_t=['README.md','client-production-template-plan.md','client-intake-template.md','client-ai-system-scope-template.md','client-system-inventory-template.md','client-data-classification-template.md','client-user-identity-model-template.md','client-tool-and-agent-inventory-template.md','client-rag-data-boundary-template.md','client-policy-and-approval-rules-template.md','client-compliance-constraints-template.md','client-risk-tolerance-template.md','client-logging-and-audit-requirements-template.md','client-incident-response-workflow-template.md','client-production-evidence-requirements-template.md','client-launch-gate-checklist-template.md','client-approver-signoff-template.md','client-residual-risk-register-template.md','client-go-no-go-decision-template.md','client-production-template-status.json','client-production-template-summary.md','blockers.md']
for n in req_art:
    if not (E/n).exists(): errs.append(f'missing {n}')
for n in req_t:
    if not (T/n).exists(): errs.append(f'missing template {n}')
def j(n):
    try:return json.loads((E/n).read_text())
    except Exception as ex: errs.append(f'bad json {n}: {ex}'); return {}
if not errs:
    s=j('version-4-client-production-template-status.json'); lg=j('client-launch-gate-template-result.json'); m=j('client-required-evidence-matrix.json'); p=j('client-placeholder-field-index.json'); a=j('client-approval-gate-model.json'); r=j('client-residual-risk-model.json'); c=j('client-claim-safety-scan.json'); mf=j('client-production-template-manifest.json')
    allowed={'TEMPLATE_ONLY','CLIENT_PRODUCTION_TEMPLATE_DEFINED','CLIENT_PRODUCTION_TEMPLATE_READY','CLIENT_EVIDENCE_PARTIAL','CLIENT_EVIDENCE_VERIFIED','CLIENT_CONDITIONAL_GO','CLIENT_GO','NOT_ENOUGH_EVIDENCE','NO_GO'}
    if s.get('version')!='4' or s.get('gate')!='CLIENT_SPECIFIC_PRODUCTION_TEMPLATE': errs.append('bad version/gate')
    if s.get('status') not in allowed: errs.append('bad status enum')
    for k in ['production_ready','go_decision','client_evidence_verified','client_runtime_verified','client_compliance_verified','client_approver_recorded']:
        if s.get(k) is not False: errs.append(f'{k} must be false')
    if s.get('status')=='CLIENT_PRODUCTION_TEMPLATE_READY':
        for k in ['template_files_verified','required_evidence_matrix_verified','launch_gate_template_verified','claim_safety_scan_passed','placeholder_index_verified','approval_gate_model_verified','residual_risk_model_verified']:
            if s.get(k) is not True: errs.append(f'{k} must be true')
    if lg.get('current_decision')!='NO_GO': errs.append('launch decision not NO_GO')
    if any(x.get('current_status')!='TEMPLATE_PLACEHOLDER_ONLY' for x in m.get('required_evidence_categories',[])): errs.append('matrix status not placeholder only')
    if p.get('placeholder_count')!=len(p.get('required_placeholders',[])): errs.append('placeholder_count mismatch')
    if a.get('client_approver_recorded') is not False: errs.append('approver recorded must be false')
    if r.get('risk_acceptance_recorded') is not False: errs.append('risk acceptance must be false')
    combined='\n'.join((E/n).read_text() for n in req_art if (E/n).exists())
    for bad in ['"production_ready": true','"go_decision": true','client_evidence_verified": true','client_approver_recorded": true']:
        if bad in combined: errs.append(f'forbidden claim {bad}')
    mset={Path(x.get('path','')).name for x in mf.get('required_artifacts',[])}
    for n in req_art:
        if n!='client-production-template-manifest.json' and n not in mset: errs.append(f'manifest missing {n}')
if errs:
    print('FAIL: ' + '; '.join(errs)); sys.exit(1)
print('PASS: client-production-template')
