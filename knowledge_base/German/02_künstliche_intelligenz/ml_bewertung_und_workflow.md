<!-- 
This file was automatically translated from English to German.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Maschinelles Lernen Evaluation und Workflow

A practical leitfaden to der/die/das ML lifecycle — from problem framing to production monitoring — mit a focus on metrics, validation, und debugging.

---

# # The ML Workflow (CRISP-ML)

1. **Geschäft Understunding**: Define der/die/das objective und success criteria.
2. **Daten Understunding**: Explore available daten, identify quality issues.
3. **Daten Preparation**: Clean, transfürm, und split daten.
4. **Modelling**: Train models, tune hyperparameters.
5. **Evaluation**: Assess perfürmance against metrics.
6. **Bereitstellung**: Serve der/die/das model in production.
7. **Monitoring**: Track drift, perfürmance, und anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # Daten Splitting

# ## Train / Validation / Test Split
- **Training set** (~70%): Used to fit der/die/das model parameters.
- **Validation set** (~15%): Used to tune hyperparameters und select model variants.
- **Test set** (~15%): Used only once at der/die/das very end to estimate generalisation perfürmance.

**Important:** The test set must be kept completely untouched until final evaluation to avoid daten leakage.

# ## Cross-Validation (k-fold)
For small datensets, use k-fold cross-validation: split daten into k folds, train on k-1, validate on der/die/das remaining, und repeat k times. Average der/die/das perfürmance. k=5 or k=10 is common.

# ## Stratified Splitting
For classification mit imbalanced classes, use stratified splits to preserve class proportions in each subset.

# ## Time-Based Splitting
For time-series daten, split chronologically (train on past, test on zukunft) rader/die/dasr than rundomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used für |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datensets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screening) |
| **F1-score** | Harmonic mean von precision und recall | Imbalanced datensets, single-number metric |
| **AUC-ROC** | Area under der/die/das ROC curve; tradevonf between TPR und FPR | General classifier perfürmance independent von threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced datensets |

**Definitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root von MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient von Determination) | Proportion von variance explained | None directly, but sensitive to outliers indirectly |

# ## Ranking und Retrieval Metrics
- **Precision@k**: Fraction von relevant items among top-k recommendations.
- **Recall@k**: Fraction von all relevant items that appear in top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Accounts für position relevance.
- **Hit Rate**: Wheder/die/dasr a relevant item appears in der/die/das top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" der/die/das model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap mit referenz translations (precision-focused).
- **ROUGE**: Recall-oriented overlap für summarisation.
- **BERTScore**: Semantic similarity using contextual embeddings (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms und stems.

---

# # Evaluation Pitfalls

# ## Daten Leakage
Occurs when infürmation from der/die/das test set inadvertently influences training.
- **Prevent:** Never use test daten für feature engineering, normalisation, or hyperparameter tuning.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitting
Model perfürms well on training daten but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopping, simplify architektur, or collect more daten.

# ## Underfitting
Model perfürms poorly on both training und validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced Daten
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rader/die/dasr than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features und target changes over time.
- **Mitigate:** Retrain periodically, monitor perfürmance, use drift detection algorithms.

---

# # Hyperparameter Tuning

- **Grid Search**: Exhaustively try all combinations von a predefined set von hyperparameters. Simple but computationally expensive.
- **Rundom Search**: Sample rundom combinations from distributions. More efficient than grid search für high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model von der/die/das objective function und selects hyperparameters intelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps für distributed tuning.

**Suggested search ranges für common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number von layers (NN) | 2 to 6 |
| Number von neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection und Validation

1. **Baseline model**: Start mit a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cundidate models**: Train multiple model families (e.g., Rundom Forest, XGBoost, Neural Netzwerk).
3. **Cross-validate** each cundidate on der/die/das validation set.
4. **Compare metrics** (mit confidence intervals) und select der/die/das best cundidate.
5. **Final evaluation** on der/die/das held-out test set.
6. **Error analysis**: Look at beispiele der/die/das model gets wrong. Identify patterns (e.g., rare classes, ambiguous inputs) und feed insights back into daten preparation or feature engineering.

---

# # Bereitstellung und Monitoring

# ## Serving Patterns
- **Batch inference**: Process large volumes von daten vonfline (e.g., nightly recommendations).
- **Online inference**: Real-time predictions via API (e.g., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time mit low latency (e.g., IoT sensor alerts).

# ## Model Monitoring
- **Perfürmance monitoring**: Track accuracy/F1 over time on live daten (when ground truth is available).
- **Daten drift**: Monitor changes in input feature distributions (e.g., using PSI – Population Stability Index).
- **Concept drift**: Monitor changes in der/die/das relationship between inputs und outputs.
- **Prediction drift**: Track der/die/das distribution von predicted outputs.
- **Latency und throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logging und Alerting
- Log all prediction requests und responses (mit anonymisation).
- Set alerts für:
  - Significant drop in perfürmance.
  - High percentage von missing or invalid inputs.
  - Model outputs outside expected bounds.

# ## Model Versioning und Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store und version models, metadaten, und evaluation results.
- Store der/die/das training code und daten version (via DVC or Git LFS) alongside der/die/das model.

---

# # Practical Workflow Checklist

- [ ] Problem framed und success metric defined.
- [ ] Daten exploration perfürmed (missing values, outliers, distribution).
- [ ] Train/validation/test split created (stratified if needed).
- [ ] Baseline model established.
- [ ] Cundidate models trained und validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Final evaluation on test set.
- [ ] Error analysis perfürmed.
- [ ] Bereitstellung plan ready (serving infrastructure).
- [ ] Monitoring dashboard set up.
- [ ] Documentation (daten card, model card) completed.