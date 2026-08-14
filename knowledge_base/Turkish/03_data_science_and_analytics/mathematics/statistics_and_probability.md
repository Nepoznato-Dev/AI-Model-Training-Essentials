<!--
---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# İstatistik ve Olasılık
Olasılık ve istatistik, veri biliminin, makine öğreniminin ve bilimsel araştırmanın matematiksel temelleridir. Olasılık size olayların ne kadar muhtemel olduğunu söyler; istatistikler size verilerden nasıl sonuç çıkaracağınızı anlatır. Birlikte belirsizliği ölçülebilir, yönetilebilir bilgiye dönüştürürler.
---

## Olasılık Teorisi
### Temel Kavramlar
| Konsept | Açıklama | Örnek |
|-----------|------------|------------|
| **Örnek Uzay** | Tüm olası sonuçların kümesi | Zar atmak: {1, 2, 3, 4, 5, 6} |
| **Etkinlik** | Örnek uzayın bir alt kümesi | Çift sayıyı döndürme: {2, 4, 6} |
| **Olasılık** | 0 ile 1 arasındaki sayı ölçüm olasılığı | P(yuvarlanan 6) = 1/6 |
| **Koşullu Olasılık** | P(A|B): Belirli bir B'nin gerçekleşme olasılığı | P(yağmur | bulutlu) |
| **Bağımsızlık** | Birinin diğerini etkilemediği olaylar | Yazı-tura atışları bağımsızdır |
### Olasılık Kuralları
| Kural | Formül | Kullanım Örneği |
|------|------------|----------|
| **Ekleme Kuralı** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | A veya B Olasılığı |
| **Çarpma Kuralı** | P(A ∩ B) = P(A) × P(B|A) | A ve B'nin Olasılığı |
| **Tamamlama Kuralı** | P(A değil) = 1 − P(A) | Olayın gerçekleşmeme olasılığı |
| **Toplam Olasılık Yasası** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Birbirini dışlayan olaylara göre bölümleme |
| **Bayes Teoremi** | P(A|B) = P(B|A) × P(A) / P(B) | İnançları kanıtlarla güncellemek |
### Olasılık Dağılımları
| Dağıtım | Tür | Anahtar Parametreler | Kullanım Örneği |
|---------------|------|-----|----------|
| **Normal (Gauss)** | Sürekli | Ortalama (μ), Standart sapma (σ) | Doğa olayları, ölçüm hataları |
| **Binom** | Ayrık | n (denemeler), p (olasılık) | Başarı/başarısızlık sayıları |
| **Poisson** | Ayrık | λ (oran) | Zaman/uzayda nadir olaylar |
| **Üstel** | Sürekli | λ (oran) | Etkinlikler arasındaki süre |
| **Üniforma** | Her ikisi de | a, b (sınırlar) | Eşit derecede olası sonuçlar |
| **Ki-Kare** | Sürekli | k (serbestlik derecesi) | Uyum iyiliği testleri |
| **t-Dağıtım** | Sürekli | ν (serbestlik derecesi) | Küçük örnek çıkarım |
### Dağılımların Temel Özellikleri
| Emlak | Açıklama |
|----------|----------------|
| **Ortalama (Beklenen Değer)** | Dağılımın kütle merkezi: E[X] = Σ xᵢ × P(xᵢ) |
| **Farklılık** | Ortalamanın etrafına dağılın: Var(X) = E[(X − μ)²] |
| **Standart Sapma** | Varyansın karekökü; verilerle aynı birimler |
| **Çarpıklık** | Dağıtımın asimetrisi |
| **Basıklık** | "Kuyrukluluk" - kuyrukların ne kadar ağır olduğu |
---

## İstatistiksel Çıkarım
### Tanımlayıcı ve Çıkarımsal İstatistikler
| | Açıklayıcı | Çıkarımsal |
|---|-------------|-------------|
| **Amaç** | Verileri özetleme ve açıklama | Örnekten popülasyon hakkında sonuçlar çıkarma |
| **Araçlar** | Ortalama, medyan, mod, standart sapma, grafikler | Hipotez testleri, güven aralıkları, regresyon |
| **Kapsam** | Yalnızca sahip olduğunuz veriler | Örneğinizin ötesinde genelleme |
### Hipotez Test Çerçevesi
| Adım | Açıklama |
|------|-----------------|
| 1. **Durum hipotezleri** | Boş hipotez (H₀): etki yok; Alternatif (H₁): etki mevcut |
| 2. **Önemlilik düzeyini seçin** | α = 0,05 (geleneksel) |
| 3. **Testi seçin** | Veri türüne, örneklem büyüklüğüne ve varsayımlara dayalı |
| 4. **Test istatistiklerini hesaplayın** | Seçilen teste bağlıdır |
| 5. **p-değerini bulun** | H₀ doğruysa verileri gözlemleme olasılığı |
| 6. **Karar verin** | p < α ise H₀'yi reddedin; aksi halde H₀'yi reddetmeyin |
### Ortak İstatistik Testleri
| Testi | Ne Zaman Kullanılmalı | Neleri Karşılaştırır |
|------|-------------|------|
| **t-testi** | 1–2 grubun ortalamalarını karşılaştırın | Anlam(ları) bir değere veya birbirine göre gruplandırın |
| **Ki-kare testi** | Kategorik veriler | Gözlemlenen ve beklenen frekanslar |
| **ANOVA** | 3+ grubun ortalamalarını karşılaştırın | Grup içi ve grup içi fark |
| **Mann-Whitney U** | T-testine parametrik olmayan alternatif | İki grubun sıralama dağılımları |
| **Pearson korelasyonu** | İki sürekli değişken arasındaki doğrusal ilişki | r değeri −1'den +1'e |
| **Spearman korelasyonu** | Monotonik ilişki (sıralamaya dayalı) | sıralı veya normal olmayan veriler için ρ değeri |
### Güven Aralıkları
Bir güven aralığı, bir popülasyon parametresi için bir dizi makul değer verir:
- **Ortalama için %95 GA** (bilinen σ): x̄ ± 1,96 × (σ / √n)
- **Yorum**: "Gerçek popülasyon ortalamasının bu aralıkta yer aldığından %95 eminiz"
- **Daha geniş güven aralığı** = daha fazla belirsizlik (daha küçük örneklem, daha yüksek değişkenlik veya daha yüksek güven düzeyi)
---

