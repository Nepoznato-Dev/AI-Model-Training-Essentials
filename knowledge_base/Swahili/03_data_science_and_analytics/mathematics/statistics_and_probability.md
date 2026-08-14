<!--
---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Takwimu na Uwezekano
Uwezekano na takwimu ni misingi ya hisabati ya sayansi ya data, kujifunza kwa mashine na utafiti wa kisayansi. Uwezekano hukuambia jinsi uwezekano wa matukio; takwimu inakuambia jinsi ya kupata hitimisho kutoka kwa data. Kwa pamoja, wanageuza kutokuwa na uhakika kuwa maarifa yanayoweza kupimika, yanayoweza kudhibitiwa.
---

## Nadharia ya Uwezekano
### Dhana za Msingi
| Dhana | Maelezo | Mfano |
|---------|-------------|---------|
| **Nafasi ya Mfano** | Seti ya matokeo yote yanayowezekana | Kukunja sura: {1, 2, 3, 4, 5, 6} |
| **Tukio** | Sehemu ndogo ya nafasi ya sampuli | Nambari iliyosawazishwa: {2, 4, 6} |
| **Uwezekano** | Nambari kati ya 0 na 1 uwezekano wa kupima | P(kukunja 6) = 1/6 |
| **Uwezekano wa Masharti** | P(A|B): uwezekano wa A iliyotolewa umetokea | P(mvua | mawingu) |
| **Uhuru** | Matukio ambapo moja haliathiri nyingine | Vipindi vya sarafu vinajitegemea |
### Kanuni za Uwezekano
| Kanuni | Mfumo | Tumia Kesi |
|------|---------------------|
| **Kanuni ya Nyongeza** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Uwezekano wa A au B |
| **Kanuni ya Kuzidisha** | P(A ∩ B) = P(A) × P(B|A) | Uwezekano wa A na B |
| **Kanuni inayokamilisha** | P(si A) = 1 − P(A) | Uwezekano wa tukio kutotokea |
| **Sheria ya Uwezekano wa Jumla** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Kugawanya kwa matukio ya kipekee |
| **Nadharia ya Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Kusasisha imani kwa ushahidi |
### Usambazaji Uwezekano
| Usambazaji | Aina | Vigezo Muhimu | Tumia Kesi |
|--------------------|---------------------------|
| **Kawaida (Gaussian)** | Kuendelea | Maana (μ), Mkengeuko wa kawaida (σ) | Matukio ya asili, makosa ya kipimo |
| **Binomial** | Tofauti | n (majaribio), p (uwezekano) | Hesabu za kufaulu/kufeli |
| **Poisson** | Tofauti | λ (kiwango) | Matukio adimu kwa muda/nafasi |
| **Kielelezo** | Kuendelea | λ (kiwango) | Muda kati ya matukio |
| **Sare** | Mbili | a, b (mipaka) | Matokeo yanayowezekana sawa |
| **Chi-Square** | Kuendelea | k (digrii za uhuru) | Vipimo vya wema |
| **t-Usambazaji** | Kuendelea | ν (digrii za uhuru) | Mfano mdogo wa makisio |
### Sifa Muhimu za Usambazaji
| Mali | Maelezo |
|----------|-------------|
| **Maana (Thamani Inayotarajiwa)** | Katikati ya wingi wa usambazaji: E[X] = Σ xᵢ × P(xᵢ) |
| **Tofauti** | Sambaza wastani: Var(X) = E[(X − μ)²] |
| **Mkengeuko wa Kawaida** | Mzizi wa mraba wa kutofautiana; vitengo sawa na data |
| **Upotovu** | Asymmetry ya usambazaji |
| **Kurtosis** | "Tailedness" - jinsi mikia ni nzito |
---

