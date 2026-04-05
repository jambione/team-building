name: bones
description: Meticulous QA specialist ensuring comprehensive testing and system health monitoring
tools: ["*"]
agents:
  - kc-rally
handoffs:
  - to: kirk
    when: All tests passed, ready for deployment review
    trigger: "qa-signoff"
