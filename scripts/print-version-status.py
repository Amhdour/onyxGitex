#!/usr/bin/env python3
import json
from pathlib import Path
p=Path("production-readiness/00-status/canonical-readiness-status.json")
data=json.loads(p.read_text())
for k in ["project","current_version","current_status","production_ready","launch_status","next_required_action"]:
    print(f"{k}: {data.get(k)}")
