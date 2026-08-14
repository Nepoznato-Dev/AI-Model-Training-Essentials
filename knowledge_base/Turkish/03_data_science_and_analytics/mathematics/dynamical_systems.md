<!--
---
# Metadata
title: "Dynamical Systems"
description: "Ordinary and partial differential equations, phase portraits, equilibrium and stability, Lyapunov functions, chaos theory, Lorenz attractor, bifurcation diagrams, and PDEs"
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
    changes: "Initial deep-dive into dynamical systems"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [dynamical-systems, ode, pde, phase-portraits, stability, chaos, lorenz-attractor, bifurcation, lyapunov]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
  - "numerical_methods.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Dinamik Sistemler
**Dinamik sistem**, bir durumun sabit bir kurala göre zaman içinde nasıl geliştiğini açıklar. Gezegensel yörüngelerden nüfus dinamiklerine, hava koşullarından eğitim sinir ağlarına kadar dinamik sistem teorisi, olayların nasıl değiştiğini anlamak için gerekli dili ve araçları sağlar. Bu dosya sıradan diferansiyel denklemleri (ODE'ler), kısmi diferansiyel denklemleri (PDE'ler), kararlılık analizini, kaosu ve çatallanmaları kapsar.
---

## Adi Diferansiyel Denklemler (ODE'ler)
Bir ODE, bir fonksiyonu tek bir bağımsız değişkene (genellikle zamana) göre türevleriyle ilişkilendirir.
### Sınıflandırma
| Emlak | Türler |
|----------|----------|
| **Sipariş** | En yüksek türev mevcut (1. derece, 2. derece, vb.) |
| **Doğrusal ve Doğrusal Olmayan** | Doğrusal: y'' + p(t)y' + q(t)y = g(t); Doğrusal olmayan: başka herhangi bir şey |
| **Homojen** | g(t) = 0 (zorlayıcı terim yok) |
| **Otonom** | Açık bir zaman bağımlılığı yok: dy/dt = f(y) |
| **Sabit katsayılar** | p, q sabitlerdir |
### Birinci Dereceden ODE'ler
**Genel biçim:** dy/dt = f(t, y)
| Tür | Formu | Çözüm Yöntemi |
|------|----------|------|
| Ayrılabilir | dy/dt = g(t)h(y) | Ayırın ve entegre edin: ∫dy/h(y) = ∫g(t)dt |
| Doğrusal birinci dereceden | dy/dt + p(t)y = q(t) | İntegral faktörü: μ(t) = e^(∫p dt) |
| Tam | M(t,y)dt + N(t,y)dy = 0 ile ∂M/∂y = ∂N/∂t | Potansiyel fonksiyonu bulun F(t,y) |
| Bernoulli | dy/dt + p(t)y = q(t)yⁿ | Doğrusallaştırmak için v = y^(1−n)'yi değiştirin |
**Çalışılan Örnek (İntegrasyon Faktörü):** dy/dt + 2y = e^(−t), y(0) = 1'i çözün.
- İntegral faktörü: μ(t) = e^(∫2 dt) = e^(2t)
- Çarpın: d/dt[e^(2t)y] = e^(2t) · e^(−t) = e^t
- İntegral: e^(2t)y = e^t + C
- y(t) = e^(−t) + Ce^(−2t)
- Başlangıç koşulu: y(0) = 1 → 1 = 1 + C → C = 0
- Çözüm: y(t) = e^(−t)
### İkinci Dereceden Doğrusal ODE'ler
**Genel biçim:** ay'' + by' + cy = g(t)
**Homojen durum** (g ​​= 0): ar² + br + c = 0 karakteristik denklemini çözün.
| Ayırıcı | Kökler | Genel Çözüm |
|------------|----------|-------|
| b² > 4ac (aşırı sönümlü) | İki farklı gerçek r₁, r₂ | y = C₁e^(r₁t) + C₂e^(r₂t) |
| b² = 4ac (kritik olarak sönümlenmiş) | Tekrarlanan gerçek kök r | y = (C₁ + C₂t)e^(rt) |
| b² < 4ac (düşük sönümlü) | Karmaşık kökler α ± βi | y = e^(αt)(C₁ cos βt + C₂ sin βt) |
**Fiziksel yorum:** Bir kütle-yay-sönüm sistemi mx'' + bx' + kx = 0.
- Aşırı sönümleme: ağır sönümleme, salınım yok (kapı kapatıcı)
- Kritik sönümleme: salınım olmadan en hızlı geri dönüş (araba süspansiyonu tasarım hedefi)
- Düşük sönümlü: azalan genlikle salınır (gitar teli)
### ODE Sistemleri
Birçok gerçek sistem birden fazla etkileşimli değişken içerir:
dx/dt = f(x, y)
dy/dt = g(x, y)
Bu, vektör biçiminde yazılabilir: d**x**/dt = **F**(**x**)
**Doğrusal sistemler:** d**x**/dt = A**x**, burada A bir matristir.
Çözüm A'nın özdeğerlerine bağlıdır:
| Özdeğerler | Davranış |
|---------------|-----------|
| Hem gerçek, hem negatif | Kararlı düğüm (tüm yörüngeler orijine yakınsar) |
| İkisi de gerçek, pozitif | Kararsız düğüm |
| Gerçek, zıt işaretler | Eyer noktası (kararsız) |
| Karmaşık, negatif gerçek kısım | Kararlı spiral (sönümlü salınım) |
| Karmaşık, pozitif gerçek kısım | Kararsız sarmal |
| Saf hayali | Merkez (kapalı yörüngeler) |
---