## Maelekezo ya Takwimu
### Maelezo dhidi ya Takwimu Inferential
| | Maelezo | Inferential |
|---|---------------------------|
| **Kusudi** | Fupisha na ueleze data | Hitimisho kuhusu idadi ya watu kutoka kwa sampuli |
| **Zana** | Wastani, wastani, modi, mkengeuko wa kawaida, chati | Vipimo vya nadharia, vipindi vya kujiamini, rejeshi |
| **Upeo** | Data uliyo nayo pekee | Kujumlisha zaidi ya sampuli yako |
### Mfumo wa Majaribio ya Dhahania
| Hatua | Maelezo |
|------|-------------|
| 1. **Nadharia za serikali** | Dhana potofu (H₀): hakuna athari; Mbadala (H₁): athari ipo |
| 2. **Chagua kiwango cha umuhimu** | α = 0.05 (ya kawaida) |
| 3. **Chagua jaribio** | Kulingana na aina ya data, saizi ya sampuli, na mawazo |
| 4. **Kokotoa takwimu za majaribio** | Inategemea mtihani uliochaguliwa |
| 5. **Tafuta p-thamani** | Uwezekano wa kutazama data ikiwa H₀ ni kweli |
| 6. **Fanya uamuzi** | Ikiwa p <α, kataa H₀; vinginevyo, shindwa kukataa H₀ |
### Majaribio ya Kawaida ya Takwimu
| Mtihani | Wakati wa Kutumia | Nini Inalinganisha |
|------|-------------|-----------------|
| **mtihani wa t** | Linganisha njia za vikundi 1-2 | Kikundi maana/vikundi kwa thamani au kwa kila kimoja |
| **Jaribio la Chi-mraba** | Data ya kitengo | Imezingatiwa dhidi ya masafa yanayotarajiwa |
| **ANOVA** | Linganisha njia za vikundi 3+ ​​| Tofauti kati ya kikundi dhidi ya ndani ya kikundi |
| **Mann-Whitney U** | Njia mbadala isiyo ya kigezo kwa t-test | Mgawanyo wa safu ya vikundi viwili |
| **Uwiano wa Pearson** | Uhusiano wa mstari kati ya vigezo viwili vinavyoendelea | r thamani kutoka −1 hadi +1 |
| **Uwiano wa Spearman** | Uhusiano wa Monotonic (msingi wa cheo) | ρ thamani ya data ya kawaida au isiyo ya kawaida |
### Vipindi vya Kujiamini
Muda wa kujiamini hutoa anuwai ya maadili yanayokubalika kwa kigezo cha idadi ya watu:
- **95% CI kwa maana** (inayojulikana σ): x̄ ± 1.96 × (σ / √n)
- **Ufafanuzi**: "Tuna uhakika 95% kuwa idadi ya kweli ina maana iko ndani ya muda huu"
- **CI pana** = kutokuwa na uhakika zaidi (sampuli ndogo, tofauti kubwa, au kiwango cha juu cha kujiamini)
---

## Uchambuzi wa Kurudi nyuma
### Aina za Kurudi nyuma
| Aina | Kigezo Tegemezi | Tumia Kesi |
|------|-------------------------------|
| **Rejeshi la Mstari** | Kuendelea | Kutabiri bei za nyumba, mauzo |
| **Urejeshaji wa Vifaa** | Nambari (0/1) | Uainishaji: kugundua barua taka, utambuzi wa ugonjwa |
| **Rejea la Polynomia** | Inayoendelea (iliyopinda) | Mikondo ya ukuaji, mitindo isiyo ya mstari |
| **Marudio Mengi** | Endelevu (Watabiri 2+) | Kudhibiti kwa wachanganyaji |
| **Ridge / Lasso** | Inayoendelea (iliyoratibiwa) | Kuzuia kuzidisha, uteuzi wa vipengele |
### Misingi ya Urejeshaji Mstari
Muundo: **y = β₀ + β₁x + ε**
| Sehemu | Maana |
|-----------|---------|
| β₀ (kukatiza) | Thamani ya y wakati x = 0 |
| β₁ (mteremko) | Badilisha katika y kwa mabadiliko ya kitengo kimoja katika x |
| ε (neno la makosa) | Tofauti isiyoelezeka |
**Vipimo muhimu:**
- **R² (mgawo wa uamuzi)**: Sehemu ya tofauti iliyofafanuliwa na muundo (0 hadi 1)
- **R²** Iliyorekebishwa: R² imeadhibiwa kwa idadi ya watabiri
- **RMSE**: Mizizi inamaanisha kosa lenye umbo la mraba - hitilafu ya wastani ya ubashiri katika vitengo sawa na y
### Mawazo ya Urejeshaji wa Mstari
| Dhana | Nini Maana Yake | Jinsi ya Kuangalia |
|-----------|-----------------------------|
| **Mstari** | Uhusiano kati ya X na Y ni mstari | Kutawanya viwanja |
| **Uhuru** | Uchunguzi ni huru | Ubunifu wa masomo |
| **Homoscedasticity** | Tofauti za mara kwa mara za mabaki | Viwanja vya mabaki |
| **Kawaida** | Mabaki husambazwa kwa kawaida | Njama ya Q-Q, mtihani wa Shapiro-Wilk |
| **Hakuna multicollinearity** | Watabiri hawahusiani sana | VIF (Kipengele cha Tofauti cha Mfumuko wa Bei) |
---

