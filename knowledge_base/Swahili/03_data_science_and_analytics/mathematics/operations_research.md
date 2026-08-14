<!--
---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Utafiti wa Uendeshaji
Utafiti wa uendeshaji (OR) ni matumizi ya mbinu za hisabati katika kufanya maamuzi. Ilizaliwa wakati wa Vita vya Pili vya Dunia kwa ajili ya vifaa vya kijeshi, sasa inaboresha misururu ya ugavi, inaratibu mashirika ya ndege, meli za uwasilishaji wa njia, inadhibiti orodha na kugawa rasilimali katika kila sekta. AU hutoa zana za hisabati kwa ajili ya kufanya maamuzi bora zaidi chini ya vikwazo.
---

## Michanganyiko ya Upangaji wa Mistari
### Fomu ya Kawaida
Punguza cᵀx
Inategemea: Ax = b, x ≥ 0
### Miundo ya Kawaida ya LP
**Mchanganyiko wa Bidhaa:**
- Vigeu vya maamuzi: xⱼ = wingi wa bidhaa j ya kuzalisha
- Lengo: kuongeza faida Σ pⱼxⱼ
- Vikwazo: vikomo vya rasilimali Σ aᵢⱼxⱼ ≤ bᵢ
**Tatizo la Chakula:**
- Vigezo vya maamuzi: xⱼ = kiasi cha chakula j cha kununua
- Lengo: punguza gharama Σ cⱼxⱼ
- Vikwazo: mahitaji ya lishe Σ nᵢⱼxⱼ ≥ rᵢ
**Tatizo la Kuchanganya:**
- Vigeu vya uamuzi: xⱼ = uwiano wa kiungo j katika mchanganyiko
- Lengo: kupunguza gharama
- Vizuizi: mahitaji ya ubora (ukadiriaji wa octane, nguvu, n.k.)
### Mfano Uliotekelezwa: Mipango ya Uzalishaji
Kiwanda kinatengeneza bidhaa A na B.
- A inahitaji kazi ya saa 2, nyenzo ya kilo 1; faida $30
- B inahitaji kazi ya saa 1, nyenzo za kilo 3; faida $40
- Inapatikana: masaa 40 ya kazi, vifaa vya kilo 30
** Muundo:**
- Upeo: 30x_A + 40x_B
- Inategemea: 2x_A + x_B ≤ 40 (kazi)
- x_A + 3x_B ≤ 30 (nyenzo)
- x_A, x_B ≥ 0
**Suluhisho:** Wima za eneo linalowezekana: (0,0), (20,0), (18,4), (0,10)
- (0,0): faida = 0
- (20,0): faida = 600
- (18,4): faida = 700 ← mojawapo
- (0,10): faida = 400
---

## Tatizo la Usafiri
Kuhamisha bidhaa kutoka vyanzo vya m hadi maeneo n kwa gharama ya chini.
### Muundo
- Vigeu vya maamuzi: xᵢⱼ = kiasi kilichosafirishwa kutoka chanzo i hadi lengwa j
- Lengo: punguza Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Inategemea: Σⱼ xᵢⱼ = sᵢ (vikwazo vya ugavi)
- Σᵢ xᵢⱼ = dⱼ (vikwazo vya mahitaji)
- xᵢⱼ ≥ 0
### Mbinu za Ufumbuzi
| Mbinu | Maelezo | Ubora wa Suluhisho la Awali |
|--------|----------------------------------------|
| **Kona ya Kaskazini Magharibi** | Anza juu kushoto, tenga kwa pupa | Inawezekana lakini mara nyingi ni duni |
| **Ukadiriaji wa Vogel** | Zingatia gharama za adhabu | Suluhisho bora la awali |
| **MODI / Jiwe la Kukanyaga** | Boresha suluhisho la awali mara kwa mara | Hupata mojawapo |
### Mfano Uliofanya Kazi
| | D1 | D2 | D3 | Ugavi |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Mahitaji | 40 | 30 | 30 | 100 |
---