## Aşama Portreleri
**Faz portresi** dinamik bir sistemin durum uzayındaki yörüngelerini (açıkça çözmeden) görselleştirir.
### Temel Özellikler
| Özellik | Açıklama |
|-----------|------------|
| **Sabit nokta (denge)** | Burada dx/dt = 0 (hareket yok) |
| **Yörünge** | Sistem tarafından durum uzayında izlenen yol |
| **Nullcline** | Bir bileşenin türevinin sıfır olduğu eğri |
| **Döngüyü sınırla** | İzole edilmiş kapalı yörünge (kendi kendine devam eden salınım) |
| **Cazibe havzası** | Belirli bir çekiciye yol açan başlangıç ​​koşulları kümesi |
| **Ayrılık** | Farklı çekim havzaları arasındaki sınır |
### Yırtıcı-Av Modeli (Lotka-Volterra)
dx/dt = αx − βxy (av)
dy/dt = δxy − γy (yırtıcı)
**Sabit noktalar:**
1. (0, 0) — yok olma (semer noktası)
2. (γ/δ, α/β) — bir arada yaşama (merkez — kapalı yörüngeler)
Sistem periyodik salınımlar sergiler: av artar → yırtıcılar artar → av azalır → yırtıcılar azalır → döngü tekrarları.
---

## Kararlılık Analizi
### Doğrusal Kararlılık
Sabit bir x* noktası için, onun etrafında doğrusallaştırın: u = x − x* olsun, o zaman du/dt ≈ J(x*)u burada J, Jacobian matrisidir.
**Kararlılık kriteri:** Sabit nokta:
- **Durağan** eğer J'nin tüm özdeğerleri negatif gerçel kısımlara sahipse
- **Kararsız** eğer herhangi bir özdeğer pozitif reel kısma sahipse
- **marjinal olarak kararlı** eğer özdeğerler sıfır gerçek parçaya sahipse (doğrusal olmayan analiz gerekir)
### Lyapunov Kararlılığı
**Lyapunov'un doğrudan yöntemi** doğrusallaştırma olmadan kararlılığı belirler.
A **Lyapunov fonksiyonu** V(x) şunu sağlar:
1. x ≠ x* için V(x*) = 0 ve V(x) > 0 (pozitif tanımlı)
2. yörüngeler boyunca dV/dt ≤ 0 (artmayan)
| Durum | Sonuç |
|-----------|---------------|
| dV/dt< 0 (negative definite) | Asymptotically stable |
| dV/dt ≤ 0 (negative semi-definite) | Stable (but may not converge) |
| dV/dt >0 | Kararsız |
**Çalışılan Örnek:** Sistem dx/dt = −x + y², dy/dt = −y.
- V(x,y) = x² + y²'yi (enerji benzeri fonksiyon) deneyin
- dV/dt = 2x(−x + y²) + 2y(−y) = −2x² + 2xy² − 2y²
- Başlangıç noktasına yakın: dV/dt ≈ −2x² − 2y² < 0 (küçük y için −2y² baskındır)
- Sonuç: köken lokal olarak asimptotik olarak stabildir
---

