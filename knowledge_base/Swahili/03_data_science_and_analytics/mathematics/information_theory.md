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
# Nadharia ya Habari
Nadharia ya habari, iliyoanzishwa na Claude Shannon mnamo 1948, inahesabu habari yenyewe. Je, ujumbe unakuambia kiasi gani? Je, unaweza kubana data kiasi gani? Je, unaweza kuwasiliana kwa kasi gani kwenye kituo chenye kelele? Maswali haya yana majibu sahihi ya hisabati. Zaidi ya mawasiliano, nadharia ya habari imekuwa msingi wa ujifunzaji wa mashine - njia-tofauti ni chaguo-msingi la upotezaji wa uainishaji, vipimo vya mseto wa KL ulinganifu wa usambazaji, na uteuzi wa vipengele vya viendeshi vya habari.
---

## Entropy
**Entropy** hupima wastani wa kutokuwa na uhakika au "mshangao" wa tofauti nasibu.
### Shannon Entropy (Discrete)
Kwa utofauti wa nasibu wa X na uwezekano wa kukokotoa kwa wingi wa p(x):
H(X) = −Σₓ p(x) logi₂ p(x)
Vitengo: **biti** (unapotumia log₂) au **nats** (unapotumia ln).
| Usambazaji | Entropy | Intuition |
|------------------------------------|
| Sarafu ya haki (p = 0.5, 0.5) | biti 1 | Kiwango cha juu cha kutokuwa na uhakika kwa matokeo ya jozi |
| Sarafu yenye upendeleo (p = 0.9, 0.1) | Biti 0.469 | Si ya kushangaza — mara nyingi vichwa |
| Kuamua (p = 1, 0) | Biti 0 | Hakuna shaka hata kidogo |
| Kufa kwa haki (pande 6) | Biti 2.585 | Matokeo zaidi = kutokuwa na uhakika zaidi |
| Uniform over n matokeo | log₂(n) biti | Upeo wa entropy kwa matokeo ya n |
### Sifa za Entropy
| Mali | Taarifa |
|----------|-----------|
| Kutokuwa hasi | H(X) ≥ 0 |
| Upeo | H(X) ≤ log₂(\|X\|) yenye usawa kwa usambazaji sare |
| Sheria ya mnyororo | H(X, Y) = H(X) + H(Y \| X) |
| Uwekaji viyoyozi hupunguza | H(X \| Y) ≤ H(X) |
| Upungufu | H ni chaguo la kukokotoa la usambaaji wa uwezekano |
### Differential Entropy (Inayoendelea)
Kwa utofauti unaoendelea wa X na wiani p(x):
h(X) = −∫ p(x) logi p(x) dx
Tofauti na entropy tofauti, entropy tofauti inaweza kuwa ** hasi **.
| Usambazaji | Entropy ya Tofauti |
|-----------------------------------|
| Sare kwenye [a,b] | logi(b - a) |
| N(μ, σ²) ya Kawaida | (1/2) logi(2πeσ²) |
| Kielelezo(λ) | 1 − ln(λ) |
---

## Taarifa ya Pamoja, Masharti, na ya Pamoja
### Entropy ya Pamoja
H(X, Y) = −Σₓ Σᵧ p(x, y) kumbukumbu p(x, y)
Hupima kutokuwa na uhakika wa jumla wa jozi (X, Y).
### Entropy ya Masharti
H(Y | X) = −Σₓ Σᵧ p(x, y) logi p(y | x) = H(X, Y) − H(X)
Hupima kutokuwa na uhakika kuhusu Y baada ya kutazama X.
### Taarifa za Pamoja
I(X; Y) = Σₓ Σᵧ p(x, y) kumbukumbu [p(x, y) / (p(x)p(y))]
Hupima ni kiasi gani kujua X hukuambia kuhusu Y (na kinyume chake).
| Mali | Taarifa |
|----------|-----------|
| Kutokuwa hasi | I(X; Y) ≥ 0 |
| Ulinganifu | I(X; Y) = I(Y; X) |
| Uhusiano na entropy | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Uhusiano na pamoja | I(X; Y) = H(X) + H(Y) − H(X,Y) |
| Uhuru | I(X; Y) = 0 ikiwa X na Y zinajitegemea |
| Habari binafsi | Mimi(X; X) = H(X) |
### Visual: Mchoro wa Entropy
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

