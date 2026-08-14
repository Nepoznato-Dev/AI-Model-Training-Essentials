---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
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
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
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
# Numerical na Paraan
Ang mga numerical na pamamaraan ay ang tulay sa pagitan ng matematikal na teorya at praktikal na pagtutuos. Habang ang dalisay na matematika ay nagpapatunay na may mga solusyon, ang mga numerical na pamamaraan ay aktwal na kumukwenta ng tinatayang mga sagot sa may hangganang katumpakan. Bawat machine learning model, physics simulation, at data analysis pipeline sa huli ay umaasa sa numerical computation. Ang pag-unawa sa mga pamamaraang ito — ang kanilang katumpakan, katatagan, at mga limitasyon — ay mahalaga para sa pagbuo ng maaasahang software.
---

## Floating-Point Arithmetic
Ang mga computer ay kumakatawan sa mga tunay na numero na may tiyak na katumpakan. Ang **IEEE 754 standard** ay tumutukoy kung paano iniimbak at minamanipula ang mga floating-point na numero.
### Mga Format ng IEEE 754
| Format | Bits | Exponent | Mantissa | Tinatayang Decimal Digit | Saklaw |
|--------|------|----------|----------|--------------------------|-------|
| Kalahati (fp16) | 16 | 5 | 10 | 3.3 | ±6.5 × 10⁴ |
| Single (fp32) | 32 | 8 | 23 | 7.2 | ±3.4 × 10³⁸ |
| Doble (fp64) | 64 | 11 | 52 | 15.9 | ±1.8 × 10³⁰⁸ |
### Machine Epsilon
**Machine epsilon** (ε_mach) ay ang pinakamaliit na bilang na 1 + ε_mach > 1 sa floating-point.
| Format | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9.8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1.2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2.2 × 10⁻¹⁶ |
### Mga Karaniwang Pitfalls
| Pitfall | Halimbawa | Bunga |
|---------|---------|-------------|
| **Sakuna na pagkansela** | Pag-compute (1 + x) − 1 para sa maliit na x | Pagkawala ng makabuluhang digit |
| **Pagsipsip** | 10⁸ + 1 = 10⁸ sa fp32 | Maliit na halaga ang nawala sa malalaking halaga |
| **Hindi pagkakaugnay** | (a + b) + c ≠ a + (b + c) | Mahalaga ang kabuuan ng order |
| **Dibisyon sa pamamagitan ng malapit-zero** | 1 / 10⁻³⁰⁰ → overflow | Infinity o NaN |
### Mga Istratehiya sa Pagbabawas
| Diskarte | Paglalarawan |
|----------|-------------|
| **Kahan summation** | Compensated summation para mabawasan ang absorption error |
| **Kahan-Babuska-Neumaier** | Pinahusay na bersyon ng Kahan summation |
| **Pinagbukod-bukod na pagbubuod** | Magsama muna ng maliliit na numero upang maiwasan ang pagsipsip |
| **Double-double arithmetic** | Gumamit ng mga pares ng doubles para sa pinalawig na katumpakan |
| **Pagsusuri ng conditioning** | Unawain kung ang problema mismo ay nagpapalaki ng mga error |
---

