name: kirk-fast
description: Fast, lightweight orchestrator for quick tasks and rapid iteration cycles
tools: ["*"]
agents:
  - spock
  - sulu
handoffs:
  - to: spock
    when: Task requires architectural consideration
    trigger: "fast-arch-review"
  - to: sulu
    when: Implementation can proceed quickly
    trigger: "fast-implement"
