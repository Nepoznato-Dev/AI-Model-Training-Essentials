---
# Metadata
title: "Discrete Mathematics"
description: "Sets in depth, relations, functions, combinatorics, pigeonhole principle, recurrence relations, and generating functions"
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
    changes: "Initial deep-dive into discrete mathematics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [discrete-mathematics, set-theory, relations, combinatorics, pigeonhole-principle, recurrence-relations, generating-functions]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "../logic_and_critical_thinking.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Ayrık Matematik
Ayrık matematik, pürüzsüz, kesintisiz niceliklerle ilgilenen sürekli matematiğin (matematik, gerçek analiz) aksine, temelde sayılabilir veya ayrılmış matematiksel yapıların incelenmesidir. Ayrık matematik, bilgisayar bilimi, kriptografi, algoritma tasarımı ve veri yapılarının temelini oluşturur. Sürekli matematik fiziksel dünyayı tanımlıyorsa, ayrık matematik hesaplamalı dünyayı tanımlar.
---

## Teoriyi Derinlemesine Belirleyin
Kümeler neredeyse tüm modern matematiğin üzerine inşa edildiği temeldir. **küme**, **öğeler** veya **üyeler** olarak adlandırılan farklı nesnelerin sırasız bir koleksiyonudur.
### Aksiyomatik Temeller (ZFC)
Modern küme teorisi **Seçim Aksiyomu (ZFC)** ile Zermelo-Fraenkel aksiyomlarına dayanır. Bu aksiyomlar, kümelerin nasıl oluşturulabileceğini kısıtlayarak Russell Paradoksu ("kendilerini içermeyen tüm kümelerin kümesi") gibi paradoksları çözer.
| Aksiyom | Resmi Olmayan Açıklama |
|----------|----------------------|
| Genişletilebilirlik | İki küme aynı elemanlara sahipse eşittir |
| Boş Set | Hiçbir elemanı olmayan bir küme vardır: ∅ |
| Eşleştirme | Herhangi bir a, b için {a, b} vardır |
| Birliği | Herhangi bir küme ailesi için bunların birleşimi mevcuttur |
| Güç Seti | Herhangi bir S kümesi için, S'nin tüm alt kümelerinin kümesi mevcuttur: P(S) |
| Sonsuzluk | Sonsuz bir küme var |
| Şartname | Herhangi bir A kümesi ve P özelliği için, {x ∈ A : P(x)} mevcuttur |
| Değiştirme | Tanımlanabilir bir fonksiyon altında bir kümenin görüntüsü bir kümedir |
| Düzenlilik | Boş olmayan her küme kendisinden ayrı bir öğe içerir (kendi kendine üye olmayı engeller) |
| Seçim | Boş olmayan ikili ayrık kümelerin herhangi bir ailesi için bir seçim fonksiyonu mevcuttur |
### Kümelerin Önem Derecesi ve Boyutu
|S| ile gösterilen bir kümenin **kardinalliği** onun "boyutunu" ölçer.
| Konsept | Tanımı | Örnek |
|-----------|---------------|-----------|
| Sonlu küme | Kardinalite olarak doğal bir sayıya sahiptir | |{a, b, c}| = 3 |
| Sayılabilir sonsuz | ℕ ile aynı önem derecesi | ℤ, ℚ sayılabilir sonsuzdur |
| Sayılamayan | ℕ'den büyük | ℝ, P(ℕ), tüm fonksiyonların kümesi ℕ → {0,1} |
| Cantor Teoremi | Herhangi bir S kümesi için |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**Cantor'un çapraz argümanı** ℝ'nin sayılamayan olduğunu kanıtlar: tüm gerçekleri [0,1]'de listeleyebildiğinizi varsayalım, ardından n'inci ondalık basamakta listelenen n'inci gerçekten farklı olan yeni bir gerçek oluşturabilirsiniz — çelişki.
### Setlerdeki İşlemler
| Operasyon | Gösterim | Tanımı | Emlak |
|-----------|----------|---------------|----------|
| Birliği | A ∪ B | {x : x ∈ A veya x ∈ B} | Değişmeli, ilişkisel |
| Kavşak | bir ∩ B | {x : x ∈ A ve x ∈ B} | Değişmeli, ilişkisel |
| Fark | A \ B | {x : x ∈ A ve x ∉ B} | Değişmeli değil |
| Simetrik Fark | bir △ B | (A \ B) ∪ (B \ A) | Değişmeli, ilişkisel |
| Tamamlayıcı | Aᶜ | U \ A (burada U evrensel kümedir) | (Aᶜ)ᶜ = A |
| Kartezyen Ürün | A × B | {(a,b) : a ∈ A, b ∈ B} | |A × B| = |A| · |B| |
**De Morgan Kanunları:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Dahil Etme-Hariç Tutma Prensibi** (sonlu kümeler için):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## İlişkiler
A ve B kümelerindeki A **bağıntı** R, A × B'nin bir alt kümesidir. (a, b) ∈ R olduğunda aRb yazarız.
### İlişki Türleri
Bir A kümesi üzerindeki R ilişkisi şu özelliklere sahip olabilir:
| Emlak | Tanımı | Örnek |
|----------|---------------|-----------|
| Dönüşlü | ∀a ∈ A: aRa | ≤ açık ℤ |
| Yansımasız | ∀a ∈ A: ¬(aRa) | < ℤ'da |
| Simetrik | ∀a,b: aRb → bRa | = herhangi bir sette |
| Antisimetrik | ∀a,b: aRb ∧ bRa → a = b | ≤ açık ℤ |
| Geçişli | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = açık ℤ |
### Denklik İlişkileri
**Eşdeğerlik ilişkisi** dönüşlü, simetrik ve geçişlidir. Bir kümeyi ayrık **denklik sınıflarına** böler.
**Örnek:** Modüler aritmetik. a ~ b iff a ≡ b (mod n)'yi tanımlayın. Eşdeğerlik sınıfları [0], [1], ..., [n−1]'dir ve ℤ'yu n sınıfa ayırır.
**Çalışılan Örnek:** ℤ × ℤ üzerinde (a,b) ~ (c,d)'yi tanımlayın, eğer a + d = b + c. Bu bir denklik ilişkisidir. Sınıf [(0,0)] = {(n,n) : n ∈ ℤ}. Sınıf [(1,0)] = {(n+1,n) : n ∈ ℤ}. Bu yapı aslında doğal sayılardan tam sayıları tanımlar.
### Kısmi Siparişler
**Kısmi sıra** dönüşlü, antisimetrik ve geçişlidir. Kısmi sıralı bir kümeye **kısmen sıralı küme (poset)** denir.
| Konsept | Tanımı | Örnek |
|-----------|---------------|-----------|
| Poset | (S, ≤) ≤ kısmi sıra ile | (P(A), ⊆) — dahil edilmeye göre sıralanmış alt kümeler |
| Zincir | Tamamen sıralı bir altküme | P({a,b,c})'de {∅, {a}, {a,b}} |
| Antikain | Hiçbir iki öğenin karşılaştırılabilir olmadığı bir alt küme | P({a,b})'da {{a}, {b}} |
| Hasse Diyagramı | Bir pozun görsel temsili | Kenarları yalnızca kaplama ilişkileri için çizin |
| Üst Sınır | Bir öğe ≥ bir alt kümedeki her öğe | sup({2,3}) = 6 in (ℤ, \|) (bölünebilme) |
| En Küçük Üst Sınır (up) | En küçük üst sınır | (ℕ, ≤)'daki sup({2,3}) 3'tür |
| En Büyük Alt Sınır (inf) | En büyük alt sınır | (ℕ, \|) içindeki inf({4,6}) 2'dir |
---

