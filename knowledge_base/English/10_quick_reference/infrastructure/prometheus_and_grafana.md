---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.1"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prometheus, grafana, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Prometheus and Grafana

Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability. Grafana is the leading open-source platform for visualising time-series data. Together, they form the most popular monitoring stack for modern infrastructure and applications. Prometheus collects and stores metrics; Grafana displays them in dashboards.

---

## Prometheus Architecture

| Component | Description |
|-----------|-------------|
| **Prometheus server** | Scrapes metrics from targets; stores time-series data; evaluates alert rules |
| **Exporter** | Exposes metrics from a system (Node Exporter, cAdvisor, etc.) |
| **Pushgateway** | Receives metrics from short-lived jobs (batch jobs, CI) |
| **Alertmanager** | Handles alerts: grouping, silencing, routing, inhibition |
| **Service discovery** | Automatically discovers targets (Kubernetes, Consul, EC2, etc.) |

---

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Metric** | A named measurement with optional labels and a value |
| **Time series** | A stream of data points for a specific metric + label combination |
| **Job** | A collection of targets with the same purpose |
| **Instance** | A single target to scrape (usually a process) |
| **Scrape** | Prometheus pulling metrics from a target at regular intervals |
| **Label** | A key-value pair that dimensions a metric (e.g., `method="GET"`) |
| **Sample** | A value at a point in time: (timestamp, value) |

---

## Metric Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Counter** | Monotonically increasing value (only goes up) | Request count; errors; tasks completed |
| **Gauge** | Value that can go up or down | Temperature; memory usage; queue length |
| **Histogram** | Observations bucketed by value | Request latency; response size |
| **Summary** | Similar to histogram; calculates quantiles client-side | Latency percentiles |

---

## PromQL (Query Language)

### Basic Queries

| Query | Description |
|-------|-------------|
| `http_requests_total` | Raw time series |
| `http_requests_total{method="GET"}` | Filter by label |
| `http_requests_total{method="GET", status="200"}` | Multiple label filters |
| `rate(http_requests_total[5m])` | Per-second rate over 5 minutes |
| `increase(http_requests_total[1h])` | Total increase over 1 hour |
| `sum(rate(http_requests_total[5m])) by (status)` | Aggregate rate by status |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))` | 95th percentile latency |
| `avg(node_cpu_seconds_total{mode="idle"})` | Average CPU idle |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))` | CPU utilisation |

### Common Functions

| Function | Description | Example |
|----------|-------------|---------|
| `rate()` | Per-second average rate of increase | `rate(requests_total[5m])` |
| `irate()` | Per-second rate based on last two data points | `irate(requests_total[1m])` |
| `increase()` | Total increase over time range | `increase(errors_total[1h])` |
| `sum()` | Sum across series | `sum(rate(requests_total[5m])) by (service)` |
| `avg()` | Average across series | `avg(node_memory_usage)` |
| `histogram_quantile()` | Calculate quantile from histogram | `histogram_quantile(0.99, rate(duration_bucket[5m]))` |
| `topk()` | Top K series by value | `topk(5, rate(requests_total[5m]))` |
| `predict_linear()` | Linear prediction | `predict_linear(disk_usage[1h], 4*3600)` |
| `absent()` | Check if metric is missing | `absent(up{job="myapp"})` |

---

## Common Exporters

| Exporter | What It Monitors |
|----------|-----------------|
| **Node Exporter** | Linux/Unix host metrics (CPU, memory, disk, network) |
| **cAdvisor** | Container metrics (CPU, memory, network, filesystem) |
| **MySQL Exporter** | MySQL database metrics |
| **PostgreSQL Exporter** | PostgreSQL database metrics |
| **Redis Exporter** | Redis metrics |
| **Blackbox Exporter** | Probe endpoints over HTTP, HTTPS, DNS, TCP, ICMP |
| **SNMP Exporter** | Network device metrics via SNMP |
| **JSON Exporter** | Custom metrics from JSON APIs |

---

## Grafana

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Data source** | Connection to Prometheus (or other backends) |
| **Dashboard** | Collection of panels arranged in a layout |
| **Panel** | Single visualisation (graph, gauge, table, heatmap) |
| **Variable** | Dynamic filter for dashboards (e.g., select instance) |
| **Annotation** | Mark events on graphs (deployments, incidents) |
| **Alert rule** | Threshold-based alerting within Grafana |
| **Templating** | Reusable dashboard patterns with variables |

### Useful Dashboard Patterns

| Pattern | Description |
|---------|-------------|
| **Overview row** | Key metrics at a glance: error rate, latency, throughput |
| **Drill-down** | Click from summary to detailed view using variables |
| **RED method** | Rate, Errors, Duration — the three key service metrics |
| **USE method** | Utilisation, Saturation, Errors — for infrastructure |
| **Golden signals** | Latency, traffic, errors, saturation (Google's SRE book) |

---

## Alerting

### Alert Rule Structure

```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Alertmanager Routing

| Concept | Description |
|---------|-------------|
| **Group** | Combine similar alerts into one notification |
| **Route** | Tree of matchers that determines where alerts go |
| **Receiver** | Where to send alerts (email, Slack, PagerDuty, webhook) |
| **Inhibit** | Suppress alerts when another alert is firing |
| **Silence** | Temporarily mute alerts by label matcher |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **Target down** | Check if exporter is running; check network/firewall; verify scrape config |
| **No data** | Check metric name spelling; check label filters; verify time range |
| **High cardinality** | Too many label combinations; reduce label values; use recording rules |
| **Slow queries** | Use recording rules for complex queries; increase scrape interval |
| **Alert fatigue** | Tune thresholds; add `for` duration; group related alerts |
| **Missing metrics after restart** | Prometheus stores data locally; check retention settings |

---

## Summary

Prometheus monitors systems by scraping metrics from exporters at regular intervals. Metrics come in four types: counters (only go up), gauges (up and down), histograms (bucketed observations), and summaries (quantiles). PromQL is the query language — `rate()`, `increase()`, `histogram_quantile()`, and aggregation functions (`sum`, `avg`) are the most common operations. Grafana visualises Prometheus data in dashboards with panels, variables, and annotations. Alerting uses Alertmanager for grouping, routing, silencing, and inhibiting alerts. The key monitoring patterns are Google's golden signals (latency, traffic, errors, saturation) and the RED method (rate, errors, duration) for services and USE method (utilisation, saturation, errors) for infrastructure.
