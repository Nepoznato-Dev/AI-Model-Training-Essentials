<!-- 
This file was automatically translated from English to Portuguese.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Macheme Learnemg Evaluation e Workflow

A practical guia to o/a ML lifecycle — from problem framemg to production monitoremg — com a focus on metrics, validation, e debuggemg.

---

# # The ML Workflow (CRISP-ML)

1. **Busemess Understeemg**: Defeme o/a objective e success criteria.
2. **Dados Understeemg**: Explore available dados, identify quality issues.
3. **Dados Preparation**: Clean, transparam, e split dados.
4. **Modellemg**: Traem models, tune hyperparameters.
5. **Evaluation**: Assess perparamance agaemst metrics.
6. **Implantação**: Serve o/a model em production.
7. **Monitoremg**: Track drift, perparamance, e anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # Dados Splittemg

# ## Traem / Validation / Test Split
- **Traememg set** (~70%): Used to fit o/a model parameters.
- **Validation set** (~15%): Used to tune hyperparameters e select model variants.
- **Test set** (~15%): Used only once at o/a very end to estimate generalisation perparamance.

**Important:** The test set must be kept completely untouched until femal evaluation to avoid dados leakage.

# ## Cross-Validation (k-fold)
For small dadossets, use k-fold cross-validation: split dados emto k folds, traem on k-1, validate on o/a remaememg, e repeat k times. Average o/a perparamance. k=5 or k=10 is common.

# ## Stratified Splittemg
For classification com imbalanced classes, use stratified splits to preserve class proportions em each subset.

# ## Time-Based Splittemg
For time-series dados, split chronologically (traem on past, test on futuro) rao/ar than reomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used para |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced dadossets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screenemg) |
| **F1-score** | Harmonic mean de precision e recall | Imbalanced dadossets, semgle-number metric |
| **AUC-ROC** | Area under o/a ROC curve; tradedef between TPR e FPR | General classifier perparamance emdependent de threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced dadossets |

**Defemitions:**
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
| **R²** (Coefficient de Determemation) | Proportion de variance explaemed | None directly, but sensitive to outliers emdirectly |

# ## Rankemg e Retrieval Metrics
- **Precision@k**: Fraction de relevant items among top-k recommendations.
- **Recall@k**: Fraction de all relevant items that appear em top-k.
- **NDCG** (Normalised Discounted Cumulative Gaem): Accounts para position relevance.
- **Hit Rate**: Wheo/ar a relevant item appears em o/a top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" o/a model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap com referência translations (precision-focused).
- **ROUGE**: Recall-oriented overlap para summarisation.
- **BERTScore**: Semantic similarity usemg contextual embeddemgs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms e stems.

---

# # Evaluation Pitfalls

# ## Dados Leakage
Occurs when emparamation from o/a test set emadvertently emfluences traememg.
- **Prevent:** Never use test dados para feature engemeeremg, normalisation, or hyperparameter tunemg.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfittemg
Model perparams well on traememg dados but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppemg, simplify arquitetura, or collect more dados.

# ## Underfittemg
Model perparams poorly on both traememg e validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced Dados
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rao/ar than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features e target changes over time.
- **Mitigate:** Retraem periodically, monitor perparamance, use drift detection algorithms.

---

# # Hyperparameter Tunemg

- **Grid Search**: Exhaustively try all combemations de a predefemed set de hyperparameters. Simple but computationally expensive.
- **Reom Search**: Sample reom combemations from distributions. More efficient than grid search para high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model de o/a objective function e selects hyperparameters emtelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tunemg**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps para distributed tunemg.

**Suggested search ranges para common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learnemg rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number de layers (NN) | 2 to 6 |
| Number de neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection e Validation

1. **Baseleme model**: Start com a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Ceidate models**: Traem multiple model families (e.g., Reom Forest, XGBoost, Neural Rede).
3. **Cross-validate** each ceidate on o/a validation set.
4. **Compare metrics** (com confidence emtervals) e select o/a best ceidate.
5. **Femal evaluation** on o/a held-out test set.
6. **Error analysis**: Look at exemplos o/a model gets wrong. Identify patterns (e.g., rare classes, ambiguous emputs) e feed emsights back emto dados preparation or feature engemeeremg.

---

# # Implantação e Monitoremg

# ## Servemg Patterns
- **Batch emference**: Process large volumes de dados defleme (e.g., nightly recommendations).
- **Onleme emference**: Real-time predictions via API (e.g., credit scoremg, fraud detection).
- **Streamemg emference**: Event-driven, real-time com low latency (e.g., IoT sensor alerts).

# ## Model Monitoremg
- **Perparamance monitoremg**: Track accuracy/F1 over time on live dados (when ground truth is available).
- **Dados drift**: Monitor changes em emput feature distributions (e.g., usemg PSI – Population Stability Index).
- **Concept drift**: Monitor changes em o/a relationship between emputs e outputs.
- **Prediction drift**: Track o/a distribution de predicted outputs.
- **Latency e throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggemg e Alertemg
- Log all prediction requests e responses (com anonymisation).
- Set alerts para:
  - Significant drop em perparamance.
  - High percentage de missemg or emvalid emputs.
  - Model outputs outside expected bounds.

# ## Model Versionemg e Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store e version models, metadados, e evaluation results.
- Store o/a traememg code e dados version (via DVC or Git LFS) alongside o/a model.

---

# # Practical Workflow Checklist

- [ ] Problem framed e success metric defemed.
- [ ] Dados exploration perparamed (missemg values, outliers, distribution).
- [ ] Traem/validation/test split created (stratified if needed).
- [ ] Baseleme model established.
- [ ] Ceidate models traemed e validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Femal evaluation on test set.
- [ ] Error analysis perparamed.
- [ ] Implantação plan ready (servemg emfrastructure).
- [ ] Monitoremg dashboard set up.
- [ ] Documentation (dados card, model card) completed.