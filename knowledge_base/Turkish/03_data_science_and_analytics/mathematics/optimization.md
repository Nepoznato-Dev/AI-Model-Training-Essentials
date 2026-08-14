<!--
---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Optimizasyon
Optimizasyon, bir dizi uygulanabilir çözüm arasından en iyi çözümü bulmanın matematiğidir. Şunu sorar: Bir fonksiyon ve kısıtlamalar verildiğinde, hangi girdi çıktıyı en aza indirir (veya en üst düzeye çıkarır)? Optimizasyon, makine öğreniminin motorudur; bir modelin eğitilmesi, kayıp fonksiyonunun en aza indirilmesi anlamına gelir. Yöneylem araştırmasında, ekonomide, mühendislik tasarımında ve hemen hemen her niceliksel alanda karşımıza çıkar.
---

## Problem Formülasyonu
Genel bir **optimizasyon problemi** şu şekildedir:
f(x)'i en aza indirin
Şu şartlara tabidir: gᵢ(x) ≤ 0 (eşitsizlik kısıtlamaları), hⱼ(x) = 0 (eşitlik kısıtlamaları)
| Dönem | Anlamı |
|------|------------|
| **Amaç fonksiyonu** f(x) | En aza indirilecek (veya en üst düzeye çıkarılacak) miktar |
| **Karar değişkenleri** x | Kontrol edebildiğimiz değerler |
| **Uygun bölge** | Tüm kısıtlamaları karşılayan tüm x'lerin kümesi |
| **Küresel minimum** | Tüm mümkün x'ler için f(x*) ≤ f(x) ile mümkün x* |
| **Yerel minimum** | Bir komşuluktaki tüm mümkün x'ler için f(x*) ≤ f(x) ile mümkün x* |
| **Dışbükey sorun** | f dışbükeydir, uygun bölge dışbükey kümedir (yerel min = global min) |
---

## Doğrusal Programlama (LP)
Hem amaç hem de tüm kısıtlamalar **doğrusal** olduğunda, problem doğrusal bir programdır.
### Standart Form
Cᵀx'i en aza indirin
Aşağıdakilere tabidir: Ax ≤ b, x ≥ 0
burada c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Özellikler
| Emlak | Açıklama |
|----------|-----------|
| Dışbükeylik | DP her zaman dışbükey bir problemdir |
| Optimum çözüm | Her zaman uygun politopun tepe noktasında (köşe noktasında) |
| Varoluş | Uygun bölge sınırlıysa ve boş değilse, optimal çözüm mevcuttur |
| Çoklu optimum | İki köşe optimalse, aralarındaki kenardaki her nokta da optimaldir |
### Simpleks Yöntemi
**simplex yöntemi** (Dantzig, 1947), uygun politopun kenarları boyunca tepe noktasından tepe noktasına doğru hareket eder ve optimuma ulaşana kadar her zaman hedefi iyileştirir.
| Emlak | Değer |
|----------|----------|
| En kötü durum zamanı | O(2ⁿ) (üstel — pratikte nadirdir) |
| Ortalama vaka süresi | Çoğu pratik problem için polinom |
| Anahtar fikir | Daha iyi objektif değere sahip bitişik köşeye git |
**Algoritma (genel bakış):**
1. Temel uygulanabilir bir çözümle başlayın (politopun tepe noktası)
2. Bir giriş değişkeni seçin (hedefi geliştiren bir değişken)
3. Bir ayrılan değişken seçin (fizibiliteyi koruyun)
4. Pivot: yeni köşeye git
5. İyileşen bir yön kalmayıncaya kadar tekrarlayın
### İç Nokta Yöntemleri
Simplex'e alternatif: optimuma uygun bölgenin içinden yaklaşın.
| Emlak | Değer |
|----------|----------|
| En kötü durum zamanı | Polinom (bazı değişkenler için O(n³·⁵)) |
| Pratik performans | Büyük problemlerde simpleks ile rekabet edebilir |
| Anahtar fikir | İç kısımda "merkezi yolu" takip edin |
### Çalışılan LP Örneği
**Sorun:** Bir fabrika sandalyeler (x₁) ve masalar (x₂) üretiyor.
- Kâr: Sandalye başına 30$, masa başına 50$
- Ahşap: 2x₁ + 4x₂ ≤ 100 (tahta ayakları mevcuttur)
- İşçilik: x₁ + 3x₂ ≤ 60 (mevcut saat)
- Maksimuma çıkarma: 30x₁ + 50x₂
**Çözüm (2 değişken için grafiksel yöntem):**
- Uygun bölgenin köşe noktaları: (0,0), (30,0), (40,10), (0,20)
- Her köşedeki hedefi değerlendirin:
  - (0,0): kar = 0
  - (30,0): kâr = 900
  - (40,10): kar = 1700 ← optimal
  - (0,20): kâr = 1000
