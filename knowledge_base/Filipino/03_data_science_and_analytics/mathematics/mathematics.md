---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Matematika
Ang matematika ay hindi lamang isang asignaturang pinag-aaralan sa paaralan — pinapatibay nito ang halos lahat ng larangang teknikal. Ginagamit ito ng pisika upang ilarawan ang uniberso. Ginagamit ito ng computer science upang magdisenyo ng mga algorithm. Ginagamit ito ng machine learning para i-optimize ang mga timbang. Ginagamit ito ng pananalapi sa panganib sa presyo. Hindi kailangan ang mastery ng bawat branch, ngunit ang pag-unawa sa landscape — at pag-alam kung saan nalalapat ang bawat branch — ay ginagawang mas madaling maunawaan ang iba pang mga paksa.
---

## Sistema ng Numero
Bago ang anumang bagay, nakakatulong na maunawaan ang mga uri ng mga numero na iyong ginagamit. Pinapalawak ng bawat layer ang nauna upang malutas ang problemang hindi magawa ng lumang layer.
| Uri ng Numero | Ano ang Kasama Nito | Bakit Ito Naimbento | Halimbawa |
|---|---|---|---|
| Mga natural na numero | 1, 2, 3, 4, ... | Nagbibilang ng mga bagay | 5 mansanas |
| Buong mga numero | 0, 1, 2, 3, ... | Kumakatawan sa "wala" | 0 degrees |
| Mga integer | ..., −2, −1, 0, 1, 2, ... | Utang, temperatura sa ibaba ng zero | −15°C |
| Mga makatwirang numero | p/q kung saan q ≠ 0 | Hindi pantay na paghahati ng mga bagay | 1/3, 0.75 |
| Mga numerong hindi makatwiran | Hindi maipahayag bilang mga fraction | Mga dayagonal, bilog, paglaki | √2, π, e |
| Mga totoong numero | Lahat ng makatwiran + hindi makatwiran | Ang kumpletong linya ng numero | 3.14159... |
| Mga haka-haka na numero | Multiple ng i = √(−1) | Paglutas ng x² + 1 = 0 | 3i |
| Mga kumplikadong numero | a + bi (tunay + haka-haka) | Electrical engineering, quantum mechanics | 2 + 3i |
---

## Arithmetic at Number Theory
Ang mga pangunahing kaalaman: karagdagan, pagbabawas, pagpaparami, paghahati, at ang mga panuntunang namamahala sa kanilang pagkakasunud-sunod.
**Order of operations** (PEMDAS/BODMAS): Parentheses → Exponents → Multiplication/Division (kaliwa pakanan) → Addition/Subtraction (kaliwa pakanan).
**Prime numbers** — mga buong numero na mas malaki sa 1 na walang mga divisors maliban sa 1 at ang kanilang mga sarili — ay ang mga atomo ng teorya ng numero. Ang unang ilang: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Bakit mahalaga ang mga prime na lampas sa klase ng matematika: umaasa ang modernong pag-encrypt (RSA) sa katotohanang madali ang pagpaparami ng dalawang malalaking prime, ngunit ang pagsasaalang-alang sa resulta pabalik ay brutal sa computation.
**Mga kapaki-pakinabang na operasyon:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) ng 24 at 36: 12
- Least Common Multiple (LCM) ng 4 at 6: 12
---

## Algebra
Ang algebra ay kung saan ka huminto sa pagtatrabaho sa mga partikular na numero at magsimulang magtrabaho kasama ang *mga relasyon*. Ang isang variable na tulad ng`x`ay walang nakapirming halaga — kinakatawan nito ang anumang nagpapatotoo sa equation.
**Ang quadratic formula** ay lumulutas sa ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Mga karaniwang uri ng function at kung saan lumalabas ang mga ito:**
| Function | Formula | Hugis | Halimbawa ng Tunay na Daigdig |
|---|---|---|---|
| Linear | y = mx + b | Tuwid na linya | Gastos sa bawat unit sa flat rate |
| Quadratic | y = ax² + bx + c | Parabola | Galaw ng projectile, distansya ng pagpepreno |
| Exponential | y = a × b² | Mabilis na paglaki/pagkabulok | Pinagsamang interes, paglaki ng populasyon, pagkalat ng viral |
| Logarithmic | y = log_b(x) | Mabagal na paglaki, kabaligtaran ng exponential | Decibel scale, pH scale, pagiging kumplikado ng algorithm |
**Susing bokabularyo:**
- **Domain**: lahat ng wastong input (hal., hindi maaaring hatiin sa zero, hindi maaaring kumuha ng √ ng negatibo sa reals)
- **Range**: lahat ng posibleng output
- **Slope** (m): rate ng pagbabago — "para sa bawat 1 unit ng x, y pagbabago ng m"
- **Harang**: kung saan tumatawid ang function sa isang axis
---

