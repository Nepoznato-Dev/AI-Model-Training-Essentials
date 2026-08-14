---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
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
tags: [nlp, ai-and-machine-learning]
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

# Misingi ya NLP
Usindikaji wa Lugha Asilia (NLP) ni uwanja wa mashine za kufundishia ili kuelewa, kuzalisha, na kufanya kazi na lugha ya binadamu. Huwezesha injini za utafutaji, chatbots, mifumo ya tafsiri, uchanganuzi wa hisia, na miundo mikubwa ya lugha (LLMs) ambayo imebadilisha AI tangu 2020. Faili hii inashughulikia mageuzi kutoka kwa mbinu za kitamaduni hadi usanifu wa kisasa unaotegemea Transfoma.
---

## Uchakataji Maandishi
Maandishi ghafi yana fujo. Kabla ya kutumia mfano, inahitaji kusafishwa na kupangwa.
| Hatua | Inafanya Nini | Mfano |
|------|-------------|----------|
| **Tokenisation** | Gawanya maandishi katika ishara (maneno, maneno madogo au vibambo) | "Ninapenda NLP" →`["I", "love", "NLP"]`|
| **Mwandishi mdogo** | Badilisha kuwa herufi ndogo | "Hujambo" → "hujambo" |
| **Acha kuondoa maneno** | Ondoa maneno ya kawaida (the, is, at) | "paka alikaa" → "paka alikaa" |
| **Kutoka** | Kata miisho ya maneno (ghafi) | "kimbia" → "kimbia" |
| **Lematization** | Punguza kwa umbo la kamusi (muktadha-kufahamu) | "bora" → "nzuri" |
| **Urekebishaji** | Rekebisha usimbaji, ondoa chapa maalum, panua mikazo | "usifanye" → "usifanye" |
Miundo ya Kisasa ya Transfoma mara nyingi huruka uondoaji wa neno na kuhitimisha - hujifunza ruwaza hizi kutoka kwa data.
---

## Uwakilishi wa Maandishi
Mashine zinahitaji nambari, sio maneno. Jinsi tunavyowakilisha maandishi kama vekta ni ya msingi.
### Mbinu za Kawaida
| Mbinu | Maelezo | Kizuizi |
|--------|-------------|-----------|
| **Usimbaji wa Moto Mmoja** | Kila neno ni nafasi ya kipekee katika vekta kubwa | Sparse; hakuna maana ya kisemantiki |
| **Mfuko wa Maneno (Upinde)** | Hesabu masafa ya maneno; kupuuza agizo | Hupoteza mpangilio wa maneno kabisa |
| **TF-IDF** | Uzito wa maneno kwa marudio katika hati × nadra katika jumla ya wingi | Bado inapuuza mpangilio na muktadha |
### Upachikaji wa Maneno
Hupachika maneno ya ramani kwa vekta mnene ambapo maneno yanayofanana yanakaribiana.
| Mfano | Wazo Muhimu |
|-------|-----------|
| **Word2Vec** (2013) | Bashiri neno kutoka kwa muktadha (CBOW) au muktadha kutoka kwa neno (Ruka-gramu) |
| **Glove** (2014) | Takwimu za utendakazi wa kimataifa → vekta mnene |
| **FastText** (2016) | Neno2Vec + habari ya neno ndogo (hushughulikia maneno adimu vizuri zaidi) |
Mfano maarufu:`king - man + woman ≈ queen`. Upachikaji hunasa mahusiano ya kisemantiki.
**Kizuizi**: upachikaji wa classical huweka vekta moja kwa kila neno, kwa hivyo haziwezi kushughulikia polisemia (maneno yenye maana nyingi). "Benki" katika "benki ya mto" na "akaunti ya benki" hupata vector sawa.
---

## Miundo ya Mfuatano
Kabla ya Transfoma, mbinu ya kawaida ya NLP ilikuwa kuchakata maandishi kwa kufuatana.
| Usanifu | Jinsi Inavyofanya Kazi | Nguvu | Udhaifu |
|---------------------------|----------------------|
| **RNN** | Mchakato wa ishara moja kwa wakati; kudumisha hali iliyofichwa | Hushughulikia ingizo la urefu tofauti | Gradients zinazopotea; haiwezi kunasa utegemezi wa muda mrefu |
| **LSTM** | RNN yenye milango (sahau, ingizo, pato) ili kudhibiti mtiririko wa habari | Bora katika utegemezi wa masafa marefu | Bado mfululizo; polepole kutoa mafunzo |
| **GRU** | LSTM Iliyorahisishwa (milango machache) | Kasi kuliko LSTM; utendaji sawa | Vikwazo sawa vya kimsingi |
Miundo hii huchakata maandishi kutoka kushoto kwenda kulia, ambayo ina maana kwamba ni polepole kutoa mafunzo (haiwezi kusawazisha) na hupambana na utegemezi wa masafa marefu.
---

