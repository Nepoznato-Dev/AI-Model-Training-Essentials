---
# Metadata
title: "Machine Learning Project Failures"
description: "Data leakage, expectation mismatches, deployment failures, model decay"
category: "Lessons from Failures"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, project, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Machine Learning Project Failures

Machine learning projects fail at an alarming rate — industry estimates suggest 60-85% of ML projects never reach production. The failures aren't usually in the algorithms; they're in the process, the data, the expectations, and the organisational context. Understanding why ML projects fail is essential for anyone building ML systems, because the failure modes are predictable and largely avoidable.

---

## Why ML Projects Fail

### Failure Categories

| Category | Share of Failures | Description |
|----------|------------------|-------------|
| **Data problems** | ~30% | Data is insufficient, biased, stale, or inaccessible |
| **Problem definition** | ~20% | The ML problem doesn't match the business need |
| **Expectation mismatch** | ~15% | Stakeholders expect magic; reality is incremental improvement |
| **Deployment failure** | ~15% | Model works in notebooks but can't be productionised |
| ** organisational issues** | ~10% | No clear ownership; team lacks skills; no executive support |
| **Model performance** | ~10% | Model doesn't achieve required accuracy or generalises poorly |

---

## Data-Related Failures

### Common Data Problems

| Problem | Description | Example |
|---------|-------------|---------|
| **Insufficient data** | Not enough examples to learn meaningful patterns | Training a fraud detection model on 500 transactions |
| **Label quality** | Training labels are wrong, inconsistent, or subjective | Medical images labelled by non-experts; sentiment labels with low inter-rater agreement |
| **Data leakage** | Information from the future or target leaks into features | Using customer churn outcome as a feature; including test data in training |
| **Selection bias** | Training data doesn't represent the deployment population | Training a medical model on data from one hospital; deploying nationally |
| **Concept drift** | The relationship between features and target changes over time | Consumer behaviour changes after a pandemic; model trained on pre-pandemic data |
| **Feature mismatch** | Features available during training differ from those available in production | Training with manual labels; production uses automated labels with different distribution |
| **Class imbalance** | Target classes are highly skewed | 99% negative, 1% positive; model learns to always predict negative |

### The Data Leakage Problem

| Type | Description | Example |
|------|-------------|---------|
| **Target leakage** | A feature is only available after the target occurs | "Treatment outcome" used as a feature to predict "treatment success" |
| **Train-test contamination** | Test data influences training | Scaling with global statistics (includes test data); data augmentation that leaks |
| **Sampling bias** | Training and production use different sampling | Training on web traffic; deploying on mobile app traffic |
| **Pre-processing leakage** | Preprocessing step uses information from the full dataset | Imputing missing values with the global mean (includes test data) |

---

## Problem Definition Failures

### Misalignment Patterns

| Pattern | Description | Consequence |
|---------|-------------|-------------|
| **Solving the wrong problem** | Business needs X; team builds Y | Model is technically good but useless |
| **ML when rules would suffice** | Problem has deterministic rules; ML adds complexity | Over-engineered; harder to maintain; less interpretable |
| **ML when data doesn't exist** | Problem requires data that hasn't been collected | Project can't start; months wasted on feasibility |
| **Accuracy target without business context** | "We need 95% accuracy" — but what does that mean for the business? | Model meets accuracy but doesn't solve the business problem |
| **Ignoring the cost of errors** | False positives and false negatives have different costs | Model optimises the wrong metric |
| **No baseline** | No comparison to existing approach | Can't tell if ML is actually better than a simple heuristic |

---

## Expectation Failures

### The Hype Cycle in ML Projects

| Phase | Description | Risk |
|-------|-------------|------|
| **Excitement** | "AI will solve everything!" | Over-promising; under-resourcing |
| **Proof of concept** | Model works on clean data in notebooks | False confidence; "it works!" |
| **Reality check** | Production data is messy; performance drops | Disappointment; "ML doesn't work" |
| **Death march** | Team tries to force it into production | Technical debt; burnout |
| **Abandonment or quiet deployment** | Project cancelled or deployed with no monitoring | Wasted investment |

