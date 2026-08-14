---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Termodinamik ve İstatistik Mekanik
Termodinamik, atomların neye benzediğini bilmeden sistemlerin makroskobik davranışını sıcaklık, basınç ve entropi açısından tanımlar. İstatistiksel mekanik, termodinamiği aşağıdan yukarıya doğru açıklar: çok sayıda parçacığın mikroskobik davranışından makroskobik özellikler elde eder. Birlikte, bilgi teorisine, makine öğrenimine ve ötesine taşınan enerji, entropi ve denge kavramlarına ilişkin en derin anlayışı sağlarlar.
---

## Termodinamik Değişkenler ve Durum
### Durum Değişkenleri
| Değişken | Tür | Birim | Açıklama |
|----------|------|----------|------------|
| Sıcaklık (T) | Yoğun | Kelvin (K) | Parçacık başına ortalama kinetik enerji |
| Basınç (P) | Yoğun | Paskal (Pa) | Birim alan başına kuvvet |
| Cilt (V) | Kapsamlı | m³ | Alan işgal edildi |
| İç enerji (U) | Kapsamlı | Joule (J) | Toplam mikroskobik enerji |
| Entropi (S) | Kapsamlı | J/K | Düzensizlik/mikrodurumların ölçüsü |
| Parçacık sayısı (N) | Kapsamlı | mol veya sayım | Madde miktarı |
**Yoğun** değişkenler sistem boyutuna bağlı değildir; **kapsamlı** değişkenler bunu yapar.
### Durum Denklemi
İdeal bir gaz için: PV = nRT = Nk_BT
| Sabit | Değer |
|----------|----------|
| R (gaz sabiti) | 8,314 J/(mol·K) |
| k_B (Boltzmann sabiti) | 1,381 × 10⁻²³ J/K |
| N_A (Avogadro sayısı) | 6,022 × 10²³ /mol |
---

## Termodinamik Kanunları
### Sıfırıncı Yasa
Eğer A, B ile ve B, C ile termal dengede ise, o zaman A, C ile termal dengededir.
**Anlamı:** Sıcaklık iyi tanımlanmış ve ölçülebilir bir kavramdır.
### Birinci Kanun (Enerji Korunumu)
ΔU = Q - W
| Sembol | Anlamı |
|----------|------------|
| ΔU | İç enerjideki değişim |
| Soru | Sisteme eklenen ısı |
| W | Sistem tarafından yapılan işler |
**Diferansiyel form:** dU = δQ − δW = δQ − PdV
| Süreç | Kısıtlama | Sonuç |
|-----------|-----------|------------|
| izokorik | dV = 0 | W = 0, ΔU = Q |
| İzobarik | dP = 0 | W = PΔV |
| İzotermal | dT = 0 | ΔU = 0 (ideal gaz), Q = W |
| Adyabatik | δQ = 0 | ΔU = −W |
### İkinci Yasa (Entropi)
**Clausius ifadesi:** Isı soğuktan sıcağa kendiliğinden akamaz.
**Kelvin-Planck beyanı:** Hiçbir motor ısının tamamını işe dönüştüremez.
**Entropi ifadesi:** Herhangi bir süreç için: ΔS_universe ≥ 0
| İşlem türü | ΔS_evren |
|------------|------------|
| Tersine çevrilebilir | = 0 |
| Geri döndürülemez (gerçek) | > 0 |
**Entropi değişimi:** dS = δQ_rev / T
### Üçüncü Kanun
T → 0 K olduğundan mükemmel bir kristalin entropisi sıfıra yaklaşır: lim_{T→0} S = 0
**Anlamı:** Mutlak sıfıra sonlu adımlarla ulaşılamaz.
---

## Derinlikte Entropi
### Termodinamik Entropi
S bir durum fonksiyonudur. A ve B durumları arasındaki tersinir bir süreç için:
ΔS = ∫_A^B δQ_rev / T
**Çalışılan Örnek:** Sabit basınçta suyu T₁'den T₂'ye ısıtırken entropi değişimi.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### İstatistiksel Entropi (Boltzmann)
S = k_B ln Ω
burada Ω, makro durumla tutarlı mikro durumların sayısıdır.
| Makrodurum | Mikrodurumlar (Ω) | Entropi |
|-----------|----------|-----------|
| Tüm gaz kutunun yarısında | Küçük | Düşük |
| Gaz eşit şekilde dağıtıldı | Çok büyük | Yüksek |
| 0 K'da mükemmel kristal | 1 | 0 |
**Bağlantı:** İkinci yasa istatistiksel hale gelir; sistemler daha fazla mikrodurum içeren makrodurumlara doğru evrilir çünkü bunlar çok daha olasıdır.
---

