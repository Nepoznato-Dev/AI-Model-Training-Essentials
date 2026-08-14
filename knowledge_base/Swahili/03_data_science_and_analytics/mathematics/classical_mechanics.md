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
# Mitambo ya Kawaida
Mitambo ya classical inaelezea mwendo wa vitu chini ya ushawishi wa nguvu. Kutoka kwa tufaha zinazoanguka hadi sayari zinazozunguka, kutoka kwa nyuzi zinazotetemeka hadi chembe zinazogongana, kanuni zake zinatawala ulimwengu wa macroscopic. Zaidi ya matumizi yake ya kimwili, mechanics ya classical ilizaa calculus ya tofauti, jiometri symplectic, na mfumo wa Hamiltonian ambao unasisitiza mechanics ya quantum na uboreshaji wa kisasa.
---

## Mechanics ya Newton
### Sheria Tatu za Newton
| Sheria | Taarifa | Fomu ya Hisabati |
|-----|-------------------------------|
| **Kwanza (Inertia)** | Kitu kinasalia katika hali ya kupumzika au katika mwendo wa sare isipokuwa kikitekelezwa kwa nguvu | Ikiwa F_net = 0, basi v = mara kwa mara |
| **Pili (F = ma)** | Nguvu ni sawa na kuongeza kasi ya nyakati | **F** = m**a** = m(d²**x**/dt²) |
| **Tatu (Hatua-Matendo)** | Kila tendo lina mwitikio sawa na kinyume | **F**₁₂ = −**F**₂₁ |
### Michoro isiyo na Mwili
**Mchoro wa mwili huria** hutenga kitu na kuonyesha nguvu zote zinazotenda juu yake.
**Nguvu za kawaida:**
| Nguvu | Mfumo | Mwelekeo |
|-------|----------------------|
| Mvuto (karibu na Dunia) | F = mg | Chini |
| Nguvu ya kawaida | N | Perpendicular kwa uso |
| Msuguano (tuli) | f_s ≤ μ_s N | Inapinga mwendo unaokuja |
| Msuguano (kinetic) | f_k = μ_k N | Inapinga mwendo |
| Spring (sheria ya Hooke) | F = −kx | Kurejesha (kuelekea usawa) |
| Mvutano | T | Kando ya kamba/kamba |
| Buruta | F_d = ½C_d ρAv² | Inapinga kasi |
### Mfano Uliotumika: Zuia kwenye Tekeleza
Kizuizi cha m juu kwenye mwinuko usio na msuguano kwa pembe θ.
- Nguvu: mvuto (mg chini), nguvu ya kawaida (N perpendicular to surface)
- Punguza mvuto: mg sin θ (pamoja na mwinuko), mg cos θ (kwenye uso)
- N = mg cos θ (hakuna mwendo unaoendana na uso)
- Kuongeza kasi kwa mwelekeo: a = g dhambi θ
---

## Mbinu za Nishati
### Kazi na Nishati ya Kinetic
**Kazi** iliyofanywa kwa nguvu: W = ∫ **F** · d**r**
**Nadharia ya Kazi-Nishati:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Nishati Inayowezekana
| Nguvu | Nishati Inayowezekana | Vidokezo |
|-------|-------------------------|
| Mvuto (karibu na uso) | U = mgh | h = urefu juu ya kumbukumbu |
| Mvuto (jumla) | U = −GMm/r | Sifuri kwa infinity |
| Spring | U = ½ kx² | x = kuhamishwa kutoka kwa usawa |
| Umeme | U = kq₁q₂/r | Kama gharama: chanya U |
### Uhifadhi wa Nishati
Ikiwa tu nguvu za kihafidhina zitatenda: E = KE + PE = mara kwa mara
½mv₁² + U₁ = ½mv₂² + U₂
**Mfano Uliofanyiwa Kazi:** Mpira ulidondoka kutoka urefu h.
- Awali: KE = 0, PE = mgh
- Kabla tu ya kugonga ardhi: KE = ½mv², PE = 0
- Uhifadhi: mgh = ½mv² → v = √(2gh)
### Nguvu
P = dW/dt = **F** · **v** (kiwango cha kufanya kazi)
---

