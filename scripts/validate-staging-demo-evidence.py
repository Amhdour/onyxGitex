#!/usr/bin/env python3
import json, sys
from pathlib import Path

E=Path('security-readiness/evidence-artifacts/version-3-staging-demo')
REQ=['version-3-staging-demo-status.json','staging-demo-evidence-summary.md','staging-prerequisite-checks.json','staging-service-map-evidence.json','staging-identity-boundary-evidence.json','staging-secrets-boundary-evidence.json','staging-policy-path-evidence.json','staging-rag-path-evidence.json','staging-agent-path-evidence.json','staging-observability-path-evidence.json','staging-evidence-artifact-index.json','staging-launch-gate-result.json','staging-evidence-manifest.json','validation-result.txt','blockers.md']
errs=[]
for n in REQ:
    if not (E/n).exists(): errs.append(f'missing {n}')

def j(n):
    try: return json.loads((E/n).read_text())
    except Exception as ex: errs.append(f'invalid json {n}: {ex}'); return {}

if not errs:
    s=j('version-3-staging-demo-status.json'); p=j('staging-prerequisite-checks.json'); sm=j('staging-service-map-evidence.json'); idn=j('staging-identity-boundary-evidence.json'); sec=j('staging-secrets-boundary-evidence.json'); pol=j('staging-policy-path-evidence.json'); rag=j('staging-rag-path-evidence.json'); ag=j('staging-agent-path-evidence.json'); ob=j('staging-observability-path-evidence.json'); idx=j('staging-evidence-artifact-index.json'); lg=j('staging-launch-gate-result.json'); mf=j('staging-evidence-manifest.json')
    allowed={'STAGING_DEMO_DEFINED','STAGING_DEMO_EVIDENCE_GENERATED','STAGING_DEMO_EVIDENCE_VERIFIED','STAGING_DEMO_CONTAINER_VERIFIED','NOT_ENOUGH_EVIDENCE','NO_GO'}
    if s.get('version')!='3' or s.get('gate')!='STAGING_DEMO': errs.append('bad status version/gate')
    if s.get('production_ready') is not False or s.get('go_decision') is not False: errs.append('status prod/go must be false')
    if s.get('status') not in allowed: errs.append('invalid status')
    if s.get('status')=='STAGING_DEMO_EVIDENCE_VERIFIED':
        for k,v in {'staging_demo_verified':True,'harness_type':'STAGING_DEMO_LOCAL_HARNESS','prerequisites_verified':True,'service_map_verified':True,'identity_boundary_verified':True,'secrets_boundary_verified':True,'policy_path_verified':True,'rag_path_verified':True,'agent_path_verified':True,'observability_path_verified':True,'evidence_artifact_index_verified':True,'staging_launch_gate_verified':True}.items():
            if s.get(k)!=v: errs.append(f'status {k} mismatch')
    if any(c.get('result')!='PASS' for c in p.get('checks',[])): errs.append('prereq checks not all pass')
    svcs={x.get('service_name') for x in sm.get('services',[])}
    need={'identity_provider','policy_engine','secrets_manager','rag_runtime','agent_runtime','retrieval_store','observability'}
    if not need.issubset(svcs): errs.append('service map missing required services')
    if idn.get('identity_boundary_status')!='PASS': errs.append('identity boundary not pass')
    if sec.get('secrets_boundary_status')!='PASS': errs.append('secrets boundary not pass')
    if pol.get('policy_path_status')!='PASS': errs.append('policy path not pass')
    if rag.get('rag_path_status')!='PASS': errs.append('rag path not pass')
    if ag.get('agent_path_status')!='PASS': errs.append('agent path not pass')
    if ob.get('observability_path_status')!='PASS': errs.append('obs path not pass')
    if idx.get('index_status')!='PASS': errs.append('index not pass')
    if lg.get('production_ready') is not False or lg.get('go_decision') is not False: errs.append('launch gate prod/go not false')
    combined='\n'.join((E/n).read_text() for n in REQ if (E/n).exists())
    for bad in ['"production_ready": true','"go_decision": true',' GO\n',' API_KEY=',' SECRET=',' PASSWORD=',' TOKEN=',' PRIVATE_KEY']:
        if bad in combined: errs.append(f'forbidden marker {bad.strip()}')
    if any(s.get(k) is True for k in ['container_runtime_verified','real_keycloak_runtime_verified','real_opa_runtime_verified','real_vault_runtime_verified','real_onyx_runtime_verified','real_langgraph_runtime_verified','real_retrieval_store_verified','real_external_observability_verified']): errs.append('real runtime flag true without evidence')
    mset={Path(x.get('path','')).name for x in mf.get('required_artifacts',[])}
    for n in [x for x in REQ if x!='staging-evidence-manifest.json']:
        if n not in mset: errs.append(f'manifest missing {n}')

if errs:
    print('FAIL: ' + '; '.join(errs)); sys.exit(1)
print('PASS: staging-demo-evidence')
