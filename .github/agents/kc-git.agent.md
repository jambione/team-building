name: kc-git
description: Lightweight Git operations specialist — handles creating properly named branches, Conventional Commits, PR management, and clean history maintenance.
tools:
- read_file
- search_files
- ask_followup_question
agents: []
handoffs:
- to: kirk
  when: Git operations complete and summary ready for Kirk
  trigger: "git-complete"
