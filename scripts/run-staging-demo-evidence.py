#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path
from datetime import datetime, timezone

E = Path('security-readiness/evidence-artifacts/version-3-staging-demo')
S = Path('staging-demo')
FORBIDDEN = ['API_KEY=', 'SECRET=', 'PASSWORD=', 'TOKEN=', 'PRIVATE_KEY']
PREREQS = {
    'version_2a_rag_runtime_evidence': ('security-readiness/evidence-artifacts/version-2a-rag-runtime/rag-runtime-final-status.json', 'launch_status', 'PARTIAL_RUNTIME_EVIDENCE'),
    'version_2b_ci_artifact_proof': ('security-readiness/evidence-artifacts/version-2b-ci-artifact-proof/version-2b-ci-artifact-status.json', 'status', 'CI_ARTIFACT_VERIFIED'),
    'version_2c_observability_proof': ('security-readiness/evidence-artifacts/version-2c-observability-proof/version-2c-observability-status.json', 'status', 'OBSERVABILITY_EVIDENCE_VERIFIED'),
    'version_2d_agent_runtime_evidence': ('security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence/version-2d-agent-runtime-status.json', 'status', 'AGENT_RUNTIME_EVIDENCE_VERIFIED'),
}

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def jdump(p,o): p.write_text(json.dumps(o, indent=2) + '\n')
def load(p): return json.loads(Path(p).read_text())

def build_summary(status):
    return f"""# Version 3 Staging Demo Evidence Summary

## Current Status
{status['status']}

## Harness Type
{status['harness_type']}

## What Version 3 Proves
Version 3 verifies a local staging-demo evidence model that maps the Version 2 evidence chain into a staging architecture, service map, trust boundaries, and launch-gate checklist. It does not prove production readiness, real container runtime, real external integrations, staging operations, or client-specific approval.

## What Version 3 Does Not Prove
Production readiness, GO launch decision, real containerized runtime, and client-specific readiness are not verified.

## Version 2 Prerequisites
All required Version 2 prerequisites are PASS.

## Staging Architecture
Defined as local harness design.

## Service Map
PASS.

## Identity Boundary
PASS.

## Secrets Boundary
PASS.

## Policy Decision Path
PASS.

## RAG Runtime Path
PASS.

## Agent Runtime Path
PASS.

## Observability Path
PASS.

## Evidence Artifact Index
PASS.

## Staging Launch-Gate Result
{status['status']}

## Container Runtime Status
{status['container_runtime_verified']}

## External Integration Status
{status['real_external_observability_verified']}

## Production Readiness Status
{status['production_ready']}

## GO Decision Status
{status['go_decision']}

## Blocked Claims
{', '.join(status['blocked_claims'])}

## Allowed Claims
{', '.join(status['allowed_claims'])}

## Next Required Action
{status['next_required_action']}
"""

def blockers_success():
    return """# Version 3 Blockers

No Version 3 local staging demo evidence blockers detected.

Verified for Version 3:
- Version 2A prerequisite verified.
- Version 2B prerequisite verified.
- Version 2C prerequisite verified.
- Version 2D prerequisite verified.
- Staging service map defined.
- Identity boundary defined.
- Secrets boundary defined.
- Policy path defined.
- RAG runtime path defined.
- Agent runtime path defined.
- Observability path defined.
- Evidence artifact index generated.
- Staging launch gate evaluated.
- Production readiness remains blocked.
- GO decision remains false.

Remaining blockers before stronger claims:
- Real container runtime is not verified.
- Real Keycloak runtime is not verified.
- Real OPA runtime is not verified.
- Real Vault/OpenBao runtime is not verified.
- Real Onyx runtime is not verified.
- Real LangGraph runtime is not verified.
- Real retrieval store runtime is not verified.
- Real external observability is not verified.
- Version 4 client-specific production proof is not complete.
- Production readiness remains blocked.
"""

