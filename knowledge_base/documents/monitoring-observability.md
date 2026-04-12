# Monitoring & Observability — Logging, Metrics, Alerting Standards

## Current State

**As of**: 2026-04-05  
**Health**: AMBER  
**Top active item**: Claude API PR review metrics (latency, cost, skip rate) added to CI — Grafana panel required before go-live. Rate-limit alerting for burst PR windows deferred to Sprint 2 (CF-001).

---

## Purpose

Standardized monitoring practices for production systems. Maintained by obrien, reviewed quarterly.

---

## The Three Core Operational Questions

Every service must be able to answer these at all times:

1. **Is it up?** — Health checks wired to alerting with <30s detection latency.
2. **Is it healthy?** — Golden signals captured: latency (p50/p95/p99), error rate, saturation.
3. **Is it getting worse?** — Trend tracking and SLO burn-rate alerts configured.

If a system cannot answer all three, it is not production-ready.

---

## 1. Monitoring Stack Architecture (Mermaid)

```mermaid
graph LR
    A[Application] -->|Structured Logs| B[Log Aggregator]
    C[Metric Collector] -->|Prometheus Exporter| D[Time-Series DB]
    E[Apm Agent] -->|Traces| F[Distributed Trace Store]
    G[Alert Manager] -.->|Rules| D
    H[Dashboard Layer] -.->|Queries| D & Time-Series DB

    subgraph Logging Stack
        B[ELK/Fluentd]
    end

    subgraph Metrics Stack
        C[Prometheus Node Exporter]
        D[Prometheus TSDB]
    end
```

---

## 2. Log Level Standards

| Level   | When to Use                             | Example                                           |
| ------- | --------------------------------------- | ------------------------------------------------- |
| `DEBUG` | Development, detailed flow tracing      | `user_id=123 entering checkout()`                 |
| `INFO`  | Key business events, state changes      | `order #456 created successfully`                 |
| `WARN`  | Recoverable issues, deprecation notices | `Cache miss for user profile, falling back to DB` |
| `ERROR` | Failures requiring attention            | `Failed to process payment: timeout`              |

---

## 3. Metric Naming Convention

```bash
# Pattern: <namespace>_<system>_<metric>{_label}

# Examples:
api_requests_total{method="GET",status="200"}        # Counter
api_request_duration_seconds                         # Histogram
memory_usage_bytes{gc="young"}                       # Gauge
```

---

## 4. Alerting Rules (Severity Matrix)

| Severity          | Response Time | Notification Channels     | Example                  |
| ----------------- | ------------- | ------------------------- | ------------------------ |
| **P1 - Critical** | < 5 minutes   | PagerDuty + Slack + Email | Database down, 0% uptime |
| **P2 - High**     | < 30 minutes  | Slack + Email             | Error rate > 5%          |
| **P3 - Medium**   | < 4 hours     | Slack (channel)           | Latency p99 > 2s         |

---

## 5. Health Check Endpoint Template

```bash
# Required endpoint: GET /health
# Response format: JSON with status, timestamp, checks array

{
    "status": "healthy",
    "timestamp": "2026-04-05T15:30:00Z",
    "checks": [
        {"name": "database", "status": "ok", "latency_ms": 12},
        {"name": "cache", "status": "ok", "hit_rate": 0.94}
    ]
}
```

---

## 6. SLO / SLA Definitions

### Availability Targets

| Environment | SLO Target   | Measurement Window |
| ----------- | ------------ | ------------------ |
| Production  | 99.9% uptime | Rolling 30 days    |
| Staging     | 99.0% uptime | Rolling 7 days     |

### Error Budget Policy

- 99.9% SLO = 43.8 minutes/month error budget.
- When error budget is >50% consumed: freeze non-critical deployments.
- When error budget is 100% consumed: all deployments require explicit picard approval.

---

## 7. Deployment Telemetry Prerequisite (added 2026-04-12)

Before any spoke-repo service reaches production, at minimum one structured deployment event must be emitted from the deployment workflow. This event must include:

- `environment` — staging / production / etc.
- `commit_sha` — the exact SHA being deployed
- `deployed_at` — ISO-8601 timestamp
- `outcome` — success / failure / rolled-back

Without this event, the first production incident has no deployment correlation data. "Is it up?" cannot be answered. This is the minimum viable deployment telemetry gate.

---

## 8. Current Observability Gaps (updated 2026-04-12)

| Gap                                                    | Severity | Owner  | Sprint   | Status |
| ------------------------------------------------------ | -------- | ------ | -------- | ------ |
| No application source code — nothing to instrument     | Critical | data   | Sprint 3 | open   |
| No observability platform configured                   | High     | obrien | Sprint 3 | open   |
| ~~Deployment telemetry events not emitted from workflows~~ | ~~High~~ | geordi | ~~Sprint 3~~ | **RESOLVED 2026-04-12** — deploy-staging.yml and deploy-production.yml both emit structured `DEPLOY_EVENT` telemetry |
| No SLO burn-rate alerts defined                        | High     | obrien | Sprint 3 | open   |
| No structured logging library integrated               | Medium   | data   | Sprint 3 | open   |
| deploy-staging.yml rollback notification missing `actor` field | Low | geordi | Sprint 3 | open — inconsistency vs deploy-production.yml |

---

## 9. Version History

```markdown
---
Version History:
    - 2026-04-05: picard — Initial monitoring and observability standards document
    - 2026-04-05: obrien — Added Three Core Operational Questions, SLO definitions, observability gaps; updated ownership
    - 2026-04-12: crusher — Closed deployment telemetry gap (deploy workflows now emit structured events); fixed duplicate section 7; added staging rollback actor gap; renumbered sections 8/9
---
```

---

_Created: 2026-04-05 | Owner: obrien | Review cadence: Quarterly_
