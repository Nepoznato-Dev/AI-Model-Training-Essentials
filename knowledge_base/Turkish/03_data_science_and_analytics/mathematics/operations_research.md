<!--
---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Yöneylem Araştırması
Yöneylem araştırması (OR), matematiksel yöntemlerin karar verme sürecine uygulanmasıdır. İkinci Dünya Savaşı sırasında askeri lojistik için doğmuş olan bu şirket, artık tedarik zincirlerini optimize ediyor, havayollarını programlıyor, teslimat filolarını yönlendiriyor, envanterleri yönetiyor ve kaynakları her sektöre tahsis ediyor. VEYA, kısıtlamalar altında mümkün olan en iyi kararları vermek için matematiksel araç seti sağlar.
---

## Doğrusal Programlama Formülasyonları
### Standart Form
Cᵀx'i en aza indirin
Aşağıdakilere tabidir: Ax = b, x ≥ 0
### Ortak LP Formülasyonları
**Ürün Karışımı:**
- Karar değişkenleri: xⱼ = üretilecek j ürününün miktarı
- Amaç: karı maksimuma çıkarmak Σ pⱼxⱼ
- Kısıtlamalar: kaynak sınırları Σ aᵢⱼxⱼ ≤ bᵢ
**Diyet Sorunu:**
- Karar değişkenleri: xⱼ = satın alınacak j yiyecek miktarı
- Amaç: maliyeti en aza indirmek Σ cⱼxⱼ
- Kısıtlamalar: beslenme gereksinimleri Σ nᵢⱼxⱼ ≥ rᵢ
**Harmanlama Sorunu:**
- Karar değişkenleri: xⱼ = karışımdaki j bileşeninin oranı
- Amaç: maliyeti en aza indirmek
- Kısıtlamalar: kalite gereksinimleri (oktan sayısı, güç vb.)
### Çözümlü Örnek: Üretim Planlama
Bir fabrika A ve B ürünlerini üretmektedir.
- A 2 saat işçilik, 1 kg malzeme gerektirir; kâr 30$
- B 1 saat işçilik, 3 kg malzeme gerektirir; kar 40$
- Mevcut: 40 saat işçilik, 30 kg malzeme
**Formülasyon:**
- Maksimuma Çıkarma: 30x_A + 40x_B
- Tabi: 2x_A + x_B ≤ 40 (işçilik)
- x_A + 3x_B ≤ 30 (malzeme)
- x_A, x_B ≥ 0
**Çözüm:** Uygun bölgenin köşe noktaları: (0,0), (20,0), (18,4), (0,10)
- (0,0): kar = 0
- (20,0): kâr = 600
- (18,4): kâr = 700 ← optimal
- (0,10): kâr = 400
---

## Ulaşım Sorunu
Malların m kaynaktan n varış noktasına minimum maliyetle taşınması.
### Formülasyon
- Karar değişkenleri: xᵢⱼ = i kaynağından j hedefine gönderilen miktar
- Amaç: Σᵢ Σⱼ cᵢⱼxᵢⱼ'yi en aza indirmek
- Şuna tabidir: Σⱼ xᵢⱼ = sᵢ (tedarik kısıtlamaları)
- Σᵢ xᵢⱼ = dⱼ (talep kısıtlamaları)
- xᵢⱼ ≥ 0
### Çözüm Yöntemleri
| Yöntem | Açıklama | İlk Çözümün Kalitesi |
|----------|----------------|----------------|
| **Kuzeybatı Köşesi** | Sol üstten başlayın, açgözlülükle tahsis edin | Uygun ama çoğu zaman yetersiz |
| **Vogel Yaklaşımı** | Ceza maliyetlerini göz önünde bulundurun | Daha iyi başlangıç ​​çözümü |
| **MODI / Basamak Taşı** | Başlangıç ​​çözümünü yinelemeli olarak geliştirin | En uygununu bulur |
### Çalışılan Örnek
| | D1 | D2 | D3 | Tedarik |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Talep | 40 | 30 | 30 | 100 |
---

## Atama Problemi
Toplam maliyeti en aza indirmek için n işçiyi n işe (bire bir) atamak.
### Formülasyon
- Karar değişkenleri: xᵢⱼ ∈ {0, 1} (eğer i işçisi j işine atanmışsa 1)
- Küçült: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Şu şartlara tabidir: Σⱼ xᵢⱼ = 1 (her işçi bir iş alır)
- Σᵢ xᵢⱼ = 1 (her işte bir işçi bulunur)
### Macar Algoritması
| Emlak | Değer |
|----------|----------|
| Zaman karmaşıklığı | O(n³) |
| İdeal mi? | Evet |
| Yaklaşım | Matris azaltma + minimum kaplama |
**Adımlar:**
1. Her satırdan satır minimumlarını çıkarın
2. Her sütundan sütun minimumlarını çıkarın
3. Tüm sıfırları minimum sayıda satırla örtün
4. Eğer satırlar = n ise, sıfırlar arasında en uygun atama bulunur
5. Aksi halde matrisi ayarlayın ve tekrarlayın
---

