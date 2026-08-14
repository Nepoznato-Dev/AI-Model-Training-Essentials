<!--
---
# Metadata
title: "Real Analysis"
description: "Sequences and series, limits, continuity, differentiability, Riemann and Lebesgue integration, metric spaces, uniform convergence, and measure theory"
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
    changes: "Initial deep-dive into real analysis"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [real-analysis, sequences, series, limits, continuity, integration, metric-spaces, measure-theory, convergence]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Tunay na Pagsusuri
Ang tunay na pagsusuri ay ang mahigpit na pundasyon ng calculus. Bagama't itinuturo sa iyo ng panimulang calculus kung paano mag-compute ng mga derivatives at integral, ang tunay na pagsusuri ay nagtatanong *bakit* gumagana ang mga diskarteng ito — at kapag nabigo ang mga ito. Nagbibigay ito ng tumpak na mga kahulugan ng mga limitasyon, pagpapatuloy, convergence, at integration na sumasailalim sa probability theory, functional analysis, optimization, at ang mga theoretical na garantiya sa likod ng machine learning algorithm.
---

## Mga Sequence at Serye
### Mga pagkakasunud-sunod
Ang **sequence** ay isang nakaayos na listahan ng mga totoong numero (aₙ)ₙ₌₁^∞. Ang pangunahing tanong ay: ang sequence **nagtatagpo** sa isang limitasyon?
**Kahulugan ng convergence:** Ang isang sequence (aₙ) ay nagtatagpo sa L kung para sa bawat ε > 0, mayroong N na para sa lahat n > N: |aₙ − L| < ε.
| Konsepto | Kahulugan | Halimbawa |
|---------|------------|---------|
| **Convergent** | lim aₙ = L umiiral at may hangganan | aₙ = 1/n → 0 |
| **Divergent** | Hindi nagtatagpo | aₙ = (−1)ⁿ oscillates |
| **Divergent sa ∞** | ang isangₙ ay lumalaki nang walang nakatali | aₙ = n² → ∞ |
| **Bounded** | \|aₙ\| ≤ M para sa ilang M | Bawat convergent sequence ay may hangganan |
| **Monotone** | Alinman sa palaging hindi bumababa o hindi tumataas | aₙ = 1 − 1/n ay tumataas |
| **Cauchy sequence** | ∀ε > 0, ∃N: ∀m,n > N, \|aₘ − aₙ\| < ε | Sa ℝ, Cauchy ⟺ convergent |
**Mga pangunahing teorema:**
- **Monotone Convergence Theorem:** Ang bawat bounded monotone sequence ay nagtatagpo
- **Bolzano-Weierstrass Theorem:** Ang bawat bounded sequence ay may convergent subsequence
- **Pagkakakumpleto ng ℝ:** Ang bawat Cauchy sequence sa ℝ ay nagtatagpo (ito ay nakikilala ang ℝ sa ℚ)
### Serye
Ang **serye** ay ang kabuuan ng isang sequence: Σₙ₌₁^∞ aₙ. Ang serye ay nagtatagpo kung ang sequence ng mga partial sums Sₙ = Σₖ₌₁ⁿ aₖ ay nagtatagpo.
### Mga Pagsusuri sa Convergence
| Pagsubok | Kundisyon | Konklusyon |
|------|-----------|------------|
| **Pagsusulit sa divergence** | lim aₙ ≠ 0 | Nag-iiba ang mga serye |
| **Pagsubok sa paghahambing** | 0 ≤ aₙ ≤ bₙ at Σbₙ ay nagtatagpo | Σaₙ converges |
| **Pagsusulit sa ratio** | lim \|aₙ₊₁/aₙ\| = L | Converges kung L< 1, diverges if L >1 |
| **Root test** | lim sup \|aₙ\|^(1/n) = L | Converges kung L< 1, diverges if L >1 |
| **Integral na pagsubok** | aₙ = f(n), f bumababa, positibo | Σaₙ converges iff ∫f(x)dx converges |
| **Alternating series** | bumababa ang aₙ, lim aₙ = 0, mga alternating sign | Mga serye ay nagtatagpo |
| **Ganap na tagpo** | Σ\|aₙ\| nagtatagpo | Ang Σaₙ ay nagtatagpo (at ang mga muling pagsasaayos ay nagbibigay ng parehong kabuuan) |
| **Conditional convergence** | Ang Σaₙ ay nagtatagpo ngunit Σ\|aₙ\| nag-iiba | Ang mga muling pagsasaayos ay maaaring magbigay ng anumang kabuuan (Riemann) |
### Mahalagang Serye
| Serye | Sum | Kundisyon |
|--------|-----|-----------|
| Geometric: Σ rⁿ | 1/(1−r) | \|r\| < 1 |
| p-series: Σ 1/nᵖ | Converges | p >1 |
| Harmonic: Σ 1/n | Diverges (= ∞) | — |
| Exponential: Σ xⁿ/n! | eˣ | Lahat ng x |
| Taylor para sa ln(1+x): Σ (−1)ⁿ⁺¹xⁿ/n | ln(1+x) | −1 < x ≤ 1 |
---

