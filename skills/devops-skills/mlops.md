---
# Metadata
title: "MLOps"
description: "Practices for deploying, monitoring, versioning, and maintaining machine learning models in production reliably and at scale."
category: "DevOps Skills"
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
reviewed_by: "DevOps Skills Team"
next_review: "2027-02-10"

# Classification
tags: [mlops, model-deployment, model-monitoring, ml-pipelines, model-versioning, production-ml]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# MLOps

The discipline of operationalizing machine learning models — covering deployment, monitoring, versioning, retraining, and governance in production environments.

## Overview

MLOps extends DevOps principles to the unique challenges of machine learning systems. Unlike traditional software, ML systems carry three moving parts: code, data, and the model itself. Any of these can change independently, and all three must be tracked, tested, and orchestrated together.

MLOps bridges the gap between a model that works in a notebook and a model that serves millions of requests reliably. It addresses model versioning, reproducible training pipelines, automated deployment, data drift detection, performance monitoring, and the governance structures needed when models affect real users.

As organizations move from ML experiments to ML-powered products, MLOps becomes the operational backbone that prevents models from silently degrading, breaking downstream systems, or producing harmful outputs in production.

## Core Competencies

- Designing reproducible ML pipelines from data ingestion to model serving
- Implementing model versioning and artifact management strategies
- Deploying models with zero-downtime deployment patterns (blue-green, canary, shadow)
- Monitoring model performance, data drift, and concept drift in production
- Automating retraining triggers and CI/CD for ML pipelines
- Managing feature stores and serving infrastructure
- Establishing ML governance, audit trails, and model cards

## When to Use

- Moving an ML model from development into a production serving environment
- Setting up infrastructure to monitor model health over time
- Building automated retraining pipelines triggered by data changes
- Managing multiple model versions across environments (staging, production)
- Establishing governance and compliance processes for ML systems
- Scaling ML infrastructure to handle growing data volumes or request rates
- Debugging production model issues such as silent accuracy degradation

## Framework/Methodology

### Phase 1: Pipeline Design

A production ML pipeline has five stages:

1. **Data Ingestion** — Pull from source systems, validate schema, check for anomalies
2. **Preprocessing** — Apply consistent transformations (must be identical in training and serving)
3. **Training** — Run on versioned data with tracked hyperparameters and code
4. **Evaluation** — Validate against held-out test set and comparison baseline
5. **Deployment** — Package model + preprocessing + dependencies into a deployable artifact

Each stage must be idempotent, cacheable, and independently testable.

### Phase 2: Artifact & Version Management

Track three artifacts together for every experiment:

| Artifact | What to Track | Tool Examples |
|----------|---------------|---------------|
| Code | Git commit hash, branch, config files | Git, DVC |
| Data | Dataset hash, schema version, split ratios | DVC, Delta Lake, Pachyderm |
| Model | Model weights, hyperparameters, metrics, framework version | MLflow, Weights & Biases, Neptune |

The golden rule: given any artifact version, you must be able to reproduce the exact model that was trained.

### Phase 3: Deployment Strategy

Choose a deployment pattern based on risk tolerance:

- **Rolling update** — Replace instances gradually. Simple but offers no rollback if the new model is worse.
- **Blue-green** — Run old and new models in parallel environments; switch traffic instantly. Fast rollback.
- **Canary** — Route a small percentage of traffic to the new model. Compare metrics before full rollout.
- **Shadow** — New model receives all traffic but responses are discarded. Compare outputs against the current model with zero user impact.

For ML models specifically, canary and shadow deployments are strongly preferred because model quality can only be assessed against live traffic distributions.

### Phase 4: Monitoring & Drift Detection

Monitor four categories of metrics:

1. **System metrics** — Latency, throughput, memory, GPU utilization
2. **Data drift** — Statistical divergence between training and serving input distributions (PSI, KL divergence, Wasserstein distance)
3. **Concept drift** — Change in the relationship between inputs and outputs (accuracy degradation over time)
4. **Output distribution** — Shift in prediction distributions (e.g., a classifier suddenly predicting one class 90% of the time)

Set alerts on drift metrics with thresholds calibrated from your validation data.

### Phase 5: Retraining & Lifecycle

Define retraining strategy:

