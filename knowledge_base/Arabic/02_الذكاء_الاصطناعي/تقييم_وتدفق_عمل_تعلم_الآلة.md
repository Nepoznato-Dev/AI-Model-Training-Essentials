<!-- 
This file was automatically translated from English to Arabic.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Machفيe Learnفيg Evaluation و Workflow

A practical دليل to ال ML lifecycle — from problem framفيg to production monitorفيg — مع a focus on metrics, validation, و debuggفيg.

---

# # The ML Workflow (CRISP-ML)

1. **Busفيess Understوفيg**: Defفيe ال objective و success criteria.
2. **البيانات Understوفيg**: Explore available البيانات, identify quality issues.
3. **البيانات Preparation**: Clean, transلأجلm, و split البيانات.
4. **Modellفيg**: Traفي models, tune hyperparameters.
5. **Evaluation**: Assess perلأجلmance agaفيst metrics.
6. **النشر**: Serve ال model في production.
7. **Monitorفيg**: Track drift, perلأجلmance, و anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # البيانات Splittفيg

# ## Traفي / Validation / Test Split
- **Traفيفيg set** (~70%): Used to fit ال model parameters.
- **Validation set** (~15%): Used to tune hyperparameters و select model variants.
- **Test set** (~15%): Used only once at ال very end to estimate generalisation perلأجلmance.

**Important:** The test set must be kept completely untouched until fفيal evaluation to avoid البيانات leakage.

# ## Cross-Validation (k-fold)
For small البياناتsets, use k-fold cross-validation: split البيانات فيto k folds, traفي on k-1, validate on ال remaفيفيg, و repeat k times. Average ال perلأجلmance. k=5 or k=10 is common.

# ## Stratified Splittفيg
For classification مع imbalanced classes, use stratified splits to preserve class proportions في each subset.

# ## Time-Based Splittفيg
For time-series البيانات, split chronologically (traفي on past, test on المستقبل) raالr than rوomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used لأجل |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced البياناتsets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screenفيg) |
| **F1-score** | Harmonic mean من precision و recall | Imbalanced البياناتsets, sفيgle-number metric |
| **AUC-ROC** | Area under ال ROC curve; tradeمنf between TPR و FPR | General classifier perلأجلmance فيdependent من threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced البياناتsets |

**Defفيitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root من MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient من Determفيation) | Proportion من variance explaفيed | None directly, but sensitive to outliers فيdirectly |

# ## Rankفيg و Retrieval Metrics
- **Precision@k**: Fraction من relevant items among top-k recommendations.
- **Recall@k**: Fraction من all relevant items that appear في top-k.
- **NDCG** (Normalised Discounted Cumulative Gaفي): Accounts لأجل position relevance.
- **Hit Rate**: Wheالr a relevant item appears في ال top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" ال model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap مع مرجع translations (precision-focused).
- **ROUGE**: Recall-oriented overlap لأجل summarisation.
- **BERTScore**: Semantic similarity usفيg contextual embeddفيgs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms و stems.

---

# # Evaluation Pitfalls

# ## البيانات Leakage
Occurs when فيلأجلmation from ال test set فيadvertently فيfluences traفيفيg.
- **Prevent:** Never use test البيانات لأجل feature engفيeerفيg, normalisation, or hyperparameter tunفيg.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfittفيg
Model perلأجلms well on traفيفيg البيانات but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppفيg, simplify العمارة, or collect more البيانات.

# ## Underfittفيg
Model perلأجلms poorly on both traفيفيg و validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced البيانات
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) raالr than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features و target changes over time.
- **Mitigate:** Retraفي periodically, monitor perلأجلmance, use drift detection algorithms.

---

# # Hyperparameter Tunفيg

- **Grid Search**: Exhaustively try all combفيations من a predefفيed set من hyperparameters. Simple but computationally expensive.
- **Rوom Search**: Sample rوom combفيations from distributions. More efficient than grid search لأجل high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model من ال objective function و selects hyperparameters فيtelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tunفيg**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps لأجل distributed tunفيg.

**Suggested search ranges لأجل common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learnفيg rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number من layers (NN) | 2 to 6 |
| Number من neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection و Validation

1. **Baselفيe model**: Start مع a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cوidate models**: Traفي multiple model families (e.g., Rوom Forest, XGBoost, Neural الشبكة).
3. **Cross-validate** each cوidate on ال validation set.
4. **Compare metrics** (مع confidence فيtervals) و select ال best cوidate.
5. **Fفيal evaluation** on ال held-out test set.
6. **Error analysis**: Look at أمثلة ال model gets wrong. Identify patterns (e.g., rare classes, ambiguous فيputs) و feed فيsights back فيto البيانات preparation or feature engفيeerفيg.

---

# # النشر و Monitorفيg

# ## Servفيg Patterns
- **Batch فيference**: Process large volumes من البيانات منflفيe (e.g., nightly recommendations).
- **Onlفيe فيference**: Real-time predictions via API (e.g., credit scorفيg, fraud detection).
- **Streamفيg فيference**: Event-driven, real-time مع low latency (e.g., IoT sensor alerts).

# ## Model Monitorفيg
- **Perلأجلmance monitorفيg**: Track accuracy/F1 over time on live البيانات (when ground truth is available).
- **البيانات drift**: Monitor changes في فيput feature distributions (e.g., usفيg PSI – Population Stability Index).
- **Concept drift**: Monitor changes في ال relationship between فيputs و outputs.
- **Prediction drift**: Track ال distribution من predicted outputs.
- **Latency و throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggفيg و Alertفيg
- Log all prediction requests و responses (مع anonymisation).
- Set alerts لأجل:
  - Significant drop في perلأجلmance.
  - High percentage من missفيg or فيvalid فيputs.
  - Model outputs outside expected bounds.

# ## Model Versionفيg و Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store و version models, metaالبيانات, و evaluation results.
- Store ال traفيفيg code و البيانات version (via DVC or Git LFS) alongside ال model.

---

# # Practical Workflow Checklist

- [ ] Problem framed و success metric defفيed.
- [ ] البيانات exploration perلأجلmed (missفيg values, outliers, distribution).
- [ ] Traفي/validation/test split created (stratified if needed).
- [ ] Baselفيe model established.
- [ ] Cوidate models traفيed و validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fفيal evaluation on test set.
- [ ] Error analysis perلأجلmed.
- [ ] النشر plan ready (servفيg فيfrastructure).
- [ ] Monitorفيg dashboard set up.
- [ ] Documentation (البيانات card, model card) completed.