## Paghahanap ng Root
Paghahanap ng x na ang f(x) = 0.
### Paraan ng Bisection
| Ari-arian | Halaga |
|----------|-------|
| Nangangailangan | f tuloy-tuloy, f(a) at f(b) ay may magkasalungat na palatandaan |
| Convergence | Linear (hinahati ng error ang bawat hakbang) |
| Garantisado? | Oo — laging nagtatagpo |
| Mga pag-ulit para sa d digit | ≈ d / log₁₀(2) ≈ 3.32d |
**Algorithm:**
1. Magsimula sa pagitan [a, b] kung saan f(a) · f(b) < 0
2. Compute midpoint c = (a + b) / 2
3. Kung f(c) = 0 o |b − a| < pagpaparaya, tumigil ka
4. Kung f(a) · f(c) < 0, itakda ang b = c; ibang set a = c
5. Ulitin
### Paraan ng Newton-Raphson
| Ari-arian | Halaga |
|----------|-------|
| Nangangailangan | f naiba-iba, f'(x) ≠ 0 sa ugat |
| Convergence | Quadratic (malapit sa ugat) |
| Garantisado? | Hindi — maaaring maghiwalay o umikot |
| I-update ang panuntunan | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Nagtrabaho Halimbawa:** Hanapin ang √2 sa pamamagitan ng paglutas ng f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1.5
- x₁ = 1.5 − (2.25 − 2) / 3 = 1.5 − 0.0833 = 1.4167
- x₂ = 1.4167 − (2.0069 − 2) / 2.8333 = 1.4142
- x₃ = 1.41421356... (tama hanggang 8 decimal na lugar)
### Secant Method
Tulad ng pamamaraan ni Newton ngunit tinatantya ang hinango:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Ari-arian | Halaga |
|----------|-------|
| Convergence | Superlinear (order ≈ 1.618, ang golden ratio) |
| Nangangailangan | Dalawang paunang hula (walang derivative na kailangan) |
### Paghahambing ng Root-Finding Methods
| Paraan | Convergence | Kailangan ng Derivative? | Garantisado? | Gastos sa bawat Hakbang |
|--------|-------------|-------------------|-------------|--------------|
| Hatiin | Linear (1) | Hindi | Oo | 1 function eval |
| Newton-Raphson | Quadratic (2) | Oo | Hindi | 2 function evals |
| Secant | Superlinear (1.618) | Hindi | Hindi | 1 function eval |
| Paraan ni Brent | Superlinear | Hindi | Oo | Nag-iiba |
**Ang pamamaraan ni Brent** ay pinagsasama ang bisection (garantisadong convergence) sa secant/inverse quadratic interpolation (fast convergence). Ito ang default na root-finder sa karamihan ng mga numerical na library.
---

## Numerical Integration (Quadrature)
Pag-compute ∫ₐᵇ f(x) dx humigit-kumulang.
### Mga Paraan
| Paraan | Formula | Error | Order |
|--------|---------|-------|-------|
| **Pahaba (gitnang punto)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapezoidal** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Simpson's 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpson's 3/8** | Gumagamit ng 4 na pantay na espasyong puntos | O(h⁴) | 4 |
| **Gaussian quadrature** | Pinakamainam na pagkakalagay ng node | O(h²ⁿ) | n puntos |
### Composite Rules
Para sa n subinterval ng lapad h = (b−a)/n:
| Panuntunan | Composite Formula | Error |
|------|---------------------|-------|
| Composite Trapezoidal | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Composite Simpson's | h/3[f(a) + 4Σf(kakaiba) + 2Σf(even) + f(b)] | O(h⁴) |
**Nagtrabahong Halimbawa:** Tinatayang ∫₀¹ e^(−x²) dx gamit ang composite trapezoidal na may n = 4.
- h = 0.25, mga puntos: 0, 0.25, 0.5, 0.75, 1
- f(0) = 1, f(0.25) = 0.9394, f(0.5) = 0.7788, f(0.75) = 0.5698, f(1) = 0.3679
- T = 0.25[1/2 + 0.9394 + 0.7788 + 0.5698 + 0.3679/2] = 0.25[1/2 + 2.2880 + 0.1840] = 0.7430
- True value: ≈ 0.7468 (error ≈ 0.5%)
### Adaptive Quadrature
Awtomatikong ibinabahagi ang mga pagitan kung saan mabilis na nag-iiba ang function, gamit ang mas kaunting mga punto kung saan ito ay makinis. Ito ang ginagamit ng`scipy.integrate.quad`(batay sa QUADPACK).
---

