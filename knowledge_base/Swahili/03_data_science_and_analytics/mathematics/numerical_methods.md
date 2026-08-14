<!--
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

-->
# Mbinu za Nambari
Njia za nambari ni daraja kati ya nadharia ya hisabati na hesabu ya vitendo. Wakati hisabati safi inathibitisha kuwa suluhu zipo, njia za nambari hukusanya majibu takriban kwa usahihi kamili. Kila modeli ya kujifunza kwa mashine, uigaji wa fizikia, na bomba la uchanganuzi wa data hatimaye hutegemea ukokotoaji wa nambari. Kuelewa njia hizi - usahihi, uthabiti, na mapungufu - ni muhimu kwa kuunda programu inayotegemewa.
---

## Hesabu ya Pointi Zinazoelea
Kompyuta inawakilisha nambari halisi kwa usahihi wa mwisho. **IEEEE 754 ya kawaida** inafafanua jinsi nambari za sehemu zinazoelea zinavyohifadhiwa na kubadilishwa.
### IEEE 754 Miundo
| Umbizo | Biti | Kielelezo | Mantissa | Takriban Nambari za Desimali | Safu |
>>
| Nusu (fp16) | 16 | 5 | 10 | 3.3 | ±6.5 × 10⁴ |
| Mtu Mmoja (fp32) | 32 | 8 | 23 | 7.2 | ±3.4 × 10³⁸ |
| Mara mbili (fp64) | 64 | 11 | 52 | 15.9 | ±1.8 × 10³⁰⁸ |
### Mashine ya Epsilon
**Epsilon ya mashine** (ε_mach) ndiyo nambari ndogo zaidi kwamba 1 + ε_mach > 1 katika sehemu inayoelea.
| Umbizo | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9.8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1.2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2.2 × 10⁻¹⁶ |
### Mitego ya Kawaida
| Shimo | Mfano | Matokeo |
|---------|---------|-------------|
| **Kughairiwa kwa janga** | Kompyuta (1 + x) − 1 kwa x ndogo | Kupoteza kwa tarakimu muhimu |
| **Kunyonya** | 10⁸ + 1 = 10⁸ katika fp32 | Thamani ndogo zinazopotea kwa kiasi kikubwa |
| **Kutokuwa na ushirika** | (a + b) + c ≠ a + (b + c) | Agizo la jumla ni muhimu |
| **Mgawanyiko kwa karibu-sifuri** | 1 / 10⁻³⁰⁰ → kufurika | Infinity au NaN |
### Mikakati ya Kupunguza
| Mkakati | Maelezo |
|----------|-------------|
| **Kahan mukhtasari** | Muhtasari uliofidiwa ili kupunguza hitilafu ya unyonyaji |
| **Kahan-Babuska-Neumaier** | Toleo lililoboreshwa la muhtasari wa Kahan |
| **Muhtasari uliopangwa** | Jumlisha nambari ndogo kwanza ili kuzuia kunyonya |
| **Hesabu mbili-mbili** | Tumia jozi za maradufu kwa usahihi uliopanuliwa |
| **Uchambuzi wa hali** | Elewa ikiwa shida yenyewe inakuza makosa |
---