## Ağ Akışı Optimizasyonu
### Minimum Maliyet Akışı
Kapasiteleri ve maliyetleri kenarlarda olan bir ağ verildiğinde, talepleri minimum maliyetle karşılayan akışı bulun.
**Formülasyon:**
- Minimize etme: Σ cᵢⱼxᵢⱼ
- Şunlara tabidir: her düğümde akışın korunması
- Kapasite kısıtlamaları: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Ağ Akışı Olarak En Kısa Yol
En kısa yol problemi, minimum maliyetli akışın özel bir durumudur (s'den t'ye 1 birim gönderin).
### Uygulamalar
| Başvuru | Ağ Modeli |
|------------|-------------|
| Tedarik zinciri | Düğümler = depolar, kenarlar = nakliye yolları |
| İletişim | Düğümler = yönlendiriciler, kenarlar = bant genişliğine sahip bağlantılar |
| Trafik | Düğümler = kavşaklar, kenarlar = kapasiteli yollar |
| Proje yönetimi | CPM/PERT ağları |
---

## Dinamik Programlama
**Dinamik programlama (DP)** karmaşık sorunları örtüşen alt sorunlara bölerek çözer.
### Bellman'ın Optimallik İlkesi
Optimal bir politika, başlangıç ​​durumu ve kararı ne olursa olsun, geri kalan kararların ortaya çıkan durum için optimal bir politika oluşturması gerektiği özelliğine sahiptir.
### Temel Unsurlar
| Eleman | Açıklama |
|-----------|------------|
| **Sahne** | Karar noktası (zaman adımı, madde dizini) |
| **Devlet** | Karar vermek için gereken bilgiler |
| **Karar** | Her aşamada yapılan seçim |
| **Yineleme** | n−1 aşamasına göre n aşamasındaki optimum değer |
### Klasik DP Sorunları
| Sorun | Tekrarlama | Karmaşıklık |
|-----------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) notlandırmalı |
| **Sırt çantası** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **En kısa yol** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) veya O(E log V) |
| **Mesafeyi düzenle** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+maliyet) | O(mn) |
| **En uzun ortak alt dizi** | L(i,j) = L(i−1,j−1)+1 eşleşirse, aksi halde max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Matris zincir çarpımı** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Çözümlü Örnek: 0/1 Sırt Çantası
Öğeler: {ağırlık: değer} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Kapasite W = 7.
V(i, w) = w kapasiteli ilk i öğelerini kullanan maksimum değer
| i\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Optimal: V(4, 7) = 23 (madde 1 ve 4: ağırlık 2+5=7, değer 12+11=23).
---

## Kuyruk Teorisi
Kuyruk teorisi bekleme kuyruklarını (ne kadar uzun olduklarını, ne kadar beklediklerini ve her ikisinin nasıl azaltılabileceğini) inceler.
### Kendall'ın Notasyonu
A/B/c/K/N/D burada:
- A = varış süreci (M = Markovian/Poisson, D = deterministik, G = genel)
- B = hizmet süreci (aynı seçenekler)
- c = sunucu sayısı
- K = kapasite (varsayılan ∞)
- N = nüfus (varsayılan ∞)
- D = disiplin (FIFO, LIFO, Öncelik)
### M/M/1 Sırası (Tek Sunucu)
| Metrik | Formül |
|----------|------------|
| Kullanım | ρ = λ/μ |
| Sistemdeki ortalama sayı | L = ρ/(1−ρ) |
| Sistemdeki ortalama süre | W = 1/(μ−λ) |
| Sıradaki ortalama sayı | L_q = ρ²/(1−ρ) |
| Ortalama bekleme süresi | W_q = ρ/(μ−λ) |
burada λ = varış oranı, μ = hizmet oranı, ρ = kullanım.
### M/M/c Sırası (Birden Fazla Sunucu)
| Metrik | Formül |
|----------|------------|
| Kullanım | ρ = λ/(cμ) |
| Bekleme olasılığı (Erlang C) | P_w = ρ ve c'yi içeren karmaşık formül |
| Ortalama kuyruk uzunluğu | L_q = P_w · ρ/(1−ρ) |
### Küçükler Yasası
L = λW (sistemdeki ortalama sayı = varış hızı × ortalama süre)
Bu, varış/hizmet dağılımlarına bakılmaksızın HERHANGİ bir kuyruk sistemi için geçerlidir.
### Uygulama Örnekleri
| Senaryo | Kuyruk Modeli |
|----------|----------------|
| Çağrı merkezi | M/M/c (acenteler) |
| Web sunucusu istekleri | M/M/1 veya M/G/1 |
| Hastane acil durumu | Öncelikleri olan M/G/c |
| Üretim hattı | Kuyruk ağı |
| Bilgisayar CPU planlaması | M/M/1 işlemci paylaşımı |
---