## Tatizo la Mgawo
Kuwagawia wafanyikazi n kazi za n (mmoja-mmoja) ili kupunguza gharama ya jumla.
### Muundo
- Vigeu vya maamuzi: xᵢⱼ ∈ {0, 1} (1 ikiwa mfanyakazi niliyemkabidhi kazi j)
- Punguza: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Kulingana na: Σⱼ xᵢⱼ = 1 (kila mfanyakazi anapata kazi moja)
- Σᵢ xᵢⱼ = 1 (kila kazi hupata mfanyakazi mmoja)
### Algorithm ya Hungarian
| Mali | Thamani |
|----------|-------|
| Utata wa wakati | O(n³) |
| Mojawapo? | Ndiyo |
| Mbinu | Kupunguza matrix + kifuniko cha chini zaidi |
**Hatua:**
1. Ondoa kiwango cha chini cha safu mlalo kutoka kwa kila safu
2. Ondoa viwango vya chini vya safu wima kutoka kwa kila safu
3. Funika sufuri zote na idadi ndogo ya mistari
4. Ikiwa mistari = n, mgawo bora unapatikana kati ya sufuri
5. Vinginevyo, kurekebisha matrix na kurudia
---

## Uboreshaji wa Mtiririko wa Mtandao
### Kiwango cha chini cha mtiririko wa Gharama
Kwa kuzingatia mtandao wenye uwezo na gharama kwenye kingo, tafuta mtiririko unaokidhi mahitaji kwa gharama ya chini zaidi.
** Muundo:**
- Punguza: Σ cᵢⱼxᵢⱼ
- Kwa kuzingatia: uhifadhi wa mtiririko katika kila nodi
- Vikwazo vya uwezo: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Njia Fupi Zaidi Kama Mtiririko wa Mtandao
Tatizo la njia fupi ni kesi maalum ya mtiririko wa gharama ya chini (tuma kitengo 1 kutoka s hadi t).
### Maombi
| Maombi | Muundo wa Mtandao |
|----------------------------|
| Mlolongo wa ugavi | Nodi = maghala, kingo = njia za usafirishaji |
| Mawasiliano | Nodi = ruta, kingo = viungo na bandwidth |
| Trafiki | Nodi = makutano, kingo = barabara zenye uwezo |
| Usimamizi wa mradi | CPM/PERT mitandao |
---

## Upangaji Nguvu
**Utayarishaji wa Nguvu (DP)** hutatua matatizo changamano kwa kuyagawanya katika matatizo madogo yanayopishana.
### Kanuni ya Bellman ya Ubora
Sera bora ina mali ambayo kwa hali yoyote ya awali na uamuzi, maamuzi yaliyobaki lazima yaunda sera bora kwa hali inayosababisha.
### Vipengele Muhimu
| Kipengele | Maelezo |
|---------|-------------|
| **Hatua** | Hatua ya uamuzi (hatua ya wakati, faharisi ya bidhaa) |
| **Jimbo** | Taarifa zinazohitajika kufanya uamuzi |
| **Uamuzi** | Chaguo lililofanywa katika kila hatua |
| **Rudia** | Thamani mojawapo katika hatua n kulingana na hatua n−1 |
### Matatizo ya Kawaida ya DP
| Tatizo | Kujirudia | Utata |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n-2) | O(n) yenye kumbukumbu |
| **Mkoba** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Njia fupi zaidi** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) au O(E logi V) |
| **Hariri umbali** | D(i,j) = min(D(i-1,j)+1, D(i,j−1)+1, D(i-i-1,j-1)+gharama) | O(mn) |
| **Mfululizo mrefu zaidi wa kawaida** | L(i,j) = L(i−1,j−1)+1 ikiwa inalingana, vinginevyo max(L(i-1,j), L(i,j−1)) | O(mn) |
| **Kuzidisha kwa mnyororo wa Matrix** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Mfano Uliofanyiwa Kazi: 0/1 Knapsack
Vipengee: {uzito: thamani} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Uwezo W = 7.
V(i, w) = thamani ya juu zaidi kwa kutumia vitu vya kwanza vya i na uwezo w
| mimi\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|--------|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Mojawapo: V(4, 7) = 23 (vipengee 1 na 4: uzito 2+5=7, thamani 12+11=23).
---

