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

# Discrete Mathematics
Ang discrete mathematics ay ang pag-aaral ng mathematical structures na sa panimula ay mabibilang o pinaghihiwalay — kumpara sa tuloy-tuloy na matematika (calculus, real analysis), na tumatalakay sa makinis, walang patid na dami. Ang discrete math ay sumasailalim sa computer science, cryptography, disenyo ng algorithm, at mga istruktura ng data. Kung ang tuluy-tuloy na matematika ay naglalarawan sa pisikal na mundo, ang discrete math ay naglalarawan sa computational na mundo.
---

## Itakda ang Teorya sa Lalim
Ang mga set ay ang pundasyon kung saan halos lahat ng modernong matematika ay binuo. Ang **set** ay isang hindi nakaayos na koleksyon ng mga natatanging bagay, na tinatawag na **mga elemento** o **mga miyembro**.
### Axiomatic Foundations (ZFC)
Ang modernong set theory ay nakasalalay sa **Zermelo-Fraenkel axioms na may Axiom of Choice (ZFC)**. Niresolba ng mga axiom na ito ang mga kabalintunaan tulad ng Russell's Paradox ("ang set ng lahat ng set na hindi naglalaman ng kanilang mga sarili") sa pamamagitan ng paghihigpit kung paano mabubuo ang mga set.
| Axiom | Impormal na Pahayag |
|-------|--------------------|
| Extensionity | Dalawang set ay pantay-pantay kung mayroon silang parehong mga elemento |
| Empty Set | Mayroong isang set na walang elemento: ∅ |
| Pagpares | Para sa anumang a, b, mayroong {a, b} |
| Unyon | Para sa anumang pamilya ng mga set, umiiral ang kanilang unyon |
| Power Set | Para sa anumang set S, ang set ng lahat ng subset ng S ay umiiral: P(S) |
| Infinity | Mayroong isang walang katapusang set |
| Pagtutukoy | Para sa anumang set A at property P, umiiral ang {x ∈ A : P(x)} |
| Pagpapalit | Ang imahe ng isang set sa ilalim ng isang definable function ay isang set |
| Regularidad | Ang bawat hanay na hindi walang laman ay naglalaman ng elementong magkahiwalay mula dito (pinipigilan ang pagiging miyembro ng sarili) |
| Pagpipilian | Para sa anumang pamilya ng hindi walang laman na pairwise disjoint set, mayroong isang pagpipiliang function |
### Cardinality at Sukat ng Mga Set
Ang **cardinality** ng isang set, na may kahulugang |S|, ay sumusukat sa "laki" nito.
| Konsepto | Kahulugan | Halimbawa |
|---------|------------|---------|
| May hangganan na hanay | May natural na numero bilang cardinality | |{a, b, c}| = 3 |
| Mabibilang na walang hanggan | Parehong cardinality bilang ℕ | ℤ, ℚ ay mabibilang na walang hanggan |
| Hindi mabilang | Mas malaki sa ℕ | ℝ, P(ℕ), ang set ng lahat ng function ℕ → {0,1} |
| Cantor's Theorem | Para sa anumang set S, |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**Ang diagonal na argumento ng Cantor** ay nagpapatunay na ang ℝ ay hindi mabilang: ipagpalagay na maaari mong ilista ang lahat ng real sa [0,1], pagkatapos ay bumuo ng isang bagong real na naiiba sa ika-na nakalistang real sa ika-n decimal na lugar — kontradiksyon.
### Mga Operasyon sa Mga Set
| Operasyon | Notasyon | Kahulugan | Ari-arian |
|-----------|----------|------------|----------|
| Unyon | A ∪ B | {x : x ∈ A o x ∈ B} | Commutative, associative |
| Intersection | A ∩ B | {x : x ∈ A at x ∈ B} | Commutative, associative |
| Pagkakaiba | A \ B | {x : x ∈ A at x ∉ B} | Hindi commutative |
| Symmetric na Pagkakaiba | A △ B | (A \ B) ∪ (B \ A) | Commutative, associative |
| Komplemento | Aᶜ | U \ A (kung saan ang U ay unibersal na set) | (Aᶜ)ᶜ = A |
| Produktong Cartesian | A × B | {(a,b): a ∈ A, b ∈ B} | |A × B| = |A| · |B| |
**Mga Batas ni De Morgan:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Prinsipyo ng Pagsasama-Pagbubukod** (para sa mga may hangganang hanay):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## Relasyon
Ang **relasyon** R sa set A at B ay isang subset ng A × B. Kapag (a, b) ∈ R, isinusulat namin ang aRb.
### Mga Uri ng Relasyon
Ang isang ugnayang R sa isang set A ay maaaring magkaroon ng mga katangiang ito:
| Ari-arian | Kahulugan | Halimbawa |
|----------|------------|---------|
| Reflexive | ∀a ∈ A: aRa | ≤ sa ℤ |
| Irreflexive | ∀a ∈ A: ¬(aRa) | < sa ℤ |
| Symmetric | ∀a,b: aRb → bRa | = sa anumang hanay |
| Antisymmetric | ∀a,b: aRb ∧ bRa → a = b | ≤ sa ℤ |
| Palipat | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = sa ℤ |
### Mga Relasyon sa Pagkakatumbas
Ang **kaugnay na katumbas** ay reflexive, simetriko, at transitive. Hinahati nito ang isang set sa magkahiwalay na **mga equivalence classes**.
**Halimbawa:** Modular arithmetic. Tukuyin ang a ~ b iff a ≡ b (mod n). Ang mga equivalence classes ay [0], [1], ..., [n−1], na naghahati ng ℤ sa n classes.
**Nagtrabaho Halimbawa:** Sa ℤ × ℤ, tukuyin ang (a,b) ~ (c,d) kung a + d = b + c. Ito ay isang equivalence relation. Ang klase [(0,0)] = {(n,n) : n ∈ ℤ}. Ang klase [(1,0)] = {(n+1,n) : n ∈ ℤ}. Ang konstruksiyon na ito ay aktwal na tumutukoy sa mga integer mula sa mga natural na numero.
### Mga Bahagyang Order
Ang isang **partial order** ay reflexive, antisymmetric, at transitive. Ang isang set na may partial order ay tinatawag na isang **partially ordered set (poset)**.
| Konsepto | Kahulugan | Halimbawa |
|---------|------------|---------|
| Poset | (S, ≤) na may ≤ isang bahagyang order | (P(A), ⊆) — mga subset na inayos ayon sa pagsasama |
| Kadena | Isang ganap na inutusang subset | {∅, {a}, {a,b}} sa P({a,b,c}) |
| Antichain | Isang subset kung saan walang dalawang elemento ang maihahambing | {{a}, {b}} sa P({a,b}) |
| Hasse Diagram | Visual na representasyon ng isang poset | Gumuhit ng mga gilid para lamang sa pagsakop ng mga relasyon |
| Upper Bound | Isang elemento ≥ bawat elemento sa isang subset | sup({2,3}) = 6 in (ℤ, \|) (divisibility) |
| Least Upper Bound (sup) | Pinakamaliit na upper bound | sup({2,3}) sa (ℕ, ≤) ay 3 |
| Pinakamahusay na Lower Bound (inf) | Pinakamalaking lower bound | inf({4,6}) sa (ℕ, \|) ay 2 |
---