## Interpolation
Pagtatantya ng mga halaga sa pagitan ng mga kilalang punto ng data.
### Mga Paraan
| Paraan | Paglalarawan | Kakinisan | Oscillation |
|--------|-------------|------------|-------------|
| **Pinakalapit na kapitbahay** | Gamitin ang pinakamalapit na data point | Hindi natuloy | Wala |
| **Linear** | Ikonekta ang mga punto sa mga tuwid na linya | C⁰ (patuloy) | Wala |
| **Polynomial (Lagrange)** | Single polynomial sa lahat ng puntos | C^∞ | Malubha para sa maraming puntos (Runge's phenomenon) |
| **Cubic spline** | Piecewise cubic, makinis sa joints | C² | Minimal |
| **Radial basis function** | Weighted sum ng radial kernels | Depende sa kernel | Mababa |
### Lagrange Interpolation
Dahil sa n+1 na puntos (x₀, y₀), ..., (xₙ, yₙ), ang natatanging polynomial ng degree ≤ n na dumadaan sa lahat ng puntos:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Runge's phenomenon:** High-degree polynomial interpolation sa pantay na pagitan ng mga punto ay maaaring mag-oscillate nang husto malapit sa mga gilid. Nababawasan sa pamamagitan ng paggamit ng mga Chebyshev node o splines.
### Cubic Splines
Piecewise cubic polynomial na C² tuloy-tuloy (continuous second derivatives).
| Uri | Kondisyon ng Hangganan |
|------|---------------------|
| Natural na spline | S''(x₀) = S''(xₙ) = 0 |
| Naka-clamp na spline | Tinukoy ng S'(x₀) at S'(xₙ) |
| Hindi-isang-buhol | Ang pangatlong derivative na tuloy-tuloy sa x₁ at xₙ₋₁ |
---

## Mga Solver ng ODE
Paglutas ng mga ordinaryong differential equation dy/dt = f(t, y) ayon sa numero.
### Paraan ni Euler
Ang pinakasimpleng solver ng ODE.
**Update:** y_{n+1} = y_n + h · f(t_n, y_n)
| Ari-arian | Halaga |
|----------|-------|
| Order | 1 (error sa bawat hakbang: O(h²), global: O(h)) |
| Katatagan | Kondisyon na matatag (maliit na h kinakailangan) |
| Gastos | 1 pagsusuri ng function bawat hakbang |
### Mga Paraan ng Runge-Kutta
| Paraan | Order | Mga yugto | Mga Tala |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Pinakasimple |
| **Gitnang punto** | 2 | 2 | Mas mahusay na katumpakan |
| **Heun's (RK2)** | 2 | 2 | Predictor-corrector |
| **Classic na RK4** | 4 | 4 | Karaniwang workhorse |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Adaptive na laki ng hakbang (ginamit sa ode45) |
### Classic RK4 (ika-4 na order na Runge-Kutta)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Ari-arian | Halaga |
|----------|-------|
| Order | 4 (pandaigdigang error: O(h⁴)) |
| Gastos | 4 na pagsusuri ng function bawat hakbang |
| Katatagan | Higit na mas mahusay kaysa sa Euler |
| Paggamit | Default para sa mga hindi matigas na ODE |
### Mga Matigas na ODE
Ang **stiff** ODE ay may mga bahagi na nag-iiba-iba sa iba't ibang sukat ng oras. Ang mga tahasang pamamaraan (Euler, RK4) ay nangangailangan ng hindi praktikal na maliliit na laki ng hakbang.
| Paraan | Uri | Katatagan |
|--------|------|-----------|
| Implicit Euler | Implicit | A-stable (walang kondisyon na matatag) |
| Backward Differentiation Formula (BDF) | Implicit | A-stable (hanggang sa order 5) |
| Implicit Runge-Kutta | Implicit | Umiiral ang mga L-stable na variant |
| LSODA | Awtomatikong | Nagpapalit sa pagitan ng matigas/hindi matigas |
---

## Numerical Stability at Conditioning
### Numero ng Kundisyon
Sinusukat ng **condition number** kung gaano kalaki ang pagbabago ng output ng isang problema kaugnay ng maliliit na pagbabago sa input.
Para sa isang linear system Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Interpretasyon |
|-------|----------------|
| ≈ 1 | Well-conditioned |
| 10³ | Medyo sensitibo |
| 10⁸ | Masama ang kondisyon (nawalan ng ~8 digit ng katumpakan) |
| → ∞ | Isahan (walang natatanging solusyon) |
### Katatagan ng Algorithms
Ang isang algorithm ay **numerically stable** kung ang maliliit na perturbation sa input ay humantong sa maliliit na perturbation sa output (na may kaugnayan sa condition number ng problema).
| Algorithm | Matatag? | Mga Tala |
|-----------|---------|-------|
| Gaussian elimination na may bahagyang pag-pivot | Oo | Karaniwang diskarte |
| Pag-compute ng eigenvalues ​​sa pamamagitan ng QR | Oo | Paatras na matatag |
| Walang muwang na pagsusuma (malaki + maliit muna) | Hindi | Gamitin ang Kahan summation |
| Pag-compute ng pagkakaiba-iba bilang E[X²] − (E[X])² | Posibleng hindi | Gamitin ang online na algorithm ng Welford |
### Online Algorithm ng Welford
Numerically stable computation ng running mean at variance:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Iniiwasan nito ang sakuna na pagkansela na nangyayari sa walang muwang na two-pass na formula.
---

## Kaugnayan sa Machine Learning at Data Science
| Pamamaraang Numerikal | Application |
|-----------------|-------------|
| Floating-point (fp16/fp32/bf16) | Mixed-precision training, model quantization, memory efficiency |
| Paghanap ng ugat | Maximum na pagtatantya ng posibilidad (paghanap kung saan ang gradient = 0) |
| Pagsasama ng numero | Bayesian inference (computing marginal likelihoods), inaasahang value |
| Interpolation | Smoothing, imputation, surrogate models, activation functions |
| Mga solver ng ODE | Mga Neural ODE, tuluy-tuloy na oras na RNN, dynamics ng populasyon, ML na may kaalaman sa pisika |
| Numero ng kundisyon | Pag-unawa sa mga isyu sa numero sa linear regression, mga normal na equation |
| Matatag na pagsusuma | Computing loss functions, batch normalization statistics |
| RK4 / adaptive solver | Simulating dynamical system, pagsasanay sa tuluy-tuloy na malalim na network |
---

## Buod
| Paksa | Pangunahing Ideya | Pangunahing Paraan |
|-------|-----------|------------|
| Lumulutang-punto | May hangganang katumpakan na representasyon | IEEE 754, Kahan summation |
| Paghanap ng ugat | Lutasin ang f(x) = 0 | Bisection, Newton-Raphson, Brent's |
| Pagsasama ng numero | Tinatayang ∫f(x)dx | Trapezoidal, Simpson's, Gaussian quadrature |
| Interpolation | Tantyahin sa pagitan ng mga punto ng data | Mga cubic spline, Lagrange, RBF |
| Mga solver ng ODE | Lutasin ang dy/dt = f(t,y) | Euler, RK4, mga paraan ng adaptive |
| Katatagan | Pagkasensitibo sa mga error sa pag-round | Numero ng kundisyon, mga matatag na algorithm |
Ang mga numerical na pamamaraan ay kung saan ang matematika ay nakakatugon sa katotohanan. Walang computer ang maaaring kumatawan nang eksakto sa karamihan ng mga totoong numero, walang derivative na kinukuwenta ng simboliko sa pagsasanay, at walang integral na sinusuri sa closed form para sa mga problema sa totoong mundo. Ang pag-unawa sa mga numerical na pamamaraan ay nagbibigay-daan sa iyong piliin ang tamang algorithm, hulaan ang katumpakan nito, at maiwasan ang mga banayad na bug na nagmumula sa finite-precision arithmetic.