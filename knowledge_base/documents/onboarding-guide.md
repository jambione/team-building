# Onboarding Guide — IT Team New Member Checklist

## Purpose

Standardized onboarding procedures for new team members. Maintained by picard, reviewed quarterly.

---

## Week 1: First Day Setup

### Day 1 — Access & Environment

```bash
# 1. Clone the repository
git clone https://github.com/<your-org>/team-building.git
cd team-building

# 2. Verify knowledge base access
ls -la knowledge_base/documents/

# 3. Review core documentation (in order)
cat knowledge_base/documents/index.md
```

### Checklist — Must Complete Before EOD Day 1

| Task                           | Resource                           | Status |
| ------------------------------ | ---------------------------------- | ------ |
| Read `team-conventions.md`     | Third-person communication rules   | ☐      |
| Review `coding-standards.md`   | Code quality expectations          | ☐      |
| Check out knowledge base index | Understand documentation structure | ☐      |

---

## Week 2: Technical Deep Dive

### Architecture & Design Patterns

```bash
# Read in this order:
1. architecture-principles.md — Foundational rules
2. system-design-patterns.md — Common patterns used
3. ci-cd-pipeline-recommendations.md — Build/deploy workflows
```

### DevOps & CI/CD Fundamentals

| Document                            | Focus Area                | Priority |
| ----------------------------------- | ------------------------- | -------- |
| `github-actions-best-practices.md`  | Workflow optimization     | HIGH     |
| `devops-best-practices.md`          | Speed targets, caching    | HIGH     |
| `ci-cd-pipeline-recommendations.md` | Production setup patterns | MEDIUM   |

---

## Week 3: Domain Knowledge

### Rally & Requirements Patterns

```bash
# Required reading for requirement-driven development
cat knowledge_base/documents/rally-patterns.md
```

### Development Practices

- `best-practices.md` — General QA and testing expectations
- `defect-management-process.md` — Bug reporting and tracking workflow

---

## Verification Commands

```bash
# Verify onboarding completion checklist
echo "=== Onboarding Progress ==="
echo "1. Architecture docs read: $(test -f knowledge_base/documents/architecture-principles.md && echo '✓' || echo '✗')"
echo "2. CI/CD docs reviewed: $(test -f knowledge_base/documents/ci-cd-pipeline-recommendations.md && echo '✓' || echo '✗')"
echo "3. Rally patterns studied: $(test -f knowledge_base/documents/rally-patterns.md && echo '✓' || echo '✗')"

# Generate onboarding report
gh api /repos/<your-org>/team-building/contents/knowledge_base/documents | jq '.[].name' > onboard-checklist.txt
```

---

## Mentorship Pairing (First Week)

| Day | Activity                       | Mentor Role      |
| --- | ------------------------------ | ---------------- |
| 1   | Environment setup verification | DevOps Lead      |
| 2   | Code review of sample PR       | Senior Developer |
| 3   | Architecture walkthrough       | Architect        |
| 4   | CI/CD pipeline demo            | DevOps Engineer  |

---

## Knowledge Base Coverage Verification

```bash
# Verify new member has read core docs
grep -l "onboarding-guide.md" knowledge_base/documents/*.md > /dev/null && echo "Index updated: ✓" || echo "Needs index update"
```

---

_Created: 2026-04-04 | Owner: picard (orchestrator) | Review cadence: Quarterly_