## Nadharia ya Kupanga foleni
Uchunguzi wa nadharia ya foleni - ni ya muda gani, unasubiri kwa muda gani na jinsi ya kupunguza zote mbili.
### Nukuu ya Kendall
A/B/c/K/N/D ambapo:
- A = mchakato wa kuwasili (M = Markovian/Poisson, D = uamuzi, G = jumla)
- B = mchakato wa huduma (chaguzi sawa)
- c = idadi ya seva
- K = uwezo (chaguo-msingi ∞)
- N = idadi ya watu (chaguo-msingi ∞)
- D = nidhamu (FIFO, LIFO, Kipaumbele)
### Foleni ya M/M/1 (Seva Moja)
| Kipimo | Mfumo |
|--------|----------|
| Matumizi | ρ = λ/μ |
| Wastani wa nambari katika mfumo | L = ρ/(1−ρ) |
| Muda wa wastani kwenye mfumo | W = 1/(μ−λ) |
| Idadi ya wastani kwenye foleni | L_q = ρ²/(1−ρ) |
| Muda wa wastani wa kusubiri | W_q = ρ/(μ−λ) |
ambapo λ = kiwango cha kuwasili, μ = kiwango cha huduma, ρ = matumizi.
### Foleni ya M/M/c (Seva Nyingi)
| Kipimo | Mfumo |
|--------|----------|
| Matumizi | ρ = λ/(cμ) |
| Uwezekano wa kusubiri (Erlang C) | P_w = fomula changamano inayohusisha ρ na c |
| Urefu wa wastani wa foleni | L_q = P_w · ρ/(1−ρ) |
### Sheria ya Ndogo
L = λW (wastani wa nambari katika mfumo = kiwango cha kuwasili × muda wa wastani)
Hii inashikilia mfumo WOWOTE wa kupanga foleni, bila kujali kuwasili/mgawanyo wa huduma.
### Mifano ya Maombi
| Hali | Mfano wa Foleni |
|----------|-------------|
| Kituo cha simu | M/M/c (c mawakala) |
| Maombi ya seva ya wavuti | M/M/1 au M/G/1 |
| Dharura ya hospitali | M/G/c na vipaumbele |
| Laini ya utengenezaji | Mtandao wa foleni |
| Kupanga CPU kwa Kompyuta | Kushiriki kichakataji cha M/M/1 |
---

## Miundo ya Mali
### Kiasi cha Agizo la Kiuchumi (EOQ)
Kiasi bora cha agizo ambacho kinapunguza jumla ya gharama za hesabu.
Q* = √(2DS/H)
| Tofauti | Maana |
|----------|---------|
| D | Mahitaji ya kila mwaka |
| S | Gharama ya kuagiza kwa agizo |
| H | Gharama ya kushikilia kwa kila kitengo kwa mwaka |
| Swali* | Kiasi bora cha agizo |
**Jumla ya gharama kwa Q*:** TC = √(2DSH)
### Viendelezi
| Mfano | Kiendelezi |
|-------|------------|
| **EOQ na punguzo ** | Punguzo la kiasi hubadilisha utendaji wa gharama |
| **Idadi ya agizo la uzalishaji** | Bidhaa zinazozalishwa hatua kwa hatua, hazijawasilishwa zote kwa wakati mmoja |
| **(s, Q) muundo** | Panga upya vitengo vya Q wakati hesabu inashuka hadi kiwango cha s |
| **(s, S) mfano** | Agiza hadi S wakati hesabu itashuka hadi s |
| **Muundo wa muuza magazeti** | Kipindi kimoja, mahitaji yasiyo na uhakika |
### Muundo wa Mchuuzi
Kiasi bora cha agizo kwa orodha ya bidhaa inayoweza kuharibika ya kipindi kimoja:
P(D ≤ Q*) = c_u / (c_u + c_o)
ambapo c_u = gharama ya chini (faida iliyopotea) na c_o = gharama ya ziada (taka).
---