- **Optimal:** x₁ = 40 sandalye, x₂ = 10 masa, kâr = 1700 ABD doları
---

## Dışbükey Optimizasyon
Eğer amaç fonksiyonu dışbükeyse ve uygun bölge bir dışbükey küme ise sorun **dışbükey**dir.
### Dışbükey Kümeler ve Fonksiyonlar
| Konsept | Tanımı |
|-----------|------------|
| **Dışbükey küme** | Kümedeki herhangi bir x, y ve t ∈ [0,1] için: tx + (1−t)y de kümenin içindedir |
| **Dışbükey fonksiyon** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) tüm t ∈ [0,1] |
| **Tam dışbükey** | t ∈ (0,1) ve x ≠ y | için eşitsizlik kesindir |
**Anahtar özellik:** Dışbükey optimizasyon için her yerel minimum, global bir minimumdur.
### Ortak Dışbükey Fonksiyonlar
| İşlev | Dışbükey mi? | Nerede |
|----------|------------|-------|
| balta + b (doğrusal) | Evet (ve içbükey) | Her yerde |
| x² | Evet | ℝ |
| eˣ | Evet | ℝ |
| −log(x) | Evet | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Evet | ℝⁿ |
| max(f₁, f₂) if f₁, f₂ dışbükey | Evet | Alan adlarının kesişimi |
### Gradyan İnişi
Makine öğrenimindeki en temel optimizasyon algoritması.
**Güncelleme kuralı:** x_{k+1} = x_k − α∇f(x_k)
burada α > 0 **öğrenme oranıdır** (adım boyutu).
| Varyant | Kuralı Güncelle | Avantajı |
|-----------|---------------|-----------|
| **Toplu GD** | x ← x − α∇f(x) | Kararlı yakınsama |
| **Stokastik GD (SGD)** | x ← x − α∇fᵢ(x) (bir örnek) | Yineleme başına hızlı, yerel minimumlardan kaçıyor |
| **Mini parti SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Toplu ve stokastik arasındaki denge |
| **İvme** | v ← βv − α∇f(x); x ← x + v | Düz bölgelerde hızlanır |
| **Adem** | Parametre başına uyarlanabilir öğrenme oranları | Derin öğrenme için kutudan çıktığı haliyle iyi çalışır |
| **RMSprop** | Gradyan büyüklüğünün ortalamasını çalıştırarak öğrenme oranını ölçeklendirin | RNN'ler için iyi |
### Yakınsama Oranları
| Yöntem | Dışbükey f | Kesinlikle Dışbükey f |
|----------|----------|----------|
| Gradyan iniş | Ö(1/k) | O((1−μ/L)ᵏ) (doğrusal) |
| SGD | O(1/√k) | Ö(1/k) |
| Hızlandırılmış GD (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
burada k = yineleme sayısı, μ = güçlü dışbükeylik parametresi, L = Lipschitz sabiti.
### Öğrenme Oranını Seçme
| Strateji | Açıklama |
|----------|----------------|
| Sabit α | Basit ama birbirinden uzaklaşabilir (çok büyük) veya yavaş yavaş birleşebilir (çok küçük) |
| Hat arama | Gradyan yönü boyunca f(x − α∇f(x))'i en aza indiren α'yı bulun |
| Çürüme programları | α_t = α₀ / (1 + βt) veya α_t = α₀ · βᵗ |
| Isınma | Küçük başlayın, artırın, sonra azaltın (transformatör eğitiminde yaygındır) |
| Uyarlanabilir (Adam) | Gradyan istatistiklerine dayalı parametre başına öğrenme oranları |
---

## Kısıtlı Optimizasyon
### Lagrange Çarpanları
Sorun için: h(x) = 0'a bağlı olarak f(x)'i en aza indirin.
**Lagrange:** L(x, λ) = f(x) + λh(x)
Optimumda: ∇ₓL = 0 ve ∇_λL = 0 (bu da h(x) = 0'ı verir).
**Çalışılan Örnek:** x + y = 1'e bağlı olarak f(x,y) = x² + y²'yi minimuma indirin.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Kısıtlama: x + y = 1 → −λ = 1 → λ = −1
- Çözüm: x = 1/2, y = 1/2, f = 1/2
### KKT Koşulları
**Karush-Kuhn-Tucker (KKT) koşulları** Lagrange çarpanlarını eşitsizlik kısıtlamalarına genelleştirir.
Şunun için: gᵢ(x) ≤ 0, hⱼ(x) = 0'a bağlı olarak f(x)'i en aza indirin.
**Lagrange:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**KKT koşulları** (optimalite için gerekli):
| Durum | Denklem |
|---------------|----------|
| Durağanlık | ∇ₓL = 0 |
| İlk fizibilite | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| İkili fizibilite | λᵢ ≥ 0 |
| Tamamlayıcı gevşeklik | λᵢgᵢ(x) = her i için 0 |
**Tamamlayıcı gevşeklik** şu anlama gelir: gᵢ kısıtı aktif değilse (gᵢ(x) < 0), o zaman λᵢ = 0 (kısıtlama çözümü etkilemez).
Slater koşulunu sağlayan dışbükey problemler için KKT koşulları hem gerekli hem de yeterlidir.
---

## İkilik
Her optimizasyon probleminin (**birincil**) ilişkili bir **ikili** problemi vardır.
### Zayıf ve Güçlü Dualite
| Konsept | Açıklama |
|-----------|-----------|
| **Çift işlev** | g(λ, ν) = infₓ L(x, λ, ν) |
| **İkili sorun** | λ ≥ 0'a bağlı olarak g(λ, ν)'yi maksimuma çıkarın |
| **Zayıf dualite** | İkili optimal ≤ Temel optimal (her zaman geçerli) |
| **Güçlü dualite** | İkili optimal = Primal optimal (Slater koşuluyla ilgili dışbükey problemler için geçerlidir) |
| **İkilik boşluğu** | Primal optimal – İkili optimal (güçlü dualite altında sıfır) |
### Dualite Neden Önemlidir
| Başvuru | Dualite Nasıl Yardımcı Olur |
|---------------|-----------|
| Alt sınırlar | Dual, temel çözümün ne kadar iyi olduğuna dair bir sertifika veriyor |
| SVM'ler | SVM sorununun ikilisi çekirdek hilesine yol açıyor |
| Hassasiyet analizi | İkili değişkenler, kısıtlamaların gevşetilmesi durumunda optimum değişimin ne kadar olduğunu ölçer |
| Ayrışma | Büyük problemler ikili |
---

## Tamsayı Programlama
Değişkenlerin bir kısmının veya tamamının **tamsayı** olması gerektiğinde, sorun çok daha zorlaşır (genel olarak NP-zor).
### Türler
| Tür | Açıklama |
|------|-----------------|
| Saf IP | Tüm değişkenler tam sayı olmalıdır |
| Karma IP (MIP) | Bazı değişkenler tamsayı, bazıları sürekli |
| İkili IP | Değişkenler {0, 1} ile sınırlıdır |
### Çözüm Yöntemleri
| Yöntem | Fikir |
|----------|------|
| **Dal ve sınır** | Alt problemlere bölün, DP gevşemelerini çözün, budama |
| **Düzlemlerin kesilmesi** | LP gevşemesini sıkılaştırmak için doğrusal kısıtlamalar ekleyin |
| **Dallandır ve kes** | Dal ve sınırı kesme düzlemleriyle birleştirin |
| **Buluşsal yöntem** | Yaklaşık çözümler için açgözlü, yerel arama, simüle edilmiş tavlama |
---

## Sezgisel ve Metasezgisel Yöntemler
Kesin optimizasyonun zor olduğu durumlarda buluşsal yöntemler iyi (mutlaka optimal olmayan) çözümler bulur.
| Yöntem | Anahtar Fikir | En İyisi |
|----------|----------|----------|
| **Degrade iniş** | En dik inişi takip edin | Pürüzsüz, türevlenebilir fonksiyonlar |
| **Newton'un yöntemi** | İkinci dereceden (eğrilik) bilgileri kullanın | Pürüzsüz, iyi koşullandırılmış problemler |
| **Tavlama benzetimi** | Azalan olasılıkla daha kötü çözümleri kabul edin | Küresel optimizasyon, kombinatoryal |
| **Genetik algoritmalar** | Seçim, çaprazlama ve mutasyonu kullanarak bir popülasyon geliştirin | Çok amaçlı, türevlendirilemeyen |
| **Parçacık sürüsü** | Temsilciler, en iyi bilinen konumlardan etkilenerek uzayı keşfediyor | Sürekli, dışbükey olmayan |
| **Bayes optimizasyonu** | Yedek model oluşturun, edinme işlevini kullanın | Pahalı kara kutu fonksiyonları (hiperparametre ayarı) |
### Newton'un Optimizasyon Yöntemi
**Güncelleme kuralı:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
burada H, Hessian matrisidir (ikinci türevlerin matrisi).
| Emlak | Değer |
|----------|----------|
| Yakınsama oranı | İkinci dereceden (optimuma yakın) |
| Yineleme başına maliyet | Hessian inversiyonu için O(n³) |
| Gerektirir | İki kez türevlenebilir, pozitif tanımlı Hessian |
| Yarı-Newton (BFGS) | Degradelerden yaklaşık Hessian | O(n²) yineleme başına |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Optimizasyon Konsepti | Başvuru |
|---------------------|----------------|
| Gradyan iniş | Sinir ağlarının eğitimi, lojistik regresyon, herhangi bir türevlenebilir model |
| SGD ve çeşitleri | Büyük ölçekli makine öğrenimi (mini toplu eğitim), çevrimiçi öğrenme |
| Adam, RMSprop | Derin öğrenme için varsayılan optimize ediciler |
| Dışbükey optimizasyon | SVM'ler, lojistik regresyon, LASSO, Ridge (global optimum garantisi) |
| Lagrange çarpanları | Kısıtlı öğrenme, adil makine öğrenimi, kaynak tahsisi |
| KKT koşulları | SVM ikilisini türetme, kısıtlama etkinliğini anlama |
| İkilik | SVM çekirdek numarası, duyarlılık analizi, ayrıştırma yöntemleri |
| Doğrusal programlama | Kaynak tahsisi, portföy optimizasyonu, ağ akışı |
| Tamsayı programlama | Özellik seçimi (ikili), planlama, kombinatoryal problemler |
| Bayes optimizasyonu | Hiperparametre ayarlama (Optuna, Hyperopt) |
| Newton/yarı-Newton | Küçük ve orta ölçekli problemler için ikinci dereceden yöntemler (L-BFGS) |
---

## Özet
| Yöntem | Sorun Türü | Garantiler | Ölçek |
|----------|----------------|------------|-------|
| Tek Yönlü | Doğrusal programlama | Tam optimum | Milyonlarca değişken |
| İç nokta | Dışbükey (LP, QP, SOCP) | Tam optimum | Büyük ölçekli |
| Gradyan iniş | Pürüzsüz kısıtlamasız | Yerel dakikaya yakınsar | Çok büyük (derin öğrenme) |
| SGD | Büyük ölçekli ampirik risk | Yakınsar (çürümeyle birlikte) | Devasa veri kümeleri |
| Newton / BFGS | Pürüzsüz, iki kez türevlenebilir | İkinci dereceden yakınsama | Küçük-orta |
| KKT / Lagrange | Kısıtlanmış (dışbükey) | Tam koşullar altında | Orta |
| Dal ve sınır | Tamsayı programlama | Tam optimum | Küçük-orta |
| Buluşsal Yöntem | Herhangi biri (dışbükey olmayan, kombinatoryal) | Garanti yok | Değişir |
Optimizasyon, makine öğreniminde tartışmasız en önemli matematiksel araçtır. Doğrusal regresyondan büyük dil modellerine kadar eğittiğiniz her model, bir optimizasyon probleminin çözülmesini içerir. Bir problemin ne zaman dışbükey olduğunu (garantili global optimum), gradyan inişinin ne zaman yakınsayacağını ve kısıtlamaların nasıl ele alınacağını anlamak size öğrenme algoritmalarını tasarlamak, hata ayıklamak ve geliştirmek için teorik temel sağlar.