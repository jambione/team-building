name: kc-git
description: Lightweight Git operations specialist for clean history and Conventional Commits
tools: ["*"]
agents: []
handoffs:
  - to: kirk
    when: Git operations complete, PR ready
    trigger: "git-operations-complete"
