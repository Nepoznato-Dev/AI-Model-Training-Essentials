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
# Pananaliksik sa Operasyon
Ang operations research (OR) ay ang aplikasyon ng mga pamamaraang matematikal sa paggawa ng desisyon. Ipinanganak noong Ikalawang Digmaang Pandaigdig para sa logistik ng militar, ino-optimize nito ngayon ang mga supply chain, nag-iskedyul ng mga airline, nagruruta ng mga fleet ng paghahatid, namamahala ng mga imbentaryo, at naglalaan ng mga mapagkukunan sa bawat industriya. Ang O ay nagbibigay ng mathematical toolkit para sa paggawa ng pinakamahusay na posibleng mga desisyon sa ilalim ng mga hadlang.
---

## Linear Programming Formulations
### Pamantayang Form
I-minimize ang cᵀx
Napapailalim sa: Ax = b, x ≥ 0
### Mga Karaniwang LP Formulation
**Halong Produkto:**
- Mga variable ng desisyon: xⱼ = dami ng produktong j na gagawin
- Layunin: i-maximize ang tubo Σ pⱼxⱼ
- Mga hadlang: mga limitasyon sa mapagkukunan Σ aᵢⱼxⱼ ≤ bᵢ
**Problema sa Diet:**
- Mga variable ng desisyon: xⱼ = dami ng pagkain j na bibilhin
- Layunin: bawasan ang gastos Σ cⱼxⱼ
- Mga hadlang: mga kinakailangan sa nutrisyon Σ nᵢⱼxⱼ ≥ rᵢ
** Problema sa Blending:**
- Mga variable ng desisyon: xⱼ = proporsyon ng sangkap j sa timpla
- Layunin: mabawasan ang gastos
- Mga hadlang: mga kinakailangan sa kalidad (rating ng oktano, lakas, atbp.)
### Nagtrabaho Halimbawa: Pagpaplano ng Produksyon
Ang isang pabrika ay gumagawa ng mga produkto A at B.
- Ang A ay nangangailangan ng 2 oras na paggawa, 1 kg na materyal; tubo $30
- Ang B ay nangangailangan ng 1 oras na paggawa, 3 kg na materyal; tubo $40
- Magagamit: 40 oras na paggawa, 30 kg na materyal
**Pagbuo:**
- I-maximize: 30x_A + 40x_B
- Napapailalim sa: 2x_A + x_B ≤ 40 (paggawa)
- x_A + 3x_B ≤ 30 (materyal)
- x_A, x_B ≥ 0
**Solusyon:** Mga vertice ng posible na rehiyon: (0,0), (20,0), (18,4), (0,10)
- (0,0): tubo = 0
- (20,0): tubo = 600
- (18,4): tubo = 700 ← pinakamainam
- (0,10): tubo = 400
---

## Problema sa Transportasyon
Paglipat ng mga kalakal mula sa m pinagmumulan patungo sa n destinasyon sa pinakamababang halaga.
### Pagbubuo
- Mga variable ng desisyon: xᵢⱼ = dami na ipinadala mula sa pinagmulan i hanggang sa destinasyon j
- Layunin: bawasan ang Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Napapailalim sa: Σⱼ xᵢⱼ = sᵢ (mga hadlang sa supply)
- Σᵢ xᵢⱼ = dⱼ (mga hadlang sa demand)
- xᵢⱼ ≥ 0
### Mga Paraan ng Solusyon
| Paraan | Paglalarawan | Kalidad ng Paunang Solusyon |
|--------|-------------|-------------|
| **Northwest Corner** | Magsimula sa itaas-kaliwa, maglaan nang buong kasakiman | Magagawa ngunit madalas mahirap |
| **Vogel's Approximation** | Isaalang-alang ang mga gastos sa parusa | Mas mahusay na paunang solusyon |
| **MODI / Stepping Stone** | Pahusayin ang paunang solusyon nang paulit-ulit | Naghahanap ng pinakamainam |
### Nagtrabahong Halimbawa
| | D1 | D2 | D3 | Supply |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Demand | 40 | 30 | 30 | 100 |
---

