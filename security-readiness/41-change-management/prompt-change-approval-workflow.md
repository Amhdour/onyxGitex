# Prompt Change Approval Workflow

## Scope
Controls for system prompt, policy prompt, routing prompt, and tool-use prompt updates.

## Workflow
1. Submit `AI Change Request` with **Change Type = Prompt** and prompt diff.
2. Perform risk assessment on prompt injection resistance, policy adherence, and data disclosure risk.
3. Run required tests:
   - prompt regression suite,
   - jailbreak/prompt-injection abuse tests,
   - policy conformance checks,
   - deterministic scenario checks where applicable.
4. Update evidence with prompt versions, test outputs, and observed behavior changes.
5. Obtain approvals before production release.
6. Deploy with rollback version pointer.
7. Re-evaluate launch gate impact from safety/performance outcomes.

## Required Control Fields
- **Change Type:** Prompt
- **Risk Assessment:** Mandatory
- **Required Tests:** Mandatory
- **Evidence Update:** Mandatory
- **Approval Owner:** AI Safety Owner
- **Rollback:** Required (prompt version revert)
- **Launch Gate Impact:** Required

## Minimum Approval Criteria
- No new high-risk leakage or policy-bypass outcomes.
- Prompt behavior changes are traceable and justified.
- Evidence artifacts are complete and auditable.
