<!--
---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
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
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Optik ve Dalgalar
Dalgalar her yerdedir: ses, ışık, su, radyo sinyalleri, kuantum olasılık genlikleri, borsa dalgalanmaları ve sinir ağı aktivasyonlarının titreşimleri. Optik - ışığın incelenmesi - en gelişmiş dalga bilimidir ve matematiksel araçları (Fourier analizi, girişim, kırınım) her dalga olgusuna uygulanır. Dalgaları anlamak, sinyal işleme, görüntü analizi, iletişim ve tüm modern teknolojinin fiziksel katmanı için gereklidir.
---

## Dalga Denklemi
### Genel Dalga Denklemi
Tek boyutlu dalga denklemi:
∂²u/∂t² = c² ∂²u/∂x²
burada u(x,t) dalga yer değiştirmesidir ve c dalga hızıdır.
### Genel Çözüm (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
burada f sağa doğru ilerleyen bir dalgadır ve g sola doğru ilerleyen bir dalgadır.
### Anahtar Dalga Parametreleri
| Parametre | Sembol | Birim | Açıklama |
|-----------|-----------|------|-------------|
| Genlik | bir | değişir | Maksimum yer değiştirme |
| Dalgaboyu | λ | metre | Ardışık tepeler arasındaki mesafe |
| Frekans | f veya ν | Hertz (Hz) | Saniye başına döngü |
| Dönem | T = 1/f | saniye | Bir tam döngü süresi |
| Dalga numarası | k = 2π/λ | rad/m | Uzamsal frekans |
| Açısal frekans | ω = 2πf | rad/s | Zamansal frekans |
| Dalga hızı | c = fλ = ω/k | m/sn | Yayılma hızı |
### Sinüzoidal Dalga
u(x,t) = A sin(kx − ωt + φ)
burada φ faz sabitidir.
### Farklı Ortamlarda Dalga Hızı
| Dalga Tipi | Orta | Hız Formülü |
|-----------|-----------|---------------|
| Dize | Gerilim T, doğrusal yoğunluk μ | c = √(T/μ) |
| Ses | Yığın modülü B, yoğunluk ρ | c = √(B/ρ) |
| Ses (ideal gaz) | γ, R, T, M | c = √(γRT/M) |
| EM dalgası | Geçirgenlik ε, geçirgenlik μ | c = 1/√(με) |
| EM dalgası (vakum) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Süperpozisyon ve Girişim
### Süperpozisyon Prensibi
İki veya daha fazla dalga örtüştüğünde ortaya çıkan yer değiştirme, bireysel yer değiştirmelerin toplamıdır:
u_toplam = u₁ + u₂ + ... + uₙ
Bu doğrusal dalga denklemleri için geçerlidir.
### İki Dalganın Girişimi
Aynı frekans ve genliğe sahip iki dalga, faz farkı Δφ:
u_toplam = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Faz Farkı | Sonuç | Yoğunluk |
|----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Yapıcı** (genlik = 2A) | 4I₀ (maksimum) |
| Δφ = π, 3π, 5π, ... | **Yıkıcı** (genlik = 0) | 0 (minimum) |
| Δφ = π/2 | Kısmi | 2I₀ |
### Parazit Koşulları
| Durum | Tür | Yol Farkı |
|-----------|----------|------|
| Yapıcı | Parlak saçak | ΔL = mλ (m = 0, 1, 2, ...) |
| Yıkıcı | Koyu saçak | ΔL = (m + ½)λ |
---

## Young'ın Çift Yarık Deneyi
Işık, d mesafesi kadar ayrılmış iki dar yarıktan geçerek, L mesafesindeki bir ekranda bir girişim deseni oluşturur.
### Kenar Pozisyonları
| saçak | Ekrandaki Konumu |
|----------|-----------|
| Parlak (maxima) | y_m = mλL/d |
| Koyu (minimum) | y_m = (m + ½)λL/d |
| Saçak aralığı | Δy = λL/d |
Bu deney ışığın dalga doğasını kanıtladı (Thomas Young, 1801) ve daha sonra kuantum mekaniğinin (dalga-parçacık ikiliği) merkezi haline geldi.
---

