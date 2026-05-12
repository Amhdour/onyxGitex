# Tool Capability Matrix

| Tool name | Purpose | Risk level | Allowed by default? | Requires approval? | Required permission | Audit required? | Launch status |
|---|---|---|---|---|---|---|---|
| search_documents | Retrieve internal knowledge | Medium | Yes | No | knowledge.read | Yes | PARTIALLY_CONFIRMED |
| draft_email | Draft outbound communication | Medium | Yes | No | comms.draft | Yes | PARTIALLY_CONFIRMED |
| send_email | Send outbound communication | High | No | Yes | comms.send | Yes | NOT_RUN |
| create_ticket | Open operations ticket | Medium | Yes | No | ticket.create | Yes | PARTIALLY_CONFIRMED |
| read_customer_record | Read scoped customer record | High | No | Conditional | customer.read.scoped | Yes | NOT_ENOUGH_EVIDENCE |
| update_customer_record | Modify customer record | High | No | Yes | customer.write.scoped | Yes | NOT_RUN |
| export_data | Export datasets | Critical | No | Yes | data.export.approved | Yes | NOT_RUN |
| delete_record | Delete records | Critical | No (Denied) | N/A | none | Yes | DENIED_BY_DEFAULT |