## Mga Limitasyon at Pagpapatuloy
### Mga Limitasyon ng Mga Pag-andar
**Kahulugan:** lim_{x→c} f(x) = L ay nangangahulugang: para sa bawat ε > 0, mayroong δ > 0 na ang 0 < |x − c| < δ ay nagpapahiwatig |f(x) − L| < ε.
Ito ang **ε-δ definition** — ang mahigpit na bersyon ng "f(x) ay lumalapit sa L habang ang x ay lumalapit sa c."
### Pagpapatuloy
Ang function na f ay **continuous sa c** kung lim_{x→c} f(x) = f(c). Katumbas nito: para sa bawat ε > 0, mayroong δ > 0 na ang |x − c| < δ ay nagpapahiwatig |f(x) − f(c)| < ε.
**Mga uri ng discontinuity:**
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| Matatanggal | May limitasyon ngunit ≠ f(c) | f(x) = sin(x)/x sa x = 0 |
| Tumalon | Umiiral ang kaliwa at kanang mga limitasyon ngunit magkaiba | Step function |
| Walang-hanggan | Ang limitasyon ay ±∞ | f(x) = 1/x² sa x = 0 |
| Oscillating | Walang limitasyon | f(x) = sin(1/x) sa x = 0 |
### Mga Pangunahing Teorema para sa Tuloy-tuloy na Mga Pag-andar
| Teorama | Pahayag |
|---------|------------|
| **Teorama ng Intermediate Value** | Kung ang f ay tuloy-tuloy sa [a,b] at f(a) < k < f(b), pagkatapos ay ∃c ∈ (a,b): f(c) = k |
| **Extreme Value Theorem** | Kung ang f ay tuloy-tuloy sa [a,b], natatamo ng f ang maximum at minimum nito sa [a,b] |
| **Boundedness Theorem** | Kung ang f ay tuloy-tuloy sa [a,b], ang f ay nakatali sa [a,b] |
| **Pagpapatuloy ng Uniform** | Ang f ay pare-parehong tuloy-tuloy sa [a,b] kung f ay tuloy-tuloy sa [a,b] (Heine-Cantor) |
**Nagtrabahong Halimbawa (IVT):** Ipakita ang x³ + x − 1 = 0 ay may solusyon sa (0, 1).
- Hayaang f(x) = x³ + x − 1. f ay tuloy-tuloy (polynomial).
- f(0) = −1< 0 and f(1) = 1 >0.
- Sa pamamagitan ng IVT, ∃c ∈ (0,1): f(c) = 0.
---

## Pagkakaiba
### Depinisyon
f'(c) = lim_{h→0} (f(c+h) − f(c)) / h
Kung umiiral ang limitasyong ito, ang f ay **nakakaiba** sa c.
### Pagkakaiba kumpara sa Pagpapatuloy
| Relasyon | Pahayag |
|--------------|-----------|
| Naiiba → Tuloy-tuloy | Kung ang f ay naiba sa c, ang f ay tuloy-tuloy sa c |
| Tuloy-tuloy ↛ Naiiba | f(x) = \|x\| ay tuloy-tuloy sa 0 ngunit hindi naiba-iba doon |
| Nowhere differentiable | Weierstrass function: tuloy-tuloy sa lahat ng dako, hindi naiba kahit saan |
### Pangunahing Resulta
| Teorama | Pahayag |
|---------|------------|
| **Mean Value Theorem** | Kung ang f ay tuloy-tuloy sa [a,b] at naiba sa (a,b), ∃c: f'(c) = (f(b)−f(a))/(b−a) |
| **Rolle's Theorem** | Espesyal na kaso ng MVT kapag f(a) = f(b): ∃c: f'(c) = 0 |
| **L'Hôpital's Rule** | Kung lim f/g = 0/0 o ∞/∞, pagkatapos ay lim f/g = lim f'/g' (kapag umiiral ang huli) |
| **Teorem ni Taylor** | f(x) = Σₖ₌₀ⁿ f⁽ᵏ⁾(a)/k! · (x−a)ᵏ + Rₙ(x) na may tahasang natitira |
---

