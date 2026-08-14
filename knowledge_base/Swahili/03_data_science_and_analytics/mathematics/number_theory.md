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
# Nadharia ya Nambari
Nadharia ya nambari ni utafiti wa nambari kamili - nambari nzima na mali zao. Gauss aliiita "malkia wa hisabati." Licha ya kusoma vitu rahisi zaidi (1, 2, 3, ...), nadharia ya nambari hutoa shida kubwa na ngumu zaidi katika hisabati yote. Leo, inasisitiza usimbaji fiche wa kisasa, algoriti za hashing, misimbo ya kusahihisha makosa, na uundaji wa nambari bila mpangilio.
---

## Mgawanyiko na Kanuni ya Mgawanyiko
### Ufafanuzi wa Msingi
| Muda | Ufafanuzi | Mfano |
|------|------------|----------|
| **Mgawanyiko** | \| b ina maana ∃k ∈ ℤ: b = ak | 3 \| 12 (tangu 12 = 3 × 4) |
| **Kigawanyiko** | Nambari inayogawanya nyingine | Vigawanyiko vya 12: 1, 2, 3, 4, 6, 12 |
| **Nyingi** | b ni kizidishio cha a if a \| b | 15 ni kizidishio cha 5 |
| **Nukuu** | Matokeo ya mgawanyiko | 17 ÷ 5 = mgawo 3 |
| **Salio** | Kilichosalia baada ya mgawanyiko | 17 ÷ 5 = salio 2 |
### Kanuni ya Mgawanyiko
Kwa nambari zozote a na b na b > 0, kuna nambari kamili za kipekee q (mgawo) na r (zinazosalia) kama vile:
a = bq + r, ambapo 0 ≤ r < b
**Mfano:** 23 = 5 × 4 + 3. Nukuu q = 4, salio r = 3.
### Sifa za Kugawanyika
| Mali | Taarifa |
|----------|-----------|
| Upitaji | Ikiwa \| b na b \| c, kisha \| c |
| Linearity | Ikiwa \| b na \| c, kisha \| (bx + cy) kwa nambari zote x, y |
| Kulinganisha | Ikiwa \| b na b > 0, kisha a ≤ b |
| Kidogo | \| 0 kwa wote; 1 \| a kwa wote; \| a kwa wote ≠ 0 |
---

## Mgawanyiko Mkuu wa Kawaida (GCD)
**Kigawanyiko kikuu cha kawaida** cha a na b, kinachoashiria gcd(a, b), ni nambari kamili chanya kubwa inayogawanya a na b.
### Kanuni ya Euclidean
Algorithm ya ufanisi zaidi ya classical kwa kompyuta ya GCD.
**Maarifa muhimu:** gcd(a, b) = gcd(b, mod b)
**Algorithm:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Mfano Uliofanyiwa Kazi:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Matokeo: gcd(252, 105) = 21
| Mali | Thamani |
|----------|-------|
| Utata wa wakati | O(logi(min(a,b))) |
| Utata wa nafasi | O(1) mara kwa mara |
### Utambulisho wa Bézout
Kwa nambari zozote a, b, kuna nambari kamili x, y kama vile:
shoka + kwa = gcd(a, b)
**Algorithm Iliyoongezwa ya Euclidean** hukokotoa gcd(a, b) na viambajengo x, y kwa wakati mmoja.
**Mfano Uliofanya Kazi:** Tafuta x, y kiasi kwamba 252x + 105y = 21.
- Kubadilisha nyuma kutoka kwa algorithm ya Euclidean:
  - 21 = 105 − 42 × 2
  - 42 = 252 - 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 - 252 × 2
- Kwa hiyo x = -2, y = 5. Angalia: 252(-2) + 105(5) = -504 + 525 = 21.
### Sifa Muhimu za GCD
| Mali | Taarifa |
|----------|-----------|
| gcd(a, 0) | =a |
| gcd(a, 1) | = 1 (a na 1 daima ni coprime) |
| gcd(a, b) = gcd(b, a) | Inabadilika |
| gcd(a, b) = gcd(a, b + ka) | Kuongeza vizidishi hakubadilishi GCD |
| gcd(ca, cb) | = c · gcd(a, b) |
| Coprime | gcd(a, b) = 1 inamaanisha a na b haishiriki mambo ya kawaida |
---

