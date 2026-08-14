<!--
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

-->
# Teorya ng Impormasyon
Ang teorya ng impormasyon, na itinatag ni Claude Shannon noong 1948, ay binibilang ang impormasyon mismo. Magkano ang sinasabi sa iyo ng isang mensahe? Magkano ang maaari mong i-compress ng data? Gaano ka kabilis makipag-usap sa isang maingay na channel? Ang mga tanong na ito ay may tumpak na mga sagot sa matematika. Higit pa sa komunikasyon, ang teorya ng impormasyon ay naging pundasyon sa pag-aaral ng makina — ang cross-entropy ay ang default na pagkawala ng function para sa pag-uuri, ang KL divergence ay sumusukat sa pagkakatulad ng pamamahagi, at ang mutual na impormasyon ay nagtutulak sa pagpili ng tampok.
---

## Entropy
Sinusukat ng **Entropy** ang average na kawalan ng katiyakan o "sorpresa" ng isang random na variable.
### Shannon Entropy (Discrete)
Para sa isang discrete random variable X na may probability mass function p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Mga Unit: **bits** (kapag gumagamit ng log₂) o **nats** (kapag gumagamit ng ln).
| Pamamahagi | Entropy | Intuwisyon |
|-------------|---------|-----------|
| Patas na barya (p = 0.5, 0.5) | 1 bit | Pinakamataas na kawalan ng katiyakan para sa binary na kinalabasan |
| May kinikilingang barya (p = 0.9, 0.1) | 0.469 bits | Hindi gaanong nakakagulat — karamihan ay mga ulo |
| Deterministic (p = 1, 0) | 0 bits | Walang katiyakan sa lahat |
| Makatarungang mamatay (6 na panig) | 2.585 bits | Higit pang mga resulta = higit pang kawalan ng katiyakan |
| Uniform sa ibabaw n mga resulta | log₂(n) bits | Pinakamataas na entropy para sa n kinalabasan |
### Mga Katangian ng Entropy
| Ari-arian | Pahayag |
|----------|-----------|
| Non-negatibiti | H(X) ≥ 0 |
| Pinakamataas | H(X) ≤ log₂(\|X\|) na may pagkakapantay-pantay para sa pare-parehong pamamahagi |
| Panuntunan ng chain | H(X, Y) = H(X) + H(Y \| X) |
| Binabawasan ng conditioning | H(X \| Y) ≤ H(X) |
| Lukong | Ang H ay isang malukong function ng probability distribution |
### Differential Entropy (Patuloy)
Para sa tuluy-tuloy na random na variable X na may density p(x):
h(X) = −∫ p(x) log p(x) dx
Hindi tulad ng discrete entropy, ang differential entropy ay maaaring **negatibo**.
| Pamamahagi | Differential Entropy |
|-------------|---------------------|
| Uniporme sa [a,b] | log(b − a) |
| Normal N(μ, σ²) | (1/2) log(2πeσ²) |
| Exponential(λ) | 1 − ln(λ) |
---

## Pinagsamang, Kondisyon, at Mutual na Impormasyon
### Pinagsamang Entropy
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Sinusukat ang kabuuang kawalan ng katiyakan ng pares (X, Y).
### Conditional Entropy
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Sinusukat ang natitirang kawalan ng katiyakan tungkol sa Y pagkatapos obserbahan ang X.
### Impormasyon sa Mutual
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Sinusukat kung gaano karaming sinasabi sa iyo ng pag-alam sa X tungkol sa Y (at kabaliktaran).
| Ari-arian | Pahayag |
|----------|-----------|
| Non-negatibiti | I(X; Y) ≥ 0 |
| Symmetry | I(X; Y) = I(Y; X) |
| Kaugnayan sa entropy | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Kaugnayan sa joint | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Kalayaan | I(X; Y) = 0 kung ang X at Y ay independyente |
| Impormasyon sa sarili | I(X; X) = H(X) |
### Visual: Ang Entropy Diagram
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

