<!--
---
# Metadata
title: "Real Analysis"
description: "Sequences and series, limits, continuity, differentiability, Riemann and Lebesgue integration, metric spaces, uniform convergence, and measure theory"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into real analysis"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [real-analysis, sequences, series, limits, continuity, integration, metric-spaces, measure-theory, convergence]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Gerçek Analiz
Gerçek analiz, hesabın sağlam temelidir. Giriş seviyesi matematik size türevleri ve integralleri nasıl hesaplayacağınızı öğretirken, gerçek analiz bu tekniklerin *neden* işe yaradığını ve ne zaman başarısız olduklarını sorar. Olasılık teorisini, fonksiyonel analizi, optimizasyonu ve makine öğrenimi algoritmalarının arkasındaki teorik garantileri destekleyen limitlerin, sürekliliğin, yakınsamanın ve entegrasyonun kesin tanımlarını sağlar.
---

## Diziler ve Seriler
### Diziler
**dizi**, (aₙ)ₙ₌₁^∞ gerçek sayılarından oluşan sıralı bir listedir. Temel soru şudur: Dizi bir limite **yakınsar mı**?
**Yakınsaklığın tanımı:** Bir (aₙ) dizisi, her ε > 0 için, tüm n > N'ler için N mevcutsa, L'ye yakınsar: |aₙ − L| < ε.
| Konsept | Tanımı | Örnek |
|-----------|---------------|-----------|
| **Yakınsak** | lim aₙ = L mevcuttur ve sonludur | aₙ = 1/n → 0 |
| **Iraksak** | Yakınsamıyor | aₙ = (−1)ⁿ salınım yapar |
| **∞'dan ıraksak** | aₙ sınırsız büyür | aₙ = n² → ∞ |
| **Sınırlı** | \|aₙ\| Bazı M için ≤ M | Her yakınsak dizi sınırlıdır |
| **Tek ton** | Ya her zaman azalmayan ya da artmayan | aₙ = 1 − 1/n artıyor |
| **Cauchy dizisi** | ∀ε > 0, ∃N: ∀m,n > N, \|aₘ − aₙ\| < ε | ℝ'de Cauchy ⟺ yakınsak |
**Anahtar teoremler:**
- **Monoton Yakınsama Teoremi:** Her sınırlı monoton dizi yakınsar
- **Bolzano-Weierstrass Teoremi:** Her sınırlı dizinin yakınsak bir alt dizisi vardır
- **ℝ'nin Tamlığı:** ℝ'deki her Cauchy dizisi yakınsar (bu, ℝ'yi ℚ'den ayırır)
### Seri
Bir **seri** bir dizinin toplamıdır: Σₙ₌₁^∞ aₙ. Kısmi toplamlar dizisi Sₙ = Σₖ₌₁ⁿ aₖ yakınsarsa seri yakınsar.
### Yakınsama Testleri
| Testi | Durum | Sonuç |
|------|-----------|-----------|
| **Farklılık testi** | lim aₙ ≠ 0 | Seri ayrılıyor |
| **Karşılaştırma testi** | 0 ≤ aₙ ≤ bₙ ve Σbₙ yakınsar | Σaₙ yakınsar |
| **Oran testi** | lim \|aₙ₊₁/aₙ\| = L | L< 1, diverges if L >1 | ise yakınsar
| **Kök testi** | lim sup \|aₙ\|^(1/n) = L | L< 1, diverges if L >1 | ise yakınsar
| **İntegral testi** | aₙ = f(n), f azalan, pozitif | Σaₙ yakınsar iff ∫f(x)dx yakınsar |
| **Alternatif seriler** | aₙ azalan, lim aₙ = 0, değişen işaretler | Seriler yakınlaşıyor |
| **Mutlak yakınsaklık** | Σ\|aₙ\| yakınsıyor | Σaₙ yakınsar (ve yeniden düzenlemeler aynı toplamı verir) |
| **Koşullu yakınsama** | Σaₙ yakınsar ancak Σ\|aₙ\| uzaklaşıyor | Yeniden düzenlemeler herhangi bir toplamı verebilir (Riemann) |
### Önemli Seri
| Serisi | Toplam | Durum |
|----------|-----|-----------|
| Geometrik: Σ rⁿ | 1/(1−r) | \|r\| < 1 |
| p-series: Σ 1/nᵖ | Converges | p >1 |
| Harmonik: Σ 1/n | Uzaklaşıyor (= ∞) | — |
| Üstel: Σ xⁿ/n! | eˣ | Hepsi x |
| ln(1+x) için Taylor: Σ (−1)ⁿ⁺¹xⁿ/n | ln(1+x) | −1 < x ≤ 1 |
---