## Kaos Teorisi
**Kaos** deterministiktir ancak tahmin edilemez: Sistem kesin kurallara uyar, ancak başlangıç ​​koşullarındaki küçük farklılıklar çok farklı sonuçlara yol açar.
### Kaos için Gereksinimler
| Emlak | Açıklama |
|----------|----------------|
| Deterministik | Rastgelelik yoktur — kesin denklemlerle yönetilir |
| Başlangıç ​​koşullarına duyarlı | Yakındaki yörüngeler katlanarak ayrılıyor |
| Sınırlı | Yörüngeler sonsuza kaçmaz |
| Periyodik olmayan | Hiçbir zaman tam olarak tekrarlanmaz |
### Lorenz Sistemi
Deterministik kaosun klasik örneği:
dx/dt = σ(y − x)
dy/dt = x(ρ − z) − y
dz/dt = xy - βz
Standart parametrelerle σ = 10, ρ = 28, β = 8/3:
- Sistemin üç sabit noktası vardır ve hepsi kararsızdır.
- Yörüngeler sabit bir noktanın etrafında döner, sonra aniden diğerine geçer
- Sonuç **Lorenz çekicisi** — fraktal yapıya sahip garip bir çekici
**Lyapunov üssü:** Yakındaki yörüngelerin sapma oranını ölçer.
- Pozitif Lyapunov üssü → kaos
- Standart parametrelere sahip Lorenz sistemi için: en büyük üs ≈ 0,9 > 0
### Lojistik Haritası
Kaos sergileyen basit bir ayrık sistem:
x_{n+1} = rx_n(1 − x_n)
| Parametre r | Davranış |
|---------------|-----------|
| 0 < r < 1 | Nüfus tükeniyor (x → 0) |
| 1 < r < 3 | x = 1 − 1/r'de kararlı sabit nokta |
| 3 < r < 3,449 | Periyod-2 salınımı |
| 3,449 < r < 3,544 | Periyod-4 salınımı |
| 3,544 < r < 3,570 | Dönem-8, 16, 32, ... (iki katına çıkan dönem) |
| r ≈ 3,570 | Kaosun başlangıcı |
| 3.570 < r < 4 | Çoğunlukla kaotik, periyodik pencerelerle |
| r = 4 | [0, 1]'de tamamen kaotik |
### Kelebek Etkisi
Başlangıç ​​koşullarına hassas bağımlılığın popüler adı. Hava durumu sistemlerinde (Lorenz denklemleriyle modellenmiştir), Brezilya'da kanatlarını çırpan bir kelebeğin Teksas'ta bir kasırgayı tetiklemesi mümkündür; bunun nedeni kelebeğin sebep olması değil, küçük dalgalanmaların katlanarak artmasıdır.
---

## Çatallanma Teorisi
**Çatallanma**, bir parametre değiştikçe sistem davranışında meydana gelen niteliksel bir değişikliktir.
### Çatallanma Türleri
| Çatallanma | Normal Form | Ne Olur |
|-------------|------------|-------------|
| **Eyer düğümü** | dx/dt = r - x² | İki sabit nokta görünüyor/kayboluyor |
| **Transkritik** | dx/dt = rx − x² | İki sabit nokta değişim kararlılığı |
| **Dirgen (süperkritik)** | dx/dt = rx − x³ | Bir kararlı nokta iki kararlı + bir kararsız olarak bölünür |
| **Dirgen (kritik altı)** | dx/dt = rx + x³ | Dengesiz dallar çöker (çoğunlukla felaket olur) |
| **Hopf** | 2 boyutlu sistem | Sabit nokta kararsız hale gelir, limit döngüsü belirir |
### Çatallanma Diyagramı
Stabiliteyi gösteren sabit noktaların parametre değerine karşı grafiği (katı = stabil, kesikli = kararsız). Lojistik haritanın çatallanma diyagramı, kaosa giden periyodu ikiye katlayan rotayı ve ünlü **Feigenbaum sabiti** δ ≈ 4,669'u (ardışık çatallanma aralıkları arasındaki evrensel oran) ortaya koyuyor.
---