## Kutafuta Mizizi
Kupata x kama kwamba f(x) = 0.
### Mbinu ya Sehemu mbili
| Mali | Thamani |
|----------|-------|
| Inahitaji | f kuendelea, f(a) na f(b) zina ishara kinyume |
| Muunganisho | Linear (kosa nusu kila hatua) |
| Imehakikishwa? | Ndiyo - huungana kila mara |
| Marudio ya tarakimu d | ≈ d / logi₁₀(2) ≈ 3.32d |
**Algorithm:**
1. Anza na muda [a, b] ambapo f(a) · f(b) <0
2. Kokotoa sehemu ya katikati c = (a + b) / 2
3. Ikiwa f(c) = 0 au |b -a| <uvumilivu, acha
4. Ikiwa f(a) · f(c) < 0, weka b = c; mwingine kuweka = c
5. Rudia
### Mbinu ya Newton-Raphson
| Mali | Thamani |
|----------|-------|
| Inahitaji | f inayoweza kutofautishwa, f'(x) ≠ 0 kwenye mzizi |
| Muunganisho | Quadratic (karibu na mzizi) |
| Imehakikishwa? | Hapana - inaweza kutofautiana au kuzunguka |
| Sasisha kanuni | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Mfano Uliofanyiwa Kazi:** Tafuta √2 kwa kutatua f(x) = x² − 2 = 0.
- f'(x) = 2x
- x₀ = 1.5
- x₁ = 1.5 − (2.25 − 2) / 3 = 1.5 − 0.0833 = 1.4167
- x₂ = 1.4167 − (2.0069 − 2) / 2.8333 = 1.4142
- x₃ = 1.41421356... (sahihi hadi nafasi 8 za desimali)
### Njia ya Secant
Kama njia ya Newton lakini inakadiria derivative:
x_{n+1} = x_n − f(x_n) · (x_n − x_{n-1}) / (f(x_n) − f(x_{n-1}))
| Mali | Thamani |
|----------|-------|
| Muunganisho | Superlinear (agizo ≈ 1.618, uwiano wa dhahabu) |
| Inahitaji | Makisio mawili ya awali (hakuna derivative inayohitajika) |
### Ulinganisho wa Mbinu za Kutafuta Mizizi
| Mbinu | Muunganisho | Mbadala Inahitajika? | Imehakikishwa? | Gharama kwa Hatua |
>>
| Sehemu mbili | Mstari (1) | Hapana | Ndiyo | Eval 1 ya chaguo la kukokotoa |
| Newton-Raphson | Quadratic (2) | Ndiyo | Hapana | 2 tathmini za kazi |
| Safi | Superlinear (1.618) | Hapana | Hapana | Eval 1 ya chaguo la kukokotoa |
| Mbinu ya Brent | Superlinear | Hapana | Ndiyo | Inatofautiana |
**Njia ya Brent** inachanganya mgawanyiko (muunganisho uliohakikishwa) na ukalimani wa kiduta/kinyume cha quadratic (muunganisho wa haraka). Ni kitafuta-msingi chaguo-msingi katika maktaba nyingi za nambari.
---

## Muunganisho wa Nambari (Quadrature)
Inakokotoa ∫ₐᵇ f(x) dx takriban.
### Mbinu
| Mbinu | Mfumo | Hitilafu | Agizo |
|--------|-----------------|-------|
| **Mstatili (katikati)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapezoidal** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Simpson's 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Simpson's 3/8** | Hutumia pointi 4 zilizowekwa kwa nafasi sawa | O(h⁴) | 4 |
| **Gaussian quadrature** | Uwekaji bora wa nodi | O(h²ⁿ) | n pointi |
### Kanuni za Mchanganyiko
Kwa n vipindi vidogo vya upana h = (b-a)/n:
| Kanuni | Mfumo wa Mchanganyiko | Hitilafu |
|------|-------------------|-------|
| Mchanganyiko wa Trapezoidal | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Composite Simpson's | h/3[f(a) + 4Σf(isiyo ya kawaida) + 2Σf(hata) + f(b)] | O(h⁴) |
**Mfano Uliofanya Kazi:** Kadirio ∫₀¹ e^(−x²) dx kwa kutumia trapezoidal ya mchanganyiko na n = 4.
- h = 0.25, pointi: 0, 0.25, 0.5, 0.75, 1
- f(0) = 1, f(0.25) = 0.9394, f(0.5) = 0.7788, f(0.75) = 0.5698, f(1) = 0.3679
- T = 0.25[1/2 + 0.9394 + 0.7788 + 0.5698 + 0.3679/2] = 0.25[1/2 + 2.2880 + 0.1840] = 0.7430
- Thamani ya kweli: ≈ 0.7468 (kosa ≈ 0.5%)
### Quadrature Inayobadilika
Hugawanya vipindi kiotomatiki ambapo chaguo za kukokotoa hutofautiana kwa haraka, kwa kutumia pointi chache ambapo ni laini. Hivi ndivyo`scipy.integrate.quad`hutumia (kulingana na QUADPACK).
---

