---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Sayısal Yöntemler
Sayısal yöntemler matematiksel teori ile pratik hesaplama arasındaki köprüdür. Saf matematik çözümlerin var olduğunu kanıtlarken, sayısal yöntemler aslında yaklaşık yanıtları sonlu hassasiyetle hesaplar. Her makine öğrenimi modeli, fizik simülasyonu ve veri analizi hattı sonuçta sayısal hesaplamaya dayanır. Bu yöntemleri (doğruluklarını, kararlılıklarını ve sınırlamalarını) anlamak, güvenilir yazılım oluşturmak için çok önemlidir.
---

## Kayan Nokta Aritmetiği
Bilgisayarlar gerçek sayıları sonlu hassasiyetle temsil eder. **IEEE 754 standardı** kayan nokta sayılarının nasıl saklanacağını ve yönetileceğini tanımlar.
### IEEE 754 Formatları
| Biçim | Bitler | Üs | Mantis | Yaklaşık Ondalık Basamaklar | Menzil |
|----------|----------|----------|----------|--------------------------|-------|
| Yarı (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Tek (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Çift (fp64) | 64 | 11 | 52 | 15.9 | ±1,8 × 10³⁰⁸ |
### Makine Epsilon
**Makine epsilon** (ε_mach), kayan noktada 1 + ε_mach > 1 olacak en küçük sayıdır.
| Biçim | ε_mach |
|----------|-----------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Yaygın Tuzaklar
| Tuzak | Örnek | Sonuç |
|-----------|-----------|-------------|
| **Felaket iptal** | Hesaplama (1 + x) − 1 küçük x için | Önemli rakamların kaybı |
| **Soğurma** | fp32'de 10⁸ + 1 = 10⁸ | Küçük değerler büyük meblağlarda kayboluyor |
| **İlişkili olmama** | (a + b) + c ≠ a + (b + c) | Toplam sipariş önemlidir |
| **Sıfıra yakın bölme** | 1 / 10⁻³⁰⁰ → taşma | Sonsuzluk veya NaN |
### Etki Azaltma Stratejileri
| Strateji | Açıklama |
|----------|----------------|
| **Kahan toplamı** | Emilim hatasını azaltmak için telafi edilmiş toplama |
| **Kahan-Babuska-Neumaier** | Kahan toplamının geliştirilmiş versiyonu |
| **Sıralı toplama** | Emilmeyi önlemek için önce küçük sayıları toplayın |
| **Çift-çift aritmetiği** | Daha fazla hassasiyet için ikili çiftler kullanın |
| **Koşullandırma analizi** | Sorunun kendisinin hataları artırıp artırmadığını anlayın |
---

## Kök Bulma
f(x) = 0 olacak şekilde x'i bulmak.
### İkiye Bölme Yöntemi
| Emlak | Değer |
|----------|----------|
| Gerektirir | f sürekli, f(a) ve f(b) zıt işaretlere sahiptir |
| Yakınsama | Doğrusal (hata her adımı yarıya indirir) |
| Garantili mi? | Evet — her zaman yakınsar |
| d basamakları için yinelemeler | ≈ d / log₁₀(2) ≈ 3,32d |
**Algoritma:**
1. [a, b] aralığıyla başlayın; burada f(a) · f(b) < 0
2. Orta nokta c = (a + b) / 2'yi hesaplayın
3. Eğer f(c) = 0 veya |b − a| < tolerans, durdurma
4. Eğer f(a) · f(c) < 0 ise b = c olsun; Aksi takdirde a = c'yi ayarlayın
5. Tekrarlayın
### Newton-Raphson Yöntemi
| Emlak | Değer |
|----------|----------|
| Gerektirir | f türevlenebilir, kökte f'(x) ≠ 0 |
| Yakınsama | İkinci dereceden (kökün yakınında) |
| Garantili mi? | Hayır — birbirinden uzaklaşabilir veya döngüye girebilir |
| Kuralı güncelle | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Çözülmüş Örnek:** f(x) = x² − 2 = 0'ı çözerek √2'yi bulun.
- f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (8 ondalık basamağa doğru)
### Sekant Yöntemi
Newton'un yöntemine benzer ancak türevine yaklaşır:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Emlak | Değer |
|----------|----------|
| Yakınsama | Süperdoğrusal (sıra ≈ 1,618, altın oran) |
| Gerektirir | İlk iki tahmin (türev gerekmez) |
### Kök Bulma Yöntemlerinin Karşılaştırılması
| Yöntem | Yakınsama | Türev Gerekli mi? | Garantili mi? | Adım Başına Maliyet |
|----------|----------------|-----------|---------------|---------------|
| İkiye bölme | Doğrusal (1) | Hayır | Evet | 1 fonksiyon değerlendirmesi |
| Newton-Raphson | İkinci Dereceden (2) | Evet | Hayır | 2 fonksiyon değerlendirmesi |
| Sekant | Süper Doğrusal (1,618) | Hayır | Hayır | 1 fonksiyon değerlendirmesi |
| Brent'in yöntemi | Süper Doğrusal | Hayır | Evet | Değişir |
**Brent yöntemi** ikiye bölmeyi (garantili yakınsama) sekant/ters ikinci dereceden enterpolasyonla (hızlı yakınsama) birleştirir. Çoğu sayısal kitaplıkta varsayılan kök bulucudur.
---

## Sayısal Entegrasyon (Dörtlü)
∫ₐᵇ f(x) dx'i yaklaşık olarak hesaplıyoruz.
### Yöntemler
| Yöntem | Formül | Hata | Sipariş |
|----------|------------|----------|-------|
| **Dikdörtgen (orta nokta)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Yamuk** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Simpson'ın 1/3'ü** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpson'ın 3/8'i** | Eşit aralıklı 4 nokta kullanır | O(h⁴) | 4 |
| **Gauss karelemesi** | Optimum düğüm yerleşimi | O(h²ⁿ) | n puan |
### Bileşik Kurallar
h = (b−a)/n genişliğindeki n alt aralık için:
| Kural | Kompozit Formül | Hata |
|----------|-----------|-------|
| Kompozit Trapez | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Bileşik Simpson'ın | h/3[f(a) + 4Σf(tek) + 2Σf(çift) + f(b)] | O(h⁴) |
**Çalışılan Örnek:** n = 4 ile bileşik yamuk kullanarak yaklaşık ∫₀¹ e^(−x²) dx'i hesaplayın.
- h = 0,25, puanlar: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Gerçek değer: ≈ 0,7468 (hata ≈ %0,5)
### Uyarlanabilir Dörtgen
İşlevin hızla değiştiği aralıkları, düzgün olduğu yerlerde daha az nokta kullanarak otomatik olarak alt bölümlere ayırır. `scipy.integrate.quad`'nin kullandığı şey budur (QUADPACK'e dayalıdır).
---

## Enterpolasyon
Bilinen veri noktaları arasındaki değerleri tahmin etme.
### Yöntemler
| Yöntem | Açıklama | Pürüzsüzlük | Salınım |
|----------|----------------|---------------|------------|
| **En yakın komşu** | En yakın veri noktasını kullan | Süreksiz | Yok |
| **Doğrusal** | Noktaları düz çizgilerle bağlayın | C⁰ (sürekli) | Yok |
| **Polinom (Lagrange)** | Tüm noktalardan geçen tek polinom | C^∞ | Birçok noktada şiddetli (Runge fenomeni) |
| **Kübik spline** | Parçalı kübik, bağlantı noktaları pürüzsüz | C² | Asgari |
| **Radyal temel işlevi** | Radyal çekirdeklerin ağırlıklı toplamı | Çekirdeğe bağlıdır | Düşük |
### Lagrange İnterpolasyonu
Verilen n+1 nokta (x₀, y₀), ..., (xₙ, yₙ), tüm noktalardan geçen ≤ n derecesinin benzersiz polinomu:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Runge fenomeni:** Eşit aralıklı noktalarda yüksek dereceli polinom enterpolasyonu, kenarlara yakın yerlerde çılgınca salınım yapabilir. Chebyshev düğümleri veya spline'lar kullanılarak azaltılmıştır.
### Kübik Spline'lar
C² sürekli olan parçalı kübik polinomlar (sürekli ikinci türevler).
| Tür | Sınır Durumu |
|----------------|-----------|
| Doğal spline | S''(x₀) = S''(xₙ) = 0 |
| Kelepçeli spline | S'(x₀) ve S'(xₙ) belirtildi |
| Düğüm değil | x₁ ve xₙ₋₁'de sürekli üçüncü türev |
---

## ODE Çözücüler
Adi diferansiyel denklemlerin dy/dt = f(t, y) sayısal olarak çözülmesi.
### Euler Yöntemi
En basit ODE çözücü.
**Güncelleme:** y_{n+1} = y_n + h · f(t_n, y_n)
| Emlak | Değer |
|----------|----------|
| Sipariş | 1 (adım başına hata: O(h²), genel: O(h)) |
| Kararlılık | Koşullu olarak kararlı (küçük h gereklidir) |
| Maliyet | Adım başına 1 fonksiyon değerlendirmesi |
### Runge-Kutta Yöntemleri
| Yöntem | Sipariş | Aşamalar | Notlar |
|-----------|----------|-----------|-------|
| **Euler** | 1 | 1 | En basit |
| **Orta nokta** | 2 | 2 | Daha iyi doğruluk |
| **Heun'un (RK2)** | 2 | 2 | Tahmin-düzeltici |
| **Klasik RK4** | 4 | 4 | Standart beygir |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Uyarlanabilir adım boyutu (ode45'te kullanılır) |
### Klasik RK4 (4. dereceden Runge-Kutta)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Emlak | Değer |
|----------|----------|
| Sipariş | 4 (genel hata: O(h⁴)) |
| Maliyet | Adım başına 4 fonksiyon değerlendirmesi |
| Kararlılık | Euler'den çok daha iyi |
| Kullanım | Sert olmayan ODE'ler için varsayılan |
### Sert ODE'ler
**Sert** bir ODE'nin çok farklı zaman ölçeklerinde değişen bileşenleri vardır. Açık yöntemler (Euler, RK4), uygulanamayacak kadar küçük adım boyutları gerektirir.
| Yöntem | Tür | Kararlılık |
|----------|----------|-----------|
| Örtülü Euler | Örtülü | A-kararlı (koşulsuz olarak kararlı) |
| Geriye Farklılaşma Formülü (BDF) | Örtülü | A-stabil (5. sıraya kadar) |
| Örtülü Runge-Kutta | Örtülü | L-kararlı çeşitleri mevcuttur |
| LSODA | Otomatik | Sert/sert olmayan arasında geçiş yapar |
---

## Sayısal Kararlılık ve Koşullandırma
### Durum Numarası
**Koşul numarası**, bir problemin çıktısının, girdideki küçük değişikliklere göre ne kadar değiştiğini ölçer.
Doğrusal bir sistem için Ax = b: κ(A) = ||A|| · ||A⁻¹||
| k(A) | Yorumlama |
|----------|---------------|
| ≈ 1 | İyi iklimlendirilmiş |
| 10³ | Hafif derecede hassas |
| 10⁸ | Kötü koşullandırılmış (~8 basamaklı doğruluk kaybı) |
| → ∞ | Tekil (benzersiz çözüm yok) |
### Algoritmaların Kararlılığı
Girdideki küçük bozulmalar çıktıda küçük bozulmalara yol açıyorsa (problemin durum numarasına göre) bir algoritma **sayısal olarak kararlıdır**.
| Algoritma | Stabil? | Notlar |
|-----------|------------|-------|
| Kısmi dönme ile Gauss eliminasyonu | Evet | Standart yaklaşım |
| QR aracılığıyla özdeğerlerin hesaplanması | Evet | Geriye doğru kararlı |
| Basit toplama (önce büyük + küçük) | Hayır | Kahan toplamını kullan |
| Varyansın E[X²] − (E[X])² olarak hesaplanması | Potansiyel olarak hayır | Welford'un çevrimiçi algoritmasını kullanın |
### Welford'un Çevrimiçi Algoritması
Çalışan ortalama ve varyansın sayısal olarak kararlı hesaplanması:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Bu, saf iki geçişli formülde meydana gelen yıkıcı iptali önler.
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Sayısal Yöntem | Başvuru |
|----------------|----------------|
| Kayan nokta (fp16/fp32/bf16) | Karma duyarlıklı eğitim, model nicemleme, bellek verimliliği |
| Kök bulma | Maksimum olabilirlik tahmini (gradyanın = 0 olduğu yeri bulma) |
| Sayısal entegrasyon | Bayes çıkarımı (marjinal olasılıkların hesaplanması), beklenen değerler |
| Enterpolasyon | Yumuşatma, atama, vekil modeller, aktivasyon fonksiyonları |
| ODE çözücüler | Sinirsel ODE'ler, sürekli zamanlı RNN'ler, popülasyon dinamikleri, fizik bilgili ML |
| Durum numarası | Doğrusal regresyon ve normal denklemlerdeki sayısal konuları anlama |
| Kararlı toplama | Kayıp fonksiyonlarının hesaplanması, toplu normalleştirme istatistikleri |
| RK4 / uyarlanabilir çözücüler | Dinamik sistemleri simüle etme, sürekli derinlikli ağları eğitme |
---

## Özet
| Konu | Temel Fikir | Anahtar Yöntemi |
|----------|---------------|-----------|
| Kayan nokta | Sonlu hassas gösterim | IEEE 754, Kahan toplamı |
| Kök bulma | f(x) = 0 | Biseksiyon, Newton-Raphson, Brent'in |
| Sayısal entegrasyon | Yaklaşık ∫f(x)dx | Yamuk, Simpson, Gauss karelemesi |
| Enterpolasyon | Veri noktaları arasındaki tahmin | Kübik eğriler, Lagrange, RBF |
| ODE çözücüler | dy/dt = f(t,y)'yi çözün | Euler, RK4, uyarlanabilir yöntemler |
| Kararlılık | Yuvarlama hatalarına duyarlılık | Koşul numarası, kararlı algoritmalar |
Sayısal yöntemler matematiğin gerçeklikle buluştuğu yerdir. Hiçbir bilgisayar gerçek sayıların çoğunu tam olarak temsil edemez, pratikte hiçbir türev sembolik olarak hesaplanmaz ve gerçek dünya problemleri için hiçbir integral kapalı biçimde değerlendirilmez. Sayısal yöntemleri anlamak, doğru algoritmayı seçmenize, doğruluğunu tahmin etmenize ve sonlu duyarlıklı aritmetikten kaynaklanan ince hatalardan kaçınmanıza olanak tanır.