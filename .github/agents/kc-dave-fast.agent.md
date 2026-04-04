name: kc-dave-fast
description: The fast, lightweight version of kc-dave focused on speed and rapid iteration for quick tasks and simple implementations.
tools:
  - read_file
  - write_to_file
  - replace_in_file
  - search_files
  - ask_followup_question
agents:
  - kc-matt
  - kc-kevin
  - kc-jonathan
handoffs:
  - to: kc-dave
    when: Task complexity exceeds fast-track scope or requires deep analysis
    trigger: "escalate"
  - to: kc-hang, kc-shawn
    when: DevOps work is required within a fast track
    trigger: "devops-fast"
