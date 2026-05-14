import json, subprocess
from pathlib import Path

E=Path('security-readiness/evidence-artifacts/version-4-client-production-template')


def test_client_template_flow():
    run=subprocess.run(['python','scripts/run-client-production-template.py'],capture_output=True,text=True)
    assert run.returncode==0, run.stdout+run.stderr
    for cmd in [
        ['python','scripts/validate-client-production-template.py'],
    ]:
        r=subprocess.run(cmd,capture_output=True,text=True)
        assert r.returncode==0, r.stdout+r.stderr

    status=json.loads((E/'version-4-client-production-template-status.json').read_text())
    assert status['status']=='CLIENT_PRODUCTION_TEMPLATE_READY'
    for k in ['production_ready','go_decision','client_evidence_verified','client_runtime_verified','client_compliance_verified','client_approver_recorded']:
        assert status[k] is False
    launch=json.loads((E/'client-launch-gate-template-result.json').read_text())
    assert launch['current_decision']=='NO_GO'
    matrix=json.loads((E/'client-required-evidence-matrix.json').read_text())
    assert all(x['current_status']=='TEMPLATE_PLACEHOLDER_ONLY' for x in matrix['required_evidence_categories'])
    ph=json.loads((E/'client-placeholder-field-index.json').read_text())
    assert ph['placeholder_count']>=10
    scan=json.loads((E/'client-claim-safety-scan.json').read_text())
    assert scan['fake_client_evidence_detected'] is False
    assert scan['forbidden_claims_detected'] is False
