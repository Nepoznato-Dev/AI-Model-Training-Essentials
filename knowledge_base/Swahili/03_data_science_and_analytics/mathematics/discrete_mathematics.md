<!--
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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
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

-->
# Hisabati Mbalimbali
Hisabati mahususi ni utafiti wa miundo ya hisabati ambayo kimsingi inaweza kuhesabika au kutenganishwa - kinyume na hesabu endelevu (calculus, uchanganuzi halisi), ambayo inahusika na idadi laini, isiyovunjika. Hisabati mahususi hutegemeza sayansi ya kompyuta, kriptografia, muundo wa algoriti, na miundo ya data. Ikiwa hesabu inayoendelea inaelezea ulimwengu halisi, hesabu ya kipekee inaelezea ulimwengu wa hesabu.
---

## Weka Nadharia kwa Kina
Seti ndio msingi ambao karibu hisabati zote za kisasa hujengwa. **seti** ni mkusanyiko usio na mpangilio wa vitu tofauti, vinavyoitwa **vipengele** au **wanachama**.
### Misingi ya Axiomatic (ZFC)
Nadharia ya seti ya kisasa inaegemea kwenye **Miashirio ya Zermelo-Frankel yenye Axiom of Choice (ZFC)**. Mihimili hii hutatua vitendawili kama vile Kitendawili cha Russell ("seti ya seti zote ambazo hazina zenyewe") kwa kuzuia jinsi seti zinavyoweza kuundwa.
| Axiom | Taarifa Isiyo Rasmi |
|-------|--------------------|
| Ugani | Seti mbili ni sawa ikiwa zina vipengele sawa |
| Seti Tupu | Kuna seti isiyo na vipengele: ∅ |
| Kuoanisha | Kwa yoyote a, b, kuna {a, b} |
| Muungano | Kwa familia yoyote ya seti, muungano wao upo |
| Seti ya Nguvu | Kwa seti yoyote ya S, seti ya vikundi vidogo vyote vya S ipo: P(S) |
| Infinity | Kuna seti isiyo na kikomo |
| Maelezo | Kwa seti yoyote A na sifa P, {x ∈ A : P(x)} ipo |
| Uingizwaji | Picha ya seti chini ya chaguo za kukokotoa inayoweza kufafanuliwa ni seti |
| Kawaida | Kila seti isiyo tupu ina kipengele kitenganishi kutoka kwayo (huzuia uanachama binafsi) |
| Chaguo | Kwa familia yoyote ya seti zisizo tupu za viunganishi vya jozi, chaguo la kukokotoa lipo |
### Kardinali na Ukubwa wa Seti
**Kadinali** ya seti, inayoashiria |S|, hupima "ukubwa" wake.
| Dhana | Ufafanuzi | Mfano |
|---------|------------|----------|
| Seti kamili | Ina nambari asilia kama kadinali | |{a, b, c}| = 3 |
| Isiyo na kikomo | Kardinali sawa na ℕ | ℤ, ℚ hazina kikomo |
| Isiyohesabika | Kubwa kuliko ℕ | ℝ, P(ℕ), seti ya vitendakazi vyote ℕ → {0,1} |
| Nadharia ya Cantor | Kwa seti yoyote S, |P(S)| >> |S| | |P(ℕ)| > |ℕ| |
**Hoja ya mshazari ya Cantor** inathibitisha kwamba ℝ haiwezi kuhesabika: chukulia kuwa unaweza kuorodhesha halisi zote katika [0,1], kisha utengeneze halisi mpya ambayo inatofautiana na halisi iliyoorodheshwa ya nth katika nafasi ya nambari ya desimali - ukinzani.
### Uendeshaji kwenye Seti
| Operesheni | Nukuu | Ufafanuzi | Mali |
|-----------|-----------------------|-----------|
| Muungano | A ∪ B | {x : x ∈ A au x ∈ B} | Inabadilika, ya ushirika |
| Makutano | A ∩ B | {x : x ∈ A na x ∈ B} | Inabadilika, ya ushirika |
| Tofauti | A \ B | {x : x ∈ A na x ∉ B} | Sio ya kubadilisha |
| Tofauti ya Ulinganifu | A △ B | (A \ B) ∪ (B \ A) | Inabadilika, ya ushirika |
| Kukamilisha | Aᶜ | U \ A (ambapo U ni seti ya ulimwengu wote) | (Aᶜ)ᶜ = A |
| Bidhaa ya Cartesian | A × B | {(a,b) : a ∈ A, b ∈ B} | |A × B| = |A| · |B| |
**Sheria za De Morgan:**
- (A ∪ B) ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B) ᶜ = Aᶜ ∪ Bᶜ
**Kanuni ya Kujumuisha-Kutengwa** (kwa seti zenye ukomo):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

