<!--
---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, evaluation, workflow, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Machine Learning Evaluation at Workflow
Isang praktikal na gabay sa lifecycle ng ML — mula sa pag-frame ng problema hanggang sa pagsubaybay sa produksyon — na may pagtuon sa mga sukatan, pagpapatunay, at pag-debug.
---

## Ang ML Workflow (CRISP-ML)
1. **Pag-unawa sa Negosyo**: Tukuyin ang layunin at pamantayan ng tagumpay.
2. **Pag-unawa sa Data**: I-explore ang available na data, tukuyin ang mga isyu sa kalidad.
3. **Paghahanda ng Data**: Linisin, ibahin ang anyo, at hatiin ang data.
4. **Pagmomodelo**: Mga modelo ng tren, i-tune ang mga hyperparameter.
5. **Pagsusuri**: Tayahin ang pagganap laban sa mga sukatan.
6. **Deployment**: Ihatid ang modelo sa produksyon.
7. **Pagsubaybay**: Subaybayan ang drift, performance, at mga anomalya.
Ito ay isang umuulit na loop — muli mong bisitahin ang mga naunang hakbang batay sa mga resulta ng pagsusuri.
---

## Paghahati ng Data
### Train / Validation / Test Split
- **Training set** (~70%): Ginagamit upang magkasya sa mga parameter ng modelo.
- **Validation set** (~15%): Ginagamit upang ibagay ang mga hyperparameter at pumili ng mga variant ng modelo.
- **Test set** (~15%): Isang beses lang ginamit sa pinakadulo para tantyahin ang performance ng generalization.
**Mahalaga:** Ang test set ay dapat na panatilihing ganap na hindi nagalaw hanggang sa huling pagsusuri upang maiwasan ang pagtagas ng data.
### Cross-Validation (k-fold)
Para sa maliliit na dataset, gumamit ng k-fold cross-validation: hatiin ang data sa k fold, sanayin sa k-1, validate sa natitira, at ulitin ang k beses. Katamtaman ang pagganap. k=5 o k=10 ay karaniwan.
### Stratified Splitting
Para sa pag-uuri na may mga hindi balanseng klase, gumamit ng mga stratified split upang mapanatili ang mga proporsyon ng klase sa bawat subset.
### Time-Based Splitting
Para sa data ng time-series, hatiin ayon sa pagkakasunod-sunod (magsanay sa nakaraan, subukan sa hinaharap) sa halip na random.
---

## Mga Sukatan ng Pagsusuri
### Mga Sukatan ng Pag-uuri
| Sukatan | Ano ang sinusukat nito | Pinakamahusay na ginamit para sa |
|--------|------------------|----------------|
| **Katumpakan** | (TP + TN) / (TP + TN + FP + FN) | Mga balanseng dataset |
| **Katumpakan** | TP / (TP + FP) | Kapag mahal ang mga maling positibo (hal., pagtukoy ng spam) |
| **Recall** | TP / (TP + FN) | Kapag mahal ang mga maling negatibo (hal., pagsusuri sa kanser) |
| **F1-score** | Harmonic na ibig sabihin ng precision at recall | Mga hindi balanseng dataset, sukatan ng solong numero |
| **AUC-ROC** | Lugar sa ilalim ng ROC curve; tradeoff sa pagitan ng TPR at FPR | Pangkalahatang pagganap ng classifier na hindi nakasalalay sa threshold |
| **AUC-PR** | Lugar sa ilalim ng Precision-Recall curve | Highly imbalanced datasets |
**Mga Kahulugan:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = Maling Negatibo (Type II error)
### Mga Sukatan ng Pagbabalik
| Sukatan | Ano ang sinusukat nito | Pagkasensitibo sa mga outlier |
|---------|------|-------------------------|
| **MSE** (Mean Squared Error) | Average na squared difference | Mataas |
| **RMSE** (Root Mean Squared Error) | Square root ng MSE (parehong mga unit bilang target) | Mataas |
| **MAE** (Mean Absolute Error) | Average na ganap na pagkakaiba | Mababa |
| **R²** (Coefficient of Determination) | Ipinaliwanag ang proporsyon ng pagkakaiba | Wala nang direkta, ngunit hindi direktang sensitibo sa mga outlier |
### Mga Sukatan sa Pagraranggo at Pagkuha
- **Precision@k**: Fraction ng mga nauugnay na item sa mga top-k na rekomendasyon.
- **Recall@k**: Fraction ng lahat ng nauugnay na item na lumalabas sa top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Mga account para sa kaugnayan ng posisyon.
- **Rate ng Hit**: Kung may lalabas na nauugnay na item sa top-k.
### Mga Sukatan ng Generative / LLM
- **Perplexity**: Gaano ka "nagulat" ang modelo sa isang naka-hold-out na text (mas maganda ang mas mababa).
- **BLEU**: nagsasapawan ang n-gram sa mga pagsasalin ng sanggunian (nakatuon sa katumpakan).
- **ROUGE**: Recall-oriented na overlap para sa pagbubuod.
- **BERTScore**: Semantic similarity gamit ang contextual embeddings (mas matatag kaysa sa BLEU).
- **METEOR**: Naka-align sa mga kasingkahulugan at stem ng WordNet.
---

