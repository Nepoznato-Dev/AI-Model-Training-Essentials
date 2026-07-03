# Makine Öğrenimi Değerlendirme ve İş Akışı

Problem çerçevelemeden production izlemeye kadar uzanan ML yaşam döngüsüne yönelik; metrikler, doğrulama ve hata ayıklamaya odaklanan pratik bir rehber.

---

## ML İş Akışı (CRISP-ML)

1. **İş Anlayışı**: Hedefi ve başarı ölçütlerini tanımlayın.
2. **Veri Anlayışı**: Mevcut veriyi inceleyin, kalite sorunlarını belirleyin.
3. **Veri Hazırlama**: Veriyi temizleyin, dönüştürün ve bölün.
4. **Modelleme**: Modelleri eğitin, hyperparameter'ları ayarlayın.
5. **Değerlendirme**: Performansı metriklere göre ölçün.
6. **Dağıtım**: Modeli production'da servis edin.
7. **İzleme**: Drift, performans ve anomalileri takip edin.

Bu süreç yinelemeli bir döngüdür — değerlendirme sonuçlarına göre önceki adımlara geri dönersiniz.

---

## Veri Bölme

### Train / Validation / Test Ayrımı
- **Training set** (~%70): Model parametrelerini uyarlamak için kullanılır.
- **Validation set** (~%15): Hyperparameter ayarlamak ve model varyantlarını seçmek için kullanılır.
- **Test set** (~%15): Genelleme performansını tahmin etmek için yalnızca en sonda bir kez kullanılır.

**Önemli:** Veri sızıntısını önlemek için test seti, son değerlendirmeye kadar tamamen dokunulmadan tutulmalıdır.

### Cross-Validation (k-fold)
Küçük veri kümelerinde k-fold cross-validation kullanın: veriyi k parçaya bölün, k-1 parça üzerinde eğitip kalan parça üzerinde doğrulayın ve bunu k kez tekrarlayın. Performansın ortalamasını alın. Genellikle k=5 veya k=10 kullanılır.

### Stratified Splitting
Dengesiz sınıflara sahip sınıflandırma problemlerinde, her alt kümede sınıf oranlarını korumak için stratified split kullanın.

### Time-Based Splitting
Time-series verilerinde rastgele bölmek yerine kronolojik bölme yapın (geçmişte eğit, gelecekte test et).

---

## Değerlendirme Metrikleri

### Sınıflandırma Metrikleri

| Metric | Ne ölçer | En uygun kullanım |
|--------|----------|-------------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Dengeli veri kümeleri |
| **Precision** | TP / (TP + FP) | False positive'lerin maliyetli olduğu durumlar (ör. spam tespiti) |
| **Recall** | TP / (TP + FN) | False negative'lerin maliyetli olduğu durumlar (ör. kanser taraması) |
| **F1-score** | Precision ve recall'un harmonik ortalaması | Dengesiz veri kümeleri, tek sayılık metrik |
| **AUC-ROC** | ROC eğrisi altındaki alan; TPR ile FPR arasındaki ödünleşim | Threshold'dan bağımsız genel sınıflandırıcı performansı |
| **AUC-PR** | Precision-Recall eğrisi altındaki alan | Aşırı dengesiz veri kümeleri |

**Tanımlar:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Type I error)
- FN = False Negative (Type II error)

### Regresyon Metrikleri

| Metric | Ne ölçer | Aykırı değerlere duyarlılık |
|--------|----------|-----------------------------|
| **MSE** (Mean Squared Error) | Kare farkların ortalaması | Yüksek |
| **RMSE** (Root Mean Squared Error) | MSE'nin karekökü (hedef ile aynı birimler) | Yüksek |
| **MAE** (Mean Absolute Error) | Mutlak farkların ortalaması | Düşük |
| **R²** (Coefficient of Determination) | Açıklanan varyans oranı | Doğrudan yoktur, ancak dolaylı olarak aykırı değerlere duyarlıdır |

### Sıralama ve Erişim Metrikleri
- **Precision@k**: İlk k öneri içindeki ilgili öğelerin oranı.
- **Recall@k**: Tüm ilgili öğelerden ilk k içinde yer alanların oranı.
- **NDCG** (Normalised Discounted Cumulative Gain): Konumun ilgililik üzerindeki etkisini hesaba katar.
- **Hit Rate**: İlgili bir öğenin ilk k içinde görünüp görünmediği.

### Üretici Model / LLM Metrikleri
- **Perplexity**: Modelin elde tutulmuş bir metne ne kadar "şaşırdığını" gösterir (düşük olması daha iyidir).
- **BLEU**: Referans çevirilerle n-gram örtüşmesi (precision odaklı).
- **ROUGE**: Özetleme için recall odaklı örtüşme.
- **BERTScore**: Bağlamsal embedding'lerle anlamsal benzerlik ölçer (BLEU'dan daha dayanıklıdır).
- **METEOR**: WordNet eş anlamlılarını ve kökleri hizalar.

---

## Değerlendirme Tuzakları

### Veri Sızıntısı
Test setinden gelen bilginin istemeden eğitimi etkilemesiyle oluşur.
- **Önleme:** Feature engineering, normalisation veya hyperparameter tuning için test verisini asla kullanmayın.
- **Tespit:** Modeliniz şüpheli derecede yüksek skor alıyorsa veri sızıntısından şüphelenin.

