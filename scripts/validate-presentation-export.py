#!/usr/bin/env python3
import json,re,sys
from pathlib import Path
root=Path('.')
exp=root/'presentation-export'
req=['README.md','powerpoint-export-plan.md','slide-content-for-ppt.md','slide-layout-spec.md','speaker-notes-export.md','one-page-handout.md','presentation-claim-boundaries.md','export-status.json','export-manifest.json','validation-result.txt','blockers.md']
errs=[]
if not exp.exists(): errs.append('presentation-export missing')
for f in req:
    if not (exp/f).exists(): errs.append(f'missing file: presentation-export/{f}')
status={}
if (exp/'export-status.json').exists():
    status=json.loads((exp/'export-status.json').read_text())
    if status.get('status') not in ['POWERPOINT_DECK_EXPORT_READY','POWERPOINT_DECK_SOURCE_READY']: errs.append('invalid status')
    for k,v in [('slide_count',10),('production_ready',False),('go_decision',False),('client_evidence_verified',False)]:
        if status.get(k)!=v: errs.append(f'export-status {k} invalid')
slides=(exp/'slide-content-for-ppt.md').read_text() if (exp/'slide-content-for-ppt.md').exists() else ''
if len(re.findall(r'^## Slide \d+$',slides,re.M))!=10: errs.append('slide count in source not 10')
titles=["AI Trust & Security Readiness for RAG and Autonomous Agents","The Problem: AI Systems Move Faster Than Their Evidence","The Solution: Evidence-Based Readiness and Launch Gates","The Evidence Chain","RAG Readiness: Retrieval Boundaries and Citation Safety","CI and Observability: Evidence That Can Be Rechecked","Agent Runtime Safety: Identity, Tools, Approval, and Fail-Closed Behavior","Staging Demo: Mapping Evidence Into a Deployment Shape","Client-Specific Production Template","Next Step: Client Discovery and Evidence Intake"]
for t in titles:
    if f'- Title: {t}' not in slides: errs.append(f'missing title: {t}')
if (exp/'export-manifest.json').exists():
    man=json.loads((exp/'export-manifest.json').read_text())
    paths=[x.get('path') for x in man.get('required_files',[])]
    for rf in [f'presentation-export/{x}' for x in req]:
        if rf not in paths: errs.append(f'manifest missing {rf}')
    for item in man.get('required_files',[]):
        p=Path(item['path'])
        if str(p).startswith('presentation-export/generated/') and item.get('exists') and (not p.exists()): errs.append(f'manifest incorrectly marks generated file exists: {p}')
if status.get('pptx_generated') and not Path(status.get('pptx_path','')).exists(): errs.append('pptx path missing')
if status.get('pdf_generated') and not Path(status.get('pdf_path','')).exists(): errs.append('pdf path missing')
forbidden=['production_ready: true','go_decision: true','client_evidence_verified: true','CLIENT_GO','production ready','fully secure','guaranteed safe','client approved','compliance approved','real production GO','universal production safety']
allowed=['production readiness remains blocked','not production-ready without real client evidence','production readiness remains blocked until real client evidence exists']
for fp in exp.glob('*.md'):
    txt=fp.read_text().lower()
    if fp.name=='presentation-claim-boundaries.md':
        continue
    for w in forbidden:
        lw=w.lower()
        if lw in txt:
            if 'does not prove' in txt or 'do not say' in txt:
                continue
            errs.append(f'forbidden phrase in {fp.name}: {w}')
for fp in exp.glob('*.json'):
    txt=fp.read_text().lower()
    for w in forbidden[:3]:
        if w.lower() in txt: errs.append(f'forbidden claim in {fp.name}: {w}')
if errs:
    print('FAIL: ' + '; '.join(errs)); sys.exit(1)
print('PASS: presentation-export')
