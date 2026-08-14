<!--
---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
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
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teorya ng Numero
Ang teorya ng numero ay ang pag-aaral ng mga integer — mga buong numero at ang kanilang mga katangian. Tinawag ito ni Gauss na "reyna ng matematika." Sa kabila ng pag-aaral ng mga pinakasimpleng bagay (1, 2, 3, ...), ang teorya ng numero ay gumagawa ng ilan sa pinakamalalim at pinakamahirap na problema sa lahat ng matematika. Sa ngayon, pinagbabatayan nito ang modernong cryptography, hashing algorithm, error-correcting codes, at random number generation.
---

## Divisibility at ang Division Algorithm
### Mga Pangunahing Kahulugan
| Termino | Kahulugan | Halimbawa |
|------|------------|---------|
| **Hati** | isang \| Ang ibig sabihin ng b ay ∃k ∈ ℤ: b = ak | 3 \| 12 (mula noong 12 = 3 × 4) |
| **Divisor** | Isang numero na naghahati sa isa pang | Mga divisors ng 12: 1, 2, 3, 4, 6, 12 |
| **Marami** | b ay isang multiple ng a kung a \| b | Ang 15 ay isang multiple ng 5 |
| **Quotient** | Ang resulta ng paghahati | 17 ÷ 5 = quotient 3 |
| **Natitira** | Ano ang natitira pagkatapos ng dibisyon | 17 ÷ 5 = natitirang 2 |
### Ang Division Algorithm
Para sa anumang mga integer a at b na may b > 0, mayroong mga natatanging integer na q (quotient) at r (natitira) tulad ng:
a = bq + r, kung saan 0 ≤ r < b
**Halimbawa:** 23 = 5 × 4 + 3. Quotient q = 4, remainder r = 3.
### Mga Katangian ng Divisibility
| Ari-arian | Pahayag |
|----------|-----------|
| Transitivity | Kung ang isang \| b at b \| c, pagkatapos ay isang \| c |
| Linearity | Kung ang isang \| b at isang \| c, pagkatapos ay isang \| (bx + cy) para sa lahat ng integer x, y |
| Paghahambing | Kung ang isang \| b at b > 0, pagkatapos ay a ≤ b |
| Walang kabuluhan | isang \| 0 para sa lahat a; 1 \| a para sa lahat a; isang \| a para sa lahat a ≠ 0 |
---

## Pinakamahusay na Common Divisor (GCD)
Ang **pinakamalaking karaniwang divisor** ng a at b, na may kahulugang gcd(a, b), ay ang pinakamalaking positive integer na naghahati sa parehong a at b.
### Ang Euclidean Algorithm
Ang pinaka mahusay na klasikal na algorithm para sa pag-compute ng GCD.
**Pangunahing insight:** gcd(a, b) = gcd(b, a mod b)
**Algorithm:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Nagtrabahong Halimbawa:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Resulta: gcd(252, 105) = 21
| Ari-arian | Halaga |
|----------|-------|
| Pagiging kumplikado ng oras | O(log(min(a, b))) |
| Pagiging kumplikado ng espasyo | O(1) umuulit |
### Pagkakakilanlan ni Bézout
Para sa anumang mga integer a, b, mayroong mga integer x, y tulad na:
ax + by = gcd(a, b)
**Extended Euclidean Algorithm** compute gcd(a, b) at ang coefficients x, y nang sabay-sabay.
**Nagtrabaho Halimbawa:** Hanapin ang x, y na 252x + 105y = 21.
- Bumalik-pagpapalit mula sa Euclidean algorithm:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Kaya x = −2, y = 5. Suriin: 252(−2) + 105(5) = −504 + 525 = 21.
### Mga Pangunahing Katangian ng GCD
| Ari-arian | Pahayag |
|----------|-----------|
| gcd(a, 0) | = isang |
| gcd(a, 1) | = 1 (ang a at 1 ay palaging coprime) |
| gcd(a, b) = gcd(b, a) | Commutative |
| gcd(a, b) = gcd(a, b + ka) | Ang pagdaragdag ng mga multiple ay hindi nagbabago sa GCD |
| gcd(ca, cb) | = c · gcd(a, b) |
| Coprime | Ang ibig sabihin ng gcd(a, b) = 1 ay ang a at b ay hindi magkaparehong salik |
---

