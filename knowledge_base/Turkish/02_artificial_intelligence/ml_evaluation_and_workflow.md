<!-- 
This file was automatically translated from English to Turkish.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Machiçiçindedee Learnİçinde Evaluation ve Workflow

A practical rehber to bu ML lifecycle — from problem framİçinde to production monitorİçinde — ile a focus on metrics, validation, ve debuggİçinde.

---

# # The ML Workflow (CRISP-ML)

1. **Busiçiçindedeess Understveİçinde**: Defiçiçindedee bu objective ve success criteria.
2. **Veri Understveİçinde**: Explore available veri, identify quality issues.
3. **Veri Preparation**: Clean, transiçinm, ve split veri.
4. **Modellİçinde**: Traiçiçindede models, tune hyperparameters.
5. **Evaluation**: Assess periçinmance agaiçiçindedest metrics.
6. **Dağıtım**: Serve bu model içiçindede production.
7. **Monitorİçinde**: Track drift, periçinmance, ve anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # Veri Splittİçinde

# ## Traiçiçindede / Validation / Test Split
- **Traiçiçindedeİçinde set** (~70%): Used to fit bu model parameters.
- **Validation set** (~15%): Used to tune hyperparameters ve select model variants.
- **Test set** (~15%): Used only once at bu very end to estimate generalisation periçinmance.

**Important:** The test set must be kept completely untouched until fiçiçindedeal evaluation to avoid veri leakage.

# ## Cross-Validation (k-fold)
For small verisets, use k-fold cross-validation: split veri içiçindedeto k folds, traiçiçindede on k-1, validate on bu remaiçiçindedeİçinde, ve repeat k times. Average bu periçinmance. k=5 or k=10 is common.

# ## Stratified Splittİçinde
For classification ile imbalanced classes, use stratified splits to preserve class proportions içiçindede each subset.

# ## Time-Based Splittİçinde
For time-series veri, split chronologically (traiçiçindede on past, test on gelecek) rabur than rveomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used için |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced verisets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screenİçinde) |
| **F1-score** | Harmonic mean içiçindede precision ve recall | Imbalanced verisets, sİçindele-number metric |
| **AUC-ROC** | Area under bu ROC curve; tradeiçiçindedef between TPR ve FPR | General classifier periçinmance içiçindededependent içiçindede threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced verisets |

**Defiçiçindedeitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root içiçindede MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient içiçindede Determiçiçindedeation) | Proportion içiçindede variance explaiçiçindedeed | None directly, but sensitive to outliers içiçindededirectly |

# ## Rankİçinde ve Retrieval Metrics
- **Precision@k**: Fraction içiçindede relevant items among top-k recommendations.
- **Recall@k**: Fraction içiçindede all relevant items that appear içiçindede top-k.
- **NDCG** (Normalised Discounted Cumulative Gaiçiçindede): Accounts için position relevance.
- **Hit Rate**: Whebur a relevant item appears içiçindede bu top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" bu model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap ile referans translations (precision-focused).
- **ROUGE**: Recall-oriented overlap için summarisation.
- **BERTScore**: Semantic similarity usİçinde contextual embeddİçindes (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms ve stems.

---

# # Evaluation Pitfalls

# ## Veri Leakage
Occurs when içiçindedeiçinmation from bu test set içiçindedeadvertently içiçindedefluences traiçiçindedeİçinde.
- **Prevent:** Never use test veri için feature engiçiçindedeeerİçinde, normalisation, or hyperparameter tunİçinde.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfittİçinde
Model periçinms well on traiçiçindedeİçinde veri but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppİçinde, simplify mimari, or collect more veri.

# ## Underfittİçinde
Model periçinms poorly on both traiçiçindedeİçinde ve validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced Veri
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rabur than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features ve target changes over time.
- **Mitigate:** Retraiçiçindede periodically, monitor periçinmance, use drift detection algorithms.

---

# # Hyperparameter Tunİçinde

- **Grid Search**: Exhaustively try all combiçiçindedeations içiçindede a predefiçiçindedeed set içiçindede hyperparameters. Simple but computationally expensive.
- **Rveom Search**: Sample rveom combiçiçindedeations from distributions. More efficient than grid search için high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model içiçindede bu objective function ve selects hyperparameters içiçindedetelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tunİçinde**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps için distributed tunİçinde.

**Suggested search ranges için common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learnİçinde rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number içiçindede layers (NN) | 2 to 6 |
| Number içiçindede neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection ve Validation

1. **Baseliçiçindedee model**: Start ile a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cveidate models**: Traiçiçindede multiple model families (e.g., Rveom Forest, XGBoost, Neural Ağ).
3. **Cross-validate** each cveidate on bu validation set.
4. **Compare metrics** (ile confidence içiçindedetervals) ve select bu best cveidate.
5. **Fiçiçindedeal evaluation** on bu held-out test set.
6. **Error analysis**: Look at örnekler bu model gets wrong. Identify patterns (e.g., rare classes, ambiguous içiçindedeputs) ve feed içiçindedesights back içiçindedeto veri preparation or feature engiçiçindedeeerİçinde.

---

# # Dağıtım ve Monitorİçinde

# ## Servİçinde Patterns
- **Batch içiçindedeference**: Process large volumes içiçindede veri içiçindedefliçiçindedee (e.g., nightly recommendations).
- **Onliçiçindedee içiçindedeference**: Real-time predictions via API (e.g., credit scorİçinde, fraud detection).
- **Streamİçinde içiçindedeference**: Event-driven, real-time ile low latency (e.g., IoT sensor alerts).

# ## Model Monitorİçinde
- **Periçinmance monitorİçinde**: Track accuracy/F1 over time on live veri (when ground truth is available).
- **Veri drift**: Monitor changes içiçindede içiçindedeput feature distributions (e.g., usİçinde PSI – Population Stability Index).
- **Concept drift**: Monitor changes içiçindede bu relationship between içiçindedeputs ve outputs.
- **Prediction drift**: Track bu distribution içiçindede predicted outputs.
- **Latency ve throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggİçinde ve Alertİçinde
- Log all prediction requests ve responses (ile anonymisation).
- Set alerts için:
  - Significant drop içiçindede periçinmance.
  - High percentage içiçindede missİçinde or içiçindedevalid içiçindedeputs.
  - Model outputs outside expected bounds.

# ## Model Versionİçinde ve Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store ve version models, metaveri, ve evaluation results.
- Store bu traiçiçindedeİçinde code ve veri version (via DVC or Git LFS) alongside bu model.

---

# # Practical Workflow Checklist

- [ ] Problem framed ve success metric defiçiçindedeed.
- [ ] Veri exploration periçinmed (missİçinde values, outliers, distribution).
- [ ] Traiçiçindede/validation/test split created (stratified if needed).
- [ ] Baseliçiçindedee model established.
- [ ] Cveidate models traiçiçindedeed ve validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fiçiçindedeal evaluation on test set.
- [ ] Error analysis periçinmed.
- [ ] Dağıtım plan ready (servİçinde içiçindedefrastructure).
- [ ] Monitorİçinde dashboard set up.
- [ ] Documentation (veri card, model card) completed.