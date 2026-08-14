---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, engineering, mlops, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# ML Engineering and MLOps

Building a machine learning model is only half the battle. Getting it into production, keeping it running reliably, monitoring for drift, and iterating on it — that's where ML engineering and MLOps come in. This file covers the full lifecycle from experiment to production system.

---

## The ML Lifecycle

| Phase | Description | Key Activities |
|-------|-------------|---------------|
| **1. Problem Definition** | Frame the business problem as an ML task | Define metrics, constraints, success criteria |
| **2. Data Collection** | Gather and label training data | ETL, labelling, augmentation |
| **3. Experimentation** | Train and evaluate models | Feature engineering, hyperparameter tuning |
| **4. Model Selection** | Choose the best model | Compare metrics, assess trade-offs |
| **5. Deployment** | Ship the model to production | Serving infrastructure, API, batch |
| **6. Monitoring** | Watch for drift and degradation | Data drift, concept drift, performance |
| **7. Retraining** | Update the model with new data | Scheduled or triggered retraining |

Most of the value (and difficulty) is in phases 5–7. A model sitting in a Jupyter notebook doesn't create business value.

---

## Model Serving Patterns

| Pattern | Description | Latency | Use Case |
|---------|-------------|---------|----------|
| **Batch Inference** | Run model on a batch of data on a schedule | Hours | Daily recommendations, fraud scoring |
| **Online Inference** | Real-time prediction per request | Milliseconds | Search ranking, real-time classification |
| **Streaming Inference** | Process predictions on a data stream | Seconds | Anomaly detection, event processing |

### Serving Infrastructure

| Tool | Type | Best For |
|------|------|----------|
| **TensorFlow Serving** | Model server | TensorFlow models |
| **TorchServe** | Model server | PyTorch models |
| **Triton Inference Server** | Multi-framework | GPU inference, multiple frameworks |
| **vLLM** | LLM serving | High-throughput LLM inference |
| **BentoML** | Unified serving | Framework-agnostic deployment |
| **Seldon** | K8s-native | Kubernetes model deployment |
| **Ray Serve** | Scalable serving | Large models, distributed inference |

---

## Model Registries

A model registry is a centralised store for managing ML models — their versions, metadata, metrics, and deployment status.

| Capability | Description |
|-----------|-------------|
| **Versioning** | Track every model version with unique ID |
| **Metadata** | Training data, hyperparameters, metrics, author |
| **Stage Transitions** | Move models through stages: Staging → Production → Archived |
| **Lineage** | Trace which data and code produced each model |

| Tool | Description |
|------|-------------|
| **MLflow** | Open-source; model registry + experiment tracking |
| **Weights & Biases (W&B)** | Commercial; experiment tracking + model registry |
| **DVC** | Data and model versioning with Git |
| **Azure ML / SageMaker** | Cloud-native model management |

---

## Experiment Tracking

Every ML experiment should be tracked: what data was used, what hyperparameters, what metrics resulted.

| Tool | Key Features |
|------|-------------|
| **MLflow** | Open-source, self-hosted, tracks params/metrics/artifacts |
| **W&B** | Rich UI, sweeps, artifact versioning, reports |
| **Neptune** | Metadata store for MLOps |
| **TensorBoard** | Built into TensorFlow; visualise training curves |

### What to Track

| Category | Examples |
|----------|---------|
| **Parameters** | Learning rate, batch size, model architecture, number of epochs |
| **Metrics** | Accuracy, loss, F1, AUC-ROC (per epoch and final) |
| **Artifacts** | Model weights, confusion matrices, prediction samples |
| **Data** | Dataset version, split ratios, preprocessing steps |
| **Environment** | Python version, library versions, hardware |

---

## Model Deployment Strategies

