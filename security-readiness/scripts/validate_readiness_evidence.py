#!/usr/bin/env python3
"""Canonical readiness metadata consistency validator.
PASS means metadata consistency only; it does NOT mean production readiness.
"""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
status_f = ROOT / 'security-readiness/meta/canonical-version-status.json'
launch_f = ROOT / 'security-readiness/launch-gates/canonical-launch-gate-decision.json'
manifest_f = ROOT / 'security-readiness/evidence-artifacts/canonical-evidence-manifest.json'
out_f = ROOT / 'security-readiness/evidence-artifacts/canonical-validation-result.json'

errors, warnings = [], []
checked = [str(status_f), str(launch_f), str(manifest_f)]

for f in [status_f, launch_f, manifest_f]:
    if not f.exists():
        errors.append(f"Missing required canonical file: {f}")

if not errors:
    status = json.loads(status_f.read_text())
    launch = json.loads(launch_f.read_text())
    manifest = json.loads(manifest_f.read_text())
    items = manifest.get('evidence_items', [])

    has_prod = any(i.get('category') == 'Production evidence' and i.get('status') in {'PASSED','PRESENT','PARTIAL'} and i.get('evidence_level') in {'PRODUCTION_RUNTIME','CLIENT_VERIFIED'} for i in items)
    has_client = any(i.get('category') == 'Client evidence' and i.get('status') in {'PASSED','PRESENT'} and i.get('evidence_level') == 'CLIENT_VERIFIED' for i in items)

    if status.get('production_ready') and not has_prod:
        errors.append('production_ready=true without production runtime evidence')
    if status.get('client_verified') and not has_client:
        errors.append('client_verified=true without client verified evidence')

    p0_blockers = launch.get('blocking_items', [])
    if p0_blockers and launch.get('decision') != 'NO_GO':
        errors.append('launch decision must be NO_GO when blockers exist')

    for i in items:
        lvl = i.get('evidence_level')
        cat = i.get('category','')
        if lvl == 'TEMPLATE_ONLY' and 'runtime' in cat.lower():
            errors.append(f"Template-only counted as runtime: {i.get('evidence_id')}")
        if lvl == 'DESIGN_ONLY' and i.get('status') in {'PASSED'}:
            errors.append(f"Design-only evidence marked PASSED: {i.get('evidence_id')}")

result = {
    'validation_status': 'FAIL' if errors else 'PASS',
    'validation_scope': 'metadata_consistency_only_not_production_readiness',
    'allow_go': False,
    'production_ready': False,
    'client_verified': False,
    'errors': errors,
    'warnings': warnings,
    'checked_files': checked,
    'timestamp_utc': datetime.now(timezone.utc).replace(microsecond=0).isoformat()
}
out_f.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
