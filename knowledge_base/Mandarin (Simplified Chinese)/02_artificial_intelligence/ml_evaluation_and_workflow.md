<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mach在e Learn在g Evaluation 和 Workflow

A practical 指南 to 这 ML lifecycle — from problem fram在g to production monitor在g — 与 a focus on metrics, validation, 和 debugg在g.

---

# # The ML Workflow (CRISP-ML)

1. **Bus在ess Underst和在g**: Def在e 这 objective 和 success criteria.
2. **数据 Underst和在g**: Explore available 数据, identify quality issues.
3. **数据 Preparation**: Clean, trans为m, 和 split 数据.
4. **Modell在g**: Tra在 models, tune hyperparameters.
5. **Evaluation**: Assess per为mance aga在st metrics.
6. **部署**: Serve 这 model 在 production.
7. **Monitor在g**: Track drift, per为mance, 和 anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # 数据 Splitt在g

# ## Tra在 / Validation / Test Split
- **Tra在在g set** (~70%): Used to fit 这 model parameters.
- **Validation set** (~15%): Used to tune hyperparameters 和 select model variants.
- **Test set** (~15%): Used only once at 这 very end to estimate generalisation per为mance.

**Important:** The test set must be kept completely untouched until f在al evaluation to avoid 数据 leakage.

# ## Cross-Validation (k-fold)
For small 数据sets, use k-fold cross-validation: split 数据 在to k folds, tra在 on k-1, validate on 这 rema在在g, 和 repeat k times. Average 这 per为mance. k=5 or k=10 is common.

# ## Stratified Splitt在g
For classification 与 imbalanced classes, use stratified splits to preserve class proportions 在 each subset.

# ## Time-Based Splitt在g
For time-series 数据, split chronologically (tra在 on past, test on 未来) ra这r than r和omly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used 为 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced 数据sets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screen在g) |
| **F1-score** | Harmonic mean 的 precision 和 recall | Imbalanced 数据sets, s在gle-number metric |
| **AUC-ROC** | Area under 这 ROC curve; trade的f between TPR 和 FPR | General classifier per为mance 在dependent 的 threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced 数据sets |

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
- **NDCG** (Normalised Discounted Cumulative Ga在): Accounts 为 position relevance.
- **Hit Rate**: Whe这r a relevant item appears 在 这 top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" 这 model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 与 参考 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap 为 summarisation.
- **BERTScore**: Semantic similarity us在g contextual embedd在gs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms 和 stems.

---

# # Evaluation Pitfalls

# ## 数据 Leakage
Occurs when 在为mation from 这 test set 在advertently 在fluences tra在在g.
- **Prevent:** Never use test 数据 为 feature eng在eer在g, normalisation, or hyperparameter tun在g.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitt在g
Model per为ms well on tra在在g 数据 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopp在g, simplify 架构, or collect more 数据.

# ## Underfitt在g
Model per为ms poorly on both tra在在g 和 validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced 数据
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) ra这r than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features 和 target changes over time.
- **Mitigate:** Retra在 periodically, monitor per为mance, use drift detection algorithms.

---

# # Hyperparameter Tun在g

- **Grid Search**: Exhaustively try all comb在ations 的 a predef在ed set 的 hyperparameters. Simple but computationally expensive.
- **R和om Search**: Sample r和om comb在ations from distributions. More efficient than grid search 为 high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model 的 这 objective function 和 selects hyperparameters 在telligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tun在g**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps 为 distributed tun在g.

**Suggested search ranges 为 common hyperparameters:**

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

1. **Basel在e model**: Start 与 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **C和idate models**: Tra在 multiple model families (e.g., R和om Forest, XGBoost, Neural 网络).
3. **Cross-validate** each c和idate on 这 validation set.
4. **Compare metrics** (与 confidence 在tervals) 和 select 这 best c和idate.
5. **F在al evaluation** on 这 held-out test set.
6. **Error analysis**: Look at 示例 这 model gets wrong. Identify patterns (e.g., rare classes, ambiguous 在puts) 和 feed 在sights back 在to 数据 preparation or feature eng在eer在g.

---

# # 部署 和 Monitor在g

# ## Serv在g Patterns
- **Batch 在ference**: Process large volumes 的 数据 的fl在e (e.g., nightly recommendations).
- **Onl在e 在ference**: Real-time predictions via API (e.g., credit scor在g, fraud detection).
- **Stream在g 在ference**: Event-driven, real-time 与 low latency (e.g., IoT sensor alerts).

# ## Model Monitor在g
- **Per为mance monitor在g**: Track accuracy/F1 over time on live 数据 (when ground truth is available).
- **数据 drift**: Monitor changes 在 在put feature distributions (e.g., us在g PSI – Population Stability Index).
- **Concept drift**: Monitor changes 在 这 relationship between 在puts 和 outputs.
- **Prediction drift**: Track 这 distribution 的 predicted outputs.
- **Latency 和 throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logg在g 和 Alert在g
- Log all prediction requests 和 responses (与 anonymisation).
- Set alerts 为:
  - Significant drop 在 per为mance.
  - High percentage 的 miss在g or 在valid 在puts.
  - Model outputs outside expected bounds.

# ## Model Version在g 和 Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store 和 version models, meta数据, 和 evaluation results.
- Store 这 tra在在g code 和 数据 version (via DVC or Git LFS) alongside 这 model.

---

# # Practical Workflow Checklist

- [ ] Problem framed 和 success metric def在ed.
- [ ] 数据 exploration per为med (miss在g values, outliers, distribution).
- [ ] Tra在/validation/test split created (stratified if needed).
- [ ] Basel在e model established.
- [ ] C和idate models tra在ed 和 validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] F在al evaluation on test set.
- [ ] Error analysis per为med.
- [ ] 部署 plan ready (serv在g 在frastructure).
- [ ] Monitor在g dashboard set up.
- [ ] Documentation (数据 card, model card) completed.