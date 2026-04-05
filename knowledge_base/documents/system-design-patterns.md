# System Design Patterns — IT Team Knowledge Base

## Purpose

Document scalable, maintainable system design patterns the team uses consistently. Updated quarterly by spock.

---

## Core Principles (From architecture-principles.md)

```
1. Simplicity first, then performance, maintainability, operational excellence
2. Single Responsibility Principle — each component does one thing well
3. Composition over inheritance for flexibility and testability
4. Design for long-term maintenance, not short-term speed
```

---

## Scalable System Patterns

### 1. Layered Architecture Pattern

**When to use:** Multi-tier applications with clear separation of concerns

**Structure:**

```
┌─────────────┐
│   UI Layer │ — Presentation, user interaction
├─────────────┤
│  Logic Layer│ — Business rules, domain operations
├─────────────┤
│ Data Layer  │ — Persistence, queries, caching
└─────────────┘
```

**Verification:** Each layer should be independently testable and replaceable.

---

### 2. Circuit Breaker Pattern

**When to use:** External service calls with timeout/retry requirements

**Implementation notes:**

- Prevent cascading failures
- Allow periodic health checks even when circuit is open
- Document fallback behaviors

---

### 3. Event Sourcing Pattern

**When to use:** Audit trails, temporal queries, domain-driven design

**Key considerations:**

- Command vs Query responsibility separation
- Read model projection strategy
- Event schema evolution handling

---

## Maintainability Patterns

### 4. Feature Flag Pattern

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Default   │───▶│  Flag Check │───▶│  Feature A  │
│  Behavior   │    │  Evaluation │    │  or Feature │
└─────────────┘    └─────────────┘    └─────────────┘
```

**Benefits:** Safe rollouts, A/B testing, zero-deployment feature releases

---

### 5. Strangler Fig Pattern

**For migrating monoliths to microservices:**

1. Identify bounded contexts
2. Create API gateway routes to new services
3. Gradually shift traffic
4. Decommission old code paths

---

## Verification Commands

```bash
# Search knowledge base for pattern references
grep -r "pattern\|layer" knowledge_base/documents/*.md | head -30

# Review architecture-related commits
git log --since="1 month ago" --oneline -- "*arch*" | head -20
```

---

_Created: 2026-04-04 | Owner: spock (Architect) | Review Cadence: Quarterly_
