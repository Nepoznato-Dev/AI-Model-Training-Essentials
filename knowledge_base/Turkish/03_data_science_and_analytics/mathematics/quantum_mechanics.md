---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Kuantum Mekaniği
Kuantum mekaniği, atomlar, elektronlar, fotonlar ve doğanın temel parçacıkları gibi en küçük ölçeklerdeki fiziğin teorisidir. Klasik mekaniğin deterministik dünyasının yerine olasılıkları, süperpozisyonları ve dolaşıklığı koyuyor. Mantık dışı doğasına rağmen kuantum mekaniği bilimin tamamında en kesin şekilde test edilmiş teoridir. Günümüzde ilkeleri, belirli sorunları klasik makinelerden katlanarak daha hızlı çözmeyi vaat eden kuantum bilgisayarlar aracılığıyla bilgi işlemle doğrudan ilgili hale geliyor.
---

## Tarihsel Motivasyon
### Klasik Fiziğin Başarısızlıkları
| Sorun | Klasik Tahmin | Gözlem | Çözünürlük |
|-----------|----------|------------|------------|
| Kara cisim radyasyonu | Ultraviyole felaketi (kısa λ'da sonsuz enerji) | Sonlu tepe dalga boyu | Planck: enerji kuantumlanmıştır (E = nhν) |
| Fotoelektrik etki | KE frekansa değil yoğunluğa bağlıdır | KE frekansa bağlıdır | Einstein: ışık kuantize edilmiştir (fotonlar, E = hν) |
| Atom spektrumları | Sürekli emisyon spektrumu | Ayrık spektral çizgiler | Bohr: elektronlar nicelenmiş yörüngelerde bulunur |
| Elektron kırınımı | Parçacıklar kırınıma uğramaz | Elektronlar girişim desenleri üretir | de Broglie: parçacıkların dalga boyu λ = h/p |
### Anahtar Sabitler
| Sabit | Sembol | Değer |
|----------|-----------|-------|
| Planck sabiti | h | 6,626 × 10⁻³⁴ J·s |
| Azaltılmış Planck sabiti | ℏ = h/2π | 1,055 × 10⁻³⁴ J·s |
| Işık hızı | c | 3,0 × 10⁸ m/s |
| Elektron kütlesi | m_e | 9,109 × 10⁻³¹ kg |
| Temel ücret | e | 1,602 × 10⁻¹⁹C |
| Bohr yarıçapı | a₀ | 5,292 × 10⁻¹¹m |
---

## Dalga-Parçacık İkiliği
### de Broglie Dalga Boyu
Momentumu p olan her parçacığın ilişkili bir dalga boyu vardır:
λ = h/p = h/(mv)
| Parçacık | Tipik λ | Gözlemlenebilir Dalga Davranışı? |
|----------|-----------|----------------|
| Elektron (100 eV) | 0,12nm | Evet (kristal kırınımı) |
| Proton | 0,003nm | Evet (nötron saçılması) |
| Beyzbol (40 m/s) | 10⁻³⁴ m | Hayır (algılanamayacak kadar küçük) |
### Çift Yarık Deneyi
Özetin özeti kuantum deneyi:
1. Parçacıkları (elektronlar, fotonlar) iki yarıkta birer birer ateşleyin
2. Her parçacık dedektör üzerinde tek bir noktaya iner
3. Zamanla, sanki her parçacık her iki yarıktan aynı anda geçmiş gibi bir girişim deseni ortaya çıkıyor
4. Parçacığın hangi yarıktan geçtiğini ölçerseniz girişim deseni kaybolur
**Sonuç:** Kuantum nesneleri ne salt parçacık ne de salt dalgadır. Gözlenmediğinde dalga benzeri, ölçüldüğünde parçacık benzeri davranış sergilerler.
---

## Dalga Fonksiyonu
### Tanım
**dalga fonksiyonu** ψ(x, t) tamamen bir kuantum sistemini tanımlar. Kare modülü olasılık yoğunluğunu veren karmaşık değerli bir fonksiyondur:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalleştirme
Toplam olasılık 1'e eşit olmalıdır:
∫ |ψ(x)|² dx = 1 (tüm uzayda)
### Doğuş Kuralı
Parçacığın x ile x + dx arasında bulunma olasılığı:
P(x'ten x+dx'e) = |ψ(x)|² dx
φₙ özdurumlarıyla gözlemlenebilir genel bir durum için:
P(özdeğer aₙ ölçümü) = |⟨φₙ|ψ⟩|²
---

## Schrödinger Denklemi
### Zamana Bağlı Schrödinger Denklemi
benℏ ∂ψ/∂t = Ĥψ
burada Ĥ **Hamilton operatörü**'dür (toplam enerji operatörü).
### Zamandan Bağımsız Schrödinger Denklemi
Durağan durumlar için (enerji özdurumları):
Ĥψ = Eψ
Bu bir özdeğer denklemidir: izin verilen enerjiler E, Ĥ'nın özdeğerleridir.
### Kutudaki Parçacık (Sonsuz Kare Kuyu)
En basit kuantum sistemi: 0 < x < L ile sınırlı parçacık.
| Miktar | Sonuç |
|----------|-----------|
| Dalga Fonksiyonları | ψₙ(x) = √(2/L) sin(nπx/L) |
| Enerji seviyeleri | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Temel durum | n = 1, E₁ = h²/(8mL²) |
| Sıfır noktası enerjisi | E₁ > 0 (parçacık tamamen hareketsiz olamaz) |
| Kuantum numarası | n = 1, 2, 3, ... (yalnızca pozitif tam sayılar) |
### Kuantum Harmonik Osilatör
V(x) = ½mω²x²
| Miktar | Sonuç |
|----------|-----------|
| Enerji seviyeleri | Eₙ = (n + ½)ℏω |
| Sıfır noktası enerjisi | E₀ = ½ℏω |
| Aralık | ΔE = ℏω (düzgün) |
| Dalga Fonksiyonları | Hermit polinomları × Gaussian |
---

## Operatörler ve Gözlenebilirler
Kuantum mekaniğinde gözlemlenebilir her fiziksel bir **Hermit operatörüne** karşılık gelir.
### Ana Operatörler
| Gözlemlenebilir | Operatör (konum alanı) | Özdeğerler |
|-----------|---------------|------------|
| Pozisyon | x̂ = x | Hepsi gerçek x |
| ivme | p̂ = −iℏ ∂/∂x | Hepsi gerçek p |
| Enerji (Hamiltoniyen) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (bağlı durumlar için ayrık) |
| Açısal momentum | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Döndürme | Ŝ = (ℏ/2)σ (Pauli matrisleri) | ±ℏ/2 (döndürme-½ için) |
### Beklenti Değerleri
ψ durumunda gözlemlenebilir A'nın ölçülmesinin ortalama sonucu:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Değiştirme İlişkileri
[Â, B̂] = ÂB̂ − B̂Â
| Komütatör | Sonuç | Önemi |
|-----------|-----------|------------|
| [x̂, p̂] | benℏ | Konum ve momentum uyumsuz |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Açısal momentum bileşenleri uyumsuzdur |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Pauli matrisleri (döndürme bileşenleri) |
Eğer [Â, B̂] = 0 ise, gözlenebilirler eş zamanlı olarak ölçülebilir (özdurumları paylaşır).
---

## Belirsizlik İlkesi
### Heisenberg Belirsizlik İlkesi
Δx · Δp ≥ ℏ/2
Daha genel olarak, herhangi iki gözlemlenebilir A ve B için:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Belirsizlik İlişkileri
| Çift | İlişki | Yorumlama |
|----------|----------|-----|
| Konum-momentum | ΔxΔp ≥ ℏ/2 | Her ikisini de tam olarak bilemiyorum |
| Enerji-zaman | ΔEΔt ≥ ℏ/2 | Kısa ömürlü devletlerin enerjisi belirsizdir |
| Açısal momentum | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | Tüm bileşenler aynı anda bilinemiyor |
**Önemli:** Belirsizlik ölçüm bozukluğuyla ilgili değildir; kuantum durumlarının temel bir özelliğidir. Bir parçacığın aynı anda belirli bir konumu ve momentumu yoktur.
---

## Kuantum Durumları ve Süperpozisyon
### Dirac Notasyonu (Bra-Ket)
| Sembol | İsim | Anlamı |
|----------|------|-----------|
| \|ψ⟩ | Ket | Durum vektörü (sütun vektörü) |
| ⟨ψ\| | Sütyen | Eşlenik devrik (satır vektörü) |
| ⟨φ\|ψ⟩ | İç ürün | ψ durumunda bulunacak genlik φ |
| \|ψ\|² | Normun karesi | Olasılık |
### Süperpozisyon Prensibi
Eğer \|ψ₁⟩ ve \|ψ₂⟩ geçerli kuantum durumlarıysa, o zaman herhangi bir doğrusal kombinasyon da geçerlidir:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

burada |α|² + |β|² = 1 (normalizasyon).
**Ölçüm:** Ölçüldüğünde, sistem |α|² olasılığıyla \|ψ₁⟩'ye veya |β|² olasılığıyla \|ψ₂⟩'ye "çöker".
### Kübitler
**qubit** bir kuantum bitidir: iki seviyeli bir kuantum sistemi.
\|ψ⟩ = α\|0⟩ + β\|1⟩, burada |α|² + |β|² = 1
| Temsil | \|0⟩ | \|1⟩ |
|---------------|----------|------|
| Döndürme | Döndürme ↑ | Aşağı dönüş ↓ |
| Foton polarizasyonu | Yatay | Dikey |
| Enerji seviyesi | Temel durum | Heyecanlı durum |
| Devre | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Bloch küresi:** Herhangi bir kübit durumu şu şekilde yazılabilir:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
burada θ ∈ [0, π] ve φ ∈ [0, 2π). Durum uzayı bir küredir.
---

## Dolaşma
Ortak durumları bireysel durumların bir ürünü olarak yazılamadığında iki kübit **dolanıktır**.
### Çan Durumları (Maksimum Dolaşıklık)
| Devlet | İfade | İsim |
|----------|---------------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Çan durumu |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Çan durumu |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Çan durumu |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Tekli durumu |
### Dolaşıklığın Özellikleri
| Emlak | Açıklama |
|----------|----------------|
| Korelasyon | Bir kübitin ölçülmesi, mesafeden bağımsız olarak diğerini anında belirler |
| İletişim yok | Işıktan daha hızlı bilgi göndermek için dolaşma tek başına kullanılamaz |
| Tekeşlilik | A, B ile maksimum düzeyde dolaşmışsa, C ile dolaşık olamaz |
| Kırılganlık | Çevreyle etkileşim dolaşıklığı (eşevresizliği) yok eder |
### EPR Paradoksu ve Bell Teoremi
Einstein, Podolsky ve Rosen, kuantum mekaniğinin eksik olması gerektiğini (gizli değişkenler) savundu. Bell, herhangi bir yerel gizli değişken teorisinin belirli eşitsizlikleri karşıladığını gösterdi. Deneyler Bell eşitsizliklerini ihlal ederek kuantum mekaniğini doğruluyor ve yerel gizli değişkenleri dışlıyor.
---

## Kuantum Kapıları
Kuantum kapıları kübitler üzerinde yapılan üniter işlemlerdir.
### Tek Kübitli Kapılar
| Kapı | Matris | Efekt |
|------|--------|--------|
| **Pauli-X** (DEĞİL) | [[0,1],[1,0]] | Bit çevirme: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,−i],[i,0]] | Bit + faz çevirme |
| **Pauli-Z** | [[1,0],[0,−1]] | Faz çevirme: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Süperpozisyon oluşturur: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Faz** (S) | [[1,0],[0,i]] | Z çevresinde π/2 dönüş |
| **T kapısı** | [[1,0],[0,e^{iπ/4}]] | Z çevresinde π/4 dönüş |
| **Döndürme** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | X ekseni etrafında θ ile döndürme |
### İki Kübitli Kapılar
| Kapı | Açıklama | Efekt |
|------|-------------|-------|
| **CNOT** | Kontrollü-DEĞİL | Kontrol \|1⟩ | ise hedefi döndürür
| **CZ** | Kontrollü-Z | Denetim \|1⟩ | ise hedefe Z uygulanır
| **DEĞİŞİM** | Kübit değişimi | \|ab⟩ → \|ba⟩ |
### Dolaşma Yaratmak
Kübit 1'e H uygulayın, ardından kübit 1'i kontrol olarak kullanarak CNOT'u uygulayın:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Kuantum Algoritmaları
| Algoritma | Hızlandırma | Başvuru |
|-----------|------------|-------------|
| **Shor'lar** | Üstel (faktoring) | RSA şifrelemesini kırar |
| **Kıvırcık** | İkinci dereceden (arama) | O(√N)'de yapılandırılmamış arama |
| **VQE** | Sezgisel | Temel durum enerjilerini bulma (kimya, malzeme) |
| **QAOA** | Sezgisel | Kombinatoryal optimizasyon |
| **HHL** | Üstel (koşullar altında) | Doğrusal sistemleri çözme |
| **Kuantum simülasyonu** | Üstel | Kuantum sistemlerini simüle etmek (Feynman'ın orijinal motivasyonu) |
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Kuantum Kavramı | Başvuru |
|----------------|---------------|
| Kübitler ve süperpozisyon | Kuantum makine öğrenimi, kuantumla geliştirilmiş örnekleme |
| Dolaşma | Kuantum iletişimi, kuantum anahtar dağıtımı (QKD) |
| Kuantum kapıları | ML alt rutinleri için kuantum devre tasarımı |
| Grover'ın algoritması | Arama tabanlı optimizasyon için ikinci dereceden hızlanma |
| Shor'un algoritması | Mevcut kriptografiye yönelik tehdit; kuantum sonrası kriptoyu motive ediyor |
| Kuantum simülasyonu | İlaç keşfi, malzeme bilimi, kimya simülasyonu |
| Varyasyonel algoritmalar (VQE, QAOA) | NISQ cihazlarında yakın dönem kuantum makine öğrenimi |
| Doğum kuralı | Dağılımlardan örneklemeye benzer olasılıksal sonuçlar |
| Tensör ürünler | Çok kübitli sistemler (üstel durum uzayı — ML'deki çoklu doğrusal cebirle aynı matematik) |
| Üniter matrisler | Ortogonal dönüşümlerin kuantum analogları |
---

## Özet
| Konsept | Temel Fikir | Anahtar Denklem |
|-----------|-----------|------------|
| Dalga-parçacık ikiliği | Maddenin dalga özellikleri vardır | λ = h/p |
| Dalga fonksiyonu | Kuantum durumunun tam açıklaması | P(x) = \|ψ(x)\|² |
| Schrödinger denklemi | Kuantum durumları nasıl gelişir | iℏ ∂ψ/∂t = Ĥψ |
| Operatörler | Gözlenebilirler Hermit operatörleridir | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Belirsizlik | Eşzamanlı bilginin temel sınırları | ΔxΔp ≥ ℏ/2 |
| Süperpozisyon | Eyaletler eklenebilir | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Dolaşma | Ayrılamayan eklem durumları | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Kuantum kapıları | Kübitler üzerinde üniter işlemler | H, CNOT ve üniversal kapı setleri |
Kuantum mekaniği, gerçeklik hakkındaki en derin sezgilerimize meydan okuyor: Dalga olan parçacıklar, aynı anda iki yerde bulunan nesneler, klasik açıklamaya meydan okuyan korelasyonlar. Ancak matematiği kesindir ve öngörüleri benzersiz doğruluktadır. Veri bilimcileri için kuantum mekaniği, optimizasyonu, kriptografiyi, simülasyonu ve potansiyel olarak makine öğrenimini dönüştürmeyi vaat eden kuantum hesaplama yoluyla doğrudan alakalı hale geliyor.