## Tofauti ya KL
Tofauti ya **Kullback-Leibler (KL)** hupima jinsi usambazaji mmoja ulivyo tofauti na mwingine.
D_KL(P || Q) = Σₓ logi ya P(x) [P(x) / Q(x)]
| Mali | Taarifa |
|----------|-----------|
| Kutokuwa hasi | D_KL(P \|\| Q) ≥ 0 (kukosekana kwa usawa kwa Gibbs) |
| Utambulisho | D_KL(P \|\| Q) = 0 ikiwa P = Q |
| Asymmetry | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) kwa ujumla |
| Sio kipimo | Inashindwa ulinganifu na usawa wa pembetatu |
**Tafsiri:** D_KL(P || Q) ni idadi ya ziada ya biti zinazohitajika ili kusimba data kutoka P kwa kutumia msimbo ulioboreshwa kwa Q.
### Uhusiano na Kiasi Nyingine
| Uhusiano | Mfumo |
|-----------------------|
| Msalaba entropy | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Taarifa za pamoja | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL ya Masharti | D_KL(P(Y\|X) \|\| Q(Y\|X)) ina wastani wa X |
---

## Mtambuka
**Mtambuka** kati ya usambazaji P na Q:
H(P, Q) = −Σₓ logi ya P(x) Q(x) = H(P) + D_KL(P || Q)
### Uingizaji Mtambuka kama Kazi ya Kupoteza
Katika uainishaji, P ndio usambazaji wa kweli (lebo iliyosimbwa ya moto-moja) na Q ni usambazaji uliotabiriwa wa mfano.
**Binary cross-entropy (BCE):**
L = −[y logi(ŷ) + (1−y) logi(1−ŷ)]
**Kategoria mtambuka:**
L = −Σᵢ yᵢ logi(ŷᵢ)
| Hali | y (kweli) | ŷ (iliyotabiriwa) | Hasara |
|----------|----------|--------------|-------|
| Sahihi, ujasiri | 1 | 0.95 | 0.051 |
| Sahihi, sina uhakika | 1 | 0.55 | 0.598 |
| Sio sahihi, kujiamini | 1 | 0.05 | 2.996 |
| Si sahihi, sina uhakika | 1 | 0.45 | 0.799 |
Kupunguza mtambuka ni sawa na kupunguza tofauti ya KL kutoka kwa usambazaji wa kweli - ndiyo maana inafanya kazi vizuri kama chaguo la kukokotoa la upotezaji.
---

## Uwezo wa Kituo
### Muundo wa Kituo cha Mawasiliano
```
X → [Channel] → Y
```

- X: ingizo la kutofautiana kwa nasibu
- Y: pato la kutofautiana kwa nasibu
- Kituo: kinafafanuliwa kwa uwezekano wa masharti p(y|x)
### Nadharia ya Usimbaji ya Idhaa Yenye Kelele ya Shannon
Kwa chaneli yenye uwezo wa C, ikiwa kiwango cha maambukizi R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, mawasiliano ya kuaminika hayawezekani.
**Uwezo wa kituo:**
C = max_{p(x)} I(X; Y)
### Mifano Muhimu ya Idhaa
| Kituo | Maelezo | Uwezo |
|---------|-------------|----------|
| **Ulinganifu wa binary (BSC)** | Hugeuza kila biti kwa uwezekano p | 1 − H(p) biti |
| **Ufutaji wa njia mbili (BEC)** | Hufuta kila biti kwa uwezekano ε | 1 − ε biti |
| **Gaussian (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)logi(1 + SNR) biti |
| **Binari isiyo na kelele** | Usambazaji kamili | biti 1 |
---

## Chanzo Usimbaji na Mfinyazo
### Nadharia ya Usimbaji Chanzo
Idadi ya wastani ya biti zinazohitajika ili kusimba chanzo imefungwa hapa chini na entropy yake:
L ≥ H(X)
Nambari mojawapo ya kuthibitisha itafikia L ≈ H(X).
### Usimbaji wa Huffman
Msimbo **isiyo na kiambishi awali** unaoweka misimbo mifupi kwa alama zinazowezekana zaidi.
| Alama | Uwezekano | Msimbo wa Huffman | Urefu |
|--------|--------------------------|---------|
| A | 0.5 | 0 | 1 |
| B | 0.25 | 10 | 2 |
| C | 0.125 | 110 | 3 |
| D | 0.125 | 111 | 3 |
Urefu wa wastani: 0.5(1) + 0.25(2) + 0.125(3) + 0.125(3) = biti 1.75/alama
Entropy: H = 1.75 bits/alama (bora katika kesi hii!)
### Isiyo na hasara dhidi ya Mfinyazo wa Kupoteza
| Aina | Kanuni | Mifano | Kikomo |
|------|-----------|----------|-------|
| **Bila hasara** | Ondoa upungufu wa takwimu | ZIP, PNG, FLAC | Kiwango cha entropy H(X) |
| **Hasara** | Ondoa maelezo yasiyo na maana | JPEG, MP3, H.264 | Chaguo za kukokotoa viwango R(D) |
**Nadharia ya ukadiriaji wa ukadiriaji:** Kwa mbano yenye hasara yenye upotoshaji wa juu zaidi D, kiwango cha chini zaidi ni R(D) = dakika I(X; X̂) kulingana na E[d(X, X̂)] ≤ D.
---

