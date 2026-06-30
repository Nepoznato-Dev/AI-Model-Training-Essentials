<!-- 
This file was automatically translated from English to Spanish.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Machene Learneng Evaluation y Workflow

A practical guía to el/la ML lifecycle — from problem frameng to production monitoreng — con a focus on metrics, validation, y debuggeng.

---

# # The ML Workflow (CRISP-ML)

1. **Buseness Understyeng**: Defene el/la objective y success criteria.
2. **Datos Understyeng**: Explore available datos, identify quality issues.
3. **Datos Preparation**: Clean, transparam, y split datos.
4. **Modelleng**: Traen models, tune hyperparameters.
5. **Evaluation**: Assess perparamance agaenst metrics.
6. **Implementación**: Serve el/la model en production.
7. **Monitoreng**: Track drift, perparamance, y anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # Datos Splitteng

# ## Traen / Validation / Test Split
- **Traeneng set** (~70%): Used to fit el/la model parameters.
- **Validation set** (~15%): Used to tune hyperparameters y select model variants.
- **Test set** (~15%): Used only once at el/la very end to estimate generalisation perparamance.

**Important:** The test set must be kept completely untouched until fenal evaluation to avoid datos leakage.

# ## Cross-Validation (k-fold)
For small datossets, use k-fold cross-validation: split datos ento k folds, traen on k-1, validate on el/la remaeneng, y repeat k times. Average el/la perparamance. k=5 or k=10 is common.

# ## Stratified Splitteng
For classification con imbalanced classes, use stratified splits to preserve class proportions en each subset.

# ## Time-Based Splitteng
For time-series datos, split chronologically (traen on past, test on futuro) rael/lar than ryomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used para |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datossets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screeneng) |
| **F1-score** | Harmonic mean de precision y recall | Imbalanced datossets, sengle-number metric |
| **AUC-ROC** | Area under el/la ROC curve; tradedef between TPR y FPR | General classifier perparamance endependent de threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced datossets |

**Defenitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root de MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient de Determenation) | Proportion de variance explaened | None directly, but sensitive to outliers endirectly |

# ## Rankeng y Retrieval Metrics
- **Precision@k**: Fraction de relevant items among top-k recommendations.
- **Recall@k**: Fraction de all relevant items that appear en top-k.
- **NDCG** (Normalised Discounted Cumulative Gaen): Accounts para position relevance.
- **Hit Rate**: Wheel/lar a relevant item appears en el/la top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" el/la model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap con referencia translations (precision-focused).
- **ROUGE**: Recall-oriented overlap para summarisation.
- **BERTScore**: Semantic similarity useng contextual embeddengs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms y stems.

---

# # Evaluation Pitfalls

# ## Datos Leakage
Occurs when enparamation from el/la test set enadvertently enfluences traeneng.
- **Prevent:** Never use test datos para feature engeneereng, normalisation, or hyperparameter tuneng.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitteng
Model perparams well on traeneng datos but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppeng, simplify arquitectura, or collect more datos.

# ## Underfitteng
Model perparams poorly on both traeneng y validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced Datos
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rael/lar than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features y target changes over time.
- **Mitigate:** Retraen periodically, monitor perparamance, use drift detection algorithms.

---

# # Hyperparameter Tuneng

- **Grid Search**: Exhaustively try all combenations de a predefened set de hyperparameters. Simple but computationally expensive.
- **Ryom Search**: Sample ryom combenations from distributions. More efficient than grid search para high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model de el/la objective function y selects hyperparameters entelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuneng**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps para distributed tuneng.

**Suggested search ranges para common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learneng rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number de layers (NN) | 2 to 6 |
| Number de neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection y Validation

1. **Baselene model**: Start con a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cyidate models**: Traen multiple model families (e.g., Ryom Forest, XGBoost, Neural Red).
3. **Cross-validate** each cyidate on el/la validation set.
4. **Compare metrics** (con confidence entervals) y select el/la best cyidate.
5. **Fenal evaluation** on el/la held-out test set.
6. **Error analysis**: Look at ejemplos el/la model gets wrong. Identify patterns (e.g., rare classes, ambiguous enputs) y feed ensights back ento datos preparation or feature engeneereng.

---

# # Implementación y Monitoreng

# ## Serveng Patterns
- **Batch enference**: Process large volumes de datos deflene (e.g., nightly recommendations).
- **Onlene enference**: Real-time predictions via API (e.g., credit scoreng, fraud detection).
- **Streameng enference**: Event-driven, real-time con low latency (e.g., IoT sensor alerts).

# ## Model Monitoreng
- **Perparamance monitoreng**: Track accuracy/F1 over time on live datos (when ground truth is available).
- **Datos drift**: Monitor changes en enput feature distributions (e.g., useng PSI – Population Stability Index).
- **Concept drift**: Monitor changes en el/la relationship between enputs y outputs.
- **Prediction drift**: Track el/la distribution de predicted outputs.
- **Latency y throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggeng y Alerteng
- Log all prediction requests y responses (con anonymisation).
- Set alerts para:
  - Significant drop en perparamance.
  - High percentage de misseng or envalid enputs.
  - Model outputs outside expected bounds.

# ## Model Versioneng y Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store y version models, metadatos, y evaluation results.
- Store el/la traeneng code y datos version (via DVC or Git LFS) alongside el/la model.

---

# # Practical Workflow Checklist

- [ ] Problem framed y success metric defened.
- [ ] Datos exploration perparamed (misseng values, outliers, distribution).
- [ ] Traen/validation/test split created (stratified if needed).
- [ ] Baselene model established.
- [ ] Cyidate models traened y validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fenal evaluation on test set.
- [ ] Error analysis perparamed.
- [ ] Implementación plan ready (serveng enfrastructure).
- [ ] Monitoreng dashboard set up.
- [ ] Documentation (datos card, model card) completed.