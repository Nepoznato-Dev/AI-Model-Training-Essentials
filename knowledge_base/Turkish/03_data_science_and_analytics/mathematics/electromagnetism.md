<!--
---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Elektromanyetizma
Elektromanyetizma, elektrik ve manyetik alanların ve bunların etkileşimlerinin incelenmesidir. 1860'larda Maxwell tarafından birleştirilen elektromanyetizma, ışığı, elektriği, manyetizmayı, radyo dalgalarını ve atomların yapısını açıklar. Matematiksel olarak tam olarak anlaşılan ilk temel kuvvetti ve denklemleri Einstein'ın özel görelilik ve modern alan teorisine ilham kaynağı oldu.
---

## Elektrik Alanları
### Coulomb Yasası
r mesafesiyle ayrılmış iki nokta yükü q₁ ve q₂ arasındaki kuvvet:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Sabit | Değer |
|----------|----------|
| ε₀ (boş alanın geçirgenliği) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (Coulomb sabiti k) | 8,988 × 10⁹ N·m²/C² |
### Elektrik Alanı Tanımı
**E** = **F**/q (birim yük başına kuvvet)
Bir Q nokta yükü için: **E** = (1/4πε₀) · (Q/r²) · r̂
### Elektrik Alan Hatları
| Emlak | Kural |
|----------|------|
| Yön | Pozitif yüklerden uzağa, negatife doğru işaret edin |
| Yoğunluk | Daha yakın çizgiler = daha güçlü alan |
| Geçiş | Alan çizgileri asla kesişmez |
| İletkenler | Çizgiler yüzeyle dik olarak buluşuyor |
### Elektrik Potansiyeli (Gerilim)
V = −∫ **E** · d**l** (potansiyel fark, E'nin negatif çizgi integralidir)
**E** = −∇V (alan, potansiyelin negatif eğimidir)
Bir nokta yük için: V = (1/4πε₀) · Q/r
| Konsept | Formül | Birim |
|-----------|-----------|------|
| Potansiyel enerji | U = qV | Joule |
| Elektron-volt | 1 eV = 1,602 × 10⁻¹⁹ J | Enerji ünitesi |
| Eş potansiyel yüzey | V'nin sabit olduğu yüzey | E ona dik |
---

## Gauss Yasası
### İfade
Herhangi bir kapalı yüzeyden geçen toplam elektrik akısı, kapalı yükün ε₀'ye bölünmesine eşittir:
∮ **E** · d**A** = Q_enc / ε₀
Diferansiyel formda: ∇ · **E** = ρ/ε₀
### Gauss Yasasını Kullanmak
Gauss yasası en çok simetrinin E'nin integralden çıkarılmasına izin verdiği durumlarda kullanışlıdır.
| Simetri | Gauss Yüzeyi | Sonuç |
|----------|----------|----------|
| Küresel | Küre | E = Q/(4πε₀r²) dış |
| Silindirik (hat şarjı) | Silindir | E = λ/(2πε₀r) |
| Düzlemsel (sonsuz sayfa) | İlaç Kutusu | E = σ/(2ε₀) |
| Paralel plakalar arasında | İlaç Kutusu | E = σ/ε₀ |
---

## İletkenler ve Kondansatörler
### Elektrostatik Dengede İletkenler
| Emlak | Açıklama |
|----------|----------------|
| E = 0 içeride | Dahili alanı iptal etmek için ücretler yeniden düzenlendi |
| Tüm yük yüzeyde | İç mekanda net ücret yok |
| E yüzeye dik | Teğetsel bileşen yok (aksi takdirde yükler hareket eder) |
| Boyunca eşpotansiyel | İçeride ve yüzeyde her yerde aynı V |
### Kapasitörler
**kapasitör** enerjiyi iki iletken arasındaki elektrik alanında depolar.
| Yapılandırma | Kapasite |
|----------------|------------|
| Paralel plakalar | C = ε₀A/d |
| Silindirik | C = 2πε₀L / ln(b/a) |
| Küresel | C = 4πε₀ab / (b−a) |
| Formül | İfade |
|-----------|------------|
| Şarj voltajı | S = CV |
| Depolanan enerji | U = ½CV² = ½Q²/C |
| Enerji yoğunluğu | u = ½ε₀E² |
| Seri kombinasyonu | 1/C_toplam = 1/C₁ + 1/C₂ + ... |
| Paralel kombinasyon | C_toplam = C₁ + C₂ + ... |
### Dielektrikler
Sabit κ'ye sahip bir dielektrik (yalıtım malzemesi) eklemek kapasitansı artırır: C = κC₀.
---

## Manyetik Alanlar
### Manyetik Kuvvet
**F** = q(**v** × **B**) (Lorentz kuvveti, manyetik bileşen)
| Emlak | Açıklama |
|----------|-----------|
| Yön | Hem v hem de B'ye dik (sağ el kuralı) |
| Yapılan iş | Sıfır (kuvvet hıza diktir) |
| Dairesel hareket | Tek tip B alanında yarıçap r = mv/(qB) |
### Biot-Savart Yasası
Küçük bir akım elemanından kaynaklanan manyetik alan:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Sabit | Değer |
|----------|----------|
| μ₀ (boş alanın geçirgenliği) | 4π × 10⁻⁷ T·m/A |
### Ampere Yasası
∮ **B** · d**l** = μ₀I_enc
Diferansiyel formda: ∇ × **B** = μ₀**J**
**Uygulamalar:**
| Yapılandırma | B alanı |
|----------------|-----------|
| Uzun düz tel | B = μ₀I/(2πr) |
| Solenoid (iç) | B = μ₀nI |
| Toroid (içeride) | B = μ₀NI/(2πr) |
---

## Elektromanyetik İndüksiyon
### Faraday Yasası
Değişen bir manyetik akı, bir elektromotor kuvveti (EMF) indükler:
EMF = −dΦ_B/dt
burada Φ_B = ∫ **B** · d**A** manyetik akıdır.
Diferansiyel formda: ∇ × **E** = −∂**B**/∂t
**Lenz yasası:** İndüklenen EMF, akıştaki değişime karşıdır (eksi işareti).
### İndüksiyon Uygulamaları
| Başvuru | Prensip |
|---------------|-----------|
| Jeneratör | B alanında dönen bobin → alternatif EMF |
| Trafo | Birincilde akımın değiştirilmesi → İkincilde EMF |
| İndüktör | Akımdaki değişikliklere karşı çıkar: EMF = −L(dI/dt) |
| Girdap akımları | Yığın iletkenlerde indüklenen akımlar (frenleme, ısıtma) |
### İndüktörler
| Formül | İfade |
|-----------|------------|
| Akı bağlantısı | Φ = LI |
| Depolanan enerji | U = ½LI² |
| Seri kombinasyonu | L_toplam = L₁ + L₂ + ... |
| Paralel kombinasyon | 1/L_toplam = 1/L₁ + 1/L₂ + ... |
---

## Maxwell Denklemleri
Maxwell denklemleri elektrik ve manyetizmayı tek bir teoride birleştiriyor.
### İntegral Formda
| Denklem | İsim | Açıklama |
|----------|----------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Gauss yasası (elektrik) | Elektrik akısı = kapalı yük |
| ∮ **B** · d**A** = 0 | Gauss yasası (manyetik) | Manyetik tek kutup yok |
| ∮ **E** · d**l** = −dΦ_B/dt | Faraday yasası | B'yi değiştirmek E'yi tetikler |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Amper-Maxwell yasası | Güncel ve değişen E, B'yi üretir |
### Diferansiyel Formda
| Denklem | İsim | İfade |
|----------|------|------------|
| Gauss (elektrik) | ∇ · **E** = ρ/ε₀ |
| Gauss (manyetik) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Amper-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### Yer Değiştirme Akımı
Maxwell'in önemli eklemesi: μ₀ε₀ ∂**E**/∂t (yer değiştirme akımı) terimi. Bu, şarjın korunmasını sağlar ve elektromanyetik dalgaları tahmin eder.
---

## Elektromanyetik Dalgalar
Vakumda (yük yok, akım yok), Maxwell denklemleri dalga denklemlerini verir:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Işık hızı:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### EM Dalgalarının Özellikleri
| Emlak | Açıklama |
|----------|----------------|
| Enine | E ve B birbirlerine ve yayılma yönüne diktir |
| Aşamada | E ve B aynı anda maksimuma ulaşıyor |
| Büyüklük oranı | E = cB |
| Enerji akışı | S = (1/μ₀)**E** × **B** (Poynting vektörü) |
| Yoğunluk | ben = ⟨S⟩ = E₀²/(2μ₀c) |
### Elektromanyetik Spektrum
| Tür | Dalgaboyu | Frekans | Kaynak |
|------|-----------|-----------|-----------|
| Radyo | > 1 m | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30 EHz | Nükleer süreçler |
---

## AC Devreleri
### RLC Devre Bileşenleri
| Bileşen | Gerilim-Akım İlişkisi | Empedans |
|-----------|----------------|-----------|
| Direnç (R) | V = IR | Z_R = R |
| İndüktör (L) | V = L(dI/dt) | Z_L = jωL |
| Kondansatör (C) | ben = C(dV/dt) | Z_C = 1/(jωC) |
### Empedans ve Rezonans
Toplam empedans (RLC serisi): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Rezonans:** ωL = 1/ωC → ω₀ = 1/√(LC) olduğunda
- Rezonansta: empedans minimumdur (= R), akım maksimumdur
- **Kalite faktörü:** Q = ω₀L/R (rezonansın keskinliği)
### AC Devrelerinde Güç
| Miktar | Formül |
|----------|-----------|
| Ortalama güç | P_ortalama = V_rms · I_rms · cos φ |
| Güç faktörü | çünkü φ = R/\|Z\| |
| RMS gerilimi | V_rms = V₀/√2 |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| EM Konsepti | Başvuru |
|-----------|----------------|
| Maxwell denklemleri | Fizik bilgili sinir ağları, hesaplamalı elektromanyetik |
| Dalga denklemi | Sinyal işlemenin temeli, Fourier analizi motivasyonu |
| Elektromanyetik spektrum | Sensör verileri (kızılötesi kameralar, radar, uydu görüntüleri) |
| AC devreleri / empedans | Makine öğrenimini çalıştıran donanımı anlama (güç kaynakları, sinyal bütünlüğü) |
| Poynting vektör | Kablosuz iletişimde enerji akışı (IoT/edge ML ile ilgili) |
| Gauss yasası | Akışkanlar dinamiği simülasyonlarında kullanılan vektör hesabındaki sapmaya benzer |
| Kapasitörler/indüktörler | Sinir ağları için analog hesaplama, nöromorfik donanım |
| Rezonans | Filtre tasarımı, frekans alanı analizi, spektral yöntemler |
| Sınır değer problemleri | Sonlu elemanlar yöntemleri, ağ tabanlı simülasyonlar |
| Vektör hesabı (∇·, ∇×) | ML teorisi boyunca kullanılan temel matematiksel araçlar |
---

## Özet
| Hukuk | Ne Diyor | Diferansiyel Formu |
|-----|-------------|--------|
| Gauss (elektrik) | Yükler elektrik alanında sapma yaratır | ∇ · E = ρ/ε₀ |
| Gauss (manyetik) | Manyetik tek kutup yok | ∇ · B = 0 |
| Faraday | B'yi değiştirmek E kıvırmayı oluşturur | ∇ × E = −∂B/∂t |
| Amper-Maxwell | Mevcut ve değişen E, kıvrılma B'yi oluşturur | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
Elektromanyetizma şimdiye kadar oluşturulmuş en eksiksiz ve en iyi şekilde test edilmiş fiziksel teoridir. Sadece dört denklemi, statik elektrikten ışığa ve şimdiye kadar yapılmış her elektronik cihazın davranışına kadar her şeyi açıklıyor. Veri bilimcileri için elektromanyetizmayı anlamak, dalga olayları, vektör hesabı ve tüm modern bilgi işlem donanımlarının temelini oluşturan fizik için derin bir sezgi sağlar.