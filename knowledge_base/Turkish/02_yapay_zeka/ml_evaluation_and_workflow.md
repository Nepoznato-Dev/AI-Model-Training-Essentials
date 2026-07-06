# Makine Öğrenmesi Değerlendirmesi ve İş Akışı

ML yaşam döngüsüne yönelik pratik bir rehber — problem çerçevelemeden üretim izlemeye kadar — metriklere, doğrulamaya ve hata ayıklamaya odaklanır.

---

## ML İş Akışı (CRISP-ML)

1. **İş Anlayışı**: Hedefi ve başarı ölçütlerini tanımlayın.
2. **Veri Anlayışı**: Mevcut verileri inceleyin, kalite sorunlarını belirleyin.
3. **Veri Hazırlama**: Veriyi temizleyin, dönüştürün ve bölün.
4. **Modelleme**: Modelleri eğitin, hiperparametreleri ayarlayın.
5. **Değerlendirme**: Performansı metriklere göre ölçün.
6. **Dağıtım**: Modeli üretim ortamında sunun.
7. **İzleme**: Drift'i, performansı ve anomalileri takip edin.

Bu yinelemeli bir döngüdür — değerlendirme sonuçlarına göre önceki adımlara geri dönersiniz.

---

## Veri Bölme

### Eğitim / Doğrulama / Test Bölmesi
- **Eğitim kümesi** (~%70): Model parametrelerini uydurmak için kullanılır.
- **Doğrulama kümesi** (~%15): Hiperparametreleri ayarlamak ve model varyantlarını seçmek için kullanılır.
- **Test kümesi** (~%15): Genelleme performansını tahmin etmek için yalnızca en sonda bir kez kullanılır.

**Önemli:** Veri sızıntısını önlemek için test kümesi nihai değerlendirmeye kadar tamamen dokunulmadan tutulmalıdır.

### Çapraz Doğrulama (k-fold)
Küçük veri kümelerinde k-fold çapraz doğrulama kullanın: veriyi k katmana ayırın, k-1 katman üzerinde eğitin, kalan katmanda doğrulayın ve bunu k kez tekrarlayın. Performansın ortalamasını alın. k=5 veya k=10 yaygındır.

### Katmanlı Bölme
Dengesiz sınıflara sahip sınıflandırma problemlerinde, her alt kümede sınıf oranlarını korumak için katmanlı bölmeler kullanın.

### Zamana Dayalı Bölme
Zaman serisi verilerinde rastgele bölmek yerine kronolojik olarak bölün (geçmiş üzerinde eğit, gelecek üzerinde test et).

---

## Değerlendirme Metrikleri

### Sınıflandırma Metrikleri

| Metrik | Ne ölçer | En uygun kullanım |
|--------|----------|-------------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Dengeli veri kümeleri |
| **Precision** | TP / (TP + FP) | Yanlış pozitiflerin maliyetli olduğu durumlar (ör. spam tespiti) |
| **Recall** | TP / (TP + FN) | Yanlış negatiflerin maliyetli olduğu durumlar (ör. kanser taraması) |
| **F1-score** | Precision ve recall'un harmonik ortalaması | Dengesiz veri kümeleri, tek sayılı metrik |
| **AUC-ROC** | ROC eğrisi altındaki alan; TPR ve FPR arasındaki ödünleşim | Eşikten bağımsız genel sınıflandırıcı performansı |
| **AUC-PR** | Precision-Recall eğrisi altındaki alan | Çok dengesiz veri kümeleri |

**Tanımlar:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (Tip I hata)
- FN = False Negative (Tip II hata)

### Regresyon Metrikleri

| Metrik | Ne ölçer | Aykırı değerlere duyarlılık |
|--------|----------|-----------------------------|
| **MSE** (Mean Squared Error) | Ortalama karesel fark | Yüksek |
| **RMSE** (Root Mean Squared Error) | MSE'nin karekökü (hedefle aynı birimler) | Yüksek |
| **MAE** (Mean Absolute Error) | Ortalama mutlak fark | Düşük |
| **R²** (Belirlilik Katsayısı) | Açıklanan varyans oranı | Doğrudan yok, ancak dolaylı olarak aykırı değerlere duyarlı |

### Sıralama ve Getirme Metrikleri
- **Precision@k**: En iyi k öneri içindeki ilgili öğelerin oranı.
- **Recall@k**: Tüm ilgili öğelerden en iyi k içinde görünenlerin oranı.
- **NDCG** (Normalised Discounted Cumulative Gain): Konum alakasını hesaba katar.
- **Hit Rate**: İlgili bir öğenin en iyi k içinde görünüp görünmediği.

### Üretken / LLM Metrikleri
- **Perplexity**: Modelin ayrılmış bir metin karşısında ne kadar "şaşırdığı" (düşük olması daha iyidir).
- **BLEU**: Referans çevirilerle n-gram örtüşmesi (precision odaklı).
- **ROUGE**: Özetleme için recall odaklı örtüşme.
- **BERTScore**: Bağlamsal embedding'lerle anlamsal benzerlik (BLEU'dan daha sağlam).
- **METEOR**: WordNet eş anlamlıları ve köklerle hizalama yapar.

---

## Değerlendirme Tuzakları

### Veri Sızıntısı
Test kümesinden gelen bilgi istemeden eğitimi etkilediğinde ortaya çıkar.
- **Önleme:** Test verisini özellik mühendisliği, normalizasyon veya hiperparametre ayarı için asla kullanmayın.
- **Tespit:** Modeliniz şüpheli derecede yüksek skor alıyorsa sızıntıdan kuşkulanın.

