# Sandboxed Tool Model

Purpose: define deterministic non-production tool boundaries for study evidence.

## Tool risk levels
- low
- medium
- high
- critical

## Tool categories
- read-only
- draft-only
- approval-required
- blocked
- critical-deny

## Mock/sandbox rules
- never call real external services
- never send real emails
- never modify real records
- never delete records
- never expose secrets

## Required sandbox test cases
- send_email is simulated only
- update_crm_record is simulated only
- delete_record is denied fail-closed
- unknown external_api_call is denied fail-closed
- policy unavailable denies fail-closed

## Evidence required
- graph-denied-tool-call-log.json
- graph-human-approval-required-log.json
- graph-fail-closed-log.json
- graph-audit-events.json
