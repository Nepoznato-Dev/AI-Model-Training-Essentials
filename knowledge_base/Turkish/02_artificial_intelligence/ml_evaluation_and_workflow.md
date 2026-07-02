<!-- 
This file was automatically translated from English to Turkish.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Makine Öğrenimi Evaluation ve Workflow

A practical Rehber to bu ML lifecycle — from problem framing to production monitoring — ile a focus on metrics, validation, ve debugging.

---

## bu ML Workflow (CRISP-ML)

1. **İş Understanding**: Define bu objective ve success criteria.
2. **Veri Understanding**: Explore available Veri, identify quality issues.
3. **Veri Preparation**: Clean, transform, ve split Veri.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess Performans against metrics.
6. **Dağıtım**: Serve bu model içinde production.
7. **Monitoring**: Track drift, Performans, ve anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## Veri Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit bu model parameters.
- **Validation set** (~15%): Used to tune hyperparameters ve select model variants.
- **Test set** (~15%): Used only once at bu very end to estimate generalisation Performans.

**Important:** bu test set must be kept completely untouched until final evaluation to avoid Veri leakage.

### Cross-Validation (k-fold)
için small datasets, use k-fold cross-validation: split Veri into k folds, train on k-1, validate on bu remaining, ve repeat k times. Average bu Performans. k=5 or k=10 is common.

### Stratified Splitting
için classification ile imbalanced classes, use stratified splits to preserve class proportions içinde each subset.

### Time-Based Splitting
için time-series Veri, split chronologically (train on past, test on Gelecek) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used için |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean içinde precision ve recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under bu ROC curve; tradeoff between TPR ve FPR | General classifier Performans independent içinde threshold |
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
| **RMSE** (Root Mean Squared Error) | Square root içinde MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient içinde Determination) | Proportion içinde variance explained | None directly, but sensitive to outliers indirectly |

### Ranking ve Retrieval Metrics
- **Precision@k**: Fraction içinde relevant items among top-k recommendations.
- **Recall@k**: Fraction içinde all relevant items that appear içinde top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts için position relevance.
- **Hit Rate**: Whether a relevant item appears içinde bu top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" bu model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap ile Referans translations (precision-focused).
- **ROUGE**: Recall-oriented overlap için summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms ve stems.

---

## Evaluation Pitfalls

### Veri Leakage
Occurs when information from bu test set inadvertently influences training.
- **Prevent:** Never use test Veri için feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training Veri but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify Mimari, or collect more Veri.

### Underfitting
Model performs poorly on both training ve validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced Veri
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
bu relationship between features ve target changes over time.
- **Mitigate:** Retrain periodically, monitor Performans, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations içinde a predefined set içinde hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search için high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model içinde bu objective function ve selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps için distributed tuning.

**Suggested search ranges için common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number içinde layers (NN) | 2 to 6 |
| Number içinde neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection ve Validation

1. **Baseline model**: Start ile a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural Ağ).
3. **Cross-validate** each candidate on bu validation set.
4. **Compare metrics** (ile confidence intervals) ve select bu best candidate.
5. **Final evaluation** on bu held-out test set.
6. **Error analysis**: Look at Örnekler bu model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) ve feed insights back into Veri preparation or feature engineering.

---

## Dağıtım ve Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes içinde Veri offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time ile low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **Performans monitoring**: Track accuracy/F1 over time on live Veri (when ground truth is available).
- **Veri drift**: Monitor changes içinde input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes içinde bu relationship between inputs ve outputs.
- **Prediction drift**: Track bu distribution içinde predicted outputs.
- **Latency ve throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging ve Alerting
- Log all prediction requests ve responses (ile anonymisation).
- Set alerts için:
  - Significant drop içinde Performans.
  - High percentage içinde missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning ve Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store ve version models, metadata, ve evaluation results.
- Store bu training code ve Veri version (via DVC or Git LFS) alongside bu model.

---

## Practical Workflow Checklist

- [ ] Problem framed ve success metric defined.
- [ ] Veri exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained ve validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] Dağıtım plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (Veri card, model card) completed.