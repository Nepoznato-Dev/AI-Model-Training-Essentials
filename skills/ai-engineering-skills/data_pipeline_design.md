---
# Metadata
title: "Data Pipeline Design"
description: "Build robust, scalable data pipelines for ML training, validation, and inference workloads with proper error handling, monitoring, and reproducibility."
category: "AI Engineering Skills"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2026-08-10"
reviewed_by: "AI Engineering Skills Team"
next_review: "2027-02-10"

# Classification
tags: [data-pipelines, etl, data-engineering, ml-infrastructure, scalability]
difficulty_level: "intermediate"
prerequisites:
  - "Python programming"
  - "Basic understanding of ML training workflows"
estimated_reading_time: "20 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Data Pipeline Design

Build data pipelines that are reliable, reproducible, and scalable — handling real-world messiness while feeding clean data to ML training and inference systems.

## Overview

Data pipelines are the unsung infrastructure of ML systems. A well-designed pipeline transforms raw data into training-ready features reliably, handles failures gracefully, and produces consistent results across runs. A poorly designed one causes silent data corruption, irreproducible experiments, and 3 AM pages when it breaks.

This skill covers the architecture patterns, error handling strategies, and scalability considerations needed to build pipelines that work in production — not just in notebooks. It bridges the gap between "it runs on my machine" and "it processes 10M examples daily without intervention."

The core principle: **treat your data pipeline as production software, not a throwaway script.**

## Quick-Start Decision Tree

```
Building a data pipeline?
│
├─ Data volume?
│   ├─ < 10 GB → Single-machine, in-memory (Pandas/Polars)
│   ├─ 10–500 GB → Single-machine, chunked/streaming (Dask, Polars lazy)
│   └─ > 500 GB → Distributed (Spark, Ray Data)
│
├─ Pipeline complexity?
│   ├─ Linear (load → transform → save) → Simple script + validation
│   ├─ Branching (multiple outputs) → DAG orchestrator (Prefect, Airflow)
│   └─ Streaming (real-time) → Event-driven (Kafka + Flink)
│
└─ Reproducibility needs?
    ├─ Research/experiment → DVC + pinned versions
    └─ Production → Containerized + orchestrated + monitored
```

## Core Competencies

- **Architecture Selection**: Choose the right processing model (batch, streaming, micro-batch) and tools for your data volume and latency requirements
- **Error Handling**: Design pipelines that fail loudly on real errors and gracefully on transient issues — never silently produce wrong data
- **Data Validation**: Implement schema checks, distribution monitoring, and quality gates at each pipeline stage
- **Reproducibility**: Ensure the same input always produces the same output — versioned data, pinned dependencies, deterministic processing
- **Scalability**: Design for growth — start simple but architect so you can scale without rewriting
- **Monitoring**: Detect pipeline failures, data drift, and quality degradation before they affect model performance

## When to Use

- Building data ingestion and preprocessing for ML training
- Creating feature engineering pipelines that transform raw data into model inputs
- Designing inference pipelines that serve features to models in production
- Migrating notebook-based workflows to production systems
- Scaling data processing beyond single-machine memory limits

## Framework/Methodology

### Phase 1: Map the Data Flow

Before writing code, document what data flows where:

```
Raw Source          Processing Stages              Output
┌─────────┐       ┌──────────────────┐          ┌──────────┐
│ API /   │──────▶│ 1. Extract       │─────────▶│ Training │
│ Files / │       │ 2. Validate      │          │ Dataset  │
│ Stream  │       │ 3. Clean         │          └──────────┘
└─────────┘       │ 4. Transform     │          ┌──────────┐
                  │ 5. Feature Eng.  │─────────▶│ Validation│
                  │ 6. Split         │          │ Dataset  │
                  │ 7. Export        │          └──────────┘
                  └──────────────────┘          ┌──────────┐
                                                │ Test     │
                                                │ Dataset  │
                                                └──────────┘
```

For each stage, define:
- **Input**: What data enters this stage (format, schema, expected volume)
- **Output**: What data leaves this stage (format, schema, expected volume)
- **Failure mode**: What can go wrong, and what happens if it does

### Phase 2: Choose Processing Model