- **Scheduled** — Retrain every N days/weeks regardless of need
- **Trigger-based** — Retrain when drift exceeds threshold, or when new labeled data arrives
- **Continuous** — Online learning or incremental updates on every batch

Document the model lifecycle: development → staging → production → archived → deprecated.

## Practical Templates

### Template 1: Model Card

```markdown
# Model Card: [Model Name]

## Overview
- **Task**: [classification / regression / generation / ...]
- **Input**: [description of input data]
- **Output**: [description of output format]
- **Framework**: [PyTorch / TensorFlow / ...] v[version]

## Training
- **Dataset**: [name, version, size, date range]
- **Preprocessing**: [link to preprocessing code version]
- **Hyperparameters**: [learning rate, batch size, epochs, ...]
- **Training time**: [hours on hardware type]

## Evaluation
| Metric | Value | Test Set | Baseline |
|--------|-------|----------|----------|
| Accuracy | 0.94 | v2.1 test | 0.91 (v3.2) |
| F1 Score | 0.92 | v2.1 test | 0.89 (v3.2) |

## Limitations
- [Known failure modes, demographic biases, out-of-distribution behavior]

## Deployment
- **Serving format**: [ONNX / TorchScript / TF SavedModel]
- **Hardware**: [GPU type / CPU / edge device]
- **Latency SLA**: [p50 / p99 in milliseconds]
- **Owner**: [team or individual]
```

### Template 2: Drift Monitoring Configuration

```yaml
# drift_monitor.yaml
model_name: "customer_classifier_v4"
monitor:
  schedule: "every 6 hours"
  metrics:
    - name: "feature_psi"
      type: "population_stability_index"
      reference: "s3://artifacts/train_data_v4.parquet"
      threshold: 0.2
      features: ["age", "income", "tenure", "usage_score"]
    - name: "prediction_drift"
      type: "distribution_comparison"
      reference: "s3://artifacts/train_predictions_v4.parquet"
      threshold: 0.15
      method: "kolmogorov_smirnov"
  actions:
    - condition: "any_metric_exceeded"
      notify: ["ml-team@company.com", "pagerduty:ml-critical"]
    - condition: "psi > 0.3"
      trigger: "retraining_pipeline"
      params:
        max_training_hours: 12
        evaluation_set: "s3://artifacts/eval_set_latest.parquet"
```

### Template 3: CI/CD Pipeline for ML

