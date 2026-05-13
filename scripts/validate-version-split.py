#!/usr/bin/env python3
import json
from pathlib import Path
required=["VERSION_STATUS.md","portfolio-lab/README.md","production-readiness/README.md","staging-demo/README.md","client-production-template/README.md","archive/README.md","production-readiness/00-status/canonical-readiness-status.json","staging-demo/09-launch-gate/staging-launch-gate-result.json"]
missing=[p for p in required if not Path(p).exists()]
bad=[]
for p in ["production-readiness/00-status/canonical-readiness-status.json","staging-demo/09-launch-gate/staging-launch-gate-result.json"]:
    try:
        json.loads(Path(p).read_text())
    except Exception as e:
        bad.append(f"{p}: {e}")
if missing or bad:
    print("FAIL")
    if missing:
        print("Missing files:")
        [print(f"- {m}") for m in missing]
    if bad:
        print("Invalid JSON:")
        [print(f"- {b}") for b in bad]
else:
    print("PASS")
    print("All required files exist and JSON files are valid.")
