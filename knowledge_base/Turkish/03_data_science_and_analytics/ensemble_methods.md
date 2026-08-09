---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Topluluk Yöntemleri
Topluluk yöntemleri, tek bir modelin tek başına başarabileceğinden daha iyi tahminler üretmek için birden fazla makine öğrenimi modelini birleştirir. Sezgi basittir: Her biri bir dereceye kadar doğru olan ancak farklı hatalar yapan birkaç modeliniz varsa, bunların tahminlerini birleştirmek bireysel hataları iptal edecek ve daha sağlam bir sonuç üretecektir. Topluluklar, çoğu rekabetçi makine öğrenimi çözümünün arkasında yer alır ve üretim sistemlerindeki en güvenilir tekniklerden bazıları olmaya devam etmektedir.
---

## Topluluklar Neden Çalışır?
| Prensip | Açıklama |
|-----------|----------------|
| **Kalabalığın bilgeliği** | Çoklu kusurlu tahminlerin ortalaması, herhangi bir tek tahminden daha iyidir |
| **Önyargı-varyans dengesi** | Topluluklar, diğerinden ödün vermeden varyansı (torbalama) veya önyargıyı (artırma) azaltabilir |
| **Hata çeşitliliği** | Modeller farklı hatalar yaparsa, bunları birleştirmek bireysel hataları iptal eder |
| **Karar sınırlarını yumuşatma** | Birden fazla model, tek bir modele göre daha sağlam bir karar yüzeyi oluşturur |
---

## Torbalama (Önyükleme Toplama)
### Nasıl Çalışır?
| Adım | Açıklama |
|------|-----------------|
| **1. Önyükleme örneklemesi** | Eğitim verilerinden birden fazla rastgele örnek (değiştirilerek) çizin |
| **2. Tren üssü modelleri** | Her önyükleme örneğinde bir model eğitin (genellikle karar ağaçları) |
| **3. Toplam** | Regresyon için: ortalama tahminler. Sınıflandırma için: çoğunluk oyu |
### Temel Özellikler
| karakteristik | Açıklama |
|---------------|---------------|
| **Farklılığı azaltır** | Ortalama alma, bireysel model dalgalanmalarını düzeltir |
| **Paralel eğitim** | Her temel model bağımsızdır; aynı anda eğitilebilir |
| **Çanta dışı değerlendirme** | Her örnek bazı önyükleme örneklerinin dışında bırakılır; bunları doğrulama için kullanın |
| **Dekorelasyon** | Her bölmede rastgele özellik seçimi, ağaçlar arasındaki korelasyonu azaltır |
### Rastgele Orman
| Görünüş | Açıklama |
|----------|----------------|
| **Temel öğrenci** | Karar ağaçları |
| **Anahtar ekleme** | Her bölmede, yalnızca rastgele bir özellik alt kümesini göz önünde bulundurun (genellikle sqrt(n_features)) |
| **Neden işe yarıyor** | Rastgele özellik seçimi ağaçların ilişkisini bozarak topluluğu daha sağlam hale getirir |
| **Hiperparametreler** | Ağaç sayısı; maksimum derinlik; yaprak başına minimum numune; maksimum özellikler |
| **Güçlü yönler** | Yüksek boyutlu verileri işler; aykırı değerlere karşı dayanıklı; özellik önemi sağlar |
| **Zayıf yönler** | Tek ağaçlara göre daha az yorumlanabilir; gürültülü regresyon görevlerine fazla uyum sağlayabilir |
---

## Artırma
### Nasıl Çalışır?
| Adım | Açıklama |
|------|-----------------|
| **1. İlk modeli eğitin** | Veriler üzerinde bir temel model (genellikle sığ bir ağaç / "kütük") eğitin |
| **2. Hataları tanımlayın** | Modelin hangi durumlarda hata yaptığını bulun |
| **3. Sonraki modeli eğitin** | Hatalara odaklanan yeni bir model eğitin (yeniden ağırlıklandırılmış veya artık takılan) |
| **4. Sırayla birleştir** | Her yeni model, önceki tüm modellerin birikmiş hatalarını düzeltir |
| **5. Tekrarla** | Belirli sayıda tur boyunca devam edin |
### Algoritmaların Güçlendirilmesi
| Algoritma | Kayıp Fonksiyonu | Temel Özellik |
|-----------|-----------------|-------------|
| **AdaBoost** | Üstel | Yanlış sınıflandırılmış örnekleri yeniden ağırlıklandırır; basit; gürültüye duyarlı |
| **Gradyan Arttırma** | Herhangi bir türevlenebilir kayıp | Artıklara uyar (kayıp derecesi); daha esnek |
| **XGBoost** | Düzenli degrade artırma | L1/L2 düzenlemesi; ikinci dereceden gradyanlar; donanım optimizasyonu |
| **IşıkGBM** | Gradyan bazlı tek taraflı örnekleme | Yaprak şeklinde büyüme; histogram tabanlı; büyük veri kümelerinde hızlı |
| **CatBoost** | Arttırılması emredildi | Kategorik özellikleri yerel olarak işler; aşırı uyumu azaltır |
### Arttırma vs Torbalama
| Boyut | Torbalama | Artırma |
|-----------|------------|----------|
| **Eğitim** | Paralel | Sıralı |
| **Odaklanma** | Farkı azaltır | Önyargıyı azaltır |
| **Temel modeller** | Yüksek varyans, düşük önyargı (derin ağaçlar) | Düşük varyans, yüksek önyargı (sığ ağaçlar / kütükler) |
| **Kombinasyon** | Eşit ağırlık | Performansa göre ağırlıklandırılmış |
| **Fazla uyum** | Daha az eğilimli | Çok fazla tur olursa fazla sığabilir |
| **Gürültü duyarlılığı** | Sağlam | Gürültülü verilere karşı hassas |
---

