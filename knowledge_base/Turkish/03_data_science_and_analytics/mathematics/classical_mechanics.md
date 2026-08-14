<!--
---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
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

-->
# Klasik Mekanik
Klasik mekanik, kuvvetlerin etkisi altındaki nesnelerin hareketini açıklar. Düşen elmalardan yörüngede dönen gezegenlere, titreşen sicimlerden çarpışan parçacıklara kadar ilkeleri makroskobik dünyayı yönetir. Klasik mekanik, fiziksel uygulamalarının ötesinde, varyasyonlar hesabını, simplektik geometriyi ve kuantum mekaniği ile modern optimizasyonun temelini oluşturan Hamilton çerçevesini doğurdu.
---

## Newton Mekaniği
### Newton'un Üç Yasası
| Hukuk | Açıklama | Matematiksel Form |
|-----|-----------|-----------|
| **İlk (Eylemsizlik)** | Bir nesne, üzerine bir kuvvet uygulanmadığı sürece hareketsiz veya düzgün hareket halinde kalır | F_net = 0 ise v = sabit |
| **İkinci (F = ma)** | Kuvvet eşittir kütle çarpı ivme | **F** = m**a** = m(d²**x**/dt²) |
| **Üçüncü (Etki-Tepki)** | Her etkinin eşit ve zıt bir tepkisi vardır | **F**₁₂ = −**F**₂₁ |
### Serbest Cisim Diyagramları
**Serbest cisim diyagramı** bir nesneyi izole eder ve ona etki eden tüm kuvvetleri gösterir.
**Ortak güçler:**
| Kuvvet | Formül | Yön |
|----------|------------|-----------|
| Yerçekimi (Dünya'ya yakın) | F = mg | Aşağı |
| Normal kuvvet | N | Yüzeye dik |
| Sürtünme (statik) | f_s ≤ μ_s N | Yaklaşan harekete karşı çıkıyor |
| Sürtünme (kinetik) | f_k = μ_k N | Harekete karşı çıkıyor |
| Bahar (Hooke yasası) | F = −kx | Geri yükleme (dengeye doğru) |
| Gerginlik | T | İp/ip boyunca |
| Sürükle | F_d = ½C_d ρAv² | Hıza karşı çıkıyor |
### Çözümlü Örnek: Eğimde Blok
θ açısında sürtünmesiz bir eğim üzerinde m kütleli bir blok.
- Kuvvetler: yerçekimi (mg aşağı), normal kuvvet (N yüzeye dik)
- Yer çekimini ayrıştırın: mg sin θ (eğim boyunca), mg cos θ (yüzeye doğru)
- N = mg cos θ (yüzeye dik hareket yok)
- Eğim boyunca hızlanma: a = g sin θ
---

## Enerji Yöntemleri
### İş ve Kinetik Enerji
**Bir kuvvetin yaptığı iş**: W = ∫ **F** · d**r**
**İş-Enerji Teoremi:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Potansiyel Enerji
| Kuvvet | Potansiyel Enerji | Notlar |
|----------|----------|----------|
| Yerçekimi (yüzeye yakın) | U = mgh | h = referansın üzerindeki yükseklik |
| Yerçekimi (genel) | U = −GMm/r | Sonsuzda sıfır |
| Bahar | U = ½kx² | x = dengeden yer değiştirme |
| Elektrostatik | U = kq₁q₂/r | Benzer yükler: pozitif U |
### Enerjinin Korunumu
Yalnızca korunumlu kuvvetler etki ediyorsa: E = KE + PE = sabit
½mv₁² + U₁ = ½mv₂² + U₂
**Çalışılan Örnek:** h yüksekliğinden bırakılan bir top.
- Başlangıç: KE = 0, PE = mgh
- Yere çarpmadan hemen önce: KE = ½mv², PE = 0
- Korunum: mgh = ½mv² → v = √(2gh)
### Güç
P = dW/dt = **F** · **v** (iş yapma oranı)
---

## Momentum ve Çarpışmalar
### Doğrusal Momentum
**p** = m**v**
Newton'un ikinci yasası (alternatif biçim): **F** = d**p**/dt
### Momentumun Korunumu
Eğer dış kuvvet yoksa: toplam momentum korunur.
| Çarpışma Türü | KE Korundu mu? | Momentum Korundu mu? |
|---------------|---------------|----------|
| **Elastik** | Evet | Evet |
| **Esnek olmayan** | Hayır | Evet |
| **Mükemmel elastik olmayan** | Hayır (maksimum kayıp) | Evet (nesneler birbirine yapışıyor) |
**1 boyutlu elastik çarpışma:** Başlangıç hızları u₁, u₂ olan iki kütleli m₁, m₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Açısal Momentum
**L** = **r** × **p** = m(**r** × **v**)
Tork: **τ** = d**L**/dt = **r** × **F**
**Korunum:** Harici tork yoksa açısal momentum korunur.
---

## Lagrange Mekaniği
**Lagrangian** formülasyonu kuvvetlerin yerine enerjiyi koyarak daha zarif ve genel bir çerçeve sağlar.
### Lagrange
L = T − V (kinetik enerji eksi potansiyel enerji)
### En Az Eylem Prensibi (Hamilton Prensibi)
Bir sistemin t₁ ile t₂ zamanları arasında izlediği gerçek yol, **eylemi** en aza indirir (daha kesin olarak durağan hale getirir):
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Euler-Lagrange Denklemleri
δS = 0 koşulu şunu verir:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
her genelleştirilmiş koordinat için q.
**Çalışılan Örnek:** Basit sarkaç (uzunluk l, kütle m, dikeyden θ açısı).
- T = ½ml²θ̇²
- V = −mgl çünkü θ
- L = ½ml²θ̇² + mgl çünkü θ
- ∂L/∂θ = −mgl sin θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) sin θ = 0
### Lagrange Mekaniğinin Avantajları
| Avantajı | Açıklama |
|-----------|----------------|
| Koordinattan bağımsız | Her koordinat sisteminde çalışır |
| Kısıtlamaları doğal bir şekilde ele alır | Kısıtlama kuvvetlerini hesaplamaya gerek yok |
| Simetri → korunum | Noether teoremi simetrileri korunan miktarlara bağlar |
| Kolayca genelleştirir | Alanlara, göreliliğe, kuantum mekaniğine |
---

