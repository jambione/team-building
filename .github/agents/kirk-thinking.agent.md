name: kirk-thinking
description: Deep-thinking, high-quality version of Kirk focused on excellence and robustness for complex tasks and production-grade work.
tools:
- read_file
- search_files
- ask_followup_question
agents: []
handoffs:
- to: spock
  when: Complex architecture review needed with deep analysis
  trigger: "deep-analysis"