## Mga Pag-andar
A **function** f: Ang A → B ay nagtatalaga sa bawat elemento ng A ng eksaktong isang elemento ng B.
### Pag-uuri ng Mga Pag-andar
| Uri | Kahulugan | Halimbawa |
|------|------------|---------|
| Pantukoy (isa-sa-isa) | f(a) = f(b) → a = b | f(x) = 2x mula sa ℤ → ℤ |
| Surjective (papunta) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2 mula sa ℤ → {0,1} |
| Bijective | Parehong injective at surjective | f(x) = x + 1 mula sa ℤ → ℤ |
### Mga Konsepto ng Mahalagang Function
| Konsepto | Kahulugan | Use Case |
|---------|------------|----------|
| Baliktad na function | Umiiral ang f⁻¹ kung ang f ay bijective | Pagde-decrypt ng naka-encrypt na data |
| Komposisyon | (g ∘ f)(x) = g(f(x)) | Pagkakadena ng mga pagbabago |
| Pag-andar ng pagkakakilanlan | id(x) = x | Neutral na elemento para sa komposisyon |
| Nakapirming punto | f(x) = x | Mga recursive na kahulugan, semantika |
| Permutasyon | Isang bijection mula sa isang set patungo sa sarili nito | Muling pag-aayos ng data, pag-shuffling |
### Nagbibilang ng Mga Function
Ibinigay na may hangganan na hanay |A| = m at |B| = n:
| Uri | Bilangin |
|------|-------|
| Lahat ng mga function A → B | nᵐ |
| Mga pag-andar ng injective | n! / (n−m)! (kung n ≥ m, iba pa 0) |
| Surjective function | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (sa pamamagitan ng pagsasama-pagbubukod) |
| Bijective function | n! (kapag m = n) |
---