## Hamilton Mekaniği
**Hamilton** formülasyonu, Lagrange mekaniğinin (konumlar ve hızlar yerine) konumları ve momentumları kullanan yeniden formüle edilmiş halidir.
### Hamiltoniyen
H = Σᵢ pᵢq̇ᵢ − L = T + V (çoğu mekanik sistem için)
burada pᵢ = ∂L/∂q̇ᵢ **genelleştirilmiş momentumlardır**.
### Hamilton Denklemleri
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Bunlar 2n adet birinci dereceden ODE'dir (n adet ikinci dereceden Euler-Lagrange denklemine karşılık).
**Çalışılan Örnek:** Harmonik osilatör (kütle m, yay sabiti k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (beklendiği gibi)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Hooke yasası)
### Poisson Parantezleri
f(q, p) ve g(q, p) fonksiyonları için:
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Emlak | Açıklama |
|----------|-----------|
| Zaman evrimi | df/dt = {f, H} + ∂f/∂t |
| Koruma | f korunur eğer {f, H} = 0 (ve ∂f/∂t = 0) |
| Temel parantez | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Kuantum mekaniğiyle bağlantı:** Poisson parantezleri komutatör haline gelir: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Korunum Yasaları ve Noether Teoremi
### Noether Teoremi
Lagrange'ın her sürekli simetrisi, korunan bir miktara karşılık gelir.
| Simetri | Korunan Miktar |
|----------|-----------|
| Zaman öteleme değişmezliği | Enerji |
| Uzamsal çeviri değişmezliği | Doğrusal momentum |
| Dönme değişmezliği | Açısal momentum |
| Gösterge değişmezliği | Elektrik yükü |
Bu, tüm fizikteki en derin sonuçlardan biridir; uzay-zamanın geometrisini temel korunum yasalarına bağlar.
---