## Nambari kuu
**prime** ni nambari kamili zaidi ya 1 ambayo vigawanyiko chanya pekee ni 1 na yenyewe.
### Sifa za Msingi
| Mali | Taarifa |
|----------|-----------|
| **Nadharia ya Msingi ya Hesabu** | Kila nambari kamili n > 1 ina uainishaji mkuu wa kipekee |
| **Infinitude of primes** | Kuna primes nyingi sana (Euclid, ~300 BC) |
| **Nadharia ya Nambari Mkuu** | Idadi ya primes ≤ n ni takriban n / ln(n) |
| **Kazi ya Bertrand** | Kwa kila n > 1, kuna p mkuu na n < p < 2n |
### Wakuu wa Kwanza
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Prime Factorization
Kila nambari n > 1 inaweza kuandikwa kipekee kama:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
ambapo p₁ < p₂ < ... < pₖ ni za mwanzo na aᵢ ≥ 1.
**Mifano:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Kutumia factorization kukokotoa GCD na LCM:**
- gcd(a, b) = bidhaa ya nguvu ndogo za primes zilizoshirikiwa
- lcm(a, b) = bidhaa ya mamlaka ya juu ya primes zote
**Mfano:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Ungo wa Eratosthenes
Algorithm ya kawaida ya kupata primes zote hadi kikomo N.
| Mali | Thamani |
|----------|-------|
| Utata wa wakati | O(N logi N) |
| Utata wa nafasi | O(N) |
**Algorithm:**
1. Orodhesha nambari zote kuanzia 2 hadi N.
2. Anza na p = 2. Vunja vizidishi vyote vya p (kuanzia p²).
3. Tafuta nambari inayofuata ambayo haijavuka > uk. Weka p kwa nambari hiyo.
4. Rudia hadi p² > N. Nambari zote ambazo hazijavuka ni kuu.
### Jaribio la Ubora
| Mbinu | Aina | Wakati | Tumia Kesi |
|--------|------|------|-----------|
| Mgawanyiko wa majaribio | Kuamua | O(√n) | Nambari ndogo |
| Mtihani wa Fermat | Uwezekano | O(k logi² n) | Uchunguzi wa haraka |
| Miller-Rabin | Uwezekano | O(k logi² n) | Kusudi la jumla |
| AKS | Kuamua | O(logi⁶ n) | Umuhimu wa kinadharia |
**Jaribio la ubora wa Fermat:** Ikiwa p ni msingi na gcd(a, p) = 1, basi aᵖ⁻¹ ≡ 1 (mod p). Ikiwa hii itashindwa kwa baadhi a, basi p hakika ni mchanganyiko. Ikiwa itapita kwa maadili mengi bila mpangilio, p labda ni ya msingi.
**Tahadhari:** Nambari za Carmichael (k.m., 561) hufaulu jaribio la Fermat kwa besi zote za coprime lakini ni mchanganyiko. Miller-Rabin anaepuka suala hili.
---

## Hesabu ya Msimu
Hesabu za msimu husoma nambari kamili chini ya "mzunguko" - hesabu kwenye uso wa saa.
### Mahusiano ya Mahusiano
a ≡ b (mod n) ina maana n | (a - b), yaani, a na b huacha salio lile lile linapogawanywa na n.
### Sifa za Hesabu
| Operesheni | Kanuni |
|-----------|------|
| Nyongeza | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Kuzidisha | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Ufafanuzi | aᵇ mod n inaweza kukokotwa kwa ufanisi kwa kurudia rudia squaring |
| Kukanusha | (−a) mod n = n − (a mod n) |
### Ufafanuzi wa Msimu
Kukokotoa aᵇ mod n kwa ufanisi kwa kutumia **kupeana mara kwa mara**:
**Mfano Uliofanya Kazi:** 3¹³ mod 7
- 13 kwa binary: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Mali | Thamani |
|----------|-------|
| Utata wa wakati | O(logi b · log² n) |
| Utata wa nafasi | O(1) |
### Kazi ya Totient ya Euler
φ(n) huhesabu nambari kamili kutoka 1 hadi n ambazo ni coprime hadi n.
| n | φ(n) | Nambari kamili za Coprime |
|---|------|------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 ni mkuu) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Mfumo:**
- Ikiwa p ni kuu: φ(p) = p -1
- Ikiwa p ni msingi: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Ikiwa gcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (kuzidisha)
- Jumla: φ(n) = n · Π_{p|n} (1 − 1/p) ambapo bidhaa iko juu ya vipengele muhimu vya n
---