## Geometry
Pinag-aaralan ng geometry ang mga hugis, sukat, at spatial na relasyon. Nagpapakita ito sa lahat ng dako: ginagamit ito ng mga game engine para sa pag-render, ginagamit ito ng robotics para sa pagpaplano ng landas, ginagamit ito ng arkitektura para sa disenyo ng istruktura.
**Mga mahahalagang formula:**
| Hugis | Ari-arian | Formula |
|---|---|---|
| Tatsulok | kabuuan ng anggulo | 180° |
| Quadrilateral | kabuuan ng anggulo | 360° |
| Circle | Circumference | 2πr |
| Circle | Lugar | πr² |
| Sphere | Dami | (4/3)πr³ |
| Kanang tatsulok | Pythagorean theorem | a² + b² = c² |
**π (pi)** ≈ 3.14159 — ang ratio ng circumference ng anumang bilog sa diameter nito. Lumalabas ito sa mga lugar na hindi mo inaasahan: probability (normal distribution), engineering (signal processing), maging ang equation para sa uncertainty principle ng Heisenberg.
---

## Calculus
Pag-aaral ng calculus *pagbabago* at *akumulasyon*. Kung ang algebra ang humahawak ng mga snapshot, ang calculus ang humahawak ng mga motion picture.
### Differential Calculus
Mga rate ng pagbabago. Ang derivative na f'(x) ay nagsasabi sa iyo kung gaano kabilis ang pagbabago ng f sa anumang punto.
| Function f(x) | Derivative f'(x) | Intuwisyon |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Panuntunan ng kapangyarihan |
| eˣ | eˣ | Ang tanging function na katumbas ng sarili nitong derivative |
| ln(x) | 1/x | Bumabagal ang rate ng paglago habang tumataas ang x |
| kasalanan(x) | cos(x) | Rate ng pagbabago ng oscillation |
**Bakit mahalaga ang mga derivative sa ML:** gradient descent — ang algorithm na nagsasanay sa karamihan ng mga neural network — ay gumagana sa pamamagitan ng pag-compute ng mga derivatives ng loss function at paghakbang sa direksyon na nagpapababa ng error.
### Pangunahing Panuntunan sa Pagkakaiba
| Panuntunan | Formula | Use Case |
|------|---------|----------|
| **Chain Rule** | (f∘g)' = f'(g(x)) · g'(x) | Mga nested function — backpropagation sa mga neural network |
| ** Panuntunan ng Produkto** | (fg)' = f'g + fg' | Pagpaparami ng dalawang function ng x |
| **Quotient Rule** | (f/g)' = (f'g − fg') / g² | Paghahati ng dalawang function ng x |
### Integral Calculus
Pagtitipon. Ang integral ay kumakatawan sa lugar sa ilalim ng isang kurba. Kung ang mga derivatives ay sumagot ng "gaano kabilis ito nagbabago?", ang mga integral ay sumagot ng "magkano ang naipon?"
Ang **pangunahing theorem ng calculus** ay nag-uugnay sa parehong: ang pagkita ng kaibhan at pagsasama ay mga kabaligtaran na operasyon.
| Integral | Resulta | Use Case |
|----------|--------|----------|
| ∫ xⁿ dx | xⁿ⁺¹/(n+1) + C | Lugar sa ilalim ng polynomial curves |
| ∫ eˣ dx | eˣ + C | Kabuuang naipon na paglago |
| ∫ 1/x dx | ln|x| + C | Logarithmic accumulation |
---

