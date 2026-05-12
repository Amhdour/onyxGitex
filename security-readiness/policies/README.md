# Policy-as-Code Foundation (YAML + Schema)

## Scope
This directory provides an explicit, testable policy-as-code baseline for:
- retrieval authorization; and
- tool authorization.

Current implementation uses YAML policies validated by JSON Schema with a local Python evaluator. OPA/Rego is **not** integrated in runtime yet.

## Artifacts
- `retrieval_authorization.yaml`: role, tenant, department, and document-level retrieval rules.
- `tool_authorization.yaml`: tool access and risk/approval requirements.
- `policy_schema.json`: strict schema enforcing default deny and fail-closed semantics.
- `policy_evaluator.py`: lightweight loader + evaluator returning structured decisions.
- `examples/atlas-advisory-access-policy.yaml`: request examples.
- `tests/test_policy_evaluator.py`: policy tests for required deny/allow outcomes.

## Required policy fields
Policies and request evaluation cover:
- subject user id
- role
- department
- tenant/workspace (`tenant_id`)
- document owner department
- document classification
- allowed roles
- denied roles
- tool name
- tool risk level
- human approval required
- default deny
- fail closed on missing context

## Decision shape
The evaluator returns:
- `allow` (boolean)
- `reason` (machine-readable)
- `policy_id`
- `missing_fields` (for fail-closed)
- `evidence` (matching rule/tool/fail-closed marker)

## OPA migration note
This baseline can be migrated to OPA/Rego by:
1. Preserving field names and request envelopes as Rego `input`.
2. Translating YAML rule arrays into Rego data documents.
3. Mirroring `missing_fields` checks as explicit deny rules.
4. Keeping structured decision payload fields aligned.