## Takwimu za Bayesian
### Mtaalamu wa mara kwa mara dhidi ya Bayesian
| | Mtaalamu wa mara kwa mara | Kibayesi |
|---|-------------|----------|
| **Uwezekano unamaanisha** | Masafa ya muda mrefu | Kiwango cha imani |
| **Vigezo ni** | Imewekwa lakini haijulikani | Vigeu vya nasibu vilivyo na usambazaji |
| **Hutumia** | maadili ya p, vipindi vya kujiamini | Usambazaji wa nyuma, vipindi vinavyoaminika |
| **Nguvu** | Lengo, imara | Inajumuisha maarifa ya awali, tafsiri angavu |
### Nadharia ya Bayes katika Mazoezi
** Nyuma = (Uwezekano × Kabla) / Ushahidi**
Mfano - mtihani wa matibabu:
- Kuenea kwa ugonjwa: 1% (kabla)
- Usikivu wa mtihani: 95% (kiwango chanya cha kweli)
- Ubora wa mtihani: 90% (kiwango cha kweli hasi)
- Ukipimwa kuwa chanya: P(ugonjwa | chanya) = (0.95 × 0.01) / (0.95 × 0.01 + 0.10 × 0.99) ≈ 8.8%
Matokeo haya yanayopingana - matokeo chanya zaidi ni chanya za uwongo wakati ugonjwa ni nadra - ni **uongo wa kiwango cha msingi**, na inaonyesha kwa nini mawazo ya Bayesian ni muhimu.
---

## Vidokezo Vitendo
- **Tazama data yako kila mara** kabla ya kufanya jaribio lolote la takwimu
- **Angalia dhana** - ukiukaji unaweza kubatilisha matokeo
- **Ukubwa wa madoido ni muhimu** - matokeo muhimu kitakwimu yanaweza yasiwe na maana yoyote
- **Uhusiano sio sababu** — hata miunganisho mikali inaweza kuwa na utata
- **Ulinganisho mwingi** huongeza viwango vya chanya vya uwongo - tumia masahihisho (Bonferroni, FDR)
- **Ripoti vipindi vya kujiamini**, si tu maadili ya p
---

## Kwa Nini Jambo Hili
Takwimu ni uti wa mgongo wa utafiti wa kisayansi, uchanganuzi wa biashara, na ujifunzaji wa mashine. Bila hivyo, huwezi kutofautisha mawimbi kutoka kwa kelele, kutambua athari halisi kutokana na kushuka kwa thamani kwa nasibu, au kufanya ubashiri kwa kutokuwa na uhakika uliothibitishwa. Iwe unachanganua majaribio ya A/B, unafunza miundo ya ML, au unasoma karatasi za utafiti, ujuzi wa takwimu ni muhimu.