## Kırınım
**Kırınım**, dalgaların engeller etrafında ve açıklıklar boyunca bükülmesi ve yayılmasıdır.
### Tek Yarık Kırınım
Genişlikteki bir yarıktan geçen ışık, parlak ve karanlık saçaklardan oluşan bir desen oluşturur.
| Özellik | Durum |
|-----------|-----------|
| Merkezi maksimum | En geniş ve en parlak; genişlik = 2λL/a |
| Minima (koyu saçaklar) | a sin θ = mλ (m = ±1, ±2, ...) |
| İkincil maksimumlar | Yaklaşık olarak minimumlar arasında; çok daha sönük |
### Kırınım Izgarası
N eşit aralıklı yarık (d aralığı) çok keskin maksimumlar üretir:
d sin θ = mλ (m = 0, 1, 2, ...)
| Emlak | Efekt |
|----------|-----------|
| Daha fazla yarık (daha büyük N) | Daha keskin, daha parlak maksimum |
| Çözümleme gücü | R = mN (yakın dalga boylarını ayırt edebilir) |
| Uygulamalar | Spektroskopi, dalga boyu ölçümü |
### Rayleigh Kriteri (Çözünürlük Sınırı)
İki nokta kaynağı, birinin merkezi maksimumu diğerinin ilk minimumuna denk geldiğinde çözülebilir:
θ_min = 1,22 λ/D
burada D açıklık çapıdır.
| Sistem | λ | D | θ_dak |
|-----------|---|---|-------|
| İnsan gözü | 550nm | 5mm | 1,3 × 10⁻⁴ radyal (~0,01°) |
| Hubble Uzay Teleskobu | 550nm | 2,4 m | 2,8 × 10⁻⁷ ışın |
| Radyo teleskop (Arecibo) | 21 cm | 305 m | 8,4 × 10⁻⁴ rad |
---

## Polarizasyon
**Polarizasyon**, enine bir dalgadaki elektrik alanı salınımının yönünü tanımlar.
### Polarizasyon Türleri
| Tür | Açıklama |
|------|-----------------|
| **Doğrusal** | E sabit bir düzlemde salınır |
| **Dairesel** | E bir daire içinde döner (sağ veya sol elle) |
| **Eliptik** | E bir elips çizer (en genel) |
| **Polarize edilmemiş** | Tüm polarizasyonların rastgele karışımı (en doğal ışık) |
### Malus Yasası
Polarize ışık bir polarizörden polarizasyon yönüne θ açısıyla geçtiğinde:
ben = I₀ cos²θ
| Açı θ | İletilen Yoğunluk |
|-----------|------------|
| 0° | %100 (I₀) |
| 30° | %75 |
| 45° | %50 |
| 60° | %25 |
| 90° | %0 (tamamen engellendi) |
### Yansımayla Polarizasyon (Brewster Açısı)
Brewster açısından yansıyan ışık tamamen polarizedir:
tan θ_B = n₂/n₁
| Arayüz | n₁ | n₂ | θ_B |
|-----------|----|----|-----|
| Hava → cam | 1.0 | 1.5 | 56,3° |
| Hava → su | 1.0 | 1.33 | 53,1° |
| Cam → elmas | 1.5 | 2.42 | 58,1° |
---

## Geometrik Optik
Geometrik (ışın) optik, ışığı düz çizgiler halinde ilerleyen, arayüzeylerde bükülen ışınlar olarak ele alır.
### Snell Yasası (Kırılma)
n₁ sin θ₁ = n₂ sin θ₂
| Malzeme | Kırılma İndeksi n |
|----------|-----------|
| Vakum | 1.000 |
| Hava | 1.0003 |
| Su | 1.33 |
| Cam (taç) | 1.52 |
| Cam (çakmaktaşı) | 1.62 |
| Elmas | 2.42 |
### Toplam İç Yansıma
Işık, **kritik açının** ötesinde, çok yoğun ortamdan az yoğun ortama doğru gittiğinde:
θ_c = arcsin(n₂/n₁)
Tüm ışık yansıtılır; optik fiberler bu şekilde çalışır.
### İnce Mercek Denklemi
1/f = 1/d_o + 1/d_i
| Miktar | Anlamı |
|----------|-----------|
| f | Odak uzaklığı |
| d_o | Nesne mesafesi |
| d_i | Görüntü mesafesi |
| M = −d_i/d_o | Büyütme |
| Objektif Tipi | f | Resim |
|-----------|---|-------|
| Yakınsak (dışbükey) | Olumlu | Gerçek (d_o > f ise) veya sanal |
| Uzaklaşan (içbükey) | Negatif | Her zaman sanal, dik, azaltılmış |
### Ayna Denklemi
Mercek denklemiyle aynı formdadır: 1/f = 1/d_o + 1/d_i, burada küresel aynalar için f = R/2.
---

## Fourier Optik
Fourier optiği, görüntüleme ve kırınım işlemlerini Fourier dönüşümü işlemleri olarak ele alır.
### Temel Prensip
Bir açıklığın uzak alan kırınım modeli, açıklık fonksiyonunun **Fourier dönüşümü**'dür.
| Diyafram | Kırınım Deseni (Fourier Dönüşümü) |
|----------|------------------------------------------|
| Tek yarık | beri işlevi |
| Dairesel açıklık | Havadar disk (J₁(r)/r) |
| Dikdörtgen açıklık | 2D'den beri |
| Izgara | Ayrık delta fonksiyonları |
### Optik Fourier Dönüşümü
Bir mercek 2D Fourier dönüşümü gerçekleştirir: Bir nesneyi ön odak düzlemine yerleştirmek, arka odak düzleminde Fourier dönüşümünü üretir.
### Uygulamalar
| Başvuru | Fourier Optics Nasıl Yardımcı Olur |
|------------|--------------|
| Görüntü filtreleme | Uzamsal frekansları engellemek/geçirmek için maskeleri Fourier düzlemine yerleştirin |
| Kenar algılama | Fourier düzleminde yüksek geçişli filtreleme |
| Desen tanıma | Fourier dönüşümleri aracılığıyla korelasyon |
| Holografi | Dalga cephelerini kaydetme ve yeniden oluşturma |
| Optik bilgi işlem | Fourier dönüşümlerini ışık hızında gerçekleştirme |
---

