---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Stokastik Süreçler
**Stokastik süreç** zamana (veya uzaya) göre indekslenen rastgele değişkenlerin bir koleksiyonudur. Olasılık teorisi bireysel rastgele olayları incelerken, stokastik süreçler rastgeleliğin zaman içinde nasıl geliştiğini inceler. Hisse senedi fiyatlarını, kuyruk uzunluklarını, hastalıkların yayılmasını, dil oluşumunu ve makine öğrenimi modellerinin eğitim dinamiklerini modellerler.
---

## Temeller
### Tanım
Bir stokastik süreç {X_t : t ∈ T}, ortak bir olasılık uzayında tanımlanan rastgele değişkenlerin bir ailesidir. T **indeks kümesidir** (zaman):
- **Ayrık zaman:** T = {0, 1, 2, ...}
- **Sürekli zaman:** T = [0, ∞)
**durum uzayı** S, X_t'nin alabileceği olası değerler kümesidir.
### Anahtar Özellikler
| Emlak | Tanımı |
|----------|---------------|
| **Durağanlık** | (X_{t₁}, ..., X_{tₖ})'nin ortak dağılımı (X_{t₁+τ}, ..., X_{tₖ+τ}) ile aynı |
| **Bağımsızlık** | t ≠ s için X_t X_s'den bağımsız |
| **Ergodiklik** | Zaman ortalamaları topluluk ortalamalarına yakınsıyor |
| **Markov mülkü** | Gelecek geçmişe değil, yalnızca bugüne bağlıdır |
| **Martingale** | Beklenen gelecekteki değer mevcut değere eşittir |
---

