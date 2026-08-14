<!--
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

-->
# Teorya ng Laro
Ang teorya ng laro ay ang matematika ng estratehikong pakikipag-ugnayan — mga sitwasyon kung saan ang iyong kinalabasan ay nakasalalay hindi lamang sa iyong sariling mga pagpipilian, ngunit sa mga pagpipilian ng iba. Mula sa mga digmaan sa pagpepresyo sa pagitan ng mga kumpanya hanggang sa karera ng armas nukleyar, mula sa mga online na auction hanggang sa evolutionary biology, ang teorya ng laro ay nagbibigay ng mga tool para sa pagsusuri ng salungatan at pakikipagtulungan. Lalo itong naging nauugnay sa machine learning sa pamamagitan ng multi-agent reinforcement learning, generative adversarial network (GAN), at disenyo ng mekanismo para sa mga online na platform.
---

## Mga Larong Madiskarteng-Anyo
### Depinisyon
Ang isang **strategic-form (normal-form) na laro** ay binubuo ng:
- Isang hanay ng mga manlalaro N = {1, 2, ..., n}
- Ang diskarte ay nagtatakda ng S₁, S₂, ..., Sₙ para sa bawat manlalaro
- Mga function ng Payoff na u₁, u₂, ..., uₙ na pagmamapa ng mga profile ng diskarte sa mga totoong numero
### Halimbawa: Prisoner's Dilemma
| | Makipagtulungan (C) | Depekto (D) |
|---|----------------|------------|
| **Makipagtulungan (C)** | (−1, −1) | (−3, 0) |
| **Depekto (D)** | (0, −3) | (−2, −2) |
| Pagsusuri | Resulta |
|----------|--------|
| Dominant na diskarte | Depekto (D dominates C para sa parehong mga manlalaro) |
| Nash ekwilibriyo | (D, D) na may kabayaran (−2, −2) |
| Social optimum | (C, C) na may kabayaran (−1, −1) |
| Dilemma | Ang indibidwal na rasyonalidad ay humahantong sa kolektibong irrationality |
### Higit pang Mga Klasikong Laro
**Labanan ng mga Kasarian:**
| | Opera | Football |
|---|-------|----------|
| Opera | (2, 1) | (0, 0) |
| Football | (0, 0) | (1, 2) |
Dalawang Nash equilibria: (Opera, Opera) at (Football, Football).
**Manok (Hawk-Dove):**
| | Lawin | kalapati |
|---|------|------|
| Lawin | (−10, −10) | (5, 0) |
| kalapati | (0, 5) | (1, 1) |
Dalawang Nash equilibria: (Lawin, Kalapati) at (Lawak, Lawin).
---

## Dominant na Istratehiya
| Konsepto | Kahulugan |
|---------|------------|
| **Mahigpit na nangingibabaw** | Ang Strategy sᵢ ay nagbibigay ng mas mataas na kabayaran kaysa sa anumang iba pang diskarte, anuman ang mga pagpipilian ng mga kalaban |
| **Mahina ang nangingibabaw** | Ang Strategy sᵢ ay nagbibigay ng hindi bababa sa kasing taas ng kabayaran gaya ng iba, at mahigpit na mas mataas para sa ilang profile ng kalaban |
| **Pinapangibabaw na diskarte** | Isang diskarte na hindi kailanman isang pinakamahusay na tugon |
**Paulit-ulit na pag-aalis ng mga dominated na diskarte:**
1. Alisin ang anumang mahigpit na pinangungunahan ng mga diskarte
2. Ulitin hanggang sa wala nang matatanggal
3. Kung mananatili ang isang profile ng diskarte, ito ang natatanging balanse ng Nash
---

