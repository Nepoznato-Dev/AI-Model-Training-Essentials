---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [time, series, forecasting, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mfululizo wa Wakati na Utabiri
Data ya mfululizo wa saa ni data yoyote inayokusanywa kwa wakati: bei za hisa, usomaji wa halijoto, trafiki ya tovuti, takwimu za mauzo, vichunguzi vya mapigo ya moyo, matumizi ya nishati. Utabiri unamaanisha kutabiri thamani za siku zijazo kulingana na mifumo ya zamani. Ni mojawapo ya matumizi muhimu sana ya sayansi ya data - na mojawapo ya magumu zaidi, kwa sababu siku zijazo hazina uhakika na mfululizo wa wakati wa ulimwengu halisi umejaa kelele, msimu na mapumziko ya muundo.
---

## Sifa za Msururu wa Muda
| Sehemu | Maelezo | Mfano |
|-----------|-------------|---------|
| **Mtindo** | Kuongezeka au kupungua kwa muda mrefu | Halijoto duniani kuongezeka kwa miongo kadhaa |
| **Msimu** | Mifumo ya kawaida, inayotabirika katika vipindi vilivyowekwa | Ongezeko la mauzo ya rejareja kila Desemba |
| **Mzunguko** | Kushuka kwa thamani kwa vipindi visivyobadilika (mara nyingi kiuchumi) | Kushuka kwa uchumi kila baada ya miaka 5-10 |
| **Kelele (mabaki)** | Tofauti nasibu ambayo haiwezi kuelezewa | Harakati za bei za kila siku |
| **Uhusiano otomatiki** | Thamani za sasa zinategemea thamani zilizopita | Halijoto ya leo ni sawa na ya jana |
### Utulivu
Mfululizo wa saa ni **ya kudumu** ikiwa sifa zake za takwimu (maana, tofauti) hazibadiliki kadiri muda unavyopita. Mbinu nyingi za utabiri zinadhania kusimama.
| Mtihani | Kusudi |
|------|----------|
| **Dickey-Fuller Iliyoongezwa (ADF)** | Hujaribu kama mzizi wa kitengo upo (usiosimama) |
| **Jaribio la KPSS** | Hujaribu kama mfululizo ni wa mtindo |
| Mabadiliko | Wakati wa Kutumia |
|-----------------------------|
| **Kutofautisha** | Ondoa mwelekeo: y'(t) = y(t) - y(t-1) |
| **Badilisha kumbukumbu** | Thibitisha tofauti (kwa ukuaji mkubwa) |
| **Tofauti za msimu** | Ondoa msimu: y'(t) = y(t) - y(t-s) ambapo s ni urefu wa msimu |
---

## Mbinu za Utabiri wa Kawaida
### Wastani wa Kusonga
| Mbinu | Maelezo | Bora Kwa |
|--------|-------------|----------|
| **Wastani Rahisi wa Kusonga (SMA)** | Wastani wa uchunguzi N wa mwisho | Data ya kelele ya kulainisha |
| **Wastani wa Kusonga Uzito** | Uchunguzi wa hivi majuzi zaidi hupata uzito mkubwa | Wakati data ya hivi majuzi ni muhimu zaidi |
| **Wastani wa Kusonga kwa Kielelezo (EMA)** | Kupungua kwa uzani kwa kasi | Kufuatilia mitindo kwa kuchelewa kidogo |
### Urejeshaji wa Kielelezo
| Mbinu | Vipengele | Tumia Kesi |
|--------|-----------|-----------|
| **Rahisi (SES)** | Kiwango pekee | Hakuna mtindo, hakuna msimu |
| **Holt's (Mbili)** | Kiwango + mwelekeo | Data yenye mwenendo lakini hakuna msimu |
| **Holt-Winters (Matatu)** | Kiwango + mwenendo + msimu | Data yenye mitindo na msimu |
### ARIMA na Vibadala
ARIMA (AutoRegressive Integrated Moving Wastani) ni kazi bora ya utabiri wa mfululizo wa muda.
| Sehemu | Maana | Kigezo |
|-----------|---------|------------|
| **AR (p)** | Rejea kwa thamani za p zilizotangulia | Ni thamani ngapi za zamani za kutumia |
| **Mimi (d)** | Idadi ya hatua tofauti za kufanya stationary | Tofauti mara ngapi |
| **MA (q)** | Toa mfano wa kosa kama mseto wa makosa yaliyopita | Ni makosa mangapi ya awali ya kutumia |
| Lahaja | Kiendelezi | Tumia Kesi |
|---------|-----------|-----------|
| **SARIMA** | Huongeza vipengele vya msimu (P, D, Q, s) | Data yenye msimu thabiti |
| **ARIMAX** | Huongeza vigeu vya nje | Unapojua kuhusu matukio yajayo |
| **VAR** | Multivariate ARIMA; mfululizo mbalimbali unaotegemeana | Vigeu vinapoathiri kila mmoja |
---

## Mbinu za Kisasa za ML
### Miundo ya LSTM na RNN
| Mfano | Usanifu | Faida |
|-------|-------------|------------|
| **LSTM** | Mtandao wa Kumbukumbu ya Muda Mrefu | Hunasa tegemezi za muda za masafa marefu |
| **GRU** | Kitengo cha Kawaida cha Gated (LSTM rahisi) | Mafunzo ya haraka; utendaji sawa |
| **Seq2Seq** | Kisimbaji-kisimbuaji kwa mfululizo wa saa | Ingizo / urefu wa pato nyumbufu |
| **Mtandao wa Mabadiliko ya Muda (TCN)** | Mipasuko ya sababu iliyopanuka | Mafunzo sambamba; uwanja mrefu wa kupokea |
### Mtume (Meta)
Zana ya vitendo ya utabiri iliyoundwa kwa mfululizo wa saa za biashara.
| Kipengele | Maelezo |
|---------|-------------|
| **Mtengano** | Mtindo + msimu + likizo |
| **Inayonyumbulika** | Hushughulikia kukosa data, wauzaji nje, na mapumziko ya muundo |
| **Inaweza kufasiriwa** | Vipengele vinaweza kusomeka na binadamu |
| **Otomatiki** | Mipangilio inayofaa; urekebishaji mdogo unahitajika |
| Nguvu | Kizuizi |
|----------|------------|
| Inafaa kwa vipimo vya biashara (mauzo, watumiaji) | Si bora kwa data ya masafa ya juu sana |
| Hushughulikia likizo na matukio maalum | Huchukua msimu wa nyongeza au wa kuzidisha |
| Imara kwa wauzaji wa nje | Si sahihi kuliko kujifunza kwa kina kwa mifumo changamano |
### Miundo Inayotokana na Transfoma
| Mfano | Kipengele Muhimu |
|-------|-------------|
| **Mtoa habari** | ProbSparse makini kwa mlolongo mrefu |
| **Kitengeneza otomatiki** | Utaratibu wa uunganisho otomatiki wa mtengano wa mfululizo |
| **PatchTST** | Huweka viraka mfululizo wa saa; inayojitegemea |
| **TimesFM** (Google) | Mfano wa msingi wa mfululizo wa wakati; mafunzo ya awali juu ya data mbalimbali |
| **Chronos** (Amazon) | Ishara za mfululizo wa wakati; hutumia usanifu wa mtindo wa LLM |
---

## Utambuzi Usio wa Kawaida katika Msururu wa Saa
Kugundua mifumo isiyo ya kawaida ambayo inapotoka kutoka kwa tabia inayotarajiwa.
| Mbinu | Mbinu | Tumia Kesi |
|--------|----------|-----------|
| **Takwimu** | Z-alama, IQR, chati za udhibiti | Rahisi, inayoeleweka vyema |
| **Msitu wa Kutengwa** | Msingi wa miti; hutenganisha hitilafu kwa kugawanya bila mpangilio | Ugunduzi wa hitilafu nyingi |
| **LOF** (Mambo ya Nje ya Ndani) | Msongamano-msingi; inalinganisha msongamano wa eneo na majirani | Wakati hitilafu ziko katika maeneo yenye msongamano wa chini |
| **Visimbaji kiotomatiki** | Hitilafu ya kujenga upya; kosa kubwa = hali isiyo ya kawaida | Miundo tata, isiyo ya mstari |
| **LSTM-msingi** | Tabiri hatua inayofuata; kosa kubwa la utabiri = hali isiyo ya kawaida | Hitilafu za kufuatana |
### Maombi
| Kikoa | Nini Maana Ya Kukosea |
|--------|-------------------|
| **Fedha** | Ulaghai, ajali za soko, ajali za flash |
| **Huduma za afya** | Mapigo ya moyo yasiyo ya kawaida, kuanza kwa mshtuko |
| **Utengenezaji** | Kushindwa kwa vifaa, kasoro za ubora |
| **Usalama mtandao** | Majaribio ya kuingilia, mashambulizi ya DDoS |
| **Miundombinu** | Upakiaji mwingi wa seva, hitilafu za mtandao |
---

## Vipimo vya Tathmini
| Kipimo | Mfumo (dhana) | Wakati wa Kutumia |
|--------|--------------------|-------------|
| **MAE** (Maana ya Hitilafu Kabisa) | Wastani wa makosa kabisa | Inaweza kufasiriwa; vitengo sawa na data |
| **RMSE** (Root Mean Squared Error) | Mzizi wa mraba wa wastani wa makosa ya mraba | Huadhibu makosa makubwa zaidi |
| **MAPE** (Maana ya Hitilafu ya Asilimia Kabisa) | Wastani wa makosa ya asilimia kamili | Wakati makosa ya jamaa ni muhimu |
| **SMPE** (MAPE Ulinganifu) | Toleo la ulinganifu la MAPE | Hushughulikia thamani karibu na sufuri bora |
| **MASE** (Maana ya Hitilafu Kabisa Iliyopimwa) | MAE kuhusiana na utabiri wa kijinga | Kulinganisha katika mfululizo tofauti |
---

## Mtiririko wa Kazi wa Vitendo
| Hatua | Maelezo |
|------|-------------|
| **1. Chunguza** | Panga mfululizo; kutambua mwenendo, msimu, outliers |
| **2. Oza** | Tenganisha katika mitindo, msimu, na vipengele vya mabaki |
| **3. Stationarise** | Tumia utofautishaji au ubadilishe ikihitajika |
| **4. Gawanya** | Mgawanyiko unaotegemea wakati (kamwe usigawanywe nasibu kwa mfululizo wa saa) |
| **5. Msingi** | Anza na utabiri wa kutojua (thamani ya mwisho, ujinga wa msimu) |
| **6. Mfano** | Jaribu mbinu za kitamaduni (ARIMA, Prophet), kisha mbinu za ML |
| **7. Tathmini** | Tumia vipimo vinavyofaa; kulinganisha na msingi |
| **8. Iterate** | Ongeza vipengele, jaribu miundo tofauti, tune hyperparameta |
---

## Zana na Maktaba
| Zana | Kusudi |
|------|----------|
| **miundo ya takwimu** | Mfululizo wa wakati wa kawaida (ARIMA, ETS, mtengano) |
| **Nabii** (Meta) | Utabiri wa mfululizo wa saa za biashara |
| **wakati wa kucheza** | Kiolesura cha ML kilichounganishwa kwa mfululizo wa saa |
| **Vishale** | Maktaba ya kina ya utabiri (kujifunza kwa kina + kwa kina) |
| **GluonTS** (Amazon) | Uundaji wa mfululizo wa wakati unaowezekana |
| **NeuralProphet** | Nabii aliye na vijenzi vya mtandao wa neva |
| **tsfresh** | Uchimbaji wa kipengele cha mfululizo wa saa otomatiki |
| **panda** | Udanganyifu na urekebishaji wa mfululizo wa saa |
---

## Muhtasari
Utabiri wa mfululizo wa saa unachanganya takwimu za kitamaduni na ujifunzaji wa kisasa wa mashine. Mbinu za kitamaduni (ARIMA, kulainisha kielelezo, Nabii) zinaweza kufasirika, kwa haraka, na mara nyingi ni sahihi. Mbinu za kujifunza kwa kina (LSTM, Transfoma) hunasa ruwaza changamano lakini zinahitaji data na urekebishaji zaidi. Kanuni kuu husalia zile zile bila kujali mbinu: elewa muundo wa data yako (mwelekeo, msimu, kelele), linganisha dhidi ya msingi rahisi, tathmini ukitumia vipimo vinavyofaa, na weka hesabu kwa ukweli kwamba siku zijazo hazitaiga yaliyopita haswa.