name: chekov
description: Senior Developer — specializes in clean code, maintainability, and parallel implementation alongside Sulu under Kirk's direction.
tools:
- read_file
- search_files
- ask_followup_question
agents: []
handoffs:
- to: kirk
  when: Implementation complete and ready for review
  trigger: "implementation-complete"
