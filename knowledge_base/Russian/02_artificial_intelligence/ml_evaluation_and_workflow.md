<!-- 
This file was automatically translated from English to Russian.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Машинное обучение Evaluation и Workflow

A practical Руководство to the ML lifecycle — from problem framing to production monitoring — с a focus on metrics, validation, и debugging.

---

## the ML Workflow (CRISP-ML)

1. **Бизнес Understanding**: Define the objective и success criteria.
2. **Данные Understanding**: Explore available Данные, identify quality issues.
3. **Данные Preparation**: Clean, transform, и split Данные.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess Производительность against metrics.
6. **Развертывание**: Serve the model в production.
7. **Monitoring**: Track drift, Производительность, и anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## Данные Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit the model parameters.
- **Validation set** (~15%): Used to tune hyperparameters и select model variants.
- **Test set** (~15%): Used only once at the very end to estimate generalisation Производительность.

**Important:** the test set must be kept completely untouched until final evaluation to avoid Данные leakage.

### Cross-Validation (k-fold)
для small datasets, use k-fold cross-validation: split Данные into k folds, train on k-1, validate on the remaining, и repeat k times. Average the Производительность. k=5 or k=10 is common.

### Stratified Splitting
для classification с imbalanced classes, use stratified splits to preserve class proportions в each subset.

### Time-Based Splitting
для time-series Данные, split chronologically (train on past, test on Будущее) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used для |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean из precision и recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under the ROC curve; tradeoff between TPR и FPR | General classifier Производительность independent из threshold |
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
| **RMSE** (Root Mean Squared Error) | Square root из MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient из Determination) | Proportion из variance explained | None directly, but sensitive to outliers indirectly |

### Ranking и Retrieval Metrics
- **Precision@k**: Fraction из relevant items among top-k recommendations.
- **Recall@k**: Fraction из all relevant items that appear в top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts для position relevance.
- **Hit Rate**: Whether a relevant item appears в the top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" the model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap с Справочник translations (precision-focused).
- **ROUGE**: Recall-oriented overlap для summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms и stems.

---

## Evaluation Pitfalls

### Данные Leakage
Occurs when information from the test set inadvertently influences training.
- **Prevent:** Never use test Данные для feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training Данные but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify Архитектура, or collect more Данные.

### Underfitting
Model performs poorly on both training и validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced Данные
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
the relationship between features и target changes over time.
- **Mitigate:** Retrain periodically, monitor Производительность, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations из a predefined set из hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search для high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model из the objective function и selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps для distributed tuning.

**Suggested search ranges для common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number из layers (NN) | 2 to 6 |
| Number из neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection и Validation

1. **Baseline model**: Start с a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural Сеть).
3. **Cross-validate** each candidate on the validation set.
4. **Compare metrics** (с confidence intervals) и select the best candidate.
5. **Final evaluation** on the held-out test set.
6. **Error analysis**: Look at Примеры the model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) и feed insights back into Данные preparation or feature engineering.

---

## Развертывание и Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes из Данные offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time с low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **Производительность monitoring**: Track accuracy/F1 over time on live Данные (when ground truth is available).
- **Данные drift**: Monitor changes в input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes в the relationship between inputs и outputs.
- **Prediction drift**: Track the distribution из predicted outputs.
- **Latency и throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging и Alerting
- Log all prediction requests и responses (с anonymisation).
- Set alerts для:
  - Significant drop в Производительность.
  - High percentage из missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning и Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store и version models, metadata, и evaluation results.
- Store the training code и Данные version (via DVC or Git LFS) alongside the model.

---

## Practical Workflow Checklist

- [ ] Problem framed и success metric defined.
- [ ] Данные exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained и validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] Развертывание plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (Данные card, model card) completed.