## KL Divergence
Ang **Kullback-Leibler (KL) divergence** ay sumusukat kung gaano kaiba ang isang distribusyon sa isa pa.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Ari-arian | Pahayag |
|----------|-----------|
| Non-negatibiti | D_KL(P \|\| Q) ≥ 0 (Hindi pagkakapantay-pantay ni Gibbs) |
| Pagkakakilanlan | D_KL(P \|\| Q) = 0 kung P = Q |
| Kawalaan ng simetrya | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) sa pangkalahatan |
| Hindi isang sukatan | Nabigo ang symmetry at hindi pagkakapantay-pantay ng tatsulok |
**Interpretasyon:** Ang D_KL(P || Q) ay ang dagdag na bilang ng mga bit na kailangan para mag-encode ng data mula sa P gamit ang isang code na na-optimize para sa Q.
### Relasyon sa Iba Pang Dami
| Relasyon | Formula |
|-------------|---------|
| Cross-entropy | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Mutual na impormasyon | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| Kondisyon KL | D_KL(P(Y\|X) \|\| Q(Y\|X)) na na-average sa X |
---

## Cross-Entropy
**Cross-entropy** sa pagitan ng mga distribusyon P at Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Cross-Entropy bilang isang Loss Function
Sa pag-uuri, ang P ay ang tunay na pamamahagi (one-hot na naka-encode na label) at ang Q ay ang hinulaang pamamahagi ng modelo.
**Binary cross-entropy (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Categorical cross-entropy:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Sitwasyon | y (totoo) | ŷ (nahula) | Pagkawala |
|----------|----------|----------------|------|
| Tama, tiwala | 1 | 0.95 | 0.051 |
| Tama, hindi sigurado | 1 | 0.55 | 0.598 |
| Mali, tiwala | 1 | 0.05 | 2.996 |
| Mali, hindi sigurado | 1 | 0.45 | 0.799 |
Ang pag-minimize ng cross-entropy ay katumbas ng pagliit ng KL divergence mula sa tunay na distribusyon — kung kaya't ito ay gumagana nang mahusay bilang isang loss function.
---

## Kapasidad ng Channel
### Modelo ng Channel ng Komunikasyon
```
X → [Channel] → Y
```

- X: input random variable
- Y: random na variable ng output
- Channel: tinukoy ng mga kondisyong probabilidad p(y|x)
### Ang Maingay na Channel Coding Theorem ni Shannon
Para sa isang channel na may kapasidad C, kung ang transmission rate R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, ang maaasahang komunikasyon ay imposible.
**Kasya ng channel:**
C = max_{p(x)} I(X; Y)
### Mahahalagang Halimbawa ng Channel
| Channel | Paglalarawan | Kapasidad |
|---------|-------------|----------|
| **Binary symmetric (BSC)** | I-flip ang bawat bit na may posibilidad na p | 1 − H(p) bits |
| **Binary erasure (BEC)** | Binura ang bawat bit na may posibilidad na ε | 1 − ε bits |
| **Gaussian (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bits |
| **walang ingay na binary** | Perpektong paghahatid | 1 bit |
---

## Source Coding at Compression
### Source Coding Theorem
Ang average na bilang ng mga bit na kailangan para mag-encode ng source ay nililimitahan sa ibaba ng entropy nito:
L ≥ H(X)
Ang pinakamainam na code ay nakakamit ng L ≈ H(X).
### Huffman Coding
Isang **prefix-free** code na nagtatalaga ng mas maiikling code sa mas malamang na mga simbolo.
| Simbolo | Probability | Huffman Code | Haba |
|--------|-------------|-------------|--------|
| Isang | 0.5 | 0 | 1 |
| B | 0.25 | 10 | 2 |
| C | 0.125 | 110 | 3 |
| D | 0.125 | 111 | 3 |
Average na haba: 0.5(1) + 0.25(2) + 0.125(3) + 0.125(3) = 1.75 bits/simbolo
Entropy: H = 1.75 bits/simbolo (pinakamainam sa kasong ito!)
### Lossless vs Lossy Compression
| Uri | Prinsipyo | Mga halimbawa | Limitahan |
|------|-----------|----------|-------|
| **Hindi nawawala** | Alisin ang statistical redundancy | ZIP, PNG, FLAC | Entropy rate H(X) |
| **Lossy** | Alisin ang perceptual na walang kaugnayang impormasyon | JPEG, MP3, H.264 | Rate-distortion function R(D) |
**Rate-distortion theory:** Para sa lossy compression na may maximum distortion D, ang minimum na rate ay R(D) = min I(X; X̂) napapailalim sa E[d(X, X̂)] ≤ D.
---

## Mga Koneksyon sa Iba Pang Mga Patlang
### Teorya ng Impormasyon at Thermodynamics
| Konsepto | Teorya ng Impormasyon | Thermodynamics |
|----------------------|--------------------|----------------|
| Entropy | Shannon entropy H(X) | Boltzmann entropy S = k_B ln W |
| Pinakamataas na entropy | Unipormeng pamamahagi | Thermal equilibrium |
| KL divergence | Pagkakaiba sa pamamahagi | Libreng pagkakaiba sa enerhiya |
| Mutual na impormasyon | Nakabahaging impormasyon | Mga ugnayan sa mga pisikal na sistema |
Magkapareho ang mga anyong matematikal — sadyang hiniram ni Shannon ang terminong "entropy" mula sa statistical mechanics.
### Teorya at Istatistika ng Impormasyon
| Konsepto | Application |
|---------|-------------|
| Pinakamataas na posibilidad | Katumbas ng pagliit ng KL divergence mula sa empirical hanggang sa pamamahagi ng modelo |
| Impormasyon ng Fisher | Curvature ng KL divergence; lower bound sa estimator variance (Cramér-Rao) |
| Minimum na haba ng paglalarawan (MDL) | Pagpili ng modelo sa pamamagitan ng pagliit ng kabuuang haba ng pag-encode |
| AIC / BIC | Tinatayang pamantayan sa pagpili ng modelo na nakabatay sa KL |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng IT | ML Application |
|-----------|----------------|
| Pagkawala ng cross-entropy | Default na pagkawala ng klasipikasyon (binary at multi-class) |
| KL divergence | Pagkawala ng VAE (termino ng regularisasyon), pagtutugma ng pamamahagi, paglilinis |
| Mutual na impormasyon | Pagpili ng tampok (MIFS), pagkatuto ng representasyon (InfoMax), pagkakabukod |
| Entropy | Decision tree splitting criterion (nakuha ng impormasyon), paggalugad sa RL (maximum entropy RL) |
| Kapasidad ng channel | Pagiging kumplikado ng komunikasyon, pag-unawa sa mga hangganan ng generalization |
| Source coding | Data compression para sa storage at transmission, mahusay na pag-encode |
| Pinakamataas na entropy | MaxEnt classifiers, naunang pagpili sa Bayesian inference |
| Rate-distortion | Pag-unawa sa mga trade-off sa lossy compression, quantization sa mga neural network |
| Impormasyon ng Fisher | Natural na gradient descent, pag-unawa sa sensitivity ng parameter |
| MDL / AIC / BIC | Pagpili ng modelo, pinipigilan ang overfitting |
---

## Buod
| Dami | Formula (discrete) | Ibig sabihin |
|----------|--------------------|---------|
| Entropy H(X) | −Σ p(x) log p(x) | Average na kawalan ng katiyakan |
| Pinagsamang entropy H(X,Y) | −Σ p(x,y) log p(x,y) | Kabuuang kawalan ng katiyakan ng pares |
| Conditional entropy H(Y\|X) | H(X,Y) − H(X) | Ang natitirang kawalan ng katiyakan tungkol sa Y na ibinigay X |
| Mutual na impormasyon I(X;Y) | H(X) − H(X\|Y) | Impormasyong ibinahagi sa pagitan ng X at Y |
| KL divergence D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | "Distansya" sa pagitan ng mga pamamahagi |
| Cross-entropy H(P,Q) | −Σ P(x) log Q(x) | Gastos sa pag-encode gamit ang maling pamamahagi |
| Kapasidad ng channel C | max I(X;Y) | Pinakamataas na maaasahang rate ng komunikasyon |
Ang teorya ng impormasyon ay nagbibigay ng mga pangunahing limitasyon ng kung ano ang maaaring matutunan, i-compress, at ipaalam. Para sa mga practitioner ng machine learning, ipinapaliwanag nito kung bakit gumagana ang cross-entropy bilang loss function, kung paano sukatin ang kalidad ng mga natutunang representasyon, at kung paano pag-isipan ang trade-off sa pagitan ng pagiging kumplikado ng modelo at pagkakaakma ng data. Ang mga insight ni Shannon mula 1948 ay nananatiling may kaugnayan sa modernong AI tulad ng mga ito sa telekomunikasyon.