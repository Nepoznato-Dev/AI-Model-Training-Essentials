<!-- 
This file was automatically translated from English to French.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Apprentissage automatique Evaluation et Workflow

A practical Guide to le/la ML lifecycle — from problem framing to production monitoring — avec a focus on metrics, validation, et debugging.

---

## le/la ML Workflow (CRISP-ML)

1. **Entreprise Understanding**: Define le/la objective et success criteria.
2. **Données Understanding**: Explore available Données, identify quality issues.
3. **Données Preparation**: Clean, transform, et split Données.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess Performance against metrics.
6. **Déploiement**: Serve le/la model dans production.
7. **Monitoring**: Track drift, Performance, et anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## Données Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit le/la model parameters.
- **Validation set** (~15%): Used to tune hyperparameters et select model variants.
- **Test set** (~15%): Used only once at le/la very end to estimate generalisation Performance.

**Important:** le/la test set must be kept completely untouched until final evaluation to avoid Données leakage.

### Cross-Validation (k-fold)
pour small datasets, use k-fold cross-validation: split Données into k folds, train on k-1, validate on le/la remaining, et repeat k times. Average le/la Performance. k=5 or k=10 is common.

### Stratified Splitting
pour classification avec imbalanced classes, use stratified splits to preserve class proportions dans each subset.

### Time-Based Splitting
pour time-series Données, split chronologically (train on past, test on Futur) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used pour |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean de precision et recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under le/la ROC curve; tradeoff between TPR et FPR | General classifier Performance independent de threshold |
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
| **RMSE** (Root Mean Squared Error) | Square root de MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient de Determination) | Proportion de variance explained | None directly, but sensitive to outliers indirectly |

### Ranking et Retrieval Metrics
- **Precision@k**: Fraction de relevant items among top-k recommendations.
- **Recall@k**: Fraction de all relevant items that appear dans top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts pour position relevance.
- **Hit Rate**: Whether a relevant item appears dans le/la top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" le/la model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap avec Référence translations (precision-focused).
- **ROUGE**: Recall-oriented overlap pour summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms et stems.

---

## Evaluation Pitfalls

### Données Leakage
Occurs when information from le/la test set inadvertently influences training.
- **Prevent:** Never use test Données pour feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training Données but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify Architecture, or collect more Données.

### Underfitting
Model performs poorly on both training et validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced Données
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
le/la relationship between features et target changes over time.
- **Mitigate:** Retrain periodically, monitor Performance, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations de a predefined set de hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search pour high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model de le/la objective function et selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps pour distributed tuning.

**Suggested search ranges pour common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number de layers (NN) | 2 to 6 |
| Number de neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection et Validation

1. **Baseline model**: Start avec a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural Réseau).
3. **Cross-validate** each candidate on le/la validation set.
4. **Compare metrics** (avec confidence intervals) et select le/la best candidate.
5. **Final evaluation** on le/la held-out test set.
6. **Error analysis**: Look at Exemples le/la model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) et feed insights back into Données preparation or feature engineering.

---

## Déploiement et Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes de Données offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time avec low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **Performance monitoring**: Track accuracy/F1 over time on live Données (when ground truth is available).
- **Données drift**: Monitor changes dans input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes dans le/la relationship between inputs et outputs.
- **Prediction drift**: Track le/la distribution de predicted outputs.
- **Latency et throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging et Alerting
- Log all prediction requests et responses (avec anonymisation).
- Set alerts pour:
  - Significant drop dans Performance.
  - High percentage de missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning et Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store et version models, metadata, et evaluation results.
- Store le/la training code et Données version (via DVC or Git LFS) alongside le/la model.

---

## Practical Workflow Checklist

- [ ] Problem framed et success metric defined.
- [ ] Données exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained et validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] Déploiement plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (Données card, model card) completed.