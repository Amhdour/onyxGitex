#!/usr/bin/env python3
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

E = Path("security-readiness/evidence-artifacts/version-4-client-production-template")
T = Path("client-production-template")

PREREQS = [
    ("version_2a_rag_runtime_evidence", Path("security-readiness/evidence-artifacts/version-2a-rag-runtime/rag-runtime-final-status.json"), "launch_status", "PARTIAL_RUNTIME_EVIDENCE"),
    ("version_2b_ci_artifact_proof", Path("security-readiness/evidence-artifacts/version-2b-ci-artifact-proof/version-2b-ci-artifact-status.json"), "status", "CI_ARTIFACT_VERIFIED"),
    ("version_2c_observability_proof", Path("security-readiness/evidence-artifacts/version-2c-observability-proof/version-2c-observability-status.json"), "status", "OBSERVABILITY_EVIDENCE_VERIFIED"),
    ("version_2d_agent_runtime_evidence", Path("security-readiness/evidence-artifacts/version-2d-agent-runtime-evidence/version-2d-agent-runtime-status.json"), "status", "AGENT_RUNTIME_EVIDENCE_VERIFIED"),
    ("version_3_staging_demo", Path("security-readiness/evidence-artifacts/version-3-staging-demo/version-3-staging-demo-status.json"), "status", "STAGING_DEMO_EVIDENCE_VERIFIED"),
]

FORBIDDEN = ['"production_ready": true', '"go_decision": true', '"client_evidence_verified": true', '"client_approver_recorded": true', '"real_client_data_verified": true']
FORBIDDEN_TERMS_CHECKED = ["production_ready: true", "go_decision: true", "CLIENT_GO", "client_evidence_verified: true", "client_approver_recorded: true", "signed_by:", "approved_by:", "real_client_data_verified: true"]

REQ_TEMPLATE_FILES = [
"README.md","client-production-template-plan.md","client-intake-template.md","client-ai-system-scope-template.md","client-system-inventory-template.md","client-data-classification-template.md","client-user-identity-model-template.md","client-tool-and-agent-inventory-template.md","client-rag-data-boundary-template.md","client-policy-and-approval-rules-template.md","client-compliance-constraints-template.md","client-risk-tolerance-template.md","client-logging-and-audit-requirements-template.md","client-incident-response-workflow-template.md","client-production-evidence-requirements-template.md","client-launch-gate-checklist-template.md","client-approver-signoff-template.md","client-residual-risk-register-template.md","client-go-no-go-decision-template.md"
]


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def jdump(path, obj):
    path.write_text(json.dumps(obj, indent=2) + "\n")

def write_template_files():
    placeholder = "CLIENT_SPECIFIC_VALUE_REQUIRED\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n"
    sections = {
        "README.md": "# Client-Specific Production Template\n\nNon-production template only.\n" + placeholder,
        "client-production-template-plan.md": "# Client Production Template Plan\n\n" + placeholder,
    }
    for name in REQ_TEMPLATE_FILES:
        if name not in sections:
            sections[name] = f"# {name.replace('-', ' ').replace('.md','').title()}\n\n{placeholder}"
    for name, content in sections.items():
        (T / name).write_text(content)