## Sınırlar ve Süreklilik
### Fonksiyonların Sınırları
**Tanım:** lim_{x→c} f(x) = L şu anlama gelir: her ε > 0 için, δ > 0 vardır, öyle ki 0 < |x − c| < δ |f(x) − L|'yi ima eder < ε.
Bu **ε-δ tanımıdır** - "x c'ye yaklaşırken f(x) L'ye yaklaşır" ifadesinin kesin versiyonudur.
### Süreklilik
Eğer lim_{x→c} f(x) = f(c) ise, f fonksiyonu **c**'de süreklidir. Eşdeğer olarak: her ε > 0 için δ > 0 vardır, öyle ki |x − c| < δ |f(x) − f(c)| anlamına gelir < ε.
**Süreksizlik türleri:**
| Tür | Açıklama | Örnek |
|------|-------------|--------|
| Çıkarılabilir | Limit mevcut ancak ≠ f(c) | f(x) = sin(x)/x, x = 0'da |
| Atla | Sol ve sağ sınırlar mevcuttur ancak farklıdır | Adım işlevi |
| Sonsuz | Limit ±∞ | f(x) = 1/x², x = 0 |
| Salınımlı | Sınır mevcut değil | x = 0'da f(x) = sin(1/x) |
### Sürekli Fonksiyonlar için Temel Teoremler
| Teorem | Açıklama |
|-----------|-----------|
| **Ara Değer Teoremi** | Eğer f, [a,b] üzerinde sürekliyse ve f(a) < k < f(b), o zaman ∃c ∈ (a,b): f(c) = k |
| **Ekstrem Değer Teoremi** | Eğer f, [a,b] üzerinde sürekli ise, f maksimum ve minimumuna [a,b] |
| **Sınırlılık Teoremi** | Eğer f [a,b] üzerinde sürekli ise, f [a,b] üzerinde sınırlıdır |
| **Tekdüze Süreklilik** | f, [a,b] üzerinde sürekli ise f, [a,b] üzerinde düzgün şekilde süreklidir (Heine-Cantor) |
**Çalışılmış Örnek (IVT):** x³ + x − 1 = 0'ın (0, 1)'de bir çözümü olduğunu gösterin.
- f(x) = x³ + x − 1 olsun. f süreklidir (polinom).
- f(0) = −1< 0 and f(1) = 1 >0.
- IVT'ye göre, ∃c ∈ (0,1): f(c) = 0.
---

## Farklılaşma
### Tanım
f'(c) = lim_{h→0} (f(c+h) − f(c)) / h
Eğer bu limit mevcutsa, f c'de **diferansiyellenebilir**'dir.
### Türevlenebilirlik ve Süreklilik
| İlişki | Açıklama |
|----------------|-----------|
| Türevlenebilir → Sürekli | Eğer f c'de türevlenebilirse, f c'de süreklidir |
| Sürekli ↛ Türevlenebilir | f(x) = \|x\| 0'da süreklidir ancak orada türevlenebilir değildir |
| Hiçbir yerde türevlenebilir | Weierstrass fonksiyonu: her yerde sürekli, hiçbir yerde türevlenebilir |
### Temel Sonuçlar
| Teorem | Açıklama |
|-----------|-----------|
| **Ortalama Değer Teoremi** | Eğer f, [a,b] üzerinde sürekli ve (a,b) üzerinde türevlenebilirse, ∃c: f'(c) = (f(b)−f(a))/(b−a) |
| **Rolle Teoremi** | f(a) = f(b) olduğunda MVT'nin özel durumu: ∃c: f'(c) = 0 |
| **L'Hôpital Kuralı** | Eğer lim f/g = 0/0 veya ∞/∞ ise, o zaman lim f/g = lim f'/g' (ikincisi mevcut olduğunda) |
| **Taylor Teoremi** | f(x) = Σₖ₌₀ⁿ f⁽ᵏ⁾(a)/k! · (x−a)ᵏ + Rₙ(x) açık kalanlı |
---