## Ses ve Akustik
### Ses Dalgası Özellikleri
| Emlak | Tipik Aralık | Birim |
|----------|-----------------|------|
| Frekans | 20 − 20.000 (insan işitmesi) | Hz |
| Hız (hava, 20°C) | 343 | m/sn |
| Hız (su) | 1.480 | m/sn |
| Hız (çelik) | 5.960 | m/sn |
| Yoğunluk eşiği | 10⁻¹² | W/m² |
### Desibel Ölçeği
β = 10 log₁₀(I/I₀) dB, burada I₀ = 10⁻¹² W/m²
| Ses | Yoğunluk (W/m²) | Seviye (dB) |
|----------|-----------|------------|
| İşitme eşiği | 10⁻¹² | 0 |
| Hışırdayan yapraklar | 10⁻¹¹ | 10 |
| Normal konuşma | 10⁻⁶ | 60 |
| Rock konseri | 1 | 120 |
| Acı eşiği | 10 | 130 |
| Jet motoru | 100 | 140 |
### Doppler Etkisi
Kaynak ve gözlemci birbirine göre hareket ettiğinde gözlemlenen frekans:
f' = f(v ± v_o)/(v ∓ v_s)
| Senaryo | Efekt |
|----------|-----------|
| Kaynak yaklaşıyor | Daha yüksek frekans (ışık için maviye kayma) |
| Kaynak uzaklaşıyor | Daha düşük frekans (ışık için kırmızıya kayma) |
| Uygulamalar | Radar, tıbbi ultrason, astronomi (galaksilerin kırmızıya kayması) |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Dalga/Optik Konsepti | Başvuru |
|---------------------|----------------|
| Dalga denklemi | Fizik bilgili sinir ağları, sismik veri analizi, ses işleme |
| Fourier analizi | Sinyal işlemenin temeli, spektral analiz, özellik çıkarma |
| Fourier dönüşümü | CNN'ler dolaylı olarak yerel Fourier analizini gerçekleştirir; Veri ön işlemede kullanılan FFT |
| Girişim | Analog hesaplama, optik sinir ağları |
| Kırınım | Görüntü oluşturma modelleri, bulanıklık giderme algoritmaları, hesaplamalı fotoğrafçılık |
| Polarizasyon | Uzaktan algılama, malzeme sınıflandırması, uydu görüntüleri analizi |
| Geometrik optik | Sentetik veri üretimi için bilgisayarlı görüntü ve ışın izlemede kamera modelleri |
| Mercek denklemi | Kamera kalibrasyonu, derinlik tahmini, 3 boyutlu yeniden yapılandırma |
| Fourier optiği | Optik hesaplama, kırınımlı derin sinir ağları (D²NN) |
| Doppler etkisi | Radar sinyal işleme, tıbbi görüntüleme (Doppler ultrason), hız tahmini |
| Desibel ölçeği | Ses özelliği mühendisliği, konuşma tanıma ön işleme |
| Örnekleme teorisi | Nyquist-Shannon teoremi dalga teorisini dijital sinyal işlemeye bağlar |
---

## Özet
| Konu | Temel Fikir | Anahtar Denklem |
|----------|-----------|------------|
| Dalga denklemi | Dalgalar c hızıyla yayılır | ∂²u/∂t² = c²∂²u/∂x² |
| Süperpozisyon | Dalgalar doğrusal olarak eklenir | u = u₁ + u₂ |
| Girişim | Aşama takviyeyi belirler | Δφ = 2πΔL/λ |
| Kırınım | Dalgalar engellerin etrafından bükülür | a sin θ = mλ (tek yarık) |
| Polarizasyon | Salınım yönü | Malus yasası: I = I₀cos²θ |
| Geometrik optik | Işınlar kadar ışık | Snell yasası: n₁sinθ₁ = n₂sinθ₂ |
| Fourier optiği | Fourier dönüşümü olarak görüntüleme | Uzak alan = FT açıklığı |
| Doppler etkisi | Hareketten kaynaklanan frekans kayması | f' = f(v ± v_o)/(v ∓ v_s) |
Dalgalar, salınan sistemlerin evrensel dilidir. İster ses sinyallerini işliyor, ister zaman serilerini analiz ediyor, görüntü tanıma sistemleri tasarlıyor veya fizik simülasyonları oluşturuyor olun, dalgaların matematiği (süperpozisyon, Fourier analizi, girişim, kırınım) temel araç setini sağlar. Optik, en olgun dalga bilimi olarak, modern veri bilimine nüfuz eden hem teorik temeli hem de pratik teknikleri sunar.