## Problema sa Takdang-Aralin
Pagtatalaga ng n manggagawa sa n trabaho (isa-sa-isa) upang mabawasan ang kabuuang gastos.
### Pagbubuo
- Mga variable ng desisyon: xᵢⱼ ∈ {0, 1} (1 kung manggagawang itinalaga ko sa trabaho j)
- Bawasan: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Napapailalim sa: Σⱼ xᵢⱼ = 1 (bawat manggagawa ay makakakuha ng isang trabaho)
- Σᵢ xᵢⱼ = 1 (bawat trabaho ay makakakuha ng isang manggagawa)
### Hungarian Algorithm
| Ari-arian | Halaga |
|----------|-------|
| Pagiging kumplikado ng oras | O(n³) |
| Pinakamainam? | Oo |
| Diskarte | Pagbabawas ng matrix + minimum na takip |
**Mga Hakbang:**
1. Ibawas ang mga minimum na row sa bawat row
2. Ibawas ang mga minimum na column sa bawat column
3. Takpan ang lahat ng mga zero na may pinakamababang bilang ng mga linya
4. Kung ang mga linya = n, ang pinakamainam na pagtatalaga ay matatagpuan sa mga zero
5. Kung hindi, ayusin ang matrix at ulitin
---

## Pag-optimize ng Daloy ng Network
### Minimum na Daloy ng Gastos
Dahil sa isang network na may mga kapasidad at gastos sa mga gilid, hanapin ang daloy na nakakatugon sa mga pangangailangan sa pinakamababang halaga.
**Pagbuo:**
- Bawasan: Σ cᵢⱼxᵢⱼ
- Napapailalim sa: pag-iingat ng daloy sa bawat node
- Mga limitasyon sa kapasidad: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Pinakamaikling Landas bilang Daloy ng Network
Ang pinakamaikling problema sa landas ay isang espesyal na kaso ng pinakamababang daloy ng gastos (magpadala ng 1 yunit mula s hanggang t).
### Mga Application
| Application | Modelo ng Network |
|-------------|--------------|
| Supply chain | Mga node = mga bodega, mga gilid = mga ruta ng pagpapadala |
| Komunikasyon | Mga node = mga router, mga gilid = mga link na may bandwidth |
| Trapiko | Mga node = mga intersection, mga gilid = mga kalsadang may kapasidad |
| Pamamahala ng proyekto | CPM/PERT network |
---

## Dynamic na Programming
Ang **Dynamic programming (DP)** ay lumulutas ng mga kumplikadong problema sa pamamagitan ng paghahati sa mga ito sa magkakapatong na mga subproblema.
### Prinsipyo ng Optimality ni Bellman
Ang pinakamainam na patakaran ay may pag-aari na anuman ang paunang estado at desisyon, ang natitirang mga desisyon ay dapat na bumubuo ng pinakamainam na patakaran para sa resultang estado.
### Mga Pangunahing Elemento
| Elemento | Paglalarawan |
|---------|-------------|
| **Yugto** | Desisyon point (time step, item index) |
| **Estado** | Impormasyong kailangan upang makagawa ng desisyon |
| **Desisyon** | Pagpipiliang ginawa sa bawat yugto |
| **Pag-ulit** | Pinakamainam na halaga sa yugto n sa mga tuntunin ng yugto n−1 |
### Mga Klasikong Problema sa DP
| Problema | Pag-ulit | Pagiging kumplikado |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) na may memoisasyon |
| **Knapsack** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Pinakamaikling landas** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) o O(E log V) |
| **I-edit ang distansya** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+gastusin) | O(mn) |
| **Pinakamahabang karaniwang kasunod** | L(i,j) = L(i−1,j−1)+1 kung tugma, kung hindi max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Pagpaparami ng chain ng matrix** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Nagtrabaho Halimbawa: 0/1 Knapsack
Mga item: {weight: value} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Kapasidad W = 7.
V(i, w) = max na halaga gamit ang first i item na may kapasidad na w
| i\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Pinakamainam: V(4, 7) = 23 (mga item 1 at 4: timbang 2+5=7, halaga 12+11=23).
---