## Nash Equilibrium
Ang **Nash equilibrium** ay isang profile ng diskarte kung saan walang manlalaro ang makakapagpahusay sa kanilang kabayaran sa pamamagitan ng unilateral na pagbabago sa kanilang diskarte.
### Depinisyon
(s₁*, s₂*, ..., sₙ*) ay isang Nash equilibrium kung para sa bawat manlalaro ay:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) para sa lahat ng sᵢ ∈ Sᵢ
### Paghahanap ng Nash Equilibria (2×2 na Laro)
**Pinakamahusay na paraan ng pagtugon:**
1. Para sa bawat column, salungguhitan ang pinakamahusay na tugon ng player 1
2. Para sa bawat hilera, salungguhitan ang pinakamahusay na tugon ng manlalaro 2
3. Ang mga cell kung saan parehong may salungguhit ay Nash equilibria
### Existence (Teorem ni Nash)
Ang bawat may hangganang laro ay may hindi bababa sa isang Nash equilibrium (maaaring sa magkahalong diskarte).
### Pinaghalong Istratehiya
Ang **halo-halong diskarte** ay isang probability distribution sa mga purong diskarte.
| Konsepto | Kahulugan |
|---------|------------|
| Pinaghalong diskarte σᵢ | Pamamahagi ng probabilidad sa Sᵢ |
| Pinaghalong diskarte NE | Walang manlalaro ang makakapagpabuti ng inaasahang kabayaran sa pamamagitan ng pagpapalit ng kanilang timpla |
| Suporta | Set ng mga purong diskarte na nilalaro na may positibong posibilidad |
**Nagtrabaho Halimbawa: Matching Pennies**
| | Mga ulo | Mga buntot |
|---|-------|-------|
| Mga ulo | (1, −1) | (−1, 1) |
| Mga buntot | (−1, 1) | (1, −1) |
Walang purong diskarte NE. Mixed NE: parehong naglalaro ng H at T na may posibilidad na ½ bawat isa.
---

## Minimax Theorem
### Mga Larong Zero-Sum
Sa isang **zero-sum game**, ang pakinabang ng isang manlalaro ay eksaktong pagkawala ng isa: u₁ + u₂ = 0.
### Ang Minimax Theorem ni Von Neumann
Para sa bawat may hangganang dalawang-manlalaro na zero-sum na laro:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
Ang **maximin** (pinakamahusay na worst-case para sa player 1) ay katumbas ng **minimax** (best worst-case para sa player 2). Ang karaniwang halaga na ito ay ang **halaga ng laro**.
### Paglutas ng Mga Larong Zero-Sum
Para sa 2×2 zero-sum game na may matrix:
| | L | R |
|---|---|---|
| T | isang | b |
| B | c | d |
Ang pinakamainam na pinaghalong diskarte ng Manlalaro 1: maglaro ng T na may posibilidad na p = (d−c)/((a−b)+(d−c))
Halaga ng laro: v = (ad−bc)/((a−b)+(d−c))
---

## Mga Larong Extensive-Form
Ang mga larong may sunud-sunod na galaw ay kinakatawan bilang **game tree**.
### Mga Pangunahing Konsepto
| Konsepto | Kahulugan |
|---------|------------|
| **Game tree** | Puno na nagpapakita ng lahat ng posibleng pagkakasunod-sunod ng mga galaw |
| **Impormasyon set** | Set ng mga node na hindi matukoy ng manlalaro |
| **Perpektong impormasyon** | Ang bawat set ng impormasyon ay isang singleton (lahat ng mga galaw ay napapansin) |
| **Subgame perfect NE** | Nash equilibrium sa bawat subgame |
| **Backward induction** | Lutasin mula sa dulo ng puno pabalik |
### Teorem ni Zermelo
Sa may hangganan, perpektong impormasyon, mga larong may dalawang manlalaro na walang pagkakataon: alinman sa isang manlalaro ay may diskarte sa panalong, o pareho silang mapipilitang gumuhit (hal., chess).
---

