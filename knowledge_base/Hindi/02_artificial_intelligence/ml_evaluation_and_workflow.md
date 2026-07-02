# मशीन लर्निंग मूल्यांकन और वर्कफ़्लो

ML lifecycle के लिए एक व्यावहारिक मार्गदर्शिका — समस्या-परिभाषा से लेकर production monitoring तक — जिसमें metrics, validation और debugging पर विशेष ध्यान दिया गया है।

---

## ML वर्कफ़्लो (CRISP-ML)

1. **Business Understanding**: उद्देश्य और success criteria परिभाषित करें।
2. **Data Understanding**: उपलब्ध डेटा का अन्वेषण करें, quality issues पहचानें।
3. **Data Preparation**: डेटा को साफ़ करें, transform करें और split करें।
4. **Modelling**: models को train करें, hyperparameters tune करें।
5. **Evaluation**: metrics के विरुद्ध performance का आकलन करें।
6. **Deployment**: model को production में serve करें।
7. **Monitoring**: drift, performance और anomalies को track करें।

यह एक iterative loop है — मूल्यांकन परिणामों के आधार पर आप पहले के चरणों पर वापस लौटेंगे।

---

## डेटा विभाजन

### Train / Validation / Test Split
- **Training set** (~70%): model parameters को fit करने के लिए उपयोग किया जाता है।
- **Validation set** (~15%): hyperparameters tune करने और model variants चुनने के लिए उपयोग किया जाता है।
- **Test set** (~15%): केवल बिल्कुल अंत में generalisation performance का अनुमान लगाने के लिए एक बार उपयोग किया जाता है।

**महत्वपूर्ण:** data leakage से बचने के लिए final evaluation तक test set को पूरी तरह अछूता रखा जाना चाहिए।

### Cross-Validation (k-fold)
छोटे datasets के लिए k-fold cross-validation का उपयोग करें: डेटा को k folds में बाँटें, k-1 पर train करें, शेष पर validate करें, और इसे k बार दोहराएँ। फिर performance का औसत लें। k=5 या k=10 सामान्य हैं।

### Stratified Splitting
Imbalanced classes वाली classification के लिए stratified splits का उपयोग करें ताकि प्रत्येक subset में class proportions बनी रहें।

### Time-Based Splitting
Time-series data के लिए यादृच्छिक रूप से बाँटने के बजाय कालानुक्रमिक रूप से split करें (अतीत पर train, भविष्य पर test)।

---

## मूल्यांकन मेट्रिक्स

### Classification Metrics

| Metric | यह क्या मापता है | कब सबसे उपयोगी |
|--------|------------------|----------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Balanced datasets |
| **Precision** | TP / (TP + FP) | जब false positives महंगे हों (उदा., spam detection) |
| **Recall** | TP / (TP + FN) | जब false negatives महंगे हों (उदा., cancer screening) |
| **F1-score** | precision और recall का harmonic mean | Imbalanced datasets, single-number metric |
| **AUC-ROC** | ROC curve के नीचे का area; TPR और FPR के बीच tradeoff | threshold से स्वतंत्र सामान्य classifier performance |
| **AUC-PR** | Precision-Recall curve के नीचे का area | अत्यधिक imbalanced datasets |

**परिभाषाएँ:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

### Regression Metrics

| Metric | यह क्या मापता है | Outliers के प्रति संवेदनशीलता |
|--------|------------------|------------------------------|
| **MSE** (Mean Squared Error) | squared difference का औसत | High |
| **RMSE** (Root Mean Squared Error) | MSE का square root (target की ही units में) | High |
| **MAE** (Mean Absolute Error) | absolute difference का औसत | Low |
| **R²** (Coefficient of Determination) | समझाई गई variance का अनुपात | सीधे तौर पर नहीं, पर अप्रत्यक्ष रूप से outliers के प्रति संवेदनशील |

### Ranking and Retrieval Metrics
- **Precision@k**: top-k recommendations में relevant items का अनुपात।
- **Recall@k**: सभी relevant items में से top-k में आने वाले items का अनुपात।
- **NDCG** (Normalised Discounted Cumulative Gain): position relevance को ध्यान में रखता है।
- **Hit Rate**: क्या top-k में कोई relevant item दिखाई देता है।

### Generative / LLM Metrics
- **Perplexity**: held-out text देखकर model कितना "आश्चर्यचकित" होता है (कम बेहतर है)।
- **BLEU**: reference translations के साथ n-gram overlap (precision-केंद्रित)।
- **ROUGE**: summarisation के लिए recall-oriented overlap।
- **BERTScore**: contextual embeddings का उपयोग करके semantic similarity (BLEU से अधिक robust)।
- **METEOR**: WordNet synonyms और stems के साथ alignment करता है।

---

## मूल्यांकन में सामान्य समस्याएँ

### Data Leakage
यह तब होता है जब test set की जानकारी अनजाने में training को प्रभावित करती है।
- **रोकथाम:** feature engineering, normalisation या hyperparameter tuning के लिए कभी भी test data का उपयोग न करें।
- **पहचान:** यदि model का score असामान्य रूप से बहुत अधिक है, तो leakage का संदेह करें।