## Entalpi ve Serbest Enerji
### Entalpi
H = U + PV
Sabit basınçtaki işlemler için kullanışlıdır (çoğu kimya ve biyoloji).
ΔH = Q_p (sabit basınçta ısı)
### Helmholtz Serbest Enerjisi
F = U - TS
| Emlak | Açıklama |
|----------|-----------|
| Anlamı | Sabit T, V'de çıkarılabilir maksimum iş |
| Denge | Sistem F'yi sabit T, V'de en aza indirir |
| Bölüm işleviyle ilişki | F = −k_BT ln Z |
### Gibbs Serbest Enerjisi
G = H - TS = U + PV - TS
| Emlak | Açıklama |
|----------|-----------|
| Anlamı | Sabit T, P'de maksimum genişlemeyen iş |
| Denge | Sistem G'yi sabit T, P'de en aza indirir |
| Kendiliğindenlik | ΔG < 0 → kendiliğinden; ΔG = 0 → denge |
| Kimyasal reaksiyonlar | ΔG = ΔH − TΔS yönü belirler |
### Termodinamik Potansiyellerin Özeti
| Potansiyel | Doğal Değişkenler | Diferansiyel | Küçültülmüş Zaman |
|-----------|-----------|---------------|----------------|
| U (iç enerji) | S, V | dU = TdS - PdV | İzole sistem |
| H (entalpi) | S, P | dH = TdS + VdP | Sabit P, adyabatik |
| F (Helmholtz) | T, V | dF = −SdT − PdV | Sabit T, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | Sabit T, P |
---

## Carnot Döngüsü
**Carnot çevrimi**, T_H (sıcak) ve T_C (soğuk) sıcaklıkları arasında çalışan, mümkün olan en verimli ısı motorudur.
### Dört Aşama
| Sahne | Süreç | Ne Olur |
|----------|------------|-------------|
| 1 → 2 | İzotermal genleşme | Sıcak rezervuardan Q_H ısısını T_H |
| 2 → 3 | Adyabatik genişleme | Gaz T_H'den T_C'ye soğuyor |
| 3 → 4 | İzotermal sıkıştırma | Q_C ısısını T_C'deki soğuk rezervuara reddet |
| 4 → 1 | Adyabatik sıkıştırma | Gaz T_C'den T_H'ye ısıtılır |
### Carnot Verimliliği
η_Carnot = 1 - T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500 Bin | 300 Bin | %40 |
| 1000 Bin | 300 Bin | %70 |
| 300 Bin | 299 bin | %0,33 |
**Hiçbir gerçek motor Carnot verimliliğini aşamaz.** Gerçek motorlar her zaman geri döndürülemez (sürtünme, türbülans, sonlu sıcaklık farkları).
---

## İstatistiksel Mekanik
### Boltzmann Dağılımı
T sıcaklığında termal dengede olan bir sistem için, E_i enerjili bir mikro durumda olma olasılığı:
P(E_i) = (1/Z) e^{−E_i / k_BT}
burada Z **bölüm işlevi**'dir:
Z = Σᵢ e^{−E_i / k_BT}
### Bölümleme İşlevi
Z, sistem hakkındaki tüm termodinamik bilgileri kodlar.
| Miktar | Formül |
|----------|-----------|
| Helmholtz serbest enerjisi | F = −k_BT ln Z |
| Ortalama enerji | ⟨E⟩ = −∂(ln Z)/∂β burada β = 1/(k_BT) |
| Entropi | S = k_B(ln Z + β⟨E⟩) |
| Isı kapasitesi | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Basınç | P = (1/β) ∂(ln Z)/∂V |
### Çözümlü Örnek: İki Durumlu Sistem
Bir parçacık 0 durumunda (enerji 0) veya 1 durumunda (enerji ε) olabilir.
Z = 1 + e^{−βε}
| Miktar | Sonuç |
|----------|-----------|
| P(durum 0) | 1/(1 + e^{−βε}) |
| P(durum 1) | e^{−βε}/(1 + e^{−βε}) |
| ⟨E⟩ | ε/(1 + e^{βε}) |
| Yüksek T limiti (β→0) | ⟨E⟩ → ε/2 (eşit olasılık) |
| Düşük T limiti (β→∞) | ⟨E⟩ → 0 (temel durum) |
### Eş Bölünme Teoremi
Her ikinci dereceden serbestlik derecesi, ortalama enerjiye ½k_BT katkıda bulunur.
| Sistem | Serbestlik Derecesi | ⟨E⟩ |
|----------|-----------|------|
| Tek atomlu gaz (He) | 3 çeviri | (3/2)k_BT |
| T odasında diatomik gaz (N₂) | 3 trans + 2 çürük | (5/2)k_BT |
| Yüksek T'de diatomik gaz | 3 geçiş + 2 çürük + 1 titreşim | (7/2)k_BT |
| Katı (Einstein modeli) | 3 titreşimli (atom başına) | 3k_BT |
---