## Kasi na Migongano
### Kasi ya Mstari
**p** = m**v**
Sheria ya pili ya Newton (fomu mbadala): **F** = d**p**/dt
### Uhifadhi wa Kasi
Ikiwa hakuna nguvu za nje: kasi kamili huhifadhiwa.
| Aina ya Mgongano | KE Imehifadhiwa? | Kasi Imehifadhiwa? |
|-------------------------------|--------------------
| **Elastiki** | Ndiyo | Ndiyo |
| **Inayobadilika** | Hapana | Ndiyo |
| **Inayobadilika kabisa** | Hapana (hasara ya juu zaidi) | Ndiyo (vitu vinashikamana) |
**1D mgongano wa elastic:** Misa miwili m₁, m₂ yenye kasi za awali u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Kasi ya Angular
**L** = **r** × **p** = m(**r** × **v**)
Torque: **τ** = d**L**/dt = **r** × **F**
**Uhifadhi:** Ikiwa hakuna torati ya nje, kasi ya angular huhifadhiwa.
---

## Lagrangian Mechanics
Uundaji wa **Lagrangian** hubadilisha nguvu na nishati, kutoa mfumo wa kifahari zaidi na wa jumla.
### The Lagrangian
L = T - V (nishati ya kinetic minus nishati inayoweza kutokea)
### Kanuni ya Kitendo Kidogo (Kanuni ya Hamilton)
Njia halisi inayochukuliwa na mfumo kati ya nyakati t₁ na t₂ hupunguza (kwa usahihi zaidi, hufanya kusimama) **kitendo**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Milinganyo ya Euler-Lagrange
Hali δS = 0 mavuno:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
kwa kila uratibu wa jumla q.
**Mfano Uliofanyiwa Kazi:** Pendulum rahisi (urefu l, wingi m, pembe θ kutoka wima).
- T = ½ml²θ̇²
- V = −mgl cos θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl dhambi θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sin θ = 0 → θ̈ + (g/l) dhambi θ = 0
### Manufaa ya Mitambo ya Lagrangian
| Faida | Ufafanuzi |
|-----------|-------------|
| Kuratibu-kujitegemea | Inafanya kazi katika mfumo wowote wa kuratibu |
| Hushughulikia vikwazo kwa kawaida | Hakuna haja ya kuhesabu nguvu za vizuizi |
| Ulinganifu → uhifadhi | Nadharia ya Noether inaunganisha ulinganifu na kiasi kilichohifadhiwa |
| Inajumuisha kwa urahisi | Kwa nyanja, uhusiano, quantum mechanics |
---