## Utaratibu wa Kuzingatia
Kuzingatia huruhusu modeli kutazama nafasi zote kwa mlolongo kwa wakati mmoja na kuamua ni zipi zinafaa zaidi kwa utabiri wa sasa.
### Maarifa Muhimu
Badala ya kubana sentensi nzima kuwa hali moja iliyofichwa (kama RNN hufanya), umakini unajumuisha jumla ya uzani wa majimbo yote yaliyofichwa, ambapo uzani hujifunza.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Sehemu | Jukumu |
|-----------|------|
| **Swali (Q)** | Je, ninatafuta nini? |
| **Ufunguo (K)** | Je, nina nini? |
| **Thamani (V)** | Je, nitatoa taarifa gani? |
| **√d_k** | Sababu ya kuongeza ili kuzuia bidhaa kubwa za nukta |
---

## Usanifu wa Transfoma
Transfoma (Vaswani et al., 2017 — "Uangalifu Ndio Wote Unaohitaji") ilibadilisha ujirudiaji kabisa na umakini. Ni msingi wa karibu NLP zote za kisasa.
### Usanifu
| Sehemu | Maelezo |
|-----------|-------------|
| **Kisimbazi** | Inasoma maandishi ya kuingiza; hutoa uwakilishi wa muktadha |
| **Kisimbuaji** | Inazalisha maandishi ya pato; huhudhuria matokeo ya kisimbaji |
| **Kujijali** | Kila ishara hushughulikia tokeni zingine zote kwa mlolongo sawa |
| **Tahadhari ya Vichwa vingi** | Endesha vichwa vya tahadhari nyingi kwa sambamba; kunasa mahusiano tofauti |
| **Usimbaji wa Nafasi** | Ingiza maelezo ya msimamo (kwa kuwa hakuna urudiaji) |
| **Mtandao wa Kusambaza Mlisho** | Inatumika kwa kila nafasi kwa kujitegemea |
| **Urekebishaji wa Tabaka** | Imarisha mafunzo |
| **Miunganisho ya Mabaki** | Ruka miunganisho ya mtiririko wa gradient |
### Kisimbaji Pekee, Kisimbuaji-Pekee, Kisimbaji-Kisimbuaji
| Lahaja | Usanifu | Bora Kwa | Mifano |
|---------|------------------------|----------|
| **Kisimbaji pekee** | Anaelewa maandishi | Uainishaji, NER, uchanganuzi wa hisia | BERT, RoBERTa, DeBERTa |
| **Kisimbuaji pekee** | Huzalisha maandishi | Mitindo ya lugha, chatbots, kizazi cha msimbo | GPT-3/4, LLaMA, Claude |
| **Kisimbaji-Kisimbuaji** | Hubadilisha maandishi | Tafsiri, muhtasari | T5, BART, MBART |
---

## Familia za Mfano Mkuu
### Familia ya BERT (Encoder-Pekee)
| Mfano | Kipengele Muhimu |
|-------|-------------|
| **BERT** (2018) | Muundo wa Lugha Uliofichwa + Utabiri wa Sentensi Inayofuata |
| **RoBERTa** | NSP imeondolewa; mafunzo kwa muda mrefu na data zaidi |
| **ALBERT** | Kushiriki kwa parameter; alama ndogo zaidi |
| **DeBERTa** | Usikivu uliovunjika; NLU iliyoboreshwa |
| **DistilBERT** | 40% ndogo, 60% haraka, itabaki 97% ya utendaji wa BERT |
### Familia ya GPT (Dekoda-Pekee)
| Mfano | Vigezo | Vidokezo |
|-------|-----------|--------|
| **GPT-2** | 1.5B | Miundo iliyoonyeshwa ya avkodare pekee inaweza kutoa maandishi thabiti |
| **GPT-3** | 175B | Kujifunza kwa risasi chache; kuhamasishwa badala ya kusawazishwa |
| **GPT-3.5 / GPT-4** | Haijulikani | Maagizo-iliyopangwa + RLHF; mazungumzo |
| **LLaMA** (Meta) | 7B–70B | Uzito wazi; ilianzisha mfumo ikolojia wa LLM wa chanzo huria |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Miundo ya wazi yenye ufanisi na utendakazi dhabiti |
---

