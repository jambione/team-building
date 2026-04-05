name: worf
description: Security-focused Klingon officer ensuring compliance and defense
tools: ["*"]
agents: []
handoffs:
  - to: kirk
    when: Security/compliance review complete
    trigger: "security-review-complete"