## Hamiltonian Mechanics
Uundaji wa **Hamiltonian** ni uundaji upya wa mechanics ya Lagrangian ambayo hutumia nafasi na momenta (badala ya nafasi na kasi).
### The Hamiltonian
H = Σᵢ pᵢq̇ᵢ − L = T + V (kwa mifumo mingi ya mitambo)
ambapo pᵢ = ∂L/∂q̇ᵢ ni **muda wa jumla**.
### Milinganyo ya Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Hizi ni ODE za mpangilio wa 2n (vs n milinganyo ya pili ya Euler-Lagrange).
**Mfano Uliofanya Kazi:** Kisisitio cha Harmonic (wingi m, chemchemi mara kwa mara k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (kama inavyotarajiwa)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (Sheria ya Hooke)
### Mabano ya Poisson
Kwa chaguo za kukokotoa f(q, p) na g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Mali | Taarifa |
|----------|-----------|
| Mageuzi ya wakati | df/dt = {f, H} + ∂f/∂t |
| Uhifadhi | f imehifadhiwa ikiwa {f, H} = 0 (na ∂f/∂t = 0) |
| Mabano ya Msingi | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Muunganisho kwa mechanics ya quantum:** Mabano ya Poisson yanabadilika: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Sheria za Uhifadhi na Nadharia ya Noether
### Nadharia ya Noether
Kila ulinganifu unaoendelea wa Lagrangian unafanana na kiasi kilichohifadhiwa.
| Ulinganifu | Kiasi Kilichohifadhiwa |
|----------|-------------------|
| Tofauti ya tafsiri ya wakati | Nishati |
| Utofauti wa tafsiri za anga | Kasi ya mstari |
| Ukiukaji wa mzunguko | Kasi ya angular |
| Tofauti ya kipimo | Chaji ya umeme |
Hili ni mojawapo ya matokeo ya kina zaidi katika fizikia yote - inaunganisha jiometri ya muda wa anga na sheria za kimsingi za uhifadhi.
---

## Mienendo Imara ya Mwili
**mwili mgumu** ni kitu ambamo umbali wote wa ndani hubaki ukiwa haubadiliki.
### Dhana Muhimu
| Dhana | Mfumo | Maelezo |
|---------|---------|-------------|
| **Wakati wa hali** | I = Σmᵢrᵢ² au mimi = ∫r² dm | Upinzani wa kuongeza kasi ya mzunguko |
| **KE ya Mzunguko** | KE = ½Iω² | Nishati ya mzunguko |
| ** Kasi ya angular ** | L = Iω | Analogi ya mzunguko wa p = mv |
| **Torque** | τ = Ia | Analogi ya mzunguko wa F = ma |
### Nyakati za Inertia (Maumbo ya Kawaida)
| Muundo | Mhimili | Mimi |
|-------|------|---|
| Tufe Imara | Kupitia kituo | (2/5)MR² |
| Tufe tupu | Kupitia kituo | (2/3)MR² |
| Silinda imara | Kando ya mhimili | (1/2)MR² |
| Fimbo nyembamba | Kupitia katikati, perpendicular | (1/12)ML² |
| Fimbo nyembamba | Kupitia mwisho, perpendicular | (1/3)ML² |
| Diski | Kupitia katikati, perpendicular | (1/2)MR² |
---

## Orbital Mechanics
### Sheria za Kepler
| Sheria | Taarifa |
|-----|------------|
| **Kwanza (Ellipses)** | Sayari husogea katika duaradufu na Jua kwa mwelekeo mmoja |
| **Pili (Maeneo Sawa)** | Mstari kutoka Jua hadi sayari hufagia maeneo sawa kwa nyakati sawa |
| **Tatu (Harmonic)** | T² ∝ a³ (kipindi cha mraba sawia na mchemraba wa nusu-kuu mhimili) |
### Nishati ya Orbital
E = ½mv² − Gmm/r
| E | Aina ya Obiti |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hyperbolic (isiyofungwa) |
### Kasi ya Kuepuka
v_escape = √(2GM/R)
Kwa Dunia: v_escape ≈ 11.2 km/s
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Dhana ya Mitambo | Maombi |
|------------------|-------------|
| Sheria za Newton | Injini za fizikia katika uigaji, mchezo wa AI, roboti |
| Mbinu za Nishati | Mifano zinazotegemea nishati, mitandao ya Hopfield, mashine za Boltzmann |
| Mitambo ya Lagrangian | Mitandao ya neva yenye taarifa za fizikia, udhibiti bora, uboreshaji wa njia |
| Mitambo ya Hamilton | Mitandao ya neva ya Hamilton (HNNs), viunganishi vya ulinganifu vya kuiga |
| Sheria za uhifadhi | Upendeleo wa kufata neno katika miundo ya ML, mitandao ya neural sawa |
| Nadharia ya Noether | Kujifunza kwa mashine inayofahamu ulinganifu, kujifunza kwa kina kijiometri |
| Mienendo migumu ya mwili | Uigaji wa roboti, mienendo ya Masi, uhuishaji wa 3D |
| Mitambo ya Orbital | Nafasi ya setilaiti (GPS kwa ML inayotegemea eneo), muundo wa misheni ya anga |
| Nafasi ya awamu (Hamiltonian) | Kuelewa mifumo ya nguvu, mitandao ya vivutio |
| Mahesabu ya tofauti | Usafiri bora, uundaji wa uzalishaji (kulinganisha mtiririko) |
---

## Muhtasari
| Mfumo | Mlinganyo wa Msingi | Nguvu |
|-----------|--------------------------|
| Newtonian | **F** = m**a** | Intuitive, uchambuzi wa nguvu ya moja kwa moja |
| Lagrangi | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Bila kuratibu, hushughulikia vikwazo |
| Hamilton | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Muundo wa ulinganifu, unaunganishwa na QM |
| Sheria za uhifadhi | Nadharia ya Noether | Muunganisho wa kina wa ulinganifu-uhifadhi |
Mitambo ya kitamaduni sio tu kuhusu mipira inayoanguka na pendulum zinazobembea. Mifumo yake ya hisabati - Mekaniki ya Lagrangian na Hamiltonian - ni kati ya mawazo yenye ushawishi mkubwa katika sayansi yote. Hujumlisha kwa quantum mechanics, the field theory, na hata ujifunzaji wa kisasa wa mashine, ambapo miundo ya msingi ya nishati na mitandao ya neural yenye taarifa za fizikia huchota moja kwa moja kwenye uundaji huu wa karne nyingi.