## Entegrasyon
### Riemann Entegrasyonu
**Riemann integrali** ∫ₐᵇ f(x)dx'i Riemann toplamlarının limiti olarak tanımlar.
**İnşaat:**
1. [a,b]'yi alt aralıklara ayırın: P = {x₀, x₁, ..., xₙ}
2. Örnek noktaları seçin tᵢ ∈ [xᵢ₋₁, xᵢ]
3. Riemann toplamı: S(P,f) = Σᵢ f(tᵢ)(xᵢ − xᵢ₋₁)
4. Eğer S(P,f)'nin limiti mesh → 0 olarak mevcutsa, f Riemann integrallenebilirdir
**Riemann entegre edilebilirlik kriterleri:**
| Durum | Entegre edilebilir mi? |
|-----------|----------------|
| Sürekli [a,b] | Evet |
| Sonlu sayıda süreksizlikle sınırlı | Evet |
| [a,b] üzerinde monoton | Evet |
| Dirichlet işlevi (ℚ üzerinde 1, irrasyonel sayılar üzerinde 0) | Hayır |
### Analizin Temel Teoremi
| Bölüm | Açıklama |
|------|---------------|
| **Bölüm 1** | Eğer f [a,b] üzerinde sürekli ise, o zaman F(x) = ∫ₐˣ f(t)dt türevlenebilirdir ve F'(x) = f(x) |
| **Bölüm 2** | Eğer F' = f ve f Riemann integrallenebilir ise, o zaman ∫ₐᵇ f(x)dx = F(b) − F(a) |
### Lebesgue Entegrasyonu
Riemann integralinin sınırlamaları vardır; analiz ve olasılıkta ortaya çıkan birçok fonksiyonu entegre edemez. **Lebesgue integrali** entegrasyonu çok daha geniş bir fonksiyon sınıfına genişletir.
**Ana fikir:** Etki alanını (x ekseni) bölümlemek yerine aralığı (y ekseni) bölümlendirin.
| Görünüş | Riemann İntegrali | Lebesgue İntegrali |
|----------|----------|------------------|
| Yaklaşım | Bölüm alanı (x ekseni) | Bölüm aralığı (y ekseni) |
| Bütünleşir | Sürekli, parçalı sürekli | Ölçülebilir işlevler |
| Limit teoremleri | Zayıf | Güçlü (Baskın Yakınsama, Monoton Yakınsama) |
| Kulplar | "Güzel" işlevler | Yoğun süreksizlik içeren fonksiyonlar |
| Kuruluşu | Klasik hesap | Modern olasılık teorisi |
**Lebesgue kriteri:** f, [a,b] üzerinde Riemann integrallenebilirdir, eğer f sınırlı ve hemen hemen her yerde süreklidir (süreksizlikler kümesinin ölçüsü sıfırdır).
---