## Prime Numbers
Ang **prime** ay isang integer na mas malaki sa 1 na ang mga positibong divisors lang ay 1 at ang sarili nito.
### Mga Pangunahing Katangian
| Ari-arian | Pahayag |
|----------|-----------|
| **Pundamental Theorem of Arithmetic** | Ang bawat integer n > 1 ay may natatanging prime factorization |
| **Infinitude ng primes** | Mayroong walang katapusang maraming prime (Euclid, ~300 BC) |
| **Prime Number Theorem** | Ang bilang ng mga prime ≤ n ay tinatayang n / ln(n) |
| **Posulate ni Bertrand** | Para sa bawat n > 1, mayroong prime p na may n < p < 2n |
### Ang Mga Unang Primes
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Prime Factorization
Ang bawat integer n > 1 ay maaaring isulat nang natatangi bilang:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
kung saan ang p₁ < p₂ < ... < pₖ ay mga primes at aᵢ ≥ 1.
**Mga Halimbawa:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Paggamit ng factorization para kalkulahin ang GCD at LCM:**
- gcd(a, b) = produkto ng min powers ng shared primes
- lcm(a, b) = produkto ng max powers ng lahat ng primes
**Halimbawa:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Salain ng Eratosthenes
Ang klasikal na algorithm para sa paghahanap ng lahat ng prime hanggang sa isang limitasyon N.
| Ari-arian | Halaga |
|----------|-------|
| Pagiging kumplikado ng oras | O(N log log N) |
| Pagiging kumplikado ng espasyo | O(N) |
**Algorithm:**
1. Ilista ang lahat ng integer mula 2 hanggang N.
2. Magsimula sa p = 2. I-cross out ang lahat ng multiple ng p (nagsisimula sa p²).
3. Hanapin ang susunod na uncrossed na numero > p. Itakda ang p sa numerong iyon.
4. Ulitin hanggang p² > N. Ang lahat ng hindi naka-cross na numero ay prime.
### Pangunahing Pagsubok
| Paraan | Uri | Oras | Use Case |
|--------|------|------|----------|
| Dibisyon ng pagsubok | Deterministic | O(√n) | Maliit na numero |
| Fermat test | Probabilistic | O(k log² n) | Mabilis na screening |
| Miller-Rabin | Probabilistic | O(k log² n) | Pangkalahatang layunin |
| AKS | Deterministic | O(log⁶ n) | Teoretikal na kahalagahan |
**Fermat primality test:** Kung p ang prime at gcd(a, p) = 1, aᵖ⁻¹ ≡ 1 (mod p). Kung nabigo ito para sa ilang a, kung gayon ang p ay tiyak na pinagsama-sama. Kung pumasa ito para sa maraming random na halaga, ang p ay malamang na prime.
**Caveat:** Ang mga numero ng Carmichael (hal., 561) ay pumasa sa Fermat test para sa lahat ng coprime base ngunit composite. Iniiwasan ni Miller-Rabin ang isyung ito.
---

## Modular Arithmetic
Modular arithmetic studies integers under "wraparound" — arithmetic on a clock face.
### Congruence Relations
Ang ibig sabihin ng ≡ b (mod n) ay n | (a − b), ibig sabihin, ang a at b ay nag-iiwan ng parehong natitira kapag hinati sa n.
### Arithmetic Properties
| Operasyon | Panuntunan |
|-----------|------|
| Dagdag | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Multiplikasyon | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Exponentiation | aᵇ mod n maaaring makalkula nang mahusay sa pamamagitan ng paulit-ulit na pag-squaring |
| Negasyon | (−a) mod n = n − (a mod n) |
### Modular Exponentiation
Pag-compute sa mod n mahusay gamit ang **paulit-ulit na pag-squaring**:
**Nagtrabaho Halimbawa:** 3¹³ mod 7
- 13 sa binary: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Ari-arian | Halaga |
|----------|-------|
| Pagiging kumplikado ng oras | O(log b · log² n) |
| Pagiging kumplikado ng espasyo | O(1) |
### Totient Function ni Euler
Binibilang ng φ(n) ang mga integer mula 1 hanggang n na coprime sa n.
| n | φ(n) | Coprime integer |
|---|------|------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 ang prime) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Mga Formula:**
- Kung ang p ay prime: φ(p) = p − 1
- Kung ang p ay prime: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Kung gcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (multiplikativity)
- Pangkalahatan: φ(n) = n · Π_{p|n} (1 − 1/p) kung saan ang produkto ay higit sa natatanging prime factor ng n
---