## Pagsusuri Pitfalls
### Data Leakage
Nangyayari kapag ang impormasyon mula sa set ng pagsubok ay hindi sinasadyang nakakaimpluwensya sa pagsasanay.
- **Pigilan:** Huwag kailanman gumamit ng data ng pagsubok para sa feature engineering, normalisasyon, o hyperparameter tuning.
- **Detect:** Kung ang iyong modelo ay nakakuha ng kahina-hinalang mataas, maghinala ng pagtagas.
### Overfitting
Mahusay na gumaganap ang modelo sa data ng pagsasanay ngunit hindi maganda sa pagpapatunay/pagsusulit.
- **Bawasan:** Gumamit ng regularisasyon, maagang paghinto, pasimplehin ang arkitektura, o mangolekta ng higit pang data.
### Underfitting
Mahina ang pagganap ng modelo sa parehong pagsasanay at pagpapatunay.
- **Bawasan:** Gumamit ng mas kumplikadong modelo, magdagdag ng mga feature, o bawasan ang regularisasyon.
### Hindi balanseng Data
- **Bawasan:** Gumamit ng mga timbang ng klase, oversample (SMOTE), undersample, o gumamit ng naaangkop na sukatan (F1, AUC-PR) sa halip na katumpakan.
### Temporal Drift (Concept Drift)
Ang ugnayan sa pagitan ng mga feature at target ay nagbabago sa paglipas ng panahon.
- **Bawasan:** Pana-panahong sanayin, subaybayan ang pagganap, gumamit ng mga algorithm ng drift detection.
---

## Hyperparameter Tuning
- **Paghahanap sa Grid**: Ganap na subukan ang lahat ng kumbinasyon ng isang paunang natukoy na hanay ng mga hyperparameter. Simple pero computationally mahal.
- **Random na Paghahanap**: Sample ng mga random na kumbinasyon mula sa mga distribusyon. Mas mahusay kaysa sa paghahanap sa grid para sa mga high-dimensional na espasyo.
- **Bayesian Optimation**: Bumubuo ng probabilistic na modelo ng layunin na function at matalinong pumili ng mga hyperparameter. Mga Aklatan: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Gumamit ng mga tool tulad ng Optuna, Ray Tune, o Weights & Biases Sweeps para sa distributed tuning.
**Iminungkahing hanay ng paghahanap para sa mga karaniwang hyperparameter:**
| Parameter | Iminungkahing hanay (log-scale) |
|-----------|------------------------------|
| Rate ng pagkatuto | 1e-5 hanggang 1e-1 |
| Laki ng batch | 16, 32, 64, 128, 256 |
| Bilang ng mga layer (NN) | 2 hanggang 6 |
| Bilang ng mga neuron (NN) | 32 hanggang 1024 |
| Regularisasyon (L2) | 1e-6 hanggang 1e-2 |
| Lalim ng puno (XGBoost) | 3 hanggang 12 |
---

