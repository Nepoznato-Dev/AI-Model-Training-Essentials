---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Nadharia ya Mchezo
Nadharia ya mchezo ni hisabati ya mwingiliano wa kimkakati - hali ambapo matokeo yako hayategemei tu chaguo lako mwenyewe, lakini na chaguo za wengine. Kuanzia vita vya bei kati ya makampuni hadi mbio za silaha za nyuklia, kutoka kwa minada ya mtandaoni hadi baiolojia ya mabadiliko, nadharia ya mchezo hutoa zana za kuchanganua migogoro na ushirikiano. Imekuwa muhimu zaidi kwa ujifunzaji wa mashine kupitia ujifunzaji wa uimarishaji wa mawakala wengi, mitandao generative adversarial (GANs), na muundo wa mitambo ya mifumo ya mtandaoni.
---

## Michezo ya Fomu ya Kimkakati
### Ufafanuzi
Mchezo **wa kimkakati (umbo la kawaida)** unajumuisha:
- Seti ya wachezaji N = {1, 2, ..., n}
- Mkakati huweka S₁, S₂, ..., Sₙ kwa kila mchezaji
- Utendaji wa malipo u₁, u₂, ..., uₙ kuchora wasifu wa mkakati kwa nambari halisi
### Mfano: Matatizo ya Mfungwa
| | Shirikiana (C) | Kasoro (D) |
|---|---------------|------------|
| **Shirikiana (C)** | (−1, −1) | (−3, 0) |
| **Kasoro (D)** | (0, −3) | (−2, −2) |
| Uchambuzi | Matokeo |
|----------|--------|
| Mbinu kuu | Kasoro (D inatawala C kwa wachezaji wote wawili) |
| Nash usawa | (D, D) pamoja na malipo (−2, −2) |
| Ubora wa kijamii | (C, C) pamoja na malipo (−1, −1) |
| Shida | Urazini wa mtu binafsi husababisha kutokuwa na busara kwa pamoja |
### Michezo Zaidi ya Kawaida
**Vita vya Jinsia:**
| | Opera | Kandanda |
|---|-------|----------|
| Opera | (2, 1) | (0, 0) |
| Kandanda | (0, 0) | (1, 2) |
Msawazo wa Nash mbili: (Opera, Opera) na (Soka, Soka).
**Kuku (Njiwa-Njiwa):**
| | Mwewe | Njiwa |
|---|------|------|
| Mwewe | (−10, −10) | (5, 0) |
| Njiwa | (0, 5) | (1, 1) |
Msawazo wa Nash mbili: (Hawk, Njiwa) na (Njiwa, Hawk).
---

## Mikakati Kuu
| Dhana | Ufafanuzi |
|---------|------------|
| **Inatawala sana** | Mkakati sᵢ unatoa faida kubwa kuliko mkakati mwingine wowote, bila kujali chaguo za wapinzani |
| **Inatawala kwa udhaifu** | Mbinu sᵢ inatoa angalau malipo ya juu kama nyingine yoyote, na ya juu zaidi kwa wasifu wa wapinzani |
| **Mkakati unaotawaliwa** | Mkakati ambao kamwe sio jibu bora |
**Kuondolewa mara kwa mara kwa mikakati inayotawala:**
1. Ondoa mikakati yoyote iliyodhibitiwa kabisa
2. Rudia hadi hakuna zaidi inaweza kuondolewa
3. Ikiwa wasifu mmoja wa mkakati utasalia, ni usawa wa kipekee wa Nash
---

