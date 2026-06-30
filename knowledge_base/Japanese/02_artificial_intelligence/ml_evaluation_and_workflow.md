<!-- 
This file was automatically translated from English to Japanese.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mache Learn Evaluation Workflow

A practical ガイド to 機械学習 lifecycle — from problem fram to production monitor — a focus on metrics, validation, debugg.

---

# # The 機械学習 Workflow (CRISP-機械学習)

1. **Buss Underst**: Defe objective success criteria.
2. **データ Underst**: 探索 available データ, identify quality issues.
3. **データ Preparation**: Clean, transにm, split データ.
4. **Modell**: Tra models, tune hyperparameters.
5. **Evaluation**: Assess perにmance 対照 metrics.
6. **デプロイ**: Serve model production.
7. **Monitor**: Track drift, perにmance, anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # データ Splitt

# ## Tra / Validation / Test Split
- **Tra set** (~70%): Used to fit model parameters.
- **Validation set** (~15%): Used to tune hyperparameters select model variants.
- **Test set** (~15%): Used only once at very end to estimate generalisation perにmance.

**Important:** The test set must be kept completely untouched until fal evaluation to avoid データ leakage.

# ## Cross-Validation (k-fold)
For small データsets, use k-fold cross-validation: split データ へ k folds, tra on k-1, validate on rema, repeat k times. Average perにmance. k=5 or k=10 is common.

# ## Stratified Splitt
For classification imbalanced classes, use stratified splits to preserve class proportions each subset.

# ## Time-Based Splitt
For time-series データ, split chronologically (tra on past, test on 未来) rar than romly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used に |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced データsets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screen) |
| **F1-score** | Harmonic mean precision recall | Imbalanced データsets, sle-number metric |
| **AUC-ROC** | Area under ROC curve; tradef between TPR FPR | General classifier perにmance dependent threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced データsets |

**Defitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient Determation) | Proportion variance explaed | None directly, but sensitive to outliers directly |

# ## Rank Retrieval Metrics
- **Precision@k**: Fraction relevant items among top-k recommendations.
- **Recall@k**: Fraction all relevant items that appear top-k.
- **NDCG** (Normalised Discounted Cumulative Ga): Accounts に position relevance.
- **Hit Rate**: Wher a relevant item appears top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap リファレンス translations (precision-focused).
- **ROUGE**: Recall-oriented overlap に summarisation.
- **BERTScore**: Semantic similarity us contextual embedds (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms stems.

---

# # Evaluation Pitfalls

# ## データ Leakage
Occurs when にmation from test set advertently fluences tra.
- **Prevent:** Never use test データ に feature engeer, normalisation, or hyperparameter tun.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitt
Model perにms well on tra データ but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopp, simplify アーキテクチャ, or collect more データ.

# ## Underfitt
Model perにms poorly on both tra validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced データ
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rar than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features target changes over time.
- **Mitigate:** Retra periodically, monitor perにmance, use drift detection algorithms.

---

# # Hyperparameter Tun

- **Grid Search**: Exhaustively try all combations a predefed set hyperparameters. Simple but computationally expensive.
- **Rom Search**: Sample rom combations from distributions. More efficient than grid search に high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model objective function selects hyperparameters telligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tun**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps に distributed tun.

**Suggested search ranges に common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learn rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number layers (NN) | 2 to 6 |
| Number neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection Validation

1. **Basele model**: から始める a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cidate models**: Tra multiple model families (e.g., Rom Forest, XGBoost, Neural ネットワーク).
3. **Cross-validate** each cidate on validation set.
4. **Compare metrics** ( confidence tervals) select best cidate.
5. **Fal evaluation** on held-out test set.
6. **Error analysis**: Look at 例 model gets wrong. Identify patterns (e.g., rare classes, ambiguous puts) feed sights back へ データ preparation or feature engeer.

---

# # デプロイ Monitor

# ## Serv Patterns
- **Batch ference**: Process large volumes データ fle (e.g., nightly recommendations).
- **Onle ference**: Real-time predictions via API (e.g., credit scor, fraud detection).
- **Stream ference**: Event-driven, real-time low latency (e.g., IoT sensor alerts).

# ## Model Monitor
- **Perにmance monitor**: Track accuracy/F1 over time on live データ (when ground truth is available).
- **データ drift**: Monitor changes put feature distributions (e.g., us PSI – Population Stability Index).
- **Concept drift**: Monitor changes relationship between puts outputs.
- **Prediction drift**: Track distribution predicted outputs.
- **Latency throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logg Alert
- Log all prediction requests responses ( anonymisation).
- Set alerts に:
 - Significant drop perにmance.
 - High percentage miss or valid puts.
 - Model outputs outside expected bounds.

# ## Model Version Registry
- Use a model registry (e.g., 機械学習flow, Weights & Biases, Sagemaker Model Registry) to store version models, メタデータ, evaluation results.
- Store tra code データ version (via DVC or Git LFS) alongside model.

---

# # Practical Workflow Checklist

- [ ] Problem framed success metric defed.
- [ ] データ exploration perにmed (miss values, outliers, distribution).
- [ ] Tra/validation/test split created (stratified if needed).
- [ ] Basele model established.
- [ ] Cidate models traed validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fal evaluation on test set.
- [ ] Error analysis perにmed.
- [ ] デプロイ plan ready (serv frastructure).
- [ ] Monitor dashboard set up.
- [ ] Documentation (データ card, model card) completed.