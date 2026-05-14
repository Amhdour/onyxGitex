#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
req={"status":ROOT/'security-readiness/meta/canonical-version-status.json',"launch":ROOT/'security-readiness/launch-gates/canonical-launch-gate-decision.json',"p0_manifest":ROOT/'security-readiness/evidence-artifacts/p0-runtime-boundary-proof/manifest.json'}
out_f=ROOT/'security-readiness/evidence-artifacts/canonical-validation-result.json'
ALLOWED={"PASSED","FAILED_ASSERTION","FAILED_TEST_RUNTIME","BLOCKED_IMPORT_DEPENDENCY","BLOCKED_TEST_COLLECTION","BLOCKED_ENVIRONMENT","BLOCKED_COMMAND_MISSING","BLOCKED_TIMEOUT","BLOCKED_TEST_RUNTIME_TIMEOUT","NOT_EXECUTED"}
ALLOWED_EVIDENCE={"LOCAL_HARNESS","LOCAL_HARNESS_ASSERTION_FAILED","LOCAL_HARNESS_PARTIAL","LOCAL_RUNTIME","LOCAL_INTEGRATION","LOCAL_TEST_ASSERTION_FAILED","CI_RUNTIME","STAGING_RUNTIME","PRODUCTION_RUNTIME","BLOCKED_IMPORT_DEPENDENCY","BLOCKED_TEST_COLLECTION","BLOCKED_ENVIRONMENT","BLOCKED_NO_RUNTIME","BLOCKED_TIMEOUT"}
errors=[]
counts={k:0 for k in ['passed','failed_assertion','failed_test_runtime','blocked_import_dependency','blocked_test_collection','blocked_environment','blocked_command_missing','blocked_timeout','blocked_test_runtime_timeout','not_executed','assertions_reached','controls_local_harness_passed','controls_local_runtime_passed','controls_local_integration_passed']}
for f in req.values():
    if not f.exists(): errors.append(f'Missing required canonical file: {f}')
if not errors:
    status=json.loads(req['status'].read_text()); launch=json.loads(req['launch'].read_text()); m=json.loads(req['p0_manifest'].read_text())
    for c in m.get('controls',[]):
        p=ROOT/c['folder_path']/'evidence-result.json'
        if not p.exists(): errors.append(f'Missing evidence-result.json: {p}'); continue
        er=json.loads(p.read_text()); st=er.get('status'); ev=er.get('evidence_level')
        if st not in ALLOWED: errors.append(f'Invalid status {st} in {p}')
        if ev not in ALLOWED_EVIDENCE: errors.append(f'Invalid evidence_level {ev} in {p}')
        if er.get('assertions_reached') is True: counts['assertions_reached']+=1
        sm={'PASSED':'passed','FAILED_ASSERTION':'failed_assertion','FAILED_TEST_RUNTIME':'failed_test_runtime','BLOCKED_IMPORT_DEPENDENCY':'blocked_import_dependency','BLOCKED_TEST_COLLECTION':'blocked_test_collection','BLOCKED_ENVIRONMENT':'blocked_environment','BLOCKED_COMMAND_MISSING':'blocked_command_missing','BLOCKED_TIMEOUT':'blocked_timeout','BLOCKED_TEST_RUNTIME_TIMEOUT':'blocked_test_runtime_timeout','NOT_EXECUTED':'not_executed'}
        if st in sm: counts[sm[st]]+=1
        if st=='PASSED' and ev=='LOCAL_HARNESS': counts['controls_local_harness_passed']+=1
        if st=='PASSED' and ev=='LOCAL_RUNTIME': counts['controls_local_runtime_passed']+=1
        if st=='PASSED' and ev=='LOCAL_INTEGRATION': counts['controls_local_integration_passed']+=1
        if st in {'BLOCKED_TIMEOUT','BLOCKED_TEST_RUNTIME_TIMEOUT'}:
            if er.get('timed_out') is not True: errors.append(f'Timeout status requires timed_out=true in {p}')
            if er.get('assertions_reached') is not False: errors.append(f'Timeout status requires assertions_reached=false in {p}')
            if 'TEST_TIMEOUT' not in er.get('blockers',[]): errors.append(f'Timeout status requires TEST_TIMEOUT blocker in {p}')
        if st!='PASSED' and any(er.get(k) for k in ['supports_go_claim','supports_production_claim','supports_client_claim','supports_staging_claim']):
            errors.append(f'Non-passed control cannot support GO/production/client/staging claims in {p}')
    if counts['passed']<len(m.get('controls',[])) and launch.get('decision')!='NO_GO': errors.append('Launch decision must be NO_GO while any P0 control is not PASSED')
    if status.get('production_ready') or status.get('client_verified') or status.get('staging_verified'): errors.append('production/client/staging flags must remain false without higher-tier evidence')

res={"validation_status":"FAIL" if errors else "PASS","allow_go":False,"production_ready":False,"client_verified":False,"staging_verified":False,"p0_controls":{"total":7,**counts},"errors":errors,"warnings":[],"timestamp_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat()}
out_f.write_text(json.dumps(res,indent=2)+"\n")
print(json.dumps(res,indent=2))
