---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [federated, learning, privacy, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Kujifunza kwa Shirikisho na Faragha
Kujifunza kwa shirikisho ni mbinu ya kufunza miundo ya mashine ya kujifunza kwenye vifaa au mashirika mengi bila kushiriki data ghafi. Badala ya kutuma data kwa seva kuu, kila kifaa hufunza muundo wa ndani na hushiriki tu masasisho ya modeli (gradient au uzito). Seva kuu hujumlisha masasisho haya ili kutoa muundo wa kimataifa. Iliundwa na Google kwa ajili ya kufunza miundo ya lugha ya kibodi kwenye simu za Android - na tangu wakati huo imekuwa mbinu kuu ya AI ya kuhifadhi faragha.
---

## Kwa nini Kushirikishwa Kujifunza?
| Kuhamasisha | Maelezo | Mfano |
|------------|------------------------|
| **Faragha ya data** | Data ghafi haiachi kamwe kifaa | Rekodi za matibabu hukaa hospitalini; picha kaa kwenye simu |
| **Uzingatiaji wa udhibiti** | GDPR, HIPAA na kanuni zingine huzuia kushiriki data | Benki zinaweza kushirikiana bila kushiriki data ya mteja |
| **Kiasi cha data** | Kuhamisha data ni ghali na polepole | Mafunzo kwa mabilioni ya simu hayawezekani ikiwa ni lazima data ipakwe |
| **Unyeti wa data** | Baadhi ya data ni nyeti sana kushirikiwa, hata kwa kibali | Ujasusi wa serikali; data ya afya ya kibinafsi |
---

## Jinsi Mafunzo Yaliyoshirikishwa Hufanya Kazi
### Itifaki ya Msingi (FedAvg)
| Hatua | Nini Kinatokea |
|------|-------------|
| **1. Anzisha** | Seva ya kati huunda muundo wa kimataifa na uzani nasibu |
| **2. Sambaza** | Seva hutuma muundo wa sasa wa kimataifa kwa vifaa vilivyochaguliwa |
| **3. Mafunzo ya ndani** | Kila kifaa hufunza muundo kwenye data yake ya ndani kwa vipindi kadhaa |
| **4. Pakia** | Vifaa hutuma uzani wa muundo uliosasishwa (sio data) kwenye seva |
| **5. Jumla** | Seva huweka wastani wa uzani (Wastani wa Shirikisho) ili kuunda muundo mpya wa kimataifa |
| **6. Rudia** | Rudi kwenye hatua ya 2 hadi muundo uungane |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Sifa Muhimu
| Mali | Maelezo |
|----------|-------------|
| **Data zisizo za IID** | Kila kifaa kina usambazaji tofauti wa data (sio huru na kusambazwa sawa) |
| **Data isiyo na usawa** | Vifaa vingine vina data nyingi, vingine vina kidogo sana |
| **Kushiriki kwa sehemu** | Sio vifaa vyote vinapatikana kwa kila mzunguko |
| **Ufanisi wa mawasiliano** | Kikwazo ni mawasiliano, sio hesabu |
---

## Lahaja Zilizoshirikishwa za Kujifunza
| Lahaja | Maelezo | Faida |
|---------|-------------|-----------|
| **FedAvg** | Uzani wa wastani wa miundo kwenye vifaa vyote | Rahisi; inafanya kazi vizuri kwa data ya IID |
| **FedProx** | Huongeza muhula wa karibu kwa mafunzo ya ndani | Bora kwa data isiyo ya IID |
| **SCAFFOLD** | Hutumia vidhibiti tofauti kusahihisha utofauti wa data | Muunganiko wa haraka kwenye data isiyo ya IID |
| **FedSGD** | Kama FedAvg lakini kwa hatua moja ya gradient kwa kila raundi | Gharama ya chini ya mawasiliano kwa kila mzunguko |
| **FL** Iliyobinafsishwa | Kila kifaa hudumisha muundo uliobinafsishwa pamoja na ule wa kimataifa | Utendaji bora kwa kila kifaa |
| **Wima FL** | Vipengele tofauti (si sampuli tofauti) kote pande zote | Wakati vyama vinashikilia vipengele tofauti vya data sawa |
---

## Faragha Tofauti
Faragha tofauti (DP) hutoa hakikisho la hisabati kwamba matokeo ya algoriti hayaonyeshi ikiwa data ya mtu yeyote ilijumuishwa.
### Ufafanuzi wa Msingi
Utaratibu M hutosheleza (ε, δ) -faragha tofauti ikiwa kwa seti mbili za data D na D' zinazotofautiana katika rekodi moja:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Kigezo | Maana |
|-----------|---------|
| **ε (epsilon)** | Bajeti ya faragha. Ndogo = faragha zaidi. Thamani za kawaida: 0.1–10. |
| **δ (delta)** | Uwezekano wa dhamana ya faragha kushindwa. Kwa kawaida huwekwa kuwa 1/N (kinyume cha saizi ya mkusanyiko wa data). |
### Mbinu za Kuongeza Faragha
| Utaratibu | Jinsi Inavyofanya Kazi | Tumia Kesi |
|-----------|-------------------------|
| **Utaratibu wa Gaussian** | Ongeza kelele ya Gaussian iliyosawazishwa kwa unyeti wa hoja | Thamani zinazoendelea (uzito wa mfano) |
| **Utaratibu wa laplace** | Ongeza kelele za Laplace | Kuhesabu maswali |
| **Utaratibu wa kielelezo** | Chagua matokeo yenye uwezekano sawia na matumizi yake | Chaguzi za kipekee |
### DP-SGD (Kushuka kwa Kiwango cha Kibinafsi kwa Tofauti cha Stochastic)
| Hatua | Maelezo |
|------|-------------|
| 1. Kokotoa kwa kila sampuli gradients | Badala ya batch gradients |
| 2. Clip gradients | Hufunga kiwango cha juu cha kawaida cha kila kipenyo (huweka mipaka ya ushawishi wa sampuli moja) |
| 3. Ongeza kelele | Ongeza kelele ya Gaussian iliyorekebishwa kwenye upinde rangi iliyojumlishwa |
| 4. Sasisha vigezo | Hatua ya mteremko wa kawaida |
| Biashara | Maelezo |
|-----------|-------------|
| **Faragha dhidi ya usahihi** | Faragha thabiti (chini ε) inahitaji kelele zaidi, ambayo hupunguza usahihi wa muundo |
| **Faragha dhidi ya muda wa mafunzo** | Kelele zaidi inamaanisha muunganiko wa polepole |
| **Ufuatiliaji wa bajeti ya faragha** | Kila hatua ya mafunzo hutumia baadhi ya bajeti ya faragha; ikitumika, haiwezi kurejeshwa |
---

## Kuchanganya Mafunzo Yaliyoshirikishwa na Faragha Tofauti
| Tabaka | Ulinzi |
|-------|------------|
| **Kujifunza kwa Shirikisho** | Data ghafi husalia kwenye vifaa |
| **Faragha tofauti** | Hata masasisho ya mfano ni ya kelele, yanalinda michango ya mtu binafsi |
| **Ukusanyaji salama** | Seva huona tu jumla ya masasisho yote, si yale mahususi |
Mseto huu hutoa hakikisho dhabiti za faragha: hata kama seva imeingiliwa, haiwezi kubainisha ikiwa data mahususi ya mtu binafsi ilitumika katika mafunzo.
---

## Mbinu Nyingine za Kuhifadhi Faragha
### Salama Ukokotoaji wa Vyama Vingi (SMPC)
Vyama vingi hukusanya chaguo la kukokotoa juu ya data zao zilizounganishwa bila kufichua maingizo yao mahususi.
| Kipengele | Maelezo |
|---------|-------------|
| **Jinsi inavyofanya kazi** | Data imegawanywa katika hisa zinazosambazwa kwa pande zote; hesabu hufanyika kwenye hisa |
| **Dhamana** | Hakuna chama kinachojifunza chochote kuhusu maoni ya wengine |
| **Kichwa** | Gharama kubwa ya mawasiliano na hesabu |
| **Tumia kesi** | Benki zinazotumia mifumo ya pamoja ya hatari bila kushiriki data ya mteja |
### Usimbaji wa Homomorphic (HE)
Fanya hesabu moja kwa moja kwenye data iliyosimbwa.
| Aina | Inasaidia Nini | Juu |
|------|----------------------------|
| **Kwa kiasi HE** | Operesheni moja (nyongeza AU kuzidisha) | Chini |
| **Kwa kiasi fulani HE** | Idadi ndogo ya shughuli zote mbili | Kati |
| **Kabisa HE** | Mahesabu ya kiholela | Juu sana (kupungua kwa 100-1000x) |
| Maombi | Maelezo |
|---------------------------|
| **Maelekezo ya kibinafsi** | Endesha miundo ya ML kwenye data iliyosimbwa; rudisha ubashiri uliosimbwa kwa njia fiche |
| **Mafunzo yaliyosimbwa kwa njia fiche** | Treni juu ya data iliyosimbwa (bado ni ya kinadharia kwa ujifunzaji wa kina) |
| **Maswali ya kibinafsi** | Hoji hifadhidata bila kufichua hoja au data |
### Mazingira ya Utekelezaji Yanayoaminika (TEEs)
Kutengwa kwa msingi wa maunzi (Intel SGX, ARM Trustzone) ambayo hulinda data hata kutoka kwa OS.
| Faida | Kizuizi |
|-----------|------------|
| Utendaji wa karibu wa asili | Inahitaji maunzi maalum |
| Dhamana kali za usalama | Kumbukumbu ndogo (ukubwa wa enclave) |
| Hakuna maandishi ya siri | Mashambulizi ya pembeni yanawezekana |
---

## Kanuni za Faragha na ML
| Udhibiti | Mkoa | Athari kwa ML |
|---------------------|-------------|
| **GDPR** | EU | Haki ya maelezo; kupunguza data; idhini ya usindikaji; haki ya kufuta |
| **CCPA** | California | Haki ya kujua, kufuta, na kuchagua kutoka kwa uuzaji wa data |
| **HIPAA** | Marekani (huduma ya afya) | Udhibiti mkali wa data ya afya; mahitaji ya de-kitambulisho |
| **PIPL** | China | Ujanibishaji wa data; mahitaji ya kibali; sheria za uhamisho wa mpaka |
| **Kitendo cha AI** | EU | Mahitaji ya uwazi; uainishaji wa hatari; mazoea yaliyopigwa marufuku |
### Athari kwa Mitiririko ya Kazi ya ML
| Kanuni ya GDPR | Maana ya ML |
|--------------------------------|
| **Upunguzaji wa data** | Kusanya tu kile kinachohitajika; kujifunza kwa shirikisho husaidia |
| **Kizuizi cha kusudi** | Haiwezi kutumia tena data bila idhini mpya |
| **Haki ya kufuta** | Lazima uweze kuondoa data ya mtu kutoka kwa kielelezo kilichofunzwa (kuacha kujifunza kwa mashine) |
| **Haki ya maelezo** | Miundo lazima iweze kufasirika vya kutosha ili kuelezea utabiri wa mtu binafsi |
| **Faragha kwa muundo** | Faragha lazima ijengwe katika mifumo tangu mwanzo |
---

##Changamoto
| Changamoto | Maelezo |
|-----------|-------------|
| **Gharama ya mawasiliano** | Kutuma masasisho ya miundo zaidi ya mamilioni ya vifaa ni ghali |
| **Data zisizo za IID** | Vifaa vina usambazaji tofauti wa data, na kuumiza muunganisho |
| **Stragglers** | Vifaa vya polepole huchelewesha mzunguko mzima |
| **Biashara ya matumizi ya faragha** | Faragha thabiti inamaanisha utendakazi mbaya zaidi wa muundo |
| **Mashambulizi ya sumu** | Washiriki hasidi wanaweza kufisidi muundo wa kimataifa |
| **Uchimbaji wa mfano** | Hata masasisho ya miundo ya pamoja yanaweza kuvuja taarifa kuhusu data ya mafunzo |
| **Utofauti wa maunzi** | Vifaa tofauti vina uwezo tofauti wa kukokotoa |
---

## Zana na Mifumo
| Zana | Kusudi |
|------|----------|
| **Maua** | Mfumo wa kujifunza ulioshirikishwa kwa vyanzo huria; mfumo-agnostic |
| **TensorFlow Federated** | Mfumo wa FL wa Google wa miundo ya TensorFlow |
| **PySyft** (OpenMined) | ML ya kuhifadhi faragha katika PyTorch |
| **FATE** (Webank) | Jukwaa la elimu la shirikisho la viwango vya viwanda |
| **JANI** | Benchmark Suite kwa ajili ya utafiti wa shirikisho wa kujifunza |
| **Opacus** (Meta) | Faragha tofauti ya PyTorch |
| **Faragha ya TF ya Google** | Faragha tofauti kwa TensorFlow |
---

## Muhtasari
Mbinu zilizoshirikishwa za kujifunza na kuhifadhi faragha hushughulikia mvutano wa kimsingi: unawezaje kuunda miundo thabiti ya AI wakati data inasambazwa, nyeti, au kudhibitiwa? Mafunzo yaliyoshirikishwa huhifadhi data kwenye vifaa na kushiriki masasisho ya miundo pekee. Faragha tofauti huongeza uhakikisho wa hisabati kwamba michango ya mtu binafsi haiwezi kutambuliwa. Uhesabuji salama na usimbaji fiche wa homomorphic huenda mbali zaidi, ikiruhusu kukokotoa kwa data iliyosimbwa. Kila mbinu ina gharama - juu ya mawasiliano, usahihi uliopunguzwa, gharama ya hesabu - lakini kwa pamoja huunda zana ya kujenga AI ambayo inaheshimu faragha wakati bado inajifunza kutoka kwa data ya ulimwengu.