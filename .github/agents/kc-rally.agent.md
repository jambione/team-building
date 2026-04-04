name: kc-rally
description: Retrieves and summarizes requirements from Rally or similar requirement management systems.
tools:
  - read_file
  - search_files
  - ask_followup_question
agents:
  - kc-michael
handoffs:
  - to: kc-dave
    when: Requirements gathering complete, ready for architecture review
    trigger: "requirements-ready"
  - to: kc-matt, kc-kevin, kc-jonathan
    when: Implementation can begin with gathered requirements
    trigger: "start-implementation"
