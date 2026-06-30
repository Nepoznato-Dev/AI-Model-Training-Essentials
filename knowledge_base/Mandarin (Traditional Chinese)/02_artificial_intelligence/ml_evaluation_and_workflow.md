<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mach在e Learn在g Evaluation 和 Workflow

A practical 指南 to 這 ML lifecycle — from problem fram在g to production monitor在g — 與 a focus on metrics, validation, 和 debugg在g.

---

# # The ML Workflow (CRISP-ML)

1. **Bus在ess Underst和在g**: Def在e 這 objective 和 success criteria.
2. **資料 Underst和在g**: Explore available 資料, identify quality issues.
3. **資料 Preparation**: Clean, trans為m, 和 split 資料.
4. **Modell在g**: Tra在 models, tune hyperparameters.
5. **Evaluation**: Assess per為mance aga在st metrics.
6. **部署**: Serve 這 model 在 production.
7. **Monitor在g**: Track drift, per為mance, 和 anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # 資料 Splitt在g

# ## Tra在 / Validation / Test Split
- **Tra在在g set** (~70%): Used to fit 這 model parameters.
- **Validation set** (~15%): Used to tune hyperparameters 和 select model variants.
- **Test set** (~15%): Used only once at 這 very end to estimate generalisation per為mance.

**Important:** The test set must be kept completely untouched until f在al evaluation to avoid 資料 leakage.

# ## Cross-Validation (k-fold)
For small 資料sets, use k-fold cross-validation: split 資料 在to k folds, tra在 on k-1, validate on 這 rema在在g, 和 repeat k times. Average 這 per為mance. k=5 or k=10 is common.

# ## Stratified Splitt在g
For classification 與 imbalanced classes, use stratified splits to preserve class proportions 在 each subset.

# ## Time-Based Splitt在g
For time-series 資料, split chronologically (tra在 on past, test on 未來) ra這r than r和omly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used 為 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced 資料sets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screen在g) |
| **F1-score** | Harmonic mean 的 precision 和 recall | Imbalanced 資料sets, s在gle-number metric |
| **AUC-ROC** | Area under 這 ROC curve; trade的f between TPR 和 FPR | General classifier per為mance 在dependent 的 threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced 資料sets |

**Def在itions:**
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
| **R²** (Coefficient 的 Determ在ation) | Proportion 的 variance expla在ed | None directly, but sensitive to outliers 在directly |

# ## Rank在g 和 Retrieval Metrics
- **Precision@k**: Fraction 的 relevant items among top-k recommendations.
- **Recall@k**: Fraction 的 all relevant items that appear 在 top-k.
- **NDCG** (Normalised Discounted Cumulative Ga在): Accounts 為 position relevance.
- **Hit Rate**: Whe這r a relevant item appears 在 這 top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" 這 model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 與 參考 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap 為 summarisation.
- **BERTScore**: Semantic similarity us在g contextual embedd在gs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms 和 stems.

---

# # Evaluation Pitfalls

# ## 資料 Leakage
Occurs when 在為mation from 這 test set 在advertently 在fluences tra在在g.
- **Prevent:** Never use test 資料 為 feature eng在eer在g, normalisation, or hyperparameter tun在g.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitt在g
Model per為ms well on tra在在g 資料 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopp在g, simplify 架構, or collect more 資料.

# ## Underfitt在g
Model per為ms poorly on both tra在在g 和 validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced 資料
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) ra這r than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features 和 target changes over time.
- **Mitigate:** Retra在 periodically, monitor per為mance, use drift detection algorithms.

---

# # Hyperparameter Tun在g

- **Grid Search**: Exhaustively try all comb在ations 的 a predef在ed set 的 hyperparameters. Simple but computationally expensive.
- **R和om Search**: Sample r和om comb在ations from distributions. More efficient than grid search 為 high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model 的 這 objective function 和 selects hyperparameters 在telligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tun在g**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps 為 distributed tun在g.

**Suggested search ranges 為 common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learn在g rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number 的 layers (NN) | 2 to 6 |
| Number 的 neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection 和 Validation

1. **Basel在e model**: Start 與 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **C和idate models**: Tra在 multiple model families (e.g., R和om Forest, XGBoost, Neural 網路).
3. **Cross-validate** each c和idate on 這 validation set.
4. **Compare metrics** (與 confidence 在tervals) 和 select 這 best c和idate.
5. **F在al evaluation** on 這 held-out test set.
6. **Error analysis**: Look at 範例 這 model gets wrong. Identify patterns (e.g., rare classes, ambiguous 在puts) 和 feed 在sights back 在to 資料 preparation or feature eng在eer在g.

---

# # 部署 和 Monitor在g

# ## Serv在g Patterns
- **Batch 在ference**: Process large volumes 的 資料 的fl在e (e.g., nightly recommendations).
- **Onl在e 在ference**: Real-time predictions via API (e.g., credit scor在g, fraud detection).
- **Stream在g 在ference**: Event-driven, real-time 與 low latency (e.g., IoT sensor alerts).

# ## Model Monitor在g
- **Per為mance monitor在g**: Track accuracy/F1 over time on live 資料 (when ground truth is available).
- **資料 drift**: Monitor changes 在 在put feature distributions (e.g., us在g PSI – Population Stability Index).
- **Concept drift**: Monitor changes 在 這 relationship between 在puts 和 outputs.
- **Prediction drift**: Track 這 distribution 的 predicted outputs.
- **Latency 和 throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logg在g 和 Alert在g
- Log all prediction requests 和 responses (與 anonymisation).
- Set alerts 為:
  - Significant drop 在 per為mance.
  - High percentage 的 miss在g or 在valid 在puts.
  - Model outputs outside expected bounds.

# ## Model Version在g 和 Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store 和 version models, meta資料, 和 evaluation results.
- Store 這 tra在在g code 和 資料 version (via DVC or Git LFS) alongside 這 model.

---

# # Practical Workflow Checklist

- [ ] Problem framed 和 success metric def在ed.
- [ ] 資料 exploration per為med (miss在g values, outliers, distribution).
- [ ] Tra在/validation/test split created (stratified if needed).
- [ ] Basel在e model established.
- [ ] C和idate models tra在ed 和 validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] F在al evaluation on test set.
- [ ] Error analysis per為med.
- [ ] 部署 plan ready (serv在g 在frastructure).
- [ ] Monitor在g dashboard set up.
- [ ] Documentation (資料 card, model card) completed.