## İşlevler
A **fonksiyonu** f: A → B, A'nın her elemanına B'nin tam olarak bir elemanını atar.
### Fonksiyonların Sınıflandırılması
| Tür | Tanımı | Örnek |
|------|------------|-----------|
| Enjektif (bire bir) | f(a) = f(b) → a = b | f(x) = 2x ℤ → ℤ |
| Surjektif (üzerine) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2'den ℤ → {0,1} |
| Bijektif | Hem birebir hem de örten | f(x) = x + 1 ℤ → ℤ |
### Önemli Fonksiyon Kavramları
| Konsept | Tanımı | Kullanım Örneği |
|-----------|---------------|----------|
| Ters fonksiyon | f⁻¹ var ancak f bijektiftir | Şifrelenmiş verilerin şifresini çözme |
| Kompozisyon | (g ∘ f)(x) = g(f(x)) | Zincirleme dönüşümler |
| Kimlik işlevi | kimlik(x) = x | Kompozisyon için nötr unsur |
| Sabit nokta | f(x) = x | Yinelenen tanımlar, anlambilim |
| Permütasyon | Bir kümeden kendisine bir çıkarım | Verileri yeniden düzenleme, karıştırma |
### Sayma İşlevleri
Verilen sonlu kümeler |A| = m ve |B| =n:
| Tür | Sayısı |
|------|----------|
| Tüm işlevler A → B | yok |
| Enjeksiyon fonksiyonları | N! / (n−m)! (eğer n ≥ m, değilse 0) |
| Surjektif işlevler | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (dahil etme-hariç tutma yoluyla) |
| Bijektif işlevler | N! (m = n olduğunda) |
---