## Metrik Uzaylar
**metrik uzay** "mesafe" kavramını soyut kümelere genelleştirir.
### Tanım
Bir **metrik uzay** (X, d), d uzaklık fonksiyonuna sahip bir X kümesidir: X × X → ℝ:
| Aksiyom | Açıklama |
|----------|---------------|
| Olumsuzluk | d(x,y) ≥ 0 |
| Kimlik | d(x,y) = 0 if x = y |
| Simetri | d(x,y) = d(y,x) |
| Üçgen eşitsizliği | d(x,z) ≤ d(x,y) + d(y,z) |
### Ortak Metrik Uzaylar
| Uzay | Ayarla | Metrik | Başvuru |
|----------|-----|-----------|-------------|
| ℝⁿ Öklid ile | ℝⁿ | d(x,y) = √Σ(xᵢ−yᵢ)² | Standart geometri |
| ℝⁿ Manhattan'la | ℝⁿ | d(x,y) = Σ\|xᵢ−yᵢ\| | Izgara tabanlı yollar, LASSO |
| ℝⁿ Chebyshev ile | ℝⁿ | d(x,y) = maksimum\|xᵢ−yᵢ\| | Satranç kralı mesafesi |
| Ayrık metrik | Herhangi bir set | d(x,y) = 1 eğer x≠y ise 0 eğer x=y | Topoloji örnekleri |
| Fonksiyon uzayı C[a,b] | Sürekli işlevler | d(f,g) = maksimum\|f(x)−g(x)\| | Yaklaşım teorisi |
| Daha fazla alan | p-integrallenebilir fonksiyonlar | d(f,g) = (∫\|f−g\|ᵖ)^(1/p) | Fonksiyonel analiz, ML normları |
### Metrik Uzaylarda Topolojik Kavramlar
| Konsept | Tanımı | Örnek |
|-----------|---------------|-----------|
| **Açık top** | B(x,r) = {y : d(x,y) < r} | ℝ cinsinden açık aralık (x−r, x+r) |
| **Açık set** | Sette her noktanın bir topu vardır | (0,1) ℝ'de açık |
| **Kapalı set** | Açık bir kümenin tamamlayıcısı | [0,1] ℝ |
| **Kapanış** | S | içeren en küçük kapalı küme | Kapanışı (0,1) = [0,1] |
| **Kompakt** | Her açık kapağın sonlu bir alt kapağı vardır | ℝⁿ'de: kapalı ve sınırlı (Heine-Borel) |
| **Tamamlandı** | Her Cauchy dizisi yakınsar | ℝ tamamlandı; ℚ değil |
---

## Düzgün Yakınsaklık
Bir fonksiyon dizisi (fₙ) iki şekilde yakınlaşabilir:
| Tür | Tanımı | Sürekliliği Koruyor mu? |
|------|---------------|-----------|
| **Noktasal** | ∀x: fₙ(x) → f(x) | Hayır |
| **Üniforma** | sup\|fₙ(x) − f(x)\| → 0 | Evet |
**Tek tip yakınsama** daha güçlüdür: yakınsama oranı her yerde aynıdır.
**Anahtar teoremler:**
- Sürekli fonksiyonların düzgün limiti süreklidir
- Riemann-integrallenebilir fonksiyonların düzgün limiti Riemann-integrallenebilirdir ve limitin integrali, integrallerin limitine eşittir
- **Weierstrass M-testi:** Eğer |fₙ(x)| ≤ Mₙ tüm x ve ΣMₙ yakınsamaları için, o zaman Σfₙ düzgün yakınsar
---