## Bilgi Teorisine Bağlantı
### Shannon Entropisi ve Termodinamik Entropisi
| Görünüş | Shannon Entropi H(X) | Termodinamik Entropi S |
|----------|----------|--------------------------|
| Tanımı | −Σ pᵢ log pᵢ | k_B ln Ω (veya −k_B Σ pᵢ ln pᵢ) |
| Maksimum ne zaman | Düzgün dağıtım | Termal denge |
| Önlemler | Belirsizlik / bilgi içeriği | Erişilebilir mikro durumların sayısı |
| Birimler | Bitler veya natlar | J/K |
**Gibbs entropi formülü:** S = −k_B Σᵢ pᵢ ln pᵢ (şekil olarak Shannon entropisiyle aynı)
### Maksimum Entropi Prensibi
Her iki alan da aynı prensibi kullanır: Bilgi durumumuzu en iyi temsil eden dağılım, bilinen kısıtlamalara tabi olarak entropiyi maksimuma çıkaran dağılımdır.
| Kısıtlama | Sonuç Dağıtımı |
|-----------|---------------|
| Bilinen ortalama | Üstel dağılım |
| Bilinen ortalama ve varyans | Gauss dağılımı |
| Bilinen enerji ⟨E⟩ | Boltzmann dağıtımı |
| Kısıtlama yok | Düzgün dağıtım |
### Landauer Prensibi
Bir bitlik bilginin silinmesi, en az k_BT ln 2 enerjinin ısı olarak dağılmasına neden olur. Bu, bilgi işlemeyi doğrudan termodinamiğe bağlar; hesaplamanın temel bir enerji maliyeti vardır.
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Termo/StatMech Konsepti | Başvuru |
|--------------------------|---------------|
| Boltzmann dağıtımı | Softmax işlevi, enerji tabanlı modeller, tavlama benzetimi |
| Bölüm işlevi | Olasılıksal modellerde normalleştirme sabiti, genel olarak inatçı |
| Serbest enerji | Varyasyonel çıkarım (değişimsel serbest enerjinin en aza indirilmesi = KL farklılığının en aza indirilmesi) |
| Entropi | RL'de düzenleme, araştırma (maksimum entropi RL), karar ağaçları |
| Maksimum entropi ilkesi | MaxEnt sınıflandırıcıları, ön seçim, dağılım tahmini |
| Tavlama simülasyonu | "Sıcaklığı" kademeli olarak azaltarak küresel optimizasyon |
| İstatistiksel mekanik | Öğrenmede aşama geçişlerini anlama (grokking, çift iniş) |
| Eşbölümleme | Fiziksel simülasyonlarda enerji dağılımını anlama |
| Landauer ilkesi | Hesaplamanın temel sınırları, tersine çevrilebilir hesaplama |
| Gibbs örneklemesi | MCMC yöntemi doğrudan istatistiksel mekanikten esinlenmiştir |
| Sıcaklık (softmax cinsinden) | Tahminlerin rastgeleliğini kontrol eder: P(i) ∝ exp(z_i/T) |
---

## Özet
| Hukuk/Kavram | Temel Fikir | Formül |
|---------------|-----------|-----------|
| Sıfırıncı yasa | Sıcaklık iyi tanımlanmıştır | Termal dengenin geçişliliği |
| Birinci yasa | Enerji korunur | ΔU = Q − W |
| İkinci yasa | Evrenin entropisi artıyor | ΔS ≥ 0 |
| Üçüncü yasa | Mutlak sıfıra ulaşılamaz | S → 0 olarak T → 0 |
| Boltzmann entropisi | Entropi mikro durumları sayar | S = k_B ln Ω |
| Boltzmann dağıtımı | Enerji durumlarının olasılığı | P ∝ e^{−E/k_BT} |
| Bölüm işlevi | Tüm termodinamik bilgileri kodlar | Z = Σ e^{−E_i/k_BT} |
| Serbest enerji | Yararlı çalışmalar mevcut | F = U - TS, G = H - TS |
| Carnot verimliliği | Maksimum ısı motoru verimliliği | η = 1 − T_C/T_H |
Termodinamik ve istatistiksel mekanik, fiziğin bilgi teorisiyle buluştuğu yerdir. Isı motorlarını yöneten aynı entropi, veri sıkıştırmayı da yönetir. Gaz moleküllerini tanımlayan aynı Boltzmann dağılımı, her sınıflandırıcıdaki softmax katmanına güç verir. Bu bağlantıları anlamak size fizik, olasılık ve makine öğrenimi konusunda birleşik bir görünüm sunar.