## Kombinatorik
Kombinatorik sayma, düzenleme ve seçme matematiğidir.
### Temel Sayma İlkeleri
| Prensip | Açıklama | Örnek |
|-----------|-----------|-----------|
| Toplam Kuralı | A ve B ayrıksa |A ∪ B| = |A| + |B| | Meyve seçimi: 3 elma + 4 portakal = 7 seçenek |
| Çarpım Kuralı | |A × B| = |A| · |B| | Kıyafet: 3 gömlek × 4 pantolon = 12 kıyafet |
| Bijeksiyon Kuralı | Eğer f: A → B bir eşleştirme ise, |A| = |B| | İkili dizeleri sayarak alt kümeleri sayın |
| Tamamlayıcı | |A| = |U| − |Aᶜ| | "En az bir"i toplam eksi "yok" olarak sayın |
### Permütasyonlar ve Kombinasyonlar
| Gösterim | İsim | Formül | Anlamı |
|----------|------|-----------|---------|
| C(n, k) veya (n k) | Binom katsayısı | N! / (k!(n−k)!) | N sayıda öğeden k öğe seçmenin yolları (sıra önemli değil) |
| P(n, k) | n'nin k-permütasyonları | N! / (n−k)! | N'den k öğeyi düzenlemenin yolları (sıralama önemlidir) |
| N! | Faktöriyel | n × (n−1) × ... × 1 | Tüm n öğeyi düzenlemenin yolları |
| (n k) tekrarlı | Çoklu Seçim | C(n+k−1, k) | Tekrarlamaya izin verilen n arasından k'yi seçin |
**Binom Teoremi:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Pascal'ın Kimliği:** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Güvercin Deliği Prensibi
**Temel biçim:** n+1 nesne n kutuya yerleştirilirse en az bir kutuda ≥ 2 nesne bulunur.
**Genel biçim:** Eğer k kutuya N nesne yerleştirilirse, en az bir kutu ≥ ⌈N/k⌉ nesne içerir.
**Çalışılan Örnekler:**
1. Herhangi 13 kişiden en az 2'si aynı doğum ayını paylaşıyor. (13 kişi, 12 ay → güvercin yuvası.)
2. Herhangi bir 5 tam sayı arasında toplamı 3'e bölünebilen 3 sayının bulunduğunu gösterin.
   - Mod 3'teki kalıntıları göz önünde bulundurun: {0, 1, 2}. 5 tam sayı ve 3 kalıntı sınıfıyla, genelleştirilmiş güvercin deliğine göre, en az ⌈5/3⌉ = 2 bir kalıntıyı paylaşır.
   - Eğer 3 kişi bir r kalıntısını paylaşıyorsa: bunların toplamı ≡ 3r ≡ 0 (mod 3).
   - 2 kalıntı 0'ı ve 2 kalıntı 1'i paylaşıyorsa: her çiftten bir tane artı bir kalıntı-0 elemanı seçin → toplam ≡ 0 (mod 3).