## Katı Cisim Dinamiği
**Sert cisim**, tüm iç mesafelerin sabit kaldığı bir nesnedir.
### Temel Kavramlar
| Konsept | Formül | Açıklama |
|-----------|-----------|-------------|
| **Atalet momenti** | I = Σmᵢrᵢ² veya I = ∫r² dm | Dönme ivmesine karşı direnç |
| **Döner KE** | KE = ½Iω² | Dönme enerjisi |
| **Açısal momentum** | L = Iω | p = mv'nin dönme analoğu |
| **Tork** | τ = Iα | F = ma'nın dönme analoğu |
### Atalet Momentleri (Genel Şekiller)
| Şekil | Eksen | ben |
|----------|------|---|
| Katı küre | Merkezden | (2/5)MR² |
| İçi boş küre | Merkezden | (2/3)MR² |
| Katı silindir | Eksen boyunca | (1/2)MR² |
| İnce çubuk | Merkezden dikey | (1/12)ML² |
| İnce çubuk | Uçtan uca dikey | (1/3)ML² |
| Disk | Merkezden dikey | (1/2)MR² |
---

## Yörünge Mekaniği
### Kepler Kanunları
| Hukuk | Açıklama |
|-----|-----------|
| **İlk (Elipsler)** | Gezegenler, odak noktası Güneş olacak şekilde elips şeklinde hareket ediyor |
| **İkinci (Eşit alanlar)** | Güneş'ten gezegene doğru bir çizgi eşit zamanlarda eşit alanları tarar |
| **Üçüncü (Harmonik)** | T² ∝ a³ (periyodun karesi yarı ana eksenin küpüyle orantılı) |
### Yörünge Enerjisi
E = ½mv² − GMm/dev
| E | Yörünge Türü |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hiperbolik (bağlanmamış) |
### Kaçış Hızı
v_kaçış = √(2GM/R)
Dünya için: v_escape ≈ 11,2 km/s
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Mekanik Konsepti | Başvuru |
|---------------------|----------------|
| Newton yasaları | Simülasyonlarda fizik motorları, oyun yapay zekası, robotik |
| Enerji yöntemleri | Enerji tabanlı modeller, Hopfield ağları, Boltzmann makineleri |
| Lagrange mekaniği | Fizik bilgili sinir ağları, optimal kontrol, yörünge optimizasyonu |
| Hamilton mekaniği | Hamilton sinir ağları (HNN'ler), simülasyon için basit entegratörler |
| Koruma yasaları | ML modellerinde endüktif önyargılar, eşdeğişken sinir ağları |
| Noether teoremi | Simetriye duyarlı makine öğrenimi, geometrik derin öğrenme |
| Katı cisim dinamiği | Robotik simülasyon, moleküler dinamik, 3D animasyon |
| Yörünge mekaniği | Uydu konumlandırma (konum tabanlı ML için GPS), uzay görevi tasarımı |
| Faz uzayı (Hamiltoniyen) | Dinamik sistemleri, çekici ağları anlama |
| Varyasyon hesabı | Optimum taşıma, üretken modelleme (akış eşleştirme) |
---

## Özet
| Çerçeve | Çekirdek Denklemi | Güç |
|-----------|-----------------|----------|
| Newtonyen | **F** = m**a** | Sezgisel, doğrudan kuvvet analizi |
| Lagrange | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Koordinat içermez, kısıtlamaları yönetir |
| Hamiltoniyen | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Basit yapı, QM'ye bağlanır |
| Koruma yasaları | Noether teoremi | Derin simetri koruma bağlantısı |
Klasik mekanik sadece düşen toplardan ve sallanan sarkaçlardan ibaret değildir. Matematiksel çerçeveleri - Lagrange ve Hamilton mekaniği - tüm bilimdeki en etkili fikirler arasındadır. Enerji tabanlı modellerin ve fizik bilgili sinir ağlarının doğrudan bu asırlık formülasyonlardan yararlandığı kuantum mekaniği, alan teorisi ve hatta modern makine öğrenimine genelleme yapıyorlar.