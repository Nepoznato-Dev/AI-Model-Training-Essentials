---
# Metadata
title: "Data Pipeline and ETL Failures"
description: "Schema drift, duplicate data, validation gaps, pipeline monitoring"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, pipeline, etl, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Data Pipeline and ETL Failures

Data pipelines are the plumbing of modern organisations — they move data from source systems through transformations into the databases, warehouses, and lakes where it's used for analytics, machine learning, and decision-making. When they work, nobody notices. When they fail, decisions are made on stale data, models train on garbage, reports show impossible numbers, and trust in the entire data platform erodes. Data pipeline failures are among the most common and most costly failures in technology organisations.

---

## Common Failure Modes

### Data Quality Issues

| Failure | Description | Impact | Detection Difficulty |
|---------|-------------|--------|---------------------|
| **Silent data corruption** | Data is modified incorrectly without any error being raised | Downstream systems trust bad data; decisions based on false information | Very hard — no error signal |
| **Schema drift** | Source system changes schema (adds, removes, renames columns) | Pipeline breaks or silently drops data | Medium — pipeline may fail or produce partial results |
| **Data type mismatch** | Source sends string where integer expected; float precision changes | Pipeline fails; data truncated; rounding errors | Medium — may cause pipeline error or subtle data issues |
| **Duplicate records** | Same event processed multiple times | Inflated counts; incorrect aggregations | Hard — each record looks valid individually |
| **Null / missing values** | Expected fields are empty | Calculations fail; models produce wrong predictions | Medium — depends on null handling |
| **Out-of-range values** | Values outside expected bounds (negative ages; future dates) | Skewed statistics; broken business logic | Medium — requires validation rules |
| **Late-arriving data** | Data arrives after the processing window has closed | Incomplete results; missed records | Hard — results look complete but aren't |

### Pipeline Infrastructure Issues

| Failure | Description | Impact |
|---------|-------------|--------|
| **Orchestration failure** | Scheduler (Airflow, Prefect) doesn't trigger the pipeline | Data is stale; no processing occurs |
| **Resource exhaustion** | Pipeline runs out of memory, CPU, or disk | Pipeline crashes; partial results |
| **Dependency failure** | Upstream system is down or slow | Pipeline waits indefinitely or fails |
| **Concurrency issues** | Multiple pipelines modify the same data simultaneously | Race conditions; data corruption |
| **Configuration drift** | Environment changes (network, credentials, endpoints) not reflected in pipeline | Pipeline fails unexpectedly |
| **Backpressure** | Data arrives faster than the pipeline can process | Growing queues; increasing latency |

---

## Case Studies

### Case Study 1: Silent Data Duplication

| Aspect | Description |
|--------|-------------|
| **Scenario** | An e-commerce company's order pipeline processes events from a message queue |
| **What went wrong** | A consumer restart caused messages to be re-consumed; no deduplication logic existed |
| **Impact** | Revenue figures were inflated by 15% for 3 weeks before anyone noticed |
| **Root cause** | No idempotency keys; at-least-once delivery without deduplication |
| **Fix** | Added idempotency keys based on order ID; implemented exactly-once semantics |
| **Lesson** | At-least-once delivery requires deduplication; always validate totals against source systems |

### Case Study 2: Schema Change Breaks Downstream

| Aspect | Description |
|--------|-------------|
| **Scenario** | A payment provider changes a field name in their API response |
| **What went wrong** | The ETL pipeline silently started writing null values; no schema validation |
| **Impact** | Financial reports showed zero revenue from that payment method for 2 months |
| **Root cause** | No schema validation at ingestion; null values treated as valid |
| **Fix** | Added schema validation with alerts; required fields enforced; null checks |
| **Lesson** | Never trust external schemas to remain stable; validate at the boundary |

### Case Study 3: Time Zone Catastrophe

| Aspect | Description |
|--------|-------------|
| **Scenario** | A global company aggregates daily metrics across offices |
| **What went wrong** | Some sources used UTC, others used local time; pipeline didn't normalise |
| **Impact** | Daily totals didn't match; some transactions counted in wrong day; month-end close was wrong |
| **Root cause** | No standard time zone policy; timestamps stored inconsistently |
| **Fix** | All timestamps stored as UTC; conversion to local time only at presentation layer |
| **Lesson** | Standardise on UTC everywhere; be explicit about time zones at every boundary |

---

## Prevention Strategies

### Data Validation

| Strategy | Description | Tool Examples |
|----------|-------------|---------------|
| **Schema validation** | Verify data matches expected schema at each stage | Great Expectations; Deequ; Soda |
| **Range checks** | Values fall within expected bounds | Custom assertions; dbt tests |
| **Freshness checks** | Data is recent enough to be useful | Monitoring timestamps; SLA alerts |
| **Volume checks** | Row counts are within expected range | Anomaly detection on row counts |
| **Referential integrity** | Foreign keys match; no orphaned records | SQL constraints; data quality tools |
| **Cross-source reconciliation** | Totals match between source and target | Automated reconciliation jobs |

### Pipeline Design Patterns

| Pattern | Description | Benefit |
|---------|-------------|---------|
| **Idempotency** | Running the pipeline multiple times produces the same result | Safe to retry; no duplicates |
| **Atomicity** | Pipeline either fully succeeds or fully fails (no partial state) | No half-processed data |
| **Checkpointing** | Save progress at each stage; resume from last checkpoint | Fault tolerance; no reprocessing |
| **Dead letter queues** | Failed records go to a separate queue for investigation | No data loss; can investigate and replay |
| **Circuit breakers** | Stop processing when downstream is failing | Prevent cascading failures |
| **Data contracts** | Agreement between producers and consumers about data format | Schema changes are coordinated |

### Monitoring and Alerting

| What to Monitor | Why | How |
|-----------------|-----|-----|
| **Pipeline duration** | Increasing duration signals problems | Trend analysis; SLA tracking |
| **Row counts** | Sudden changes indicate problems | Compare with historical averages |
| **Null rates** | Increasing nulls signal schema or source issues | Column-level null tracking |
| **Data freshness** | Stale data means pipeline isn't running | Timestamp of latest record |
| **Downstream impact** | Are reports and models using correct data? | End-to-end data lineage |
| **Resource usage** | CPU; memory; disk; network | Infrastructure monitoring |

---

## Recovery Strategies

| Situation | Strategy |
|-----------|----------|
| **Bad data already in warehouse** | Identify affected time range; reprocess from source; notify downstream consumers |
| **Pipeline failure mid-run** | Idempotent design allows safe re-run; checkpointing allows resume |
| **Schema change broke pipeline** | Fix transformation; backfill affected data; add schema evolution handling |
| **Silent corruption discovered late** | Root cause analysis; determine blast radius; reprocess; add monitoring to catch recurrence |
| **Data loss** | Restore from backup; replay from source; assess whether loss is recoverable |

---

## Summary

Data pipeline failures are ubiquitous and often more costly than application outages because they produce wrong answers rather than obvious errors. Silent data corruption, schema drift, duplicates, time zone bugs, and missing values are the most common culprits. The key prevention strategies are: validate data at every boundary (schema, range, volume, freshness); design pipelines to be idempotent and atomic; monitor everything (duration, row counts, null rates, freshness); use dead letter queues for failed records; and establish data contracts between producers and consumers. When failures occur, the response should include root cause analysis, reprocessing of affected data, notification of downstream consumers, and — critically — adding monitoring to catch the same class of failure in the future. The organisations that get this right treat data pipelines with the same rigour as production software: testing, monitoring, alerting, incident response, and post-mortems.