## Miunganisho kwa Sehemu Zingine
### Nadharia ya Habari na Thermodynamics
| Dhana | Nadharia ya Habari | Thermodynamics |
|---------|------------------|----------------|
| Entropy | Shannon entropy H(X) | Boltzmann entropy S = k_B ln W |
| Upeo entropy | Usambazaji sare | Usawa wa joto |
| Tofauti ya KL | Tofauti ya usambazaji | Tofauti ya nishati ya bure |
| Taarifa za pamoja | Habari iliyoshirikiwa | Uhusiano katika mifumo ya kimwili |
Fomu za hisabati zinafanana - Shannon aliazima kimakusudi neno "entropy" kutoka kwa mechanics ya takwimu.
### Nadharia ya Habari na Takwimu
| Dhana | Maombi |
|---------|-------------|
| Uwezekano wa juu zaidi | Sawa na kupunguza tofauti za KL kutoka kwa usambazaji wa majaribio hadi kwa mfano |
| Maelezo ya wavuvi | Mviringo wa tofauti za KL; mipaka ya chini kwenye tofauti ya mkadiriaji (Cramér-Rao) |
| Urefu wa chini kabisa wa maelezo (MDL) | Uteuzi wa muundo kwa kupunguza jumla ya urefu wa usimbaji |
| AIC / BIC | Kadirio la vigezo vya uteuzi wa muundo kulingana na KL |
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Dhana ya IT | Programu ya ML |
|-----------|----------------|
| Kupoteza kwa njia nyingi | Hasara ya uainishaji chaguo-msingi (binary na tabaka nyingi) |
| Tofauti ya KL | Hasara ya VAE (neno la udhibiti), kulinganisha usambazaji, kunereka |
| Taarifa za pamoja | Uteuzi wa vipengele (MIFS), mafunzo ya uwakilishi (InfoMax), kutenganisha |
| Entropy | Kigezo cha mgawanyiko wa mti wa uamuzi (faida ya habari), uchunguzi katika RL (kiwango cha juu cha entropy RL) |
| Uwezo wa kituo | Utata wa mawasiliano, uelewa wa mipaka ya jumla |
| Usimbaji wa chanzo | Mfinyazo wa data kwa uhifadhi na usambazaji, usimbaji bora |
| Upeo entropy | Viainishi vya MaxEnt, uteuzi wa awali katika uelekezaji wa Bayesian |
| Kiwango-upotoshaji | Kuelewa mabadiliko katika ukandamizaji wa hasara, hesabu katika mitandao ya neva |
| Maelezo ya wavuvi | Asili ya asili ya upinde rangi, uelewa wa parameta |
| MDL / AIC / BIC | Uchaguzi wa mfano, kuzuia overfitting |
---

## Muhtasari
| Kiasi | Mfumo (wa kipekee) | Maana |
|----------|-----------------------------|
| Entropy H(X) | −Σ p(x) logi p(x) | Wastani wa kutokuwa na uhakika |
| Entropy ya pamoja H(X,Y) | −Σ p(x,y) kumbukumbu p(x,y) | Jumla ya kutokuwa na uhakika wa jozi |
| Entropy ya masharti H(Y\|X) | H(X,Y) − H(X) | Kutokuwa na uhakika juu ya Y iliyopewa X |
| Taarifa za pamoja I(X;Y) | H(X) − H(X\|Y) | Taarifa iliyoshirikiwa kati ya X na Y |
| KL tofauti D_KL(P\|\|Q) | Σ logi ya P(x)(P(x)/Q(x)) | "Umbali" kati ya usambazaji |
| Mtambuka H(P,Q) | −Σ P(x) logi Q(x) | Gharama ya usimbaji kwa kutumia usambazaji usio sahihi |
| Uwezo wa kituo C | upeo wa I(X;Y) | Kiwango cha juu cha kuaminika cha mawasiliano |
Nadharia ya habari hutoa mipaka ya kimsingi ya kile kinachoweza kujifunza, kubanwa, na kuwasilishwa. Kwa wataalamu wa kujifunza kwa mashine, inaeleza kwa nini cross-entropy hufanya kazi kama chaguo la kupoteza, jinsi ya kupima ubora wa uwasilishaji uliojifunza, na jinsi ya kufikiria juu ya ubadilishanaji kati ya utata wa muundo na usawa wa data. Maarifa ya Shannon kutoka 1948 yanabaki kuwa muhimu kwa AI ya kisasa kama yalivyo kwa mawasiliano ya simu.