## Ölçü Teorisi
**Ölçü teorisi** uzunluk, alan ve hacim kavramlarını genelleştirir.
### Tanım
Bir X kümesindeki bir **ölçü**, aşağıdakileri sağlayan bir μ fonksiyonudur: Σ → [0, ∞] (burada Σ, alt kümelerin bir σ-cebiridir):
- μ(∅) = 0
- **Sayılabilir toplamsallık:** μ(∪ᵢ Aᵢ) = Σᵢ μ(Aᵢ) ayrık Aᵢ için
### Lebesgue Ölçüsü
ℝ üzerindeki **Lebesgue ölçüsü** λ uzunluk kavramını genişletir:
| Ayarla | Lebesgue Ölçüsü |
|-----|-----------------|
| Aralık [a,b] | b - a |
| Tek nokta {x} | 0 |
| Sonlu küme | 0 |
| Sayılabilir küme (örneğin, ℚ) | 0 |
| Cantor seti | 0 (sayılamayan ancak sıfır olarak ölçülür) |
| [0,1] ∩ ℚ | 0 |
| [0,1] \ ℚ | 1 |
### Temel Kavramlar
| Konsept | Tanımı |
|-----------|------------|
| **Hemen hemen her yerde (a.e.)** | Bir özellik, sıfır ölçü kümesi dışında geçerlidir |
| **Ölçülebilir fonksiyon** | Her açık setin ön görüntüsü ölçülebilir |
| **Lebesgue integrali** | İntegral ölçü teorisi kullanılarak tanımlandı |
| **Lᵖ boşlukları** | Sonlu p'inci kuvvet integrali olan fonksiyonların uzayları |
### Önemli Yakınsaklık Teoremleri
Bu teoremler ileri matematikte Lebesgue entegrasyonunun tercih edilmesinin nedenidir:
| Teorem | Açıklama |
|-----------|-----------|
| **Tek Tonlu Yakınsama** | Eğer fₙ ↑ f noktasal ve fₙ ≥ 0 ise, o zaman ∫fₙ → ∫f |
| **Hakim Yakınsama** | Eğer fₙ → f noktasal ve \|fₙ\| ≤ g (integrallenebilir), o zaman ∫fₙ → ∫f |
| **Fatou'nun Lemması** | ∫lim inf fₙ ≤ lim inf ∫fₙ |
Bu teoremler limitlerin ve integrallerin değiş tokuşuna izin verir; bu genel olarak Riemann entegrasyonu için başarısız olan bir şeydir.
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Analiz Konsepti | Başvuru |
|----------------|----------------|
| Limitler ve yakınsama | Yinelemeli algoritmaların (gradyan iniş, EM) ne zaman yakınsadığını anlama |
| Süreklilik | Geri yayılım için aktivasyon fonksiyonları sürekli olmalıdır |
| Türevlenebilirlik | Gradyan tabanlı optimizasyon, türevlenebilir kayıp fonksiyonları gerektirir |
| Ortalama Değer Teoremi | Sayısal yaklaşımda hata sınırları, yakınsama kanıtları |
| Metrik uzaylar | Kümelemede uzaklık fonksiyonları (k-ortalamalar, DBSCAN), en yakın komşular |
| Kompaktlık | Optimum çözümler için varlık kanıtları, sonlu boyutlu optimizasyonda Heine-Borel |
| Düzgün yakınsama | Yaklaşımların (sinir ağı evrensel yaklaşımı) her yerde işe yaradığının garanti edilmesi |
| Ölçü teorisi | Modern olasılığın temeli (olasılık bir ölçüdür), Lebesgue integralleri olarak beklenen değerler |
| Lebesgue entegrasyonu | Beklenen değer E[X] = ∫X dP bir Lebesgue integralidir |
| Lᵖ boşlukları | Düzenlemede L¹ (LASSO), L² (Ridge), Lᵖ normları |
| Baskın Yakınsama | Tahmincilerin tutarlılığının kanıtlanması, Bayes çıkarımında limitlerin değiştirilmesi |
---

## Özet
| Konu | Temel Fikir | Temel Sonuç |
|----------|---------------|-----------|
| Diziler | Sıralı numara listeleri | Yakınsama, Cauchy kriteri, Bolzano-Weierstrass |
| Serisi | Sonsuz toplamlar | Yakınsama testleri, mutlak ve koşullu |
| Limitler | "Yaklaşma" konusunda titiz yaklaşım | ε-δ tanımı |
| Süreklilik | Mola veya atlama yok | IVT, Ekstrem Değer Teoremi |
| Farklılaşma | Anlık değişim oranı | Ortalama Değer Teoremi, Taylor teoremi |
| Riemann Entegrasyonu | Eğrilerin altındaki alan | Analizin Temel Teoremi |
| Lebesgue Entegrasyonu | Ölçü yoluyla entegrasyon | Baskın/Monoton Yakınsama |
| Metrik Uzaylar | Soyut mesafe | Açık/kapalı kümeler, kompaktlık, bütünlük |
| Düzgün Yakınsaklık | Her yerde aynı oranda yakınsama | Sürekliliği ve entegre edilebilirliği korur |
| Ölçü Teorisi | Genelleştirilmiş uzunluk/alan/hacim | Olasılığın temeli, Lebesgue ölçüsü |
Gerçek analiz matematiğin büyüdüğü yerdir. Sezgisel "yaklaşma", "sürekli" ve "alan" kavramlarını kanıtlanabilen ve genelleştirilebilen kesin tanımlarla değiştirir. Analiz, veri bilimcileri ve makine öğrenimi mühendisleri için teorik garantileri sağlar: Gradyan iniş ne zaman birleşir? Bir kayıp fonksiyonu ne zaman iyi davranır? Sınırları ve beklentileri ne zaman paylaşabiliriz? Bunlar felsefi sorular değil; algoritmanızın sessizce çalışıp çalışmayacağını belirler.