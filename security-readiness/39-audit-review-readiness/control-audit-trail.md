# Control Audit Trail

## Purpose
Track control-level audit history, findings, and remediation progress with accountable sign-off.

## Control Audit Trail Log

| Control ID | Review Criteria | Evidence Required | Reviewer | Status | Finding Severity | Remediation | Sign-off |
|---|---|---|---|---|---|---|---|
| CTRL-001 | Control design matches documented threat scenario. | Threat-control mapping reference and control spec. |  | Not Started | N/A |  | Pending |
| CTRL-002 | Control implementation is traceable to code/config. | Repo path + commit SHA + config reference. |  | Not Started | N/A |  | Pending |
| CTRL-003 | Control verification includes positive/negative tests. | Test commands, outputs, pass/fail summary. |  | Not Started | N/A |  | Pending |
| CTRL-004 | Control emits required audit telemetry. | Log field schema, sample event IDs, trace links. |  | Not Started | N/A |  | Pending |
| CTRL-005 | Exceptions and failures are fail-closed or explicitly risk-accepted. | Failure mode evidence and risk acceptance record. |  | Not Started | N/A |  | Pending |

## Severity Scale
- `Critical`: Launch-blocking security weakness.
- `High`: Significant weakness requiring remediation before approval.
- `Medium`: Important issue; can proceed only with documented compensating controls.
- `Low`: Minor issue; track to closure.
- `N/A`: No finding yet.

## Sign-off Record
- Audit Cycle:
- Final Reviewer:
- Date (YYYY-MM-DD):
- Decision:
- Notes:
- Signature/Initials:
