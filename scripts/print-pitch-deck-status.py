#!/usr/bin/env python3
import json
from pathlib import Path

status = json.loads((Path(__file__).resolve().parents[1]/"pitch-deck-pack"/"deck-status.json").read_text())
print(f"pack: {status['pack']}")
print(f"status: {status['status']}")
print(f"slide_count: {status['slide_count']}")
print(f"production_ready: {status['production_ready']}")
print(f"go_decision: {status['go_decision']}")
print(f"client_evidence_verified: {status['client_evidence_verified']}")
print(f"source_pack: {status['source_pack']}")
print(f"source_pack_status: {status['source_pack_status']}")
for k in ["version_2a","version_2b","version_2c","version_2d","version_3","version_4"]:
    print(f"{k}: {status['based_on_versions'][k]}")
for k in ["production_claim_allowed","go_claim_allowed","client_go_claim_allowed"]:
    print(f"{k}: {status['claim_safety'][k]}")
print(f"next_required_action: {status['next_required_action']}")
