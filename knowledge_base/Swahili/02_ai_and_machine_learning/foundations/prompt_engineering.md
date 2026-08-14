<!--
---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prompt, engineering, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Uhandisi wa haraka
Uhandisi wa haraka ni mazoezi ya kubuni, kuboresha, na kuboresha vidokezo vya ingizo ili kupata matokeo bora zaidi kutoka kwa muundo wa lugha. Ni sanaa na sayansi, na ni kiolesura cha msingi cha kudhibiti tabia ya LLM bila kusawazisha.
---

## Kanuni za Msingi
### Uwazi na Umaalumu
Kidokezo cha wazi hakiachi nafasi ya utata. Bainisha unachotaka hasa, ikijumuisha umbizo, urefu na mtazamo.
**Wazi:**
> "Niambie kuhusu Python."
**Maalum:**
> "Eleza Kufuli la Wakalimani Ulimwenguni la Python (GIL). Eleza athari yake katika usomaji wa maandishi mengi, toa suluhisho moja, na uweke jibu lako chini ya maneno 200."
### Toa Muktadha
Wanamitindo hufanya vyema zaidi wanapojua jukumu, hadhira na lengo.
**Bila muktadha:**
> "Andika chaguo la kukokotoa ili kupanga orodha."
**Pamoja na muktadha:**
> "Wewe ni msanidi mkuu wa Python. Andika chaguo la kukokotoa ili kupanga orodha ya kamusi kwa ufunguo uliyopewa. Tumia vidokezo vya aina na ushughulikie matukio makali. Hadhira ni wasanidi wachanga."
### Tumia Maagizo Chanya
Mwambie mfano nini cha kufanya, sio kile cha kuepuka. "Usijumuishe jargon" ni dhaifu kuliko "Tumia lugha rahisi inayopatikana kwa mtoto wa miaka 10."
---

## Miundo ya Haraka
### Majukumu ya Mfumo / Mtumiaji / Mratibu
API nyingi za LLM zinaunga mkono muundo wa zamu nyingi:
- **Ujumbe wa mfumo**: Huweka tabia, mtu, na vikwazo vya kielelezo (hudumu kwa kipindi kizima).
- **Ujumbe wa mtumiaji**: Hoja au maagizo ya sasa.
- **Ujumbe wa Mratibu**: Majibu ya awali ya modeli (yametumika kwa mwendelezo).
**Mfano (mtindo wa API ya OpenAI):**
Mfumo: Wewe ni msaidizi muhimu wa usimbaji. Unajibu kwa mifano fupi ya msimbo na maelezo mafupi. Usiwahi kutoa msimbo usio salama.
Mtumiaji: Andika kazi ya Python kupakua faili kutoka kwa URL.
### Uhamasishaji wa Risasi Chache
Toa mifano 2-3 ya umbizo la pato la ingizo kabla ya kuuliza kielelezo kutekeleza kazi. Hii inafundisha muundo.
**Mfano:**
Mtumiaji: Badilisha sentensi hizi ziwe sauti tulivu:
Ingizo: Paka alifukuza panya.
Pato: Panya alifukuzwa na paka.
Ingizo: Mpishi alipika chakula.
Pato: Chakula kilipikwa na mpishi.
Ingizo: Dhoruba iliharibu nyumba.
Pato: (mfano umekamilika)
### Mlolongo-wa-Mawazo (CoT)
Himiza modeli kuonyesha hoja zake hatua kwa hatua. Hii inaboresha usahihi wa kazi za hesabu, mantiki na hatua nyingi.
**Bila CoT:**
> "24 × 37 ni nini?"
**Na CoT:**
> "Hesabu 24 × 37. Onyesha hoja zako hatua kwa hatua."
Mfano huo utazalisha hatua za kati, kupunguza makosa ya hesabu.
### Matokeo Yanayoundwa
Omba umbizo mahususi kama vile JSON, YAML, au jedwali za alama ili kufanya uchanganuzi uwe wa kuaminika.
Mtumiaji: Orodhesha faida tatu na hasara tatu za huduma ndogo. Rudisha tu kitu halali cha JSON chenye funguo "faida" na "hasara", kila safu ya mifuatano.
---