## İstifleme
### Nasıl Çalışır?
| Adım | Açıklama |
|------|-----------------|
| **1. Tren üssü modelleri** | Çeşitli modelleri eğitin (ör. rastgele orman, SVM, sinir ağı, degrade artırma) |
| **2. Tahminler oluşturun** | Giriş özellikleri olarak kullanıma hazır tahminleri (çapraz doğrulama) kullanın |
| **3. Meta modeli eğitin** | Temel modellerin tahminlerine göre ikinci düzey bir model eğitin |
| **4. Nihai tahmin** | Temel modeller öngörüyor; meta-model tahminlerini birleştiriyor |
### En İyi Yığınlama Uygulamaları
| Alıştırma | Nedeni |
|----------|-----------|
| **Çeşitli temel modelleri kullanın** | Farklı algoritmalar farklı hatalar yapar; çeşitlilik bütün meseledir |
| **Temel tahminler için çapraz doğrulamayı kullanın** | Meta-modelin aşırı uyum temel modellerinden yararlanmayı öğrenmesini engeller |
| **Meta modeli basit tutun** | Lojistik regresyon veya sığ ağaç; temel modeller işin ağır yükünü üstleniyor |
| **Meta modele ham özellikleri dahil edin** | Bazen meta-modelin orijinal özelliklere de erişmesine izin vermek yararlı olabilir |
---

## Oylama ve Ortalama Alma
### Zorunlu Oylama (Sınıflandırma)
| Modeli | Tahmin |
|----------|---------------|
| Model A | Sınıf 1 |
| Modeli B | Sınıf 0 |
| C Modeli | Sınıf 1 |
| **Çoğunluk oyu** | **Sınıf 1** |
### Yumuşak Oylama (Sınıflandırma)
| Modeli | P(Sınıf 0) | P(Sınıf 1) |
|----------|---------------|-----------|
| Model A | 0.3 | 0.7 |
| Modeli B | 0.6 | 0.4 |
| C Modeli | 0.4 | 0.6 |
| **Ortalama** | **0,43** | **0,57** |
| **Tahmin** | | **Sınıf 1** |
### Ağırlıklı Ortalama
| Modeli | Ağırlık | Tahmin |
|----------|-----------|-----------|
| Model A | 0,5 | 0.8 |
| Modeli B | 0.3 | 0.6 |
| C Modeli | 0.2 | 0.9 |
| **Ağırlıklı ortalama** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Pratik Rehberlik
### Hangi Topluluk Ne Zaman Kullanılmalı
| Senaryo | Önerilen Yöntem |
|----------|-----------|
| **Hızlı temel; tablo verileri** | Rastgele Orman |
| **Maksimum doğruluk; tablo verileri** | XGBoost / LightGBM / CatBoost |
| **Gürültülü veriler** | Torbalama (güçlendirme gürültüyü aşacaktır) |
| **Yorumlanabilirlik gerekli** | Tek model veya özellik önemi olan küçük topluluk |
| **Çeşitli model türleri** | İstifleme veya oylama |
| **Çevrimiçi öğrenme** | Akış topluluğu yöntemleri; uyarlanabilir güçlendirme |
| **Dengesiz veriler** | Dengeli Rastgele Orman; maliyete duyarlı güçlendirme |
### Topluluk Çeşitliliği Stratejileri
| Strateji | Açıklama |
|----------|----------------|
| **Farklı algoritmalar** | Ağaç tabanlı, doğrusal ve sinirsel modelleri birleştirin |
| **Farklı özellikler** | Modelleri farklı özellik alt kümeleri üzerinde eğitin |
| **Farklı veri alt kümeleri** | Torbalama; alt örnekleme |
| **Farklı hiperparametreler** | Çeşitli konfigürasyonlarla aynı algoritma |
| **Farklı zaman dilimleri** | Farklı zaman aralıklarında tren |
---

## Özet
Topluluk yöntemleri işe yarar çünkü birden fazla kusurlu modeli tek bir sağlam tahminde birleştirirler. Torbalama (rastgele ormanlar), önyükleme örnekleri ve ortalama alma üzerinde modelleri paralel olarak eğiterek varyansı azaltır. Güçlendirme (XGBoost, LightGBM, CatBoost), modelleri sırayla eğiterek ve her biri önceki hataları düzelterek önyargıyı azaltır. Yığınlama, çeşitli temel modelleri birleştirmek için bir meta model kullanır. Oylama ve ortalama alma en basit topluluklardır. Ortak nokta çeşitliliktir: topluluklar, bileşen modelleri bireysel olarak makul olduğunda ancak farklı hatalar yaptığında en iyi şekilde çalışır. Uygulamada, tablo halindeki veriler üzerinde gradyan artırma genellikle en yüksek performanslı tek yaklaşım olurken, çeşitli modellerin istiflenmesi yarışmalarda ve yüksek riskli uygulamalarda doğruluğu daha da ileriye taşır.