## Mga Pangunahing Teorema
### Ang Little Theorem ni Fermat
Kung ang p ay prime at gcd(a, p) = 1, kung gayon:
aᵖ⁻¹ ≡ 1 (mod p)
**Corollary (para sa lahat ng a):** aᵖ ≡ a (mod p)
**Gamitin:** Mabilis na modular inverse kapag ang modulus ay prime: a⁻¹ ≡ aᵖ⁻² (mod p)
**Nagtrabaho Halimbawa:** Maghanap ng 3⁻¹ mod 7.
- Ni Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Suriin: 3 × 5 = 15 ≡ 1 (mod 7).
### Euler's Theorem (Generalization of Fermat)
Kung ang gcd(a, n) = 1, kung gayon:
a^φ(n) ≡ 1 (mod n)
Ito ay pangkalahatan ang Fermat's Little Theorem mula sa primes hanggang sa anumang modulus.
### Chinese Remainder Theorem (CRT)
Kung ang m₁, m₂, ..., mₖ ay pairwise coprime, ang system:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
ay may natatanging solusyon modulo M = m₁ · m₂ · ... · mₖ.
**Nagtrabaho Halimbawa:** Lutasin ang x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Maghanap ng mga inverse: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Suriin: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Wilson's Theorem
(p − 1)! ≡ −1 (mod p) kung at kung p ang prime.
Karamihan ay theoretical interest — hindi praktikal para sa primality testing dahil mahal ang computing factorial.
### Quadratic Residues
Ang integer a ay **quadratic residue mod n** kung ang x² ≡ a (mod n) ay may solusyon.
**Ang pamantayan ni Euler:** a ay isang parisukat na residue mod prime p iff a^((p−1)/2) ≡ 1 (mod p).
**Simbolo ng alamat:** (a/p) = a^((p−1)/2) mod p, nagbibigay ng +1, −1, o 0.
**Quadratic Reciprocity** (Gauss): Para sa natatanging odd prime p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Ang malalim na teorem na ito ay nag-uugnay sa mga parisukat na nalalabi sa iba't ibang prime at may walong karagdagang batas na humahawak sa mga kaso p = 2.
---

## Mga Application sa Cryptography
### RSA Cryptosystem
Ang pinaka-tinatanggap na pampublikong-key na cryptosystem, batay sa kahirapan ng pag-factor ng malalaking integer.
**Setup:**
1. Pumili ng dalawang malalaking prime p, q (karaniwang 1024+ bit bawat isa)
2. Compute n = pq at φ(n) = (p−1)(q−1)
3. Piliin ang e na ang 1 < e < φ(n) at gcd(e, φ(n)) = 1 (common: e = 65537)
4. Compute d ≡ e⁻¹ (mod φ(n)) gamit ang Extended Euclidean Algorithm
5. **Public key:** (n, e). **Pribadong susi:** (n, d)
**Encryption:** c = mᵉ mod n (kung saan ang m ay ang plaintext na mensahe)
**Decryption:** m = cᵈ mod n
**Bakit ito gumagana:** cᵈ = m^(ed) ≡ m (mod n) ng Euler's theorem, mula noong ed ≡ 1 (mod φ(n)).
**Seguridad:** Ang pag-factor ng n sa p at q ay hindi magagawa sa computation para sa malalaking n (2048+ bits). Kung walang p at q, hindi macompute ng isang attacker ang φ(n) at sa gayon ay hindi mahanap ang d.
### Diffie-Hellman Key Exchange
Nagbibigay-daan sa dalawang partido na magtatag ng isang nakabahaging lihim sa isang hindi secure na channel.
**Setup:** Sumang-ayon sa isang malaking prime p at isang generator g (mod p).
**Protocol:**
1. Pumili si Alice ng lihim na a, ipinadala ang A = gᵃ mod p kay Bob
2. Pinili ni Bob ang sikretong b, ipinadala ang B = gᵇ mod p kay Alice
3. Kinakalkula ni Alice ang s = Bᵃ mod p = gᵃᵇ mod p
4. Kinuwenta ni Bob ang s = Aᵇ mod p = gᵃᵇ mod p
5. Parehong nagbabahagi ng sikretong s = gᵃᵇ mod p
**Seguridad:** Batay sa kahirapan ng **discrete logarithm problem** — paghahanap ng mula sa gᵃ mod p.
### Mga Pag-andar ng Hash at Teorya ng Numero
Gumagamit ang magagandang hash function ng modular arithmetic para pantay na ipamahagi ang mga key:
- **Multiplikatibong pag-hash:** h(k) = (k · A) mod m, kung saan A ≈ m · (√5 − 1) / 2 (golden ratio)
- **Pangkalahatang hashing:** h(k) = ((ak + b) mod p) mod m, kung saan ang p ay prime, ang a, b ay random
---

