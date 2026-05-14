# PowerPoint Export Plan

1. Source mapping
   - Use the 10 existing slide markdown files in `pitch-deck-pack/`.
   - Preserve claim boundaries from `deck-claim-boundaries.md`.
2. Presentation packaging
   - Build canonical slide source in `slide-content-for-ppt.md`.
   - Define reusable style system in `slide-layout-spec.md`.
3. Presenter materials
   - Export speaker notes to `speaker-notes-export.md`.
   - Export one-page summary to `one-page-handout.md`.
4. Safety controls
   - Keep `production_ready=false`, `go_decision=false`, `client_evidence_verified=false`.
   - Validate claim wording with `scripts/validate-presentation-export.py`.
5. Binary generation attempt
   - Attempt `.pptx` generation with local tooling.
   - If unavailable, keep source-ready status and document blocker.