## Kombinatorika
Ang Combinatorics ay ang matematika ng pagbibilang, pag-aayos, at pagpili.
### Mga Pangunahing Prinsipyo sa Pagbilang
| Prinsipyo | Pahayag | Halimbawa |
|-----------|-----------|---------|
| Panuntunan ng Sum | Kung ang A at B ay magkahiwalay, |A ∪ B| = |A| + |B| | Pagpili ng prutas: 3 mansanas + 4 na dalandan = 7 pagpipilian |
| Panuntunan ng Produkto | |A × B| = |A| · |B| | Outfit: 3 shirt × 4 na pantalon = 12 outfit |
| Panuntunan ng Bijection | Kung ang f: A → B ay isang bijection, |A| = |B| | Bilangin ang mga subset sa pamamagitan ng pagbibilang ng mga binary string |
| Komplemento | |A| = |U| − |Aᶜ| | Bilangin ang "kahit isa" bilang kabuuang minus "wala" |
### Mga Permutasyon at Kumbinasyon
| Notasyon | Pangalan | Formula | Ibig sabihin |
|----------|------|---------|---------|
| C(n, k) o (n k) | Binomial coefficient | n! / (k!(n−k)!) | Mga paraan upang pumili ng k aytem mula sa n (hindi mahalaga ang pagkakasunod-sunod) |
| P(n, k) | k-permutations ng n | n! / (n−k)! | Mga paraan upang ayusin ang k aytem mula sa n (order matters) |
| n! | Factorial | n × (n−1) × ... × 1 | Mga paraan upang ayusin ang lahat ng n aytem |
| (n k) na may pag-uulit | Multichoose | C(n+k−1, k) | Pumili ng k mula sa n na may pinapayagang pag-uulit |
**Binomial Theorem:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Pagkakakilanlan ni Pascal:** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Ang Prinsipyo ng Pigeonhole
**Basic form:** Kung ang n+1 na mga bagay ay inilagay sa n mga kahon, hindi bababa sa isang kahon ang naglalaman ng ≥ 2 mga bagay.
**Pangkalahatang anyo:** Kung ang N bagay ay inilagay sa k kahon, kahit isang kahon ay naglalaman ng ≥ ⌈N/k⌉ bagay.
**Mga Nagtrabahong Halimbawa:**
1. Sa alinmang 13 tao, hindi bababa sa 2 ang nakikibahagi sa isang buwan ng kapanganakan. (13 tao, 12 buwan → pigeonhole.)
2. Ipakita na sa alinmang 5 integer, mayroong 3 na ang kabuuan ay nahahati sa 3.
   - Isaalang-alang ang mga residue mod 3: {0, 1, 2}. Sa 5 integer at 3 nalalabi na klase, sa pamamagitan ng pangkalahatang pigeonhole, hindi bababa sa ⌈5/3⌉ = 2 ang nagbabahagi ng nalalabi.
   - Kung ang 3 ay nagbahagi ng nalalabi r: ang kanilang kabuuan ≡ 3r ≡ 0 (mod 3).
   - Kung ang 2 ay nagbabahagi ng residue 0 at 2 ay nagbabahagi ng residue 1: pumili ng isa mula sa bawat pares kasama ang residue-0 na elemento → sum ≡ 0 (mod 3).