## Nash Equilibrium
**Msawazo wa Nash** ni wasifu wa mkakati ambapo hakuna mchezaji anayeweza kuboresha malipo yake kwa kubadilisha mkakati wao kwa upande mmoja.
### Ufafanuzi
(s₁*, s₂*, ..., sₙ*) ni msawazo wa Nash ikiwa kwa kila mchezaji i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) kwa sᵢ ∈ Sᵢ
### Kupata Usawa wa Nash (Michezo 2×2)
**Njia bora ya majibu:**
1. Kwa kila safu, pigia mstari jibu bora la mchezaji 1
2. Kwa kila safu, pigia mstari jibu bora la mchezaji 2
3. Seli ambazo zote zimepigiwa mstari ni usawa wa Nash
### Kuwepo (Nadharia ya Nash)
Kila mchezo wenye kikomo una angalau usawa mmoja wa Nash (labda katika mikakati mchanganyiko).
### Mikakati Mchanganyiko
**mkakati mseto** ni usambazaji wa uwezekano juu ya mikakati madhubuti.
| Dhana | Ufafanuzi |
|---------|------------|
| Mbinu mchanganyiko σᵢ | Uwezekano wa usambazaji juu ya Sᵢ |
| Mbinu mchanganyiko NE | Hakuna mchezaji anayeweza kuboresha malipo yanayotarajiwa kwa kubadilisha mchanganyiko wao |
| Msaada | Seti ya mikakati safi iliyochezwa na uwezekano chanya |
**Mfano Uliofanyiwa Kazi: Peni Zinazolingana**
| | Vichwa | Mikia |
|---|-------|-------|
| Vichwa | (1, −1) | (−1, 1) |
| Mikia | (−1, 1) | (1, −1) |
Hakuna mkakati safi NE. NE iliyochanganywa: zote hucheza H na T kwa uwezekano ½ kila moja.
---

## Nadharia ya kiwango cha chini
### Michezo ya Sifuri-Jumla
Katika mchezo **sufuri-jumla**, faida ya mchezaji mmoja ni hasara ya mwingine: u₁ + u₂ = 0.
### Nadharia ya Minimax ya Von Neumann
Kwa kila mchezo wenye kikomo wa wachezaji wawili wa sifuri:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
**maximin** (hali mbaya zaidi kwa mchezaji 1) ni sawa na **kiwango cha chini zaidi** (hali mbaya zaidi kwa mchezaji 2). Thamani hii ya kawaida ni **thamani ya mchezo**.
### Kutatua Michezo ya Sifuri-Jumla
Kwa mchezo wa 2 × 2 wa sifuri na tumbo:
| | L | R |
|---|---|---|
| T | a | b |
| B | c | d |
Mbinu iliyochanganywa ya mchezaji 1: cheza T na uwezekano p = (d-c)/((a-b)+(d-c))
Thamani ya mchezo: v = (ad-bc)/((a-b)+(d−c))
---

## Michezo ya Kidato Kina
Michezo iliyo na hatua zinazofuatana inawakilishwa kama **miti ya mchezo**.
### Dhana Muhimu
| Dhana | Ufafanuzi |
|---------|------------|
| **Mti wa mchezo** | Mti unaoonyesha mifuatano yote inayowezekana ya miondoko |
| **Seti ya habari** | Seti ya nodi ambazo mchezaji hawezi kutofautisha |
| **Taarifa kamili** | Kila taarifa iliyowekwa ni singleton (hatua zote zinaonekana) |
| **Mchezo mdogo NE** | Usawa wa Nash katika kila mchezo mdogo |
| **Uingizaji wa nyuma** | Tatua kutoka mwisho wa mti kuelekea nyuma |
### Nadharia ya Zermelo
Katika maelezo mafupi, kamili, michezo ya wachezaji wawili bila nafasi: mchezaji mmoja ana mkakati wa kushinda, au wote wanaweza kulazimisha sare (k.m., chess).
---

