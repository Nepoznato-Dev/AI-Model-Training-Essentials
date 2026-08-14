---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Pag-optimize
Ang pag-optimize ay ang matematika ng paghahanap ng pinakamahusay na solusyon mula sa isang hanay ng mga magagawang solusyon. Nagtatanong ito: binigyan ng isang function at mga hadlang, anong input ang nagpapaliit (o nag-maximize) sa output? Ang pag-optimize ay ang makina ng machine learning — ang pagsasanay sa isang modelo ay nangangahulugan ng pagliit ng isang function ng pagkawala. Lumilitaw ito sa pananaliksik sa pagpapatakbo, ekonomiya, disenyo ng inhinyero, at halos lahat ng larangan ng dami.
---

## Pagbubuo ng Suliranin
Ang isang pangkalahatang **problema sa pag-optimize** ay may form:
I-minimize ang f(x)
Napapailalim sa: gᵢ(x) ≤ 0 (mga hadlang sa hindi pagkakapantay-pantay), hⱼ(x) = 0 (mga hadlang sa pagkakapantay-pantay)
| Termino | Ibig sabihin |
|------|---------|
| **Layunin function** f(x) | Ang dami upang i-minimize (o i-maximize) |
| **Mga variable ng desisyon** x | Ang mga halaga na maaari nating kontrolin |
| **Maaaring rehiyon** | Set ng lahat ng x na nagbibigay-kasiyahan sa lahat ng mga hadlang |
| **Pandaigdigang minimum** | Magagawa x* na may f(x*) ≤ f(x) para sa lahat ng magagawa x |
| **Lokal na minimum** | Feasible x* with f(x*) ≤ f(x) para sa lahat ng feasible x sa ilang neighborhood |
| **Problema sa matambok** | Ang f ay matambok, ang posible na rehiyon ay nakatakdang matambok (lokal na min = pandaigdigang min) |
---

## Linear Programming (LP)
Kapag ang layunin at lahat ng mga hadlang ay **linear**, ang problema ay isang linear na programa.
### Pamantayang Form
I-minimize ang cᵀx
Napapailalim sa: Ax ≤ b, x ≥ 0
kung saan c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Mga Katangian
| Ari-arian | Pahayag |
|----------|-----------|
| Convexity | Ang LP ay palaging isang matambok na problema |
| Pinakamainam na solusyon | Palaging nasa isang vertex (corner point) ng feasible polytope |
| Pag-iral | Kung ang posible na rehiyon ay may hangganan at hindi walang laman, ang pinakamainam na solusyon ay umiiral |
| Maramihang optima | Kung ang dalawang vertices ay pinakamainam, ang bawat punto sa gilid sa pagitan ng mga ito ay pinakamainam din |
### Ang Simplex Method
Ang **simplex method** (Dantzig, 1947) ay gumagalaw sa mga gilid ng feasible polytope mula sa vertex patungo sa vertex, palaging pinapabuti ang layunin, hanggang sa maabot ang pinakamabuting kalagayan.
| Ari-arian | Halaga |
|----------|-------|
| Worst-case na oras | O(2ⁿ) (exponential — bihira sa pagsasanay) |
| Average-case na oras | Polynomial para sa karamihan ng mga praktikal na problema |
| Pangunahing ideya | Ilipat sa katabing vertex na may mas magandang layunin na halaga |
**Algorithm (pangkalahatang-ideya):**
1. Magsimula sa isang basic feasible solution (vertex ng polytope)
2. Pumili ng isang pumapasok na variable (isa na nagpapabuti sa layunin)
3. Pumili ng variable na umaalis (panatilihin ang pagiging posible)
4. Pivot: lumipat sa bagong vertex
5. Ulitin hanggang sa walang pagpapabuting direksyon na umiiral
### Mga Paraan ng Panloob na Punto
Alternatibo sa simplex: lapitan ang pinakamabuting kalagayan mula sa loob ng posible na rehiyon.
| Ari-arian | Halaga |
|----------|-------|
| Worst-case na oras | Polynomial (O(n³·⁵) para sa ilang variant) |
| Praktikal na pagganap | Competitive sa simplex sa malalaking problema |
| Pangunahing ideya | Sundin ang isang "gitnang landas" sa loob ng |
### Nagtrabahong Halimbawa ng LP
**Problema:** Ang isang pabrika ay gumagawa ng mga upuan (x₁) at mesa (x₂).
- Kita: $30 bawat upuan, $50 bawat mesa
- Kahoy: 2x₁ + 4x₂ ≤ 100 (available ang board feet)
- Paggawa: x₁ + 3x₂ ≤ 60 (mga oras na available)
- I-maximize: 30x₁ + 50x₂
**Solusyon (graphical na paraan para sa 2 variable):**
- Mga vertice ng posible na rehiyon: (0,0), (30,0), (40,10), (0,20)
- Suriin ang layunin sa bawat tuktok:
  - (0,0): tubo = 0
  - (30,0): tubo = 900
  - (40,10): tubo = 1700 ← pinakamainam
  - (0,20): tubo = 1000