## Pagpili at Pagpapatunay ng Modelo
1. **Baseline model**: Magsimula sa isang simpleng heuristic o simpleng modelo (hal., logistic regression, mean predictor) upang magtatag ng lower bound.
2. **Mga modelo ng kandidato**: Sanayin ang maraming pamilya ng modelo (hal., Random Forest, XGBoost, Neural Network).
3. **Cross-validate** ang bawat kandidato sa validation set.
4. **Ihambing ang mga sukatan** (na may mga pagitan ng kumpiyansa) at piliin ang pinakamahusay na kandidato.
5. **Panghuling pagsusuri** sa itinakdang set ng pagsusulit.
6. **Error analysis**: Tingnan ang mga halimbawang nagkakamali ang modelo. Tukuyin ang mga pattern (hal., mga bihirang klase, hindi malinaw na input) at i-feed ang mga insight pabalik sa paghahanda ng data o feature engineering.
---

## Deployment at Pagsubaybay
### Mga Pattern ng Paghahatid
- **Batch inference**: Iproseso ang malalaking volume ng data offline (hal., mga rekomendasyon sa gabi).
- **Online na hinuha**: Mga real-time na hula sa pamamagitan ng API (hal., credit scoring, fraud detection).
- **Streaming inference**: Event-driven, real-time na may mababang latency (hal., IoT sensor alert).
### Pagsubaybay ng Modelo
- **Pagsubaybay sa pagganap**: Subaybayan ang katumpakan/F1 sa paglipas ng panahon sa live na data (kapag available ang ground truth).
- **Data drift**: Subaybayan ang mga pagbabago sa input feature distribution (hal., gamit ang PSI – Population Stability Index).
- **Concept drift**: Subaybayan ang mga pagbabago sa relasyon sa pagitan ng mga input at output.
- **Prediction drift**: Subaybayan ang pamamahagi ng mga hinulaang output.
- **Latency at throughput**: Tiyaking natutugunan ang mga SLA (Service Level Agreements).
### Pag-log at Pag-alerto
- I-log ang lahat ng mga kahilingan at tugon sa hula (na may hindi nagpapakilala).
- Magtakda ng mga alerto para sa:
  - Makabuluhang pagbaba sa pagganap.
  - Mataas na porsyento ng nawawala o di-wastong mga input.
  - Mga output ng modelo sa labas ng inaasahang mga hangganan.
### Pag-bersyon ng Modelo at Rehistro
- Gumamit ng registry ng modelo (hal., MLflow, Weights & Biases, Sagemaker Model Registry) para mag-imbak at mga bersyon ng mga modelo, metadata, at mga resulta ng pagsusuri.
- I-imbak ang code ng pagsasanay at bersyon ng data (sa pamamagitan ng DVC o Git LFS) sa tabi ng modelo.
---

## Checklist ng Praktikal na Daloy ng Trabaho
- [ ] Naka-frame ang problema at tinukoy ang sukatan ng tagumpay.
- [ ] Ginawa ang paggalugad ng data (mga nawawalang value, outlier, distribusyon).
- [ ] Train/validation/test split ginawa (stratified kung kailangan).
- [ ] Itinatag ang baseline model.
- [ ] Ang mga modelo ng kandidato ay sinanay at napatunayan.
- [ ] Ang mga hyperparameter ay nakatutok.
- [ ] Pinakamahusay na modelo na pinili sa pamamagitan ng cross-validation.
- [ ] Panghuling pagsusuri sa set ng pagsubok.
- [ ] Ginawa ang pagsusuri ng error.
- [ ] Handa na ang plano sa deployment (nagsisilbing imprastraktura).
- [ ] Pag-set up ng dashboard ng pagsubaybay.
- [ ] Nakumpleto ang dokumentasyon (data card, model card).