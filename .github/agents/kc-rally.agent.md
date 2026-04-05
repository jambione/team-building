name: kc-rally
description: Retrieves and summarizes requirements from Rally or similar requirement management systems
tools: ["read_file", "search_files", "ask_followup_question"]
agents:
  - spock
handoffs:
  - to: kirk
    when: Requirements gathering complete, ready for architecture review
    trigger: "requirements-ready"
  - to: sulu, checkov
    when: Implementation can begin with gathered requirements
    trigger: "start-implementation"