| Model | Latency | Throughput | Complexity | When to Use |
|-------|---------|------------|------------|-------------|
| Batch | Hours | Very high | Low | Daily/weekly retraining, offline analysis |
| Micro-batch | Minutes | High | Medium | Near-real-time features, periodic updates |
| Streaming | Milliseconds | Continuous | High | Real-time inference, live feature computation |

**Start with batch** unless you have a specific latency requirement that demands streaming. Batch is simpler, cheaper, and easier to debug. You can migrate to streaming later if needed.

### Phase 3: Build with Validation at Every Stage

The most dangerous pipeline bug is silent corruption — wrong data that looks right. Prevent this with validation gates.

**Validation layers:**

```python
# Layer 1: Schema validation (structure is correct)
def validate_schema(df, expected_schema):
    """Check columns, types, and required fields."""
    for col, dtype in expected_schema.items():
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
        if df[col].dtype != dtype:
            raise ValueError(f"Column {col}: expected {dtype}, got {df[col].dtype}")

# Layer 2: Range validation (values are plausible)
def validate_ranges(df, rules):
    """Check that values fall within expected ranges."""
    for col, (min_val, max_val) in rules.items():
        out_of_range = df[(df[col] < min_val) | (df[col] > max_val)]
        if len(out_of_range) > 0:
            pct = len(out_of_range) / len(df) * 100
            if pct > 5:  # More than 5% out of range = real problem
                raise ValueError(f"{col}: {pct:.1f}% values out of range [{min_val}, {max_val}]")

# Layer 3: Distribution validation (data looks statistically right)
def validate_distribution(df, col, expected_mean, expected_std, tolerance=3):
    """Check that data distribution hasn't shifted dramatically."""
    actual_mean = df[col].mean()
    if abs(actual_mean - expected_mean) > tolerance * expected_std:
        raise Warning(f"{col} distribution may have shifted: mean={actual_mean:.2f}, expected={expected_mean:.2f}")
```

### Phase 4: Handle Failures Intentionally

**Failure handling strategies:**

| Strategy | When to Use | Example |
|----------|-------------|---------|
| Fail fast | Schema violations, missing required data | Missing column → stop pipeline, alert |
| Retry with backoff | Transient network/API errors | API timeout → retry 3x with exponential backoff |
| Skip and log | Corrupt individual records in large dataset | Malformed JSON line → log and skip, continue processing |
| Fallback | External service unavailable | Embedding API down → use cached embeddings from last run |
| Dead letter queue | Records that need manual review | Ambiguous classifications → send to review queue |

**Anti-pattern**: Catching all exceptions and continuing silently.
```python
# BAD — hides real problems
try:
    process(record)
except Exception:
    pass  # Never do this

# GOOD — specific handling
try:
    process(record)
except json.JSONDecodeError as e:
    logger.warning(f"Malformed record at line {line_num}: {e}")
    dead_letter_queue.put(record, error=str(e))
except ConnectionError:
    raise  # Re-raise transient errors for retry logic
```

### Phase 5: Ensure Reproducibility

**Reproducibility requirements:**
1. **Pin data versions** — Use hashes or DVC to track exact input data
2. **Pin code versions** — Git commit hash for all processing code
3. **Pin dependencies** — requirements.txt or lock file with exact versions
4. **Deterministic operations** — Set seeds, use sorted operations where order matters
5. **Document environment** — Python version, OS, hardware configuration

```python
# Reproducible pipeline configuration
PIPELINE_CONFIG = {
    "version": "1.2.0",
    "data_hash": "sha256:abc123...",  # Input data fingerprint
    "code_commit": "git:main@a1b2c3d",
    "python_version": "3.11.5",
    "seed": 42,
    "dependencies": "requirements_2026_08_10.txt",
}
```

### Phase 6: Monitor in Production

**What to monitor:**

| Signal | Alert Threshold | Action |
|--------|----------------|--------|
| Pipeline duration | >2x normal runtime | Check for data volume spike or resource contention |
| Record count | >10% deviation from expected | Check source for missing data or duplicates |
| Null rate | >5% in previously clean columns | Source schema change or upstream bug |
| Feature distribution | Mean shifts >3σ from baseline | Data drift — may need model retraining |
| Error rate | >1% of records failing | Upstream quality issue or code bug |