## Envanter Modelleri
### Ekonomik Sipariş Miktarı (EOQ)
Toplam stok maliyetlerini en aza indiren optimum sipariş miktarı.
Q* = √(2DS/H)
| Değişken | Anlamı |
|----------|-----------|
| D | Yıllık talep |
| S | Sipariş başına sipariş maliyeti |
| H | Yıllık birim başına elde bulundurma maliyeti |
| Soru* | Optimum sipariş miktarı |
**Q*:**'da toplam maliyet TC = √(2DSH)
### Uzantılar
| Modeli | Uzantı |
|----------|---------------|
| **İndirimli EOQ** | Miktar indirimleri maliyet fonksiyonunu değiştirir |
| **Üretim siparişi miktarı** | Ürünler bir anda değil, kademeli olarak üretiliyor |
| **(s, Q) modeli** | Envanter s seviyesine düştüğünde Q birimlerini yeniden sıralayın |
| **(s, S) modeli** | Envanter s'ye düştüğünde S'ye kadar sipariş verin |
| **Haber satıcısı modeli** | Tek dönemli, belirsiz talep |
### Haber Satıcısı Modeli
Tek dönemli çabuk bozulan stoklar için optimum sipariş miktarı:
P(D ≤ Q*) = c_u / (c_u + c_o)
burada c_u = reşit olmayan maliyet (kar kaybı) ve c_o = fazla kullanım maliyeti (atık).
---

## Planlama
### İş Mağazası Planlaması
| Gösterim | Anlamı |
|----------|-----------|
| n/m/J/C_maks | n iş, m makine, atölye, yapım süresini en aza indirme |
| Akış mağazası | Tüm işler makineleri aynı sırayla ziyaret eder |
| İş mağazası | Her işin kendi makine sırası vardır |
| Mağazayı aç | Sipariş kısıtlaması yok |
### Öncelik Kuralları
| Kural | Açıklama | Efekt |
|------|-------------|-------|
| FCFS | İlk gelen ilk alır | Adil ama optimal değil |
| SPT | Önce en kısa işlem süresi | Ortalama tamamlamayı en aza indirir |
| EDD | Önce en erken vade tarihi | Maksimum gecikmeyi en aza indirir |
| CR | Kritik oran (kalan vade tarihi / işlem süresi) | Dengeli |
| LPT | İlk önce en uzun işlem süresi | Paralel makinelerde makespan için iyi |
### Johnson Algoritması (2 Makineli Akış Atölyesi)
2 makinedeki n iş için yapım süresini en aza indiren:
1. İşlem süresi en kısa olan işi bulun
2. Makine 1'deyse önce onu planlayın; makine 2'deyse, bunu en sona planla
3. Bu işi kaldırın ve işlemi tekrarlayın
2 makine için ideal; 3+ makine için NP-zor.
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| VEYA Konsepti | Başvuru |
|-----------|----------------|
| Doğrusal programlama | Kaynak tahsisi, portföy optimizasyonu, reklam bütçesi tahsisi |
| Ulaşım/ödeme | Lojistik, araç paylaşımı eşleştirmesi, görev atama |
| Ağ akışı | Tedarik zinciri optimizasyonu, veri merkezi trafiği yönlendirme |
| Dinamik programlama | Dizi hizalaması (biyoinformatik), Viterbi algoritması (HMM'ler), RL (Bellman denklemi) |
| Kuyruk teorisi | Sunucu kapasitesi planlama, gecikme modelleme, bulut kaynak tahsisi |
| Envanter modelleri | Talep tahmini entegrasyonu, tedarik zinciri ML |
| Planlama | Makine öğrenimi ardışık düzeni orkestrasyonu, GPU iş planlaması, hiperparametre arama planlaması |
| Tamsayı programlama | Özellik seçimi (ikili), model seçimi, ağ tasarımı |
---

## Özet
| Konu | Temel Sorun | Anahtar Yöntemi |
|----------|----------------|------------|
| LP Formülasyonları | Kısıtlamalarla doğrusal hedefi optimize edin | Simpleks, iç nokta |
| Ulaşım | Malları minimum maliyetle gönderin | MODI, basamak taşı |
| Ödev | İşçileri işlerle eşleştirin | Macar algoritması |
| Ağ Akışı | Bir ağ üzerinden akışı yönlendirin | Minimum maliyetli akış algoritmaları |
| Dinamik Programlama | Örtüşen alt problemler | Bellman ilkesi, not alma |
| Kuyruk Teorisi | Bekleme hattı analizi | M/M/1, Little yasası |
| Envanter | Ne zaman ve ne kadar sipariş verilir | EOQ, haber satıcısı |
| Planlama | Makinelerde sıralı işler | Öncelik kuralları, Johnson algoritması |
Yöneylem araştırması karar almayı sanattan bilime dönüştürür. OR, gerçek dünya problemlerini matematiksel olarak formüle ederek, her sektörü etkileyen lojistik, zamanlama, kaynak tahsisi ve planlama sorunlarına kanıtlanmış optimal (veya optimale yakın) çözümler sağlar. Veri bilimcileri için OR yöntemleri makine öğrenimini tamamlar: ML tahmin ederken, OR öngörüde bulunur ve birlikte akıllı karar sistemlerinin temelini oluştururlar.