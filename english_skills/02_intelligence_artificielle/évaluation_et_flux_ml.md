<!-- 
This file was automatically translated from English to French.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Machdanse Learndansg Evaluation et Workflow

A practical guide to le/la ML lifecycle — from problem framdansg to production monitordansg — avec a focus on metrics, validation, et debuggdansg.

---

# # The ML Workflow (CRISP-ML)

1. **Busdansess Understetdansg**: Defdanse le/la objective et success criteria.
2. **Données Understetdansg**: Explore available données, identify quality issues.
3. **Données Preparation**: Clean, transpourm, et split données.
4. **Modelldansg**: Tradans models, tune hyperparameters.
5. **Evaluation**: Assess perpourmance agadansst metrics.
6. **Déploiement**: Serve le/la model dans production.
7. **Monitordansg**: Track drift, perpourmance, et anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # Données Splittdansg

# ## Tradans / Validation / Test Split
- **Tradansdansg set** (~70%): Used to fit le/la model parameters.
- **Validation set** (~15%): Used to tune hyperparameters et select model variants.
- **Test set** (~15%): Used only once at le/la very end to estimate generalisation perpourmance.

**Important:** The test set must be kept completely untouched until fdansal evaluation to avoid données leakage.

# ## Cross-Validation (k-fold)
For small donnéessets, use k-fold cross-validation: split données dansto k folds, tradans on k-1, validate on le/la remadansdansg, et repeat k times. Average le/la perpourmance. k=5 or k=10 is common.

# ## Stratified Splittdansg
For classification avec imbalanced classes, use stratified splits to preserve class proportions dans each subset.

# ## Time-Based Splittdansg
For time-series données, split chronologically (tradans on past, test on futur) rale/lar than retomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used pour |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced donnéessets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screendansg) |
| **F1-score** | Harmonic mean de precision et recall | Imbalanced donnéessets, sdansgle-number metric |
| **AUC-ROC** | Area under le/la ROC curve; tradedef between TPR et FPR | General classifier perpourmance dansdependent de threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced donnéessets |

**Defdansitions:**
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
| **R²** (Coefficient de Determdansation) | Proportion de variance expladansed | None directly, but sensitive to outliers dansdirectly |

# ## Rankdansg et Retrieval Metrics
- **Precision@k**: Fraction de relevant items among top-k recommendations.
- **Recall@k**: Fraction de all relevant items that appear dans top-k.
- **NDCG** (Normalised Discounted Cumulative Gadans): Accounts pour position relevance.
- **Hit Rate**: Whele/lar a relevant item appears dans le/la top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" le/la model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap avec référence translations (precision-focused).
- **ROUGE**: Recall-oriented overlap pour summarisation.
- **BERTScore**: Semantic similarity usdansg contextual embedddansgs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms et stems.

---

# # Evaluation Pitfalls

# ## Données Leakage
Occurs when danspourmation from le/la test set dansadvertently dansfluences tradansdansg.
- **Prevent:** Never use test données pour feature engdanseerdansg, normalisation, or hyperparameter tundansg.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfittdansg
Model perpourms well on tradansdansg données but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppdansg, simplify architecture, or collect more données.

# ## Underfittdansg
Model perpourms poorly on both tradansdansg et validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced Données
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rale/lar than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features et target changes over time.
- **Mitigate:** Retradans periodically, monitor perpourmance, use drift detection algorithms.

---

# # Hyperparameter Tundansg

- **Grid Search**: Exhaustively try all combdansations de a predefdansed set de hyperparameters. Simple but computationally expensive.
- **Retom Search**: Sample retom combdansations from distributions. More efficient than grid search pour high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model de le/la objective function et selects hyperparameters danstelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tundansg**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps pour distributed tundansg.

**Suggested search ranges pour common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learndansg rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number de layers (NN) | 2 to 6 |
| Number de neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection et Validation

1. **Baseldanse model**: Start avec a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cetidate models**: Tradans multiple model families (e.g., Retom Forest, XGBoost, Neural Réseau).
3. **Cross-validate** each cetidate on le/la validation set.
4. **Compare metrics** (avec confidence danstervals) et select le/la best cetidate.
5. **Fdansal evaluation** on le/la held-out test set.
6. **Error analysis**: Look at exemples le/la model gets wrong. Identify patterns (e.g., rare classes, ambiguous dansputs) et feed danssights back dansto données preparation or feature engdanseerdansg.

---

# # Déploiement et Monitordansg

# ## Servdansg Patterns
- **Batch dansference**: Process large volumes de données defldanse (e.g., nightly recommendations).
- **Onldanse dansference**: Real-time predictions via API (e.g., credit scordansg, fraud detection).
- **Streamdansg dansference**: Event-driven, real-time avec low latency (e.g., IoT sensor alerts).

# ## Model Monitordansg
- **Perpourmance monitordansg**: Track accuracy/F1 over time on live données (when ground truth is available).
- **Données drift**: Monitor changes dans dansput feature distributions (e.g., usdansg PSI – Population Stability Index).
- **Concept drift**: Monitor changes dans le/la relationship between dansputs et outputs.
- **Prediction drift**: Track le/la distribution de predicted outputs.
- **Latency et throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggdansg et Alertdansg
- Log all prediction requests et responses (avec anonymisation).
- Set alerts pour:
  - Significant drop dans perpourmance.
  - High percentage de missdansg or dansvalid dansputs.
  - Model outputs outside expected bounds.

# ## Model Versiondansg et Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store et version models, metadonnées, et evaluation results.
- Store le/la tradansdansg code et données version (via DVC or Git LFS) alongside le/la model.

---

# # Practical Workflow Checklist

- [ ] Problem framed et success metric defdansed.
- [ ] Données exploration perpourmed (missdansg values, outliers, distribution).
- [ ] Tradans/validation/test split created (stratified if needed).
- [ ] Baseldanse model established.
- [ ] Cetidate models tradansed et validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fdansal evaluation on test set.
- [ ] Error analysis perpourmed.
- [ ] Déploiement plan ready (servdansg dansfrastructure).
- [ ] Monitordansg dashboard set up.
- [ ] Documentation (données card, model card) completed.