### Managing Expectations

| Strategy | Description |
|----------|-------------|
| **Start with a baseline** | Compare against the simplest possible approach (rules; human performance) |
| **Define success metrics upfront** | Business metrics (revenue; cost savings) not just ML metrics (accuracy; F1) |
| **Time-box exploration** | Give the team 2-4 weeks to assess feasibility before committing |
| **Show what ML can't do** | Be honest about limitations; set realistic expectations |
| **Iterate incrementally** | Deploy a simple model first; improve iteratively |
| **Quantify the cost of errors** | Translate model performance into business impact |

---

## Deployment Failures

### Why Models Don't Make It to Production

| Problem | Description | Solution |
|---------|-------------|----------|
| **Notebook to production gap** | Code works in Jupyter but isn't production-ready | MLOps practices; CI/CD for ML; code review |
| **Latency requirements** | Model inference is too slow for real-time use | Model optimisation; quantisation; caching |
| **Scalability** | Model can't handle production traffic | Batch processing; horizontal scaling; model serving infrastructure |
| **Monitoring gaps** | No way to detect when model degrades | Data drift monitoring; performance monitoring; alerting |
| **Dependency management** | Training and serving environments differ | Containerisation; reproducible environments |
| **No rollback plan** | Can't revert to previous model when new model fails | Model registry; versioning; automated rollback |

### Model Decay

| Type | Description | Detection |
|------|-------------|-----------|
| **Data drift** | Input feature distributions change | Monitor feature statistics; KL divergence; PSI |
| **Concept drift** | Relationship between features and target changes | Monitor prediction accuracy over time |
| **Label drift** | Definition or distribution of the target changes | Track label distributions; business metric correlation |
| **Upstream changes** | Data source changes format, timing, or quality | Schema validation; freshness monitoring |

---

## Organisational Failures

| Failure | Description | Prevention |
|---------|-------------|------------|
| **No clear ownership** | Nobody is accountable for the model in production | Assign model owners; define RACI |
| **Siloed teams** | Data scientists build models; engineers deploy; nobody communicates | Cross-functional teams; shared goals |
| **No MLOps maturity** | No model registry; no CI/CD; no monitoring | Invest in MLOps infrastructure incrementally |
| **Unrealistic timelines** | "Build a production ML system in 2 weeks" | Time-box exploration; iterate; communicate complexity |
| **Lack of domain expertise** | ML team doesn't understand the business problem | Embed domain experts in ML teams |
| **No evaluation framework** | Can't tell if the model is working in production | Define business metrics; set up dashboards; regular reviews |

---

## Lessons Learned

### The ML Project Checklist

| Phase | Key Question |
|-------|-------------|
| **Problem definition** | Is this actually an ML problem? What's the baseline? What does success look like? |
| **Data assessment** | Do we have enough data? Is it representative? Are labels reliable? |
| **Feasibility** | Can we build a working prototype in 2-4 weeks? What are the risks? |
| **Development** | Is there data leakage? Are we using the right evaluation metric? |
| **Pre-production** | Does it work with production data? Is it fast enough? Is it monitored? |
| **Deployment** | Can we roll back? Who is on-call? What happens when it degrades? |
| **Post-deployment** | Are we monitoring drift? Are business metrics tracked? Is there a retraining plan? |

---

## Summary

ML projects fail not because the algorithms are too hard, but because the process around them is broken. Data problems — insufficient data, poor labels, leakage, drift — account for the largest share of failures. Problem definition failures — solving the wrong problem, using ML when rules would suffice, ignoring the cost of errors — waste months of effort. Expectation failures — over-promising, under-delivering, not managing stakeholders — destroy organisational trust in ML. Deployment failures — notebook-to-production gaps, latency issues, no monitoring — mean models that work in development never create value in production. Organisational failures — no ownership, siloed teams, no MLOps — make it structurally impossible to succeed. The antidote is disciplined practice: start with a baseline; time-box exploration; validate data rigorously; check for leakage; define business metrics; deploy incrementally; monitor continuously; and iterate. The best ML teams spend more time on data and process than on models.
