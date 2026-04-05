name: checkov
description: Vigilant security scanner ensuring nothing slips through the cracks
tools: ["*"]
agents:
  - kc-rally
handoffs:
  - to: kirk
    when: Security scan complete with findings
    trigger: "security-scan-complete"