## Regresyon Analizi
### Regresyon Türleri
| Tür | Bağımlı Değişken | Kullanım Örneği |
|----------|-----------|----------|
| **Doğrusal Regresyon** | Sürekli | Ev fiyatlarını, satışlarını tahmin etmek |
| **Lojistik Regresyon** | İkili (0/1) | Sınıflandırma: spam tespiti, hastalık teşhisi |
| **Polinom Regresyon** | Sürekli (kavisli) | Büyüme eğrileri, doğrusal olmayan eğilimler |
| **Çoklu Regresyon** | Sürekli (2+ tahminci) | Karıştırıcıları kontrol etmek |
| **Sırt / Kement** | Sürekli (düzenlenmiş) | Aşırı uyumu önleme, özellik seçimi |
### Doğrusal Regresyonun Temelleri
Model: **y = β₀ + β₁x + ε**
| Bileşen | Anlamı |
|-----------|------------|
| β₀ (kesme) | x = 0 olduğunda y'nin değeri |
| β₁ (eğim) | x'teki bir birimlik değişim için y'deki değişim |
| ε (hata terimi) | Açıklanamayan varyasyon |
**Temel ölçümler:**
- **R² (belirleme katsayısı)**: Modelin açıkladığı varyans oranı (0 ila 1)
- **Düzeltilmiş R²**: R², öngörücü sayısı nedeniyle cezalandırıldı
- **RMSE**: Ortalama kare hatasının kökü — y ile aynı birimlerdeki ortalama tahmin hatası
### Doğrusal Regresyonun Varsayımları
| Varsayım | Ne Anlama Geliyor | Nasıl Kontrol Edilir |
|-----------|-----------------|--------------|
| **Doğrusallık** | X ve Y arasındaki ilişki doğrusaldır | Dağılım grafikleri |
| **Bağımsızlık** | Gözlemler bağımsızdır | Çalışma tasarımı |
| **Homoskedastisite** | Artıkların sabit varyansı | Kalan araziler |
| **Normallik** | Artıklar normal şekilde dağıtılır | Q-Q grafiği, Shapiro-Wilk testi |
| **Çoklu bağlantı yok** | Tahminler yüksek oranda ilişkili değil | VIF (Varyans Enflasyon Faktörü) |
---

## Bayes İstatistikleri
### Frequentist ve Bayesian
| | Frequentist | Bayesian |
|---|-----------------|----------|
| **Olasılık demek** | Uzun vadeli frekans | İnanç derecesi |
| **Parametreler** | Düzeltildi ancak bilinmiyor | Dağılımlı rastgele değişkenler |
| **Kullanımlar** | p değerleri, güven aralıkları | Arka dağılımlar, güvenilir aralıklar |
| **Güçlü yönler** | Objektif, köklü | Ön bilgiyi ve sezgisel yorumu birleştirir |
### Bayes Teoremi Uygulamada
**Sonraki = (Olasılık × Önceki) / Kanıt**
Örnek – tıbbi testler:
- Hastalık yaygınlığı: %1 (önceki)
- Test hassasiyeti: %95 (gerçek pozitif oran)
- Test özgüllüğü: %90 (gerçek negatif oran)
- Testiniz pozitif çıkarsa: P(hastalık | pozitif) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ %8,8
Bu mantığa aykırı sonuç (hastalık nadir olduğunda çoğu olumlu sonuç yanlış pozitiftir) **temel oran yanılgısıdır** ve Bayesci düşüncenin neden önemli olduğunu gösterir.
---

## Pratik İpuçları
- **Herhangi bir istatistiksel testi çalıştırmadan önce daima verilerinizi görselleştirin**
- **Varsayımları kontrol edin** — ihlaller sonuçları geçersiz kılabilir
- **Etki büyüklüğü önemlidir** — istatistiksel olarak anlamlı bir sonuç pratikte anlamsız olabilir
- **Korelasyon nedensellik değildir** — güçlü korelasyonlar bile kafa karıştırıcı olabilir
- **Çoklu karşılaştırma** hatalı pozitif oranları artırır — düzeltmeleri uygulayın (Bonferroni, FDR)
- **Yalnızca p değerlerini değil, güven aralıklarını da bildirin**
---

## Bu Neden Önemli?
İstatistikler bilimsel araştırmanın, iş analitiğinin ve makine öğreniminin omurgasıdır. Bu olmadan, sinyali gürültüden ayırt edemez, rastgele dalgalanmalardan gerçek etkileri belirleyemez veya niceliksel belirsizlikle tahminlerde bulunamazsınız. İster A/B testlerini analiz ediyor olun, ister makine öğrenimi modellerini eğitiyor olun, ister araştırma makalelerini okuyor olun, istatistik okuryazarlığı çok önemlidir.