3. **CS'deki uygulama:** Kayıpsız sıkıştırma algoritmalarının bazı girişleri genişletmesi gerekir. (Her n bitlik dize < n bit olarak sıkıştırılırsa, 2ⁿ dizeyi 2ⁿ'den daha az sıkıştırılmış dizeyle eşleştirirsiniz; bu da birebirliği ihlal eder.)
### Katalan Numaraları
n'inci **Katalan numarası** Cₙ = C(2n, n) / (n+1) şunları sayar:
| Yapı | Örnek |
|-----------|------------|
| Geçerli parantez dizileri | n = 2 için ()(), (()) |
| n dahili düğüme sahip ikili ağaçlar | n = 2 için 2 ağaç |
| Çaprazı geçmeyen yollar | (0,0)'dan (n,n)'ye kadar olan kılavuz yolları y = x |
| Çokgen üçgenlemeleri | (n+2)-gon'u üçgenlere bölmenin yolları |
İlk birkaçı: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Tekrarlanma: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Tekrarlama İlişkileri
**Yineleme ilişkisi** bir dizinin her terimini önceki terimlerin bir fonksiyonu olarak tanımlar.
### Türler ve Çözümler
| Tür | Formu | Çözüm Yöntemi |
|------|----------|------|
| Doğrusal homojen (sabit katsayı) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Karakteristik denklem |
| Doğrusal homojen olmayan | aₙ = c₁aₙ₋₁ + ... + f(n) | Özel çözüm + homojen çözüm |
| Böl ve fethet | T(n) = aT(n/b) + f(n) | Usta teoremi |
### Karakteristik Denklem Yöntemi
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ için karakteristik denklemi oluşturun:
r² - c₁r - c₂ = 0
| Durum | Kökler | Genel Çözüm |
|------|----------|-------|
| İki farklı reel kök r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Tekrarlanan kök r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Karmaşık kökler α ± βi | Polar'a dönüştür: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |
**Çalışılan Örnek:** Fibonacci dizisi Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Karakteristik denklem: r² − r − 1 = 0
- Kökler: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1,618, ψ = (1−√5)/2 ≈ −0,618
- Genel çözüm: Fₙ = A·φⁿ + B·ψⁿ
- Başlangıç koşullarından: A = 1/√5, B = −1/√5
- **Kapalı form:** Fₙ = (φⁿ − ψⁿ) / √5 (Binet formülü)
### Ana Teoremi
T(n) = aT(n/b) + f(n) formundaki yinelemeler için, burada a ≥ 1, b > 1:
c = log_b(a) olsun.
| Durum | Durum | Çözüm |
|------|---------------|----------|
| 1 | f(n) = O(nᵈ) burada d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c ve bazı k < 1 için af(n/b) ≤ kf(n) | T(n) = Θ(nᵈ) |
**Örnekler:**
- Birleştirme sıralaması: T(n) = 2T(n/2) + O(n). Burada a=2, b=2, c=1, f(n)=n=Θ(n¹). Durum 2: T(n) = Θ(n log n).
- İkili arama: T(n) = T(n/2) + O(1). Burada a=1, b=2, c=0, f(n)=1=Θ(n⁰). Durum 2: T(n) = Θ(log n).
---