### Aşırı Uyum
Model eğitim verisinde iyi performans gösterir, ancak doğrulama/test verisinde kötü performans gösterir.
- **Azaltma:** Düzenlileştirme kullanın, erken durdurma uygulayın, mimariyi sadeleştirin veya daha fazla veri toplayın.

### Yetersiz Uyum
Model hem eğitim hem doğrulama verisinde kötü performans gösterir.
- **Azaltma:** Daha karmaşık bir model kullanın, özellik ekleyin veya düzenlileştirmeyi azaltın.

### Dengesiz Veri
- **Azaltma:** Accuracy yerine sınıf ağırlıkları, oversampling (SMOTE), undersampling veya uygun metrikler (F1, AUC-PR) kullanın.

### Zamansal Drift (Concept Drift)
Özellikler ile hedef arasındaki ilişki zaman içinde değişir.
- **Azaltma:** Periyodik olarak yeniden eğitin, performansı izleyin, drift tespit algoritmaları kullanın.

---

## Hiperparametre Ayarı

- **Grid Search**: Önceden tanımlanmış bir hiperparametre kümesindeki tüm kombinasyonları kapsamlı biçimde dener. Basittir ancak hesaplama açısından pahalıdır.
- **Random Search**: Dağılımlardan rastgele kombinasyonlar örnekler. Yüksek boyutlu uzaylarda grid search'ten daha verimlidir.
- **Bayesian Optimisation**: Amaç fonksiyonunun olasılıksal bir modelini kurar ve hiperparametreleri akıllıca seçer. Kütüphaneler: Optuna, Hyperopt, scikit-optimise.
- **Otomatik Ayar**: Dağıtık ayarlama için Optuna, Ray Tune veya Weights & Biases Sweeps gibi araçları kullanın.

**Yaygın hiperparametreler için önerilen arama aralıkları:**

| Parametre | Önerilen aralık (log ölçeği) |
|-----------|------------------------------|
| Learning rate | 1e-5 ile 1e-1 arası |
| Batch size | 16, 32, 64, 128, 256 |
| Katman sayısı (NN) | 2 ile 6 arası |
| Nöron sayısı (NN) | 32 ile 1024 arası |
| Düzenlileştirme (L2) | 1e-6 ile 1e-2 arası |
| Ağaç derinliği (XGBoost) | 3 ile 12 arası |

---

## Model Seçimi ve Doğrulama

1. **Baseline model**: Alt sınırı belirlemek için basit bir sezgisel yöntem veya basit bir modelle (ör. lojistik regresyon, ortalama tahminleyici) başlayın.
2. **Aday modeller**: Birden çok model ailesini (ör. Random Forest, XGBoost, Neural Network) eğitin.
3. Her adayı doğrulama kümesinde **çapraz doğrulayın**.
4. **Metrikleri karşılaştırın** (güven aralıklarıyla) ve en iyi adayı seçin.
5. Ayrılmış test kümesinde **nihai değerlendirme** yapın.
6. **Hata analizi**: Modelin yanlış yaptığı örneklere bakın. Örüntüleri (ör. nadir sınıflar, belirsiz girdiler) belirleyin ve içgörüleri veri hazırlama veya özellik mühendisliğine geri besleyin.

---

## Dağıtım ve İzleme

### Sunum Örüntüleri
- **Batch inference**: Büyük veri hacimlerini çevrimdışı işleme (ör. gecelik öneriler).
- **Online inference**: API üzerinden gerçek zamanlı tahminler (ör. kredi puanlama, dolandırıcılık tespiti).
- **Streaming inference**: Düşük gecikmeli, olay güdümlü gerçek zamanlı tahmin (ör. IoT sensör uyarıları).

### Model İzleme
- **Performans izleme**: Canlı veride zaman içinde accuracy/F1 takibi (ground truth mevcut olduğunda).
- **Veri drift'i**: Girdi özellik dağılımlarındaki değişimleri izleyin (ör. PSI – Population Stability Index kullanarak).
- **Concept drift**: Girdiler ve çıktılar arasındaki ilişkideki değişimleri izleyin.
- **Tahmin drift'i**: Tahmin edilen çıktıların dağılımını takip edin.
- **Gecikme ve verim**: SLA'ların (Service Level Agreements) karşılandığından emin olun.

### Günlükleme ve Uyarı
- Tüm tahmin isteklerini ve yanıtlarını (anonimleştirerek) günlükleyin.
- Şunlar için uyarılar ayarlayın:
  - Performansta belirgin düşüş.
  - Eksik veya geçersiz girdilerin yüksek yüzdesi.
  - Beklenen sınırların dışındaki model çıktıları.

### Model Sürümleme ve Registry
- Modelleri, metadataları ve değerlendirme sonuçlarını saklamak ve sürümlemek için bir model registry (ör. MLflow, Weights & Biases, Sagemaker Model Registry) kullanın.
- Eğitim kodunu ve veri sürümünü (DVC veya Git LFS aracılığıyla) modelin yanında saklayın.

---

## Pratik İş Akışı Kontrol Listesi

- [ ] Problem çerçevelendi ve başarı metriği tanımlandı.
- [ ] Veri keşfi yapıldı (eksik değerler, aykırı değerler, dağılım).
- [ ] Eğitim/doğrulama/test bölmesi oluşturuldu (gerekirse katmanlı).
- [ ] Baseline model oluşturuldu.
- [ ] Aday modeller eğitildi ve doğrulandı.
- [ ] Hiperparametreler ayarlandı.
- [ ] En iyi model çapraz doğrulama yoluyla seçildi.
- [ ] Test kümesinde nihai değerlendirme yapıldı.
- [ ] Hata analizi yapıldı.
- [ ] Dağıtım planı hazır (sunum altyapısı).
- [ ] İzleme panosu kuruldu.
- [ ] Dokümantasyon (data card, model card) tamamlandı.
