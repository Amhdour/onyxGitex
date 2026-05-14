#!/usr/bin/env python3
import json
from pathlib import Path

p=Path('security-readiness/evidence-artifacts/version-3-staging-demo/version-3-staging-demo-status.json')
status=json.loads(p.read_text())
keys=['version','gate','status','harness_type','production_ready','go_decision','staging_demo_verified','container_runtime_verified','real_keycloak_runtime_verified','real_opa_runtime_verified','real_vault_runtime_verified','real_onyx_runtime_verified','real_langgraph_runtime_verified','real_retrieval_store_verified','real_external_observability_verified','prerequisites_verified','service_map_verified','identity_boundary_verified','secrets_boundary_verified','policy_path_verified','rag_path_verified','agent_path_verified','observability_path_verified','evidence_artifact_index_verified','staging_launch_gate_verified','next_required_action']
for k in keys:
    print(f'{k}: {status.get(k)}')
