---
# Metadata
title: "Testing Methodologies"
description: "Unit, integration, E2E, TDD, BDD, test pyramids"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [testing, methodologies, coding-and-technology]
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

# Mbinu za Upimaji
Kujaribu ni jinsi unavyopata imani kuwa msimbo wako hufanya kazi - na muhimu zaidi, mabadiliko yake hayavunji kile ambacho tayari kinafanya kazi. Upimaji mzuri hupata hitilafu kabla ya watumiaji kufanya, hati za tabia inayotarajiwa, na huwezesha urekebishaji bila woga. Faili hii inajumuisha wigo kamili wa mikakati ya majaribio, kutoka kwa majaribio ya vitengo hadi majaribio ya mwisho hadi mwisho, na kanuni zinazofanya majaribio kuwa na ufanisi.
---

## Piramidi ya Kujaribu
Piramidi ya majaribio inaelezea usambazaji bora wa majaribio katika mradi.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Kiwango | Hesabu | Kasi | Gharama | Inajaribu Nini |
|-------|-------|-------|------|---------------|
| **Kitengo** | Nyingi | Haraka (ms) | Chini | Kazi za kibinafsi, madarasa, mbinu |
| **Muunganisho** | Baadhi | Wastani (100ms-s) | Kati | Jinsi vipengele vinavyoingiliana; maswali ya hifadhidata; Simu za API |
| **E2E** | Chache | Polepole (sekunde-dakika) | Juu | Mtumiaji kamili hutiririka kupitia mfumo halisi |
---

## Upimaji wa Kitengo
Kujaribu vitengo vya kibinafsi vya msimbo kwa kutengwa.
### Kanuni
| Kanuni | Maelezo |
|-----------|-------------|
| **Haraka** | Kila jaribio linapaswa kufanywa kwa milisekunde |
| **Kutengwa** | Vipimo havitegemei kila mmoja; hakuna hali iliyoshirikiwa |
| **Kuamua** | Ingizo sawa → pato sawa kila wakati (hakuna nasibu, hakuna utegemezi wa wakati) |
| **Kujiangalia** | Mtihani hupita au kutofaulu kiotomatiki; hakuna ukaguzi wa mikono |
| **Kwa wakati** | Imeandikwa kando au kabla ya msimbo (TDD) |
### Anatomy ya Mtihani
| Awamu | Maelezo |
|-------|-------------|
| **Panga** | Sanidi data ya jaribio na vitegemezi |
| **Kitendo** | Piga simu kitendakazi au mbinu inayojaribiwa |
| **Dalili** | Thibitisha matokeo yanalingana na matarajio |
### Nini cha Kujaribu
| Kitengo | Mifano |
|----------|---------|
| **Njia ya furaha** | Ingizo za kawaida hutoa matokeo yanayotarajiwa |
| **Kesi za makali** | Ingizo tupu, null, sufuri, viwango vya juu zaidi, kipengele kimoja |
| **Kesi za hitilafu** | Ingizo batili, data inayokosekana, ruhusa imekataliwa |
| **Masharti ya mipaka** | Mbali na moja; haswa katika mipaka |
### Kudhihaki na Kuchokoza
| Muda | Maelezo | Wakati wa Kutumia |
|------|-------------|-------------|
| **Mzaha** | Kitu ghushi kinachorekodi jinsi kilivyoitwa | Kuthibitisha mwingiliano (njia hii iliitwa?) |
| **Nyumba** | Kitu ghushi ambacho hurejesha thamani zilizoamuliwa mapema | Kutoa data ya majaribio (mrudishe mtumiaji huyu kutoka kwa hifadhidata) |
| **Jasusi** | Kanga ambayo inarekodi wito kwa kitu halisi | Uthibitishaji wa sehemu |
| **Bandia** | Utekelezaji uliorahisishwa lakini unaofanya kazi | Hifadhidata ya kumbukumbu ya majaribio |
| Maktaba ya Mzaha | Lugha |
|-------------------------|
| **unittest.kejeli** | Chatu |
| **Mcheshi** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Moq** | C# |
| **shuhudia / dharau** | Nenda |
---