## Practical Templates

### Template 1: Pipeline Stage Definition

```python
class PipelineStage:
    """Base class for pipeline stages with built-in validation and logging."""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(f"pipeline.{name}")
    
    def validate_input(self, data):
        """Override to add input validation."""
        pass
    
    def process(self, data):
        """Override with transformation logic."""
        raise NotImplementedError
    
    def validate_output(self, data):
        """Override to add output validation."""
        pass
    
    def run(self, data):
        """Execute stage with validation and logging."""
        self.logger.info(f"Starting stage: {self.name}")
        self.validate_input(data)
        
        result = self.process(data)
        
        self.validate_output(result)
        self.logger.info(
            f"Completed stage: {self.name} | "
            f"Input records: {len(data)} | Output records: {len(result)}"
        )
        return result
```

### Template 2: Pipeline Configuration

```yaml
# pipeline_config.yaml
pipeline:
  name: "training_data_preparation"
  version: "1.0.0"
  
stages:
  - name: "extract"
    source:
      type: "s3"
      bucket: "raw-data"
      prefix: "contracts/2026/"
    validation:
      min_records: 1000
      required_columns: ["id", "text", "metadata", "created_at"]
  
  - name: "clean"
    operations:
      - remove_duplicates: true
      - handle_nulls:
          strategy: "drop"  # or "impute"
          columns: ["text"]
      - normalize_text:
          lowercase: true
          strip_whitespace: true
  
  - name: "transform"
    operations:
      - tokenize:
          method: "sentencepiece"
          model: "models/tokenizer_v2.model"
      - encode_labels:
          mapping: "configs/label_mapping.json"
  
  - name: "split"
    strategy: "stratified"
    ratios: {train: 0.8, val: 0.1, test: 0.1}
    stratify_by: "domain"
    seed: 42
  
  - name: "export"
    format: "parquet"
    output_dir: "s3://processed-data/training/"
    compression: "snappy"

monitoring:
  alert_channels: ["slack:#ml-pipelines", "email:ml-team@company.com"]
  duration_threshold_multiplier: 2.0
  record_count_deviation_pct: 10
```

### Template 3: Data Quality Report

