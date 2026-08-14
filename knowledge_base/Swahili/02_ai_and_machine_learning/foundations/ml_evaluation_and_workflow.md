---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [ml, evaluation, workflow, ai-and-machine-learning]
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

# Tathmini ya Kujifunza kwa Mashine na mtiririko wa kazi
Mwongozo wa vitendo kwa mzunguko wa maisha wa ML - kutoka kwa kuunda shida hadi ufuatiliaji wa uzalishaji - kwa kuzingatia vipimo, uthibitishaji na utatuzi.
---

## Mtiririko wa Kazi wa ML (CRISP-ML)
1. **Uelewa wa Biashara**: Bainisha lengo na vigezo vya mafanikio.
2. **Uelewa wa Data**: Chunguza data inayopatikana, tambua masuala ya ubora.
3. **Maandalizi ya Data**: Safisha, badilisha na ugawanye data.
4. ** Uundaji wa modeli**: Treni mifano, tune hyperparameters.
5. **Tathmini**: Tathmini utendakazi dhidi ya vipimo.
6. **Usambazaji**: Tumia kielelezo katika uzalishaji.
7. **Ufuatiliaji**: Fuatilia mteremko, utendakazi na hitilafu.
Hiki ni kitanzi kinachojirudia - utarejea hatua za awali kulingana na matokeo ya tathmini.
---

## Kugawanya Data
### Treni / Uthibitishaji / Mgawanyiko wa Jaribio
- **Seti ya mafunzo** (~70%): Inatumika kutoshea vigezo vya mfano.
- **Seti ya uthibitishaji** (~15%): Inatumika kurekebisha vigezo na kuchagua vibadala vya miundo.
- **Seti ya majaribio** (~15%): Inatumika mara moja tu mwishoni kukadiria utendakazi wa jumla.
**Muhimu:** Seti ya majaribio lazima iwekwe bila kuguswa kabisa hadi tathmini ya mwisho ili kuepuka kuvuja kwa data.
### Uthibitishaji Mtambuka (k-fold)
Kwa seti ndogo za data, tumia uthibitishaji mtambuka wa k-fold: gawanya data katika mikunjo ya k, treni kwenye k-1, thibitisha kwenye iliyosalia, na urudie mara k. Wastani wa utendaji. k=5 au k=10 ni kawaida.
### Mgawanyiko Uliotabaka
Kwa uainishaji na madarasa yasiyo na usawa, tumia mgawanyiko wa tabaka ili kuhifadhi uwiano wa darasa katika kila kitengo.
### Mgawanyiko Kulingana na Wakati
Kwa data ya mfululizo wa saa, gawanya kwa mpangilio (funza kuhusu yaliyopita, jaribu kuhusu siku zijazo) badala ya nasibu.
---

## Vipimo vya Tathmini
### Vipimo vya Uainishaji
| Kipimo | Inapima nini | Inatumika vyema kwa |
|--------|-----------------|---------------|
| **Usahihi** | (TP + TN) / (TP + TN + FP + FN) | Seti za data zilizosawazishwa |
| ** Usahihi** | TP / (TP + FP) | Wakati chanya za uwongo ni ghali (k.m., kugundua taka) |
| **Kumbuka** | TP / (TP + FN) | Wakati matokeo mabaya ya uwongo yanagharimu (k.m., uchunguzi wa saratani) |
| **F1-alama** | Maana ya Harmonic ya usahihi na kukumbuka | Seti za data zisizo na usawa, kipimo cha nambari moja |
| **AUC-ROC** | Eneo chini ya curve ROC; biashara kati ya TPR na FPR | Utendaji wa kiainishaji wa jumla bila kikomo |
| **AUC-PR** | Eneo lililo chini ya Precision-Recall Curve | Seti za data zisizo na usawa |
**Ufafanuzi:**
- TP = Kweli Chanya
- TN = Kweli Hasi
- FP = Chanya Isiyo sahihi (Hitilafu ya Aina ya I)
- FN = Hasi ya Uongo (Hitilafu ya Aina ya II)
### Vipimo vya Kurudi nyuma
| Kipimo | Inapima nini | Unyeti kwa wauzaji wa nje |
|--------|-------------------------------------------|
| **MSE** (Maana ya Hitilafu ya Mraba) | Wastani wa tofauti ya mraba | Juu |
| **RMSE** (Root Mean Squared Error) | Mzizi wa mraba wa MSE (vizio sawa na lengo) | Juu |
| **MAE** (Maana ya Hitilafu Kabisa) | Wastani wa tofauti kabisa | Chini |
| **R²** (Mgawo wa Uamuzi) | Uwiano wa tofauti umeelezwa | Hakuna moja kwa moja, lakini nyeti kwa wauzaji wa nje kwa njia isiyo ya moja kwa moja |
### Vipimo vya Uwekaji Cheo na Urejeshaji
- **Precision@k**: Sehemu ya vipengee muhimu kati ya mapendekezo ya juu-k.
- **Recall@k**: Sehemu ya vipengee vyote muhimu vinavyoonekana kwenye top-k.
- **NDCG** (Faida Nyongeza Lililopunguzwa Lililopunguzwa): Hesabu za umuhimu wa nafasi.
- **Kiwango cha Kupiga**: Iwapo kipengee husika kinaonekana katika sehemu ya juu-k.
### Vipimo vya Uzalishaji / LLM
- **Utata**: Jinsi "umeshangazwa" mtindo ni kwa maandishi yaliyoshikiliwa (ya chini ni bora).
- **BLEU**: n-gram hupishana na tafsiri za marejeleo (zinazolenga kwa usahihi).
- **ROUGE**: Mwingiliano wenye mwelekeo wa kukumbuka kwa muhtasari.
- **BERTScore**: Kufanana kwa kisemantiki kwa kutumia upachikaji wa kimuktadha (imara zaidi kuliko BLEU).
- **METEOR**: Inalingana na visawe na mashina ya WordNet.
---