## Kaugnayan sa Machine Learning at Data Science
| Konsepto ng Teorya ng Numero | Application |
|----------------------|--------------------------|
| Modular arithmetic | Hashing (hash table, hash maps), random na pagbuo ng numero |
| Mga pangunahing numero | Hash table sizing (gumamit ng prime table sizes para mabawasan ang mga banggaan) |
| GCD / Euclidean algorithm | Rational arithmetic, pinapasimple ang mga fraction sa posibilidad |
| Modular exponentiation | Cryptographic na seguridad para sa ML model na naghahatid sa HTTPS |
| Totient ni Euler | RSA key generation, pag-unawa sa mga cryptographic na garantiya |
| Chinese Remainder Theorem | Naipamahagi computation, parallel modular arithmetic |
| Pangunahing pagsubok | Pagbuo ng mga prime para sa mga cryptographic na operasyon |
| Quadratic residues | Quadratic residuosity problema sa advanced cryptography |
| May hangganan na mga field (GF(p), GF(2ᵏ)) | Mga code sa pagwawasto ng error, Reed-Solomon code, AES encryption |
---

## Buod
| Paksa | Pangunahing Ideya | Susing Resulta |
|-------|-----------|------------|
| Divisibility | Dibisyon na may natitira | Algorithm ng division: a = bq + r |
| GCD | Pinakamalaking nakabahaging salik | Euclidean algorithm: O(log n) |
| Primes | Atoms ng integers | Fundamental Theorem of Arithmetic (natatanging factorization) |
| Modular Arithmetic | Wraparound arithmetic | Mga klase ng congruence, modular exponentiation |
| Euler's Totient | Nagbibilang ng mga coprime integer | φ(n) = n · Π(1 − 1/p) |
| Ang Little Theorem ni Fermat | Prime modulus shortcut | aᵖ⁻¹ ≡ 1 (mod p) |
| Teorama ni Euler | Pangkalahatang Fermat | a^φ(n) ≡ 1 (mod n) |
| Chinese Remainder Theorem | Pinagsasama-sama ang mga modular system | Natatanging solusyon mod na produkto ng coprime moduli |
| Cryptography | Mahirap na numero-teoretikong mga problema | RSA (factoring), Diffie-Hellman (discrete log) |
Binabago ng teorya ng numero ang mga simpleng tanong tungkol sa mga integer sa malalim na matematika na may malalim na praktikal na mga aplikasyon. Ang bawat secure na koneksyon sa web, naka-encrypt na mensahe, at digital na lagda ay umaasa sa mga resultang number-theoretic na natuklasan ilang siglo bago umiral ang mga computer. Para sa mga data scientist at ML engineer, ang pag-unawa sa teorya ng numero ay nagbibigay ng insight sa pag-hash, random na pagbuo ng numero, at ang cryptographic na imprastraktura na nagpoprotekta sa data sa transit at sa pahinga.