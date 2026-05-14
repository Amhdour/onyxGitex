import json
import subprocess
from pathlib import Path

E=Path('security-readiness/evidence-artifacts/version-3-staging-demo')
REQ=['version-3-staging-demo-status.json','staging-demo-evidence-summary.md','staging-prerequisite-checks.json','staging-service-map-evidence.json','staging-identity-boundary-evidence.json','staging-secrets-boundary-evidence.json','staging-policy-path-evidence.json','staging-rag-path-evidence.json','staging-agent-path-evidence.json','staging-observability-path-evidence.json','staging-evidence-artifact-index.json','staging-launch-gate-result.json','staging-evidence-manifest.json','validation-result.txt','blockers.md']


def test_staging_demo_evidence_end_to_end():
    subprocess.run(['python','scripts/run-staging-demo-evidence.py'], check=True)
    for n in REQ:
        assert (E/n).exists(), n
    subprocess.run(['python','scripts/validate-staging-demo-evidence.py'], check=True)

    status=json.loads((E/'version-3-staging-demo-status.json').read_text())
    prereq=json.loads((E/'staging-prerequisite-checks.json').read_text())
    sm=json.loads((E/'staging-service-map-evidence.json').read_text())
    assert status['status']=='STAGING_DEMO_EVIDENCE_VERIFIED'
    assert all(x['result']=='PASS' for x in prereq['checks'])
    assert {x['service_name'] for x in sm['services']} >= {'identity_provider','policy_engine','secrets_manager','rag_runtime','agent_runtime','retrieval_store','observability'}
    for jf,key in [('staging-identity-boundary-evidence.json','identity_boundary_status'),('staging-secrets-boundary-evidence.json','secrets_boundary_status'),('staging-policy-path-evidence.json','policy_path_status'),('staging-rag-path-evidence.json','rag_path_status'),('staging-agent-path-evidence.json','agent_path_status'),('staging-observability-path-evidence.json','observability_path_status')]:
        assert json.loads((E/jf).read_text())[key]=='PASS'
    launch=json.loads((E/'staging-launch-gate-result.json').read_text())
    assert launch['production_ready'] is False and launch['go_decision'] is False and launch['staging_go_decision'] is False
    assert status['production_ready'] is False and status['go_decision'] is False
    for k in ['container_runtime_verified','real_keycloak_runtime_verified','real_opa_runtime_verified','real_vault_runtime_verified','real_onyx_runtime_verified','real_langgraph_runtime_verified','real_retrieval_store_verified','real_external_observability_verified']:
        assert status[k] is False
    combined='\n'.join((E/n).read_text() for n in REQ)
    for token in ['API_KEY=','SECRET=','PASSWORD=','TOKEN=','PRIVATE_KEY']:
        assert token not in combined
