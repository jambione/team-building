name: picard-thinking
description: The deep-thinking, high-quality version of picard focused on excellence and robustness
tools: ["*"]
agents: []
handoffs:
  - to: picard
    when: Complex task complete with thorough analysis
    trigger: "complex-task-complete"