##Mahusiano
**uhusiano** R kwenye seti A na B ni sehemu ndogo ya A × B. Wakati (a, b) ∈ R, tunaandika aRb.
### Aina za Mahusiano
Uhusiano R kwenye seti A inaweza kuwa na sifa hizi:
| Mali | Ufafanuzi | Mfano |
|----------|------------|---------|
| Kutafakari | ∀a ∈ A: aRa | ≤ kwenye ℤ |
| Isiyobadilika | ∀a ∈ A: ¬(aRa) | < kwenye ℤ |
| Ulinganifu | ∀a,b: aRb → bRa | = kwenye seti yoyote |
| Antisymmetric | ∀a,b: aRb ∧ bRa → a = b | ≤ kwenye ℤ |
| Mpito | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = kwenye ℤ |
### Mahusiano ya Usawa
**Uhusiano wa usawa** unarejelea, ulinganifu, na badilifu. Inagawanya seti katika tofauti **madarasa ya usawa**.
**Mfano:** Hesabu ya msimu. Bainisha a ~ b if a ≡ b (mod n). Madarasa ya usawa ni [0], [1], ..., [n−1], ambayo yanagawanya ℤ katika madarasa n.
**Mfano Uliofanyiwa Kazi:** Kwenye ℤ × ℤ, fafanua (a,b) ~ (c,d) if a + d = b + c. Huu ni uhusiano wa usawa. Darasa [(0,0)] = {(n,n) : n ∈ ℤ}. Darasa [(1,0)] = {(n+1,n) : n ∈ ℤ}. Ujenzi huu kwa kweli hufafanua nambari kamili kutoka kwa nambari asilia.
### Maagizo Sehemu
**Mpangilio usio kamili** ni wa kujirejelea, unapinga ulinganifu, na badilifu. Seti yenye mpangilio wa sehemu inaitwa **seti iliyoagizwa kwa sehemu (poset)**.
| Dhana | Ufafanuzi | Mfano |
|---------|------------|----------|
| Weka | (S, ≤) na ≤ agizo la sehemu | (P(A), ⊆) - vikundi vidogo vilivyopangwa kwa kujumuisha |
| Mnyororo | Sehemu ndogo iliyoagizwa kabisa | {∅, {a}, {a,b}} katika P({a,b,c}) |
| Antichain | Sehemu ndogo ambapo hakuna vipengele viwili vinavyoweza kulinganishwa | {{a}, {b}} katika P({a,b}) |
| Mchoro wa Hasse | Uwakilishi unaoonekana wa pozi | Chora kingo tu kwa kufunika mahusiano |
| Upande wa Juu | Kipengele ≥ kila kipengele katika kikundi kidogo | sup({2,3}) = 6 in (ℤ, \|) (mgawanyiko) |
| Angalau Upper Bonds (sup) | Ndogo ya juu kabisa | sup({2,3}) katika (ℕ, ≤) ni 3 |
| Kiwango Kikubwa Zaidi cha Chini (inf) | Kubwa chini kabisa | inf({4,6}) katika (ℕ, \|) ni 2 |
---

## Kazi
A **kazi** f: A → B inapeana kila kipengele cha A kipengele kimoja cha B.
### Uainishaji wa Kazi
| Aina | Ufafanuzi | Mfano |
|------|------------|----------|
| Sindano (moja-kwa-moja) | f(a) = f(b) → a = b | f(x) = 2x kutoka ℤ → ℤ |
| Dhamira (kwenye) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2 kutoka ℤ → {0,1} |
| Lengo | Sindano na kidhamira | f(x) = x + 1 kutoka ℤ → ℤ |
### Dhana Muhimu za Kazi
| Dhana | Ufafanuzi | Tumia Kesi |
|---------|------------|-----------|
| Kitendaji kinyume | f⁻¹ ipo ikiwa f ni lengo kuu | Kusimbua data iliyosimbwa |
| Muundo | (g ∘ f)(x) = g(f(x)) | Mabadiliko ya minyororo |
| Kitendaji cha utambulisho | kitambulisho(x) = x | Kipengele cha upande wowote cha utunzi |
| Pointi zisizohamishika | f(x) = x | Ufafanuzi wa kujirudi, semantiki |
| Ruhusa | Mtazamo kutoka kwa seti hadi yenyewe | Kupanga upya data, kuchanganya |
### Kuhesabu Kazi
Kwa kuzingatia seti zenye kikomo |A| = m na |B| = n:
| Aina | Hesabu |
|------|-------|
| Vitendaji vyote A → B | nᵐ |
| Vitendaji vya sindano | n! / (n−m)! (kama n ≥ m, mwingine 0) |
| Vitendaji dhamira | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (kwa kujumuisha-kutengwa) |
| Vitendaji vya shabaha | n! (wakati m = n) |
---

