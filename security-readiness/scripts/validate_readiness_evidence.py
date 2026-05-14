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
errors=[]; warnings=[]; checked=[str(v) for v in req.values()]
for f in req.values():
    if not f.exists(): errors.append(f"Missing required canonical file: {f}")

def exists_or_waived(path, item):
    status=item.get('status','')
    if status in {'MISSING','TO_BE_CREATED'}: return True
    return (ROOT / path).exists()

checked_controls=[]; p0_passed=0; p0_not=0
if not errors:
    status=json.loads(req['status'].read_text())
    launch=json.loads(req['launch'].read_text())
    manifest=json.loads(req['manifest'].read_text())
    p0_manifest=json.loads(req['p0_manifest'].read_text())
    p0_final=json.loads(req['p0_final'].read_text())

    for it in manifest.get('evidence_items',[]):
        fp=it.get('file_path','')
        if fp and not exists_or_waived(fp,it): errors.append(f"Evidence path missing: {fp} ({it.get('evidence_id')})")

    for c in p0_manifest.get('controls',[]):
        checked_controls.append(c.get('control_id'))
        folder=ROOT / c.get('folder_path','')
        if not folder.exists(): errors.append(f"Missing P0 folder: {folder}")
        for rf in c.get('required_files',[]):
            if not (folder/rf).exists(): errors.append(f"Missing required P0 file: {folder/rf}")
        erp=folder/'evidence-result.json'
        if erp.exists():
            er=json.loads(erp.read_text())
            for k in ['control_id','control_name','status','evidence_level','test_executed','supports_go_claim','supports_production_claim','supports_client_claim','limitations','next_required_action']:
                if k not in er: errors.append(f"{erp} missing field: {k}")
            if er.get('status')=='PASSED': p0_passed+=1
            if er.get('status')=='NOT_EXECUTED': p0_not+=1
            if er.get('supports_go_claim'):
                good_level=er.get('evidence_level') in {'LOCAL_RUNTIME','CI_RUNTIME','STAGING_RUNTIME','PRODUCTION_RUNTIME','CLIENT_VERIFIED'}
                rlp=ROOT/er.get('runtime_log_path','missing')
                pop=ROOT/er.get('pytest_output_path','missing')
                if not (er.get('status')=='PASSED' and er.get('test_executed') is True and good_level and rlp.exists() and pop.exists()):
                    errors.append(f"Invalid GO-supporting claim in {erp}")
            if er.get('evidence_level') in {'DESIGN_ONLY','TEMPLATE_ONLY','STATIC_REVIEW','P0_PROOF_STRUCTURE_ONLY'} and (er.get('supports_go_claim') or er.get('supports_production_claim') or er.get('supports_client_claim')):
                errors.append(f"Invalid claim support for low evidence level in {erp}")
        for ph in ['runtime-log.placeholder.txt','pytest-output.placeholder.txt']:
            phf=folder/ph
            if phf.exists() and 'PLACEHOLDER_ONLY' not in phf.read_text():
                errors.append(f"Placeholder marker missing in {phf}")

    if status.get('production_ready'): errors.append('production_ready=true without production evidence is not allowed')
    if status.get('client_verified'): errors.append('client_verified=true without client evidence is not allowed')
    if status.get('versions',{}).get('v3_staging_demo',{}).get('status') in {'VERIFIED','PASSED'}:
        errors.append('staging_verified style claim without deployed evidence is not allowed')
    total=len(p0_manifest.get('controls',[]))
    if p0_passed<total and launch.get('decision')!='NO_GO': errors.append('Launch decision must remain NO_GO while any P0 control is not PASSED')

result={
"validation_status":"FAIL" if errors else "PASS",
"validation_scope":"metadata_and_artifact_consistency_only_not_runtime_or_production_readiness",
"allow_go":False,
"production_ready":False,
"client_verified":False,
"staging_verified":False,
"p0_controls":{"total":7,"passed":p0_passed,"not_executed":p0_not},
"errors":errors,
"warnings":warnings,
"checked_files":checked,
"checked_p0_controls":checked_controls,
"timestamp_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat()
}
out_f.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
