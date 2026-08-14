---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Bilgi Teorisi
Claude Shannon tarafından 1948'de kurulan bilgi teorisi, bilginin kendisini nicelikselleştirir. Bir mesaj size ne kadar şey anlatır? Verileri ne kadar sıkıştırabilirsiniz? Gürültülü bir kanal üzerinden ne kadar hızlı iletişim kurabilirsiniz? Bu soruların kesin matematiksel cevapları vardır. İletişimin ötesinde, bilgi teorisi makine öğreniminin temeli haline geldi; çapraz entropi sınıflandırma için varsayılan kayıp fonksiyonudur, KL farklılığı dağıtım benzerliğini ölçer ve karşılıklı bilgi özellik seçimini yönlendirir.
---

## Entropi
**Entropi** bir rastgele değişkenin ortalama belirsizliğini veya "sürprizini" ölçer.
### Shannon Entropisi (Ayrık)
Olasılık kütle fonksiyonu p(x) olan ayrık bir rastgele değişken X için:
H(X) = −Σₓ p(x) log₂ p(x)
Birimler: **bit** (log₂ kullanıldığında) veya **nats** (ln kullanıldığında).
| Dağıtım | Entropi | Sezgi |
|-------------|-----------|-----------|
| Adil para (p = 0,5, 0,5) | 1 bit | İkili sonuç için maksimum belirsizlik |
| Önyargılı para (p = 0,9, 0,1) | 0,469 bit | Daha az şaşırtıcı - çoğunlukla kafalar |
| Deterministik (p = 1, 0) | 0 bit | Hiçbir belirsizlik yok |
| Adil kalıp (6 taraf) | 2,585 bit | Daha fazla sonuç = daha fazla belirsizlik |
| n'den fazla sonuç | log₂(n) bit | n sonuç için maksimum entropi |
### Entropinin Özellikleri
| Emlak | Açıklama |
|----------|-----------|
| Olumsuzluk | H(X) ≥ 0 |
| Maksimum | Tekdüze dağılım için eşitlikle H(X) ≤ log₂(\|X\|) |
| Zincir kuralı | H(X, Y) = H(X) + H(Y \| X) |
| Koşullandırma azaltır | H(X \| Y) ≤ H(X) |
| İçbükeylik | H olasılık dağılımının içbükey bir fonksiyonudur |
### Diferansiyel Entropi (Sürekli)
Yoğunluğu p(x) olan sürekli bir rastgele değişken X için:
h(X) = −∫ p(x) log p(x) dx
Ayrık entropinin aksine, diferansiyel entropi **negatif** olabilir.
| Dağıtım | Diferansiyel Entropi |
|---------------|----------|
| Üniforma [a,b] | log(b − a) |
| Normal N(μ, σ²) | (1/2) log(2πeσ²) |
| Üstel(λ) | 1 − ln(λ) |
---

## Ortak, Koşullu ve Karşılıklı Bilgi
### Ortak Entropi
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
(X, Y) çiftinin toplam belirsizliğini ölçer.
### Koşullu Entropi
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
X'i gözlemledikten sonra Y ile ilgili kalan belirsizliği ölçer.
### Karşılıklı Bilgi
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
X'in size Y hakkında ne kadar bilgi verdiğini ölçer (ve tam tersi).
| Emlak | Açıklama |
|----------|-----------|
| Olumsuzluk | I(X; Y) ≥ 0 |
| Simetri | ben(X; Y) = I(Y; X) |
| Entropi ile İlişki | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Eklemle ilişkisi | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Bağımsızlık | I(X; Y) = 0 eğer X ve Y bağımsızsa |
| Kişisel bilgi | I(X; X) = H(X) |
### Görsel: Entropi Diyagramı
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## KL Farklılığı
**Kullback-Leibler (KL) sapması** bir dağılımın diğerinden ne kadar farklı olduğunu ölçer.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Emlak | Açıklama |
|----------|-----------|
| Olumsuzluk | D_KL(P \|\| Q) ≥ 0 (Gibbs eşitsizliği) |
| Kimlik | D_KL(P \|\| Q) = 0 eğer P = Q |
| Asimetri | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) genel olarak |
| Bir ölçü değil | Simetri ve üçgen eşitsizliği başarısız |
**Yorum:** D_KL(P || Q), Q için optimize edilmiş bir kod kullanarak P'den gelen verileri kodlamak için gereken ekstra bit sayısıdır.
### Diğer Niceliklerle İlişki
| İlişki | Formül |
|---------------|-----------|
| Çapraz entropi | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Karşılıklı bilgi | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| Koşullu KL | D_KL(P(Y\|X) \|\| Q(Y\|X)) X |
---

