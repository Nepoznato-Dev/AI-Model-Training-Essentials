<!-- 
This file was automatically translated from English to Japanese.
Source: ml_evaluation_and_workflow.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Machでe Learnでg Evaluation と Workflow

A practical ガイド to その ML lifecycle — from problem framでg to production monitorでg — と a focus on metrics, validation, と debuggでg.

---

# # The ML Workflow (CRISP-ML)

1. **Busでess Understとでg**: Defでe その objective と success criteria.
2. **データ Understとでg**: Explore available データ, identify quality issues.
3. **データ Preparation**: Clean, transのためにm, と split データ.
4. **Modellでg**: Traで models, tune hyperparameters.
5. **Evaluation**: Assess perのためにmance agaでst metrics.
6. **デプロイ**: Serve その model で production.
7. **Monitorでg**: Track drift, perのためにmance, と anomalies.

This is an iterative loop — you will revisit earlier steps based on evaluation results.

---

# # データ Splittでg

# ## Traで / Validation / Test Split
- **Traででg set** (~70%): Used to fit その model parameters.
- **Validation set** (~15%): Used to tune hyperparameters と select model variants.
- **Test set** (~15%): Used only once at その very end to estimate generalisation perのためにmance.

**Important:** The test set must be kept completely untouched until fでal evaluation to avoid データ leakage.

# ## Cross-Validation (k-fold)
For small データsets, use k-fold cross-validation: split データ でto k folds, traで on k-1, validate on その remaででg, と repeat k times. Average その perのためにmance. k=5 or k=10 is common.

# ## Stratified Splittでg
For classification と imbalanced classes, use stratified splits to preserve class proportions で each subset.

# ## Time-Based Splittでg
For time-series データ, split chronologically (traで on past, test on 未来) raそのr than rとomly.

---

# # Evaluation Metrics

# ## Classification Metrics

| Metric | What it measures | Best used のために |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced データsets |
| **Precision** | TP / (TP + FP) | When false positives are costly (e.g., spam detection) |
| **Recall** | TP / (TP + FN) | When false negatives are costly (e.g., cancer screenでg) |
| **F1-score** | Harmonic mean の precision と recall | Imbalanced データsets, sでgle-number metric |
| **AUC-ROC** | Area under その ROC curve; tradeのf between TPR と FPR | General classifier perのためにmance でdependent の threshold |
| **AUC-PR** | Area under Precision-Recall curve | Highly imbalanced データsets |

**Defでitions:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

# ## Regression Metrics

| Metric | What it measures | Sensitivity to outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Average squared difference | High |
| **RMSE** (Root Mean Squared Error) | Square root の MSE (same units as target) | High |
| **MAE** (Mean Absolute Error) | Average absolute difference | Low |
| **R²** (Coefficient の Determでation) | Proportion の variance explaでed | None directly, but sensitive to outliers でdirectly |

# ## Rankでg と Retrieval Metrics
- **Precision@k**: Fraction の relevant items among top-k recommendations.
- **Recall@k**: Fraction の all relevant items that appear で top-k.
- **NDCG** (Normalised Discounted Cumulative Gaで): Accounts のために position relevance.
- **Hit Rate**: Wheそのr a relevant item appears で その top-k.

# ## Generative / LLM Metrics
- **Perplexity**: How "surprised" その model is by a held-out text (lower is better).
- **BLEU**: n-gram overlap と リファレンス translations (precision-focused).
- **ROUGE**: Recall-oriented overlap のために summarisation.
- **BERTScore**: Semantic similarity usでg contextual embeddでgs (more robust than BLEU).
- **METEOR**: Aligns to WordNet synonyms と stems.

---

# # Evaluation Pitfalls

# ## データ Leakage
Occurs when でのためにmation from その test set でadvertently でfluences traででg.
- **Prevent:** Never use test データ のために feature engでeerでg, normalisation, or hyperparameter tunでg.
- **Detect:** If your model scores suspiciously high, suspect leakage.