## Michezo ya Ushirika
Katika **michezo ya vyama vya ushirika**, wachezaji wanaweza kuunda makubaliano na miungano inayofunga.
### Tabia ya Kazi
Mchezo wa vyama vya ushirika hufafanuliwa kwa ** sifa za kukokotoa ** v: 2^N → ℝ, ambapo v(S) ndio muungano wa thamani S unaweza kufikia.
| Mali | Ufafanuzi |
|----------|------------|
| **Ya ziada** | v(S ∪ T) ≥ v(S) + v(T) kwa kitenganishi S, T |
| **Convex** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) kwa S ⊂ T |
### Msingi
**msingi** ni seti ya mgao ambapo hakuna muungano unaweza kuboreka kwa kujitenga:
Msingi = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) kwa S ⊂ N}
Msingi unaweza kuwa tupu - katika hali ambayo hakuna mgao thabiti uliopo.
### Thamani Shapley
**Thamani ya Shapley** hutoa mgao wa kipekee wa haki kulingana na michango ya kando:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i})) − v(S)]
| Mali | Taarifa |
|----------|-----------|
| Ufanisi | Σ φᵢ = v(N) (thamani yote imesambazwa) |
| Ulinganifu | Wachangiaji sawa wanapata malipo sawa |
| Mchezaji dummy | Wasio wachangiaji wanapata sifuri |
| Nyongeza | φ(v + w) = φ(v) + φ(w) |
**Tafsiri:** Thamani ya Shapley ya kila mchezaji ni mchango wao wa wastani wa kando katika upangaji wote unaowezekana wa uundaji wa muungano.
### Mfano Uliofanya Kazi
Wachezaji watatu: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 10.
| Mchezaji | Michango ya kando (wastani juu ya maagizo) | Thamani ya Shapley |
|--------|----------------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56.7 | 37.5 |
| 2 | (100+50+60+60+50+0)/6 | 27.5 |
| 3 | (100+70+60+70+60+0)/6 | 35.0 |
(Imehesabiwa kwa usahihi kwa kutumia fomula ya Shapley kwa kila kibali.)
---

## Usanifu wa Utaratibu
**Muundo wa utaratibu** ni "nadharia ya mchezo kinyume" — badala ya kuchanganua michezo fulani, kubuni michezo ambayo hutoa matokeo unayotaka.
### Kanuni ya Ufunuo
Utaratibu wowote unaofikia matokeo yanayotarajiwa unaweza kubadilishwa na **utaratibu wa ufunuo wa moja kwa moja** ambapo kusema ukweli ni usawa wa Nash.
### Nadharia ya Mnada
| Aina ya Mnada | Kanuni | Usawa wa Mapato |
|---------------------|---------------------|
| **Zabuni ya bei ya kwanza iliyotiwa muhuri** | Mzabuni wa juu hushinda, hulipa zabuni zao | Minada yote ya kawaida hutoa mapato sawa yanayotarajiwa |
| **Zabuni ya bei ya pili (Vickrey)** | Mzabuni mkuu atashinda, hulipa zabuni ya pili kwa juu | (chini ya maadili huru ya kibinafsi) |
| **Kiingereza (kinachopanda)** | Bei inapanda; kwanza kukubali ushindi | - |
| **Kiholanzi (kushuka)** | Bei inashuka; kwanza kukubali ushindi | - |
### Mnada wa Vickrey (Bei ya Pili)
**Mkakati mkuu:** Tangaza thamani yako halisi.
| Mali | Taarifa |
|----------|-----------|
| Zabuni ya ukweli | Mbinu dhaifu |
| Ufanisi | Bidhaa huenda kwa mzabuni wa thamani ya juu |
| Mapato | Mapato sawa na yale ya bei ya kwanza (Nadharia ya Usawa wa Mapato) |
### Muundo Bora wa Mnada (Myerson)
Mnada wa kuongeza mapato:
- Inamgawia mzabuni na hesabu ya juu zaidi **.
- Inaweka bei ya akiba
- Tathmini ya mtandaoni: ψ(v) = v - (1−F(v))/f(v)
---