## Teorya ng Pagpila
Pinag-aaralan ng teorya ng pagpila ang mga linya ng paghihintay — kung gaano katagal ang mga ito, gaano ka katagal maghintay, at kung paano bawasan ang pareho.
### Notasyon ni Kendall
A/B/c/K/N/D kung saan:
- A = proseso ng pagdating (M = Markovian/Poisson, D = deterministic, G = pangkalahatan)
- B = proseso ng serbisyo (parehong mga opsyon)
- c = bilang ng mga server
- K = kapasidad (default ∞)
- N = populasyon (default ∞)
- D = disiplina (FIFO, LIFO, Priyoridad)
### M/M/1 Queue (Single Server)
| Sukatan | Formula |
|--------|---------|
| Paggamit | ρ = λ/μ |
| Average na numero sa system | L = ρ/(1−ρ) |
| Average na oras sa system | W = 1/(μ−λ) |
| Average na numero sa pila | L_q = ρ²/(1−ρ) |
| Average na oras ng paghihintay | W_q = ρ/(μ−λ) |
kung saan λ = rate ng pagdating, μ = rate ng serbisyo, ρ = utilization.
### M/M/c Queue (Maramihang Server)
| Sukatan | Formula |
|--------|---------|
| Paggamit | ρ = λ/(cμ) |
| Probability of waiting (Erlang C) | P_w = kumplikadong formula na kinasasangkutan ng ρ at c |
| Average na haba ng pila | L_q = P_w · ρ/(1−ρ) |
### Batas ni Little
L = λW (average na numero sa system = rate ng pagdating × average na oras)
Ito ay para sa ANUMANG sistema ng pagpila, anuman ang pamamahagi ng pagdating/serbisyo.
### Mga Halimbawa ng Application
| Sitwasyon | Modelo ng Queue |
|----------|-------------|
| Call center | M/M/c (c mga ahente) |
| Mga kahilingan sa web server | M/M/1 o M/G/1 |
| Emergency sa ospital | M/G/c na may mga priyoridad |
| Linya ng paggawa | Network ng mga pila |
| Pag-iiskedyul ng computer CPU | M/M/1 pagbabahagi ng processor |
---

## Mga Modelo ng Imbentaryo
### Economic Order Quantity (EOQ)
Ang pinakamainam na dami ng order na nagpapaliit sa kabuuang halaga ng imbentaryo.
Q* = √(2DS/H)
| Variable | Ibig sabihin |
|----------|---------|
| D | Taunang demand |
| S | Gastos sa pag-order sa bawat order |
| H | Halaga ng paghawak bawat yunit bawat taon |
| Q* | Pinakamainam na dami ng order |
**Kabuuang gastos sa Q*:** TC = √(2DSH)
### Mga Extension
| Modelo | Extension |
|-------|-----------|
| **EOQ na may mga diskwento** | Binabago ng mga diskwento sa dami ang function ng gastos |
| **Dami ng order ng produksyon** | Mga item na ginawa nang unti-unti, hindi naihatid nang sabay-sabay |
| **(s, Q) model** | Muling ayusin ang mga Q unit kapag bumaba ang imbentaryo sa antas s |
| **(s, S) na modelo** | Mag-order ng hanggang S kapag bumaba ang imbentaryo sa s |
| **Modelo ng Newsvendor** | Single-period, hindi tiyak na demand |
### Modelo ng Newsvendor
Pinakamainam na dami ng order para sa isang-panahong nabubulok na imbentaryo:
P(D ≤ Q*) = c_u / (c_u + c_o)
kung saan c_u = menor de edad na gastos (nawalang tubo) at c_o = labis na gastos (basura).
---

