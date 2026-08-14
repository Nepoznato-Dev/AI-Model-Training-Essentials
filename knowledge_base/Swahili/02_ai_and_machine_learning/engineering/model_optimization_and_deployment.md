---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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

# Uboreshaji wa Mfano na Usambazaji
Kufunza muundo mkubwa wa AI ni mafanikio makubwa, lakini kuusambaza kwa ufanisi ndipo juhudi nyingi za uhandisi zinahitajika. Muundo unaochukua sekunde 10 kujibu au unaohitaji GPU nane za A100 hauwezi kutumika kwa programu nyingi za ulimwengu halisi. Uboreshaji wa miundo ni mchakato wa kufanya miundo kuwa ndogo, haraka, na ya gharama nafuu zaidi - huku ikidumisha ubora unaokubalika. Faili hii inashughulikia ukadiriaji, upogoaji, kunereka, na zana za vitendo za kupeleka miundo katika uzalishaji.
---

## Kwa nini Uweke Matumaini?
| Wasiwasi | Athari |
|---------|--------|
| **Kuchelewa** | Watumiaji wanatarajia majibu chini ya sekunde 1; kila 100ms za ziada hupoteza uchumba |
| **Gharama** | Uelekezaji wa GPU ni ghali; mtindo wa 70B unagharimu ~$0.05-0.15 kwa tokeni za 1M kwenye maunzi ya wingu |
| **Kumbukumbu** | Mfano wa 7B katika FP32 unahitaji GB 28 ya VRAM; GPU nyingi za watumiaji zina GB 8-24 |
| **Nishati** | Kuendesha mifano kubwa hutumia umeme muhimu; mambo ya simu na makali |
| **Kipimo** | Kuhudumia mamilioni ya watumiaji kunahitaji miundo inayolingana na maunzi yanayopatikana |
---

## Ukadiriaji
Ukadiriaji hupunguza usahihi wa uzani wa mfano kutoka sehemu ya kuelea ya biti-32 (FP32) hadi miundo midogo kama vile INT8, INT4, au hata chini zaidi.
### Miundo ya Usahihi
| Umbizo | Biti kwa Uzito | Kumbukumbu ya 7B Model | Ubora |
|--------|-----------------------------------|---------|
| **FP32** | 32 | GB 28 | Msingi (usahihi kamili) |
| **FP16 / BF16** | 16 | GB 14 | Inakaribia kufanana na FP32 |
| **INT8** | 8 | GB 7 | Hasara ndogo sana ya ubora |
| **INT4** | 4 | GB 3.5 | Upotezaji wa ubora wa wastani; bado inatumika |
| **INT3 / INT2** | 3-2 | GB 2.6-1.75 | Upotezaji mkubwa wa ubora; hatua ya utafiti |
### Mbinu za Kuhesabu
| Mbinu | Inapotokea | Jinsi Inavyofanya Kazi | Ubora |
|--------|------------------------------|---------|
| **Ukadiriaji wa Baada ya Mafunzo (PTQ)** | Baada ya mafunzo kukamilika | Rekebisha mfano kwenye mkusanyiko mdogo wa data; pata mizani bora | Nzuri kwa INT8; inashusha hadhi kwa INT4 |
| **GPTQ** | Baada ya mafunzo | Ukadiriaji wa INT4 unaofaa kwa GPU kwa kutumia takriban maelezo ya agizo la pili | Ubora mzuri katika INT4 |
| **AWQ** (Uhesabuji wa Uzito unaotambua Uwezeshaji) | Baada ya mafunzo | Linda uzani muhimu kulingana na ukubwa wa kuwezesha | Bora kuliko GPTQ katika INT4 |
| **GGUF** (umbizo la llama.cpp) | Baada ya mafunzo | quantisation ya kirafiki ya CPU; usahihi mchanganyiko kwa safu | Imeboreshwa kwa makisio ya CPU |
| **Mafunzo ya Kufahamu Kiasi (QAT)** | Wakati wa mafunzo | Iga ukadiriaji wakati wa mafunzo ili mwanamitindo ajifunze kustahimili | Ubora bora; inahitaji mafunzo upya |
### Athari za Kiutendaji
| Mfano | Ukubwa wa FP16 | Ukubwa wa INT4 | Kuongeza kasi | Kupoteza Ubora |
|-------|-----------|-----------|---------|-------------|
| **LLaMA 7B** | GB 14 | GB 3.5 | 2-4x | ~1-2% kwenye vigezo |
| **LLaMA 70B** | GB 140 | GB 35 | 2-3x | ~2-3% kwenye vigezo |
---

