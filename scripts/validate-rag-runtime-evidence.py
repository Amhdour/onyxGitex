#!/usr/bin/env python3
import json, sys
from pathlib import Path
E=Path('security-readiness/evidence-artifacts/version-2a-rag-runtime')
req=["rag-runtime-final-status.json","rag-pytest-output.txt","rag-audit-events.json","rag-policy-decisions.json","rag-retrieval-log.json","rag-citation-check.json","rag-launch-gate-result.json","evidence-manifest.json"]
errs=[]
for f in req:
    if not (E/f).exists(): errs.append(f"missing: {f}")
status={}
if (E/'rag-runtime-final-status.json').exists():
    try: status=json.loads((E/'rag-runtime-final-status.json').read_text())
    except Exception as ex: errs.append(f"invalid json rag-runtime-final-status.json: {ex}")
ls=status.get('launch_status')
if ls not in {"NOT_ENOUGH_EVIDENCE","NO_GO","PARTIAL_RUNTIME_EVIDENCE"}: errs.append('invalid launch_status')
if status.get('production_ready') is not False: errs.append('production_ready must be false')
if status.get('go_decision') is not False: errs.append('go_decision must be false')
if ls=="GO": errs.append('GO forbidden for version 2A')
print('FAIL' if errs else 'PASS')
for e in errs: print('-',e)
sys.exit(1 if errs else 0)
