name: kc-git
description: Handles Git branching strategies, conventional commits, PR creation, and clean history maintenance.
tools:
  - execute_command
  - read_file
agents:
  - kc-hang
  - kc-shawn
handoffs:
  - to: kc-dave
    when: Git operations complete
    trigger: "git-complete"
  - to: kc-michael
    when: Branching strategy requires architectural review
    trigger: "arch-review-needed"