## Kazi za Msingi za NLP
| Kazi | Maelezo | Mfano wa Kawaida |
|------|-------------|--------------|
| **Uainishaji wa Maandishi** | Agiza lebo kwa maandishi (barua taka/sio barua taka, chanya/hasi) | BERT, waainishaji walioboreshwa |
| **Utambuzi wa Huluki (NER) Unaoitwa Jina lao (NER)** | Tambua watu, mashirika, maeneo katika maandishi | safu ya BERT + CRF |
| **Uchambuzi wa Hisia** | Amua sauti ya kihisia | BERT iliyopangwa vizuri au LLM isiyo na sifuri |
| **Tafsiri ya Mashine** | Tafsiri kati ya lugha | T5, mBART, MarianMT |
| **Majibu ya Swali** | Jibu maswali kutokana na muktadha | BERT (ya kuchimba), GPT (ya kuzalisha) |
| **Muhtasari** | Finya maandishi marefu | T5, BART, GPT |
| **Kizazi cha Maandishi** | Toa maandishi madhubuti | GPT-4, LLaMA, Claude |
---

## Urekebishaji Bora dhidi ya Uhamasishaji
| Mbinu | Jinsi Inavyofanya Kazi | Wakati wa Kutumia |
|----------|---------------------------|
| **Urekebishaji mzuri** | Sasisha uzani wa muundo kwenye data yako mahususi ya kazi | Umeandika data; zinahitaji utendaji wa juu |
| **Kuhimiza** | Toa maagizo ya kielelezo kwa lugha asilia | Uchoraji wa haraka; data ndogo; kwa kutumia LLM |
| **Picha chache** | Jumuisha mifano katika kidokezo | Unapokuwa na mifano michache lakini haitoshi kwa kusawazisha vizuri |
| **LoRA / QLoRA** | Urekebishaji mzuri wa ufanisi; sasisha matrices madogo ya cheo cha chini | Rekebisha miundo mikubwa yenye kumbukumbu ndogo ya GPU |
---

## Zana na Mifumo
| Zana | Kusudi |
|------|----------|
| **Vibadilisha uso vya Kukumbatiana** | Mitindo iliyofunzwa awali, viashiria, mabomba ya kurekebisha vizuri |
| **spaCy** | Bomba la daraja la uzalishaji la NLP (tokenisation, NER, POS, utegemezi) |
| **NLTK** | Kielimu; algoriti za kawaida za NLP |
| **Gensim** | Uundaji wa mada (LDA), upachikaji wa maneno (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Mifumo ya kujenga programu zinazoendeshwa na LLM |
| **vLLM** | LLM ya hali ya juu inayohudumia |
| **Viashiria (HF)** | Uwekaji ishara haraka (BPE, WordPiece, SentencePiece) |
---

## Mandhari ya LLM
Mandhari ya kisasa ya NLP inatawaliwa na Miundo Kubwa ya Lugha:
| Kitengo | Mifano | Vidokezo |
|----------|---------|--------|
| **Mmiliki** | GPT-4, Claude, Gemini | Utendaji bora; Ufikiaji wa API pekee |
| **Uzito-wazi** | LLaMA 3, Mistral, Qwen | Uzito unaopatikana; kukimbia ndani ya nchi |
| **Chanzo-wazi** | Pythia, OPT | Fungua kabisa (data, uzani, nambari) |
| **Multimodal** | GPT-4V, Gemini, LLaVA | Mchakato maandishi + picha |
| **Imeboreshwa na kanuni** | CodeLlama, StarCoder, DeepSeek Coder | Kufunzwa kwa kanuni |
| **Ndogo / Ufanisi** | Phi-3, Gemma, TinyLlama | Utendaji mzuri kwa kiwango kidogo |
Uwanja unaendelea kwa kasi. Kilicho kisasa zaidi leo kinaweza kufutwa baada ya miezi kadhaa. Misingi - umakini, tokenisation, urekebishaji mzuri, tathmini - inabaki thabiti.