#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import re

ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / 'presentation-export'
GENERATED = EXPORT / 'generated'
SLIDE_SRC = EXPORT / 'slide-content-for-ppt.md'
PPTX_PATH = GENERATED / 'onyxgitex-ai-trust-security-readiness-deck.pptx'

required = [
    'presentation-export/README.md','presentation-export/powerpoint-export-plan.md','presentation-export/slide-content-for-ppt.md',
    'presentation-export/slide-layout-spec.md','presentation-export/speaker-notes-export.md','presentation-export/one-page-handout.md',
    'presentation-export/presentation-claim-boundaries.md','presentation-export/export-status.json','presentation-export/export-manifest.json',
    'presentation-export/validation-result.txt','presentation-export/blockers.md'
]

def sha(path: Path):
    if not path.exists(): return None
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write_manifest():
    files = []
    for rel in required + [
        'presentation-export/generated/onyxgitex-ai-trust-security-readiness-deck.pptx',
        'presentation-export/generated/onyxgitex-ai-trust-security-readiness-deck.pdf',
        'presentation-export/generated/onyxgitex-one-page-handout.pdf'
    ]:
        p = ROOT / rel
        files.append({"path": rel, "exists": p.exists(), "sha256": 'SELF_REFERENTIAL_MANIFEST_HASH_NOT_APPLICABLE' if rel.endswith('export-manifest.json') else sha(p), "description": rel.split('/')[-1]})
    manifest = {"pack":"presentation-export","generated_at_utc":datetime.now(timezone.utc).isoformat(),"required_files":files}
    (EXPORT / 'export-manifest.json').write_text(json.dumps(manifest, indent=2)+"\n")

text = SLIDE_SRC.read_text()
blocks = re.findall(r'## Slide \d+\n(.*?)(?=\n## Slide \d+\n|\Z)', text, re.S)
status = {
  "pack":"presentation-export","status":"POWERPOINT_DECK_SOURCE_READY","source_pack":"pitch-deck-pack","source_pack_status":"PITCH_DECK_PACK_READY","slide_count":10,
  "pptx_generated":False,"pptx_path":None,"pdf_generated":False,"pdf_path":None,"one_page_handout_pdf_generated":False,
  "production_ready":False,"go_decision":False,"client_evidence_verified":False,
  "claim_safety":{"production_claim_allowed":False,"go_claim_allowed":False,"client_go_claim_allowed":False},
  "next_required_action":"Generate the PowerPoint file from presentation-export/slide-content-for-ppt.md using available presentation tooling"
}
try:
    from pptx import Presentation
    prs = Presentation()
    for block in blocks[:10]:
        title = re.search(r'- Title: (.*)', block).group(1).strip()
        mm = re.search(r'- Main message: (.*)', block).group(1).strip()
        bullets = re.findall(r'^  - (.*)$', block, re.M)
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = title
        tf = slide.shapes.placeholders[1].text_frame
        tf.text = mm
        for b in bullets:
            p = tf.add_paragraph(); p.text = b
    GENERATED.mkdir(parents=True, exist_ok=True)
    prs.save(PPTX_PATH)
    status['status'] = 'POWERPOINT_DECK_EXPORT_READY'
    status['pptx_generated'] = True
    status['pptx_path'] = 'presentation-export/generated/onyxgitex-ai-trust-security-readiness-deck.pptx'
    status['next_required_action'] = 'Use the deck for client and partner presentations, then fill Version 4 with real client evidence before any production decision'
except Exception:
    pass

(EXPORT / 'export-status.json').write_text(json.dumps(status, indent=2)+"\n")
write_manifest()
print(status['status'])
