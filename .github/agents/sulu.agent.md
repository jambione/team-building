name: sulu
description: Skilled navigator who implements well-defined tasks with precision and accuracy
tools: ["*"]
agents:
  - kc-rally
handoffs:
  - to: bones
    when: Implementation complete, needs verification
    trigger: "implement-complete"