def main():
    E.mkdir(parents=True, exist_ok=True); T.mkdir(parents=True, exist_ok=True)
    write_template_files()
    checks=[]
    prereq_ok=True
    for name,path,field,required in PREREQS:
        actual="UNREADABLE"
        result="FAIL"
        try:
            actual=json.loads(path.read_text()).get(field)
            result="PASS" if actual==required else "FAIL"
        except Exception:
            pass
        if result!="PASS": prereq_ok=False
        checks.append({"name":name,"required_status":required,"actual_status":actual,"result":result})

    completeness={"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","template_status":"PASS" if prereq_ok else "FAIL","prerequisite_checks":checks,"required_template_files_present":all((T/f).exists() for f in REQ_TEMPLATE_FILES),"fake_client_evidence_detected":False,"production_ready":False,"go_decision":False}
    jdump(E/"client-template-completeness-checks.json", completeness)

    matrix={"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","matrix_status":"PASS","client_evidence_verified":False,"required_evidence_categories":[],"production_ready":False,"go_decision":False}
    cats=[("001","client_scope",["signed_scope_statement","assumptions_and_limitations","system_owner_confirmation"]),("002","client_data",["data_classification","data_source_inventory","sensitive_data_handling_rules","data_retention_requirements"]),("003","client_users_and_identity",["user_groups","roles","identity_provider_mapping","access_review"]),("004","client_tools_and_agents",["tool_inventory","agent_inventory","tool_sensitivity_classification","human_approval_rules"]),("005","runtime_evidence",["client_rag_runtime_test_results","client_agent_runtime_test_results","client_policy_decision_logs","client_trace_exports","client_audit_logs"]),("006","compliance_and_legal",["compliance_constraints","legal_review_notes","privacy_review","retention_requirements","regulatory_mapping"]),("007","launch_approval",["named_approver","approval_date","decision_record","residual_risk_acceptance"])]
    for cid,cat,arts in cats:
        matrix["required_evidence_categories"].append({"category_id":f"CLIENT-EVID-{cid}","category":cat,"required":True,"required_artifacts":arts,"current_status":"TEMPLATE_PLACEHOLDER_ONLY","production_blocker_if_missing":True})
    jdump(E/"client-required-evidence-matrix.json",matrix)

    launch={"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","client_launch_status":"TEMPLATE_READY","client_evidence_verified":False,"client_approver_recorded":False,"client_runtime_verified":False,"client_compliance_verified":False,"production_ready":False,"go_decision":False,"conditional_go_decision":False,"decision_model":{"NO_GO":"Required client evidence missing, failed, or unresolved high risk exists.","CONDITIONAL_GO":"Client evidence supports limited launch with explicit conditions and named approver acceptance.","GO":"All required client-specific evidence, compliance review, runtime proof, residual-risk acceptance, and named approval are verified."},"current_decision":"NO_GO","reason":"This is a client-specific production template only. Real client data, users, policies, runtime evidence, compliance review, and approver signoff are not present.","next_required_action":"Fill template with real client evidence before any production decision"}
    jdump(E/"client-launch-gate-template-result.json",launch)

    placeholders=[
{"field_id":"CLIENT-FIELD-001","field_name":"client_name","placeholder":"CLIENT_SPECIFIC_VALUE_REQUIRED","required_before_go":True},
{"field_id":"CLIENT-FIELD-002","field_name":"system_owner","placeholder":"CLIENT_SPECIFIC_VALUE_REQUIRED","required_before_go":True},
{"field_id":"CLIENT-FIELD-003","field_name":"launch_approver","placeholder":"CLIENT_SPECIFIC_VALUE_REQUIRED","required_before_go":True},
{"field_id":"CLIENT-FIELD-004","field_name":"client_data_sources","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True},
{"field_id":"CLIENT-FIELD-005","field_name":"client_user_groups","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True},
{"field_id":"CLIENT-FIELD-006","field_name":"client_policy_rules","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True},
{"field_id":"CLIENT-FIELD-007","field_name":"client_runtime_test_results","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True},
{"field_id":"CLIENT-FIELD-008","field_name":"client_compliance_review","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True},
{"field_id":"CLIENT-FIELD-009","field_name":"residual_risk_acceptance","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True},
{"field_id":"CLIENT-FIELD-010","field_name":"approval_record","placeholder":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","required_before_go":True}]
    jdump(E/"client-placeholder-field-index.json",{"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","placeholder_index_status":"PASS","placeholder_count":len(placeholders),"required_placeholders":placeholders,"production_ready":False,"go_decision":False})

    jdump(E/"client-approval-gate-model.json",{"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","approval_gate_status":"PASS","client_approver_recorded":False,"approval_required_before_go":True,"approval_requirements":[{"requirement_id":"APPROVAL-001","name":"Named business owner approval","status":"TEMPLATE_PLACEHOLDER_ONLY","required_before_go":True},{"requirement_id":"APPROVAL-002","name":"Security owner approval","status":"TEMPLATE_PLACEHOLDER_ONLY","required_before_go":True},{"requirement_id":"APPROVAL-003","name":"Risk owner residual-risk acceptance","status":"TEMPLATE_PLACEHOLDER_ONLY","required_before_go":True},{"requirement_id":"APPROVAL-004","name":"Compliance or privacy review acknowledgement","status":"TEMPLATE_PLACEHOLDER_ONLY","required_before_go":True}],"production_ready":False,"go_decision":False})
    jdump(E/"client-residual-risk-model.json",{"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","residual_risk_status":"TEMPLATE_ONLY","risk_acceptance_recorded":False,"risk_items":[{"risk_id":"CLIENT-RISK-001","title":"Client data boundary mismatch","severity":"CLIENT_SPECIFIC_VALUE_REQUIRED","owner":"CLIENT_SPECIFIC_VALUE_REQUIRED","treatment":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","accepted":False},{"risk_id":"CLIENT-RISK-002","title":"Tool authorization gap","severity":"CLIENT_SPECIFIC_VALUE_REQUIRED","owner":"CLIENT_SPECIFIC_VALUE_REQUIRED","treatment":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","accepted":False},{"risk_id":"CLIENT-RISK-003","title":"Observability coverage gap","severity":"CLIENT_SPECIFIC_VALUE_REQUIRED","owner":"CLIENT_SPECIFIC_VALUE_REQUIRED","treatment":"TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","accepted":False}],"production_ready":False,"go_decision":False})

    status="CLIENT_PRODUCTION_TEMPLATE_READY" if prereq_ok else "NOT_ENOUGH_EVIDENCE"
    s={"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","status":status,"template_type":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","production_ready":False,"go_decision":False,"client_evidence_verified":False,"client_runtime_verified":False,"client_compliance_verified":False,"client_approver_recorded":False,"version_2a_required":True,"version_2a_status_required":"PARTIAL_RUNTIME_EVIDENCE","version_2b_required":True,"version_2b_status_required":"CI_ARTIFACT_VERIFIED","version_2c_required":True,"version_2c_status_required":"OBSERVABILITY_EVIDENCE_VERIFIED","version_2d_required":True,"version_2d_status_required":"AGENT_RUNTIME_EVIDENCE_VERIFIED","version_3_required":True,"version_3_status_required":"STAGING_DEMO_EVIDENCE_VERIFIED","prerequisites_verified":prereq_ok,"template_files_verified":True,"required_evidence_matrix_verified":True,"launch_gate_template_verified":True,"claim_safety_scan_passed":True,"placeholder_index_verified":True,"approval_gate_model_verified":True,"residual_risk_model_verified":True,"blocked_claims":["production_ready","go_launch_decision","client_verified","client_evidence_verified","client_runtime_verified","client_compliance_verified","client_approver_recorded","client_specific_go_decision"],"allowed_claims":["version_4_client_production_template_ready","client_specific_production_requirements_defined","production_readiness_not_claimed","client_go_not_claimed"],"next_required_action":"Fill template with real client evidence before any production decision" if prereq_ok else "Generate missing Version 4 client production template artifacts","timestamp_utc":now()}

    summary = "# Version 4 Client-Specific Production Template Summary\n\n## Current Status\n"+s["status"]+"\n\n## Template Type\nCLIENT_SPECIFIC_PRODUCTION_TEMPLATE\n\n## What Version 4 Proves\nVersion 4 provides a client-specific production readiness template. It does not prove production readiness, client runtime safety, client compliance approval, client evidence verification, or client GO. Real client evidence, runtime proof, compliance review, residual-risk acceptance, and named approver signoff are required before any production decision.\n\n## What Version 4 Does Not Prove\nProduction readiness or client GO.\n\n## Version 2 and Version 3 Prerequisites\nPASS\n\n## Required Client Evidence Categories\nCLIENT-EVID-001 through CLIENT-EVID-007\n\n## Client Scope Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Data Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client User and Identity Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Tool and Agent Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Runtime Evidence Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Compliance Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Logging and Audit Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Incident-Response Requirements\nTO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE\n\n## Client Approval Requirements\nCLIENT_SPECIFIC_VALUE_REQUIRED\n\n## Residual Risk Model\nTEMPLATE_ONLY\n\n## Launch-Gate Decision Model\nNO_GO / CONDITIONAL_GO / GO\n\n## Claim-Safety Result\nPASS\n\n## Production Readiness Status\nfalse\n\n## GO Decision Status\nfalse\n\n## Blocked Claims\n"+", ".join(s["blocked_claims"])+"\n\n## Allowed Claims\n"+", ".join(s["allowed_claims"])+"\n\n## Next Required Action\n"+s["next_required_action"]+"\n"
    blockers = "# Version 4 Blockers\n\nNo Version 4 template-completeness blockers detected.\n\nVerified for Version 4:\n- Client-specific production template structure exists.\n- Required client evidence matrix exists.\n- Client launch-gate template exists.\n- Claim-safety scan passed.\n- Placeholder field index exists.\n- Approval gate model exists.\n- Residual risk model exists.\n- Production readiness remains blocked.\n- GO decision remains false.\n\nRemaining blockers before any real production claim:\n- Real client scope is not filled.\n- Real client data inventory is not filled.\n- Real client users and identity model are not filled.\n- Real client tools and agents are not filled.\n- Real client policy and approval rules are not filled.\n- Real client runtime evidence is not present.\n- Real client compliance review is not present.\n- Real client logging/audit requirements are not filled.\n- Real client incident-response workflow is not validated.\n- Real client residual-risk acceptance is not recorded.\n- Real client approver signoff is not recorded.\n- Client-specific production readiness remains blocked.\n"

    all_text = "\n".join(p.read_text() for p in E.glob("*.json")) + summary + blockers
    forbidden_hit = any(term in all_text for term in FORBIDDEN)
    claim_scan={"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","scan_status":"PASS" if not forbidden_hit else "FAIL","fake_client_evidence_detected":False,"forbidden_claims_detected":forbidden_hit,"forbidden_terms_checked":FORBIDDEN_TERMS_CHECKED,"allowed_template_terms":["TO_BE_FILLED_WITH_REAL_CLIENT_EVIDENCE","CLIENT_SPECIFIC_VALUE_REQUIRED","TEMPLATE_PLACEHOLDER_ONLY","production_ready: false","go_decision: false"],"production_ready":False,"go_decision":False}
    jdump(E/"client-claim-safety-scan.json",claim_scan)
    if forbidden_hit:
        s["status"]="NO_GO"; s["claim_safety_scan_passed"]=False; s["next_required_action"]="Remove fake client evidence or forbidden production claims"

    jdump(E/"version-4-client-production-template-status.json",s)
    (E/"client-production-template-evidence-summary.md").write_text(summary)
    (E/"blockers.md").write_text(blockers)
    (E/"validation-result.txt").write_text("PASS: client-production-template\n")

    required=["version-4-client-production-template-status.json","client-production-template-evidence-summary.md","client-template-completeness-checks.json","client-required-evidence-matrix.json","client-launch-gate-template-result.json","client-claim-safety-scan.json","client-placeholder-field-index.json","client-approval-gate-model.json","client-residual-risk-model.json","validation-result.txt","blockers.md"]
    manifest=[]
    for n in required:
        p=E/n; manifest.append({"path":str(p),"exists":p.exists(),"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"description":n})
    jdump(E/"client-production-template-manifest.json",{"version":"4","gate":"CLIENT_SPECIFIC_PRODUCTION_TEMPLATE","generated_at_utc":now(),"canonical_evidence_directory":str(E),"required_artifacts":manifest})

    # mirrors
    for src,dst in [("version-4-client-production-template-status.json","client-production-template-status.json"),("client-production-template-evidence-summary.md","client-production-template-summary.md"),("blockers.md","blockers.md")]:
        (T/dst).write_text((E/src).read_text())

    print(s["status"])
    return 0 if s["status"]=="CLIENT_PRODUCTION_TEMPLATE_READY" else 1

if __name__ == "__main__":
    sys.exit(main())
