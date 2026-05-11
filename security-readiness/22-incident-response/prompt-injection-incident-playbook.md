# Prompt Injection Incident Playbook (Priority 14)

Date: 2026-05-11
Status: Operational Draft (Client-Facing)

## Severity mapping
Classify using `ai-incident-classification-model.md`; prioritize as Sev-1/Sev-2 when injection leads to data exfiltration or unsafe tool routing.

## Detection signals
- Spike in policy-denied prompts containing override/jailbreak patterns.
- Trace anomalies: instruction hierarchy bypass or unsafe system prompt influence.
- Retrieval/tool events triggered by low-trust content unexpectedly.
- User report of model ignoring safety boundaries or revealing restricted instructions.

## Immediate containment steps
1. Enable stricter prompt/response guardrails (fail-closed mode).
2. Disable vulnerable tool pathways and high-risk actions.
3. Block or quarantine malicious source documents/prompts.
4. Force additional policy checks before retrieval/tool execution.

## Evidence to preserve
- Full prompt chain (system/developer/user/retrieved context) with redactions.
- Guardrail decision logs and policy evaluation outputs.
- Trace IDs showing model decision path and tool/retrieval branches.
- Retrieval and tool events correlated to the affected sessions.
- Relevant model/version and configuration snapshot.

## Escalation path
- Security On-call -> AI Safety Lead -> Incident Commander -> Legal/Privacy (if data exposure risk) -> Client Success.

## Client communication notes
- Describe behavior observed and impacted capabilities.
- Provide temporary safeguards in place and expected user impact.
- Clarify that forensic review is ongoing; identify unknowns explicitly.

## Remediation
- Harden prompt-injection filters and instruction precedence controls.
- Expand adversarial test suite for known injection patterns.
- Improve trust labeling and isolation for retrieved content.
- Update secure prompting standards and operator runbooks.

## Post-incident review requirements
- Confirm whether boundary bypass occurred.
- Validate control effectiveness with replay tests.
- Track residual risk and required design changes.