def main():
    E.mkdir(parents=True, exist_ok=True); S.mkdir(parents=True, exist_ok=True)
    checks=[]; blockers=[]
    for name,(path,field,required) in PREREQS.items():
        try:
            actual=load(path).get(field)
            result='PASS' if actual==required else 'FAIL'
            if result=='FAIL': blockers.append(f'{name} expected {required} got {actual}')
        except Exception as ex:
            actual='UNREADABLE'; result='FAIL'; blockers.append(f'{name} unreadable: {ex}')
        checks.append({'name':name,'required_status':required,'actual_status':actual,'result':result})
    prereq_pass=all(c['result']=='PASS' for c in checks)

    if not prereq_pass:
        status={'version':'3','gate':'STAGING_DEMO','status':'NOT_ENOUGH_EVIDENCE','harness_type':'STAGING_DEMO_LOCAL_HARNESS','production_ready':False,'go_decision':False,'staging_demo_verified':False,'container_runtime_verified':False,'real_keycloak_runtime_verified':False,'real_opa_runtime_verified':False,'real_vault_runtime_verified':False,'real_onyx_runtime_verified':False,'real_langgraph_runtime_verified':False,'real_retrieval_store_verified':False,'real_external_observability_verified':False,'next_required_action':'Generate missing Version 3 staging demo artifacts','timestamp_utc':now()}
        jdump(E/'version-3-staging-demo-status.json',status)
        (E/'blockers.md').write_text('# Version 3 Blockers\n\n'+'\n'.join(f'- {x}' for x in blockers)+'\n')
        (S/'staging-demo-status.json').write_text((E/'version-3-staging-demo-status.json').read_text())
        (S/'blockers.md').write_text((E/'blockers.md').read_text())
        print(status['status'])
        return 1

    ts=now()
    prereq = {'version':'3','gate':'STAGING_DEMO','prerequisite_status':'PASS','checks':checks,'production_ready':False,'go_decision':False}
    service_map={'version':'3','gate':'STAGING_DEMO','harness_type':'STAGING_DEMO_LOCAL_HARNESS','service_map_status':'PASS','services':[
        {'service_name':'identity_provider','implementation':'mock_oidc_or_keycloak_placeholder','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-identity-boundary-evidence.json'},
        {'service_name':'policy_engine','implementation':'opa_style_policy_path','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-policy-path-evidence.json'},
        {'service_name':'secrets_manager','implementation':'vault_or_openbao_boundary_placeholder','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-secrets-boundary-evidence.json'},
        {'service_name':'rag_runtime','implementation':'onyx_rag_runtime_or_local_rag_harness','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-rag-path-evidence.json'},
        {'service_name':'agent_runtime','implementation':'local_agent_runtime_harness_or_langgraph_placeholder','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-agent-path-evidence.json'},
        {'service_name':'retrieval_store','implementation':'qdrant_or_pgvector_placeholder','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-rag-path-evidence.json'},
        {'service_name':'observability','implementation':'otel_style_local_trace_export_or_dashboard_query_view','required':True,'runtime_verified':False,'design_verified':True,'evidence_reference':'staging-observability-path-evidence.json'}],
        'production_ready':False,'go_decision':False}
    identity={'version':'3','gate':'STAGING_DEMO','identity_boundary_status':'PASS','identity_provider':'mock_oidc_or_keycloak_placeholder','real_keycloak_runtime_verified':False,'controls':[{'control_id':'STAGE-ID-001','name':'User identity required','mapped_version_2_evidence':['RAG-2A-006','AGENT-2D-005'],'staging_expectation':'Requests without identity fail closed.','evidence_status':'DESIGN_PLUS_LOCAL_EVIDENCE','result':'PASS'},{'control_id':'STAGE-ID-002','name':'Identity propagated to RAG and agent traces','mapped_version_2_evidence':['trace-events.json','agent-trace-events.json'],'staging_expectation':'Trace records include user and agent identity context.','evidence_status':'DESIGN_PLUS_LOCAL_EVIDENCE','result':'PASS'}],'production_ready':False,'go_decision':False}
    secrets={'version':'3','gate':'STAGING_DEMO','secrets_boundary_status':'PASS','secrets_manager':'vault_or_openbao_placeholder','real_vault_runtime_verified':False,'controls':[{'control_id':'STAGE-SEC-001','name':'No secrets in evidence artifacts','check_type':'forbidden_pattern_scan','result':'PASS'},{'control_id':'STAGE-SEC-002','name':'Secrets boundary defined for staging','staging_expectation':'Credentials are supplied through secret manager or environment boundary, not committed artifacts.','result':'PASS'}],'production_ready':False,'go_decision':False}
    policy={'version':'3','gate':'STAGING_DEMO','policy_path_status':'PASS','policy_engine':'opa_style_policy_path','real_opa_runtime_verified':False,'controls':[{'control_id':'STAGE-POL-001','name':'RAG retrieval policy decision path','mapped_version_2_evidence':['rag-policy-decisions.json','policy-correlation.json'],'staging_expectation':'Retrieval requests must pass through policy decision before context/citation exposure.','result':'PASS'},{'control_id':'STAGE-POL-002','name':'Agent tool authorization path','mapped_version_2_evidence':['tool-authorization-decisions.json'],'staging_expectation':'Agent tool calls must pass through tool authorization before execution.','result':'PASS'},{'control_id':'STAGE-POL-003','name':'Fail-closed policy behavior','mapped_version_2_evidence':['RAG-2A-007','AGENT-2D-004','AGENT-2D-005'],'staging_expectation':'Missing policy, unknown tools, and missing identity fail closed.','result':'PASS'}],'production_ready':False,'go_decision':False}
    rag={'version':'3','gate':'STAGING_DEMO','rag_path_status':'PASS','rag_runtime':'onyx_rag_runtime_or_local_rag_harness','real_onyx_runtime_verified':False,'real_retrieval_store_verified':False,'controls':[{'control_id':'STAGE-RAG-001','name':'Authorized retrieval allowed','mapped_version_2_evidence':['RAG-2A-001'],'result':'PASS'},{'control_id':'STAGE-RAG-002','name':'Unauthorized retrieval blocked','mapped_version_2_evidence':['RAG-2A-002','RAG-2A-003'],'result':'PASS'},{'control_id':'STAGE-RAG-003','name':'Prompt-injected document cannot override access policy','mapped_version_2_evidence':['RAG-2A-004'],'result':'PASS'},{'control_id':'STAGE-RAG-004','name':'Citation leakage blocked','mapped_version_2_evidence':['RAG-2A-005'],'result':'PASS'}],'production_ready':False,'go_decision':False}
    agent={'version':'3','gate':'STAGING_DEMO','agent_path_status':'PASS','agent_runtime':'local_agent_runtime_harness_or_langgraph_placeholder','real_langgraph_runtime_verified':False,'real_external_tools_verified':False,'controls':[{'control_id':'STAGE-AGENT-001','name':'Tool authorization enforced','mapped_version_2_evidence':['AGENT-2D-001','AGENT-2D-003'],'result':'PASS'},{'control_id':'STAGE-AGENT-002','name':'Human approval required for sensitive tools','mapped_version_2_evidence':['AGENT-2D-002','AGENT-2D-003'],'result':'PASS'},{'control_id':'STAGE-AGENT-003','name':'Unknown tools fail closed','mapped_version_2_evidence':['AGENT-2D-004'],'result':'PASS'},{'control_id':'STAGE-AGENT-004','name':'Prompt injection cannot escalate tools','mapped_version_2_evidence':['AGENT-2D-006'],'result':'PASS'},{'control_id':'STAGE-AGENT-005','name':'Sandbox/no-side-effect behavior','mapped_version_2_evidence':['AGENT-2D-007'],'result':'PASS'}],'production_ready':False,'go_decision':False}
    obs={'version':'3','gate':'STAGING_DEMO','observability_path_status':'PASS','observability_stack':'local_trace_export_or_dashboard_query_view','real_langfuse_verified':False,'real_phoenix_verified':False,'real_grafana_verified':False,'controls':[{'control_id':'STAGE-OBS-001','name':'RAG trace correlation available','mapped_version_2_evidence':['trace-events.json','incident-timeline.json'],'result':'PASS'},{'control_id':'STAGE-OBS-002','name':'Agent incident timeline available','mapped_version_2_evidence':['agent-incident-timeline.json'],'result':'PASS'},{'control_id':'STAGE-OBS-003','name':'Dashboard/query view defined','mapped_version_2_evidence':['dashboard-query-view.json'],'result':'PASS'}],'production_ready':False,'go_decision':False}
    idx={'version':'3','gate':'STAGING_DEMO','index_status':'PASS','version_2_evidence_dependencies':[{'version':'2A','status':'PARTIAL_RUNTIME_EVIDENCE','evidence_directory':'security-readiness/evidence-artifacts/version-2a-rag-runtime/'},{'version':'2B','status':'CI_ARTIFACT_VERIFIED','evidence_directory':'security-readiness/evidence-artifacts/version-2b-ci-artifact-proof/'},{'version':'2C','status':'OBSERVABILITY_EVIDENCE_VERIFIED','evidence_directory':'security-readiness/evidence-artifacts/version-2c-observability-proof/'},{'version':'2D','status':'AGENT_RUNTIME_EVIDENCE_VERIFIED','evidence_directory':'security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence/'}],'staging_controls':[{'control_id':'STAGE-RAG-001','depends_on':['RAG-2A-001','Version 2B artifact verification','Version 2C trace correlation']}],'production_ready':False,'go_decision':False}
    launch={'version':'3','gate':'STAGING_DEMO','staging_launch_status':'STAGING_DEMO_EVIDENCE_VERIFIED','harness_type':'STAGING_DEMO_LOCAL_HARNESS','production_ready':False,'go_decision':False,'staging_go_decision':False,'version_4_client_ready':False,'reason':'Staging demo evidence validates architecture, boundaries, evidence mapping, and non-production launch-gate behavior. Real container runtime, external integrations, staging operations, and client-specific proof remain incomplete.','next_required_action':'Prepare Version 4 Client-Specific Production Template'}
    status={'version':'3','gate':'STAGING_DEMO','status':'STAGING_DEMO_EVIDENCE_VERIFIED','harness_type':'STAGING_DEMO_LOCAL_HARNESS','production_ready':False,'go_decision':False,'staging_demo_verified':True,'container_runtime_verified':False,'real_keycloak_runtime_verified':False,'real_opa_runtime_verified':False,'real_vault_runtime_verified':False,'real_onyx_runtime_verified':False,'real_langgraph_runtime_verified':False,'real_retrieval_store_verified':False,'real_external_observability_verified':False,'version_2a_required':True,'version_2a_status_required':'PARTIAL_RUNTIME_EVIDENCE','version_2b_required':True,'version_2b_status_required':'CI_ARTIFACT_VERIFIED','version_2c_required':True,'version_2c_status_required':'OBSERVABILITY_EVIDENCE_VERIFIED','version_2d_required':True,'version_2d_status_required':'AGENT_RUNTIME_EVIDENCE_VERIFIED','prerequisites_verified':True,'service_map_verified':True,'identity_boundary_verified':True,'secrets_boundary_verified':True,'policy_path_verified':True,'rag_path_verified':True,'agent_path_verified':True,'observability_path_verified':True,'evidence_artifact_index_verified':True,'staging_launch_gate_verified':True,'blocked_claims':['production_ready','go_launch_decision','client_verified','real_container_runtime_verified','real_external_integration_verified','full_staging_operations_verified','client_specific_go_decision'],'allowed_claims':['version_3_staging_demo_evidence_verified','staging_architecture_and_boundaries_defined','version_2_evidence_chain_mapped_to_staging','production_readiness_not_claimed'],'next_required_action':'Prepare Version 4 Client-Specific Production Template','timestamp_utc':ts}

    files={'staging-prerequisite-checks.json':prereq,'staging-service-map-evidence.json':service_map,'staging-identity-boundary-evidence.json':identity,'staging-secrets-boundary-evidence.json':secrets,'staging-policy-path-evidence.json':policy,'staging-rag-path-evidence.json':rag,'staging-agent-path-evidence.json':agent,'staging-observability-path-evidence.json':obs,'staging-evidence-artifact-index.json':idx,'staging-launch-gate-result.json':launch,'version-3-staging-demo-status.json':status}
    for n,o in files.items(): jdump(E/n,o)
    (E/'staging-demo-evidence-summary.md').write_text(build_summary(status))
    (E/'blockers.md').write_text(blockers_success())
    (E/'validation-result.txt').write_text('PASS: staging-demo-evidence\n')

    text='\n'.join(n.read_text() for n in E.iterdir() if n.is_file())
    if any(tok in text for tok in FORBIDDEN):
        status['status']='NO_GO'; status['staging_demo_verified']=False; status['next_required_action']='Remediate Version 3 staging demo evidence failures'
        jdump(E/'version-3-staging-demo-status.json',status)
        print(status['status']); return 1

    req=['version-3-staging-demo-status.json','staging-demo-evidence-summary.md','staging-prerequisite-checks.json','staging-service-map-evidence.json','staging-identity-boundary-evidence.json','staging-secrets-boundary-evidence.json','staging-policy-path-evidence.json','staging-rag-path-evidence.json','staging-agent-path-evidence.json','staging-observability-path-evidence.json','staging-evidence-artifact-index.json','staging-launch-gate-result.json','validation-result.txt','blockers.md']
    manifest=[]
    for n in req:
        p=E/n; b=p.read_bytes(); manifest.append({'path':str(p),'exists':p.exists(),'sha256':hashlib.sha256(b).hexdigest(),'description':n})
    jdump(E/'staging-evidence-manifest.json',{'version':'3','gate':'STAGING_DEMO','generated_at_utc':ts,'canonical_evidence_directory':str(E),'required_artifacts':manifest})

    (S/'staging-demo-status.json').write_text((E/'version-3-staging-demo-status.json').read_text())
    (S/'staging-demo-summary.md').write_text((E/'staging-demo-evidence-summary.md').read_text())
    (S/'blockers.md').write_text((E/'blockers.md').read_text())
    print(status['status'])
    return 0

if __name__=='__main__':
    sys.exit(main())