## Pagsasama
### Pagsasama ng Riemann
Ang **Riemann integral** ay tumutukoy sa ∫ₐᵇ f(x)dx bilang limitasyon ng mga kabuuan ng Riemann.
**Paggawa:**
1. Hatiin ang [a,b] sa mga subinterval: P = {x₀, x₁, ..., xₙ}
2. Pumili ng mga sample na puntos tᵢ ∈ [xᵢ₋₁, xᵢ]
3. Riemann sum: S(P,f) = Σᵢ f(tᵢ)(xᵢ − xᵢ₋₁)
4. Kung ang limitasyon ng S(P,f) ay umiiral bilang mesh → 0, f ay Riemann integrable
**Pantayan sa pagiging integridad ng Riemann:**
| Kundisyon | Integrable? |
|-----------|-------------|
| Tuloy-tuloy sa [a,b] | Oo |
| Bounded na may finitely maraming discontinuities | Oo |
| Monotone sa [a,b] | Oo |
| Dirichlet function (1 sa ℚ, 0 sa irrationals) | Hindi |
### Ang Fundamental Theorem of Calculus
| Bahagi | Pahayag |
|------|-----------|
| **Bahagi 1** | Kung ang f ay tuloy-tuloy sa [a,b], kung gayon ang F(x) = ∫ₐˣ f(t)dt ay differentiable at F'(x) = f(x) |
| **Bahagi 2** | Kung F' = f at f ay Riemann integrable, pagkatapos ay ∫ₐᵇ f(x)dx = F(b) − F(a) |
### Pagsasama ng Lebesgue
Ang integral ng Riemann ay may mga limitasyon — hindi nito maaaring pagsamahin ang maraming mga function na lumitaw sa pagsusuri at posibilidad. Ang **Lebesgue integral** ay nagpapalawak ng pagsasama sa isang mas malawak na klase ng mga function.
**Mahalagang ideya:** Sa halip na hatiin ang domain (x-axis), hatiin ang hanay (y-axis).
| Aspeto | Riemann Integral | Lebesgue Integral |
|---------------------|-----------------|-------------------|
| Diskarte | Partition domain (x-axis) | Saklaw ng partition (y-axis) |
| Pinagsasama ang | Continuous, piecewise continuous | Mga nasusukat na function |
| Limitahan ang theorems | Mahina | Makapangyarihan (Dominated Convergence, Monotone Convergence) |
| Mga hawakan | "Maganda" na mga function | Mga function na may mga siksik na discontinuities |
| Pundasyon ng | Classical na calculus | Modernong teorya ng probabilidad |
**Ang pamantayan ng Lebesgue:** Ang f ay ang Riemann na maisasama sa [a,b] kung ang f ay may hangganan at tuluy-tuloy sa halos lahat ng dako (ang hanay ng mga discontinuity ay may sukat na zero).
---