```markdown
# Data Quality Report: [Pipeline Name]
Date: [YYYY-MM-DD]
Run ID: [unique identifier]

## Summary
- Total records processed: [N]
- Records passed validation: [N] ([%])
- Records failed/rejected: [N] ([%])
- Processing time: [duration]
- Output location: [path]

## Validation Results
| Stage | Input | Output | Rejected | Notes |
|-------|-------|--------|----------|-------|
| Extract | | | | |
| Clean | | | | |
| Transform | | | | |
| Split | | | | |

## Distribution Check
| Feature | Expected Mean | Actual Mean | Shift | Status |
|---------|--------------|-------------|-------|--------|
| | | | | OK / WARNING / ALERT |

## Issues Found
1. [Description of any issues]
2. [Recommended action]

## Sign-off
- Pipeline operator: [Name]
- Data owner: [Name]
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| No validation between stages | Silent corruption propagates through pipeline | Add schema + range checks at every stage boundary |
| Non-deterministic processing | Different results each run, irreproducible experiments | Pin seeds, sort operations, version everything |
| Processing all data in memory | Crashes on large datasets | Use streaming/chunked processing from the start |
| Catching all exceptions silently | Wrong data looks right, discovered only in production | Fail fast on unexpected errors, only skip known-bad records |
| No monitoring on pipeline health | Failures discovered by downstream model degradation | Monitor duration, record count, null rate, distribution |
| Hardcoding paths and configurations | Can't reproduce, can't parameterize | Use configuration files, environment variables |
| Skipping the dead letter queue | Bad records lost forever, can't analyze failure patterns | Always route rejected records somewhere inspectable |

## Best Practices

1. **Start simple, scale when needed.** A well-structured Pandas pipeline handles most use cases under 10 GB. Don't adopt Spark until you genuinely need it.

2. **Make failures visible.** A pipeline that silently produces wrong output is worse than one that crashes. Fail loudly, log context, and route bad records to a review queue.

3. **Version your data and code together.** A pipeline is only reproducible if both the processing code and the input data are versioned and pinned.

4. **Test with edge cases before production.** Include null inputs, empty files, malformed records, and extremely large inputs in your test suite.

5. **Log record counts at every stage.** If a stage receives 10,000 records and outputs 9,990, you need to know why 10 were dropped — is that expected filtering or a bug?

6. **Design for idempotency.** Running the same pipeline twice on the same input should produce identical output. This makes recovery from failures trivial — just re-run.

7. **Separate orchestration from logic.** Pipeline stages should be testable independently. The orchestrator (Airflow, Prefect, or a simple script) handles ordering and retry; stages handle transformation.

## Tools & Resources

### Processing Frameworks
- **[Polars](https://pola.rs/)** - Fast DataFrame library with lazy evaluation and streaming support
- **[Dask](https://www.dask.org/)** - Parallel computing for analytics at scale, Pandas-compatible API
- **[Ray Data](https://docs.ray.io/en/latest/data/data.html)** - Distributed data processing for ML workloads
- **[Apache Spark](https://spark.apache.org/)** - Large-scale distributed data processing

### Orchestration
- **[Prefect](https://www.prefect.io/)** - Modern workflow orchestration with Pythonic API
- **[Apache Airflow](https://airflow.apache.org/)** - Industry-standard DAG-based orchestration
- **[Dagster](https://dagster.io/)** - Software-defined data orchestration with strong typing

### Data Validation
- **[Great Expectations](https://greatexpectations.io/)** - Data quality validation and documentation
- **[Pandera](https://pandera.readthedocs.io/)** - Statistical data validation for DataFrames
- **[Evidently](https://www.evidentlyai.com/)** - Data quality and drift monitoring for ML

### Data Versioning
- **[DVC](https://dvc.org/)** - Data version control integrated with Git
- **[LakeFS](https://lakefs.io/)** - Git-like versioning for data lakes
- **[Delta Lake](https://delta.io/)** - Storage layer with ACID transactions and time travel

## Example Application

**Scenario**: An ML team needs a pipeline that processes 2M customer support tickets daily into training data for a classification model. The raw data comes from multiple sources (API, database, file uploads) with inconsistent formats.

**Application**:

1. **Extract**: Three source connectors pull data into a unified schema. Each connector has its own retry logic and error handling. Failed extractions are logged and retried up to 3 times.

2. **Validate**: Schema validation catches 0.3% of records with missing required fields. These go to the dead letter queue for manual review. Range validation flags 2% of records with unusual text lengths — investigation reveals a source system bug, not a pipeline issue.

3. **Clean**: Deduplication by ticket ID removes 5% of records. Text normalization (Unicode, whitespace, encoding) standardizes the remaining 1.9M records.

4. **Transform**: Tokenization and label encoding produce training-ready features. Feature validation checks that embedding distributions haven't shifted.

5. **Split**: Stratified split by issue category (80/10/10) with seed pinning for reproducibility.

6. **Export**: Parquet format with Snappy compression. Output: ~800 MB training set, ~100 MB each for val and test.

**Monitoring**: Daily Slack report shows record counts, processing time, rejection rates, and distribution checks. Alert triggers if any metric deviates >2x from 7-day average.

**Outcome**: Pipeline processes 2M records in 45 minutes on a single machine. Data quality issues are caught within hours, not weeks. The model team trusts the data because they can see validation results daily.

## Success Indicators

You've mastered data pipeline design when you can:

- Choose the right processing model (batch vs streaming) based on requirements, not hype
- Build pipelines that fail loudly on real errors and gracefully on transient ones
- Implement validation that catches silent data corruption before it reaches models
- Reproduce any past pipeline run from your versioning and logging
- Monitor pipeline health proactively, not reactively
- Scale from prototype to production without rewriting from scratch

## Related Skills

- [Model Fine-Tuning](model_fine_tuning.md) - Consuming pipeline output for model training
- [Experiment Design](experiment_design.md) - Using pipelines for reproducible experiments
- [Data Analysis](../data-skills/data_analysis.md) - Exploratory analysis that feeds pipeline design
- [CI/CD](../devops-skills/ci_cd.md) - Deploying and updating pipelines reliably
- [Experiment Tracking](../data-skills/experiment_tracking.md) - Logging pipeline runs as experiments
