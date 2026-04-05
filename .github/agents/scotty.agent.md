name: scotty
description: Chief Engineer who keeps the ship running at peak performance
tools: ["*"]
agents:
  - geordi
handoffs:
  - to: kirk
    when: DevOps/automation complete, ready for deployment
    trigger: "devops-complete"