## Combinatorics
Combinatorics ni hisabati ya kuhesabu, kupanga, na kuchagua.
### Kanuni za Msingi za Kuhesabu
| Kanuni | Taarifa | Mfano |
|-----------|-----------|---------|
| Kanuni ya Jumla | Ikiwa A na B zimetengana, |A ∪ B| = |A| + |B| | Kuchagua matunda: 3 apples + 4 machungwa = 7 chaguzi |
| Kanuni ya Bidhaa | |A × B| = |A| · |B| | Mavazi: mashati 3 × suruali 4 = mavazi 12 |
| Kanuni ya Ubaguzi | Ikiwa f: A → B ni pingamizi, |A| = |B| | Hesabu seti ndogo kwa kuhesabu mifuatano ya binary |
| Kukamilisha | |A| = |U| − |Aᶜ| | Hesabu "angalau moja" kama jumla ya kutoa "hakuna" |
### Ruhusa na Mchanganyiko
| Nukuu | Jina | Mfumo | Maana |
|----------|------|--------------------|
| C(n, k) au (n k) | Binomial mgawo | n! / (k!(n−k)!) | Njia za kuchagua vitu k kutoka n (ili haijalishi) |
| P(n, k) | k-vibali vya n | n! / (n−k)! | Njia za kupanga vitu k kutoka n (mambo ya kuagiza) |
| n! | Kiwanda | n × (n−1) × ... × 1 | Njia za kupanga vitu vyote vya n |
| (n k) na marudio | Chaguo nyingi | C(n+k−1, k) | Chagua k kutoka n na marudio yanaruhusiwa |
**Nadharia ya Binomial:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Kitambulisho cha Pascal:** C(n,k) = C(n−1,k-1) + C(n-1,k)
### Kanuni ya Njiwa
**Muundo wa kimsingi:** Ikiwa vitu vya n+1 vitawekwa kwenye visanduku n, angalau kisanduku kimoja kina vitu ≥ 2.
**Umbo la jumla:** Ikiwa vitu vya N vitawekwa kwenye visanduku k, angalau kisanduku kimoja kina vitu ≥ ⌈N/k⌉.
**Mifano Iliyofanya Kazi:**
1. Kati ya watu wowote 13, angalau 2 wanashiriki mwezi wa kuzaliwa. (Watu 13, miezi 12 → shimo la njiwa.)
2. Onyesha kuwa kati ya nambari 5 kamili, kuna 3 ambazo jumla yake inaweza kugawanywa kwa 3.
   - Zingatia mabaki ya mod 3: {0, 1, 2}. Na nambari 5 kamili na madarasa 3 ya mabaki, kwa shimo la njiwa la jumla, angalau ⌈5/3⌉ = 2 hushiriki mabaki.
   - Ikiwa 3 wanashiriki mabaki r: jumla yao ≡ 3r ≡ 0 (mod 3).
   - Ikiwa 2 hushiriki mabaki 0 ​​na 2 shiriki salio 1: chagua moja kutoka kwa kila jozi pamoja na salio-0 kipengele → jumla ≡ 0 (mod 3).
