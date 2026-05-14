#!/usr/bin/env python3
import json
from pathlib import Path
p=Path('security-readiness/evidence-artifacts/version-4-client-production-template/version-4-client-production-template-status.json')
s=json.loads(p.read_text())
for k in ['version','gate','status','template_type','production_ready','go_decision','client_evidence_verified','client_runtime_verified','client_compliance_verified','client_approver_recorded','prerequisites_verified','template_files_verified','required_evidence_matrix_verified','launch_gate_template_verified','claim_safety_scan_passed','placeholder_index_verified','approval_gate_model_verified','residual_risk_model_verified','next_required_action']:
    print(f'{k}: {s.get(k)}')
