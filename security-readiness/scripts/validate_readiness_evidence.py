#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
req = {
"status": ROOT / 'security-readiness/meta/canonical-version-status.json',
"launch": ROOT / 'security-readiness/launch-gates/canonical-launch-gate-decision.json',
"manifest": ROOT / 'security-readiness/evidence-artifacts/canonical-evidence-manifest.json',
"p0_manifest": ROOT / 'security-readiness/evidence-artifacts/p0-runtime-boundary-proof/manifest.json',
"p0_final": ROOT / 'security-readiness/evidence-artifacts/p0-runtime-boundary-proof/final-status.json',
}
out_f = ROOT / 'security-readiness/evidence-artifacts/canonical-validation-result.json'
ALLOWED={"PASSED","FAILED_ASSERTION","FAILED_TEST_RUNTIME","BLOCKED_IMPORT_DEPENDENCY","BLOCKED_TEST_COLLECTION","BLOCKED_ENVIRONMENT","BLOCKED_COMMAND_MISSING","NOT_EXECUTED"}
BLOCKED={"BLOCKED_IMPORT_DEPENDENCY","BLOCKED_TEST_COLLECTION","BLOCKED_ENVIRONMENT","BLOCKED_COMMAND_MISSING","NOT_EXECUTED"}
errors=[]; warnings=[]; checked=[str(v) for v in req.values()]
for f in req.values():
    if not f.exists(): errors.append(f"Missing required canonical file: {f}")

counts={k:0 for k in ["passed","failed_assertion","failed_test_runtime","blocked_import_dependency","blocked_test_collection","blocked_environment","blocked_command_missing","not_executed","assertions_reached"]}
checked_controls=[]
if not errors:
    status=json.loads(req['status'].read_text())
    launch=json.loads(req['launch'].read_text())
    p0_manifest=json.loads(req['p0_manifest'].read_text())

    for c in p0_manifest.get('controls',[]):
        checked_controls.append(c.get('control_id'))
        erp=ROOT / c.get('folder_path','') / 'evidence-result.json'
        if not erp.exists():
            errors.append(f"Missing evidence-result.json: {erp}")
            continue
        er=json.loads(erp.read_text())
        required=['assertions_reached','failure_classification','root_cause_summary','dependency_blockers','environment_blockers','test_collection_blockers','recommended_fix','supports_local_harness_claim','supports_staging_claim','status','exit_code']
        for k in required:
            if k not in er: errors.append(f"{erp} missing field: {k}")
        st=er.get('status')
        if st not in ALLOWED: errors.append(f"Invalid status {st} in {erp}")
        if st=="PASSED":
            counts['passed']+=1
            if er.get('assertions_reached') is not True or er.get('exit_code')!=0: errors.append(f"PASSED must have assertions_reached=true and exit_code=0 in {erp}")
        if st=="FAILED_ASSERTION":
            counts['failed_assertion']+=1
            if er.get('assertions_reached') is not True: errors.append(f"FAILED_ASSERTION must have assertions_reached=true in {erp}")
        if st=="FAILED_TEST_RUNTIME": counts['failed_test_runtime']+=1
        if st=="BLOCKED_IMPORT_DEPENDENCY":
            counts['blocked_import_dependency']+=1
            if er.get('assertions_reached') is not False: errors.append(f"BLOCKED_IMPORT_DEPENDENCY must have assertions_reached=false in {erp}")
            if not er.get('dependency_blockers'): errors.append(f"BLOCKED_IMPORT_DEPENDENCY must include dependency_blockers in {erp}")
        if st=="BLOCKED_TEST_COLLECTION": counts['blocked_test_collection']+=1
        if st=="BLOCKED_ENVIRONMENT": counts['blocked_environment']+=1
        if st=="BLOCKED_COMMAND_MISSING": counts['blocked_command_missing']+=1
        if st=="NOT_EXECUTED": counts['not_executed']+=1
        if er.get('assertions_reached') is True: counts['assertions_reached']+=1
        if st in BLOCKED:
            if er.get('supports_local_runtime_claim') or er.get('supports_go_claim') or er.get('supports_production_claim') or er.get('supports_client_claim') or er.get('supports_staging_claim'):
                errors.append(f"Blocked status cannot support runtime/GO/production/client/staging claims in {erp}")

    total=len(p0_manifest.get('controls',[]))
    if counts['passed']<total and launch.get('decision')!='NO_GO': errors.append('Launch decision must remain NO_GO while any P0 control is not PASSED')
    if status.get('production_ready'): errors.append('production_ready=true without production evidence is not allowed')
    if status.get('client_verified'): errors.append('client_verified=true without client evidence is not allowed')
    if status.get('staging_verified'): errors.append('staging_verified=true without staging evidence is not allowed')

result={
"validation_status":"FAIL" if errors else "PASS",
"validation_scope":"metadata_and_artifact_consistency_only_not_runtime_or_production_readiness",
"allow_go":False,
"production_ready":False,
"client_verified":False,
"staging_verified":False,
"p0_controls":{"total":7, **counts},
"errors":errors,
"warnings":warnings,
"checked_files":checked,
"checked_p0_controls":checked_controls,
"timestamp_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat()
}
out_f.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
