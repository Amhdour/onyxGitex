# Repository Readiness Inventory

Date: 2026-05-14 UTC

| Path | Purpose | Current status | Evidence level | Supports allowed claim | Blocks claim | Contradiction risk | Recommended action |
|---|---|---|---|---|---|---|---|
| `VERSION_STATUS.md` | Top-level status narrative | Updated to canonical NO_GO | STATIC_REVIEW | Yes | Yes | Medium | Keep synchronized with canonical JSON |
| `portfolio-lab/` | Portfolio positioning and V1 packaging | Strong methodology docs | STATIC_REVIEW | Yes | No | Low | Keep explicit non-production wording |
| `portfolio-lab/VERSION_1_STATUS.md` | V1 status | Strong/mostly achieved | STATIC_REVIEW | Yes | No | Low | Keep as V1-only context |
| `production-readiness/` | Production-track starter kit | In progress; mixed design/local evidence | DESIGN_ONLY | Partial | Yes | High | Label templates clearly; avoid production language |
| `production-readiness/00-status/canonical-readiness-status.json` | Prior status model | Contains optimistic staging wording | STATIC_REVIEW | Partial | Yes | High | Supersede by canonical status model |
| `security-readiness/` | Canonical readiness workspace | Extensive docs + artifacts | MIXED | Yes | Yes | Medium | Normalize claims/evidence linkage |
| `security-readiness/evidence-artifacts/` | Runtime and validation artifacts | Mixed quality and levels | LOCAL_RUNTIME | Partial | Yes | High | Maintain canonical manifest with strict levels |
| `security-readiness/evidence-artifacts/evidence-validation/validation-result.json` | Launch evidence validation output | Historical result retained | LOCAL_RUNTIME | Partial | Yes | Medium | Preserve and contextualize limitations |
| `security-readiness/scripts/validate-launch-evidence.py` | Legacy validator | Works on specific rule set | LOCAL_HARNESS | Partial | Yes | Medium | Keep; do not treat as full readiness proof |
| `security-readiness/scripts/validate_readiness_evidence.py` | Canonical consistency validator | Added for v2 consistency track | STATIC_REVIEW | Yes | Yes | Low | Run in CI/local and keep output artifact |
| `.github/workflows/readiness-ci.yml` | CI readiness workflow | Present | CI_RUNTIME | Partial | Yes | Medium | Ensure outputs map to canonical manifest |
| `.github/workflows/rag-boundary-runtime-evidence.yml` | RAG runtime collection workflow | Present but not complete for all gaps | CI_RUNTIME | Partial | Yes | Medium | Expand execution evidence collection |
| `.github/workflows/langgraph-agent-lab-evidence.yml` | Agent evidence workflow | Present | CI_RUNTIME | Partial | Yes | Medium | Align claims with generated artifacts only |
| `security-readiness/evidence-artifacts/version-3-staging-demo/` | Staging demo artifacts | Template/mapping heavy | TEMPLATE_ONLY | Partial | Yes | High | Downgrade to NOT_VERIFIED until deployed traces |
| `security-readiness/evidence-artifacts/version-4-client-production-template/` | Client template artifacts | Template only | TEMPLATE_ONLY | Partial | Yes | High | Keep blocked until client evidence exists |
| `security-readiness/launch-gates/` | Canonical launch decision artifacts | Added NO_GO decision | STATIC_REVIEW | Yes | Yes | Low | Use as single launch decision source |