| Strategy | How It Works | Risk |
|----------|-------------|------|
| **Shadow Deployment** | New model runs alongside old; predictions compared but not served | Zero risk; validates before going live |
| **Canary Release** | Route small % of traffic to new model; increase gradually | Low risk; fast rollback |
| **A/B Testing** | Split users between old and new; compare business metrics | Measures actual impact |
| **Blue-Green** | Two identical environments; switch all traffic at once | Instant rollback; double cost during transition |
| **Feature Flags** | Toggle model on/off per user segment | Fine-grained control |

---

## Monitoring ML Systems

ML systems need more monitoring than traditional software because the data itself can change.

### Types of Drift

| Drift Type | What Changes | Example |
|-----------|-------------|---------|
| **Data Drift** | Input distribution changes | Customer demographics shift after a marketing campaign |
| **Concept Drift** | Relationship between input and output changes | Consumer behaviour changes during a recession |
| **Label Drift** | Target distribution changes | Fraud rate increases from 1% to 5% |

### What to Monitor

| Category | Metrics |
|----------|---------|
| **Model Performance** | Accuracy, precision, recall, F1, AUC (compared to baseline) |
| **Data Quality** | Missing values, feature distributions, outliers |
| **Drift Detection** | Statistical tests (KS test, PSI, KL divergence) |
| **Infrastructure** | Latency, throughput, GPU utilisation, memory |
| **Business Metrics** | Conversion rate, revenue impact, user satisfaction |

### Monitoring Tools

| Tool | Type |
|------|------|
| **Evidently AI** | Open-source data drift and model performance monitoring |
| **Grafana** | Dashboard visualisation (works with Prometheus) |
| **WhyLabs** | Data observability platform |
| **Arize** | ML observability and root cause analysis |
| **Prometheus + Grafana** | Infrastructure and application metrics |

---

## Reproducible Training

Reproducibility means you can re-run an experiment and get the same result. It's essential for debugging, auditing, and compliance.

### Requirements

| Requirement | How to Achieve It |
|-------------|-------------------|
| **Data versioning** | DVC, Delta Lake, or dataset snapshots with hashes |
| **Code versioning** | Git for all training code |
| **Environment pinning** | `requirements.txt`, `conda env`, Docker images with exact versions |
| **Seed setting** | Fix random seeds for numpy, torch, tensorflow |
| **Config management** | Hydra, OmegaConf, or YAML configs for all hyperparameters |
| **Artifact tracking** | MLflow or W&B to log every experiment |

---

## Scaling Inference

When a model needs to serve millions of requests per day, performance matters.

| Technique | Description |
|-----------|-------------|
| **Batching** | Group multiple requests into a single forward pass |
| **Quantisation** | Reduce model precision (FP32 → INT8 or INT4) for faster inference |
| **Model Distillation** | Train a smaller model to mimic a larger one |
| **Pruning** | Remove unimportant weights or neurons |
| **Caching** | Cache frequent predictions to avoid recomputation |
| **GPU Optimisation** | TensorRT, ONNX Runtime, Flash Attention |
| **Horizontal Scaling** | Run multiple model replicas behind a load balancer |

---

## Feature Flags for ML

Feature flags let you control which model version serves which users, without redeploying.

| Use Case | Description |
|----------|-------------|
| **Gradual rollout** | Serve new model to 5% of users, then increase |
| **Kill switch** | Instantly revert to previous model if issues detected |
| **Segment-based** | Different models for different user segments |
| **Experimentation** | A/B test model variants with business metrics |

Tools: LaunchDarkly, Unleash, Flagsmith, or simple database-backed feature flags.

---

## The MLOps Maturity Curve

| Level | Characteristics |
|-------|----------------|
| **Level 0 — Manual** | Manual training, manual deployment, no monitoring |
| **Level 1 — Experimentation** | Experiment tracking, model registry, basic CI |
| **Level 2 — Automation** | Automated retraining, CI/CD for models, automated testing |
| **Level 3 — Full Pipeline** | End-to-end automated pipeline with monitoring, drift detection, and auto-retraining |

Most organisations are somewhere between Level 0 and Level 1. The goal is Level 2–3, where the ML lifecycle is automated and self-healing.
