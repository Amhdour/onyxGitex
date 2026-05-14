#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pitch-deck-pack"

required = [
    "README.md","00-deck-overview.md","01-slide-title.md","02-slide-problem.md","03-slide-solution.md",
    "04-slide-evidence-chain.md","05-slide-rag-readiness.md","06-slide-observability-and-ci.md",
    "07-slide-agent-runtime-safety.md","08-slide-staging-demo.md","09-slide-client-production-template.md",
    "10-slide-next-step.md","speaker-notes.md","demo-flow.md","visual-style-guide.md",
    "slide-by-slide-script.md","deck-claim-boundaries.md","deck-one-page-summary.md","deck-status.json",
    "deck-manifest.json","validation-result.txt","blockers.md"
]
slide_files = [
   "01-slide-title.md","02-slide-problem.md","03-slide-solution.md","04-slide-evidence-chain.md",
   "05-slide-rag-readiness.md","06-slide-observability-and-ci.md","07-slide-agent-runtime-safety.md",
   "08-slide-staging-demo.md","09-slide-client-production-template.md","10-slide-next-step.md"
]
errors=[]
if not PACK.exists():
    errors.append("pitch-deck-pack/ missing")
for f in required:
    if not (PACK/f).exists():
        errors.append(f"missing required file: {f}")
existing_slides = sorted([x.name for x in PACK.glob("[0-9][0-9]-slide-*.md")])
if existing_slides != sorted(slide_files):
    errors.append(f"slide files mismatch: {existing_slides}")

status_path=PACK/"deck-status.json"
status={}
if status_path.exists():
    try:
        status=json.loads(status_path.read_text())
    except Exception as e:
        errors.append(f"deck-status.json parse error: {e}")
else:
    errors.append("deck-status.json missing")

checks={"status":"PITCH_DECK_PACK_READY","slide_count":10,"production_ready":False,"go_decision":False,"client_evidence_verified":False}
for k,v in checks.items():
    if status.get(k)!=v:
        errors.append(f"deck-status field {k} expected {v} got {status.get(k)}")

manifest_path=PACK/"deck-manifest.json"
if manifest_path.exists():
    try:
        manifest=json.loads(manifest_path.read_text())
        listed={item.get('path') for item in manifest.get('required_files',[])}
        for f in required:
            if f not in listed:
                errors.append(f"deck-manifest.json missing required_files entry: {f}")
    except Exception as e:
        errors.append(f"deck-manifest.json parse error: {e}")
else:
    errors.append("deck-manifest.json missing")

forbidden=["production_ready: true","go_decision: true","production-ready system","fully secure","guaranteed safe","compliance approved","client approved","real production GO","universal production safety"]
for fp in list(PACK.glob("*.md"))+list(PACK.glob("*.json")):
    if fp.name == "deck-claim-boundaries.md":
        continue
    lines=fp.read_text().splitlines()
    skip=False
    for i,line in enumerate(lines,1):
        ll=line.lower().strip()
        if ll.startswith("## "):
            skip=False
        if ll == "## what not to say":
            skip=True
            continue
        if skip:
            continue
        for t in forbidden:
            tl=t.lower()
            if tl in ll and "not " + tl not in ll:
                errors.append(f"forbidden overclaim '{t}' in {fp.name}:{i}")

if errors:
    print("FAIL: " + "; ".join(errors))
    sys.exit(1)
print("PASS: pitch-deck-pack")