## Çapraz Entropi
P ve Q dağılımları arasındaki **çapraz entropi**:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Kayıp Fonksiyonu Olarak Çapraz Entropi
Sınıflandırmada P, gerçek dağılımdır (tek sıcak kodlanmış etiket) ve Q, modelin tahmin edilen dağılımıdır.
**İkili çapraz entropi (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Kategorik çapraz entropi:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Senaryo | y (doğru) | ŷ (tahmin edilen) | Kayıp |
|----------|----------|---------------|------|
| Doğru, kendinden emin | 1 | 0,95 | 0,051 |
| Doğru, belirsiz | 1 | 0,55 | 0,598 |
| Yanlış, kendinden emin | 1 | 0,05 | 2.996 |
| Yanlış, belirsiz | 1 | 0,45 | 0,799 |
Çapraz entropiyi en aza indirmek, KL'nin gerçek dağılımdan sapmasını en aza indirmeye eşdeğerdir; bu nedenle bir kayıp fonksiyonu olarak bu kadar iyi çalışır.
---

## Kanal Kapasitesi
### İletişim Kanalı Modeli
```
X → [Channel] → Y
```

- X: rastgele değişken girişi
- Y: çıktı rastgele değişkeni
- Kanal: p(y|x) koşullu olasılıklarıyla tanımlanır
### Shannon'ın Gürültülü Kanal Kodlama Teoremi
Kapasitesi C olan bir kanal için iletim hızı R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C ise güvenilir iletişim imkansızdır.
**Kanal kapasitesi:**
C = max_{p(x)} I(X; Y)
### Önemli Kanal Örnekleri
| Kanal | Açıklama | Kapasite |
|-----------|---------------|----------|
| **İkili simetrik (BSC)** | Her biti p | olasılığıyla çevirir 1 – H(p) bitleri |
| **İkili silme (BEC)** | Her biti ε | olasılığıyla siler 1 − ε bit |
| **Gauss (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bit |
| **Gürültüsüz ikili** | Mükemmel iletim | 1 bit |
---

## Kaynak Kodlama ve Sıkıştırma
### Kaynak Kodlama Teoremi
Bir kaynağı kodlamak için gereken ortalama bit sayısı, aşağıda entropisi ile sınırlanmıştır:
L ≥ H(X)
En uygun kod L ≈ H(X)'e ulaşır.
### Huffman Kodlaması
Daha olası sembollere daha kısa kodlar atayan **ön ek içermeyen** kod.
| Sembol | Olasılık | Huffman Kodu | Uzunluk |
|----------|----------------|-------------|--------|
| bir | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Ortalama uzunluk: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bit/sembol
Entropi: H = 1,75 bit/sembol (bu durumda en uygun!)
### Kayıpsız ve Kayıplı Sıkıştırma
| Tür | Prensip | Örnekler | Sınırı |
|------|-----------|----------|-------|
| **Kayıpsız** | İstatistiksel fazlalığı kaldırın | ZIP, PNG, FLAC | Entropi oranı H(X) |
| **Kayıplı** | Algısal olarak ilgisiz bilgileri kaldırın | JPEG, MP3, H.264 | Hız-bozulma fonksiyonu R(D) |
**Hız-bozulma teorisi:** Maksimum distorsiyon D ile kayıplı sıkıştırma için minimum hız, E[d(X, X̂)] ≤ D'ye tabi olarak R(D) = min I(X; X̂)'dir.
---

## Diğer Alanlara Bağlantılar
### Bilgi Teorisi ve Termodinamik
| Konsept | Bilgi Teorisi | Termodinamik |
|-----------|----------------------|----------------|
| Entropi | Shannon entropisi H(X) | Boltzmann entropisi S = k_B ln W |
| Maksimum entropi | Düzgün dağıtım | Termal denge |
| KL farklılığı | Dağıtım farkı | Serbest enerji farkı |
| Karşılıklı bilgi | Paylaşılan bilgiler | Fiziksel sistemlerdeki korelasyonlar |
Matematiksel formlar aynıdır - Shannon "entropi" terimini kasıtlı olarak istatistiksel mekanikten ödünç almıştır.
### Bilgi Teorisi ve İstatistik
| Konsept | Başvuru |
|-----------|------------|
| Maksimum olasılık | Ampirik dağılımdan model dağılımına kadar KL farklılığını en aza indirmeye eşdeğer |
| Fisher bilgileri | KL diverjansının eğriliği; Tahminci varyansının alt sınırı (Cramér-Rao) |
| Minimum açıklama uzunluğu (MDL) | Toplam kodlama uzunluğunu en aza indirerek model seçimi |
| AIC / BIC | Yaklaşık KL tabanlı model seçim kriterleri |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| BT Konsepti | ML Uygulaması |
|---------------|----------------|
| Çapraz entropi kaybı | Varsayılan sınıflandırma kaybı (ikili ve çoklu sınıf) |
| KL farklılığı | VAE kaybı (düzenleme terimi), dağıtım eşleştirme, damıtma |
| Karşılıklı bilgi | Özellik seçimi (MIFS), temsil öğrenme (InfoMax), çözme |
| Entropi | Karar ağacı bölme kriteri (bilgi kazancı), RL'de keşif (maksimum entropi RL) |
| Kanal kapasitesi | İletişim karmaşıklığı, genelleme sınırlarını anlama |
| Kaynak kodlaması | Depolama ve iletim için veri sıkıştırma, verimli kodlama |
| Maksimum entropi | MaxEnt sınıflandırıcıları, Bayes çıkarımında ön seçim |
| Hız bozulması | Sinir ağlarında kayıplı sıkıştırma ve nicemleme arasındaki dengeleri anlamak |
| Fisher bilgileri | Doğal gradyan inişi, parametre hassasiyetini anlama |
| MDL / AIC / BIC | Model seçimi, aşırı uyumu önleme |
---

## Özet
| Miktar | Formül (ayrık) | Anlamı |
|----------|-----------|-----------|
| Entropi H(X) | −Σ p(x) log p(x) | Ortalama belirsizlik |
| Ortak entropi H(X,Y) | −Σ p(x,y) log p(x,y) | Paritenin toplam belirsizliği |
| Koşullu entropi H(Y\|X) | H(X,Y) − H(X) | X verildiğinde Y hakkında kalan belirsizlik |
| Karşılıklı bilgi I(X;Y) | H(X) − H(X\|Y) | X ve Y arasında paylaşılan bilgiler |
| KL ıraksaması D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | Dağıtımlar arasındaki "Mesafe" |
| Çapraz entropi H(P,Q) | −Σ P(x) log Q(x) | Yanlış dağıtım kullanarak kodlama maliyeti |
| Kanal kapasitesi C | maksimum I(X;Y) | Maksimum güvenilir iletişim oranı |
Bilgi teorisi öğrenilebilecek, sıkıştırılabilecek ve iletilebilecek şeylerin temel sınırlarını sağlar. Makine öğrenimi uygulayıcıları için çapraz entropinin neden bir kayıp fonksiyonu olarak çalıştığını, öğrenilen temsillerin kalitesinin nasıl ölçüleceğini ve model karmaşıklığı ile veri uyumu arasındaki dengenin nasıl düşünüleceğini açıklıyor. Shannon'ın 1948'deki görüşleri, telekomünikasyonla olduğu kadar modern yapay zekayla da alakalı olmaya devam ediyor.