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
# Makine Öğrenimi Değerlendirmesi ve İş Akışı
Ölçümler, doğrulama ve hata ayıklamaya odaklanan, sorun çerçevelemeden üretim izlemeye kadar makine öğrenimi yaşam döngüsüne yönelik pratik bir kılavuz.
---

## ML İş Akışı (CRISP-ML)
1. **İş Anlayışı**: Hedefi ve başarı kriterlerini tanımlayın.
2. **Veri Anlama**: Mevcut verileri keşfedin, kalite sorunlarını belirleyin.
3. **Veri Hazırlama**: Verileri temizleyin, dönüştürün ve bölün.
4. **Modelleme**: Modelleri eğitin, hiperparametreleri ayarlayın.
5. **Değerlendirme**: Performansı metriklere göre değerlendirin.
6. **Dağıtım**: Modeli üretimde yayınlayın.
7. **İzleme**: Sapmayı, performansı ve anormallikleri izleyin.
Bu yinelenen bir döngüdür; değerlendirme sonuçlarına göre önceki adımları tekrar gözden geçireceksiniz.
---

## Veri Bölme
### Eğitim / Doğrulama / Test Bölünmesi
- **Eğitim seti** (~%70): Model parametrelerini sığdırmak için kullanılır.
- **Doğrulama seti** (~%15): Hiperparametreleri ayarlamak ve model çeşitlerini seçmek için kullanılır.
- **Test seti** (~%15): Genelleme performansını tahmin etmek için yalnızca en sonunda bir kez kullanıldı.
**Önemli:** Veri sızıntısını önlemek için test setine son değerlendirmeye kadar tamamen dokunulmamalıdır.
### Çapraz Doğrulama (k-katlama)
Küçük veri kümeleri için k-katlı çapraz doğrulamayı kullanın: verileri k kata bölün, k-1 üzerinde eğitim yapın, geri kalanı doğrulayın ve k kez tekrarlayın. Performansı ortalamalayın. k=5 veya k=10 yaygındır.
### Katmanlı Bölme
Dengesiz sınıflarla sınıflandırma için, her alt kümedeki sınıf oranlarını korumak amacıyla katmanlı bölünmeleri kullanın.
### Zamana Dayalı Bölme
Zaman serisi verileri için rastgele yerine kronolojik olarak bölün (geçmişe göre eğitim, geleceğe göre test).
---