### Overfitting
मॉडल training data पर अच्छा प्रदर्शन करता है लेकिन validation/test पर खराब।
- **नियंत्रण:** regularisation, early stopping, सरल architecture, या अधिक data का उपयोग करें।

### Underfitting
मॉडल training और validation दोनों पर खराब प्रदर्शन करता है।
- **नियंत्रण:** अधिक जटिल model का उपयोग करें, features जोड़ें, या regularisation कम करें।

### Imbalanced Data
- **नियंत्रण:** class weights, oversample (SMOTE), undersample का उपयोग करें, या accuracy के बजाय उपयुक्त metrics (F1, AUC-PR) अपनाएँ।

### Temporal Drift (Concept Drift)
समय के साथ features और target के बीच संबंध बदल जाता है।
- **नियंत्रण:** समय-समय पर retrain करें, performance monitor करें, drift detection algorithms का उपयोग करें।

---

## Hyperparameter Tuning

- **Grid Search**: पूर्वनिर्धारित hyperparameters के सभी combinations को exhaustively आज़माता है। सरल है लेकिन computationally expensive है।
- **Random Search**: distributions से random combinations sample करता है। High-dimensional spaces के लिए grid search से अधिक कुशल।
- **Bayesian Optimisation**: objective function का probabilistic model बनाता है और बुद्धिमानी से hyperparameters चुनता है। Libraries: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: distributed tuning के लिए Optuna, Ray Tune, या Weights & Biases Sweeps जैसे tools का उपयोग करें।

**सामान्य hyperparameters के लिए सुझाई गई search ranges:**

| Parameter | सुझाई गई range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Selection and Validation

1. **Baseline model**: एक सरल heuristic या सरल model (उदा., logistic regression, mean predictor) से शुरू करें ताकि lower bound स्थापित हो सके।
2. **Candidate models**: कई model families को train करें (उदा., Random Forest, XGBoost, Neural Network)।
3. **Cross-validate** प्रत्येक candidate को validation set पर करें।
4. **Compare metrics** (confidence intervals के साथ) और सर्वश्रेष्ठ candidate चुनें।
5. **Final evaluation** held-out test set पर करें।
6. **Error analysis**: उन उदाहरणों को देखें जिनमें model गलती करता है। पैटर्न पहचानें (उदा., rare classes, ambiguous inputs) और इन insights को data preparation या feature engineering में वापस उपयोग करें।

---

## Deployment and Monitoring

### Serving Patterns
- **Batch inference**: बड़े डेटा वॉल्यूम को offline प्रोसेस करें (उदा., nightly recommendations)।
- **Online inference**: API के माध्यम से real-time predictions (उदा., credit scoring, fraud detection)।
- **Streaming inference**: event-driven, low latency के साथ real-time (उदा., IoT sensor alerts)।

### Model Monitoring
- **Performance monitoring**: live data पर समय के साथ accuracy/F1 track करें (जब ground truth उपलब्ध हो)।
- **Data drift**: input feature distributions में परिवर्तनों को monitor करें (उदा., PSI – Population Stability Index का उपयोग करके)।
- **Concept drift**: inputs और outputs के बीच संबंधों में परिवर्तन monitor करें।
- **Prediction drift**: predicted outputs के distribution को track करें।
- **Latency and throughput**: सुनिश्चित करें कि SLAs (Service Level Agreements) पूरे हो रहे हैं।

### Logging and Alerting
- सभी prediction requests और responses को log करें (anonymisation के साथ)।
- इन स्थितियों के लिए alerts सेट करें:
  - performance में उल्लेखनीय गिरावट।
  - missing या invalid inputs का उच्च प्रतिशत।
  - अपेक्षित सीमाओं से बाहर model outputs।

### Model Versioning and Registry
- models, metadata और evaluation results को store और version करने के लिए model registry (उदा., MLflow, Weights & Biases, Sagemaker Model Registry) का उपयोग करें।
- model के साथ training code और data version (DVC या Git LFS के माध्यम से) भी store करें।

---

## व्यावहारिक वर्कफ़्लो चेकलिस्ट

- [ ] समस्या परिभाषित है और success metric निर्धारित है।
- [ ] Data exploration किया गया है (missing values, outliers, distribution)।
- [ ] Train/validation/test split बनाया गया है (ज़रूरत होने पर stratified)।
- [ ] Baseline model स्थापित किया गया है।
- [ ] Candidate models को train और validate किया गया है।
- [ ] Hyperparameters tune किए गए हैं।
- [ ] Cross-validation के माध्यम से सर्वश्रेष्ठ model चुना गया है।
- [ ] Test set पर final evaluation किया गया है।
- [ ] Error analysis किया गया है।
- [ ] Deployment plan तैयार है (serving infrastructure)।
- [ ] Monitoring dashboard सेट किया गया है।
- [ ] Documentation (data card, model card) पूरी की गई है।