## Tafsiri
Kukadiria thamani kati ya pointi za data zinazojulikana.
### Mbinu
| Mbinu | Maelezo | Ulaini | Kutetemeka |
|--------|-------------|------------|-------------|
| **Jirani wa karibu** | Tumia sehemu ya data iliyo karibu zaidi | Isiyoendelea | Hakuna |
| **Mstari** | Unganisha pointi kwa mistari iliyonyooka | C⁰ (inayoendelea) | Hakuna |
| **Polynomial (Lagrange)** | Polynomial moja kupitia pointi zote | C^∞ | Kali kwa pointi nyingi (jambo la Runge) |
| **Msururu wa ujazo** | Mchemraba wa kipande, laini kwenye viungo | C² | Ndogo |
| **Kitendaji cha msingi wa radi** | Uzito wa jumla ya kernels radial | Inategemea kernel | Chini |
### Ufafanuzi wa Lagrange
Kwa kuzingatia n+1 pointi (x₀, y₀), ..., (xₙ, yₙ), nambari ya kipekee ya aina nyingi za digrii ≤ n kupita pointi zote:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Hali ya Runge:** Ufafanuzi wa polinomia wa hali ya juu katika sehemu zilizopangwa kwa usawa unaweza kuzunguka kwa kasi karibu na kingo. Imepunguzwa kwa kutumia nodi za Chebyshev au splines.
### Mijazo ya Ujazo
Polimanomia za ujazo za vipande vipande ambazo ni C² zinazoendelea (vito vya pili vinavyoendelea).
| Aina | Hali ya mpaka |
|------|-------------------|
| Mstari wa asili | S''(x₀) = S''(xₙ) = 0 |
| Mstari uliofungwa | S'(x₀) na S'(xₙ) imebainishwa |
| Sio-fundo | Nyingine ya tatu inayoendelea katika x₁ na xₙ₋₁ |
---

## Vitatuzi vya ODE
Kutatua milinganyo ya kawaida ya tofauti dy/dt = f(t, y) kwa nambari.
### Mbinu ya Euler
Kitatuzi rahisi zaidi cha ODE.
**Sasisho:** y_{n+1} = y_n + h · f(t_n, y_n)
| Mali | Thamani |
|----------|-------|
| Agizo | 1 (hitilafu kwa kila hatua: O(h²), kimataifa: O(h)) |
| Utulivu | Imara kwa masharti (h ndogo inahitajika) |
| Gharama | Tathmini 1 ya utendakazi kwa kila hatua |
### Mbinu za Runge-Kutta
| Mbinu | Agizo | Hatua | Vidokezo |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Rahisi |
| **Kituo cha kati** | 2 | 2 | Usahihi bora |
| **Heun's (RK2)** | 2 | 2 | Mtabiri-msahihishaji |
| **Classic RK4** | 4 | 4 | Farasi wa kawaida |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Ukubwa wa hatua unaobadilika (hutumika katika ode45) |
### Classic RK4 (agizo la 4 Runge-Kutta)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Mali | Thamani |
|----------|-------|
| Agizo | 4 (kosa la kimataifa: O(h⁴)) |
| Gharama | Tathmini 4 za utendakazi kwa kila hatua |
| Utulivu | Bora zaidi kuliko Euler |
| Matumizi | Chaguomsingi kwa ODE zisizo ngumu |
### ODE ngumu
**ODE ngumu** ina viambajengo ambavyo hutofautiana kwa mizani tofauti ya saa. Mbinu dhahiri (Euler, RK4) zinahitaji saizi ndogo za hatua.
| Mbinu | Aina | Utulivu |
|--------|------|-----------|
| Euler Isiyo wazi | Dhahiri | A-imara (imara bila masharti) |
| Mfumo wa Kutofautisha Nyuma (BDF) | Dhahiri | A-imara (hadi agizo 5) |
| Runge-Kutta Isiyo wazi | Dhahiri | Vibadala vya L-imara vipo |
| LSODA | Otomatiki | Hubadilisha kati ya ngumu/isiyo ngumu |
---