## Jaribio la Ujumuishaji
Kujaribu jinsi vipengele vingi hufanya kazi pamoja.
| Nini cha Kujaribu | Mfano |
|-----------------------|
| **Maswali ya hifadhidata** | Je, ORM hutoa SQL sahihi? Je! faharisi zinatumika? |
| **Nyisho za API** | Je, mzunguko kamili wa majibu ya ombi hufanya kazi? |
| **Muingiliano wa huduma** | Je, huduma A inaita huduma B kwa usahihi? |
| **Vitegemezi vya nje** | Je, ujumuishaji wa lango la malipo hufanya kazi? |
### Mikakati
| Mkakati | Maelezo | Biashara |
|----------|-------------------------|
| **Mategemeo ya kweli** | Tumia hifadhidata halisi, foleni ya ujumbe halisi | Kweli zaidi; polepole; ngumu zaidi kusanidi |
| **Vyombo vya majaribio** | Zungusha vyombo vya Docker kwa kila jaribio linaloendeshwa | Usawa mzuri; inayoweza kuzaliana |
| **Mbadala za kumbukumbu** | H2 badala ya PostgreSQL; basi la ujumbe wa kumbukumbu | Haraka; huenda ukakosa masuala ya ulimwengu halisi |
| **Upimaji wa mkataba** | Thibitisha kuwa huduma zinaheshimu mikataba yao ya API | Inakamata mabadiliko ya kiolesura |
---

## Jaribio la Mwisho-hadi-Mwisho (E2E).
Kujaribu mfumo kamili kutoka kwa mtazamo wa mtumiaji.
| Zana | Aina | Bora Kwa |
|------|------|----------|
| **Mwandishi wa kucheza** | Otomatiki ya kivinjari | Maombi ya wavuti; kivinjari |
| **Mbao** | Otomatiki ya kivinjari | Maombi ya wavuti; uzoefu wa msanidi |
| **Seleniamu** | Otomatiki ya kivinjari | Urithi; msaada wa lugha pana |
| **Detox** | Simu ya E2E | React Apps Asilia |
| **Appium** | Simu ya E2E | Programu asilia na mseto za simu za mkononi |
| **Maestro** | Simu ya E2E | Programu za rununu; syntax rahisi ya YAML |
| **k6 / Nzige** | Jaribio la mzigo | Utendaji chini ya mzigo |
### E2E Mbinu Bora
| Mazoezi | Kwa nini |
|----------|-----|
| **Jaribio la njia muhimu pekee** | Vipimo vya E2E ni polepole; kuzingatia yale muhimu zaidi |
| **Tumia viwanda vya majaribio ya data** | Unda data ya jaribio kwa utaratibu; usitegemee data ya mbegu |
| **Safisha baada ya vipimo** | Kila jaribio linapaswa kuacha mfumo katika hali inayojulikana |
| **Epuka kujaribu maelezo ya UI** | Jaribu tabia, si madarasa ya CSS au nafasi za vipengele |
| **Endesha katika CI** | Majaribio ya E2E lazima yaendeshwe kiotomatiki kwa kila mabadiliko |
---

## Maendeleo Yanayoendeshwa na Mtihani (TDD)
Andika jaribio kwanza, kisha uandike msimbo ili ufaulu.
| Hatua | Maelezo |
|------|-------------|
| **1. Nyekundu** | Andika jaribio lisilofaulu linaloelezea tabia unayotaka |
| **2. Kijani** | Andika nambari ya chini zaidi ya kuthibitisha ili kufanya mtihani kupita |
| **3. Kirekebishaji** | Safisha msimbo huku ukiweka majaribio ya kijani kibichi |
| Faida | Maelezo |
|---------|-------------|
| **Maoni ya muundo** | Majaribio yanakulazimisha kufikiria juu ya miingiliano kabla ya kutekelezwa |
| **Usalama wa kurudi nyuma** | Kila mdudu anapata mtihani; mdudu hawezi kurudi kamwe |
| **Nyaraka** | Majaribio hutumika kama hati hai ya tabia inayotarajiwa |
| **Kujiamini** | Ufikiaji wa juu wa majaribio huwezesha urekebishaji bila woga |
---

## Ukuzaji Unaoendeshwa na Tabia (BDD)
BDD huongeza TDD kwa kuandika majaribio katika lugha asilia ambayo yanaelezea tabia kutoka kwa mtazamo wa mtumiaji.
### Imetolewa-Wakati-Kisha Umbizo
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Zana | Lugha |
|------|-----------|
| **Tango** | Java, JavaScript, Ruby, na wengine |
| **Kutenda** | Chatu |
| **Specflow** | C# |
| **Jest** (pamoja na kuelezea/it) | JavaScript |
---

## Aina Nyingine za Upimaji
| Aina | Inajaribu Nini | Zana |
|------|--------------|-------|
| **Utendaji/Mzigo** | Tabia ya mfumo chini ya mzigo | k6, JMeter, Nzige, Gatling |
| **Usalama** | Udhaifu na vekta za kushambulia | OWASP ZAP, Burp Suite, Snyk |
| **Ufikivu** | Ufuataji wa WCAG | shoka, Mnara wa taa, pa11y |
| **Mkataba** | API utangamano kati ya huduma | Mkataba, Mkataba wa Cloud Cloud |
| **Mabadiliko** | Ubora wa chumba cha majaribio chenyewe | Stryker, mutmut, PIT |
| **Mrejesho wa kuona** | Mabadiliko ya UI kati ya matoleo | Percy, Chromatic, BackstopJS |
| **Machafuko** | Ustahimilivu wa mfumo kwa kushindwa | Machafuko Tumbili, Litmus, Gremlin |
| **Moshi** | Utendaji wa kimsingi baada ya kupelekwa | Maandishi maalum; ukaguzi wa afya |
| **Loweka** | Tabia ya mfumo kwa muda mrefu | Vipimo vya mzigo wa muda mrefu |
---

