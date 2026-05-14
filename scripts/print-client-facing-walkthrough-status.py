#!/usr/bin/env python3
import json
from pathlib import Path

p=Path('client-facing-walkthrough-pack/walkthrough-pack-status.json')
obj=json.loads(p.read_text())
print(f"pack: {obj.get('pack')}")
print(f"status: {obj.get('status')}")
print(f"production_ready: {obj.get('production_ready')}")
print(f"go_decision: {obj.get('go_decision')}")
print(f"client_evidence_verified: {obj.get('client_evidence_verified')}")
print(f"purpose: {obj.get('purpose')}")
for k in ['version_2a','version_2b','version_2c','version_2d','version_3','version_4']:
    print(f"{k}: {obj.get('based_on_versions',{}).get(k)}")
for k in ['production_claim_allowed','go_claim_allowed','client_go_claim_allowed']:
    print(f"{k}: {obj.get('claim_safety',{}).get(k)}")
print(f"next_required_action: {obj.get('next_required_action')}")
