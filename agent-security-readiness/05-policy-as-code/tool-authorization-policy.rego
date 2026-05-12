package agent.authz

default allow = false
default requires_approval = false

missing_user_context if {
  not input.user
}

unknown_tool if {
  not input.tool in {"search_documents", "draft_email", "send_email", "create_ticket", "read_customer_record", "update_customer_record", "export_data", "delete_record"}
}

deny[msg] if {
  missing_user_context
  msg := "missing user context"
}

deny[msg] if {
  unknown_tool
  msg := "unknown tool"
}

allow if {
  not missing_user_context
  input.tool == "search_documents"
  input.user.department == input.resource_department
}

allow if {
  not missing_user_context
  input.tool == "draft_email"
}

allow if {
  not missing_user_context
  input.tool == "create_ticket"
}

requires_approval if {
  input.tool == "send_email"
}

requires_approval if {
  input.tool == "export_data"
}

requires_approval if {
  input.tool == "update_customer_record"
}

# delete_record stays denied by default via allow = false
