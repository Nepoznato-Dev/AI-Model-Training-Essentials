---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Upimaji wa Kitakwimu na Majaribio
Takwimu ni sarufi ya sayansi. Inakupa zana za kutofautisha ruwaza halisi na kelele nasibu, kupima kama mabadiliko yaliboresha mambo, na kufanya maamuzi chini ya kutokuwa na uhakika. Faili hii inashughulikia dhana za msingi za majaribio ya dhahania, muundo wa majaribio, na mitego ya kawaida ambayo huwavuta watu.
---

## Mfumo wa Majaribio ya Dhahania
Kila jaribio la takwimu hufuata mantiki sawa:
1. **Taja dhana potofu (H₀)**: Hakuna athari / hakuna tofauti.
2. **Taja dhana mbadala (H₁)**: Kuna athari / tofauti.
3. **Chagua kiwango cha umuhimu (α)**: Kawaida 0.05 (5% nafasi ya chanya ya uwongo).
4. **Kusanya data na kukokotoa takwimu za jaribio**.
5. **Kokotoa thamani ya p**: Uwezekano wa kutazama matokeo haya (au uliokithiri zaidi) ikiwa H₀ ni kweli.
6. **Fanya uamuzi**: Ikiwa p <α, kataa H₀ (muhimu kitakwimu). Vinginevyo, shindwa kukataa H₀.
### Dhana Muhimu
| Dhana | Maana | Maoni Mabaya ya Kawaida |
|---------|-------------------------------|
| **p-thamani** | P(data \| H₀ ni kweli) | SI "uwezekano kwamba H₀ ni kweli" |
| **α (kiwango cha umuhimu)** | Kizingiti cha kukataa H₀ | Sio kipimo cha umuhimu wa athari |
| **Umuhimu wa takwimu** | Matokeo hayawezekani kwa sababu ya bahati nasibu pekee | Haimaanishi muhimu kivitendo |
| **Ukubwa wa athari** | Ukubwa wa athari iliyozingatiwa | Tenganisha na thamani ya p; athari ndogo inaweza kuwa muhimu kwa N kubwa |
| **Nguvu** | Uwezekano wa kukataa kwa usahihi H₀ | ya uwongo Kwa kawaida hulenga 80%+ |
| **Kipindi cha kujiamini** | Msururu wa thamani zinazokubalika kwa kigezo | 95% CI haimaanishi "uwezekano 95% wa thamani halisi iko katika safu hii" |
---

## Aina za Makosa
| | H₀ ni Kweli | H₀ ni Uongo |
|---|------------------------|
| **Kataa H₀** | Hitilafu ya Aina ya I (chanya ya uwongo) | ✅ Sahihi (chanya halisi) |
| **Imeshindwa kukataa H₀** | ✅ Sahihi (hasi hasi) | Hitilafu ya Aina ya II (hasi ya uwongo) |
| Hitilafu | Alama | Maana |
|-------|-------------------|
| **Aina ya I** | α | Kuhitimisha kuwa kuna athari wakati hakuna |
| **Aina ya II** | β | Inakosa athari halisi |
---

## Kuchagua Mtihani Sahihi
| Hali | Mtihani | Mawazo |
|----------|------|-------------|
| Linganisha njia za vikundi 2 | **t-test** (huru) | Usambazaji wa kawaida, tofauti sawa |
| Linganisha njia za uchunguzi uliooanishwa | **Jaribio la t lililooanishwa** | Tofauti husambazwa kwa kawaida |
| Linganisha njia za vikundi 3+ ​​| **ANOVA** | Usambazaji wa kawaida, tofauti sawa |
| Linganisha usambazaji wa kategoria | **Jaribio la Chi-mraba** | Sampuli ya ukubwa wa kutosha kwa kila seli |
| Linganisha usambazaji (usio wa kigezo) | **Mann-Whitney U** | Hakuna dhana ya kawaida |
| Linganisha vikundi 3+ ​​(zisizo za kigezo) | **Kruskal-Wallis** | Hakuna dhana ya kawaida |
| Uwiano wa mtihani | **Pearson** (linear) au **Spearman** (monotonic) | Pearson: kawaida; Spearman: kulingana na cheo |
| Jaribu ikiwa data inafuata usambazaji | **Kolmogorov-Smirnov** | Data inayoendelea |
### Parametric vs Non-Parametric
| | Parametric | Isiyo ya Kigezo |
|---|---------------------------|
| **Mawazo** | Data hufuata usambazaji maalum (kawaida kawaida) | Hakuna dhana ya usambazaji |
| **Nguvu** | Juu zaidi wakati mawazo yalipokutana | Chini, lakini imara zaidi |
| **Wakati wa kutumia** | Sampuli kubwa, takriban data ya kawaida | Sampuli ndogo, data iliyopotoshwa, data ya kawaida |
---

