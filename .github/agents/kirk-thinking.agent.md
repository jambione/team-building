name: kirk-thinking
description: Deep-thinking orchestrator for complex tasks, thorough analysis, and production-grade work
tools: ["*"]
agents:
  - spock
  - scotty
  - bones
  - checkov
handoffs:
  - to: spock
    when: Complex architecture decisions needed
    trigger: "thinking-arch-decision"
  - to: scotty
    when: Infrastructure optimization required
    trigger: "thinking-devops"
  - to: bones
    when: Comprehensive testing strategy needed
    trigger: "thinking-qa-strategy"
