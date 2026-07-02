<!-- 
This file was automatically translated from English to Arabic.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# التعلم الآلي Evaluation و Workflow

A practical دليل to ال ML lifecycle — from problem framing to production monitoring — مع a focus on metrics, validation, و debugging.

---

## ال ML Workflow (CRISP-ML)

1. **الأعمال Understanding**: Define ال objective و success criteria.
2. **البيانات Understanding**: Explore available البيانات, identify quality issues.
3. **البيانات Preparation**: Clean, transform, و split البيانات.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess الأداء against metrics.
6. **النشر**: Serve ال model في production.
7. **Monitoring**: Track drift, الأداء, و anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## البيانات Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit ال model parameters.
- **Validation set** (~15%): Used to tune hyperparameters و select model variants.
- **Test set** (~15%): Used only once at ال very end to estimate generalisation الأداء.

**Important:** ال test set must be kept completely untouched until final evaluation to avoid البيانات leakage.

### Cross-Validation (k-fold)
لأجل small datasets, use k-fold cross-validation: split البيانات into k folds, train on k-1, validate on ال remaining, و repeat k times. Average ال الأداء. k=5 or k=10 is common.

### Stratified Splitting
لأجل classification مع imbalanced classes, use stratified splits to preserve class proportions في each subset.

### Time-Based Splitting
لأجل time-series البيانات, split chronologically (train on past, test on المستقبل) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used لأجل |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean من precision و recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under ال ROC curve; tradeoff between TPR و FPR | General classifier الأداء independent من threshold |
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
| **RMSE** (Root Mean Squared Error) | Square root من MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient من Determination) | Proportion من variance explained | None directly, but sensitive to outliers indirectly |

### Ranking و Retrieval Metrics
- **Precision@k**: Fraction من relevant items among top-k recommendations.
- **Recall@k**: Fraction من all relevant items that appear في top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts لأجل position relevance.
- **Hit Rate**: Whether a relevant item appears في ال top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" ال model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap مع مرجع translations (precision-focused).
- **ROUGE**: Recall-oriented overlap لأجل summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms و stems.

---

## Evaluation Pitfalls

### البيانات Leakage
Occurs when information from ال test set inadvertently influences training.
- **Prevent:** Never use test البيانات لأجل feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training البيانات but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify العمارة, or collect more البيانات.

### Underfitting
Model performs poorly on both training و validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced البيانات
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
ال relationship between features و target changes over time.
- **Mitigate:** Retrain periodically, monitor الأداء, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations من a predefined set من hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search لأجل high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model من ال objective function و selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps لأجل distributed tuning.

**Suggested search ranges لأجل common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number من layers (NN) | 2 to 6 |
| Number من neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection و Validation

1. **Baseline model**: Start مع a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural الشبكة).
3. **Cross-validate** each candidate on ال validation set.
4. **Compare metrics** (مع confidence intervals) و select ال best candidate.
5. **Final evaluation** on ال held-out test set.
6. **Error analysis**: Look at أمثلة ال model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) و feed insights back into البيانات preparation or feature engineering.

---

## النشر و Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes من البيانات offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time مع low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **الأداء monitoring**: Track accuracy/F1 over time on live البيانات (when ground truth is available).
- **البيانات drift**: Monitor changes في input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes في ال relationship between inputs و outputs.
- **Prediction drift**: Track ال distribution من predicted outputs.
- **Latency و throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging و Alerting
- Log all prediction requests و responses (مع anonymisation).
- Set alerts لأجل:
  - Significant drop في الأداء.
  - High percentage من missing or invalid inputs.
  - Model outputs outside expected bounds.

### Model Versioning و Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store و version models, metadata, و evaluation results.
- Store ال training code و البيانات version (via DVC or Git LFS) alongside ال model.

---

## Practical Workflow Checklist

- [ ] Problem framed و success metric defined.
- [ ] البيانات exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained و validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] النشر plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (البيانات card, model card) completed.