## Viunganisho kwa Mafunzo ya Mashine
### Mitandao ya Uzalishaji ya Adversarial (GANs)
GAN ni mchezo wa wachezaji wawili kati ya jenereta G na kibaguzi D:
min_G max_D V(D, G) = E[logi D(x)] + E[logi(1 − D(G(z))))]
| Dhana ya Nadharia ya Mchezo | GAN Sawa |
|--------------------------------------|
| Mchezo wa wachezaji wawili sifuri-jumla | Jenereta dhidi ya kibaguzi |
| Nash usawa | G hutoa data halisi, matokeo ya D ½ kila mahali |
| Kiwango cha chini | Kazi ya lengo la GAN |
| Kukunja kwa hali | Kukosa kufikia usawa |
### Masomo ya Kuimarisha Ajenti nyingi (MARL)
| Dhana | MARL Maombi |
|---------|-----------------|
| Nash usawa | Sera thabiti katika mipangilio ya mawakala wengi |
| Kiwango cha chini | Sera madhubuti dhidi ya wapinzani |
| Michezo ya ushirika | Uundaji wa muungano, ugawaji wa kazi |
| Thamani ya Shapley | Mgawo wa mkopo (ni wakala gani alichangia nini?) |
| Ubunifu wa utaratibu | Kubuni motisha katika mifumo ya mawakala wengi |
| Mchezo wa kutunga | Kujifunza algorithm kugeuzwa kuwa usawa wa Nash |
### Viunganisho Vingine vya ML
| Maombi | Zana ya Nadharia ya Mchezo |
|-------------------------------|
| Muundo wa mnada wa matangazo (Google, Facebook) | Ubunifu wa utaratibu, nadharia ya mnada |
| Muundo wa soko (Uber, Airbnb) | Nadharia inayolingana, muundo wa mitambo |
| Uimara wa adui | Michezo ya sifuri kati ya mshambuliaji na beki |
| Mgawanyiko wa haki | Thamani ya Shapley, mgao usio na wivu |
| Kujifunza kwa Shirikisho | Nadharia ya mchezo wa ushirika kwa kipimo cha mchango |
| Mifumo ya mapendekezo | Ubunifu wa utaratibu wa uhamasishaji wa upendeleo wa ukweli |
---

## Muhtasari
| Dhana | Wazo la Msingi | Matokeo Muhimu |
|---------|-----------|------------|
| Michezo ya kimkakati | Wachezaji, mikakati, malipo | Uwakilishi wa matrix ya mchezo |
| Mikakati kuu | Bora bila kujali wengine | Uondoaji unaorudiwa |
| Nash usawa | Hakuna kupotoka kwa upande mmoja kwa faida | Inapatikana katika kila mchezo wenye kikomo |
| Mikakati mchanganyiko | Kubahatisha juu ya vitendo | Nadharia ya uwepo wa Nash |
| Kiwango cha chini | Hali mbaya zaidi (sufuri-jumla) | Nadharia ndogo ya Von Neumann |
| Fomu ya kina | Hatua zinazofuatana | Uingizaji wa nyuma, ukamilifu wa mchezo mdogo |
| Michezo ya ushirika | Muungano unaofungamana | Msingi, thamani ya Shapley |
| Ubunifu wa utaratibu | Tengeneza michezo kwa matokeo | Kanuni ya ufunuo, minada bora zaidi |
| Nadharia ya mnada | Kuuza kupitia shindano | Usawa wa mapato, mnada wa Vickrey |
Nadharia ya mchezo ni hisabati ya mawazo ya kimkakati. Katika ulimwengu unaozidi kuwa na watu wanaowasiliana na mawakala wa AI, soko za kiotomatiki, na mifumo pinzani, nadharia ya mchezo hutoa zana muhimu ya kutabiri tabia, kubuni mbinu, na kujenga mifumo thabiti ya mawakala wengi. Kwa wanasayansi wa data, inaeleza jinsi GAN zinavyofanya kazi, jinsi minada ya mtandaoni inavyozalisha mabilioni ya mapato, na jinsi ya kuunda mifumo ya AI inayofanya kazi vizuri katika mazingira ya ushindani.