3. **Application sa CS:** Ang anumang lossless compression algorithm ay dapat magpalawak ng ilang input. (Kung ang bawat n-bit string ay naka-compress sa < n bits, imamapa mo ang 2ⁿ string sa mas kaunti sa 2ⁿ compressed string — lumalabag sa injectivity.)
### Mga Numero ng Catalan
Ang ika-n **Catalan number** Cₙ = C(2n, n) / (n+1) ay binibilang:
| Istraktura | Halimbawa |
|-----------|---------|
| Mga wastong pagkakasunud-sunod ng panaklong | ()(), (()) para sa n = 2 |
| Binary tree na may n panloob na node | 2 puno para sa n = 2 |
| Mga landas na hindi tumatawid sa dayagonal | Mga grid path mula sa (0,0) hanggang (n,n) na nananatili sa ibaba ng y = x |
| Triangulations ng isang polygon | Mga paraan upang hatiin ang isang (n+2)-gon sa mga tatsulok |
Unang ilang: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Pag-ulit: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Paulit-ulit na Relasyon
Ang **recurrence relation** ay tumutukoy sa bawat termino ng isang sequence bilang isang function ng mga naunang termino.
### Mga Uri at Solusyon
| Uri | Form | Paraan ng Solusyon |
|------|------|-----------------|
| Linear homogenous (constant coeff.) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Katangiang equation |
| Linear na hindi homogenous | aₙ = c₁aₙ₋₁ + ... + f(n) | Partikular na solusyon + homogenous na solusyon |
| Hatiin at lupigin | T(n) = aT(n/b) + f(n) | Master theorem |
### Paraan ng Equation na Katangian
Para sa aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, bumuo ng katangiang equation:
r² − c₁r − c₂ = 0
| Kaso | Mga ugat | Pangkalahatang Solusyon |
|------|-------|------------------|
| Dalawang magkaibang tunay na ugat r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Paulit-ulit na ugat r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Mga kumplikadong ugat α ± βi | I-convert sa polar: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |
**Nagtrabahong Halimbawa:** Fibonacci sequence Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Katangiang equation: r² − r − 1 = 0
- Mga Roots: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1.618, ψ = (1−√5)/2 ≈ −0.618
- Pangkalahatang solusyon: Fₙ = A·φⁿ + B·ψⁿ
- Mula sa mga unang kundisyon: A = 1/√5, B = −1/√5
- **Saradong form:** Fₙ = (φⁿ − ψⁿ) / √5 (Binet's formula)
### Ang Master Theorem
Para sa mga pag-ulit ng anyong T(n) = aT(n/b) + f(n) kung saan ang a ≥ 1, b > 1:
Hayaan c = log_b(a).
| Kaso | Kundisyon | Solusyon |
|------|-----------|----------|
| 1 | f(n) = O(nᵈ) kung saan d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c, at af(n/b) ≤ kf(n) para sa ilang k < 1 | T(n) = Θ(nᵈ) |
**Mga Halimbawa:**
- Pagsamahin ang pag-uuri: T(n) = 2T(n/2) + O(n). Dito a=2, b=2, c=1, f(n)=n=Θ(n¹). Case 2: T(n) = Θ(n log n).
- Binary na paghahanap: T(n) = T(n/2) + O(1). Dito a=1, b=2, c=0, f(n)=1=Θ(n⁰). Case 2: T(n) = Θ(log n).
---

## Pagbuo ng Mga Function
Ang **generating function** ay nag-encode ng isang sequence (aₙ) bilang coefficients ng isang pormal na power series.
### Mga uri
| Uri | Form | Use Case |
|------|------|----------|
| Ordinaryo (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Mga istrukturang walang label, komposisyon |
| Exponential (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Mga istrukturang may label, permutasyon |
### Mga Karaniwang Paggawa ng Function
| Sequence aₙ | OGF G(x) |
|-------------|-----------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) para sa fixed k | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Catalan Cₙ | (1 − √(1−4x)) / (2x) |
### Paggamit ng Mga Pagbuo ng Function para Malutas ang Mga Pag-uulit
**Nagtrabaho Halimbawa:** Lutasin ang aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Hayaan ang G(x) = Σ aₙxⁿ.
2. Mula sa pag-ulit: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Palitan: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Mga partial fraction: G(x) = 2/(1−2x) − 1/(1−x)
7. Extract coefficients: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Pagpapatunay:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Suriin: 3(3) − 2(1) = 7.
---

## Boolean Algebra at Propositional Logic
Ang Boolean algebra ay ang algebra ng dalawang truth value: **True (1)** at **False (0)**. Ito ang mathematical na pundasyon ng mga digital circuit, database query, at programming condition.
### Mga Operasyon at Batas
| Operasyon | Simbolo | Ibig sabihin | Talahanayan ng Katotohanan |
|-----------|--------|---------|-------------|
| AT | p ∧ q | Tama lamang kapag pareho ang totoo | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| O | p ∨ q | Tama kapag kahit isa ay totoo | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| HINDI | ¬p | Negasyon | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Tama kapag eksaktong isa ang totoo | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| NAGPAPAHAYAG | p → q | Mali lamang kapag p=T at q=F | T→T=T, T→F=F, F→T=T, F→F=T |
| BICONDITIONAL | p ↔ q | Tama kapag pareho ang halaga | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Mga Pangunahing Pagkakakilanlan ng Boolean
| Batas | Formula |
|-----|--------|
| Commutativity | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Pagkakaisa | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Distributivity | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| Mga Batas ni De Morgan | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Dobleng Negasyon | ¬(¬p) = p |
| Idepotence | p ∧ p = p; p ∨ p = p |
| Pagsipsip | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Contrapositive | (p → q) ≡ (¬q → ¬p) |
### Mga Normal na Form
| Form | Istraktura | Use Case |
|------|-----------|----------|
| Conjunctive Normal Form (CNF) | AT ng mga OR: (A∨B) ∧ (C∨D) | SAT solvers, resolution theorem na nagpapatunay |
| Disjunctive Normal Form (DNF) | O ng mga AND: (A∧B) ∨ (C∧D) | Disenyo ng circuit, mga sistemang nakabatay sa panuntunan |
**Pagko-convert sa CNF:** Ilapat ang mga batas ni De Morgan, ipamahagi O higit sa AT, alisin ang dobleng negasyon.
---

## Modular Arithmetic at Congruences
Modular arithmetic studies integers sa ilalim ng operasyon ng "natitira pagkatapos ng dibisyon." Ito ay mahalaga para sa cryptography, hashing, at teorya ng numero.
### Mga Pangunahing Kahulugan
| Konsepto | Notasyon | Kahulugan |
|---------|----------|------------|
| Pagkakatugma | a ≡ b (mod n) | n divides (a − b) |
| Natitirang klase | [a]ₙ | Ang set {a + kn : k ∈ ℤ} |
| Modular inverse | a⁻¹ mod n | Halaga x tulad ng ax ≡ 1 (mod n) |
| Totient ni Euler | φ(n) | Bilang ng mga integer sa {1,...,n} coprime sa n |
### Mga Pangunahing Katangian
| Ari-arian | Pahayag |
|----------|----------|
| Dagdag | Kung a ≡ b at c ≡ d (mod n), pagkatapos ay a+c ≡ b+d (mod n) |
| Multiplikasyon | Kung a ≡ b at c ≡ d (mod n), pagkatapos ay ac ≡ bd (mod n) |
| Ang Little Theorem ni Fermat | Kung ang p ay prime at gcd(a,p) = 1, pagkatapos ay aᵖ⁻¹ ≡ 1 (mod p) |
| Teorama ni Euler | Kung gcd(a,n) = 1, a^φ(n) ≡ 1 (mod n) |
| Chinese Remainder Theorem | Kung gcd(m,n) = 1, ang sistema x ≡ a (mod m), x ≡ b (mod n) ay may natatanging solusyon mod mn |
### Pag-compute ng Totient ni Euler
Para sa n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (prime factorization):
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Halimbawa:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Sa katunayan, ang {1, 5, 7, 11} ay coprime sa 12.
### Application: RSA Cryptography (Pangkalahatang-ideya)
1. Pumili ng malalaking prime p, q. Compute n = pq, φ(n) = (p−1)(q−1).
2. Piliin ang e na gcd(e, φ(n)) = 1 (public exponent).
3. Compute d ≡ e⁻¹ (mod φ(n)) (pribadong exponent).
4. I-encrypt: c = mᵉ mod n. I-decrypt: m = cᵈ mod n.
5. Ang seguridad ay umaasa sa hirap ng factoring n upang mahanap ang p at q.
---

## Mathematical Induction
**Mathematical induction** ay ang pangunahing pamamaraan ng patunay para sa mga pahayag tungkol sa lahat ng natural na numero.
### Istraktura ng isang Patunay sa pamamagitan ng Induction
1. **Base case:** Patunayan ang pahayag para sa n = 0 (o n = 1).
2. **Inductive step:** Ipagpalagay na ang pahayag ay para sa n = k (inductive hypothesis), pagkatapos ay patunayan ito para sa n = k + 1.
### Mga variant
| Variant | Kailan Gagamitin |
|---------|-------------|
| Simpleng induction | Patunayan ang P(k) → P(k+1) |
| Malakas na induction | Ipagpalagay na P(0), P(1), ..., P(k) upang patunayan ang P(k+1) |
| Structural induction | Patunayan ang mga katangian ng recursively tinukoy na mga istraktura (mga puno, mga formula) |
| Transfinite induction | I-extend ang induction sa maayos na mga set na lampas sa ℕ |
**Worked Example (Strong Induction):** Patunayan ang bawat integer n ≥ 2 ay maaaring isulat bilang isang produkto ng primes.
- Base: n = 2 ay prime, kaya ito ay produkto ng primes (mismo).
- Inductive na hakbang: Ipagpalagay na totoo para sa lahat ng integer mula 2 hanggang k. Isaalang-alang ang k+1.
  - Kung ang k+1 ay prime, tapos na.
  - Kung ang k+1 ay composite, k+1 = ab kung saan 2 ≤ a, b ≤ k. Sa pamamagitan ng inductive hypothesis, ang parehong a at b ay mga produkto ng primes, kaya ang k+1 ay isang produkto ng primes.
---

## Kaugnayan sa Machine Learning at Data Science
| Discrete Math Concept | Application sa ML / Data Science |
|-------------------------------------|------------------------------------------------|
| Itakda ang teorya | Mga pagpapatakbo ng database (SQL JOINs), pagmamanipula ng set ng tampok, mga kaganapan sa posibilidad |
| Relasyon | Mga schema ng database, pagmomodelo ng entity-relasyon, mga graph ng kaalaman |
| Mga Pag-andar | Mga function ng pag-activate, pagbabago ng tampok, pagmamapa sa pagitan ng mga puwang |
| Kombinatorika | Pagpili ng tampok (pagpili ng k mula sa n), pagsukat ng paghahanap ng hyperparameter grid |
| Prinsipyo ng pigeonhole | Hashing collisions, lower bounds sa compression, information theory proofs |
| Paulit-ulit na relasyon | Dynamic na programming, pagsusuri sa pagiging kumplikado ng algorithm, mga modelo ng serye ng oras |
| Pagbuo ng mga function | Mga function sa pagbuo ng probabilidad, paglutas ng mga problemang kombinatoryal sa feature engineering |
| Mga numero ng Catalan | Nagbibilang ng mga istruktura ng puno (mga puno ng desisyon), mga expression sa pag-parse, mga pagpapatakbo ng stack |
| Teorya ng graph (tingnan ang susunod na file) | Pagsusuri sa social network, mga sistema ng rekomendasyon, representasyon ng kaalaman |
---

## Buod
| Paksa | Pangunahing Ideya | Key Tool |
|-------|-----------|----------|
| Itakda ang Teorya | Mga koleksyon ng mga natatanging bagay | ZFC axioms, cardinality, operations |
| Relasyon | Mga koneksyon sa pagitan ng mga elemento | Mga ugnayang katumbas, bahagyang mga order |
| Mga Pag-andar | Mga pagmamapa sa pagitan ng mga hanay | Injectivity, surjectivity, bijection |
| Kombinatorika | Pagbibilang ng mga kaayusan | Binomial coefficients, prinsipyo ng pigeonhole |
| Paulit-ulit na Relasyon | Recursively tinukoy ang mga pagkakasunud-sunod | Mga katangiang equation, Master theorem |
| Pagbuo ng Mga Function | Mga pagkakasunud-sunod bilang power series | OGF/EGF, paglutas ng mga pag-ulit sa algebraically |
Ang discrete mathematics ay nagbibigay ng wika at mga tool para sa pangangatwiran tungkol sa may hangganan o mabibilang na mga istruktura — na kung ano mismo ang minamanipula ng mga computer. Ang bawat algorithm, istraktura ng data, query sa database, at cryptographic protocol ay nakasalalay sa mga hiwalay na pundasyon. Ang karunungan sa mga paksang ito ay nagpapatalas ng kakayahan sa paglutas ng problema at nagbibigay ng bokabularyo para sa advanced na pag-aaral sa mga algorithm, complexity theory, at machine learning.