## Mitego ya Tathmini
### Uvujaji wa Data
Hutokea wakati maelezo kutoka kwa seti ya jaribio huathiri bila kukusudia mafunzo.
- **Zuia:** Kamwe usitumie data ya jaribio kwa uhandisi wa vipengele, urekebishaji wa kawaida, au urekebishaji wa vigezo.
- **Tambua:** Iwapo muundo wako umepata alama za juu za kutiliwa shaka, shuku uvujaji.
### Kutosha kupita kiasi
Mfano hufanya vizuri kwenye data ya mafunzo lakini vibaya kwenye uthibitishaji/jaribio.
- **Punguza:** Tumia urekebishaji, kusimamisha mapema, kurahisisha usanifu, au kukusanya data zaidi.
### Haifai
Mfano hufanya vibaya kwenye mafunzo na uthibitishaji.
- **Punguza:** Tumia muundo changamano zaidi, ongeza vipengele, au punguza urekebishaji.
### Data Isiyosawazishwa
- **Punguza:** Tumia uzani wa darasa, sampuli ya ziada (SMOTE), sampuli ndogo, au tumia vipimo vinavyofaa (F1, AUC-PR) badala ya usahihi.
### Drift ya Muda (Drift ya Dhana)
Uhusiano kati ya vipengele na lengo hubadilika kwa wakati.
- **Punguza:** Jifunze upya mara kwa mara, fuatilia utendakazi, tumia algoriti za utambuzi wa maji.
---

## Urekebishaji wa vigezo
- **Utafutaji wa Gridi**: Jaribu kikamilifu michanganyiko yote ya seti iliyoainishwa awali ya hyperparameta. Rahisi lakini gharama ya hesabu.
- **Utafutaji Nasibu**: Sampuli ya mchanganyiko nasibu kutoka kwa usambazaji. Ufanisi zaidi kuliko utafutaji wa gridi ya nafasi za juu-dimensional.
- **Uboreshaji wa Bayesian**: Hujenga kielelezo cha uwezekano wa chaguo za kukokotoa lengwa na huteua vigezo kwa akili. Maktaba: Optuna, Hyperopt, scikit-optimise.
- **Urekebishaji Kiotomatiki**: Tumia zana kama vile Optuna, Ray Tune, au Vipimo vya Uzito na Upendeleo kwa urekebishaji uliosambazwa.
**Mifumo ya utafutaji inayopendekezwa kwa vigezo vya kawaida:**
| Kigezo | Masafa yanayopendekezwa (kiwango-logi) |
|-----------|----------------------------|
| Kiwango cha kujifunza | 1e-5 hadi 1e-1 |
| Ukubwa wa kundi | 16, 32, 64, 128, 256 |
| Idadi ya tabaka (NN) | 2 hadi 6 |
| Idadi ya niuroni (NN) | 32 hadi 1024 |
| Udhibiti (L2) | 1e-6 hadi 1e-2 |
| Kina cha mti (XGBoost) | 3 hadi 12 |
---