##Kupogoa
Kupogoa huondoa uzito au neuroni zisizo za lazima kutoka kwa modeli iliyofunzwa.
| Aina | Maelezo | Faida | Changamoto |
|------|-------------------------|------------
| **isiyo na muundo** | Ondoa uzani wa mtu binafsi (weka hadi sifuri) | Uwiano wa juu wa mbano | Inahitaji usaidizi mdogo wa maunzi |
| **Muundo** | Ondoa niuroni nzima, vichwa vya umakini, au tabaka | Inapunguza saizi ya kielelezo moja kwa moja | Huenda ikapoteza ubora zaidi |
| **Kulingana na ukubwa** | Ondoa uzani na maadili madogo kabisa | Rahisi; inafanya kazi vizuri | Huenda akakosa uzani mdogo muhimu |
| **Kulingana na umuhimu** | Ondoa uzani kulingana na mchango wao katika pato | Uhifadhi bora wa ubora | Ghali zaidi kukokotoa |
### Bomba la Kupogoa
| Hatua | Maelezo |
|------|-------------|
| 1. Treni | Treni muundo kamili kawaida |
| 2. Alama | Kokotoa alama za umuhimu kwa kila uzani/nyuroni |
| 3. Pogoa | Ondoa vipengele muhimu zaidi |
| 4. Fanya vizuri | Jifunze upya ili kurejesha usahihi uliopotea |
| 5. Rudia | Kupogoa mara kwa mara na kurekebisha vizuri kwa mgandamizo wa hali ya juu |
---

##Kuchangamsha Maarifa
Kufunza kielelezo kidogo cha "mwanafunzi" kuiga kielelezo kikubwa cha "mwalimu".
| Sehemu | Jukumu |
|-----------|------|
| **Mwalimu** | Mfano mkubwa, wa hali ya juu |
| **Mwanafunzi** | Mfano mdogo unaojifunza kutoka kwa mwalimu |
| **Hasara ya kunereka** | Mwanafunzi anajaribu kulinganisha usambazaji wa matokeo ya mwalimu (lebo laini) |
### Aina za kunereka
| Aina | Maelezo | Mfano |
|------|-------------|----------|
| **Kutokana na lojiti** | Mwanafunzi analingana na uwezekano wa pato la mwalimu | kunereka asili ya Hinton |
| **Kulingana na kipengele** | Mwanafunzi analingana na uwakilishi wa kati wa mwalimu | FitNets |
| **Kutokana na uhusiano** | Mwanafunzi hulinganisha uhusiano kati ya sampuli | RKD (Unyonyaji wa Maarifa ya Kihusiano) |
| **Bila data** | Hakuna data asili ya mafunzo inahitajika; tumia kizazi cha mwalimu | DAFL, DeepInversion |
### Mifano mashuhuri ya kunereka
| Mwalimu | Mwanafunzi | Matokeo |
|---------|-------------------|
| **GPT-4** | GPT-3.5-turbo (kuna uvumi) | Muundo mdogo wenye ubora mwingi wa GPT-4 |
| **BERT-Kubwa** | DistilBERT | 40% ndogo, 60% haraka, 97% ya utendaji wa BERT |
| **LLaMA 70B** | LLaMA 7B (kupitia kunereka) | Muundo mdogo wa chanzo huria unaokaribia ubora wa kielelezo kikubwa |
---

Uboreshaji ## Mahususi wa LLM
### Uboreshaji wa Akiba ya KV
Miundo mikubwa ya lugha huweka akiba ya jozi za ufunguo-thamani kutoka kwa tokeni zilizopita ili kuepuka kukusanywa tena.
| Mbinu | Maelezo | Athari |
|-----------|-------------|--------|
| **Tahadhari ya Maswali Mengi (MQA)** | Vichwa vyote vya umakini vinashiriki jozi moja ya KV | Inapunguza kumbukumbu; hasara kidogo ya ubora |
| **Tahadhari ya Maswali ya Kikundi (GQA)** | Vikundi vya vichwa vinashiriki jozi za KV | Usawa kati ya MQA na umakini wa kawaida |
| **Tahadhari ya dirisha inayoteleza** | Hudhuria tu tokeni za W za mwisho | Hupunguza ukubwa wa akiba ya KV kwa miktadha mirefu |
### Usimbuaji wa Kukisia
| Hatua | Maelezo |
|------|-------------|
| 1 | Mfano mdogo wa "rasimu" hutoa ishara za K haraka |
| 2 | Muundo mkubwa huthibitisha tokeni zote za K katika pasi moja ya mbele |
| 3 | Ishara zilizokubaliwa zimehifadhiwa; waliokataliwa wanazaliwa upya |
Matokeo: kasi ya 2-3x katika kizazi bila upotezaji wa ubora (mfano mkubwa huwa na usemi wa mwisho).
### Kiwango cha Makini
| Kipengele | Maelezo |
|---------|-------------|
| **Tatizo** | Uangalifu wa kawaida unahitaji kumbukumbu ya O(n²) kwa matrix ya umakini |
| **Suluhisho** | Kuhesabu umakini katika vizuizi; kamwe usifanye matrix kamili kwenye kumbukumbu |
| **Matokeo** | 2-4x haraka; huwezesha madirisha ya muktadha mrefu zaidi |
| **Vibadala** | Flash Attention 2 (haraka), FlashDecoding (imeboreshwa kwa makisio) |
---

