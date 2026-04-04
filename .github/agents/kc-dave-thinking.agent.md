name: kc-dave-thinking
description: The deep-thinking, high-quality version of kc-dave focused on excellence, robustness, and production-grade work.
tools:
  - read_file
  - write_to_file
  - replace_in_file
  - search_files
  - execute_command
  - ask_followup_question
agents:
  - kc-michael
  - kc-matt
  - kc-kevin
  - kc-jonathan
  - kc-hang
  - kc-shawn
handoffs:
  - to: kc-dave
    when: Task is complete and needs handoff to orchestrator
    trigger: "complete-task"
  - to: kc-swarna, kc-kathy, kc-kalpita, kc-jairo
    when: Comprehensive testing required for production release
    trigger: "production-qa"
