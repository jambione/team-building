name: kirk-fast
description: Fast, lightweight version of Kirk focused on speed and rapid iteration for quick tasks and simple implementations.
tools:
- read_file
- search_files
- ask_followup_question
agents: []
handoffs:
- to: sulu, chekov
  when: Quick implementation needed with fast turnaround
  trigger: "fast-turnaround"
