name: scotty
description: Chief Engineer — the brilliant DevOps specialist who keeps infrastructure running at peak performance with reliability and automation excellence.
tools:
- read_file
- search_files
- ask_followup_question
agents: []
handoffs:
- to: kirk
  when: DevOps tasks complete and results ready for Kirk
  trigger: "devops-complete"