## Markov Zincirleri
**Markov zinciri**, gelecekteki durumun yalnızca mevcut duruma (hafızasız özellik) bağlı olduğu stokastik bir süreçtir.
### Ayrık Zamanlı Markov Zincirleri (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
**Geçiş matrisi** P'nin p_{ij} = P girdileri vardır (j'ye git | şu anda i'dedir).
| Emlak | Açıklama |
|----------|-----------|
| Satır toplamları | Her satırın toplamı 1'e eşittir: Σⱼ p_{ij} = 1 |
| n adımlı geçiş | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Sabit dağıtım | πP = π (özdeğeri 1 olan sol özvektör) |
### Durumların Sınıflandırılması
| Dönem | Tanımı |
|------|------------|
| **Tekrarlayan** | Zincir 1 olasılıkla i durumuna geri döner |
| **Geçici** | Asla geri dönmeme olasılığı sıfır |
| **Emici** | p_{ii} = 1 (bir kere girildi mi, asla çıkılmadı) |
| **Dönem** | dönüş sürelerinin GCD'si; periyot 1 = periyodik olmayan |
| **İletişim** | i ve j durumları birbirine ulaşabilir |
### Sabit Dağıtım
İndirgenemez, pozitif tekrarlayan bir Markov zinciri için, sabit dağılım π mevcuttur, benzersizdir ve aşağıdakileri karşılar:
πP = π, Σᵢ πᵢ = 1
**Yorum:** πᵢ = i durumunda geçirilen zamanın uzun vadeli oranı.
**Çalışılan Örnek:** {Güneşli, Yağmurlu} durumlarını içeren hava durumu modeli.
P = [[0,9, 0,1], [0,5, 0,5]] (satırlar: Sunny'den, Rainy'den)
Sabit dağılım: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Çözüm: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Durağanlığa Yakınsama
İndirgenemez, periyodik olmayan, pozitif tekrarlayan bir zincir için:
- Pⁿ → Π (tüm satırların π'ye eşit olduğu matris) n → ∞ olarak
- **Karıştırma süresi:** Dağıtım π'ye yakın olana kadar geçen adım sayısı
- **Spektral boşluk:** 1 − |λ₂| (burada λ₂ ikinci en büyük özdeğerdir) karıştırma hızını belirler
### Sürekli Zamanlı Markov Zincirleri (CTMC)
Geçişler üstel dağılımlar tarafından yönetilen rastgele zamanlarda meydana gelir.
| Konsept | Açıklama |
|-----------|------------|
| **Oran matrisi Q** | i ≠ j için q_{ij} ≥ 0; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Geçiş olasılıkları** | P(t) = e^{Qt} (matris üstel) |
| **Sabit dağıtım** | πQ = 0 |
| **Bekleme süresi** | i durumundaki zaman Exp(−q_{ii}) |
---

## Rastgele Yürüyüşler
**Rastgele yürüyüş**, birbirini takip eden rastgele adımlardan oluşan bir yoldur.
### Basit Rastgele Yürüyüş
X_n = X_{n-1} + Z_n, burada Z_n ∈ {+1, −1} p, q = 1−p olasılıklarıyla.
| Emlak | p = 1/2 (simetrik) | p ≠ 1/2 (önyargılı) |
|----------|----------|---------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Kökene geri mi dönüyor? | Evet (1 olasılıkla) | Hayır (uzaklaşır) |
| Tekrarlayan mı? | Evet (1D ve 2D'de) | Hayır |
### Yüksek Boyutlarda Rastgele Yürüyüş
| Boyut | Tekrarlayan mı? | Sezgi |
|-----------|---------------|-----------|
| 1B | Evet | "Sarhoş bir adam her zaman evinin yolunu bulur" |
| 2 boyutlu | Evet | "Sarhoş bir kuş her zaman evinin yolunu bulur" |
| 3D+ | Hayır | "Sarhoş bir serçe asla evinin yolunu bulamaz" |
### Brownian Hareketine Bağlantı
Rastgele yürüyüşü ölçeklendirme: S_n = ΣZ_i olsun. Daha sonra adım boyutu → 0 ve adımlar → ∞ olarak:
S_{⌊nt⌋} / √n → B(t) (Donsker teoremine göre Brown hareketi)
---

## Brown Hareketi
**Brown hareketi** (Wiener süreci) B(t), rastgele yürüyüşün sürekli zaman limitidir.
### Tanım
B(t) şunları karşılar:
1. B(0) = 0
2. B(t)'nin sürekli yolları vardır
3. Bağımsız artışlar: r < s < t için B(t) − B(s), B(s) − B(r)'den bağımsızdır
4. B(t) − B(s) ~ N(0, t − s) (Gauss artışları)
### Anahtar Özellikler
| Emlak | Açıklama |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(ler), B(t)] | = dk(s, t) |
| Hiçbir yerde türevlenebilir | Yollar süreklidir ancak türevi yoktur |
| Fraktal boyut | Grafiğin Hausdorff boyutu 3/2 |
| Markov mülkü | Gelecek yalnızca mevcut duruma bağlıdır |
| Martingal | E[B(t) | F_s] = s < t için B(s) |
### Geometrik Brownian Hareketi
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Bu, Black-Scholes çerçevesindeki hisse senedi fiyatları için standart modeldir.
- μ: sürüklenme (beklenen getiri)
- σ: oynaklık
---

## Poisson Süreçleri
Bir **Poisson süreci** N(t), [0, t]'de meydana gelen olayların sayısını sayar.
### Tanım
N(t) ~ Poisson(λt), burada λ hızdır (birim zaman başına olaylar).
| Emlak | Açıklama |
|----------|-----------|
| N(0) = 0 | — |
| Bağımsız artışlar | Ayrık aralıklardaki olaylar bağımsızdır |
| Sabit artışlar | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Varışlar arası zamanlar | Üstel dağılım: T_i ~ Exp(λ) |
### Genellemeler
| Varyant | Açıklama |
|-----------|------------|
| **Homojen değil** | Oran λ(t) zamana göre değişir |
| **Bileşik Poisson** | Her olayın rastgele bir boyutu vardır: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Poisson rastgele ölçüsü** | Sadece zamanda değil, uzay-zamanda da noktalar |
| **Çok değişkenli** | Olası etkileşimlere sahip birden fazla etkinlik türü |
---

## Martingaller
**Martingale** adil bir oyundur: tüm mevcut bilgiler göz önüne alındığında beklenen gelecekteki değer, mevcut değere eşittir.
### Tanım
{X_n}, eğer: {F_n} filtrelemesine göre bir martingaldir:
1. X_n, F_n ile ölçülebilirdir (uyarlanmıştır)
2. E[|X_n|] < ∞ (integrallenebilir)
3. E[X_{n+1} | F_n] = X_n (adil oyun)
| Varyant | Durum | Yorumlama |
|-----------|---------------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Adil oyun |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Uygun oyun (yükseliyor) |
| **Süpermartingale** | E[X_{n+1} | F_n] ≤ X_n | Olumsuz oyun (aşağı yönlü gidişat) |
### Temel Teoremler
| Teorem | Açıklama |
|-----------|-----------|
| **İsteğe bağlı durdurma** | Koşullar altında, T | durma süresi için E[X_T] = E[X_0]
| **Yakınsama** | Sınırlı bir martingale neredeyse kesin olarak yakınsar |
| **Maksimum eşitsizlik** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |
---

## Monte Carlo Yöntemleri
**Monte Carlo yöntemleri** deterministik miktarları tahmin etmek için rastgele örneklemeyi kullanır.
### Temel Fikir
X ~ P iken E[f(X)]'i tahmin etmek için:
1. N örnek çizin: P'den x₁, x₂, ..., x_N
2. Hesaplayın: Î = (1/N) Σᵢ f(xᵢ)
3. Büyük sayılar kanununa göre: Î → E[f(X)] as N → ∞
**Hata:** Standart hata = σ_f / √N, burada σ_f² = Var[f(X)]
### Varyans Azaltma Teknikleri
| Tekniği | Fikir | Hızlandırma |
|-----------|------|-----------|
| **Önem örneklemesi** | P yerine Q'dan örnek, P/Q'ya göre ağırlık | Dramatik olabilir |
| **Antitetik değişkenler** | Varyansı iptal etmek için (x, −x) çiftlerini kullanın | ~2x |
| **Kontrol değişkenleri** | f ile ilişkili bilinen beklenti fonksiyonunu çıkarın | Değişir |
| **Tabakalı örnekleme** | Alanı bölün, her katmanı örnekleyin | Farkı azaltır |
| **Rao-Blackwell** | Yeterli istatistik koşulu | Her zaman yardımcı olur |
---

## Markov Zinciri Monte Carlo (MCMC)
MCMC, durağan dağılımı hedef dağılım olan bir Markov zinciri oluşturur. Bir "yanma" süresinden sonra, numuneler hedeften yaklaşık olarak çekilir.
### Metropolis-Hastings Algoritması
| Adım | Eylem |
|------|--------|
| 1 | Mevcut durum: x_t |
| 2 | Teklif: x* ~ q(x* \| x_t) (teklif dağıtımı) |
| 3 | Kabul oranı: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | α olasılığıyla kabul edin: x_{t+1} = x* (kabul et) veya x_t (reddet) |
**Özel durum — Metropolis algoritması:** Simetrik öneri q(x*|x) = q(x|x*), dolayısıyla α = min(1, π(x*)/π(x_t)).
### Gibbs Örneklemesi
Her değişkenin tam koşullu dağılımından güncellendiği özel bir Metropolis-Hastings durumu.
Hedef π(x₁, x₂, ..., xₖ) için:
1. Örnek x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Örnek x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Tüm değişkenler için devam edin
4. Tekrarlayın
| Emlak | Açıklama |
|----------|-----------|
| Her zaman kabul eder | α = 1 (reddetme adımı yok) |
| Gerektirir | Her tam koşuldan örnekleme yeteneği |
| Yakınsama | İndirgenemez, periyodik olmayan zincirler için garantili |
### MCMC Teşhisleri
| Teşhis | Amaç |
|-----------|------------|
| **İzleme grafiği** | Karıştırma ve durağanlık için görsel kontrol |
| **Otokorelasyon** | Örnek bağımlılığını ölçer (düşük otokorelasyon ister) |
| **Gelman-Rubin (R̂)** | Birden fazla zinciri karşılaştırın; R̂ < 1,05 yakınsamaya işaret ediyor |
| **Etkili örneklem büyüklüğü** | N_eff = N / (1 + 2Σρₖ); otokorelasyon hesapları |
| **Yanma** | Zincir durağanlığa ulaşmadan ilk örnekleri atın |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Stokastik Süreç | Başvuru |
|---------------------|----------------|
| Markov zincirleri | PageRank (web grafiğinde rastgele yürüyüş), metin oluşturma (n-gram modelleri), MCMC |
| Rastgele yürüyüşler | Node2Vec ve DeepWalk (grafik yerleştirmeler), RL'de keşif |
| Brown hareketi | Üretken yapay zekada hisse senedi fiyatı modellemesi, yayılma modelleri |
| Poisson süreçleri | Olay varışlarını modelleme (tıklamalar, başarısızlıklar), kuyruk teorisi |
| Martingaller | Finansal matematik, SGD'nin yakınsamasını kanıtlıyor (stokastik yaklaşım) |
| Monte Carlo | Beklenen değerleri tahmin etme, Bayes çıkarımı, takviyeli öğrenme (politika değerlendirmesi) |
| MCMC (Metropolis-Hastings) | Bayesian arka örnekleme, olasılıksal programlama (Stan, PyMC) |
| Gibbs örneklemesi | Konu modelleri (LDA), Bayes ağları, görüntü kirliliği |
| MCMC teşhisi | Olasılıksal modellerden güvenilir çıkarımların sağlanması |
---

## Özet
| Süreç | Durum Uzayı | Zaman | Anahtar Özellik |
|-----------|------------|------|-------------|
| Markov zinciri | Ayrık/sürekli | Ayrık/sürekli | Hafızasız (Markov özelliği) |
| Rastgele yürüyüş | ℤᵈ | Ayrık | Kimlik toplamı adımlar |
| Brown hareketi | ℝ | Sürekli | Gauss artışları, sürekli yollar |
| Poisson süreci | ℕ | Sürekli | Üstel boşluklarla sayma işlemi |
| Martingal | ℝ | Ayrık/sürekli | Adil oyun (E[X_{t+1}|F_t] = X_t) |
Stokastik süreçler zaman içindeki rastgeleliğin matematiğidir. Modern Bayes çıkarımını (MCMC), takviyeli öğrenmeyi (Markov karar süreçleri), üretken modellemeyi (yayılma modelleri), finansal matematiği ve kuyruk teorisini desteklerler. Bu süreçleri anlamak size belirsizliği dinamik olarak modellemek için gerekli araçları sağlar; yalnızca anlık görüntü olarak değil, aynı zamanda geliştikçe.