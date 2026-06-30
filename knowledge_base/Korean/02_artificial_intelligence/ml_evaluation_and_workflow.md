<!-- 
This file was automatically translated from English to Korean.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mache Learn Evaluation Workflow

A practical 가 이 드 to 기계 학습 lifecycle — from problem fram to production monitor — 함께 a focus on metrics, validation, debugg.

---

# # The 기계 학습 Workflow (CRISP-기계 학습)

1. **Buss Underst**: Defe objective success criteria.
2. **데이 터 Underst**: 탐색 available 데이 터, identify quality issues.
3. **데이 터 Preparation**: Clean, transm, split 데이 터.
4. **Modell**: Tra models, tune hyperparameters.
5. **Evaluation**: Assess permance 대조 metrics.
6. **배포**: Serve model production.
7. **Monitor**: Track drift, permance, anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # 데이 터 Splitt

# ## Tra / Validation / Test Split
- **Tra set** (~70%): Used to fit model parameters.
- **Validation set** (~15%): Used to tune hyperparameters select model variants.
- **Test set** (~15%): Used only once at very end to estimate generalisation permance.

**Important:** The test set must be kept completely untouched until fal evaluation to avoid 데이 터 leakage.

# ## Cross-Validation (k-fold)
For small 데이 터sets, use k-fold cross-validation: split 데이 터 로 k folds, tra on k-1, validate on rema, repeat k times. Average permance. k=5 or k=10 is common.

# ## Stratified Splitt
For classification 함께 imbalanced classes, use stratified splits to preserve class proportions each subset.

# ## Time-Based Splitt
For time-series 데이 터, split chronologically (tra on past, test on 미래) rar than romly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced 데이 터sets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screen) |
| **F1-score** | Harmonic mean precision recall | Imbalanced 데이 터sets, sle-number metric |
| **AUC-ROC** | Area under ROC curve; tradef between TPR FPR | General classifier permance dependent threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced 데이 터sets |

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
- **NDCG** (Normalised Discounted Cumulative Ga): Accounts position relevance.
- **Hit Rate**: Wher a relevant item appears top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 함께 참조 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap summarisation.
- **BERTScore**: Semantic similarity us contextual embedds (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms stems.

---

# # Evaluation Pitfalls

# ## 데이 터 Leakage
Occurs when mation from test set advertently fluences tra.
- **Prevent:** Never use test 데이 터 feature engeer, normalisation, or hyperparameter tun.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitt
Model perms well on tra 데이 터 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopp, simplify 아키텍처, or collect more 데이 터.

# ## Underfitt
Model perms poorly on both tra validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced 데이 터
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) rar than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features target changes over time.
- **Mitigate:** Retra periodically, monitor permance, use drift detection algorithms.

---

# # Hyperparameter Tun

- **Grid Search**: Exhaustively try all combations a predefed set hyperparameters. Simple but computationally expensive.
- **Rom Search**: Sample rom combations from distributions. More efficient than grid search high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model objective function selects hyperparameters telligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tun**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps distributed tun.

**Suggested search ranges common hyperparameters:**

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

1. **Basele model**: 시작 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cidate models**: Tra multiple model families (e.g., Rom Forest, XGBoost, Neural 네트워크).
3. **Cross-validate** each cidate on validation set.
4. **Compare metrics** ( 함께 confidence tervals) select best cidate.
5. **Fal evaluation** on held-out test set.
6. **Error analysis**: Look at 예시 model gets wrong. Identify patterns (e.g., rare classes, ambiguous puts) feed sights back 로 데이 터 preparation or feature engeer.

---

# # 배포 Monitor

# ## Serv Patterns
- **Batch ference**: Process large volumes 데이 터 fle (e.g., nightly recommendations).
- **Onle ference**: Real-time predictions via API (e.g., credit scor, fraud detection).
- **Stream ference**: Event-driven, real-time 함께 low latency (e.g., IoT sensor alerts).

# ## Model Monitor
- **Permance monitor**: Track accuracy/F1 over time on live 데이 터 (when ground truth is available).
- **데이 터 drift**: Monitor changes put feature distributions (e.g., us PSI – Population Stability Index).
- **Concept drift**: Monitor changes relationship between puts outputs.
- **Prediction drift**: Track distribution predicted outputs.
- **Latency throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logg Alert
- Log all prediction requests responses ( 함께 anonymisation).
- Set alerts :
 - Significant drop permance.
 - High percentage miss or valid puts.
 - Model outputs outside expected bounds.

# ## Model Version Registry
- Use a model registry (e.g., 기계 학습flow, Weights & Biases, Sagemaker Model Registry) to store version models, 메타데이 터, evaluation results.
- Store tra code 데이 터 version (via DVC or Git LFS) alongside model.

---

# # Practical Workflow Checklist

- [ ] Problem framed success metric defed.
- [ ] 데이 터 exploration permed (miss values, outliers, distribution).
- [ ] Tra/validation/test split created (stratified if needed).
- [ ] Basele model established.
- [ ] Cidate models traed validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fal evaluation on test set.
- [ ] Error analysis permed.
- [ ] 배포 plan ready (serv frastructure).
- [ ] Monitor dashboard set up.
- [ ] Documentation (데이 터 card, model card) completed.