## Değerlendirme Metrikleri
### Sınıflandırma Metrikleri
| Metrik | Neyi ölçer | En iyi kullanım alanı |
|----------|----------|---------------|
| **Doğruluk** | (TP + TN) / (TP + TN + FP + FN) | Dengeli veri kümeleri |
| **Hassaslık** | TP / (TP + FP) | Yanlış pozitifler maliyetli olduğunda (örn. spam tespiti) |
| **Geri çağırma** | TP / (TP + FN) | Yanlış negatifler maliyetli olduğunda (örn. kanser taraması) |
| **F1 puanı** | Hassasiyet ve geri çağırmanın harmonik ortalaması | Dengesiz veri kümeleri, tek rakamlı metrik |
| **AUC-ROC** | ROC eğrisinin altındaki alan; TPR ve FPR arasındaki ödünleşme | Eşikten bağımsız genel sınıflandırıcı performansı |
| **AUC-PR** | Hassasiyet-Geri Çağırma eğrisi altındaki alan | Son derece dengesiz veri kümeleri |
**Tanımlar:**
- TP = Gerçek Pozitif
- TN = Gerçek Negatif
- FP = Yanlış Pozitif (Tip I hatası)
- FN = Yanlış Negatif (Tip II hatası)
### Regresyon Metrikleri
| Metrik | Neyi ölçer | Aykırı değerlere karşı hassasiyet |
|----------|---------------------|---------------|
| **MSE** (Ortalama Karesel Hata) | Ortalama kare fark | Yüksek |
| **RMSE** (Kök Ortalama Kare Hatası) | MSE'nin karekökü (hedefle aynı birimler) | Yüksek |
| **MAE** (Ortalama Mutlak Hata) | Ortalama mutlak fark | Düşük |
| **R²** (Belirleme Katsayısı) | Açıklanan varyans oranı | Doğrudan yok, ancak aykırı değerlere dolaylı olarak duyarlı |
### Sıralama ve Geri Alma Metrikleri
- **Precision@k**: İlgili öğelerin en üst düzey öneriler arasındaki oranı.
- **Recall@k**: En üst k'de görünen tüm ilgili öğelerin kesri.
- **NDCG** (Normalleştirilmiş İndirimli Kümülatif Kazanç): Pozisyon alaka düzeyini hesaplar.
- **İsabet Oranı**: İlgili bir öğenin ilk k'de görünüp görünmediği.
### Üretken / Yüksek Lisans Metrikleri
- **Şaşırma**: Modelin uzatılmış bir metin nedeniyle ne kadar "şaşırttığı" (daha düşük olan daha iyidir).
- **BLEU**: referans çevirileriyle n-gram örtüşmesi (hassasiyet odaklı).
- **ROUGE**: Özetleme için hatırlama odaklı örtüşme.
- **BERTScore**: Bağlamsal yerleştirmeler kullanılarak anlamsal benzerlik (BLEU'dan daha sağlam).
- **METEOR**: WordNet eşanlamlılarına ve köklerine uyum sağlar.
---

## Değerlendirme Tuzakları
### Veri Sızıntısı
Test kümesindeki bilgilerin yanlışlıkla eğitimi etkilemesi durumunda oluşur.
- **Önleyin:** Test verilerini hiçbir zaman özellik mühendisliği, normalleştirme veya hiperparametre ayarlama için kullanmayın.
- **Algılama:** Modelinizin puanı şüpheli derecede yüksekse, sızıntıdan şüphelenin.
### Aşırı uyum
Model, eğitim verilerinde iyi performans gösterir ancak doğrulama/testte zayıf performans gösterir.
- **Azaltma:** Düzenlileştirmeyi, erken durdurmayı kullanın, mimariyi basitleştirin veya daha fazla veri toplayın.
### Yetersiz uyum
Model hem eğitim hem de doğrulama konusunda zayıf performans gösteriyor.
- **Azaltma:** Daha karmaşık bir model kullanın, özellikler ekleyin veya düzenlemeyi azaltın.
### Dengesiz Veri
- **Azaltma:** Doğruluk yerine sınıf ağırlıklarını, aşırı örneklemeyi (SMOTE), yetersiz örneklemeyi veya uygun ölçümleri (F1, AUC-PR) kullanın.
### Zamansal Kayma (Kavram Kayması)
Özellikler ve hedef arasındaki ilişki zamanla değişir.
- **Azaltın:** Periyodik olarak yeniden eğitim alın, performansı izleyin, sapma tespit algoritmalarını kullanın.
---

## Hiperparametre Ayarı
- **Grid Search**: Önceden tanımlanmış bir hiperparametre kümesinin tüm kombinasyonlarını kapsamlı bir şekilde deneyin. Basit ama hesaplama açısından pahalı.
- **Rastgele Arama**: Dağılımlardan rastgele kombinasyonları örnekleyin. Yüksek boyutlu uzaylar için ızgara aramasından daha verimlidir.
- **Bayes Optimizasyonu**: Hedef fonksiyonun olasılıksal bir modelini oluşturur ve hiperparametreleri akıllıca seçer. Kütüphaneler: Optuna, Hyperopt, scikit-optimise.
- **Otomatik Ayarlama**: Dağıtılmış ayarlama için Optuna, Ray Tune veya Weights & Biases Sweeps gibi araçları kullanın.
**Yaygın hiperparametreler için önerilen arama aralıkları:**
| Parametre | Önerilen aralık (log ölçeğinde) |
|-----------|-----------------|
| Öğrenme oranı | 1e-5'ten 1e-1'e |
| Parti boyutu | 16, 32, 64, 128, 256 |
| Katman sayısı (NN) | 2 - 6 |
| Nöron sayısı (NN) | 32 - 1024 |
| Düzenleme (L2) | 1e-6'dan 1e-2'ye |
| Ağaç derinliği (XGBoost) | 3 - 12 |
---

## Model Seçimi ve Doğrulaması
1. **Temel model**: Bir alt sınır oluşturmak için basit buluşsal veya basit bir modelle (ör. lojistik regresyon, ortalama tahminci) başlayın.
2. **Aday modeller**: Birden fazla model ailesini eğitin (ör. Rastgele Orman, XGBoost, Sinir Ağı).
3. Doğrulama kümesindeki her adayın **çapraz doğrulamasını yapın**.
4. **Metrikleri karşılaştırın** (güven aralıklarıyla) ve en iyi adayı seçin.
5. Uzatılan test setinin **son değerlendirmesi**.
6. **Hata analizi**: Modelin yanlış yaptığı örneklere bakın. Modelleri tanımlayın (ör. nadir sınıflar, belirsiz girdiler) ve içgörüleri veri hazırlama veya özellik mühendisliğine geri aktarın.
---

## Dağıtım ve İzleme
### Servis Kalıpları
- **Toplu çıkarım**: Büyük hacimli verileri çevrimdışı olarak işleyin (ör. gecelik öneriler).
- **Çevrimiçi çıkarım**: API aracılığıyla gerçek zamanlı tahminler (ör. kredi puanlama, sahtekarlık tespiti).
- **Akış çıkarımı**: Olay odaklı, düşük gecikmeli gerçek zamanlı (ör. IoT sensör uyarıları).
### Model İzleme
- **Performans izleme**: Canlı verilerde zaman içinde doğruluğu/F1'i izleyin (temel gerçek mevcut olduğunda).
- **Veri kayması**: Giriş özelliği dağılımlarındaki değişiklikleri izleyin (ör. PSI – Nüfus İstikrar Endeksi kullanarak).
- **Kavram sapması**: Girdiler ve çıktılar arasındaki ilişkideki değişiklikleri izleyin.
- **Tahmin sapması**: Tahmin edilen çıktıların dağılımını izleyin.
- **Gecikme ve aktarım hızı**: SLA'ların (Hizmet Düzeyi Anlaşmaları) karşılandığından emin olun.
### Günlüğe Kaydetme ve Uyarı
- Tüm tahmin isteklerini ve yanıtlarını (anonimleştirmeyle) günlüğe kaydedin.
- Şunlar için uyarı ayarlayın:
  - Performansta önemli düşüş.
  - Eksik veya geçersiz giriş yüzdesi yüksek.
  - Model çıktıları beklenen sınırların dışında.
### Model Sürümü Oluşturma ve Kayıt Defteri
- Modelleri, meta verileri ve değerlendirme sonuçlarını depolamak ve sürümlendirmek için bir model kaydı (örneğin, MLflow, Weights & Biases, Sagemaker Model Registry) kullanın.
- Eğitim kodunu ve veri sürümünü (DVC veya Git LFS aracılığıyla) modelin yanında saklayın.
---

## Pratik İş Akışı Kontrol Listesi
- [ ] Sorun çerçevelendi ve başarı ölçüsü tanımlandı.
- [ ] Veri araştırması gerçekleştirildi (eksik değerler, aykırı değerler, dağılım).
- [ ] Eğitim/doğrulama/test bölümü oluşturuldu (gerekirse katmanlandırılır).
- [ ] Temel model oluşturuldu.
- [ ] Aday modeller eğitildi ve doğrulandı.
- [ ] Hiperparametreler ayarlandı.
- [ ] Çapraz doğrulama yoluyla seçilen en iyi model.
- [ ] Test setinin son değerlendirmesi.
- [ ] Hata analizi gerçekleştirildi.
- [ ] Dağıtım planı hazır (altyapıya hizmet ediyor).
- [ ] İzleme paneli kurulumu.
- [ ] Dokümantasyon (veri kartı, model kartı) tamamlandı.