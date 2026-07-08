<!-- 
This file was automatically translated from English to Spanish.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Aprendizaje automático Evaluation y Workflow

A practical Guía to el ML lifecycle — from problem framing to production monitoring — con a focus on metrics, validation, y debugging.

---

## el ML Workflow (CRISP-ML)

1. **Negocios Understanding**: Define el objective y success criteria.
2. **Datos Understanding**: Explore Disponible Datos, identify quality issues.
3. **Datos Preparation**: Clean, transform, y split Datos.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess Rendimiento against metrics.
6. **Implementación**: Serve el model en production.
7. **Monitoring**: Track drift, Rendimiento, y anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

## Datos Splitting

### Train / Validation / Test Split
- **Training set** (~70%): Used to fit el model parameters.
- **Validation set** (~15%): Used to tune hyperparameters y select model variants.
- **Test set** (~15%): Used only once at el very end to estimate generalisation Rendimiento.

**Important:** el test set must be kept completely untouched until final evaluation to avoid Datos leakage.

### Cross-Validation (k-fold)
para small datasets, use k-fold cross-validation: split Datos into k folds, train on k-1, validate on el remaining, y repeat k times. Average el Rendimiento. k=5 or k=10 is common.

### Stratified Splitting
para classification con imbalanced classes, use stratified splits to preserve class proportions en each subset.

### Time-Based Splitting
para time-series Datos, split chronologically (train on past, test on Futuro) rather than randomly.

---

## Evaluation Metrics

### Classification Metrics

| Metric | What it measures | Best used para |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean de precision y recall | Imbalanced datasets, single-number metric |
| **AUC-ROC** | Area under el ROC curve; tradeoff between TPR y FPR | General classifier Rendimiento independent de threshold |
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

### Ranking y Retrieval Metrics
- **Precision@k**: Fraction de relevant items among top-k recommendations.
- **Recall@k**: Fraction de all relevant items that appear en top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts para position relevance.
- **Hit Rate**: Whether a relevant item appears en el top-k.

### Generative / LLM Metrics
- **Perplexity**: How "surprised" el model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap con Referencia translations (precision-focused).
- **ROUGE**: Recall-oriented overlap para summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms y stems.

---

## Evaluation Pitfalls

### Datos Leakage
Occurs when information from el test set inadvertently influences training.
- **Prevent:** Never use test Datos para feature ingeniería, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

### Overfitting
Model performs well on training Datos but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify Arquitectura, or collect more Datos.

### Underfitting
Model performs poorly on both training y validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

### Imbalanced Datos
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

### Temporal Drift (Concept Drift)
el relationship between features y target changes over time.
- **Mitigate:** Retrain periodically, monitor Rendimiento, use drift detection algorithms.

---

## Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations de a predefined set de hyperparameters. Simple but computationally expensive.
- **Random Search**: Sample random combinations from distributions. More efficient than grid search para high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model del objective function y selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
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

## Model Selection y Validation

1. **Baseline model**: Start con a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Candidate models**: Train multiple model families (e.g., Random Forest, XGBoost, Neural Red).
3. **Cross-validate** each candidate on el validation set.
4. **Compare metrics** (con confidence intervals) y select el best candidate.
5. **Final evaluation** on el held-out test set.
6. **Error analysis**: Look at Ejemplos el model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) y feed insights back into Datos preparation or feature ingeniería.

---

## Implementación y Monitoring

### Serving Patterns
- **Batch inference**: Process large volumes de Datos offline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time con low latency (e.g., IoT sensor alerts).

### Model Monitoring
- **Rendimiento monitoring**: Track accuracy/F1 over time on live Datos (when ground truth is Disponible).
- **Datos drift**: Monitor changes en input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes en el relationship between inputs y outputs.
- **Prediction drift**: Track el distribution de predicted outputs.
- **Latency y throughput**: Ensure SLAs (Service Level Agreements) are met.

### Logging y Alerting
- Log all prediction requests y responses (con anonymisation).
- Set alerts para:
 - Significant drop en Rendimiento.
 - High percentage de missing or invalid inputs.
 - Model outputs outside expected bounds.

### Model Versioning y Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store y version models, metadata, y evaluation results.
- Store el training code y Datos version (via DVC or Git LFS) a lo largo deside el model.

---

## Practical Workflow Checklist

- [ ] Problem framed y success metric defined.
- [ ] Datos exploration performed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Candidate models trained y validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis performed.
- [ ] Implementación plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (Datos card, model card) completed.