- **Optimal:** x₁ = 40 upuan, x₂ = 10 table, tubo = $1700
---

## Convex Optimization
Ang isang problema ay **convex** kung ang layunin ng function ay convex at ang magagawa na rehiyon ay isang convex set.
### Mga Convex Set at Function
| Konsepto | Kahulugan |
|---------|------------|
| **Convex set** | Para sa anumang x, y sa set at t ∈ [0,1]: tx + (1−t)y ay nasa set din |
| **Convex function** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) para sa lahat ng t ∈ [0,1] |
| **Mahigpit na matambok** | Ang hindi pagkakapantay-pantay ay mahigpit para sa t ∈ (0,1) at x ≠ y |
**Mahalagang pag-aari:** Para sa matambok na pag-optimize, bawat lokal na minimum ay isang pandaigdigang minimum.
### Mga Karaniwang Convex na Function
| Function | Matambok? | Saan |
|----------|---------|-------|
| ax + b (linear) | Oo (at malukong) | Kahit saan |
| x² | Oo | ℝ |
| eˣ | Oo | ℝ |
| −log(x) | Oo | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Oo | ℝⁿ |
| max(f₁, f₂) kung f₁, f₂ matambok | Oo | Intersection ng mga domain |
### Gradient Descent
Ang pinakapangunahing algorithm ng pag-optimize sa machine learning.
** Panuntunan sa pag-update:** x_{k+1} = x_k − α∇f(x_k)
kung saan ang α > 0 ay ang **rate ng pagkatuto** (laki ng hakbang).
| Variant | I-update ang Panuntunan | Pakinabang |
|---------|-------------|-----------|
| **Batch GD** | x ← x − α∇f(x) | Matatag na convergence |
| **Stochastic GD (SGD)** | x ← x − α∇fᵢ(x) (isang sample) | Mabilis sa bawat pag-ulit, lumalabas sa lokal na minima |
| **Mini-batch SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Balanse sa pagitan ng batch at stochastic |
| **Momentum** | v ← βv − α∇f(x); x ← x + v | Bumibilis sa mga patag na rehiyon |
| **Adan** | Adaptive learning rate bawat parameter | Gumagana nang maayos sa labas ng kahon para sa malalim na pag-aaral |
| **RMSprop** | I-scale ang rate ng pagkatuto sa pamamagitan ng average na pagpapatakbo ng gradient magnitude | Mabuti para sa mga RNN |
### Mga Rate ng Convergence
| Paraan | Matambok f | Malakas na Matambok f |
|--------|----------|--------------------|
| gradient descent | O(1/k) | O((1−μ/L)ᵏ) (linear) |
| SGD | O(1/√k) | O(1/k) |
| Pinabilis na GD (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
kung saan k = bilang ng pag-ulit, μ = malakas na parameter ng convexity, L = Lipschitz pare-pareho.
### Pagpili ng Rate ng Pagkatuto
| Diskarte | Paglalarawan |
|----------|-------------|
| Inayos ang α | Simple ngunit maaaring mag-diverge (masyadong malaki) o mabagal na mag-converge (masyadong maliit) |
| Paghahanap sa linya | Hanapin ang α na nagpapaliit ng f(x − α∇f(x)) sa direksyon ng gradient |
| Mga iskedyul ng pagkabulok | α_t = α₀ / (1 + βt) o α_t = α₀ · βᵗ |
| Warmup | Magsimula sa maliit, dagdagan, pagkatapos ay mabulok (karaniwan sa pagsasanay sa transpormer) |
| Adaptive (Adan) | Per-parameter na mga rate ng pag-aaral batay sa gradient statistics |
---

## Pinipigilan na Pag-optimize
### Mga Lagrange Multiplier
Para sa problema: i-minimize ang f(x) na napapailalim sa h(x) = 0.
**Lagrangian:** L(x, λ) = f(x) + λh(x)
Sa pinakamabuting kalagayan: ∇ₓL = 0 at ∇_λL = 0 (na nagbibigay ng h(x) = 0).
**Nagtrabaho Halimbawa:** I-minimize ang f(x,y) = x² + y² na napapailalim sa x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Limitasyon: x + y = 1 → −λ = 1 → λ = −1
- Solusyon: x = 1/2, y = 1/2, f = 1/2
### Mga Kundisyon ng KKT
Ang **Karush-Kuhn-Tucker (KKT) na mga kundisyon** ay nagsa-generalize ng mga Lagrange multiplier sa hindi pagkakapantay-pantay na mga hadlang.
Para sa: i-minimize ang f(x) na napapailalim sa gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrangian:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**KKT kundisyon** (kinakailangan para sa pinakamainam):
| Kundisyon | Equation |
|-----------|----------|
| Stationarity | ∇ₓL = 0 |
| Pangunahing pagiging posible | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Dual feasibility | λᵢ ≥ 0 |
| Komplementaryong pagkaantala | λᵢgᵢ(x) = 0 para sa lahat ng i |
Ang ibig sabihin ng **Complementary slackness** ay: kung hindi aktibo ang constraint gᵢ (gᵢ(x) < 0), λᵢ = 0 (hindi naaapektuhan ng constraint ang solusyon).
Para sa mga convex na problema na nagbibigay-kasiyahan sa kondisyon ni Slater, ang mga kondisyon ng KKT ay parehong kailangan at sapat.
---

## Duality
Ang bawat problema sa pag-optimize (ang **primal**) ay may nauugnay na **dual** na problema.
### Mahina at Malakas na Duality
| Konsepto | Pahayag |
|---------|------------|
| **Dual function** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Kambal na problema** | I-maximize ang g(λ, ν) na napapailalim sa λ ≥ 0 |
| **Mahina ang duality** | Dual optimal ≤ Primal optimal (laging hawak) |
| **Malakas na duality** | Dual optimal = Primal optimal (nagtataglay para sa mga convex na problema sa kondisyon ni Slater) |
| **duality gap** | Primal optimal − Dual optimal (zero sa ilalim ng malakas na duality) |
### Bakit Mahalaga ang Duality
| Application | Paano Nakakatulong ang Duality |
|-------------|--------------------|
| Lower bounds | Nagbibigay ang Dual ng isang sertipiko kung gaano kahusay ang pangunahing solusyon |
| Mga SVM | Ang dalawahan ng problema sa SVM ay humahantong sa kernel trick |
| Pagsusuri ng pagiging sensitibo | Sinusukat ng dalawahang variable kung gaano kalaki ang mga pinakamabuting pagbabago kung ang mga hadlang ay maluwag |
| Pagkabulok | Maaaring hatiin ang malalaking problema sa mas maliliit na subproblema sa pamamagitan ng dual |
---

## Integer Programming
Kapag ang ilan o lahat ng mga variable ay dapat na **integers**, ang problema ay nagiging mas mahirap (NP-hard sa pangkalahatan).
### Mga uri
| Uri | Paglalarawan |
|------|-------------|
| Purong IP | Ang lahat ng mga variable ay dapat na mga integer |
| Mixed IP (MIP) | Ilang variable integer, ilang tuluy-tuloy |
| Binary IP | Ang mga variable ay pinaghihigpitan sa {0, 1} |
### Mga Paraan ng Solusyon
| Paraan | Ideya |
|--------|------|
| **Sangay at nakatali** | Hatiin sa mga subproblema, lutasin ang mga pagpapahinga sa LP, putulin |
| **Pagputol ng mga eroplano** | Magdagdag ng mga linear na hadlang upang higpitan ang LP relaxation |
| **Sangay at gupit** | Pagsamahin ang branch-and-bound sa mga cutting planes |
| **Heuristics** | Matakaw, lokal na paghahanap, kunwa ng pagsusubo para sa tinatayang solusyon |
---

## Heuristic at Metaheuristic Methods
Kapag ang eksaktong pag-optimize ay hindi naaalis, ang heuristics ay nakakahanap ng mahusay (hindi kinakailangang pinakamainam) na mga solusyon.
| Paraan | Pangunahing Ideya | Pinakamahusay Para sa |
|--------|----------|----------|
| **Gradient descent** | Sundin ang pinakamatarik na pagbaba | Smooth, differentiable functions |
| **Paraan ni Newton** | Gumamit ng pangalawang-order (curvature) na impormasyon | Makinis, maayos na mga problema |
| **Simulated annealing** | Tanggapin ang mas masahol na mga solusyon na may bumababang posibilidad | Global optimization, combinatorial |
| **Mga genetic algorithm** | Mag-evolve ng populasyon gamit ang selection, crossover, mutation | Multi-layunin, hindi nakikilala |
| **Kumpol ng particle** | Ginalugad ng mga ahente ang espasyo, na naiimpluwensyahan ng mga kilalang posisyon | Tuloy-tuloy, hindi matambok |
| **Bayesian optimization** | Bumuo ng surrogate model, gumamit ng acquisition function | Mamahaling black-box function (hyperparameter tuning) |
### Paraan ng Newton para sa Pag-optimize
**Panuntunan sa pag-update:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
kung saan ang H ay ang Hessian matrix (matrix ng pangalawang derivatives).
| Ari-arian | Halaga |
|----------|-------|
| Rate ng convergence | Quadratic (malapit sa pinakamainam) |
| Per-iteration na gastos | O(n³) para sa Hessian inversion |
| Nangangailangan | Dalawang beses na differentiable, positive definite Hessian |
| Quasi-Newton (BFGS) | Tinatayang Hessian mula sa mga gradient | O(n²) bawat pag-ulit |
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Pag-optimize | Application |
|---------------------|-------------|
| gradient descent | Pagsasanay sa mga neural network, logistic regression, anumang naiba-iba na modelo |
| SGD at mga variant | Malaking ML (mini-batch na pagsasanay), online na pag-aaral |
| Adam, RMSprop | Mga default na optimizer para sa malalim na pag-aaral |
| Convex optimization | Mga SVM, logistic regression, LASSO, Ridge (garantisadong global optimum) |
| Lagrange multiplier | Pinilit na pag-aaral, patas na ML, paglalaan ng mapagkukunan |
| Mga kundisyon ng KKT | Pagkuha ng SVM dual, pag-unawa sa aktibidad ng pagpilit |
| Duality | SVM kernel trick, sensitivity analysis, decomposition method |
| Linear programming | Paglalaan ng mapagkukunan, pag-optimize ng portfolio, daloy ng network |
| Integer programming | Pagpili ng tampok (binary), pag-iiskedyul, mga problema sa kombinatoryal |
| Bayesian optimization | Hyperparameter tuning (Optuna, Hyperopt) |
| Newton/quasi-Newton | Pangalawang-order na mga pamamaraan para sa maliliit hanggang sa katamtamang mga problema (L-BFGS) |
---

## Buod
| Paraan | Uri ng Problema | Mga Garantiya | Iskala |
|--------|-------------|------------|-------|
| Simplex | Linear programming | Eksaktong pinakamabuting kalagayan | Milyun-milyong mga variable |
| Panloob na punto | Matambok (LP, QP, SOCP) | Eksaktong pinakamabuting kalagayan | Malaking sukat |
| gradient descent | Makinis na walang limitasyon | Nagko-convert sa lokal na min | Napakalaki (deep learning) |
| SGD | Malaking empirical na panganib | Converges (na may pagkabulok) | Napakalaking dataset |
| Newton / BFGS | Smooth, twice-differentiable | Quadratic convergence | Maliit hanggang katamtaman |
| KKT / Lagrange | Pinilit (matambok) | Eksaktong sa ilalim ng mga kundisyon | Katamtaman |
| Branch at bound | Integer programming | Eksaktong pinakamabuting kalagayan | Maliit hanggang katamtaman |
| Heuristics | Anumang (hindi matambok, kombinatoryal) | Walang garantiya | Nag-iiba |
Ang pag-optimize ay marahil ang pinakamahalagang tool sa matematika sa pag-aaral ng makina. Ang bawat modelong iyong sinasanay — mula sa linear regression hanggang sa malalaking modelo ng wika — ay nagsasangkot ng paglutas ng problema sa pag-optimize. Ang pag-unawa kung ang isang problema ay matambok (garantisadong pandaigdigang pinakamainam), kung kailan magtatagpo ang gradient descent, at kung paano haharapin ang mga hadlang ay nagbibigay sa iyo ng teoretikal na pundasyon upang magdisenyo, mag-debug, at mapabuti ang mga algorithm sa pag-aaral.