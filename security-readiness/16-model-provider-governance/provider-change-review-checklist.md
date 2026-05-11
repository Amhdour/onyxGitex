# 100. Provider Change Review Checklist

Date: 2026-05-11
Status: **Operational Checklist**

Use this checklist before adding/changing/removing an LLM or embedding provider/model.

## Change metadata
- [ ] Change ticket ID:
- [ ] Requestor + approver:
- [ ] Environment(s): dev / staging / prod
- [ ] Effective date (YYYY-MM-DD):

## Governance checks
- [ ] Provider is in approved vendor list.
- [ ] Data processing terms and retention reviewed for this provider/model version.
- [ ] Data classification impact reviewed (public/internal/confidential/restricted).
- [ ] Model purpose documented (chat, summarization, reasoning, embeddings, build-mode).

## Security configuration checks
- [ ] No live secrets committed; keys sourced from approved secret manager.
- [ ] Provider API base/version/custom config reviewed for least privilege.
- [ ] Persona/group/public access settings reviewed.
- [ ] Routing behavior reviewed, including override paths.
- [ ] Fallback behavior reviewed and risk accepted for target personas.

## Logging and evidence checks
- [ ] Provider/model decision logging enabled and sampled.
- [ ] Prompt/response payload logging policy validated (redaction/no retention as required).
- [ ] Embedding metrics/logging reviewed for metadata leakage risk.
- [ ] Test evidence attached: targeted unit/integration/regression tests.

## Required outcomes
- [ ] Risk rating recorded (Low/Med/High/Critical).
- [ ] Residual risks assigned with owners + due dates.
- [ ] Launch gate recommendation updated (Go / Conditional Go / No-Go).

## Launch gate effect
- Any unchecked critical item => **No-Go**.
