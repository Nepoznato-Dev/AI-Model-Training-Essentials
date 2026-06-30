<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mache Learn Evaluation 和 Workflow

A practical 指南 to 這 機器學習 lifecycle — from problem fram to production monitor — 與 a focus on metrics, validation, 和 debugg.

---

# # The 機器學習 Workflow (CRISP-機器學習)

1. **Buss Underst和**: Defe 這 objective 和 success criteria.
2. **資料 Underst和**: 探索 available 資料, identify quality issues.
3. **資料 Preparation**: Clean, trans為m, 和 split 資料.
4. **Modell**: Tra models, tune hyperparameters.
5. **Evaluation**: Assess per為mance 對照 metrics.
6. **部署**: Serve 這 model production.
7. **Monitor**: Track drift, per為mance, 和 anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # 資料 Splitt

# ## Tra / Validation / Test Split
- **Tra set** (~70%): Used to fit 這 model parameters.
- **Validation set** (~15%): Used to tune hyperparameters 和 select model variants.
- **Test set** (~15%): Used only once at 這 very end to estimate generalisation per為mance.

**Important:** The test set must be kept completely untouched until fal evaluation to avoid 資料 leakage.

# ## Cross-Validation (k-fold)
For small 資料sets, use k-fold cross-validation: split 資料 到 k folds, tra on k-1, validate on 這 rema, 和 repeat k times. Average 這 per為mance. k=5 or k=10 is common.

# ## Stratified Splitt
For classification 與 imbalanced classes, use stratified splits to preserve class proportions each subset.

# ## Time-Based Splitt
For time-series 資料, split chronologically (tra on past, test on 未來) ra這r than r和omly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used 為 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced 資料sets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screen) |
| **F1-score** | Harmonic mean 的 precision 和 recall | Imbalanced 資料sets, sle-number metric |
| **AUC-ROC** | Area under 這 ROC curve; trade的f between TPR 和 FPR | General classifier per為mance dependent 的 threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced 資料sets |

**Defitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root 的 MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient 的 Determation) | Proportion 的 variance explaed | None directly, but sensitive to outliers directly |

# ## Rank 和 Retrieval Metrics
- **Precision@k**: Fraction 的 relevant items among top-k recommendations.
- **Recall@k**: Fraction 的 all relevant items that appear top-k.
- **NDCG** (Normalised Discounted Cumulative Ga): Accounts 為 position relevance.
- **Hit Rate**: Whe這r a relevant item appears 這 top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" 這 model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 與 參考 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap 為 summarisation.
- **BERTScore**: Semantic similarity us contextual embedds (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms 和 stems.

---

# # Evaluation Pitfalls

# ## 資料 Leakage
Occurs when 為mation from 這 test set advertently fluences tra.
- **Prevent:** Never use test 資料 為 feature engeer, normalisation, or hyperparameter tun.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitt
Model per為ms well on tra 資料 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopp, simplify 架構, or collect more 資料.

# ## Underfitt
Model per為ms poorly on both tra 和 validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced 資料
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) ra這r than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features 和 target changes over time.
- **Mitigate:** Retra periodically, monitor per為mance, use drift detection algorithms.

---

# # Hyperparameter Tun

- **Grid Search**: Exhaustively try all combations 的 a predefed set 的 hyperparameters. Simple but computationally expensive.
- **R和om Search**: Sample r和om combations from distributions. More efficient than grid search 為 high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model 的 這 objective function 和 selects hyperparameters telligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tun**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps 為 distributed tun.

**Suggested search ranges 為 common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learn rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number 的 layers (NN) | 2 to 6 |
| Number 的 neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection 和 Validation

1. **Basele model**: Start 與 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **C和idate models**: Tra multiple model families (e.g., R和om Forest, XGBoost, Neural 網路).
3. **Cross-validate** each c和idate on 這 validation set.
4. **Compare metrics** (與 confidence tervals) 和 select 這 best c和idate.
5. **Fal evaluation** on 這 held-out test set.
6. **Error analysis**: Look at 範例 這 model gets wrong. Identify patterns (e.g., rare classes, ambiguous puts) 和 feed sights back 到 資料 preparation or feature engeer.

---

# # 部署 和 Monitor

# ## Serv Patterns
- **Batch ference**: Process large volumes 的 資料 的fle (e.g., nightly recommendations).
- **Onle ference**: Real-time predictions via API (e.g., credit scor, fraud detection).
- **Stream ference**: Event-driven, real-time 與 low latency (e.g., IoT sensor alerts).

# ## Model Monitor
- **Per為mance monitor**: Track accuracy/F1 over time on live 資料 (when ground truth is available).
- **資料 drift**: Monitor changes put feature distributions (e.g., us PSI – Population Stability Index).
- **Concept drift**: Monitor changes 這 relationship between puts 和 outputs.
- **Prediction drift**: Track 這 distribution 的 predicted outputs.
- **Latency 和 throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logg 和 Alert
- Log all prediction requests 和 responses (與 anonymisation).
- Set alerts 為:
 - Significant drop per為mance.
 - High percentage 的 miss or valid puts.
 - Model outputs outside expected bounds.

# ## Model Version 和 Registry
- Use a model registry (e.g., 機器學習flow, Weights & Biases, Sagemaker Model Registry) to store 和 version models, meta資料, 和 evaluation results.
- Store 這 tra code 和 資料 version (via DVC or Git LFS) alongside 這 model.

---

# # Practical Workflow Checklist

- [ ] Problem framed 和 success metric defed.
- [ ] 資料 exploration per為med (miss values, outliers, distribution).
- [ ] Tra/validation/test split created (stratified if needed).
- [ ] Basele model established.
- [ ] C和idate models traed 和 validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fal evaluation on test set.
- [ ] Error analysis per為med.
- [ ] 部署 plan ready (serv frastructure).
- [ ] Monitor dashboard set up.
- [ ] Documentation (資料 card, model card) completed.