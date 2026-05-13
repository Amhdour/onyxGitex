#!/usr/bin/env python3
import json
from pathlib import Path
p=Path('security-readiness/evidence-artifacts/version-2a-rag-runtime/rag-runtime-final-status.json')
if not p.exists():
    print('status file not found')
    raise SystemExit(1)
s=json.loads(p.read_text())
for k in ['version','gate','harness_type','run_status','tests_total','tests_passed','tests_failed','launch_status','production_ready','go_decision','ci_verified','next_required_action']:
    print(f"{k}: {s.get(k)}")
