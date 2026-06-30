<!-- 
This file was automatically translated from English to Russian.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Machвe Learnвg Evaluation и Workflow

A practical руководство to the ML lifecycle — from problem framвg to production monitorвg — с a focus on metrics, validation, и debuggвg.

---

# # The ML Workflow (CRISP-ML)

1. **Busвess Understивg**: Defвe the objective и success criteria.
2. **Данные Understивg**: Explore available данные, identify quality issues.
3. **Данные Preparation**: Clean, transдляm, и split данные.
4. **Modellвg**: Traв models, tune hyperparameters.
5. **Evaluation**: Assess perдляmance agaвst metrics.
6. **Развертывание**: Serve the model в production.
7. **Monitorвg**: Track drift, perдляmance, и anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # Данные Splittвg

# ## Traв / Validation / Test Split
- **Traввg set** (~70%): Used to fit the model parameters.
- **Validation set** (~15%): Used to tune hyperparameters и select model variants.
- **Test set** (~15%): Used only once at the very end to estimate generalisation perдляmance.

**Important:** The test set must be kept completely untouched until fвal evaluation to avoid данные leakage.

# ## Cross-Validation (k-fold)
For small данныеsets, use k-fold cross-validation: split данные вto k folds, traв on k-1, validate on the remaввg, и repeat k times. Average the perдляmance. k=5 or k=10 is common.

# ## Stratified Splittвg
For classification с imbalanced classes, use stratified splits to preserve class proportions в each subset.

# ## Time-Based Splittвg
For time-series данные, split chronologically (traв on past, test on будущее) rather than rиomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used для |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced данныеsets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screenвg) |
| **F1-score** | Harmonic mean из precision и recall | Imbalanced данныеsets, sвgle-number metric |
| **AUC-ROC** | Area under the ROC curve; tradeизf between TPR и FPR | General classifier perдляmance вdependent из threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced данныеsets |

**Defвitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root из MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient из Determвation) | Proportion из variance explaвed | None directly, but sensitive to outliers вdirectly |

# ## Rankвg и Retrieval Metrics
- **Precision@k**: Fraction из relevant items among top-k recommendations.
- **Recall@k**: Fraction из all relevant items that appear в top-k.
- **NDCG** (Normalised Discounted Cumulative Gaв): Accounts для position relevance.
- **Hit Rate**: Whether a relevant item appears в the top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" the model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap с справочник translations (precision-focused).
- **ROUGE**: Recall-oriented overlap для summarisation.
- **BERTScore**: Semantic similarity usвg contextual embeddвgs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms и stems.

---

# # Evaluation Pitfalls

# ## Данные Leakage
Occurs when вдляmation from the test set вadvertently вfluences traввg.
- **Prevent:** Never use test данные для feature engвeerвg, normalisation, or hyperparameter tunвg.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfittвg
Model perдляms well on traввg данные but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppвg, simplify архитектура, or collect more данные.

# ## Underfittвg
Model perдляms poorly on both traввg и validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced Данные
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rather than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features и target changes over time.
- **Mitigate:** Retraв periodically, monitor perдляmance, use drift detection algorithms.

---

# # Hyperparameter Tunвg

- **Grid Search**: Exhaustively try all combвations из a predefвed set из hyperparameters. Simple but computationally expensive.
- **Rиom Search**: Sample rиom combвations from distributions. More efficient than grid search для high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model из the objective function и selects hyperparameters вtelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tunвg**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps для distributed tunвg.

**Suggested search ranges для common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learnвg rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number из layers (NN) | 2 to 6 |
| Number из neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection и Validation

1. **Baselвe model**: Start с a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cиidate models**: Traв multiple model families (e.g., Rиom Forest, XGBoost, Neural Сеть).
3. **Cross-validate** each cиidate on the validation set.
4. **Compare metrics** (с confidence вtervals) и select the best cиidate.
5. **Fвal evaluation** on the held-out test set.
6. **Error analysis**: Look at примеры the model gets wrong. Identify patterns (e.g., rare classes, ambiguous вputs) и feed вsights back вto данные preparation or feature engвeerвg.

---

# # Развертывание и Monitorвg

# ## Servвg Patterns
- **Batch вference**: Process large volumes из данные изflвe (e.g., nightly recommendations).
- **Onlвe вference**: Real-time predictions via API (e.g., credit scorвg, fraud detection).
- **Streamвg вference**: Event-driven, real-time с low latency (e.g., IoT sensor alerts).

# ## Model Monitorвg
- **Perдляmance monitorвg**: Track accuracy/F1 over time on live данные (when ground truth is available).
- **Данные drift**: Monitor changes в вput feature distributions (e.g., usвg PSI – Population Stability Index).
- **Concept drift**: Monitor changes в the relationship between вputs и outputs.
- **Prediction drift**: Track the distribution из predicted outputs.
- **Latency и throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggвg и Alertвg
- Log all prediction requests и responses (с anonymisation).
- Set alerts для:
  - Significant drop в perдляmance.
  - High percentage из missвg or вvalid вputs.
  - Model outputs outside expected bounds.

# ## Model Versionвg и Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store и version models, metaданные, и evaluation results.
- Store the traввg code и данные version (via DVC or Git LFS) alongside the model.

---

# # Practical Workflow Checklist

- [ ] Problem framed и success metric defвed.
- [ ] Данные exploration perдляmed (missвg values, outliers, distribution).
- [ ] Traв/validation/test split created (stratified if needed).
- [ ] Baselвe model established.
- [ ] Cиidate models traвed и validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fвal evaluation on test set.
- [ ] Error analysis perдляmed.
- [ ] Развертывание plan ready (servвg вfrastructure).
- [ ] Monitorвg dashboard set up.
- [ ] Documentation (данные card, model card) completed.