## Mga Puwang ng Sukatan
Ang **metric space** ay nagsa-generalize ng paniwala ng "distansya" sa abstract set.
### Depinisyon
Ang **metric space** (X, d) ay isang set X na may function ng distansya d: X × X → ℝ nagbibigay-kasiyahan:
| Axiom | Pahayag |
|-------|-----------|
| Non-negatibiti | d(x,y) ≥ 0 |
| Pagkakakilanlan | d(x,y) = 0 kung x = y |
| Symmetry | d(x,y) = d(y,x) |
| Hindi pagkakapantay-pantay ng tatsulok | d(x,z) ≤ d(x,y) + d(y,z) |
### Mga Karaniwang Sukatan na Space
| Space | Itakda | Sukatan | Application |
|-------|-----|--------|-------------|
| ℝⁿ kasama ang Euclidean | ℝⁿ | d(x,y) = √Σ(xᵢ−yᵢ)² | Karaniwang geometry |
| ℝⁿ kasama ang Manhattan | ℝⁿ | d(x,y) = Σ\|xᵢ−yᵢ\| | Grid-based na mga landas, LASSO |
| ℝⁿ kasama si Chebyshev | ℝⁿ | d(x,y) = max\|xᵢ−yᵢ\| | Chess king distansya |
| Discrete na sukatan | Anumang set | d(x,y) = 1 kung x≠y, 0 kung x=y | Mga halimbawa ng topolohiya |
| Function space C[a,b] | Mga tuluy-tuloy na function | d(f,g) = max\|f(x)−g(x)\| | Teorya ng approximation |
| Lᵖ space | p-integrable function | d(f,g) = (∫\|f−g\|ᵖ)^(1/p) | Functional analysis, ML norms |
### Mga Topological na Konsepto sa Sukatan na Puwang
| Konsepto | Kahulugan | Halimbawa |
|---------|------------|---------|
| **Buksan ang bola** | B(x,r) = {y : d(x,y) < r} | Buksan ang pagitan (x−r, x+r) sa ℝ |
| **Buksan ang hanay** | Ang bawat punto ay may bolang nakapaloob sa set | (0,1) ay bukas sa ℝ |
| **Saradong hanay** | Komplemento ng isang bukas na hanay | Ang [0,1] ay sarado sa ℝ |
| **Pagsasara** | Pinakamaliit na closed set na naglalaman ng S | Pagsasara ng (0,1) = [0,1] |
| **Compact** | Ang bawat bukas na pabalat ay may hangganang subcover | Sa ℝⁿ: sarado at may hangganan (Heine-Borel) |
| **Kumpleto** | Ang bawat Cauchy sequence ay nagtatagpo | ℝ ay kumpleto; Ang ℚ ay hindi |
---

## Uniform Convergence
Ang isang sequence ng mga function (fₙ) ay maaaring magtagpo sa dalawang paraan:
| Uri | Kahulugan | Pinapanatili ang Pagpapatuloy? |
|------|------------|----------------------|
| **Pointwise** | ∀x: fₙ(x) → f(x) | Hindi |
| **Uniporme** | sup\|fₙ(x) − f(x)\| → 0 | Oo |
**Uniform convergence** ay mas malakas: ang rate ng convergence ay pareho saanman.
**Mga pangunahing teorema:**
- Ang pare-parehong limitasyon ng tuluy-tuloy na pag-andar ay tuloy-tuloy
- Ang pare-parehong limitasyon ng Riemann-integrable function ay Riemann-integrable, at ang integral ng limit ay katumbas ng limit ng integrals
- **Weierstrass M-test:** Kung |fₙ(x)| ≤ Mₙ para sa lahat ng x at ΣMₙ ay nagtatagpo, pagkatapos ay Σfₙ ay pare-parehong nagtatagpo
---