3. **Matumizi katika CS:** Kanuni yoyote ya mbano isiyo na hasara lazima ipanue baadhi ya vipengee. (Iwapo kila mfuatano wa n-bit umebanwa hadi <n biti, ungeweka mifuatano 2ⁿ katika mifuatano isiyozidi 2ⁿ iliyobanwa - kukiuka sindano.)
### Nambari za Kikatalani
Nambari ya nth **Nambari ya Kikatalani** Cₙ = C(2n, n) / (n+1) hesabu:
| Muundo | Mfano |
|-----------|---------|
| Mifuatano halali ya mabano | ()(), (()) kwa n = 2 |
| Binary miti na n nodi za ndani | miti 2 kwa n = 2 |
| Njia zisizovuka ulalo | Njia za gridi kutoka (0,0) hadi (n,n) zikikaa chini ya y = x |
| Pembetatu za poligoni | Njia za kugawanya (n+2)-gon katika pembetatu |
Chache za kwanza: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Kujirudia: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Mahusiano ya Kurudia
**uhusiano wa kujirudia** hufafanua kila neno la mfuatano kama kipengele cha istilahi zilizotangulia.
### Aina na Suluhu
| Aina | Fomu | Mbinu ya Usuluhishi |
|------|------|-----------------|
| Linear homogeneous (coeff mara kwa mara.) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Mlinganyo wa tabia |
| Linear isiyo ya homogeneous | aₙ = c₁aₙ₋₁ + ... + f(n) | Suluhisho maalum + suluhisho la homogeneous |
| Gawanya na ushinde | T(n) = aT(n/b) + f(n) | Nadharia ya bwana |
### Mbinu ya Mlingano wa Tabia
Kwa aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, tengeneza mlingano wa sifa:
r² − c₁r − c₂ = 0
| Kesi | Mizizi | Suluhisho la Jumla |
|------|-------|------------------|
| Mizizi miwili tofauti r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Mzizi unaorudiwa r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Mizizi changamano α ± βi | Badilisha kuwa polar: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B dhambi(nθ)) |
**Mfano Uliotumika:** Mfuatano wa Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Mlinganyo wa tabia: r² − r - 1 = 0
- Mizizi: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1.618, ψ = (1−√5)/2 ≈ -0.618
- Suluhisho la jumla: Fₙ = A·φⁿ + B·ψⁿ
- Kutoka kwa hali ya awali: A = 1/√5, B = -1/√5
- **Fomu iliyofungwa:** Fₙ = (φⁿ − ψⁿ) / √5 (Mchanganyiko wa Binet)
### Nadharia ya Mwalimu
Kwa marudio ya fomu T(n) = aT(n/b) + f(n) ambapo a ≥ 1, b > 1:
Acha c = log_b(a).
| Kesi | Hali | Suluhisho |
|------|-----------------------|
| 1 | f(n) = O(nᵈ) ambapo d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c, na af(n/b) ≤ kf(n) kwa baadhi ya k <1 | T(n) = Θ(nᵈ) |
**Mifano:**
- Unganisha aina: T(n) = 2T(n/2) + O(n). Hapa a=2, b=2, c=1, f(n)=n=Θ(n¹). Kesi ya 2: T(n) = Θ(n logi n).
- Utafutaji wa binary: T(n) = T(n/2) + O(1). Hapa a=1, b=2, c=0, f(n)=1=Θ(n⁰). Kesi ya 2: T(n) = Θ(logi n).
---