## Mga Larong Kooperatiba
Sa **cooperative games**, ang mga manlalaro ay maaaring bumuo ng mga umiiral na kasunduan at koalisyon.
### Katangiang Pag-andar
Ang isang larong kooperatiba ay tinutukoy ng isang **characteristic function** v: 2^N → ℝ, kung saan ang v(S) ay ang halaga ng coalition na maaaring makamit ng S.
| Ari-arian | Kahulugan |
|----------|------------|
| **Superadditive** | v(S ∪ T) ≥ v(S) + v(T) para sa magkahiwalay na S, T |
| **Matambok** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) para sa S ⊂ T |
### Ang Core
Ang **core** ay ang hanay ng mga alokasyon kung saan walang koalisyon ang maaaring mapabuti sa pamamagitan ng paghiwalay:
Core = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) para sa lahat ng S ⊂ N}
Maaaring walang laman ang core — kung saan walang umiiral na matatag na alokasyon.
### Halaga ng Shapley
Ang **Shapley value** ay nagbibigay ng natatanging patas na alokasyon batay sa mga marginal na kontribusyon:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Ari-arian | Pahayag |
|----------|-----------|
| Kahusayan | Σ φᵢ = v(N) (lahat ng halaga ay ibinahagi) |
| Symmetry | Ang mga pantay na nag-aambag ay nakakakuha ng pantay na kabayaran |
| Dummy player | Ang mga hindi nag-aambag ay nakakakuha ng zero |
| Pagkadagdag | φ(v + w) = φ(v) + φ(w) |
**Interpretasyon:** Ang halaga ng Shapley ng bawat manlalaro ay ang kanilang average na marginal na kontribusyon sa lahat ng posibleng pagkakasunud-sunod ng pagbuo ng koalisyon.
### Nagtrabahong Halimbawa
Tatlong manlalaro: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Manlalaro | Mga marginal na kontribusyon (na-average sa mga order) | Halaga ng Shapley |
|---------------------|------------------------------------------------|----------------|
| 1 | (100+50+70+70+50+0)/6 = 56.7 | 37.5 |
| 2 | (100+50+60+60+50+0)/6 | 27.5 |
| 3 | (100+70+60+70+60+0)/6 | 35.0 |
(Tiyak na kinakalkula gamit ang formula ng Shapley para sa bawat permutasyon.)
---

## Disenyo ng Mekanismo
Ang **Mechanism design** ay "inverse game theory" — sa halip na pag-aralan ang mga ibinigay na laro, magdisenyo ng mga laro na gumagawa ng gustong resulta.
### Ang Prinsipyo ng Paghahayag
Anumang mekanismo na nakakamit ng ninanais na resulta ay maaaring palitan ng **direktang revelation mechanism** kung saan ang pagsasabi ng katotohanan ay isang Nash equilibrium.
### Teorya ng Auction
| Uri ng Auction | Mga Panuntunan | Katumbas ng Kita |
|-------------|-------|---------------------|
| **First-price sealed-bid** | Ang pinakamataas na bidder ay nanalo, nagbabayad ng kanilang bid | Lahat ng karaniwang auction ay nagbubunga ng parehong inaasahang kita |
| **Second-price sealed-bid (Vickrey)** | Nanalo ang pinakamataas na bidder, nagbabayad ng pangalawang pinakamataas na bid | (sa ilalim ng mga independiyenteng pribadong halaga) |
| **Ingles (pataas)** | Tumataas ang presyo; unang tumanggap ng mga panalo | — |
| **Dutch (pababa)** | Bumaba ang presyo; unang tumanggap ng mga panalo | — |
### Vickrey Auction (Second-Price)
**Namumuno na diskarte:** I-bid ang iyong tunay na halaga.
| Ari-arian | Pahayag |
|----------|-----------|
| Makatotohanang pag-bid | Mahinang nangingibabaw na diskarte |
| Kahusayan | Napupunta ang item sa bidder na may pinakamataas na halaga |
| Kita | Parehong inaasahang kita gaya ng unang presyo (Revenue Equivalence Theorem) |
### Pinakamainam na Disenyo ng Auction (Myerson)
Ang auction na nagpapalaki ng kita:
- Naglalaan sa bidder na may pinakamataas na **virtual valuation**
- Nagtatakda ng reserbang presyo
- Virtual valuation: ψ(v) = v − (1−F(v))/f(v)
---