## Kupanga
### Ratiba ya Duka la Kazi
| Nukuu | Maana |
|----------|---------|
| n/m/J/C_max | n kazi, m mashine, duka la kazi, punguza makespan |
| Duka la mtiririko | Kazi zote tembelea mashine kwa mpangilio sawa |
| Duka la kazi | Kila kazi ina mlolongo wake wa mashine |
| Fungua duka | Hakuna vikwazo vya kuagiza |
### Kanuni za Kipaumbele
| Kanuni | Maelezo | Athari |
|------|-------------|---------|
| FCFS | Njoo wa kwanza, wa kwanza kuhudumiwa | Sawa, lakini si bora |
| SPT | Muda mfupi zaidi wa usindikaji kwanza | Hupunguza kukamilika kwa wastani |
| EDD | Tarehe ya mapema ya kukamilisha kwanza | Hupunguza kiwango cha juu cha kuchelewa |
| CR | Uwiano muhimu (tarehe ya mwisho iliyobaki / wakati wa usindikaji) | Mizani |
| LPT | Muda mrefu zaidi wa kuchakata kwanza | Nzuri kwa makespan kwenye mashine sambamba |
### Algorithm ya Johnson (Duka la Mtiririko wa Mashine-2)
Kwa kazi za n kwenye mashine 2, kupunguza makespan:
1. Tafuta kazi kwa muda mfupi zaidi wa usindikaji
2. Ikiwa iko kwenye mashine 1, ipange kwanza; ikiwa kwenye mashine 2, ratibishe mwisho
3. Ondoa kazi hiyo na kurudia
Bora kwa mashine 2; NP-ngumu kwa mashine 3+.
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| AU Dhana | Maombi |
|-----------|-------------|
| Upangaji wa mstari | Ugawaji wa rasilimali, uboreshaji wa kwingineko, ugawaji wa bajeti ya matangazo |
| Usafiri/mgawo | Lojistiki, ulinganifu wa kushiriki safari, mgawo wa kazi |
| Mtiririko wa mtandao | Uboreshaji wa mnyororo wa ugavi, uelekezaji wa trafiki wa kituo cha data |
| Utayarishaji wa nguvu | Mpangilio wa mfuatano (bioinformatics), algorithm ya Viterbi (HMM), RL (mlingano wa Bellman) |
| Nadharia ya kupanga foleni | Upangaji wa uwezo wa seva, uundaji wa muda wa kusubiri, ugawaji wa rasilimali za wingu |
| Miundo ya hesabu | Omba ujumuishaji wa utabiri, ugavi ML |
| Kupanga | Ochestration ya bomba la ML, ratiba ya kazi ya GPU, ratiba ya utafutaji wa hyperparameta |
| Upangaji nambari kamili | Uteuzi wa kipengele (jomba), uteuzi wa mfano, muundo wa mtandao |
---

## Muhtasari
| Mada | Tatizo la Msingi | Mbinu muhimu |
|-------|-------------|------------|
| Miundo ya LP | Boresha lengo la mstari na vikwazo | Simplex, mambo ya ndani uhakika |
| Usafiri | Kusafirisha bidhaa kwa gharama ya chini | MODI, jiwe la kukanyagia |
| Kazi | Linganisha wafanyikazi na kazi | Algorithm ya Hungarian |
| Mtiririko wa Mtandao | mtiririko wa njia kupitia mtandao | Kanuni za mtiririko wa gharama nafuu |
| Utayarishaji wa Nguvu | Shida ndogo zinazopishana | Kanuni ya Bellman, kumbukumbu |
| Nadharia ya Kupanga foleni | Uchambuzi wa mstari wa kusubiri | M/M/1, Sheria ya Kidogo |
| Mali | Wakati na kiasi gani cha kuagiza | EOQ, muuzaji wa habari |
| Kupanga | Panga kazi kwenye mashine | Sheria za kipaumbele, algorithm ya Johnson |
Utafiti wa uendeshaji hubadilisha kufanya maamuzi kutoka kwa sanaa hadi sayansi. Kwa kutunga matatizo ya ulimwengu halisi kihisabati, AU hutoa masuluhisho yanayoweza kufaa zaidi (au yaliyo karibu kabisa) kwa vifaa, kuratibu, ugawaji wa rasilimali na matatizo ya kupanga ambayo yanaathiri kila sekta. Kwa wanasayansi wa data, AU mbinu hukamilisha ujifunzaji wa mashine: wakati ML inabashiri, AU inaagiza - na kwa pamoja, huunda msingi wa mifumo ya maamuzi ya akili.