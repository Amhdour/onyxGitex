#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "presentation-export"
STATUS_PATH = EXPORT / "export-status.json"
MANIFEST_PATH = EXPORT / "export-manifest.json"

REQUIRED_FILES = [
    "README.md",
    "powerpoint-export-plan.md",
    "slide-content-for-ppt.md",
    "slide-layout-spec.md",
    "speaker-notes-export.md",
    "one-page-handout.md",
    "presentation-claim-boundaries.md",
    "export-status.json",
    "export-manifest.json",
    "validation-result.txt",
    "blockers.md",
]

FORBIDDEN_OVERCLAIMS = [
    "production ready",
    "fully secure",
    "guaranteed safe",
    "client approved",
    "compliance approved",
    "real production go",
    "universal production safety",
    "real client evidence verified",
    "real deployment approved",
    "real external integration proof",
    "real langgraph production proof",
]

errs = []
if not EXPORT.exists():
    errs.append("presentation-export/ does not exist")

for f in REQUIRED_FILES:
    if not (EXPORT / f).exists():
        errs.append(f"missing required file: presentation-export/{f}")

status = {}
if STATUS_PATH.exists():
    try:
        status = json.loads(STATUS_PATH.read_text())
    except Exception as ex:
        errs.append(f"export-status.json parse error: {ex}")

if status:
    if status.get("slide_count") != 10:
        errs.append("slide_count must be 10")
    for k in ["production_ready", "go_decision", "client_evidence_verified"]:
        if status.get(k) is not False:
            errs.append(f"{k} must remain false")

    st = status.get("status")
    if st == "POWERPOINT_DECK_EXPORT_READY":
        p = status.get("pptx_path")
        if status.get("pptx_generated") is not True:
            errs.append("pptx_generated must be true when export ready")
        if not p:
            errs.append("pptx_path must be set when export ready")
        elif not (ROOT / p).exists():
            errs.append("pptx_path file does not exist")
        elif (ROOT / p).stat().st_size <= 0:
            errs.append("pptx file size must be > 0")
    elif st == "POWERPOINT_DECK_SOURCE_READY":
        if status.get("pptx_generated") is not False:
            errs.append("pptx_generated must be false when source ready")
        if status.get("pptx_path") is not None:
            errs.append("pptx_path must be null when source ready")
    else:
        errs.append("status must be POWERPOINT_DECK_EXPORT_READY or POWERPOINT_DECK_SOURCE_READY")

slides_text = (EXPORT / "slide-content-for-ppt.md").read_text() if (EXPORT / "slide-content-for-ppt.md").exists() else ""
if len(re.findall(r"^## Slide \d+$", slides_text, flags=re.M)) != 10:
    errs.append("slide-content-for-ppt.md must define exactly 10 slides")

if MANIFEST_PATH.exists():
    try:
        manifest = json.loads(MANIFEST_PATH.read_text())
    except Exception as ex:
        errs.append(f"export-manifest.json parse error: {ex}")
        manifest = None

    if manifest:
        entries = manifest.get("required_files", [])
        paths = {item.get("path"): item for item in entries}

        for req in [f"presentation-export/{x}" for x in REQUIRED_FILES]:
            if req not in paths:
                errs.append(f"manifest missing source entry: {req}")

        self_entry = paths.get("presentation-export/export-manifest.json")
        if not self_entry:
            errs.append("manifest missing self-entry")
        elif self_entry.get("sha256") != "SELF_REFERENTIAL_MANIFEST_HASH_NOT_APPLICABLE":
            errs.append("manifest self-entry hash must be SELF_REFERENTIAL_MANIFEST_HASH_NOT_APPLICABLE")

        for item in entries:
            path = item.get("path")
            sha = item.get("sha256")
            if path != "presentation-export/export-manifest.json" and sha == "SELF_REFERENTIAL_MANIFEST_HASH_NOT_APPLICABLE":
                errs.append("SELF_REFERENTIAL_MANIFEST_HASH_NOT_APPLICABLE may only be used for export-manifest.json")
            if str(path).startswith("presentation-export/generated/") and item.get("exists") is True:
                if not (ROOT / path).exists():
                    errs.append(f"generated file marked exists=true but missing: {path}")

for js in EXPORT.glob("*.json"):
    text = js.read_text().lower()
    if '"production_ready": true' in text:
        errs.append(f"forbidden production_ready=true in {js.name}")
    if '"go_decision": true' in text:
        errs.append(f"forbidden go_decision=true in {js.name}")
    if '"client_evidence_verified": true' in text:
        errs.append(f"forbidden client_evidence_verified=true in {js.name}")

if errs:
    print("FAIL: " + "; ".join(errs))
    sys.exit(1)

print("PASS: presentation-export")
