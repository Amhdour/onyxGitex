#!/usr/bin/env python3
from __future__ import annotations

def _resp(tool_name: str, decision: str, reason: str, payload: dict | None = None) -> dict:
    return {
        "tool_name": tool_name,
        "simulated": True,
        "external_side_effect": False,
        "decision": decision,
        "reason": reason,
        "payload": payload or {},
    }

def search_internal_docs_mock(query: str) -> dict:
    return _resp("search_internal_docs", "ALLOW_SIMULATED", "Local simulated search only.", {"query": query})

def read_document_mock(document_id: str) -> dict:
    return _resp("read_document", "ALLOW_SIMULATED", "Local simulated read only.", {"document_id": document_id})

def draft_email_mock(subject: str, body: str) -> dict:
    return _resp("draft_email", "ALLOW_SIMULATED", "Draft only; not sent.", {"subject": subject, "body_preview": body[:80]})

def send_email_mock(recipient: str, subject: str) -> dict:
    return _resp("send_email", "SIMULATED_ONLY", "Email dispatch disabled in sandbox.", {"recipient": recipient, "subject": subject})

def update_crm_record_mock(record_id: str, field: str, value: str) -> dict:
    return _resp("update_crm_record", "SIMULATED_ONLY", "No external CRM modification occurs.", {"record_id": record_id, "field": field, "value": value})

def delete_record_mock(record_id: str) -> dict:
    return _resp("delete_record", "DENY", "Delete operation denied by sandbox policy.", {"record_id": record_id})

def external_api_call_mock(endpoint: str) -> dict:
    return _resp("external_api_call", "DENY", "Network access prohibited in this harness.", {"endpoint": endpoint})