## İşlev Oluşturma
Bir **üretme fonksiyonu**, bir (aₙ) dizisini resmi bir kuvvet serisinin katsayıları olarak kodlar.
### Türler
| Tür | Formu | Kullanım Örneği |
|------|----------|----------|
| Sıradan (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Etiketsiz yapılar, kompozisyonlar |
| Üstel (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Etiketli yapılar, permütasyonlar |
### Ortak Oluşturma İşlevleri
| Sıra aₙ | OGFG(x) |
|---------------|-----------|
| 1, 1, 1, 1,... | 1/(1−x) |
| 1, 2, 3, 4,... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| Sabit k için C(n,k) | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Katalanca Cₙ | (1 − √(1−4x)) / (2x) |
### Yinelemeleri Çözmek İçin Oluşturma İşlevlerini Kullanma
**Çalışılan Örnek:** aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3'ü çözün.
1. G(x) = Σ aₙxⁿ olsun.
2. Tekrardan: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Yerine koy: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Kısmi kesirler: G(x) = 2/(1−2x) − 1/(1−x)
7. Çıkarma katsayıları: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Doğrulama:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Kontrol edin: 3(3) − 2(1) = 7.
---

## Boole Cebiri ve Önermeler Mantığı
Boole cebiri iki doğruluk değerinin cebiridir: **Doğru (1)** ve **Yanlış (0)**. Dijital devrelerin, veritabanı sorgularının ve programlama koşullarının matematiksel temelidir.
### Operasyonlar ve Kanunlar
| Operasyon | Sembol | Anlamı | Doğruluk Tablosu |
|-----------|-----------|------------|------------|
| VE | p ∧q | Yalnızca her ikisi de doğru olduğunda doğrudur | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| VEYA | p ∨q | En az biri doğru olduğunda doğrudur | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| DEĞİL | ¬p | Olumsuzluk | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Tam olarak biri doğru olduğunda doğrudur | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| İMA EDİYOR | p → q | Yalnızca p=T ve q=F olduğunda yanlıştır | T→T=T, T→F=F, F→T=T, F→F=T |
| İKİ KOŞULLU | p ↔q | Her ikisi de aynı değere sahip olduğunda doğru | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Anahtar Boole Kimlikleri
| Hukuk | Formül |
|-----|----------|
| Değişebilirlik | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| İlişkisellik | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Dağıtıcılık | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| De Morgan Kanunları | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Çift Olumsuzluk | ¬(¬p) = p |
| İdempotans | p ∧ p = p; p ∨ p = p |
| Emilim | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Karşıt pozitif | (p → q) ≡ (¬q → ¬p) |
### Normal Formlar
| Formu | Yapı | Kullanım Örneği |
|------|---------------|----------|
| Birleşik Normal Form (CNF) | OR'lerin VE'si: (A∨B) ∧ (C∨D) | SAT çözücüler, çözünürlük teoreminin kanıtlanması |
| Ayırıcı Normal Form (DNF) | VE'lerin VEYA'sı: (A∧B) ∨ (C∧D) | Devre tasarımı, kural tabanlı sistemler |
**CNF'ye dönüştürme:** De Morgan yasalarını uygulayın, VEYA'yı VE üzerinden dağıtın, çift olumsuzlamayı ortadan kaldırın.
---

## Modüler Aritmetik ve Kongrüanslar
Modüler aritmetik, tamsayıları "bölmeden sonra kalan" işlemi altında inceler. Kriptografi, karma ve sayı teorisi için gereklidir.
### Temel Tanımlar
| Konsept | Gösterim | Tanımı |
|-----------|----------|-----------|
| Uyumluluk | a ≡ b (mod n) | n böler (a − b) |
| Kalıntı sınıfı | [a]ₙ | {a + kn : k ∈ ℤ} kümesi |
| Modüler ters | a⁻¹ mod n | ax ≡ 1 (mod n) olacak şekilde x değeri |
| Euler'in sabırlısı | φ(n) | {1,...,n} eş asalından n'ye kadar olan tamsayıların sayısı |
### Anahtar Özellikler
| Emlak | Açıklama |
|----------|----------|
| İlave | a ≡ b ve c ≡ d (mod n) ise a+c ≡ b+d (mod n) |
| Çarpma | a ≡ b ve c ≡ d (mod n) ise ac ≡ bd (mod n) |
| Fermat'ın Küçük Teoremi | Eğer p asalsa ve gcd(a,p) = 1 ise aᵖ⁻¹ ≡ 1 (mod p) |
| Euler Teoremi | Eğer gcd(a,n) = 1 ise, a^φ(n) ≡ 1 (mod n) |
| Çin Kalan Teoremi | Eğer gcd(m,n) = 1 ise, x ≡ a (mod m), x ≡ b (mod n) sisteminin benzersiz bir çözümü vardır mod mn |
### Euler Totient'inin Hesaplanması
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (asal çarpanlara ayırma) için:
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Örnek:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Aslında, {1, 5, 7, 11}, 12 ile aralarında asaldır.
### Uygulama: RSA Şifrelemesi (Genel Bakış)
1. Büyük p, q asal sayılarını seçin. n = pq, φ(n) = (p−1)(q−1)'i hesaplayın.
2. e'yi gcd(e, φ(n)) = 1 (genel üs) olacak şekilde seçin.
3. d ≡ e⁻¹ (mod φ(n)) (özel üs) değerini hesaplayın.
4. Şifrele: c = mᵉ mod n. Şifre çözme: m = cᵈ mod n.
5. Güvenlik, p ve q'yu bulmak için n'yi çarpanlarına ayırmanın zorluğuna dayanır.
---

## Matematiksel Tümevarım
**Matematiksel tümevarım** tüm doğal sayılarla ilgili ifadeler için birincil ispat tekniğidir.
### Tümevarım Yoluyla İspatın Yapısı
1. **Temel durum:** n = 0 (veya n = 1) için ifadeyi kanıtlayın.
2. **Tümevarım adımı:** İfadenin n = k (tümevarım hipotezi) için geçerli olduğunu varsayalım, ardından bunu n = k + 1 için kanıtlayın.
### Çeşitleri
| Varyant | Ne Zaman Kullanılmalı |
|-----------|------------|
| Basit indüksiyon | P(k) → P(k+1)'in ispatı |
| Güçlü indüksiyon | P(k+1)'i kanıtlamak için P(0), P(1), ..., P(k)'yi varsayalım |
| Yapısal indüksiyon | Özyinelemeli olarak tanımlanmış yapıların (ağaçlar, formüller) özelliklerini kanıtlayın |
| Sonlu ötesi indüksiyon | Tümevarımı iyi sıralanmış kümeleri ℕ'nin ötesine taşıyacak şekilde genişletin |
**Çalışılmış Örnek (Güçlü Tümevarım):** Her n ≥ 2 tamsayısının asal sayıların çarpımı olarak yazılabileceğini kanıtlayın.
- Taban: n = 2 asaldır, yani asal sayıların (kendisinin) çarpımıdır.
- Tümevarım adımı: 2'den k'ye kadar tüm tamsayılar için doğru olduğunu varsayalım. k+1'i düşünün.
  - Eğer k+1 asal ise tamamdır.
  - Eğer k+1 bileşik ise k+1 = ab, burada 2 ≤ a, b ≤ k. Tümevarım hipotezine göre, hem a hem de b asal sayıların çarpımıdır, yani k+1 asal sayıların çarpımıdır.
---

## Makine Öğrenimi ve Veri Bilimiyle İlgi
| Ayrık Matematik Kavramı | ML / Veri Biliminde Uygulama |
|--------------------------|-------------------------------------|
| Küme teorisi | Veritabanı işlemleri (SQL JOIN'ler), özellik seti manipülasyonu, olasılık olayları |
| İlişkiler | Veritabanı şemaları, varlık-ilişki modellemesi, bilgi grafikleri |
| İşlevler | Aktivasyon fonksiyonları, özellik dönüşümleri, alanlar arası eşlemeler |
| Kombinatorik | Özellik seçimi (n'den k'yi seçme), hiperparametre ızgarası arama boyutlandırma |
| Güvercin deliği ilkesi | Hashing çarpışmaları, sıkıştırmanın alt sınırları, bilgi teorisi kanıtları |
| Yinelenme ilişkileri | Dinamik programlama, algoritma karmaşıklığı analizi, zaman serisi modelleri |
| Fonksiyonlar oluşturuluyor | Olasılık üreten fonksiyonlar, özellik mühendisliğinde kombinatoryal problemlerin çözümü |
| Katalan numaraları | Ağaç yapılarını sayma (karar ağaçları), ifadeleri ayrıştırma, yığın işlemleri |
| Grafik teorisi (sonraki dosyaya bakın) | Sosyal ağ analizi, öneri sistemleri, bilgi temsili |
---

## Özet
| Konu | Temel Fikir | Anahtar Aracı |
|----------|---------------|----------|
| Küme Teorisi | Farklı nesne koleksiyonları | ZFC aksiyomları, önem derecesi, işlemler |
| İlişkiler | Elemanlar arasındaki bağlantılar | Denklik bağıntıları, kısmi sıralar |
| İşlevler | Kümeler arası eşlemeler | Enjektivite, surjektivite, bijeksiyon |
| Kombinatorik | Sayma düzenlemeleri | Binom katsayıları, güvercin yuvası ilkesi |
| Yinelenme İlişkileri | Yinelemeli olarak tanımlanan diziler | Karakteristik denklemler, Master teoremi |
| Fonksiyonlar Oluşturma | Kuvvet serisi olarak diziler | OGF/EGF, yinelemeleri cebirsel olarak çözme |
Ayrık matematik, sonlu veya sayılabilir yapılar hakkında akıl yürütmeye yönelik dili ve araçları sağlar; bilgisayarların manipüle ettiği şey de tam olarak budur. Her algoritma, veri yapısı, veritabanı sorgusu ve şifreleme protokolü ayrı temellere dayanır. Bu konulara hakim olmak, problem çözme yeteneğini geliştirir ve algoritmalar, karmaşıklık teorisi ve makine öğrenimi konularında ileri düzey çalışmalar için kelime bilgisi sağlar.