## Pag-iiskedyul
### Pag-iiskedyul ng Job Shop
| Notasyon | Ibig sabihin |
|----------|---------|
| n/m/J/C_max | n trabaho, m makina, job shop, i-minimize makespan |
| Flow shop | Lahat ng trabaho ay bumibisita sa mga makina sa parehong pagkakasunud-sunod |
| Tindahan ng trabaho | Ang bawat trabaho ay may sariling machine sequence |
| Buksan ang tindahan | Walang mga hadlang sa pag-order |
### Mga Priyoridad na Panuntunan
| Panuntunan | Paglalarawan | Epekto |
|------|-------------|--------|
| FCFS | First come, first served | Patas, ngunit hindi pinakamainam |
| SPT | Pinakamaikling oras ng pagproseso muna | Pinaliit ang average na pagkumpleto |
| EDD | Pinakamaagang takdang petsa muna | Pinaliit ang maximum na pagkahuli |
| CR | Kritikal na ratio (natitira sa takdang petsa / oras ng pagproseso) | Balanse |
| LPT | Pinakamahabang oras ng pagproseso muna | Mabuti para sa makespan sa mga parallel machine |
### Johnson's Algorithm (2-Machine Flow Shop)
Para sa n trabaho sa 2 makina, pinapaliit ang makespan:
1. Hanapin ang trabaho na may pinakamaikling oras ng pagproseso
2. Kung ito ay nasa machine 1, iiskedyul muna ito; kung sa machine 2, i-schedule ito huling
3. Alisin ang trabahong iyon at ulitin
Pinakamainam para sa 2 makina; NP-hard para sa 3+ machine.
---

## Kaugnayan sa Machine Learning at Data Science
| O Konsepto | Application |
|-----------|-------------|
| Linear programming | Paglalaan ng mapagkukunan, pag-optimize ng portfolio, paglalaan ng badyet ng ad |
| Transportasyon/pagtatalaga | Logistics, ride-sharing matching, task assignment |
| Daloy ng network | Pag-optimize ng supply chain, pagruruta ng trapiko sa data center |
| Dynamic na programming | Sequence alignment (bioinformatics), Viterbi algorithm (HMMs), RL (Bellman equation) |
| Teorya ng pagpila | Pagpaplano ng kapasidad ng server, latency modelling, cloud resource allocation |
| Mga modelo ng imbentaryo | Pagsasama ng pagtataya ng demand, supply chain ML |
| Pag-iiskedyul | ML pipeline orchestration, GPU job scheduling, hyperparameter search scheduling |
| Integer programming | Pagpili ng tampok (binary), pagpili ng modelo, disenyo ng network |
---

## Buod
| Paksa | Pangunahing Problema | Pangunahing Paraan |
|-------|-------------|------------|
| Mga Pormulasyon ng LP | I-optimize ang linear na layunin na may mga hadlang | Simplex, panloob na punto |
| Transportasyon | Ipadala ang mga kalakal sa pinakamababang halaga | MODI, stepping stone |
| Takdang-aralin | Itugma ang mga manggagawa sa mga trabaho | Hungarian algorithm |
| Daloy ng Network | Daloy ng ruta sa isang network | Mga algorithm ng daloy ng min-cost |
| Dynamic na Programming | Mga magkakapatong na subproblema | Prinsipyo ni Bellman, memoisasyon |
| Teorya ng Pagpila | Pagsusuri ng linya ng paghihintay | M/M/1, Batas ni Little |
| Imbentaryo | Kailan at magkano ang order | EOQ, newsvendor |
| Pag-iiskedyul | Pagkakasunud-sunod ng mga trabaho sa mga makina | Mga panuntunan sa priyoridad, algorithm ni Johnson |
Binabago ng pananaliksik sa operasyon ang paggawa ng desisyon mula sa sining patungo sa agham. Sa pamamagitan ng pagbalangkas ng mga real-world na problema sa matematika, ang OR ay nagbibigay ng napatunayang pinakamainam (o malapit sa pinakamainam) na solusyon sa logistik, pag-iiskedyul, paglalaan ng mapagkukunan, at mga problema sa pagpaplano na nakakaapekto sa bawat industriya. Para sa mga data scientist, ang mga pamamaraan ng OR ay umaakma sa machine learning: habang ang ML ay hinuhulaan, OR nagrereseta — at magkasama, sila ang bumubuo sa pundasyon ng mga matalinong sistema ng pagpapasya.