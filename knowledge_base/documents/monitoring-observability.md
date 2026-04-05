# Monitoring & Observability — Logging, Metrics, Alerting Standards

## Purpose
Standardized monitoring practices for production systems. Maintained by kc-dave, reviewed quarterly.

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

| Level | When to Use | Example |
|-------|-------------|---------|
| `DEBUG` | Development, detailed flow tracing | `user_id=123 entering checkout()` |
| `INFO` | Key business events, state changes | `order #456 created successfully` |
| `WARN` | Recoverable issues, deprecation notices | `Cache miss for user profile, falling back to DB` |
| `ERROR` | Failures requiring attention | `Failed to process payment: timeout` |

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

| Severity | Response Time | Notification Channels | Example |
|----------|---------------|----------------------|----------|
| **P1 - Critical** | < 5 minutes | PagerDuty + Slack + Email | Database down, 0% uptime |
| **P2 - High** | < 30 minutes | Slack + Email | Error rate > 5% |
| **P3 - Medium** | < 4 hours | Slack (channel) | Latency p99 > 2s |

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

## 6. Version History

```markdown
---
Version History:
- 2026-04-05: kc-dave — Initial monitoring and observability standards document
---
```

---

*Created: 2026-04-05 | Owner: kc-dave (orchestrator) | Review cadence: Quarterly*
