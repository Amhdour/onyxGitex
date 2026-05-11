# GitHub Repository Structure for Portfolio Packaging

## Goal
Make the readiness work easy for reviewers, clients, and hiring panels to navigate.

## Recommended Structure
- `docs/case-study-internal-company-knowledge-assistant.md`
- `docs/evidence-gallery.md`
- `docs/client-demo-pack.md`
- `docs/github-repository-structure.md`
- `docs/professional-service-offer.md`
- `security-readiness/` (phase-based evidence workspace)

## Navigation Principles
1. Keep business-facing narrative in `docs/`
2. Keep detailed evidence trail in `security-readiness/`
3. Keep implementation changes and tests traceable in commit history
4. Avoid mixing unverified claims into public-facing summaries

## Reviewer Journey
1. Start with case study page for context
2. Review evidence gallery for artifact expectations
3. Inspect client demo pack for delivery model
4. Inspect readiness workspace for phase-by-phase artifacts
5. Validate claims against code/config/test outputs

## Maintenance Guidance
- Update docs only when evidence changes
- Timestamp material changes
- Mark obsolete claims explicitly
- Preserve historical decision context where possible