```yaml
# .github/workflows/ml-pipeline.yml
name: ML Training Pipeline
on:
  push:
    paths: ["training/**", "data/schema.yaml"]

jobs:
  validate-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate data schema
        run: python scripts/validate_schema.py --data data/latest/
      - name: Check for data drift
        run: python scripts/drift_check.py --reference data/baseline.parquet

  train:
    needs: validate-data
    runs-on: gpu-runner
    steps:
      - uses: actions/checkout@v4
      - name: Train model
        run: python training/train.py --config configs/default.yaml
      - name: Log to MLflow
        run: python scripts/log_experiment.py --run-id ${{ github.sha }}
      - name: Evaluate
        run: python training/evaluate.py --model outputs/model/ --test data/test.parquet
      - name: Check quality gate
        run: python scripts/quality_gate.py --min-accuracy 0.90 --min-f1 0.85

  deploy-staging:
    needs: train
    runs-on: ubuntu-latest
    steps:
      - name: Package model
        run: python scripts/package_model.py --format onnx
      - name: Deploy to staging
        run: ./scripts/deploy.sh --env staging --model outputs/model.onnx
      - name: Run integration tests
        run: python tests/integration/test_model_endpoint.py --env staging

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
      - name: Canary deploy (10% traffic)
        run: ./scripts/deploy.sh --env production --canary 10 --model outputs/model.onnx
      - name: Monitor canary (30 min)
        run: python scripts/monitor_canary.py --duration 1800 --latency-threshold 200
      - name: Promote to full
        run: ./scripts/deploy.sh --env production --promote
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Training-serving skew | Model works in notebooks but fails in production | Use identical preprocessing code in both paths; validate with integration tests |
| No model versioning | Cannot reproduce or roll back a deployed model | Track model artifacts with experiment tracking tools from day one |
| Monitoring only system metrics | Silent accuracy degradation goes undetected | Monitor prediction distributions and drift metrics alongside latency |
| Manual deployment steps | Human error, irreproducible releases | Automate the full pipeline from validated data to deployed model |
| Ignoring data quality | Garbage in, garbage out at scale | Add data validation as the first pipeline stage with schema and statistical checks |
| Retraining on a fixed schedule regardless of need | Wasted compute or stale models | Use drift-triggered retraining with a scheduled fallback |

## Best Practices

1. **Treat models as artifacts, not scripts.** Every model should be reproducible from a specific commit, dataset version, and hyperparameter config.
2. **Validate data before training.** Schema checks, statistical range checks, and null-rate checks catch data pipeline bugs before they corrupt models.
3. **Separate model development from model serving.** Data scientists iterate in notebooks; serving infrastructure runs containerized model servers.
4. **Implement quality gates.** No model deploys without meeting minimum metric thresholds on a held-out evaluation set.
5. **Log everything.** Every training run, deployment, and inference request should produce structured logs for debugging and auditing.
6. **Plan for model retirement.** Define criteria for when a model is deprecated and how traffic transitions to its replacement.
7. **Use feature stores for shared feature logic.** When multiple models consume the same features, a feature store prevents inconsistent preprocessing across teams.

## Tools & Resources

- [MLflow](https://mlflow.org/) - Experiment tracking, model registry, and deployment management
- [Weights & Biases](https://wandb.ai/) - Experiment tracking, dataset versioning, and model evaluation
- [Kubeflow](https://www.kubeflow.org/) - ML pipeline orchestration on Kubernetes
- [DVC (Data Version Control)](https://dvc.org/) - Git-like version control for datasets and model artifacts
- [Feast](https://feast.dev/) - Open-source feature store for ML
- [Evidently AI](https://www.evidentlyai.com/) - Data drift and model monitoring
- [Google MLOps Whitepaper](https://cloud.google.com/architecture/mlops-continuous-delivery-pipeline-machine-learning-models) - Foundational reference on MLOps maturity levels
- [Made With ML - MLOps Course](https://madewithml.com/) - Practical MLOps course covering the full lifecycle

## Example Application

**Scenario**: A fintech company has a fraud detection model that achieved 96% accuracy during development. After three months in production, the fraud team notices that false positives have increased 3x, but no one caught it because overall accuracy still looks acceptable.

**Application**:

1. *Root cause* — The model was trained on pre-pandemic transaction patterns. Consumer behavior shifted, causing concept drift that accuracy alone couldn't detect (the class distribution changed, masking the degradation).

2. *Fix: monitoring* — Deploy drift detection monitoring both feature distributions (PSI on transaction amount, merchant category, time-of-day) and prediction distributions (alert if fraud probability > 0.8 for more than 5% of transactions).

3. *Fix: evaluation* — Add precision and recall as tracked production metrics, not just accuracy. Set up separate alerts for recall degradation (missed fraud is more costly than false alarms).

4. *Fix: pipeline* — Implement a trigger-based retraining pipeline that activates when PSI exceeds 0.2 on any critical feature, pulling the latest 90 days of labeled data.

5. *Governance* — Create a model card documenting known limitations, drift monitoring configuration, and retraining SLA (within 48 hours of trigger).

**Outcome**: Drift is detected within 6 hours instead of 3 months. Retraining completes automatically, reducing false positives back to baseline within two days. The model card ensures new team members understand the model's behavior and monitoring setup.

## Success Indicators

You know you've mastered MLOps when:

- Every production model has a model card with documented limitations and monitoring
- You can reproduce any deployed model from its artifact (code + data + config) within one hour
- Drift alerts fire before users notice model degradation
- Retraining pipelines run automatically without manual intervention
- Model deployments use canary or shadow patterns with automated rollback
- Your team can explain the full lifecycle of any model from training to retirement
- Compliance audits pass because every model change is logged and traceable

## Related Skills

- [CI/CD](ci_cd.md) - Core CI/CD practices that MLOps extends with model-specific stages
- [Container Orchestration](container_orchestration.md) - Kubernetes patterns for serving models at scale
- [Infrastructure as Code](infrastructure_as_code.md) - Reproducible infrastructure for ML environments
- [Data Analysis](../data-skills/data_analysis.md) - Understanding data distributions is essential for drift detection