## Kısmi Diferansiyel Denklemler (PDE'ler)
PDE'ler birden fazla değişkenin fonksiyonlarını ve bunların kısmi türevlerini içerir.
### İkinci Dereceden Doğrusal PDE'lerin Sınıflandırılması
Au_xx + 2Bu_xy + Cu_yy + ... = 0 için:
| Tür | Durum | Davranış | Örnek |
|------|-----------|-----------|-----------|
| **Eliptik** | B² − AC< 0 | Steady-state, no time dependence | Laplace's equation: ∇²u = 0 |
| **Parabolic** | B² − AC = 0 | Diffusion, smoothing over time | Heat equation: u_t = αu_xx |
| **Hyperbolic** | B² − AC >0 | Dalga yayılımı, keskin özellikleri korur | Dalga denklemi: u_tt = c²u_xx |
### Isı Denklemi
∂u/∂t = α ∂²u/∂x²
Isı yayılımını, nüfus yayılımını, opsiyon fiyatlandırmasını (Black-Scholes) modeller.
| Emlak | Açıklama |
|----------|-----------|
| Pürüzsüzleştirme | Çözümler, süreksiz ilk verilerden bile anında sorunsuz hale gelir |
| Maksimum prensibi | Maksimum sıcaklık sınırda veya başlangıç ​​zamanında meydana gelir |
| Zamanın tersine çevrilebilirliği | Geri döndürülemez — geriye doğru koşamaz |
### Dalga Denklemi
∂²u/∂t² = c² ∂²u/∂x²
Titreşen telleri, sesi, elektromanyetik dalgaları modeller.
| Emlak | Açıklama |
|----------|-----------|
| Yayılma | Engeller c hızıyla hareket eder |
| Tersine çevrilebilirlik | Zaman tersine çevrilebilir |
| d'Alembert çözümü | u(x,t) = f(x−ct) + g(x+ct) (sol/sağ dalgaların süperpozisyonu) |
### Laplace Denklemi
∇²u = ∂²u/∂x² + ∂²u/∂y² = 0
Çözümler (harmonik fonksiyonlar) kararlı durum sıcaklığını, elektrostatik potansiyeli, sıkıştırılamaz akışkan akışını temsil eder.
| Emlak | Açıklama |
|----------|-----------|
| Ortalama değer özelliği | u(x₀) = x₀ merkezli herhangi bir daire üzerindeki u ortalaması |
| Maksimum prensibi | İç maksimum veya minimum yok |
| Benzersizlik | Tamamen sınır koşullarına göre belirlenir |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| DS Konsepti | Başvuru |
|-----------|----------------|
| ODE'ler | Sinirsel ODE'ler (sürekli derinlikli ağlar), yinelenen ağ dinamikleri |
| Stabilite analizi | Gradyan inişinin eğitim dinamikleri (kayıp istikrarlı bir şekilde azalıyor mu?) |
| Lyapunov fonksiyonları | Öğrenme algoritmalarının yakınsamasını, takviyeli öğrenme kararlılığını kanıtlama |
| Kaos | RNN'lerdeki hassasiyeti anlama (kaybolan/patlayan gradyanlar), hava tahmini |
| Çatallanma | Öğrenmede aşama geçişleri (grokking), antrenman dinamiklerinde rejim değişiklikleri |
| PDE'ler | Difüzyon modelleri (puan bazlı üretken modeller), fizik bilgili sinir ağları |
| Isı denklemi | Üretken modellemede difüzyon süreçleri, grafik Laplace yumuşatma |
| Dalga denklemi | Sismik veri işleme, ses sinyali modelleme |
| Lotka-Volterra | Nüfus dinamikleri, epidemiyoloji, rakip makine öğrenimi ajanları |
| Faz portreleri | Kayıp ortamı dinamiklerini görselleştirme, GAN eğitimini anlama |
---

## Özet
| Konu | Temel Fikir | Anahtar Aracı |
|----------|---------------|----------|
| ODE'ler | Fonksiyonlar ve bunların zamana türevleri | Karakteristik denklemler, integral faktörleri |
| ODE Sistemleri | Çoklu etkileşimli değişkenler | Jacobian'ın özdeğer analizi |
| Faz portreleri | Durum uzayında dinamikleri görselleştirme | Sabit noktalar, sıfır çizgileri, limit çevrimleri |
| Kararlılık | Sistem dengeye dönecek mi? | Doğrusallaştırma, Lyapunov fonksiyonları |
| Kaos | Deterministik öngörülemezlik | Lyapunov üsleri, garip çekiciler |
| Çatallanmalar | Parametrelerle niteliksel değişiklikler | Normal formlar, çatallanma diyagramları |
| PDE'ler | Çoklu Değişkenlerin Fonksiyonları | Isı, dalga ve Laplace denklemleri |
Dinamik sistem teorisi değişimin matematiğidir. Bazı sistemlerin neden sakinleştiğini, bazılarının neden salındığını ve bazılarının neden kaotik davrandığını açıklıyor. Veri bilimcileri için eğitim dinamiklerini anlamak, kararlı algoritmalar tasarlamak, zaman serilerini modellemek ve yeni nesil fizik bilgili makine öğrenimi modellerini oluşturmak için araçlar sağlar.