# ## Overfittでg
Model perのためにms well on traででg データ but poorly on validation/test.
- **Mitigate:** Use regularisation, early stoppでg, simplify アーキテクチャ, or collect more データ.

# ## Underfittでg
Model perのためにms poorly on both traででg と validation.
- **Mitigate:** Use a more complex model, add features, or reduce regularisation.

# ## Imbalanced データ
- **Mitigate:** Use class weights, oversample (SMOTE), undersample, or use appropriate metrics (F1, AUC-PR) raそのr than accuracy.

# ## Temporal Drift (Concept Drift)
The relationship between features と target changes over time.
- **Mitigate:** Retraで periodically, monitor perのためにmance, use drift detection algorithms.

---

# # Hyperparameter Tunでg

- **Grid Search**: Exhaustively try all combでations の a predefでed set の hyperparameters. Simple but computationally expensive.
- **Rとom Search**: Sample rとom combでations from distributions. More efficient than grid search のために high-dimensional spaces.
- **Bayesian Optimisation**: Builds a probabilistic model の その objective function と selects hyperparameters でtelligently. Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tunでg**: Use tools like Optuna, Ray Tune, or Weights & Biases Sweeps のために distributed tunでg.

**Suggested search ranges のために common hyperparameters:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learnでg rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number の layers (NN) | 2 to 6 |
| Number の neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

# # Model Selection と Validation

1. **Baselでe model**: Start と a simple heuristic or simple model (e.g., logistic regression, mean predictor) to establish a lower bound.
2. **Cとidate models**: Traで multiple model families (e.g., Rとom Forest, XGBoost, Neural ネットワーク).
3. **Cross-validate** each cとidate on その validation set.
4. **Compare metrics** (と confidence でtervals) と select その best cとidate.
5. **Fでal evaluation** on その held-out test set.
6. **Error analysis**: Look at 例 その model gets wrong. Identify patterns (e.g., rare classes, ambiguous でputs) と feed でsights back でto データ preparation or feature engでeerでg.

---

# # デプロイ と Monitorでg

# ## Servでg Patterns
- **Batch でference**: Process large volumes の データ のflでe (e.g., nightly recommendations).
- **Onlでe でference**: Real-time predictions via API (e.g., credit scorでg, fraud detection).
- **Streamでg でference**: Event-driven, real-time と low latency (e.g., IoT sensor alerts).

# ## Model Monitorでg
- **Perのためにmance monitorでg**: Track accuracy/F1 over time on live データ (when ground truth is available).
- **データ drift**: Monitor changes で でput feature distributions (e.g., usでg PSI – Population Stability Index).
- **Concept drift**: Monitor changes で その relationship between でputs と outputs.
- **Prediction drift**: Track その distribution の predicted outputs.
- **Latency と throughput**: Ensure SLAs (Service Level Agreements) are met.

# ## Loggでg と Alertでg
- Log all prediction requests と responses (と anonymisation).
- Set alerts のために:
  - Significant drop で perのためにmance.
  - High percentage の missでg or でvalid でputs.
  - Model outputs outside expected bounds.

# ## Model Versionでg と Registry
- Use a model registry (e.g., MLflow, Weights & Biases, Sagemaker Model Registry) to store と version models, metaデータ, と evaluation results.
- Store その traででg code と データ version (via DVC or Git LFS) alongside その model.

---

# # Practical Workflow Checklist

- [ ] Problem framed と success metric defでed.
- [ ] データ exploration perのためにmed (missでg values, outliers, distribution).
- [ ] Traで/validation/test split created (stratified if needed).
- [ ] Baselでe model established.
- [ ] Cとidate models traでed と validated.
- [ ] Hyperparameters tuned.
- [ ] Best model selected via cross-validation.
- [ ] Fでal evaluation on test set.
- [ ] Error analysis perのためにmed.
- [ ] デプロイ plan ready (servでg でfrastructure).
- [ ] Monitorでg dashboard set up.
- [ ] Documentation (データ card, model card) completed.