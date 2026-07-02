<!-- 
This file was automatically translated from English to Portuguese.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Aprendizado de máquina Evaluation e Workflow

A practical Guia to o/a ML lifecycle — from problem framing to production monitoring — com a focus on metrics, validation, e debugging.

---

## o/a ML Workflow (CRISP-ML)

1. **Negócios Understanding**: Define o/a objective e success criteria.
2. **Dados Understanding**: Explore available Dados, identify quality issues.
3. **Dados Preparation**: Clean, transform, e split Dados.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess Desempenho against metrics.
6. **Implantação**: Serve o/a model em production.
7. **Monitoring**: Track drift, Desempenho, e anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## Dados Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit o/a model parameters.
- **Validation set** (~15%): Used to tune hyperparameters e select model variants.
- **Test set** (~15%): Used only once at o/a very end to estimate generalisation Desempenho.

**Important:** o/a test set must be kept completely untouched until final evaluation to avoid Dados leakage.

### Cross-Validation (k-fold)
para small datasets, use k-fold cross-validation: split Dados into k folds, train on k-1, validate on o/a remaining, e repeat k times. Average o/a Desempenho. k=5 or k=10 is common.

### Stratified Splitting
para classification com imbalanced classes, use stratified splits to preserve class proportions em each subset.

### Time-Based Splitting
para time-series Dados, split chronologically (train on past, test on Futuro) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used para |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean de precision e recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under o/a ROC curve; tradeoff between TPR e FPR | General classifier Desempenho independent de threshold |
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

### Ranking e Retrieval Metrics
- **Precision@k**: Fraction de relevant items among top-k recommendations.
- **Recall@k**: Fraction de all relevant items that appear em top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts para position relevance.
- **Hit Rate**: Whether a relevant item appears em o/a top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" o/a model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap com Referência translations (precision-focused).
- **ROUGE**: Recall-oriented overlap para summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms e stems.

---

## Evaluation Pitfalls

### Dados Leakage
Occurs when information from o/a test set inadvertently influences training.
- **Prevent:** Never use test Dados para feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training Dados but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify Arquitetura, or collect more Dados.

### Underfitting
Model performs poorly on both training e validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced Dados
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
o/a relationship between features e target changes over time.
- **Mitigate:** Retrain periodically, monitor Desempenho, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations de a predefined set de hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search para high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model de o/a objective function e selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps para distributed tuning.

**Suggested search ranges para common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number de layers (NN) | 2 to 6 |
| Number de neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection e Validation

1. **Baseline model**: Start com a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural Rede).
3. **Cross-validate** each candidate on o/a validation set.
4. **Compare metrics** (com confidence intervals) e select o/a best candidate.
5. **Final evaluation** on o/a held-out test set.
6. **Error analysis**: Look at Exemplos o/a model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) e feed insights back into Dados preparation or feature engineering.

---

## Implantação e Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes de Dados offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time com low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **Desempenho monitoring**: Track accuracy/F1 over time on live Dados (when ground truth is available).
- **Dados drift**: Monitor changes em input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes em o/a relationship between inputs e outputs.
- **Prediction drift**: Track o/a distribution de predicted outputs.
- **Latency e throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging e Alerting
- Log all prediction requests e responses (com anonymisation).
- Set alerts para:
  - Significant drop em Desempenho.
  - High percentage de missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning e Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store e version models, metadata, e evaluation results.
- Store o/a training code e Dados version (via DVC or Git LFS) alongside o/a model.

---

## Practical Workflow Checklist

- [ ] Problem framed e success metric defined.
- [ ] Dados exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained e validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] Implantação plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (Dados card, model card) completed.