## Utulivu wa Nambari na Uwekaji
### Nambari ya Hali
**nambari ya hali** hupima ni kiasi gani matokeo ya tatizo hubadilika ikilinganishwa na mabadiliko madogo katika ingizo.
Kwa mfumo wa mstari Ax = b: κ(A) = ||A|| · ||A⁻¹||
| κ(A) | Tafsiri |
|-------|---------------|
| ≈ 1 | Iliyo na hali nzuri |
| 10³ | Nyeti kidogo |
| 10⁸ | Haina hali mbaya (poteza ~ tarakimu 8 za usahihi) |
| → ∞ | Umoja (hakuna suluhisho la kipekee) |
### Uthabiti wa Kanuni
Algoriti ni **imara kwa nambari** ikiwa misukosuko midogo katika ingizo husababisha misukosuko midogo katika utoaji (ikilinganishwa na nambari ya hali ya tatizo).
| Algorithm | Imara? | Vidokezo |
|-----------|---------|--------|
| Kuondolewa kwa Gaussian kwa kugeuza sehemu | Ndiyo | Mbinu ya kawaida |
| Kukokotoa maadili kupitia QR | Ndiyo | Imara ya nyuma |
| Muhtasari wa Naive (kubwa + ndogo kwanza) | Hapana | Tumia Kahan kujumlisha |
| Inakokotoa tofauti kama E[X²] − (E[X])² | Uwezekano hapana | Tumia algoriti ya mtandaoni ya Welford |
### Kanuni za Mtandaoni za Welford
Uhesabuji thabiti wa idadi ya maana na tofauti:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Hii huepuka kughairiwa kwa maafa ambayo hutokea katika fomula ya pasi-mbili isiyo na ufahamu.
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Mbinu ya Nambari | Maombi |
|-------------------------------|
| Sehemu ya kuelea (fp16/fp32/bf16) | Mafunzo ya usahihi mchanganyiko, quantisation ya mfano, ufanisi wa kumbukumbu |
| Utafutaji wa mizizi | Upeo wa makadirio ya uwezekano (kupata wapi gradient = 0) |
| Ujumuishaji wa nambari | Maoni ya Bayesian (kuweka uwezekano wa kando), maadili yanayotarajiwa |
| Tafsiri | Kulainisha, kuiga, miundo mbadala, vitendaji vya kuwezesha |
| Vitatuzi vya ODE | ODE za Neural, RNN za wakati unaoendelea, mienendo ya idadi ya watu, ML yenye taarifa za fizikia |
| Nambari ya masharti | Kuelewa maswala ya nambari katika urejeshaji wa mstari, milinganyo ya kawaida |
| Muhtasari thabiti | Utendaji wa upotezaji wa kompyuta, takwimu za kuhalalisha bechi |
| RK4 / visuluhishi vinavyobadilika | Kuiga mifumo ya nguvu, mafunzo ya mitandao ya kina |
---

## Muhtasari
| Mada | Wazo la Msingi | Mbinu muhimu |
|-------|-----------|------------|
| Sehemu ya kuelea | Uwakilishi kamili wa usahihi | IEEE 754, Kahan majumuisho |
| Utafutaji wa mizizi | Tatua f(x) = 0 | Bisection, Newton-Raphson, Brent's |
| Ujumuishaji wa nambari | Takriban ∫f(x)dx | Trapezoidal, Simpson's, Gaussian quadrature |
| Tafsiri | Kadiria kati ya pointi za data | Vipande vya ujazo, Lagrange, RBF |
| Vitatuzi vya ODE | Tatua dy/dt = f(t,y) | Euler, RK4, mbinu za kurekebisha |
| Utulivu | Unyeti wa makosa ya kuzungusha | Nambari ya hali, algoriti thabiti |
Njia za nambari ni pale hisabati inapokutana na ukweli. Hakuna kompyuta inayoweza kuwakilisha nambari nyingi halisi, hakuna derivative inayokokotolewa kiishara katika mazoezi, na hakuna kiunga kinachotathminiwa kwa njia funge kwa matatizo ya ulimwengu halisi. Kuelewa mbinu za nambari hukuwezesha kuchagua algoriti sahihi, kutabiri usahihi wake, na kuepuka hitilafu fiche zinazotokana na hesabu ya usahihi wa kikomo.