## Shirika la Mtihani
| Muundo | Maelezo | Wakati wa Kutumia |
|---------|---------------------------|
| **Iliyopo pamoja** | Majaribio karibu na msimbo wanaojaribu (`src/utils.test.ts`) | Miradi mingi; rahisi kupata |
| **saraka tofauti** | Majaribio katika folda ya`tests/`au`__tests__/`| Miradi mikubwa; utengano wazi |
| **Ratiba za majaribio** | Data ya jaribio iliyoshirikiwa katika saraka ya`fixtures/`| Wakati majaribio mengi yanahitaji data sawa |
| **Jaribio la huduma** | Wasaidizi walioshirikiwa katika saraka ya`test-utils/`| Wakati mantiki ya usanidi ni changamano |
---

## Chanjo ya Msimbo
| Kipimo | Inapima Nini | Kizuizi |
|--------|------------------------------|
| **Chanjo ya mstari** | Asilimia ya mistari ya msimbo inayotekelezwa na majaribio | Haipimi ubora wa madai |
| **Utoaji wa tawi** | Asilimia ya matawi (ikiwa/vinginevyo) iliyochukuliwa | Bora kuliko chanjo ya mstari; bado haipati hitilafu zote |
| **Chanjo ya njia** | Asilimia ya njia za utekelezaji zilizochukuliwa | Ukamilifu zaidi; kielelezo katika msimbo changamano |
| **Alama ya mabadiliko** | Asilimia ya mabadiliko yaliyonaswa na majaribio | Kipimo bora cha ubora wa mtihani |
**Lengo**: 80% ya ufikiaji wa laini ni chaguomsingi inayofaa. Lakini chanjo ni mwongozo, sio lengo - ufunikaji wa 100% na madai dhaifu ni mbaya zaidi kuliko ufikiaji wa 70% kwa majaribio ya kina.
---

## Muunganisho Unaoendelea na Upimaji
| Mazoezi | Maelezo |
|----------|-------------|
| **Fanya majaribio yote ya kitengo kwa kila ahadi** | Maoni ya haraka; hupata rejeshi mara moja |
| **Fanya majaribio ya ujumuishaji kwenye PR** | Hupata masuala ambayo majaribio ya vipimo yanakosa |
| **Fanya majaribio ya E2E kila usiku au unganisha kwa main** | Polepole lakini kamili |
| **Imeshindwa haraka** | Komesha bomba kwa kushindwa kwanza kuokoa muda |
| **Sera ya majaribio hafifu** | Weka karantini au ufute vipimo hafifu mara moja; usipuuze kamwe |
| **Ulinganifu wa majaribio** | Fanya majaribio kwa sambamba ili kupunguza muda wa CI |
---

## Vidokezo Vitendo
- **Vipimo vya jina waziwazi.**`test_calculates_tax_for_high_earner`inakuambia kilichoharibika. `test_1`haikuambii chochote.
- **Madai moja kwa kila jaribio (inapowezekana).** Hurahisisha kugundua mapungufu.
- **Usijaribu maelezo ya utekelezaji.** Jaribu tabia. Ukirekebisha za ndani, majaribio hayafai kuvunjika.
- **Epuka kujaribu msimbo wa watu wengine.** Kudhihaki maktaba za nje; jaribu mwingiliano wa nambari yako nao.
- **Fanya majaribio haraka.** Jaribio lako likichukua dakika 10, wasanidi programu wataacha kuliendesha. Boresha bila kuchoka.
- **Futa majaribio yaliyokufa.** Majaribio ambayo hufaulu kila wakati au kujaribu nambari iliyoondolewa ni kelele.
- **Chukua nambari ya kuthibitisha kama vile msimbo wa uzalishaji.** Inapaswa kusomeka, kudumishwa na kupangwa vyema.
---

## Muhtasari
Kujaribu sio hiari - ni jinsi unavyounda programu ambayo haivunji. Piramidi ya majaribio hukuongoza kuelekea majaribio mengi ya haraka ya vipimo, baadhi ya majaribio ya ujumuishaji, na majaribio machache ya E2E. TDD na BDD hutoa mbinu zilizopangwa. Kejeli hutenga vitengo vya majaribio. Ufikiaji wa msimbo hupima upana lakini si kina. Kanuni muhimu zaidi ni hii: ikiwa haijajaribiwa, imevunjwa - bado haujui.