## Mbinu za Kina
### Kujisimamia
Toa majibu mengi kwa dodoso sawa (kwa halijoto> 0) na upige kura nyingi kwenye jibu la mwisho. Hii inafaa hasa kwa kazi za hoja.
### Mti-wa-Mawazo
Chunguza njia nyingi za hoja kwa sambamba, tathmini kila moja na uchague iliyo bora zaidi. Hii ni mbinu ya kiwango cha utafiti lakini inaweza kukadiria kwa kuuliza modeli "kugundua suluhu mbadala."
### Tekeleza (Kutoa Sababu + Kutenda)
Acha kielelezo kiingilie hoja na simu za zana. Inaweza kufikiri, kisha kuchukua hatua (kwa mfano, kutafuta mtandao, kukimbia msimbo), kisha kufikiri tena kulingana na matokeo.
** Muundo wa haraka:**
Unaweza kufikia kikokotoo na injini ya utafutaji. Kwa kila hatua, pato:
Mawazo: (mawazo yako)
Kitendo: (jina la zana, ingizo)
Uchunguzi: (toleo la zana)
... endelea hadi upate jibu la mwisho.
### Mgawo wa Mtu
Mpe mtu mahususi ili kutunga majibu.
**Mifano:**
- "Wewe ni msanidi wa Linux kernel anayeelezea usimamizi wa kumbukumbu kwa mhitimu mpya."
- "Wewe ni mtaalamu wa lishe anayetoa ushauri wa jumla kwa mteja."
- "Wewe ni mkosoaji mbishi wa kiteknolojia anayepitia kifaa kipya."
---

## Urekebishaji wa Vigezo
- **Joto** (0.0 - 1.0+): Hudhibiti nasibu. Chini = kinachoamua zaidi, cha juu = ubunifu zaidi. Tumia 0.0–0.3 kwa majibu ya kweli; 0.7–1.0 kwa uandishi wa ubunifu.
- **Juu-p** (sampuli ya kiini): Hupunguza uzito wa uwezekano katika kizingiti fulani limbikizi. 0.9 inamaanisha sampuli za mifano kutoka kwa 90% ya juu ya uwezekano wa tokeni. Kawaida rekebisha halijoto au top-p, sio zote mbili.
- **Tokeni za juu zaidi**: Huweka urefu wa juu zaidi wa kutoa. Kumbuka kuweka nafasi ya jibu ndani ya dirisha la muktadha.
- **Adhabu ya mara kwa mara**: Hupunguza marudio ya tokeni sawa.
- **Adhabu ya uwepo**: Huhimiza modeli kutambulisha mada mpya.
---

## Mitego na Marekebisho ya Kawaida
| Tatizo | Labda sababu | Rekebisha |
|---------|--------------|-----|
| Mfano hupuuza sehemu za haraka | Kidokezo kirefu sana au kimepakiwa | Fupisha; weka maagizo muhimu zaidi mwishoni |
| Pato ni kitenzi sana | Hakuna kikwazo cha urefu | Ongeza "Punguza hadi sentensi 3" au weka max_tokens |
| Pato ni fupi mno | Vizuizi kupita kiasi | Ongeza "Eleza kwa undani" au halijoto ya chini |
| Maoni ya kweli | Muktadha usiotosha au swali lisilo na utata | Ongeza "Ikiwa huna uhakika, sema 'sijui'" na utoe muktadha wa RAG |
| Uumbizaji usiolingana | Hakuna maagizo ya umbizo dhahiri | Uliza JSON, jedwali la alama, au orodha ya vitone |
| Majibu ya mfano katika lugha isiyo sahihi | Hakuna maagizo ya lugha | Taja kwa uwazi "Jibu kwa Kiingereza" (au lugha yako lengwa) |
---

## Violezo vya Upesi kwa Majukumu ya Kawaida
### Muhtasari
Fupisha maandishi yafuatayo katika nukta 3 za vitone. Zingatia hoja kuu na uepuke maelezo.
Maandishi: [ingiza maandishi]

### Uzalishaji wa Msimbo
Andika kitendakazi cha [lugha] ambacho [hufanya X].
Mahitaji:
Tumia vidokezo vya aina.
Jumuisha kamba ya hati.
Shughulikia kesi za makali: [orodha].
Usitumie maktaba za nje isipokuwa kama imebainishwa.

### Maelezo
Eleza [dhana] kwa [mwanafunzi asiye mtaalam / wa chuo kikuu / mtoto]. Tumia mlinganisho inapofaa.
### Mawazo
Tengeneza mawazo 10 ya [mada]. Kwa kila wazo, toa maelezo ya sentensi moja na changamoto moja inayowezekana.
maandishi
### Uainishaji
Bainisha maoni ya mteja yafuatayo kama [chanya, upande wowote, hasi].
Toa alama ya kujiamini (0-100) na sababu fupi.
Maoni: [weka maandishi]
### Tafsiri kwa Mtindo
Tafsiri maandishi yafuatayo ya Kiingereza hadi Kihispania. Tumia sauti isiyo rasmi inayofaa kwa chapisho la media ya kijamii.
Maandishi: [ingiza maandishi]
---

## Tathmini ya Vidokezo
Tumia vidokezo kama msimbo: toleo lao, lijaribu, na urudie tena.
- **Jaribio la A/B** anuwai tofauti za papo hapo kwenye seti ya hoja zilizozuiliwa.
- **Pima mafanikio** kupitia tathmini ya kibinadamu au vipimo vya kiotomatiki (k.m., mechi kamili, BLEU, alama maalum).
- **Weka sajili ya papo hapo** (faili rahisi ya maandishi au lahajedwali) na kidokezo, toleo na utendakazi uliozingatiwa.
---