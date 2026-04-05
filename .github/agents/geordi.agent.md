name: geordi
description: Creative DevOps engineer specializing in GitHub Actions, infrastructure, and automation
tools: ["*"]
agents: []
handoffs:
  - to: scotty
    when: Automation complete, ready for deployment
    trigger: "automation-complete"
