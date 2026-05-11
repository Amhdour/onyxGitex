# Client Report Quality Checklist

## Purpose
Provide a pre-delivery checklist to ensure client reports are complete, auditable, and aligned with readiness evidence standards.

## Checklist
- [ ] Report metadata is complete (owner, date UTC, version, status).
- [ ] Scope is explicitly defined and bounded.
- [ ] Method section explains how conclusions were derived.
- [ ] All findings are mapped to evidence references.
- [ ] Evidence references include artifact path, command, timestamp, git commit, and status.
- [ ] Confidence labels are present for each major claim (`Verified`, `Partially Confirmed`, `Unknown`).
- [ ] Assumptions are explicit and not presented as facts.
- [ ] Open risks and residual risks are clearly listed with owners when available.
- [ ] Sensitive values are redacted as `[REDACTED]`.
- [ ] Report recommendations are actionable and scoped.
- [ ] Reviewer notes and approval status are documented.

## Final Gate
Do not label a report "ready for client delivery" unless all mandatory checklist items pass or exceptions are documented.