## Mifumo ya Kuhudumia
| Mfumo | Bora Kwa | Kipengele Muhimu |
|-----------|----------|-------------|
| **vLLM** | LLM inahudumia | PagedAttention; batching inayoendelea; matokeo ya juu |
| **TensorRT-LLM** | Maoni ya NVIDIA GPU | Utendaji wa juu zaidi kwenye maunzi ya NVIDIA |
| **llama.cpp** | CPU na maelekezo ya GPU ya watumiaji | Huendesha miundo iliyokadiriwa kwenye kompyuta za mkononi na simu |
| **Ollama** | Muundo wa ndani unaoendeshwa | Karatasi ambayo ni rafiki kwa mtumiaji karibu na llama.cpp |
| **Seva ya Maelekezo ya Triton** | Huduma za mifumo mingi | Inaauni TensorFlow, PyTorch, ONNX, TensorRT |
| **TorchServe** | Mfano wa PyTorch unaohudumia | Ujumuishaji wa asili wa PyTorch |
| **Muda wa utekelezaji wa ONNX** | Maelekezo ya jukwaa la msalaba | Utekelezaji ulioboreshwa kwenye maunzi |
| **BentoML** | Usambazaji wa uzalishaji | Mfumo-agnostic; Hushughulikia ufungaji na kuhudumia |
---

## Mifumo ya Usambazaji
| Muundo | Maelezo | Wakati wa Kutumia |
|---------|---------------------------|
| **Usambazaji wa makali** | Endesha miundo kwenye simu, vifaa vya IoT, au maunzi yaliyopachikwa | Ucheleweshaji wa chini; nje ya mtandao; faragha |
| **API ya Wingu** | mifano ya jeshi kwenye GPU za wingu; tumikia kupitia API | Upeo wa hesabu; lipa kwa matumizi |
| **Mseto** | Mfano mdogo kwenye kifaa; mfano mkubwa katika wingu | Bora kati ya walimwengu wote |
| **Bila seva** | Kiwango hadi sifuri; lipa tu unapotumika | Trafiki ya hapa na pale; gharama nafuu |
| **Maelekezo ya kundi** | Mchakato wa data kwa wingi kwenye ratiba | Wakati muda halisi hauhitajiki |
---

## Kuweka alama
| Kipimo | Inapima Nini |
|--------|-----------------|
| **Tokeni kwa sekunde** | Uzalishaji wa kizazi (juu ni bora) |
| **Muda wa tokeni ya kwanza (TTFT)** | Ucheleweshaji kabla ya tokeni ya pato la kwanza kuonekana |
| **Uchelewaji kwa kila ombi** | Jumla ya muda kutoka ingizo hadi towe kamili |
| **Matumizi ya kumbukumbu** | VRAM au RAM inayotumiwa wakati wa makisio |
| **Mapitio** | Maombi yanayotumwa kwa sekunde |
| **Gharama kwa kila tokeni 1M** | Gharama ya dola ya usindikaji tokeni milioni 1 |
---

## Vidokezo Vitendo
- **Anza na ukadiriaji.** Ukadiriaji wa INT4 (AWQ au GPTQ) unatoa ubadilishanaji bora wa ubora hadi ukubwa. Aina nyingi za 7B huendesha kwa raha kwenye GPU ya mtumiaji mmoja katika INT4.
- **Tumia vLLM kwa huduma ya LLM.** Ndiyo chaguo la programu huria ya haraka zaidi kwa makisio ya juu ya LLM.
- **Wasifu kabla ya kuboresha.** Pima mahali ambapo wakati unatumika. Mara nyingi ni bandwidth ya kumbukumbu, sio kukokotoa, hiyo ndio kizuizi.
- **Linganisha modeli na kazi.** Muundo wa 7B unafaa kwa kazi nyingi. Usitumie 70B wakati 7B itafanya.
- **Zingatia kunereka.** Ikiwa unahitaji muundo mdogo, wa haraka kwa ajili ya uzalishaji, futa kutoka kwa muundo mkubwa badala ya mafunzo kutoka mwanzo.
- **Fuatilia kila wakati.** Utendaji wa muundo unaweza kuharibika kadiri muda unavyobadilika usambazaji wa data. Fuatilia muda wa kusubiri, matokeo na vipimo vya ubora.
---

## Muhtasari
Uboreshaji wa mfano ni daraja kati ya utafiti na uzalishaji. Ukadiriaji hupunguza miundo kwa 4-8x na upotezaji mdogo wa ubora. Kupogoa huondoa uzito uliokufa. Kunereka huhamisha maarifa kutoka kwa aina kubwa hadi ndogo. Uangalifu wa Flash na hila za kache za KV hufanya ufahamu haraka. Kwa pamoja, mbinu hizi hugeuza kielelezo kinachohitaji kituo cha data kuwa kinachotumia kompyuta ya mkononi au simu. Uga unaendelea haraka - kile kilichohitaji A100 nane mwaka jana kinatumia GPU ya watumiaji leo.