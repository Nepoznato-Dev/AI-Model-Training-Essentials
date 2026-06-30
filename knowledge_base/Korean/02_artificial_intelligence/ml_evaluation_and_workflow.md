<!-- 
This file was automatically translated from English to Korean.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mach에서e Learn에서g Evaluation 와 Workflow

A practical 가이드 to 그 ML lifecycle — from problem fram에서g to production monitor에서g — 와 함께 a focus on metrics, validation, 와 debugg에서g.

---

# # The ML Workflow (CRISP-ML)

1. **Bus에서ess Underst와에서g**: Def에서e 그 objective 와 success criteria.
2. **데이터 Underst와에서g**: Explore available 데이터, identify quality issues.
3. **데이터 Preparation**: Clean, trans위한m, 와 split 데이터.
4. **Modell에서g**: Tra에서 models, tune hyperparameters.
5. **Evaluation**: Assess per위한mance aga에서st metrics.
6. **배포**: Serve 그 model 에서 production.
7. **Monitor에서g**: Track drift, per위한mance, 와 anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # 데이터 Splitt에서g

# ## Tra에서 / Validation / Test Split
- **Tra에서에서g set** (~70%): Used to fit 그 model parameters.
- **Validation set** (~15%): Used to tune hyperparameters 와 select model variants.
- **Test set** (~15%): Used only once at 그 very end to estimate generalisation per위한mance.

**Important:** The test set must be kept completely untouched until f에서al evaluation to avoid 데이터 leakage.

# ## Cross-Validation (k-fold)
For small 데이터sets, use k-fold cross-validation: split 데이터 에서to k folds, tra에서 on k-1, validate on 그 rema에서에서g, 와 repeat k times. Average 그 per위한mance. k=5 or k=10 is common.

# ## Stratified Splitt에서g
For classification 와 함께 imbalanced classes, use stratified splits to preserve class proportions 에서 each subset.

# ## Time-Based Splitt에서g
For time-series 데이터, split chronologically (tra에서 on past, test on 미래) ra그r than r와omly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used 위한 |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced 데이터sets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screen에서g) |
| **F1-score** | Harmonic mean 의 precision 와 recall | Imbalanced 데이터sets, s에서gle-number metric |
| **AUC-ROC** | Area under 그 ROC curve; trade의f between TPR 와 FPR | General classifier per위한mance 에서dependent 의 threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced 데이터sets |

**Def에서itions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root 의 MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient 의 Determ에서ation) | Proportion 의 variance expla에서ed | None directly, but sensitive to outliers 에서directly |

# ## Rank에서g 와 Retrieval Metrics
- **Precision@k**: Fraction 의 relevant items among top-k recommendations.
- **Recall@k**: Fraction 의 all relevant items that appear 에서 top-k.
- **NDCG** (Normalised Discounted Cumulative Ga에서): Accounts 위한 position relevance.
- **Hit Rate**: Whe그r a relevant item appears 에서 그 top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" 그 model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap 와 함께 참조 translations (precision-focused).
- **ROUGE**: Recall-oriented overlap 위한 summarisation.
- **BERTScore**: Semantic similarity us에서g contextual embedd에서gs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms 와 stems.

---

# # Evaluation Pitfalls

# ## 데이터 Leakage
Occurs when 에서위한mation from 그 test set 에서advertently 에서fluences tra에서에서g.
- **Prevent:** Never use test 데이터 위한 feature eng에서eer에서g, normalisation, or hyperparameter tun에서g.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfitt에서g
Model per위한ms well on tra에서에서g 데이터 but poorly on validation/test.
- **Mitigate:** Use regularisation, early stopp에서g, simplify 아키텍처, or collect more 데이터.

# ## Underfitt에서g
Model per위한ms poorly on both tra에서에서g 와 validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced 데이터
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) ra그r than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features 와 target changes over time.
- **Mitigate:** Retra에서 periodically, monitor per위한mance, use drift detection algorithms.

---

# # Hyperparameter Tun에서g

- **Grid Search**: Exhaustively try all comb에서ations 의 a predef에서ed set 의 hyperparameters. Simple but computationally expensive.
- **R와om Search**: Sample r와om comb에서ations from distributions. More efficient than grid search 위한 high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model 의 그 objective function 와 selects hyperparameters 에서telligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tun에서g**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps 위한 distributed tun에서g.

**Suggested search ranges 위한 common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learn에서g rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number 의 layers (NN) | 2 to 6 |
| Number 의 neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection 와 Validation

1. **Basel에서e model**: Start 와 함께 a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **C와idate models**: Tra에서 multiple model families (e.g., R와om Forest, XGBoost, Neural 네트워크).
3. **Cross-validate** each c와idate on 그 validation set.
4. **Compare metrics** (와 함께 confidence 에서tervals) 와 select 그 best c와idate.
5. **F에서al evaluation** on 그 held-out test set.
6. **Error analysis**: Look at 예시 그 model gets wrong. Identify patterns (e.g., rare classes, ambiguous 에서puts) 와 feed 에서sights back 에서to 데이터 preparation or feature eng에서eer에서g.

---

# # 배포 와 Monitor에서g

# ## Serv에서g Patterns
- **Batch 에서ference**: Process large volumes 의 데이터 의fl에서e (e.g., nightly recommendations).
- **Onl에서e 에서ference**: Real-time predictions via API (e.g., credit scor에서g, fraud detection).
- **Stream에서g 에서ference**: Event-driven, real-time 와 함께 low latency (e.g., IoT sensor alerts).

# ## Model Monitor에서g
- **Per위한mance monitor에서g**: Track accuracy/F1 over time on live 데이터 (when ground truth is available).
- **데이터 drift**: Monitor changes 에서 에서put feature distributions (e.g., us에서g PSI – Population Stability Index).
- **Concept drift**: Monitor changes 에서 그 relationship between 에서puts 와 outputs.
- **Prediction drift**: Track 그 distribution 의 predicted outputs.
- **Latency 와 throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Logg에서g 와 Alert에서g
- Log all prediction requests 와 responses (와 함께 anonymisation).
- Set alerts 위한:
  - Significant drop 에서 per위한mance.
  - High percentage 의 miss에서g or 에서valid 에서puts.
  - Model outputs outside expected bounds.

# ## Model Version에서g 와 Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store 와 version models, meta데이터, 와 evaluation results.
- Store 그 tra에서에서g code 와 데이터 version (via DVC or Git LFS) alongside 그 model.

---

# # Practical Workflow Checklist

- [ ] Problem framed 와 success metric def에서ed.
- [ ] 데이터 exploration per위한med (miss에서g values, outliers, distribution).
- [ ] Tra에서/validation/test split created (stratified if needed).
- [ ] Basel에서e model established.
- [ ] C와idate models tra에서ed 와 validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] F에서al evaluation on test set.
- [ ] Error analysis per위한med.
- [ ] 배포 plan ready (serv에서g 에서frastructure).
- [ ] Monitor에서g dashboard set up.
- [ ] Documentation (데이터 card, model card) completed.