name: picard-fast
description: The fast, lightweight version of picard focused on speed and rapid iteration
tools: ["*"]
agents: []
handoffs:
  - to: picard
    when: Fast task complete, ready for detailed review
    trigger: "fast-task-complete"
