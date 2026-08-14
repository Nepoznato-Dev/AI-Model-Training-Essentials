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

# Stochastic na Proseso
Ang **stochastic process** ay isang koleksyon ng mga random na variable na na-index ng oras (o espasyo). Habang pinag-aaralan ng probability theory ang mga indibidwal na random na kaganapan, ang mga proseso ng stochastic ay nag-aaral kung paano nagbabago ang randomness sa paglipas ng panahon. Nagmomodelo sila ng mga presyo ng stock, haba ng pila, pagkalat ng sakit, pagbuo ng wika, at dynamics ng pagsasanay ng mga modelo ng machine learning.
---

## Mga pundasyon
### Depinisyon
Ang stochastic na proseso {X_t : t ∈ T} ay isang pamilya ng mga random na variable na tinukoy sa isang karaniwang espasyo ng posibilidad. Ang T ay ang **index set** (oras):
- **Discrete-time:** T = {0, 1, 2, ...}
- **Continuous-time:** T = [0, ∞)
Ang **state space** S ay ang hanay ng mga posibleng value na maaaring kunin ng X_t.
### Mga Pangunahing Katangian
| Ari-arian | Kahulugan |
|----------|------------|
| **Stationarity** | Pinagsamang pamamahagi ng (X_{t₁}, ..., X_{tₖ}) katulad ng (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Pagsasarili** | X_t independiyente sa X_s para sa t ≠ s |
| **Ergodicity** | Ang mga average ng oras ay nagtatagpo sa mga average ng ensemble |
| **Markov property** | Ang hinaharap ay nakasalalay lamang sa kasalukuyan, hindi sa nakaraan |
| **Martingale** | Ang inaasahang halaga sa hinaharap ay katumbas ng kasalukuyang halaga |
---

## Mga Kadena ng Markov
Ang **Markov chain** ay isang stochastic na proseso kung saan ang hinaharap na estado ay nakadepende lamang sa kasalukuyang estado (memoryless property).
### Discrete-Time Markov Chains (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
Ang **transition matrix** P ay may mga entry na p_{ij} = P(pumunta sa j | kasalukuyang nasa i).
| Ari-arian | Pahayag |
|----------|-----------|
| Mga kabuuan ng hilera | Ang bawat hilera ay sumasama sa 1: Σⱼ p_{ij} = 1 |
| n-step na paglipat | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Nakatigil na pamamahagi | πP = π (kaliwang eigenvector na may eigenvalue 1) |
### Pag-uuri ng Estado
| Termino | Kahulugan |
|------|------------|
| **Paulit-ulit** | Ang kadena ay bumalik sa estado i na may posibilidad na 1 |
| **Palipas** | Non-zero na posibilidad na hindi na bumalik |
| **Sisipsip** | p_{ii} = 1 (kapag nakapasok, hindi na umalis) |
| **Panahon** | GCD ng mga oras ng pagbabalik; yugto 1 = aperiodic |
| **Nakikipag-usap** | Ang mga estadong i at j ay maaaring maabot ang isa't isa |
### Nakatigil na Pamamahagi
Para sa isang hindi mababawasan, positibong paulit-ulit na Markov chain, ang nakatigil na pamamahagi π ay umiiral, natatangi, at nakakatugon sa:
πP = π, Σᵢ πᵢ = 1
**Interpretasyon:** πᵢ = pangmatagalang proporsyon ng oras na ginugol sa estado i.
**Worked Example:** Weather model with states {Sunny, Rainy}.
P = [[0.9, 0.1], [0.5, 0.5]] (mga hilera: mula kay Sunny, mula kay Rainy)
Nakatigil na pamamahagi: πP = π
- π₁ = 0.9π₁ + 0.5π₂
- π₂ = 0.1π₁ + 0.5π₂
- π₁ + π₂ = 1
- Paglutas: π₁ = 5/6 ≈ 0.833, π₂ = 1/6 ≈ 0.167
### Convergence sa Stationarity
Para sa isang hindi mababawasan, aperiodic, positibong paulit-ulit na chain:
- Pⁿ → Π (matrix na may lahat ng row na katumbas ng π) bilang n → ∞
- **Tagal ng paghahalo:** Bilang ng mga hakbang hanggang ang pamamahagi ay malapit sa π
- **Spectral gap:** 1 − |λ₂| (kung saan ang λ₂ ay ang pangalawang pinakamalaking eigenvalue) ay tumutukoy sa bilis ng paghahalo
### Continuous-Time Markov Chains (CTMC)
Nagaganap ang mga transition sa mga random na oras na pinamamahalaan ng mga exponential distribution.
| Konsepto | Paglalarawan |
|---------|-------------|
| **Rate matrix Q** | q_{ij} ≥ 0 para sa i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Mga probabilidad ng paglipat** | P(t) = e^{Qt} (matrix exponential) |
| **Patuloy na pamamahagi** | πQ = 0 |
| **Holding time** | Ang oras sa estado i ay Exp(−q_{ii}) |
---

## Mga Random na Lakad
Ang **random walk** ay isang landas na nabuo sa pamamagitan ng sunud-sunod na random na mga hakbang.
### Simple Random Walk
X_n = X_{n-1} + Z_n, kung saan ang Z_n ∈ {+1, −1} na may probabilities p, q = 1−p.
| Ari-arian | p = 1/2 (simetriko) | p ≠ 1/2 (biased) |
|-----------------------|---------------------|--------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Babalik sa pinanggalingan? | Oo (may posibilidad 1) | Hindi (naanod palayo) |
| Paulit-ulit? | Oo (sa 1D at 2D) | Hindi |
### Random na Paglalakad sa Mas Matataas na Dimensyon
| Dimensyon | Paulit-ulit? | Intuwisyon |
|-----------|------------|-----------|
| 1D | Oo | "Ang isang lasing na lalaki ay laging nakakahanap ng kanyang daan pauwi" |
| 2D | Oo | "Ang isang lasing na ibon ay laging nakakahanap ng daan pauwi" |
| 3D+ | Hindi | "Ang lasing na maya ay hindi nakakahanap ng daan pauwi" |
### Koneksyon sa Brownian Motion
Pag-scale ng random na paglalakad: hayaan ang S_n = ΣZ_i. Pagkatapos bilang laki ng hakbang → 0 at mga hakbang → ∞:
S_{⌊nt⌋} / √n → B(t) (Brownian motion, sa pamamagitan ng Donsker's theorem)
---

## Brownian Motion
**Brownian motion** (Wiener process) Ang B(t) ay ang tuloy-tuloy na limitasyon sa oras ng isang random na paglalakad.
### Depinisyon
B(t) ay nagbibigay-kasiyahan:
1. B(0) = 0
2. Ang B(t) ay may tuluy-tuloy na mga landas
3. Independent increments: B(t) − B(s) is independent of B(s) − B(r) for r < s < t
4. B(t) − B(s) ~ N(0, t − s) (Gaussian increments)
### Mga Pangunahing Katangian
| Ari-arian | Pahayag |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Nowhere differentiable | Ang mga landas ay tuloy-tuloy ngunit walang derivative |
| Dimensyon ng fractal | Ang graph ay may sukat na Hausdorff 3/2 |
| Markov property | Ang hinaharap ay nakasalalay lamang sa kasalukuyang posisyon |
| Martingale | E[B(t) | F_s] = B(s) para sa s < t |
### Geometric Brownian Motion
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Ito ang karaniwang modelo para sa mga presyo ng stock sa Black-Scholes framework.
- μ: drift (inaasahang pagbabalik)
- σ: pagkasumpungin
---

## Mga Proseso ng Poisson
A **Proseso ng Poisson** Binibilang ng N(t) ang bilang ng mga kaganapang nagaganap sa [0, t].
### Depinisyon
N(t) ~ Poisson(λt), kung saan ang λ ay ang rate (mga kaganapan sa bawat yunit ng oras).
| Ari-arian | Pahayag |
|----------|-----------|
| N(0) = 0 | — |
| Mga independiyenteng pagtaas | Ang mga kaganapan sa magkahiwalay na pagitan ay independyente |
| Mga nakatigil na pagtaas | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | = λt |
| Var[N(t)] | = λt |
| Mga oras sa pagitan ng pagdating | Exponentially distributed: T_i ~ Exp(λ) |
### Paglalahat
| Variant | Paglalarawan |
|---------|-------------|
| **Hindi homogenous** | Nag-iiba ang rate λ(t) sa oras |
| **Compound Poisson** | Ang bawat kaganapan ay may random na laki: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Poisson random measure** | Mga puntos sa espasyo-oras, hindi lang oras |
| **Multivariate** | Maramihang uri ng kaganapan na may mga posibleng pakikipag-ugnayan |
---

## Martingales
Ang **martingale** ay isang patas na laro: ang inaasahang halaga sa hinaharap, na ibinigay sa lahat ng kasalukuyang impormasyon, ay katumbas ng kasalukuyang halaga.
### Depinisyon
Ang {X_n} ay isang martingale na may kinalaman sa pagsasala {F_n} kung:
1. Ang X_n ay F_n-measurable (inaangkop)
2. E[|X_n|] < ∞ (integrable)
3. E[X_{n+1} | F_n] = X_n (patas na laro)
| Variant | Kundisyon | Interpretasyon |
|---------|-----------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Patas na laro |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Paborableng laro (nagte-trend) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Hindi kanais-nais na laro (trending down) |
### Mga Pangunahing Teorema
| Teorama | Pahayag |
|---------|------------|
| **Opsyonal na paghinto** | Sa ilalim ng mga kundisyon, E[X_T] = E[X_0] para sa oras ng paghinto T |
| **Convergence** | Ang isang bounded martingale ay halos tiyak na nagtatagpo |
| **Maximal na hindi pagkakapantay-pantay** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob's) |
---

## Mga Paraan ng Monte Carlo
**Ang mga pamamaraan ng Monte Carlo** ay gumagamit ng random sampling upang tantyahin ang mga tiyak na dami.
### Pangunahing Ideya
Upang tantyahin ang E[f(X)] kung saan X ~ P:
1. Gumuhit ng N sample: x₁, x₂, ..., x_N mula sa P
2. Compute: Î = (1/N) Σᵢ f(xᵢ)
3. Ayon sa batas ng malalaking numero: Î → E[f(X)] bilang N → ∞
**Error:** Standard error = σ_f / √N, kung saan σ_f² = Var[f(X)]
### Mga Teknik sa Pagbawas ng Variance
| Teknik | Ideya | Bilis |
|-----------|------|---------|
| **Pagsa-sample ng kahalagahan** | Sample mula sa Q sa halip na P, timbang ng P/Q | Maaaring maging dramatiko |
| **Nag-iiba-iba ang antithetic** | Gumamit ng mga pares (x, −x) upang kanselahin ang pagkakaiba | ~2x |
| **Nag-iiba ang kontrol** | Ibawas ang function na alam na inaasahan na nauugnay sa f | Nag-iiba |
| **Stratified sampling** | Hatiin ang domain, sample ng bawat stratum | Binabawasan ang pagkakaiba |
| **Rao-Blackwell** | Kundisyon sa sapat na istatistika | Palaging tumutulong |
---

## Markov Chain Monte Carlo (MCMC)
Ang MCMC ay gumagawa ng isang Markov chain na ang nakatigil na pamamahagi ay ang target na pamamahagi. Pagkatapos ng "burn-in" na panahon, ang mga sample ay tinatayang kumukuha mula sa target.
### Metropolis-Hastings Algorithm
| Hakbang | Aksyon |
|------|--------|
| 1 | Kasalukuyang estado: x_t |
| 2 | Ipanukala: x* ~ q(x* \| x_t) (pamamahagi ng mungkahi) |
| 3 | Ratio ng pagtanggap: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Tanggapin nang may posibilidad na α: x_{t+1} = x* (tanggapin) o x_t (tanggihan) |
**Espesyal na kaso — Metropolis algorithm:** Symmetric proposal q(x*|x) = q(x|x*), kaya α = min(1, π(x*)/π(x_t)).
### Gibbs Sampling
Isang espesyal na kaso ng Metropolis-Hastings kung saan ina-update ang bawat variable mula sa buong kondisyonal na pamamahagi nito.
Para sa target na π(x₁, x₂, ..., xₖ):
1. Sample x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Sample x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Magpatuloy para sa lahat ng mga variable
4. Ulitin
| Ari-arian | Pahayag |
|----------|-----------|
| Palaging tumatanggap ng | α = 1 (walang hakbang sa pagtanggi) |
| Nangangailangan | Kakayahang mag-sample mula sa bawat buong kondisyon |
| Convergence | Ginagarantiya para sa hindi mababawasan, aperiodic chain |
### MCMC Diagnostics
| Diagnostic | Layunin |
|-----------|---------|
| **Trace plot** | Visual check para sa paghahalo at stationarity |
| **Autocorrelation** | Sinusukat ang sample dependence (gusto ng mababang autocorrelation) |
| **Gelman-Rubin (R̂)** | Ihambing ang maramihang mga kadena; Ang R̂ < 1.05 ay nagmumungkahi ng convergence |
| **Epektibong laki ng sample** | N_eff = N / (1 + 2Σρₖ); mga account para sa autocorrelation |
| **Burn-in** | Itapon ang mga paunang sample bago umabot sa stationarity ang chain |
---

## Kaugnayan sa Machine Learning at Data Science
| Proseso ng Stochastic | Application |
|-------------------|-------------|
| Mga kadena ng Markov | PageRank (random walk on web graph), text generation (n-gram models), MCMC |
| Random na paglalakad | Node2Vec at DeepWalk (mga pag-embed ng graph), paggalugad sa RL |
| Brownian motion | Pagmomodelo ng presyo ng stock, mga modelo ng pagsasabog sa generative AI |
| Mga proseso ng Poisson | Pagmomodelo ng mga pagdating ng kaganapan (mga pag-click, pagkabigo), teorya ng pagpila |
| Martingales | Financial mathematics, nagpapatunay ng convergence ng SGD (stochastic approximation) |
| Monte Carlo | Pagtatantya ng mga inaasahang halaga, Bayesian inference, reinforcement learning (pagsusuri ng patakaran) |
| MCMC (Metropolis-Hastings) | Bayesian posterior sampling, probabilistic programming (Stan, PyMC) |
| Gibbs sampling | Mga modelo ng paksa (LDA), mga network ng Bayesian, denoising ng imahe |
| Mga diagnostic ng MCMC | Tinitiyak ang maaasahang hinuha mula sa mga probabilistikong modelo |
---

## Buod
| Proseso | Kalawakan ng Estado | Oras | Key Property |
|---------|-------------|------|--------------|
| Markov chain | Discrete/tuloy-tuloy | Discrete/tuloy-tuloy | Walang memorya (Markov property) |
| Random na lakad | ℤᵈ | Discrete | Kabuuan ng i.i.d. hakbang |
| Brownian motion | ℝ | Tuloy-tuloy | Gaussian increments, tuloy-tuloy na mga landas |
| Proseso ng Poisson | ℕ | Tuloy-tuloy | Proseso ng pagbibilang na may mga exponential gaps |
| Martingale | ℝ | Discrete/tuloy-tuloy | Patas na laro (E[X_{t+1}|F_t] = X_t) |
Ang mga stochastic na proseso ay ang matematika ng randomness sa paglipas ng panahon. Pinatibay nila ang modernong Bayesian inference (MCMC), reinforcement learning (Markov decision process), generative modeling (diffusion models), financial mathematics, at queuing theory. Ang pag-unawa sa mga prosesong ito ay nagbibigay sa iyo ng mga tool upang dynamic na magmodelo ng kawalan ng katiyakan — hindi lamang bilang isang snapshot, ngunit habang ito ay nagbabago.