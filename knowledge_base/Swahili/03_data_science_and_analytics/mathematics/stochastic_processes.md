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

# Michakato ya Stochastic
**mchakato wa kistokasi** ni mkusanyiko wa vigeu vya nasibu vilivyoorodheshwa kulingana na wakati (au nafasi). Ingawa nadharia ya uwezekano inachunguza matukio ya nasibu ya mtu binafsi, michakato ya kistochastiki huchunguza jinsi unasihi unavyobadilika kwa wakati. Wanatoa mfano wa bei za hisa, urefu wa foleni, kuenea kwa magonjwa, uzalishaji wa lugha na mienendo ya mafunzo ya miundo ya kujifunza kwa mashine.
---

## Misingi
### Ufafanuzi
Mchakato wa kistokasi {X_t : t ∈ T} ni familia ya vigeu vya nasibu vilivyofafanuliwa kwenye nafasi ya kawaida ya uwezekano. T ni **seti ya faharasa** (wakati):
- **Muda mahususi:** T = {0, 1, 2, ...}
- **Muda unaoendelea:** T = [0, ∞)
**nafasi ya hali** S ni seti ya thamani zinazowezekana ambazo X_t inaweza kuchukua.
### Sifa Muhimu
| Mali | Ufafanuzi |
|----------|------------|
| **Uwezo** | Usambazaji wa pamoja wa (X_{t₁}, ..., X_{tₖ}) sawa na (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Uhuru** | X_t haitegemei X_s kwa t ≠ s |
| **Ergodicity** | Wastani wa muda huungana na kuunganisha wastani |
| ** Mali ya Markov ** | Wakati ujao unategemea sasa tu, sio zamani |
| **Martingale** | Thamani inayotarajiwa ya siku zijazo ni sawa na thamani ya sasa |
---

## Markov Minyororo
**Mnyororo wa Markov** ni mchakato wa stochastic ambapo hali ya baadaye inategemea tu hali ya sasa (mali isiyo na kumbukumbu).
### Minyororo ya Markov ya Muda Maalum (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
**matriki ya mpito** P ina maingizo p_{ij} = P(nenda kwa j | kwa sasa iko i).
| Mali | Taarifa |
|----------|-----------|
| Jumla ya safu | Kila safu mlalo inajumlisha 1: Σⱼ p_{ij} = 1 |
| mpito wa n-hatua | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Usambazaji wa stationary | πP = π (eigenvector ya kushoto yenye eigenvalue 1) |
### Uainishaji wa Majimbo
| Muda | Ufafanuzi |
|------|-------------|
| **Inayojirudia** | Chain inarudi katika hali i pamoja na uwezekano 1 |
| **Muda mfupi** | Uwezekano usio sifuri wa kutorudi tena |
| **Kunyonya** | p_{ii} = 1 (ikishaingia, haikuachwa) |
| **Kipindi** | GCD ya nyakati za kurudi; kipindi 1 = mara kwa mara |
| **Kuwasiliana** | Mataifa i na j yanaweza kufikia kila mmoja |
### Usambazaji wa stationary
Kwa mnyororo wa Markov usioweza kupunguzwa, unaorudiwa chanya, usambazaji wa stationary π upo, ni wa kipekee, na unatosheleza:
πP = π, Σᵢ πᵢ = 1
**Tafsiri:** πᵢ = uwiano wa muda uliotumika katika hali i.
**Mfano Uliofanya Kazi:** Muundo wa hali ya hewa wenye hali {Jua, Mvua}.
P = [[0.9, 0.1], [0.5, 0.5]] (safu: kutoka kwa Jua, kutoka kwa Mvua)
Usambazaji wa stationary: πP = π
- π₁ = 0.9π₁ + 0.5π₂
- π₂ = 0.1π₁ + 0.5π₂
- π₁ + π₂ = 1
- Kutatua: π₁ = 5/6 ≈ 0.833, π₂ = 1/6 ≈ 0.167
### Muunganisho kwa Utulivu
Kwa mnyororo usioweza kupunguzwa, wa mara kwa mara, mzuri wa kujirudia:
- Pⁿ → Π (matrix yenye safu mlalo zote sawa na π) kama n → ∞
- **Muda wa kuchanganya:** Idadi ya hatua hadi usambazaji ukaribiane na π
- **Pengo la Spectral:** 1 − |λ₂| (ambapo λ₂ ni eigenvalue ya pili kwa ukubwa) huamua kasi ya kuchanganya
### Minyororo ya Markov ya Wakati Unaoendelea (CTMC)
Mipito hutokea kwa nyakati nasibu zinazotawaliwa na usambaaji mkubwa.
| Dhana | Maelezo |
|---------|-------------|
| **Kadiria matrix Q** | q_{ij} ≥ 0 kwa i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Uwezekano wa mpito** | P(t) = e^{Qt} (kielelezo cha matrix) |
| **Usambazaji wa stationary** | πQ = 0 |
| **Kushikilia muda** | Muda katika hali i ni Exp(−q_{ii}) |
---

## Matembezi ya Nasibu
**kutembea nasibu** ni njia inayoundwa na hatua za nasibu zinazofuatana.
### Matembezi Rahisi ya Nasibu
X_n = X_{n-1} + Z_n, ambapo Z_n ∈ {+1, −1} yenye uwezekano p, q = 1−p.
| Mali | p = 1/2 (ulinganifu) | p ≠ 1/2 (upendeleo) |
|----------|--------------------|------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Inarudi asili? | Ndiyo (pamoja na uwezekano 1) | Hapana (huondoka) |
| Inarudiwa? | Ndiyo (katika 1D na 2D) | Hapana |
### Tembea Nasibu katika Vipimo vya Juu
| Vipimo | Inarudiwa? | Intuition |
|-----------|-------------------------|
| 1D | Ndiyo | "Mtu mlevi huwa anapata njia ya kurudi nyumbani" |
| 2D | Ndiyo | "Ndege mlevi huwa anapata njia yake ya kurudi nyumbani" |
| 3D+ | Hapana | "Shomoro mlevi hapati njia ya kurudi nyumbani" |
### Muunganisho kwa Mwendo wa Brownian
Kuongeza matembezi bila mpangilio: acha S_n = ΣZ_i. Kisha kama saizi ya hatua → 0 na hatua → ∞:
S_{⌊nt⌋} / √n → B(t) (Mwendo wa Kikahawia, na nadharia ya Donsker)
---

## Mwendo wa Brownian
**Sondo la rangi ya hudhurungi** (Mchakato wa Wiener) B(t) ni kikomo cha muda usiobadilika cha matembezi bila mpangilio.
### Ufafanuzi
B(t) inatosheleza:
1. B(0) = 0
2. B (t) ina njia zinazoendelea
3. Viongezeo vya kujitegemea: B(t) − B(s) haitegemei B(s) − B(r) kwa r <s <t
4. B(t) − B(s) ~ N(0, t − s) (Ongezeko la Gaussian)
### Sifa Muhimu
| Mali | Taarifa |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | =t |
| Cov[B(s), B(t)] | = min(s, t) |
| Hakuna mahali pa kutofautisha | Njia zinaendelea lakini hazina derivative |
| Kipimo cha Fractal | Grafu ina mwelekeo wa Hausdorff 3/2 |
| Mali ya Markov | Wakati ujao unategemea tu nafasi ya sasa |
| Martingale | E[B(t) | F_s] = B(s) kwa s <t |
### Mwendo wa Kijiometri wa Brownian
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Huu ndio muundo wa kawaida wa bei za hisa katika mfumo wa Black-Scholes.
- μ: drift (inatarajiwa kurudi)
- σ: tete
---

## Taratibu za Poisson
**Mchakato wa Poisson** N(t) huhesabu idadi ya matukio yanayotokea katika [0, t].
### Ufafanuzi
N(t) ~ Poisson(λt), ambapo λ ni kiwango (matukio kwa kila wakati wa kitengo).
| Mali | Taarifa |
|----------|-----------|
| N(0) = 0 | - |
| Ongezeko la kujitegemea | Matukio katika vipindi tofauti ni huru |
| Viongezeo vya stationary | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = lat |
| Var[N(t)] | = lat |
| Nyakati za kuwasili | Imesambazwa kwa kiasi kikubwa: T_i ~ Exp(λ) |
### Ujumla
| Lahaja | Maelezo |
|---------|-------------|
| **Wasio na homogeneous** | Kiwango λ(t) hutofautiana kulingana na wakati |
| **Poisson Kiwanja** | Kila tukio lina ukubwa wa nasibu: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Poisson kipimo cha nasibu** | Pointi katika muda wa anga, si wakati tu |
| **Ongeza** | Aina nyingi za matukio na mwingiliano unaowezekana |
---

## Martingales
**martingale** ni mchezo wa haki: thamani inayotarajiwa ya siku zijazo, kutokana na maelezo yote ya sasa, ni sawa na thamani ya sasa.
### Ufafanuzi
{X_n} ni martingale kwa heshima na uchujaji {F_n} ikiwa:
1. X_n inaweza kupimika F_n (imebadilishwa)
2. E[|X_n|] < ∞ (inayounganishwa)
3. E[X_{n+1} | F_n] = X_n (mchezo wa haki)
| Lahaja | Hali | Tafsiri |
|---------|-----------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Mchezo wa haki |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Mchezo unaopendeza (unaovuma) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Mchezo usiopendeza (unaovuma) |
### Nadharia Muhimu
| Nadharia | Taarifa |
|---------|-----------|
| **Hiari ya kusimamisha** | Chini ya masharti, E[X_T] = E[X_0] kwa muda wa kusimama T |
| **Muunganisho** | Martingale iliyopakana huungana karibu hakika |
| **Usawa wa juu zaidi** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |
---

## Mbinu za Monte Carlo
**Njia za Monte Carlo** hutumia sampuli nasibu kukadiria idadi bainifu.
### Wazo la Msingi
Ili kukadiria E[f(X)] ambapo X ~ P:
1. Chora sampuli za N: x₁, x₂, ..., x_N kutoka kwa P
2. Kokotoa: Î = (1/N) Σᵢ f(xᵢ)
3. Kwa sheria ya idadi kubwa: Î → E[f(X)] kama N → ∞
**Hitilafu:** Hitilafu ya kawaida = σ_f / √N, ambapo σ_f² = Var[f(X)]
### Mbinu za Kupunguza Tofauti
| Mbinu | Wazo | Kuongeza kasi |
|-----------|------|---------|
| **Sampuli za umuhimu** | Sampuli kutoka kwa Q badala ya P, uzito kwa P/Q | Inaweza kuwa ya kushangaza |
| **Antithetic hutofautiana** | Tumia jozi (x, −x) ili kughairi tofauti | ~2x |
| **Udhibiti hutofautiana** | Ondoa chaguo la kukokotoa linalojulikana linalohusiana na f | Inatofautiana |
| **Sampuli zilizoimarishwa** | Gawanya kikoa, sampuli kila tabaka | Hupunguza tofauti |
| **Rao-Blackwell** | Hali ya takwimu za kutosha | Husaidia kila wakati |
---

## Markov Chain Monte Carlo (MCMC)
MCMC huunda mnyororo wa Markov ambao usambazaji wake wa stationary ndio usambazaji unaolengwa. Baada ya kipindi cha "kuchoma", sampuli za makadirio huchota kutoka kwa lengo.
### Algorithm ya Metropolis-Hastings
| Hatua | Kitendo |
|------|--------|
| 1 | Hali ya sasa: x_t |
| 2 | Pendekeza: x* ~ q(x* \| x_t) (usambazaji wa pendekezo) |
| 3 | Uwiano wa kukubalika: α = min(1, [π(x*)q(x_t\|x*))] / [π(x_t)q(x*\|x_t)]) |
| 4 | Kubali kwa uwezekano α: x_{t+1} = x* (kubali) au x_t (kataa) |
**Kesi maalum — Algoriti ya Metropolis:** Pendekezo la ulinganifu q(x*|x) = q(x|x*), kwa hivyo α = dakika(1, π(x*)/π(x_t)).
### Sampuli za Gibbs
Kesi maalum ya Metropolis-Hastings ambapo kila kigezo kinasasishwa kutoka kwa usambazaji wake kamili wa masharti.
Kwa lengo π(x₁, x₂, ..., xₖ):
1. Sampuli x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Sampuli x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Endelea kwa vigezo vyote
4. Rudia
| Mali | Taarifa |
|----------|-----------|
| Inakubali kila wakati | α = 1 (hakuna hatua ya kukataliwa) |
| Inahitaji | Uwezo wa sampuli kutoka kwa kila masharti kamili |
| Muunganisho | Imehakikishwa kwa minyororo isiyoweza kupunguzwa, ya mara kwa mara |
### Uchunguzi wa MCMC
| Uchunguzi | Kusudi |
|-----------|---------|
| **Fuatilia njama** | Cheki cha kuona cha kuchanganya na kusimama |
| **Uhusiano otomatiki** | Hupima utegemezi wa sampuli (unataka uunganisho otomatiki wa chini) |
| **Gelman-Rubin (R̂)** | Linganisha minyororo mingi; R̂ <1.05 inapendekeza muunganisho |
| **Ukubwa wa sampuli unaofaa** | N_eff = N / (1 + 2Σρₖ); akaunti za uunganisho otomatiki |
| **Kuchomwa moto** | Tupa sampuli za awali kabla ya mnyororo kufikia uthabiti |
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Mchakato wa Stochastic | Maombi |
|-------------------|-------------|
| Markov minyororo | PageRank (kutembea bila mpangilio kwenye grafu ya wavuti), uzalishaji wa maandishi (mifano ya n-gram), MCMC |
| Matembezi ya nasibu | Node2Vec na DeepWalk (vipachiko vya grafu), uchunguzi katika RL |
| Mwendo wa Brownian | Muundo wa bei ya hisa, mifano ya uenezaji katika AI ya uzalishaji |
| Michakato ya Poisson | Kuiga matukio ya kuwasili (mibofyo, kushindwa), nadharia ya foleni |
| Martingales | Hisabati ya kifedha, inayothibitisha muunganiko wa SGD (ukadirio wa stochastic) |
| Monte Carlo | Kukadiria maadili yanayotarajiwa, makisio ya Bayesian, mafunzo ya kuimarisha (tathmini ya sera) |
| MCMC (Metropolis-Hastings) | Sampuli za nyuma za Bayesian, upangaji uwezekano wa programu (Stan, PyMC) |
| Sampuli za Gibbs | Miundo ya mada (LDA), mitandao ya Bayesian, kuondoa sauti kwa picha |
| Uchunguzi wa MCMC | Kuhakikisha makisio ya kuaminika kutoka kwa mifano ya uwezekano |
---

