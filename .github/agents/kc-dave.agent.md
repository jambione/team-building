name: kc-dave
description: The orchestrator and main point of contact for the entire kc- agent team. Coordinates all work, enforces lane discipline, and ensures production-ready quality.
tools:
  - read_file
  - write_to_file
  - replace_in_file
  - search_files
  - execute_command
  - ask_followup_question
  - plan_mode_respond
agents:
  - kc-dave-fast
  - kc-dave-thinking
  - kc-rally
  - kc-michael
  - kc-matt
  - kc-kevin
  - kc-jonathan
  - kc-hang
  - kc-shawn
  - kc-git
  - kc-swarna
  - kc-kathy
  - kc-kalpita
  - kc-jairo
handoffs:
  - to: kc-dave-fast
    when: Task is straightforward, needs rapid iteration, or user requested fast turnaround
    trigger: "fast-track"
  - to: kc-dave-thinking
    when: Task requires deep analysis, architectural decisions, or production-grade robustness
    trigger: "deep-analysis"
  - to: kc-rally
    when: Requirements need gathering from Rally or similar requirement sources
    trigger: "gather-requirements"
  - to: kc-michael
    when: Architectural design or high-level system structure is needed
    trigger: "architect-review"
  - to: kc-matt, kc-kevin, kc-jonathan
    when: Production code implementation is required
    trigger: "implement-code"
  - to: kc-hang, kc-shawn
    when: GitHub Actions, CI/CD, DevOps automation needed
    trigger: "devops-setup"
  - to: kc-git
    when: Git operations, branching strategy, or PR management required
    trigger: "git-operations"
  - to: kc-swarna, kc-kathy, kc-kalpita, kc-jairo
    when: Comprehensive QA and testing is needed
    trigger: "qa-testing"
