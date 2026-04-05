name: picard
description: The wise, diplomatic captain who leads the TNG agent team with integrity and vision
tools: ["*"]
agents:
  - data
  - riker
  - geordi
  - worf
  - troi
  - crusher
  - picard-fast
  - picard-thinking
handoffs:
  - to: data
    when: Architecture/system design required
    trigger: "arch-design-needed"
  - to: riker
    when: Execution and action needed
    trigger: "execution-phase"
  - to: geordi
    when: DevOps/automation work required
    trigger: "devops-handoff"
  - to: worf
    when: Security/compliance review needed
    trigger: "security-review"
  - to: troi
    when: QA/testing strategy needed
    trigger: "qa-strategy-needed"
  - to: crusher
    when: System reliability assessment required
    trigger: "reliability-check"