## Uteuzi wa Mfano na Uthibitishaji
1. **Muundo wa msingi**: Anza na muundo rahisi wa kiheuristic au rahisi (k.m., urejeshaji wa kumbukumbu, wastani wa kubashiri) ili kuweka kikomo cha chini.
2. **Miundo ya watahiniwa**: Funza familia nyingi za mifano (k.m., Random Forest, XGBoost, Neural Network).
3. **Thibitisha kupita kiasi** kila mgombea kwenye seti ya uthibitishaji.
4. **Linganisha vipimo** (na vipindi vya kujiamini) na uchague mgombea bora zaidi.
5. **Tathmini ya mwisho** kwenye seti ya majaribio iliyoshikiliwa.
6. **Uchambuzi wa makosa**: Angalia mifano ambayo modeli inakosea. Tambua ruwaza (k.m., madarasa adimu, ingizo lisiloeleweka) na maarifa ya mipasho katika utayarishaji wa data au uhandisi wa vipengele.
---

## Usambazaji na Ufuatiliaji
### Kutumikia Miundo
- **Maelekezo ya kundi**: Chakata kiasi kikubwa cha data nje ya mtandao (k.m., mapendekezo ya kila usiku).
- **Mtazamo wa mtandaoni**: Utabiri wa wakati halisi kupitia API (k.m., bao la mkopo, utambuzi wa ulaghai).
- **Maelekezo ya kutiririsha**: Inaendeshwa na tukio, wakati halisi na utulivu wa chini (k.m., arifa za kihisi cha IoT).
### Ufuatiliaji wa Mfano
- **Ufuatiliaji wa utendaji**: Fuatilia usahihi/F1 baada ya muda kwenye data ya moja kwa moja (wakati ukweli msingi unapatikana).
- **Mteremko wa data**: Fuatilia mabadiliko katika usambazaji wa vipengele vya ingizo (k.m., kwa kutumia PSI - Fahirisi ya Uthabiti wa Idadi ya Watu).
- **Drift ya dhana**: Fuatilia mabadiliko katika uhusiano kati ya pembejeo na matokeo.
- **Mteremko wa utabiri**: Fuatilia usambazaji wa matokeo yaliyotabiriwa.
- **Uchelewaji na matokeo**: Hakikisha SLAs (Makubaliano ya Kiwango cha Huduma) yanatimizwa.
### Kuweka na Kutahadharisha
- Ingia maombi yote ya utabiri na majibu (pamoja na utambulisho).
- Weka arifa kwa:
  - Kupungua kwa kiasi kikubwa katika utendaji.
  - Asilimia kubwa ya ingizo zinazokosekana au batili.
  - Matokeo ya mfano nje ya mipaka inayotarajiwa.
### Matoleo ya Muundo na Usajili
- Tumia sajili ya kielelezo (k.m., MLflow, Weights & Biases, Sagemaker Model Registry) kuhifadhi na matoleo ya miundo, metadata na matokeo ya tathmini.
- Hifadhi msimbo wa mafunzo na toleo la data (kupitia DVC au Git LFS) kando ya modeli.
---

## Orodha ya Kukagua ya Mtiririko wa Kazi
- [ ] Tatizo limepangwa na kipimo cha mafanikio kimebainishwa.
- [ ] Uchunguzi wa data umefanywa (thamani zinazokosekana, viambajengo, usambazaji).
- [ ] Treni/uthibitishaji/mgawanyiko wa jaribio umeundwa (utaratibu ikiwa inahitajika).
- [ ] Muundo wa msingi umeanzishwa.
- [ ] Vielelezo vya watahiniwa vilivyofunzwa na kuthibitishwa.
- [ ] Vigezo vimewekwa.
- [ ] Muundo bora uliochaguliwa kupitia uthibitishaji mtambuka.
- [ ] Tathmini ya mwisho kwenye seti ya majaribio.
- [ ] Uchambuzi wa hitilafu umefanywa.
- [ ] Mpango wa upelekaji tayari (miundombinu inayohudumia).
- [ ] Dashibodi ya ufuatiliaji imewekwa.
- [ ] Nyaraka (kadi ya data, kadi ya mfano) imekamilika.