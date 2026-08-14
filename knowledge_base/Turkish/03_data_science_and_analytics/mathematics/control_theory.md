---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Kontrol Teorisi
Kontrol teorisi, sistemlerin sizin istediğiniz şekilde davranmasını sağlamanın matematiğidir. Termostatlardan otopilotlara, robot kollardan kimyasal reaktörlere kadar kontrol sistemleri istenen davranışı algılar, karar verir ve harekete geçer. Bu alan; takviyeli öğrenmeye, hiper parametre ayarlamaya ve uyarlanabilir sistemlere taşınan kavramlar olan kararlılığı, performansı ve sağlamlığı analiz etmek için titiz araçlar sağlar.
---

## Temel Kavramlar
### Açık Döngü ve Kapalı Döngü
| Tür | Açıklama | Örnek | Avantajı |
|------|-------------|--------|-----------|
| **Açık döngü** | Çıkıştan bağımsız kontrol eylemi | Çamaşır makinesi zamanlayıcısı | Basit, sensöre gerek yok |
| **Kapalı döngü (geri bildirim)** | Kontrol eylemi çıktıya bağlıdır | Termostat, hız sabitleyici | Rahatsızlıkları reddeder, sağlam |
### Blok Diyagram Elemanları
| Eleman | Sembol | İşlev |
|-----------|-----------|----------|
| **Bitki** | G(ler) | Kontrol edilen sistem |
| **Denetleyici** | C(ler) | Kontrol eylemini hesaplar |
| **Sensör** | H(ler) | Çıkışı ölçer |
| **Toplama kavşağı** | ⊕ | Hesaplama hatası: r − y |
| **Referans** | r(t) | İstenilen çıktı |
| **Hata** | e(t) = r(t) − y(t) | İstenilen ve gerçek arasındaki fark |
| **Rahatsızlık** | d(t) | Tesisi etkileyen istenmeyen girdiler |
### Kapalı Döngü Transfer Fonksiyonu
Standart bir negatif geri bildirim sistemi için:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Miktar | Formül |
|----------|-----------|
| Açık döngü aktarım işlevi | L(s) = C(s)G(s)H(s) |
| Kapalı döngü aktarım işlevi | T(ler) = L(ler)/H(ler) / (1 + L(ler)) |
| Hata aktarma işlevi | E(ler)/R(ler) = 1 / (1 + L(ler)) |
| Hassasiyet | S(ler) = 1 / (1 + L(ler)) |
---

## Aktarım İşlevleri
Bir **transfer fonksiyonu** H(s) = Y(s)/X(s), Laplace alanındaki doğrusal zamanla değişmeyen (LTI) bir sistemin giriş-çıkış ilişkisini tanımlar.
### Standart Formlar
| Sistem | Aktarım İşlevi | Parametreler |
|----------|-----------|------------|
| **Birinci dereceden** | K/(τs + 1) | K = kazanç, τ = zaman sabiti |
| **İkinci dereceden** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = doğal frekans, ζ = sönümleme oranı |
| **Entegratör** | K/s | — |
| **Farklılaştırıcı** | K | — |
| **Gecikme** | e^{−sT_d} | T_d = zaman gecikmesi |
### İkinci Dereceden Sistem Davranışı
| Sönümleme Oranı ζ | Davranış | Kutup Konumları |
|----------------|---------------|---------------|
| ζ = 0 | Sönümsüz salınım | Saf hayali |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Aşırı sönümlü (yavaş, salınım yok) | Gerçek, farklı |
### Performans Metrikleri (Adım Yanıtı)
| Metrik | Formül (2. dereceden, az sönümlü) | Açıklama |
|----------|--------------------------|------------|
| Yükseliş zamanı (t_r) | ≈ 1,8/ωₙ | %10'dan %90'a çıkma zamanı |
| Yoğun zaman (t_p) | π/(ωₙ√(1−ζ²)) | İlk maksimuma ulaşma süresi |
| Aşım (M_p) | e^{−πζ/√(1−ζ²)} × %100 | Nihai değerin üzerindeki maksimum tepe |
| Yerleşme süresi (t_s) | ≈ 4/(ζωₙ) | Finalin %2'si dahilinde kalma süresi |
| Kararlı durum hatası | Sistem türüne bağlıdır | İstenilen ile gerçek arasındaki fark şu şekildedir: t → ∞ |
---