## Mga set
Ang **set** ay isang koleksyon ng mga natatanging bagay — ang pundasyon ng modernong matematika.
| Operasyon | Simbolo | Ibig sabihin | Halimbawa (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Unyon | A ∪ B | Mga elemento sa alinmang hanay | {1, 2, 3, 4} |
| Intersection | A ∩ B | Mga elemento sa parehong hanay | {2} |
| Pagkakaiba | A \ B | Mga Elemento sa A ngunit hindi B | {1, 3} |
| Walang laman na hanay | ∅ | Walang laman | {} |
| Subset | A ⊂ B | Ang lahat ng mga elemento ng A ay nasa B | {1,2} ⊂ {1,2,3} |
Ang teorya ng set ay lumalabas sa mga database (Ang SQL JOIN ay mahalagang nakatakdang mga operasyon), probabilidad (ang mga kaganapan ay mga hanay ng mga kinalabasan), at programming (mga set, hash na mapa).
---

## Binary at Number Base
Ang mga computer ay nag-iisip sa binary (base 2): 0s at 1s lamang. Ang mga tao ay nag-iisip sa decimal (base 10). Ang mga programmer ay kadalasang gumagamit ng hexadecimal (base 16) bilang isang compact na paraan upang kumatawan sa binary.
| Base | Mga Digit na Ginamit | Halimbawa | Katumbas ng Decimal |
|---|---|---|---|
| Binary (base 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Decimal (base 10) | 0–9 | 11 | 11 |
| Hexadecimal (base 16) | 0–9, A–F | B | 11 |
| Hexadecimal | 0–9, A–F | A3 | 160 + 3 = 163 |
**Bakit ito mahalaga:** bawat piraso ng data sa isang computer — teksto, mga larawan, audio, video — sa huli ay binary lang. Ang isang byte (8 bits) ay maaaring kumatawan sa 256 natatanging mga halaga. Ang mga kulay sa CSS (#FF5733), mga memory address (0x7FFF), at mga IP address ay gumagamit lahat ng hex dahil pini-compress nito ang mahahabang binary string sa isang bagay na nababasa.
---

## Linear Algebra para sa ML at Graphics
Ang linear algebra — mga vector, matrice, at mga pagbabagong-anyo — ay ang mathematical engine sa likod ng machine learning, computer graphics, physics simulation, at search engine.
### Mga Vector
Ang **Vectors** ay mga nakaayos na listahan ng mga numero. Sa ML, ang bawat data point ay vector ng mga feature:
- [23, 1.8, 75] ay maaaring kumatawan sa edad ng isang tao, taas sa metro, at timbang sa kg.
| Vector Operation | Formula | Use Case |
|-----------------|---------|----------|
| **Dagdag** | a + b = [a₁+b₁, a₂+b₂, ...] | Pinagsasama-sama ang mga feature na vector |
| **Scalar multiplication** | c·a = [c·a₁, c·a₂, ...] | Mga tampok sa pag-scale |
| **Produktong tuldok** | a·b = Σ aᵢbᵢ | Pagkakatulad, mga projection |
| **Norm (magnitude)** | ||a|| = √(Σ aᵢ²) | Haba ng vector |
| **Cross product** | a × b (3D lang) | Perpendikular na vector, lugar |
### Matrice
Ang **Matrice** ay mga 2D array ng mga numero. Ang mga timbang ng neural network ay iniimbak bilang mga matrice. Ang isang batch ng 100 larawan ay maaaring isang matrix ng hugis (100, 784) — 100 row, bawat isa ay may 784 pixel value.
**Mga pangunahing operasyon:**
| Operasyon | Ano ang Ginagawa Nito | Saan Ito Nagpapakita |
|---|---|---|
| Produktong tuldok | Sinusukat ang pagkakatulad sa pagitan ng dalawang vector | Mga sistema ng rekomendasyon, pagkakatulad ng cosine |
| Pagpaparami ng matris | Pinagsasama ang mga linear na pagbabago | Ang bawat layer ng isang neural network |
| Eigenvalues/eigenvectors | Mga direksyon sa isang matrix scale (hindi umiikot) | Pagbawas ng dimensyon ng PCA, PageRank |
| Ranggo ng matrix | Dami ng independiyenteng impormasyon | Compression, low-rank approximation |
| Ilipat | I-flip ang mga row at column | Gradient computation |
| Baliktad | A⁻¹ na ang A·A⁻¹ = I | Paglutas ng mga linear system |
**Cosine similarity** = (a·b) / (||a|| × ||b||) — mula −1 (kabaligtaran) hanggang 1 (parehong direksyon). Ito ay kung paano sinusukat ng mga search engine kung ang dalawang dokumento ay "halos magkatulad na bagay" at kung paano pinaghahambing ng mga modelo ang pagkakatulad ng semantiko.
---

## Buod
| Sangay | Pangunahing Tanong | Key Application |
|---|---|---|
| Arithmetic at Number Theory | Paano kumikilos ang mga numero? | Cryptography, pag-hash |
| Algebra | Paano nauugnay ang mga hindi kilala? | Pagmomodelo, mga equation |
| Geometry | Paano gumagana ang mga hugis at espasyo? | Mga graphic, robotics, arkitektura |
| Calculus | Paano nagbabago ang mga bagay? | Pagsasanay sa mga neural network, pisika |
| Itakda ang Teorya | Paano nauugnay ang mga koleksyon? | Mga database, posibilidad |
| Linear Algebra | Paano gumagana ang mga pagbabago? | ML, graphics, mga search engine |
Hindi lahat ng mga paksang ito ay kailangan kaagad. Gayunpaman, habang ang isa ay lumalalim sa anumang teknikal na larangan, ang mga pundasyong ito ay nagiging mas may kaugnayan. Ang bawat sangay ay nagiging mas malinaw kapag naunawaan ang problemang idinisenyo upang lutasin.