## Nadharia Muhimu
### Nadharia Ndogo ya Fermat
Ikiwa p ni kuu na gcd(a, p) = 1, basi:
aᵖ⁻¹ ≡ 1 ( mod p)
**Muhimu (kwa wote a):** aᵖ ≡ a (mod p)
**Tumia:** Kinyume cha kasi cha moduli wakati moduli ni kuu: a⁻¹ ≡ aᵖ⁻² (mod p)
**Mfano Uliofanya Kazi:** Tafuta 3⁻¹ mod 7.
- Imeandikwa na Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (moduli 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Angalia: 3 × 5 = 15 ≡ 1 (mod 7).
### Nadharia ya Euler (Ujumla wa Fermat)
Ikiwa gcd(a, n) = 1, basi:
a^φ(n) ≡ 1 (mod n)
Hii inajumlisha Nadharia Ndogo ya Fermat kutoka za mwanzo hadi moduli yoyote.
### Nadharia ya Mabaki ya Kichina (CRT)
Ikiwa m₁, m₂, ..., mₖ ni nakala mbili, mfumo:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
ina suluhisho la kipekee modulo M = m₁ · m₂ · ... · mₖ.
**Mfano Uliofanya Kazi:** Tatua x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Tafuta kinyume: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  Miaka 21₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  Miaka 15₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Angalia: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Nadharia ya Wilson
(uk − 1)! ≡ −1 (mod p) ikiwa na tu ikiwa p ni kuu.
Zaidi ya maslahi ya kinadharia - si ya vitendo kwa ajili ya majaribio ya primality kwa kuwa vifaa vya kompyuta ni ghali.
### Mabaki ya Quadratic
Nambari kamili a ni **mabaki ya quadratic mod n** ikiwa x² ≡ a (mod n) ina suluhu.
**Kigezo cha Euler:** a ni mabaki ya quadratic mod prime p if a^((p-1)/2) ≡ 1 (mod p).
**Alama ya hadithi:** (a/p) = a^((p-1)/2) mod p, kutoa +1, −1, au 0.
**Uwiano wa Quadratic** (Gauss): Kwa mihimili isiyo ya kawaida p, q:
(p/q)(q/p) = (−1)^((p-1)/2 · (q−1)/2)
Nadharia hii ya kina inaunganisha mabaki ya quadratic katika kanuni tofauti na ina sheria nane za ziada zinazoshughulikia kesi p = 2.
---

## Maombi ya Kujificha
### Mfumo wa Cryptosystem wa RSA
Mfumo wa siri wa ufunguo wa umma uliosambazwa zaidi, kulingana na ugumu wa kuweka nambari kubwa.
**Mpangilio:**
1. Chagua herufi mbili kubwa p, q (kawaida biti 1024+ kila moja)
2. Kokotoa n = pq na φ(n) = (p−1)(q−1)
3. Chagua e hivi kwamba 1 < e < φ(n) na gcd(e, φ(n)) = 1 (kawaida: e = 65537)
4. Kokotoa d ≡ e⁻¹ (mod φ(n)) kwa kutumia Algorithm Iliyoongezwa ya Euclidean
5. **Ufunguo wa umma:** (n, e). **Ufunguo wa kibinafsi:** (n, d)
**Usimbaji fiche:** c = mᵉ mod n (ambapo m ni ujumbe wa maandishi wazi)
**Usimbuaji fiche:** m = cᵈ mod n
**Kwa nini inafanya kazi:** cᵈ = m^(ed) ≡ m (mod n) kulingana na nadharia ya Euler, tangu ed ≡ 1 (mod φ(n)).
**Usalama:** Kuweka n katika p na q hakuwezekani kwa hesabu kwa n kubwa (biti 2048+). Bila p na q, mshambuliaji hawezi kuhesabu φ(n) na hivyo hawezi kupata d.
### Diffie-Hellman Key Exchange
Huruhusu pande mbili kuanzisha siri iliyoshirikiwa juu ya chaneli isiyo salama.
**Sanidi:** Kubali p kubwa kuu na jenereta g (mod p).
**Itifaki:**
1. Alice anachagua siri a, anatuma A = gᵃ mod p kwa Bob
2. Bob anachagua siri b, anatuma B = gᵇ mod p kwa Alice
3. Alice anakokotoa s = Bᵃ mod p = gᵃᵇ mod p
4. Bob anakokotoa s = Aᵇ mod p = gᵃᵇ mod p
5. Wote wanashiriki siri s = gᵃᵇ mod p
**Usalama:** Kulingana na ugumu wa **tatizo tofauti la logariti** — kutafuta a kutoka gᵃ mod uk.
### Kazi za Hashi na Nadharia ya Nambari
Utendaji mzuri wa heshi hutumia hesabu ya kawaida kusambaza vitufe kwa usawa:
- **Hashing nyingi:** h(k) = (k · A) mod m, ambapo A ≈ m · (√5 − 1) / 2 (uwiano wa dhahabu)
- **Hashing ya ulimwengu wote:** h(k) = ((ak + b) mod p) mod m, ambapo p ni kuu, a, b ni nasibu
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Dhana ya Nadharia ya Nambari | Maombi |
|---------------------|-------------|
| Hesabu ya msimu | Hashi (meza za hashi, ramani za hashi), kizazi cha nambari bila mpangilio |
| Nambari kuu | Upimaji wa ukubwa wa jedwali la hashi (tumia saizi kuu za jedwali ili kupunguza migongano) |
| Algorithm ya GCD / Euclidean | Hesabu ya busara, kurahisisha sehemu katika uwezekano |
| Ufafanuzi wa msimu | Usalama wa kriptografia kwa muundo wa ML unaotumika kupitia HTTPS |
| Totient ya Euler | Kizazi muhimu cha RSA, kuelewa dhamana za kriptografia |
| Nadharia ya Mabaki ya Kichina | Kusambazwa kwa hesabu, hesabu ya msimu sambamba |
| Mtihani wa ubora | Inazalisha matoleo ya awali ya shughuli za kriptografia |
| Mabaki ya quadratic | Tatizo la quadratic residuosity katika cryptography ya hali ya juu |
| Sehemu Filamu (GF(p), GF(2ᵏ)) | Misimbo ya kusahihisha hitilafu, misimbo ya Reed-Solomon, usimbaji fiche wa AES |
---

## Muhtasari
| Mada | Wazo la Msingi | Matokeo Muhimu |
|-------|-----------|------------|
| Mgawanyiko | Mgawanyiko na salio | Algorithm ya mgawanyiko: a = bq + r |
| GCD | Sababu kubwa zaidi iliyoshirikiwa | Algorithm ya Euclidean: O(logi n) |
| Wakuu | Atomi za nambari kamili | Nadharia ya Msingi ya Hesabu (uainishaji wa kipekee) |
| Hesabu ya Msimu | Hesabu za kuzunguka | Madarasa ya mshikamano, ufafanuzi wa msimu |
| Totient ya Euler | Kuhesabu nambari kamili za coprime | φ(n) = n · Π(1 − 1/p) |
| Nadharia Ndogo ya Fermat | Njia ya mkato ya moduli | aᵖ⁻¹ ≡ 1 ( mod p) |
| Nadharia ya Euler | Fermat ya Jumla | a^φ(n) ≡ 1 (mod n) |
| Nadharia ya Mabaki ya Kichina | Kuchanganya mifumo ya msimu | Suluhisho la kipekee la bidhaa ya moduli ya coprime |
| Crystalgraphy | Matatizo magumu ya kinadharia ya nambari | RSA (factoring), Diffie-Hellman (logi tofauti) |
Nadharia ya nambari hubadilisha maswali rahisi kuhusu nambari kamili kuwa hisabati ya kina yenye matumizi ya kina ya vitendo. Kila muunganisho salama wa wavuti, ujumbe uliosimbwa kwa njia fiche na sahihi ya dijitali hutegemea matokeo ya nadharia ya nambari yaliyogunduliwa karne nyingi kabla ya kompyuta kuwepo. Kwa wanasayansi wa data na wahandisi wa ML, uelewa wa nadharia ya nambari hutoa maarifa kuhusu hashing, uundaji wa nambari nasibu, na miundo mbinu ya kriptografia ambayo hulinda data katika usafiri na wakati wa kupumzika.