## Muhtasari
| Mchakato | Nafasi ya Jimbo | Wakati | Mali muhimu |
|---------|--------------------|--------------|
| Markov mnyororo | Ya kipekee/inayoendelea | Ya kipekee/inayoendelea | Isiyo na kumbukumbu (mali ya Markov) |
| Kutembea bila mpangilio | ℤᵈ | Tofauti | Jumla ya i.i.d. hatua |
| Mwendo wa Brownian | ℝ | Kuendelea | Ongezeko la Gaussian, njia zinazoendelea |
| Mchakato wa Poisson | ℕ | Kuendelea | Mchakato wa kuhesabu na mapungufu makubwa |
| Martingale | ℝ | Ya kipekee/inayoendelea | Mchezo wa haki (E[X_{t+1}|F_t] = X_t) |
Michakato ya Stochastic ni hisabati ya nasibu kwa wakati. Zinasisitiza uelekezaji wa kisasa wa Bayesian (MCMC), ujifunzaji wa uimarishaji (michakato ya uamuzi wa Markov), uundaji mzalishaji (miundo ya uenezi), hisabati ya kifedha, na nadharia ya foleni. Kuelewa michakato hii hukupa zana za kuiga kutokuwa na uhakika kwa nguvu - sio tu kama muhtasari, lakini jinsi inavyobadilika.