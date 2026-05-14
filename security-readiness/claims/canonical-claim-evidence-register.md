# Canonical Claim-Evidence Register

| Claim ID | Claim text | Claim type | Status | Evidence path | Evidence quality | Limitation | External-safe wording | Forbidden wording |
|---|---|---|---|---|---|---|---|---|
| CLM-001 | This repo demonstrates a readiness methodology for RAG and agent systems. | portfolio | ALLOWED | portfolio-lab/README.md | Strong static | Not runtime proof | Methodology demonstration | Proven production security |
| CLM-002 | This repo includes control design artifacts for retrieval authorization, tool authorization, telemetry, and launch-gate decisions. | design | ALLOWED | security-readiness/, production-readiness/ | Strong design | Design != enforcement | Includes control design artifacts | Fully enforced in production |
| CLM-003 | This repo includes local or CI evidence only where explicitly shown in evidence artifacts. | local runtime | ALLOWED | security-readiness/evidence-artifacts/ | Partial runtime | Coverage incomplete | Evidence is scoped and explicit | All controls runtime-proven |
| CLM-004 | This repo proves production-grade security. | production | NOT_ALLOWED | N/A | None | Missing production runtime | Not claimed | Proves production-grade security |
| CLM-005 | This repo is client-production ready. | client | NOT_ALLOWED | N/A | None | Template-only client artifacts | Not claimed | Client-production ready |
| CLM-006 | All RAG leakage risks are eliminated. | production | BLOCKED | N/A | None | Not provable | Risk reduced in tested scope only | Risks eliminated |
| CLM-007 | All agent tool risks are eliminated. | production | BLOCKED | N/A | None | Not provable | Partial controls and tests exist | Risks eliminated |
| CLM-008 | This is compliant with ISO/IEC 42001. | production | NOT_ALLOWED | security-readiness/21-compliance-frameworks/iso-iec-42001-mapping.md | Mapping only | No certification audit | Mapping references only | ISO/IEC 42001 compliant |