## Mga Koneksyon sa Machine Learning
### Mga Generative Adversarial Network (GAN)
Ang mga GAN ay isang larong may dalawang manlalaro sa pagitan ng generator G at discriminator D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Konsepto ng Teorya ng Laro | Katumbas ng GAN |
|--------------------|----------------|
| Dalawang-manlalaro na zero-sum game | Generator vs discriminator |
| Nash ekwilibriyo | Ang G ay bumubuo ng totoong data, ang D ay naglalabas ng ½ kahit saan |
| Minimax | Ang layunin ng GAN function |
| Pagbagsak ng mode | Pagkabigong maabot ang ekwilibriyo |
### Multi-Agent Reinforcement Learning (MARL)
| Konsepto | Aplikasyon ng MARL |
|---------|-----------------|
| Nash ekwilibriyo | Mga matatag na patakaran sa mga setting ng maraming ahente |
| Minimax | Matatag na mga patakaran laban sa mga kalaban na kalaban |
| Mga larong kooperatiba | Pagbubuo ng koalisyon, paglalaan ng gawain |
| Halaga ng Shapley | Credit assignment (anong ahente ang nag-ambag ng ano?) |
| Disenyo ng mekanismo | Pagdidisenyo ng mga insentibo sa mga multi-agent system |
| kathang-isip na dula | Learning algorithm converging sa Nash equilibrium |
### Iba pang Koneksyon sa ML
| Application | Tool sa Teorya ng Laro |
|-------------|-----------------|
| Disenyo ng ad auction (Google, Facebook) | Disenyo ng mekanismo, teorya ng auction |
| Disenyo ng marketplace (Uber, Airbnb) | Pagtutugma ng teorya, disenyo ng mekanismo |
| Katatagan ng kalaban | Zero-sum na laro sa pagitan ng attacker at defender |
| Patas na dibisyon | Shapley value, walang inggit na alokasyon |
| Federated learning | Teorya ng larong kooperatiba para sa pagsukat ng kontribusyon |
| Mga sistema ng rekomendasyon | Disenyo ng mekanismo para sa matapat na preference elicitation |
---

## Buod
| Konsepto | Pangunahing Ideya | Susing Resulta |
|---------|-----------|------------|
| Mga larong madiskarteng anyo | Mga manlalaro, diskarte, kabayaran | Game matrix representasyon |
| Mga dominanteng estratehiya | Pinakamahusay anuman ang iba | Inulit na pag-aalis |
| Nash ekwilibriyo | Walang kumikitang unilateral deviation | Umiiral sa bawat larong may hangganan |
| Pinaghalong diskarte | I-randomize ang mga aksyon | Nash's existence theorem |
| Minimax | Pinakamahusay na pinakamasamang kaso (zero-sum) | Ang minimax theorem ni Von Neumann |
| Malawak na anyo | Mga sunud-sunod na galaw | Paatras na induction, subgame perfection |
| Mga larong kooperatiba | Nagbubuklod na mga koalisyon | Core, halaga ng Shapley |
| Disenyo ng mekanismo | Magdisenyo ng mga laro para sa mga kinalabasan | Prinsipyo ng paghahayag, pinakamainam na mga auction |
| Teorya ng auction | Pagbebenta sa pamamagitan ng kumpetisyon | Katumbas ng kita, Vickrey auction |
Ang teorya ng laro ay ang matematika ng madiskarteng pag-iisip. Sa isang mundong lalong nagiging populasyon ng mga nakikipag-ugnayang ahente ng AI, mga automated na marketplace, at mga adversarial system, ang teorya ng laro ay nagbibigay ng mahalagang toolkit para sa paghula ng kilos, pagdidisenyo ng mga mekanismo, at pagbuo ng matatag na multi-agent system. Para sa mga data scientist, ipinapaliwanag nito kung paano gumagana ang mga GAN, kung paano nagkakaroon ng bilyun-bilyong kita ang mga online auction, at kung paano bumuo ng mga AI system na mahusay na gumaganap sa mga mapagkumpitensyang kapaligiran.