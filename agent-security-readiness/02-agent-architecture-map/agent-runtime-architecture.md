# Agent Runtime Architecture

Flow:
User request → identity context → agent planner → policy decision point → tool registry → tool authorization decision → human approval gate when required → tool execution → audit log → final response → evidence store

Trust boundaries:
- User boundary
- Agent planner boundary
- Tool execution boundary
- Policy boundary
- Approval boundary
- External API boundary
- Audit/evidence boundary