## PID Kontrolörleri
**PID denetleyici** endüstride en yaygın kullanılan denetleyicidir (endüstriyel denetleyicilerin %90'ından fazlası).
### PID Formülü
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
Laplace alanında: C(s) = K_p + K_i/s + K_d s
| Dönem | Efekt | Çok Fazla | Çok Az |
|------|--------|----------|------------|
| **Orantılı (K_p)** | Mevcut hataya tepki verir | Salınım, kararsızlık | Yavaş yanıt, büyük hata |
| **İntegral (K_i)** | Kararlı durum hatasını ortadan kaldırır | Aşım, salınım | Kalıcı ofset |
| **Türev (K_d)** | Gelecekteki hatayı tahmin eder (sönümleme) | Gürültü amplifikasyonu | Yetersiz rahatsızlık reddi |
### PID Ayarlama Yöntemleri
| Yöntem | Yaklaşım |
|----------|----------|
| **Ziegler-Nichols** | Salınıma kadar K_u'yu artırın; kazançları ayarlamak için K_u ve P_u periyodunu kullanın |
| **Cohen-Coon** | Adım yanıtı parametrelerine dayalıdır (kazanç, zaman sabiti, ölü zaman) |
| **IMC (Dahili Model Kontrolü)** | Süreç modeline göre; iyi sağlamlık sağlar |
| **Otomatik ayarlama** | Çevrimiçi tanımlama + ayarlama (birçok modern denetleyici) |
| **Kılavuz** | Yalnızca K_p ile başlayın, ofseti kaldırmak için K_i ekleyin, sönümleme için K_d ekleyin |
### Ziegler-Nichols Kuralları
1. K_i = K_d = 0 olarak ayarlayın
2. Sürekli salınım gerçekleşene kadar K_p'yi artırın: nihai kazanç K_u, periyot P_u
3. Kazanımları ayarlayın:
| Denetleyici | K_p | K_i | K_d |
|-----------|-----|-----|-----|
| P | 0.5K_u | — | — |
| PI | 0.45K_u | 1.2K_u/P_u | — |
| PID | 0.6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Kararlılık Analizi
Bir sistem, çıkışı sınırlı girdiler için sınırlı kalıyorsa (BIBO kararlılığı) **kararlıdır**.
### Kutup Tabanlı Stabilite
| Durum | Kararlılık |
|-----------|---------------|
| Tüm kutuplar sol yarım düzlemde (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Kararsız |
| Hayali eksendeki kutuplar (Re(s) = 0) | Marjinal olarak kararlı (veya tekrarlanan durumlarda kararsız) |
### Routh-Hurwitz Kriteri
Kutupları açıkça hesaplamadan kararlılığı belirler. Karakteristik polinom katsayılarından Routh dizisini oluşturur.
**Kural:** İlk sütundaki işaret değişikliklerinin sayısı, sağ yarım düzlemdeki kutupların sayısına eşittir.
### Nyquist Stabilite Kriteri
Açık döngü frekans tepkisini L(jω) karmaşık düzlemde çizer.
**Kural:** Nyquist grafiği, (−1, 0) noktasını saat yönünün tersine, açık döngüdeki kararsız kutupların sayısına eşit sayıda çevreliyorsa, kapalı döngü sistemi kararlıdır.
**Kazanç marjı:** Kararsızlıktan önce ne kadar kazanç artabilir (gerçek eksende olay örgüsünden −1'e olan mesafe).
**Faz marjı:** Kararsızlıktan önce ne kadar faz gecikmesi artabilir (kazanç geçişinde çizimden birim daireye açı).
### Bode Grafiği Analizi
Kazanç (dB) ve faz (derece) ile frekansın (log ölçeği) grafiğini çizer.
| Metrik | Tanımı | İstenilen Değer |
|----------|---------------|---------------|
| **Kazanç marjı (GM)** | Faz = −180° |'de 0 dB'ye ulaşacak şekilde kazanç artışı > 6 dB |
| **Faz marjı (PM)** | Kazanç geçişinde faz (0 dB) + 180° | > 45° |
| **Geçiş elde edin** | Kazanç = 0 dB | — |
| **Faz geçişi** | Faz = −180° | — |
---

## Durum-Uzay Temsili
Çok girişli çok çıkışlı (MIMO) sistemler için durum uzayı formu, transfer fonksiyonlarından daha doğaldır.
### Standart Form
ẋ(t) = Ax(t) + Bu(t) (durum denklemi)
y(t) = Cx(t) + Du(t) (çıktı denklemi)
| Matris | İsim | Boyutlar |
|----------|----------|-----------|
| bir | Sistem/durum matrisi | n × n |
| B | Giriş matrisi | n × m |
| C | Çıkış matrisi | p × n |
| D | Geçiş matrisi | p × m |
### Durum Uzayından Transfer Fonksiyonu
G(s) = C(sI − A)⁻¹B + D
### Kontrol Edilebilirlik ve Gözlemlenebilirlik
| Emlak | Testi | Anlamı |
|----------|------|-----------|
| **Kontrol edilebilir** | Sıra[C_B] = n (burada C_B = [B, AB, A²B, ...]) | Herhangi bir duruma yönlendirilebilir |
| **Gözlemlenebilir** | Sıra[O_B] = n (burada O_B = [C; CA; CA²; ...]) | Çıkıştan durumu belirleyebilir |
Bir sistemin geri bildirimle kararlı hale getirilebilmesi için kontrol edilebilir olması ve durum tahmini için gözlemlenebilir olması gerekir.
### Durum Geri Bildirimi
u = −Kx + r (tam durum geri beslemesi)
Kapalı döngü: ẋ = (A − BK)x + Br
**Kutup yerleşimi:** A − BK'nin istenen özdeğerlere (kutuplara) sahip olmasını sağlayacak şekilde K'yi seçin.
---

## Optimum Kontrol
### Doğrusal Karesel Regülatör (LQR)
Minimize etme: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
burada Q ≥ 0 (durum maliyeti) ve R > 0 (kontrol maliyeti).
**Çözüm:** u = −Kx burada K = R⁻¹BᵀP ve P, **cebirsel Riccati denklemini çözer:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Ayarlama | Efekt |
|----------|-----------|
| Q'yu Artır | Daha hızlı yanıt, daha fazla kontrol çabası |
| R'yi Artırın | Daha yavaş yanıt, daha az kontrol çabası |
| S ≫ R | Agresif kontrol (yüksek K_p gibi) |
### Kalman Filtresi
Gauss gürültülü doğrusal sistemler için en uygun durum tahmincisi.
**Sistem modeli:**
ẋ = Ax + Bu + w (işlem gürültüsü w ~ N(0, Q))
y = Cx + v (ölçüm gürültüsü v ~ N(0, R))
**Kalman filtre denklemleri:**
- Tahmin: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Güncelleme: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
Kalman filtresi LQR ikilisidir; tahmin hatası varyansını en aza indirir.
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Kontrol Teorisi Kavramı | Başvuru |
|---------------------|----------------|
| Geri bildirim kontrolü | Uyarlanabilir öğrenme oranları, eğitim stabilizasyonu |
| PID kontrolörleri | Hiperparametre ayarı, veri merkezlerinde sıcaklık kontrolü |
| Durum uzayı modelleri | Zaman serisi modelleme, tekrarlayan sinir ağları |
| Kalman filtresi | İzleme, sensör füzyonu, durum tahmini, zaman serisi tahmini |
| LQR / optimal kontrol | Takviyeli öğrenme (LQG kontrolü), robotik |
| Stabilite analizi | GAN'ların eğitim dinamikleri, RL algoritmalarının yakınsaması |
| Kontrol edilebilirlik/gözlemlenebilirlik | RNN ifadesini anlama, sistem tanımlama |
| Aktarım fonksiyonları | CNN'leri doğrusal filtreler, frekans alanı analizi olarak anlamak |
| Nyquist/Bode | Uyarlanabilir sistemler için sağlamlık analizi |
| Kutup yerleşimi | Öğrenilmiş sistemlerin dinamiklerini tasarlama (Nöral ODE'ler) |
---

## Özet
| Konsept | Temel Fikir | Anahtar Aracı |
|-----------|---------------|----------|
| Geribildirim | Girişi düzeltmek için çıkışı kullanın | Kapalı döngü aktarım işlevi |
| Aktarım fonksiyonu | S-alanında giriş-çıkış ilişkisi | G(ler) = Y(ler)/X(ler) |
| PID kontrolü | Orantılı + İntegral + Türev | En yaygın kullanılan endüstriyel kontrolör |
| Kararlılık | Sınırlı giriş için sınırlı çıktı | Routh-Hurwitz, Nyquist, Bode |
| Durum uzayı | Dahili devlet temsili | ẋ = Ax + Bu, y = Cx + Du |
| Kontrol Edilebilirlik | Herhangi bir duruma ulaşabilir miyiz? | Kontrol edilebilirlik matrisinde sıralama testi |
| Gözlemlenebilirlik | Devleti anlayabilir miyiz? | Gözlemlenebilirlik matrisinde sıralama testi |
| LQR | Optimum durum geri bildirimi | Riccati denklemi |
| Kalman filtresi | Optimum durum tahmini | Tahmin-güncelleme döngüsü |
Kontrol teorisi, sistemlerin istediğinizi güvenilir, sağlam ve verimli bir şekilde yapmasını sağlamanın matematiğidir. Geri bildirim, istikrar ve optimallik ilkelerinin evrensel olduğu kanıtlanmıştır ve robotikten pekiştirmeli öğrenmeye, ekonomiden biyolojiye kadar birçok alanda ortaya çıkmıştır. Veri bilimcileri için kontrol teorisi, uyarlanabilir sistemleri anlamak, istikrarlı eğitim prosedürleri tasarlamak ve dinamik ortamlarla etkileşime giren akıllı aracılar oluşturmak için gerekli dili sağlar.