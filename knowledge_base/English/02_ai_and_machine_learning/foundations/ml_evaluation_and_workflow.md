<!--
---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, evaluation, workflow, ai-and-machine-learning]
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

-->
# Machine Learning Evaluation and Workflow

A practical guide to the ML lifecycle — from problem framing to production monitoring — with a focus on metrics, validation, and debugging.

---

## The ML Workflow (CRISP-ML)

1. **Business Understanding**: Define the objective and success criteria.
2. **Data Understanding**: Explore available data, identify quality issues.
3. **Data Preparation**: Clean, transform, and split data.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess performance against metrics.
6. **Deployment**: Serve the model in production.
7. **Monitoring**: Track drift, performance, and anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## Data Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit the model parameters.
- **Validation set** (~15%): Used to tune hyperparameters and select model variants.
- **Test set** (~15%): Used only once at the very end to estimate generalisation performance.

**Important:** The test set must be kept completely untouched until final evaluation to avoid data leakage.

### Cross-Validation (k-fold)
For small datasets, use k-fold cross-validation: split data into k folds, train on k-1, validate on the remaining, and repeat k times. Average the performance. k=5 or k=10 is common.

### Stratified Splitting
For classification with imbalanced classes, use stratified splits to preserve class proportions in each subset.

### Time-Based Splitting
For time-series data, split chronologically (train on past, test on future) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used for |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean of precision and recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under the ROC curve; tradeoff between TPR and FPR | General classifier performance independent of threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced datasets |

**Definitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

### Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root of MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient of Determination) | Proportion of variance explained | None directly, but sensitive to outliers indirectly |

### Ranking and Retrieval Metrics
- **Precision@k**: Fraction of relevant items among top-k recommendations.
- **Recall@k**: Fraction of all relevant items that appear in top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts for position relevance.
- **Hit Rate**: Whether a relevant item appears in the top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" the model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap with reference translations (precision-focused).
- **ROUGE**: Recall-oriented overlap for summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms and stems.

---

## Evaluation Pitfalls

### Data Leakage
Occurs when information from the test set inadvertently influences training.
- **Prevent:** Never use test data for feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training data but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify architecture, or collect more data.

### Underfitting
Model performs poorly on both training and validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced Data
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
The relationship between features and target changes over time.
- **Mitigate:** Retrain periodically, monitor performance, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations of a predefined set of hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search for high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model of the objective function and selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps for distributed tuning.

**Suggested search ranges for common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection and Validation

1. **Baseline model**: Start with a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural Network).
3. **Cross-validate** each candidate on the validation set.
4. **Compare metrics** (with confidence intervals) and select the best candidate.
5. **Final evaluation** on the held-out test set.
6. **Error analysis**: Look at examples the model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) and feed insights back into data preparation or feature engineering.

---

## Deployment and Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes of data offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time with low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **Performance monitoring**: Track accuracy/F1 over time on live data (when ground truth is available).
- **Data drift**: Monitor changes in input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes in the relationship between inputs and outputs.
- **Prediction drift**: Track the distribution of predicted outputs.
- **Latency and throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging and Alerting
- Log all prediction requests and responses (with anonymisation).
- Set alerts for:
  - Significant drop in performance.
  - High percentage of missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning and Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store and version models, metadata, and evaluation results.
- Store the training code and data version (via DVC or Git LFS) alongside the model.

---

## Practical Workflow Checklist

- [ ] Problem framed and success metric defined.
- [ ] Data exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained and validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] Deployment plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (data card, model card) completed.