## Majaribio Maalum kwa Kina
### T-Jaribio
Inalinganisha njia za vikundi viwili.
| Lahaja | Tumia Kesi |
|---------|----------|
| **Jaribio la t la kujitegemea** | Vikundi viwili tofauti (matibabu dhidi ya udhibiti) |
| **Jaribio la t lililooanishwa** | Kikundi kimoja kilipimwa mara mbili (kabla dhidi ya baada) |
| **Mtihani wa t wa mfano mmoja** | Linganisha wastani wa sampuli na thamani inayojulikana |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Uchambuzi wa Tofauti)
Kulinganisha kunamaanisha katika vikundi 3 au zaidi. Vipimo kama angalau kikundi kimoja kinatofautiana na vingine.
| Aina | Ubunifu |
|------|--------|
| **ANOVA ya njia moja** | Tofauti moja huru yenye viwango 3+ |
| **Njia mbili ANOVA** | Vigezo viwili vya kujitegemea; hujaribu athari za mwingiliano |
| **Hatua Zinazorudiwa ANOVA** | Masomo sawa kupimwa chini ya hali tofauti |
Ikiwa ANOVA ni muhimu, fuatilia na **majaribio ya baada ya hoc** (Tukey's HSD) ili kupata vikundi mahususi vinavyotofautiana.
### Jaribio la Chi-Square
Hujaribu kama viwezo viwili vya kategoria vinajitegemea.
| Tumia Kesi | Mfano |
|----------|---------|
| **Mtihani wa uhuru** | Je, jinsia inahusishwa na upendeleo wa bidhaa? |
| **Uzuri wa kufaa** | Je, safu ya kufa inafuata usambazaji sawa? |
**Kanuni ya kidole gumba**: kila seli inapaswa kuwa na hesabu inayotarajiwa ya angalau 5.
---

## Jaribio la A/B
Jaribio la A/B ni matumizi ya majaribio ya dhahania kwa maamuzi ya biashara - kwa kawaida kulinganisha kidhibiti (A) na kibadala (B).
### Mchakato wa Usanifu
| Hatua | Maelezo |
|------|-------------|
| **1. Bainisha dhana** | "Kubadilisha rangi ya kitufe kutoka bluu hadi kijani kutaongeza kiwango cha kubofya" |
| **2. Chagua kipimo** | Msingi: kiwango cha kubofya. Sekondari: kiwango cha ubadilishaji, mapato. |
| **3. Hesabu saizi ya sampuli** | Kulingana na madoido ya chini zaidi inayoweza kutambulika, nguvu (80%), na umuhimu (5%) |
| **4. Nasibu** | Wape watumiaji udhibiti na matibabu bila mpangilio |
| **5. Endesha jaribio** | Kusanya data hadi ukubwa wa sampuli lengwa ufikiwe |
| **6. Uchambuzi** | Linganisha vipimo kwa kutumia mtihani unaofaa wa takwimu |
| **7. Amua** | Tekeleza ikiwa ni muhimu kitakwimu na kivitendo |
### Sampuli ya Kukokotoa Ukubwa
Saizi ya sampuli unayohitaji inategemea:
| Sababu | Athari kwa Saizi ya Sampuli |
|--------|----------------------|
| **Athari ndogo ya kugundua** | Unahitaji sampuli zaidi |
| **Nguvu ya juu** | Unahitaji sampuli zaidi |
| **Kiwango cha chini cha umuhimu** | Unahitaji sampuli zaidi |
| **Tofauti ya juu zaidi** | Unahitaji sampuli zaidi |
### Makosa ya Kawaida ya Upimaji wa A/B
| Kosa | Kwanini Ni Makosa |
|---------|---------------|
| **Kuchungulia mapema** | Kukagua matokeo kila siku huongeza kiwango chanya cha uwongo |
| **Vipimo vingi bila marekebisho** | Kujaribu vipimo 20 kwa α=0.05 → tarajia 1 chanya kwa bahati nasibu |
| **Kusimama kabla ya lengo N** | Jaribio lisilo na nguvu nyingi haliwezi kugundua athari halisi |
| **Kupuuza msimu** | Kufanya mtihani katika kipindi cha likizo dhidi ya wiki ya kawaida |
| **Kazi isiyo ya nasibu** | Upendeleo wa uteuzi (k.m., kuwapa watumiaji wapya matibabu) |
| **Umuhimu unaochanganya na umuhimu** | Lifti ya 0.1% inaweza kuwa muhimu kitakwimu lakini haifai kusafirishwa |
---

## Ulinganisho Nyingi
Unapofanya majaribio mengi kwa wakati mmoja, nafasi ya angalau moja ya matokeo chanya huongezeka sana.
| Idadi ya Majaribio | Uwezekano wa ≥1 Uongo Chanya (katika α=0.05) |
|------------------------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Marekebisho
| Mbinu | Jinsi Inavyofanya Kazi | Wakati wa Kutumia |
|--------|-------------|-------------|
| **Bonferroni** | Gawanya α kwa idadi ya majaribio (α/n) | Mhafidhina; kulinganisha chache |
| **Holm-Bonferroni** | Utaratibu wa kushuka chini; chini ya kihafidhina | Matumizi ya jumla |
| **Benjamini-Hochberg (FDR)** | Hudhibiti kiwango cha ugunduzi wa uwongo | Vipimo vingi; uchambuzi wa uchunguzi |
---

## Ukubwa wa Athari
Thamani za P hukuambia *kama* athari ipo. Ukubwa wa madoido hukuambia *ukubwa* ni nini.
| Pima | Kwa | Tafsiri |
|---------|-----|---------------|
| **Cohen's d** | Tofauti kati ya njia mbili | 0.2 = ndogo, 0.5 = kati, 0.8 = kubwa |
| **R** ya Pearson | Uhusiano | 0.1 = ndogo, 0.3 = wastani, 0.5 = kubwa |
| **η² (eta-mraba)** | ANOVA | 0.01 = ndogo, 0.06 = kati, 0.14 = kubwa |
| **Uwiano wa Odds** | Matokeo ya kategoria | 1.0 = hakuna athari; >1 au <1 = athari |
**Ripoti ukubwa wa athari kila wakati pamoja na thamani za p.** Matokeo yanaweza kuwa muhimu kitakwimu lakini yasiyo na maana yoyote.
---

## Bayesian dhidi ya Frequentist
| Kipengele | Mtaalamu wa mara kwa mara | Kibayesi |
|--------|------------|-----------|
| **Uwezekano** | Masafa ya matukio ya muda mrefu | Kiwango cha imani |
| **Vigezo** | Imewekwa lakini haijulikani | Vigeu vya nasibu vilivyo na usambazaji |
| **Hutumia** | maadili ya p, vipindi vya kujiamini, vipimo vya nadharia | Usambazaji wa nyuma, vipindi vinavyoaminika |
| **Kabla** | Hakuna imani za awali zilizojumuishwa | Usambazaji dhahiri wa hapo awali |
| **Tafsiri** | "Ikiwa tulirudia jaribio hili mara nyingi ..." | "Kwa kuzingatia data, uwezekano kwamba ..." |
| **Nguvu** | Lengo, imara, rahisi | Ufafanuzi wa angavu, hujumuisha maarifa ya awali |
| **Udhaifu** | p-maadili hayajaeleweka sana | Chaguo la hapo awali linaweza kuwa la kibinafsi |
---

## Misingi ya Maelekezo ya Sababu
Uwiano sio sababu. Lakini wakati mwingine unahitaji kujua *kama X ilisababisha Y*, si tu kama wanahusishwa.
| Mbinu | Maelezo | Wakati wa Kutumia |
|--------|-------------|-------------|
| **Majaribio ya nasibu** | Kiwango cha dhahabu; mgawo wa nasibu huondoa utatanishi | Wakati unaweza kubahatisha |
| **Tofauti-katika-Tofauti (DiD)** | Linganisha mabadiliko ya muda kati ya matibabu na udhibiti | Mabadiliko ya sera, majaribio ya asili |
| **Kuacha Kurudi nyuma (RDD)** | Tumia kizingiti cha kukata | Masomo, viwango vya kustahiki |
| **Vigezo vya Ala (IV)** | Tumia kifaa kinachoathiri matibabu lakini sio matokeo moja kwa moja | Wakati kubahatisha haiwezekani |
| **Ulinganifu wa Alama za Mwelekeo** | Linganisha vitengo vilivyotibiwa na kudhibiti kwenye sifa zinazozingatiwa | Masomo ya uchunguzi |
---

## Makosa ya Kawaida ya Kitakwimu
| Kosa | Maelezo |
|---------|-------------|
| **p-hacking** | Kujaribu michanganuo mingi hadi upate p <0.05 |
| **KUHAKIKI** | Hypothesising Baada ya Matokeo Inajulikana |
| **Upendeleo wa kunusurika** | Kuangalia tu mafanikio (k.m., kampuni zilizofanikiwa) |
| **Kitendawili cha Simpson** | Mwenendo hubadilika data inapojumlishwa dhidi ya kugawanywa kwa kikundi |
| **Kupuuzwa kwa kiwango cha msingi** | Kupuuza uwezekano wa awali wakati wa kutafsiri matokeo |
| **Uongo wa kiikolojia** | Kuingiza tabia ya mtu binafsi kutoka kwa data ya kiwango cha kikundi |
| **Inachanganya** | Kigezo cha tatu kinaelezea uhusiano unaozingatiwa |
| **Kufaa kupita kiasi** | Mfano unanasa kelele, sio ishara |
---

## Muhtasari
Upimaji wa takwimu ni juu ya kufanya maamuzi chini ya kutokuwa na uhakika na uaminifu wa kiakili. Daima sema dhana zako kabla ya kukusanya data. Chagua jaribio linalofaa kwa aina yako ya data. Ripoti ukubwa wa athari, sio tu maadili ya p. Sahihi kwa kulinganisha nyingi. Na kumbuka: umuhimu wa takwimu sio sawa na umuhimu wa vitendo.