## Kuzalisha Kazi
**kitendakazi cha kuzalisha** husimba mfuatano (aₙ) kama vigawo vya mfululizo rasmi wa nishati.
### Aina
| Aina | Fomu | Tumia Kesi |
|------|------|----------|
| Kawaida (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Miundo isiyo na lebo, nyimbo |
| Kielelezo (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Miundo yenye lebo, vibali |
### Kazi za Kawaida za Kuzalisha
| Mfuatano aₙ | OGF G(x) |
|-------------|-----------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) kwa k fasta | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Kikatalani Cₙ | (1 − √(1−4x)) / (2x) |
### Kutumia Vitendo vya Kuzalisha ili Kusuluhisha Marudio
**Mfano Uliotumika:** Tatua aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Acha G(x) = Σ aₙxⁿ.
2. Kutokana na kujirudia: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Kibadala: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Sehemu za sehemu: G(x) = 2/(1−2x) − 1/(1−x)
7. Dondoo coefficients: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Uthibitishaji:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Angalia: 3(3) − 2(1) = 7.
---

## Aljebra ya Boolean na Mantiki ya Mapendekezo
Aljebra ya Boolean ni aljebra ya thamani mbili za ukweli: **Kweli (1)** na **Sivyo (0)**. Ni msingi wa hisabati wa saketi za dijiti, maswali ya hifadhidata, na masharti ya programu.
### Uendeshaji na Sheria
| Operesheni | Alama | Maana | Jedwali la Ukweli |
|-----------|------------------|-------------|
| NA | p ∧ q | Kweli tu wakati zote mbili ni kweli | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| AU | p ∨ q | Kweli wakati angalau moja ni kweli | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| SIO | ¬p | Kukanusha | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Kweli wakati moja ni kweli | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| INA MAANA | p → q | Si kweli tu wakati p=T na q=F | T→T=T, T→F=F, F→T=T, F→F=T |
| MASHARTI | p ↔ q | Kweli wakati zote zina thamani sawa | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Vitambulisho Muhimu vya Boolean
| Sheria | Mfumo |
|-----|--------|
| Mawasiliano | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Ushirika | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Usambazaji | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| Sheria za De Morgan | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Kukanusha Maradufu | ¬(¬p) = p |
| Upungufu wa nguvu za kiume | p ∧ p = p; p ∨ p = p |
| Kunyonya | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Kinyume | (p → q) ≡ (¬q → ¬p) |
### Fomu za Kawaida
| Fomu | Muundo | Tumia Kesi |
|------|-----------------------|
| Fomu ya Pamoja ya Kawaida (CNF) | NA ya AU: (A∨B) ∧ (C∨D) | Vitatuzi vya SAT, nadharia ya azimio inayothibitisha |
| Tofauti ya Fomu ya Kawaida (DNF) | AU ya AND: (A∧B) ∨ (C∧D) | Ubunifu wa mzunguko, mifumo inayotegemea sheria |
**Kugeuza kuwa CNF:** Tekeleza sheria za De Morgan, sambaza AU juu ya NA, ondoa kanusho maradufu.
---

## Hesabu ya Msimu na Mapatano
Msimu wa masomo ya hesabu integers chini ya uendeshaji wa "salio baada ya mgawanyiko." Ni muhimu kwa kriptografia, hashing, na nadharia ya nambari.
### Ufafanuzi wa Msingi
| Dhana | Nukuu | Ufafanuzi |
|---------|----------|------------|
| Ulinganifu | a ≡ b (mod n) | n mgawanyiko (a − b) |
| Darasa la mabaki | [a]ₙ | Seti {a + kn : k ∈ ℤ} |
| Inverse ya msimu | a⁻¹ mod n | Thamani x vile shoka ≡ 1 (mod n) |
| Totient ya Euler | φ(n) | Hesabu ya nambari kamili katika {1,...,n} coprime hadi n |
### Sifa Muhimu
| Mali | Taarifa |
|----------|----------|
| Nyongeza | Ikiwa a ≡ b na c ≡ d (mod n), basi a+c ≡ b+d (mod n) |
| Kuzidisha | Ikiwa ≡ b na c ≡ d (mod n), basi ac ≡ bd (mod n) |
| Nadharia Ndogo ya Fermat | Ikiwa p ni mkuu na gcd(a,p) = 1, basi aᵖ⁻¹ ≡ 1 (mod p) |
| Nadharia ya Euler | Ikiwa gcd(a,n) = 1, basi a^φ(n) ≡ 1 (mod n) |
| Nadharia ya Mabaki ya Kichina | Ikiwa gcd(m,n) = 1, mfumo x ≡ a (mod m), x ≡ b (mod n) una suluhisho la kipekee mod mn |
### Computing Euler's Totient
Kwa n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (uainishaji mkuu):
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Mfano:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Hakika, {1, 5, 7, 11} ni coprime hadi 12.
### Utumizi: Ufichaji wa RSA (Muhtasari)
1. Chagua primes kubwa p, q. Kokotoa n = pq, φ(n) = (p-1)(q-1).
2. Chagua e vile kwamba gcd(e, φ(n)) = 1 (kipeo cha umma).
3. Kokotoa d ≡ e⁻¹ (mod φ(n)) (kipeo cha kibinafsi).
4. Ficha: c = mᵉ mod n. Simbua: m = cᵈ mod n.
5. Usalama unategemea ugumu wa factoring n kupata p na q.
---

## Uingizaji wa Hisabati
**Uingizaji wa hisabati** ndiyo mbinu ya msingi ya uthibitisho wa taarifa kuhusu nambari zote asilia.
### Muundo wa Uthibitisho kwa Utangulizi
1. **Kesi ya msingi:** Thibitisha kauli ya n = 0 (au n = 1).
2. **Hatua ya kufata neno:** Chukulia kuwa taarifa inashikilia n = k (dhahania ya kufata neno), kisha ithibitishe kwa n = k + 1.
### Vibadala
| Lahaja | Wakati wa Kutumia |
|---------|-------------|
| Uingizaji rahisi | Thibitisha P(k) → P(k+1) |
| Uingizaji wa nguvu | Chukulia P(0), P(1), ..., P(k) ili kuthibitisha P(k+1) |
| Uingizaji wa miundo | Thibitisha sifa za miundo iliyoainishwa kwa kujirudia (miti, fomula) |
| Uingizaji wa uhakika | Ongeza utangulizi kwa seti zilizoagizwa vizuri zaidi ya ℕ |
**Mfano Uliofanyiwa Kazi (Uingizaji Wenye Nguvu):** Thibitisha kila nambari n ≥ 2 inaweza kuandikwa kama bidhaa ya msingi.
- Msingi: n = 2 ni mkuu, hivyo ni bidhaa ya primes (yenyewe).
- Hatua ya kufata neno: Chukulia kuwa kweli kwa nambari zote kuanzia 2 hadi k. Zingatia k+1.
  - Ikiwa k+1 ni ya kwanza, imekamilika.
  - Ikiwa k+1 ni mchanganyiko, k+1 = ab ambapo 2 ≤ a, b ≤ k. Kwa nadharia ya kufata neno, a na b ni bidhaa za msingi, kwa hivyo k+1 ni bidhaa ya msingi.
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Dhana ya Pekee ya Hisabati | Maombi katika ML / Sayansi ya Data |
|-------------------------------------------------------|
| Weka nadharia | Operesheni za hifadhidata (SQL JOINs), uchezaji wa seti za vipengele, matukio ya uwezekano |
| Mahusiano | Mipangilio ya hifadhidata, muundo wa uhusiano wa chombo, grafu za maarifa |
| Kazi | Vitendaji vya kuwezesha, mabadiliko ya vipengele, upangaji kati ya nafasi |
| Mchanganyiko | Uteuzi wa kipengele (kuchagua k kutoka n), ukubwa wa utafutaji wa gridi ya hyperparameta |
| Kanuni ya njiwa | Migongano ya hashing, mipaka ya chini juu ya ukandamizaji, uthibitisho wa nadharia ya habari |
| Mahusiano ya kujirudia | Upangaji wa nguvu, uchanganuzi wa ugumu wa algorithm, mifano ya mfululizo wa saa |
| Inazalisha vitendaji | Uwezekano wa kuzalisha vitendaji, kutatua matatizo ya ujumuishaji katika uhandisi wa kipengele |
| Nambari za Kikatalani | Kuhesabu miundo ya miti (miti ya maamuzi), misemo ya kuchanganua, shughuli za mrundikano |
| Nadharia ya grafu (tazama faili inayofuata) | Uchambuzi wa mtandao wa kijamii, mifumo ya mapendekezo, uwakilishi wa maarifa |
---

## Muhtasari
| Mada | Wazo la Msingi | Zana Muhimu |
|-------|-----------|-----------|
| Weka Nadharia | Mkusanyiko wa vitu tofauti | Misingi ya ZFC, ukardinali, shughuli |
| Mahusiano | Viunganisho kati ya vipengele | Mahusiano ya usawa, maagizo ya sehemu |
| Kazi | Ramani kati ya seti | Sindano, surjectivity, bijection |
| Mchanganyiko | Mipango ya kuhesabu | Coefficients Binomial, kanuni ya njiwa |
| Mahusiano ya Kujirudia | Mifuatano imefafanuliwa kwa kujirudia | Milinganyo ya tabia, nadharia kuu |
| Kuzalisha Kazi | Mfuatano kama mfululizo wa nguvu | OGF/EGF, kutatua kurudiwa kwa aljebra |
Hisabati mahususi hutoa lugha na zana za kusababu kuhusu miundo yenye kikomo au inayoweza kuhesabika - ambayo ndiyo hasa kompyuta hudhibiti. Kila algoriti, muundo wa data, hoja ya hifadhidata na itifaki ya kriptografia hutegemea misingi tofauti. Umahiri wa mada hizi huongeza uwezo wa kusuluhisha matatizo na hutoa msamiati kwa ajili ya utafiti wa hali ya juu katika algoriti, nadharia changamano na kujifunza kwa mashine.