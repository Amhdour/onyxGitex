#!/usr/bin/env python3
from pathlib import Path
import json
import sys

base = Path('client-facing-walkthrough-pack')
required = [
"README.md","00-executive-overview.md","01-problem-statement.md","02-service-positioning.md","03-evidence-chain-map.md","04-version-by-version-walkthrough.md","05-what-this-project-proves.md","06-what-this-project-does-not-prove.md","07-client-engagement-workflow.md","08-demo-script-15-minute.md","09-demo-script-30-minute.md","10-client-meeting-talk-track.md","11-sales-one-pager.md","12-technical-one-pager.md","13-deliverables-list.md","14-client-questions-and-answers.md","15-objection-handling.md","16-use-case-internal-company-knowledge-assistant.md","17-how-to-use-version-4-template.md","18-launch-gate-decision-model.md","19-readiness-maturity-model.md","20-next-step-email-template.md","21-linkedin-post-template.md","22-website-service-page-copy.md","23-partner-outreach-script.md","24-consultant-partnership-brief.md","25-private-school-university-offer.md","26-ai-agency-offer.md","27-founder-cto-brief.md","28-checklist-before-client-call.md","29-glossary-simple-english.md","30-glossary-technical.md","claim-boundaries.md","walkthrough-pack-status.json","walkthrough-pack-manifest.json","validation-result.txt","blockers.md"
]
errors=[]
if not base.exists():
    errors.append('missing folder client-facing-walkthrough-pack')
for f in required:
    if not (base/f).exists():
        errors.append(f'missing file {f}')

status_path=base/'walkthrough-pack-status.json'
if status_path.exists():
    try:
        status=json.loads(status_path.read_text())
        if status.get('status')!='CLIENT_WALKTHROUGH_PACK_READY': errors.append('status mismatch')
        if status.get('production_ready') is not False: errors.append('production_ready must be false')
        if status.get('go_decision') is not False: errors.append('go_decision must be false')
        if status.get('client_evidence_verified') is not False: errors.append('client_evidence_verified must be false')
    except Exception as e:
        errors.append(f'invalid status json: {e}')

manifest_path=base/'walkthrough-pack-manifest.json'
if manifest_path.exists():
    try:
        mani=json.loads(manifest_path.read_text())
        listed={Path(i.get('path','')).name for i in mani.get('required_files',[])}
        for f in required:
            if f not in listed:
                errors.append(f'manifest missing {f}')
    except Exception as e:
        errors.append(f'invalid manifest json: {e}')

forbidden=['production_ready: true','go_decision: true','CLIENT_GO','production-ready system','fully secure','guarantees safety','compliance approved','client approved','real production GO']
for p in base.iterdir():
    if p.suffix.lower() not in ['.md','.json','.txt']:
        continue
    text=p.read_text()
    for bad in forbidden:
        if bad in text:
            errors.append(f'forbidden phrase in {p.name}: {bad}')

if errors:
    print('FAIL: ' + '; '.join(errors))
    sys.exit(1)
print('PASS: client-facing-walkthrough-pack')