### Overfitting
Model training verisinde iyi, validation/test verisinde kötü performans gösterir.
- **Azaltma:** Regularisation kullanın, early stopping uygulayın, mimariyi sadeleştirin veya daha fazla veri toplayın.

### Underfitting
Model hem training hem validation verisinde kötü performans gösterir.
- **Azaltma:** Daha karmaşık bir model kullanın, yeni feature'lar ekleyin veya regularisation'ı azaltın.

### Dengesiz Veri
- **Azaltma:** Class weight kullanın, oversample (SMOTE) yapın, undersample uygulayın veya accuracy yerine uygun metrikleri (F1, AUC-PR) tercih edin.

### Zamansal Drift (Concept Drift)
Feature'lar ile hedef arasındaki ilişki zaman içinde değişir.
- **Azaltma:** Düzenli olarak yeniden eğitin, performansı izleyin, drift detection algoritmaları kullanın.

---

## Hyperparameter Ayarlama

- **Grid Search**: Önceden tanımlı hyperparameter kümesindeki tüm kombinasyonları dener. Basittir ancak hesaplama maliyeti yüksektir.
- **Random Search**: Dağılımlardan rastgele kombinasyonlar örnekler. Yüksek boyutlu uzaylarda grid search'ten daha verimlidir.
- **Bayesian Optimisation**: Amaç fonksiyonunun olasılıksal bir modelini kurar ve hyperparameter'ları akıllıca seçer. Kütüphaneler: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Dağıtık ayarlama için Optuna, Ray Tune veya Weights & Biases Sweeps gibi araçları kullanın.

**Yaygın hyperparameter'lar için önerilen arama aralıkları:**

| Parameter | Önerilen aralık (log-scale) |
|-----------|------------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Model Seçimi ve Doğrulama

1. **Baseline model**: Alt sınırı belirlemek için basit bir sezgisel yöntemle ya da basit bir modelle başlayın (ör. logistic regression, mean predictor).
2. **Candidate models**: Birden fazla model ailesini eğitin (ör. Random Forest, XGBoost, Neural Network).
3. Her adayı validation set üzerinde **cross-validate** edin.
4. **Metrikleri karşılaştırın** (güven aralıklarıyla birlikte) ve en iyi adayı seçin.
5. Elde tutulmuş test seti üzerinde **nihai değerlendirme** yapın.
6. **Hata analizi**: Modelin yanlış yaptığı örneklere bakın. Örüntüleri belirleyin (ör. nadir sınıflar, belirsiz girdiler) ve içgörüleri veri hazırlama ya da feature engineering aşamasına geri besleyin.

---

## Dağıtım ve İzleme

### Serving Kalıpları
- **Batch inference**: Büyük hacimli veriyi çevrimdışı işleyin (ör. gecelik öneriler).
- **Online inference**: API üzerinden gerçek zamanlı tahminler yapın (ör. credit scoring, fraud detection).
- **Streaming inference**: Olay güdümlü, düşük gecikmeli gerçek zamanlı tahminler üretin (ör. IoT sensör uyarıları).

### Model İzleme
- **Performance monitoring**: Canlı veride zaman içinde accuracy/F1 değerlerini takip edin (ground truth mevcut olduğunda).
- **Data drift**: Girdi feature dağılımlarındaki değişimleri izleyin (ör. PSI – Population Stability Index kullanarak).
- **Concept drift**: Girdiler ile çıktılar arasındaki ilişkideki değişimleri izleyin.
- **Prediction drift**: Tahmin edilen çıktıların dağılımını takip edin.
- **Latency and throughput**: SLA'lerin (Service Level Agreements) karşılandığından emin olun.

### Logging ve Alerting
- Tüm prediction request ve response'larını kaydedin (anonimleştirme ile birlikte).
- Şunlar için uyarılar tanımlayın:
  - Performansta belirgin düşüş.
  - Eksik veya geçersiz girdilerin yüksek oranı.
  - Beklenen sınırların dışındaki model çıktıları.

### Model Sürümleme ve Registry
- Modelleri, metadata'yı ve değerlendirme sonuçlarını depolamak ve sürümlemek için bir model registry kullanın (ör. MLflow, Weights & Biases, Sagemaker Model Registry).
- Eğitim kodunu ve veri sürümünü (DVC veya Git LFS aracılığıyla) modelle birlikte saklayın.

---

## Pratik İş Akışı Kontrol Listesi

- [ ] Problem çerçevelendi ve başarı metriği tanımlandı.
- [ ] Veri keşfi yapıldı (eksik değerler, aykırı değerler, dağılım).
- [ ] Train/validation/test ayrımı oluşturuldu (gerekirse stratified).
- [ ] Baseline model oluşturuldu.
- [ ] Candidate model'ler eğitildi ve doğrulandı.
- [ ] Hyperparameter'lar ayarlandı.
- [ ] En iyi model cross-validation ile seçildi.
- [ ] Test seti üzerinde nihai değerlendirme yapıldı.
- [ ] Hata analizi gerçekleştirildi.
- [ ] Dağıtım planı hazır (serving altyapısı).
- [ ] İzleme dashboard'u kuruldu.
- [ ] Dokümantasyon (data card, model card) tamamlandı.