## Teorya ng Sukat
**Teorya ng Pagsukat** ay ginagawang pangkalahatan ang mga konsepto ng haba, lawak, at dami.
### Depinisyon
Ang **measure** sa isang set X ay isang function μ: Σ → [0, ∞] (kung saan ang Σ ay isang σ-algebra ng mga subset) na nagbibigay-kasiyahan:
- μ(∅) = 0
- **Countable additivity:** μ(∪ᵢ Aᵢ) = Σᵢ μ(Aᵢ) para sa disjoint Aᵢ
### Panukalang Lebesgue
Ang **Lebesgue measure** λ on ℝ ay nagpapalawak ng paniwala ng haba:
| Itakda | Pagsukat sa Lebesgue |
|-----|----------------|
| Pagitan [a,b] | b − a |
| Isang punto {x} | 0 |
| May hangganan na hanay | 0 |
| Countable set (hal., ℚ) | 0 |
| Cantor set | 0 (hindi mabilang ngunit may sukat na zero) |
| [0,1] ∩ ℚ | 0 |
| [0,1] \ ℚ | 1 |
### Mga Pangunahing Konsepto
| Konsepto | Kahulugan |
|---------|------------|
| **Halos saanman (a.e.)** | Ang isang ari-arian ay may hawak maliban sa isang hanay ng sukat na zero |
| **Masusukat na function** | Ang preimage ng bawat bukas na set ay masusukat |
| **Lebesgue integral** | Tinutukoy ang integral gamit ang teorya ng sukat |
| **Lᵖ space** | Mga puwang ng mga function na may finite p-th power integral |
### Mahalagang Convergence Theorems
Ang mga theorem na ito ang dahilan kung bakit ang pagsasama ng Lebesgue ay ginustong sa advanced na matematika:
| Teorama | Pahayag |
|---------|------------|
| **Monotone Convergence** | Kung fₙ ↑ f pointwise at fₙ ≥ 0, pagkatapos ay ∫fₙ → ∫f |
| **Dominated Convergence** | Kung fₙ → f pointwise at \|fₙ\| ≤ g (integrable), pagkatapos ay ∫fₙ → ∫f |
| **Fatou's Lemma** | ∫lim inf fₙ ≤ lim inf ∫fₙ |
Ang mga theorems na ito ay nagpapahintulot sa pagpapalitan ng mga limitasyon at integral — isang bagay na nabigo para sa Riemann integration sa pangkalahatan.
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Pagsusuri | Application |
|-----------------|-------------|
| Mga limitasyon at convergence | Pag-unawa kapag ang mga umuulit na algorithm (gradient descent, EM) ay nagtatagpo |
| Pagpapatuloy | Dapat tuloy-tuloy ang activation function para sa backpropagation |
| Pagkakaiba | Ang gradient-based na pag-optimize ay nangangailangan ng differentiable loss function |
| Mean Value Theorem | May hangganan ang error sa numerical approximation, convergence proofs |
| Mga metric space | Mga function ng distansya sa clustering (k-means, DBSCAN), pinakamalapit na kapitbahay |
| pagiging compact | Existence proofs para sa pinakamainam na solusyon, Heine-Borel sa finite-dimensional optimization |
| Uniform convergence | Ginagarantiyahan na ang mga pagtatantya (neural network universal approximation) ay gumagana sa lahat ng dako |
| Sukatin ang teorya | Pundasyon ng modernong probabilidad (ang probabilidad ay isang sukat), inaasahang mga halaga bilang integral ng Lebesgue |
| Pagsasama ng Lebesgue | Ang inaasahang halaga E[X] = ∫X dP ay isang integral sa Lebesgue |
| Lᵖ mga puwang | L¹ (LASSO), L² (Ridge), Lᵖ mga pamantayan sa regularisasyon |
| Dominated Convergence | Pagpapatunay ng pagkakapare-pareho ng mga estimator, pagpapalitan ng mga limitasyon sa Bayesian inference |
---

## Buod
| Paksa | Pangunahing Ideya | Susing Resulta |
|-------|-----------|------------|
| Mga Sequence | Inayos ang mga listahan ng mga numero | Convergence, Cauchy criterion, Bolzano-Weierstrass |
| Serye | Walang katapusang kabuuan | Mga pagsubok sa convergence, absolute vs conditional |
| Mga Limitasyon | Mahigpit na diskarte sa "paglapit" | ε-δ kahulugan |
| Pagpapatuloy | Walang break o jumps | IVT, Extreme Value Theorem |
| Differentiation | Mabilisang rate ng pagbabago | Mean Value Theorem, Taylor's theorem |
| Riemann Integration | Lugar sa ilalim ng mga kurba | Pangunahing Teorama ng Calculus |
| Pagsasama ng Lebesgue | Pagsasama sa pamamagitan ng panukala | Dominado/Monotone Convergence |
| Mga Puwang ng Sukatan | Abstract na distansya | Open/closed sets, compactness, completeness |
| Uniform Convergence | Convergence sa parehong rate sa lahat ng dako | Pinapanatili ang pagpapatuloy at pagkakaisa |
| Teorya ng Sukat | Pangkalahatang haba/lugar/volume | Foundation ng probabilidad, Lebesgue measure |
Ang tunay na pagsusuri ay kung saan lumalaki ang matematika. Pinapalitan nito ang mga intuitive na ideya ng "papalapit," "tuloy-tuloy," at "lugar" na may mga tiyak na kahulugan na maaaring patunayan at pangkalahatan. Para sa mga data scientist at ML engineer, ang pagsusuri ay nagbibigay ng mga teoretikal na garantiya: kailan nagtatagpo ang gradient descent? Kailan maayos ang pag-uugali ng loss function? Kailan tayo maaaring makipagpalitan ng mga limitasyon at inaasahan? Ang mga ito ay hindi pilosopikal na mga tanong - tinutukoy nila kung gumagana o tahimik ang iyong algorithm.