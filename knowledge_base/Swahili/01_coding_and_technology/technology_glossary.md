---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
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
tags: [technology, glossary, coding-and-technology]
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

# Kamusi ya Teknolojia
Faharasa ya marejeleo inayofunika miundo ya AI, maunzi, vigezo, na dhana za msingi
katika AI ya kisasa na mazingira ya kompyuta.
---

## Miundo ya Lugha ya AI na Wasaidizi
### ChatGPT
ChatGPT ni chatbot ya AI iliyotengenezwa na OpenAI, iliyotolewa kwa mara ya kwanza mnamo Novemba 2022.
Inaendeshwa na mfululizo wa GPT wa miundo mikubwa ya lugha (LLMs). ChatGPT ni moja
ya bidhaa za AI za watumiaji zinazokua kwa kasi zaidi katika historia, na kufikia milioni 100
watumiaji ndani ya miezi miwili baada ya kuzinduliwa. Inasaidia mazungumzo ya msingi wa maandishi, msimbo
kizazi, muhtasari, na uandishi wa ubunifu. Viwango vya kulipwa vinatoa ufikiaji
miundo yenye nguvu zaidi kama vile GPT-4 na GPT-4o.
### GPT (Generative Pre-trained Transformer)
GPT ni familia ya miundo mikubwa ya lugha iliyoundwa na OpenAI. Usanifu
hutumia Transfoma ya dekoda pekee iliyofunzwa ikiwa na lengo la ubashiri wa ishara inayofuata
shirika kubwa la maandishi. Matoleo muhimu yanajumuisha GPT-2 (2019, vigezo vya 1.5B, vyema
kwa utangazaji wa "hatari sana kutolewa", GPT-3 (2020, vigezo 175B, kwa upana
kutumika kupitia API), GPT-3.5 (uti wa mgongo wa ChatGPT asili), na GPT-4
(2023, multimodal, utendaji karibu na kiwango cha wataalamu wa binadamu kwenye vigezo vingi).
### Claude
Claude ni msaidizi wa AI iliyotengenezwa na Anthropic. Inaitwa baada ya Claude
Shannon, mwanzilishi wa nadharia ya habari. Anthropic ilianzishwa na zamani
Watafiti wa OpenAI na inaangazia "AI ya kikatiba" - mbinu ya kutengeneza
mifano salama zaidi kwa kuwafunza kufuata seti ya kanuni. Mifano ya Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) zinajulikana kwa madirisha marefu ya muktadha (juu.
hadi tokeni 200,000), hoja zisizoeleweka, na kupunguza matokeo hatari ikilinganishwa na
LLM za msingi.
### Gemini
Gemini ni familia ya Google DeepMind ya miundo mingi ya AI, iliyotangazwa mnamo
Desemba 2023. Gemini ni asili ya mitindo mingi - amefunzwa kutoka chini kwenda juu
maandishi, picha, sauti na video kwa wakati mmoja, tofauti na miundo ya awali iliyokuwa nayo
njia zilizoongezwa kupitia urekebishaji mzuri. Matoleo ni pamoja na Gemini Nano (kwenye kifaa),
Gemini Flash (haraka, gharama nafuu), na Gemini Ultra (uwezo wa juu zaidi).
Gemini huwezesha Google AI chatbot Bard (iliyopewa jina Gemini) na Google Search AI
Muhtasari.
### Phi-3-mini
Phi-3-mini ni modeli ya lugha ndogo (SLM) iliyotengenezwa na Microsoft na 3.8B
vigezo. Ilitolewa mnamo Aprili 2024. Tofauti na mifano mingi kubwa, Phi-3-mini
alifunzwa kwenye mkusanyiko wa data wa "ubora wa vitabu vya kiada" ulioratibiwa kwa uangalifu - mbinu
iliyoanzishwa na Utafiti wa Microsoft - ambayo inatanguliza ubora wa data juu ya kiasi ghafi.
Licha ya kuwa ndogo sana kuliko GPT-4 au Claude 3 Opus, mechi za Phi-3-mini au
inashinda modeli mara kadhaa kubwa kwenye vigezo vya hoja kama vile MMLU na
HumanEval. Inaauni dirisha la muktadha wa tokeni 4k katika lahaja yake ya msingi na 128k
dirisha katika lahaja ya muktadha mrefu. Phi-3-mini inaweza kuendeshwa kwenye GPU ya mtumiaji mmoja
au hata kwenye kifaa kwenye simu mahiri ya kisasa yenye RAM ya kutosha.
### Llama (Meta AI)
Llama (Mfano wa Lugha Kubwa Meta AI) ni familia ya uzani wazi ya wanamitindo
iliyotolewa na Meta. Llama 2 (2023) ilitolewa kwa matumizi ya utafiti na kibiashara
na ukubwa kuanzia 7B hadi 70B vigezo. Llama 3 (2024) imeboreshwa
utendaji kwa kiasi kikubwa, na mifano kuanzia 8B hadi 70B (na baadaye 400B+).
Kwa sababu uzani unaweza kupakuliwa hadharani, mifano ya Llama ndio msingi
kwa mfumo mkubwa wa ikolojia wa anuwai zilizopangwa vizuri (Alpaca, Vicuna, nk.)
na hutumiwa sana kwa usambazaji wa AI wa ndani/binafsi.
### Mistral
Mistral AI ni kampuni ya AI ya Ufaransa ambayo inakuza LLM zilizo wazi na za umiliki.
Mistral 7B (2023) ilionyesha kuwa mfano wa parameta 7B unaweza kuendana na
utendaji wa miundo mikubwa zaidi kwa kutumia mbinu bora kama vile kuteleza
usikivu wa dirisha na umakini wa maswali ya vikundi. Mixtral 8x7B (2023) ni mchanganyiko-
mfano wa wataalam - huelekeza kila ishara kwa kikundi kidogo cha mitandao 8 ya wataalam,
kufikia utendakazi wa kiwango cha GPT-3.5 huku ukiwa wa bei nafuu kimahesabu.
Miundo ya Mistral ina uzani wazi kabisa na inaweza kuendeshwa ndani ya nchi.
---

## Kadi za maunzi ya GPU na Michoro
### GPU (Kitengo cha Uchakataji wa Michoro)
GPU ni kichakataji kilichoundwa kwa ukokotoaji unaolingana sana. Awali
iliyoundwa kwa ajili ya kutoa michoro ya 3D, GPU zimekuwa muhimu kwa mafunzo ya AI/ML
na makisio kwa sababu wanaweza kufanya maelfu ya shughuli za sehemu zinazoelea
wakati huo huo kwa kutumia maelfu ya cores ndogo. Watengenezaji wakuu wawili wa GPU
kwa AI ni NVIDIA na AMD.
### Mfululizo wa NVIDIA GeForce RTX
Msururu wa RTX (Ray Tracing Texel eXtreme) ni laini ya watumiaji wa NVIDIA ya GPU. RTX
30xx (Ampere, 2020) na RTX 40xx (Ada Lovelace, 2022) ni pamoja na vizazi
Tensor Cores zilizojitolea kwa ajili ya kuharakisha shughuli za AI. VRAM (RAM ya video) ni
muhimu kwa kuendesha miundo ya AI ndani ya nchi - GPU ya 8GB inaweza kushughulikia kigezo cha 7B
mifano katika quantisation 4-bit; GPU ya 24GB inaweza kushughulikia miundo ya 70B katika 4-bit.
### NVIDIA A-Series na H-Series (Kituo cha Data)
A100 (Ampere, 2020) na H100 (Hopper, 2022) ni AI ya kitaalam ya NVIDIA.
vichapuzi. H100 ina hadi 80GB ya kumbukumbu ya HBM3 na ndiyo ya kawaida
vifaa nyuma ya mafunzo ya kiwango kikubwa cha LLM leo. GPU hizi zinagharimu $25,000–
$40,000 kila moja lakini toa 10–30× matumizi ya AI ya kadi za RTX za watumiaji.
### Mfululizo wa AMD Radeon RX
Mstari wa GPU wa watumiaji wa AMD. RX 7900 XTX (2022) ina 24GB VRAM na inaweza kukimbia
LLM za ndani kupitia ROCm (bunda la kukokotoa la GPU la AMD). GPU za AMD kwa ujumla ni chache
inayoungwa mkono vyema kuliko NVIDIA kwa mifumo ya AI, ingawa usaidizi unaboreka.
### Intel Arc
Intel Arc ni laini ya bidhaa ya Intel ya GPU, iliyotolewa kuanzia 2022. Arc
GPU zinatumia XeSS (sampuli bora za Intel) na zina usaidizi mdogo lakini unaokua
kwa kazi za uelekezaji za AI kupitia mifumo ya OpenVINO na IPEX-LLM.
### ARK Intel (ark.intel.com)
ARK ni hifadhidata rasmi ya maelezo ya bidhaa ya Intel katika ark.intel.com. Ni
hutoa maelezo ya kina ya kiufundi kwa kila Intel CPU, GPU, FPGA, na
Bidhaa ya NUC, pamoja na hesabu za msingi, kasi ya saa, TDP, aina za kumbukumbu zinazotumika,
na vipengele vya kuweka maelekezo. Unaposikia "angalia ARK kwa vipimo," inamaanisha
kutembelea hifadhidata hiyo kwa habari halali ya maunzi.
---

## Vigezo vya Utendaji wa AI
### MMLU (Uelewa Mkubwa wa Lugha wa Kazi nyingi)
MMLU ni kiwango cha kupima maarifa ya LLM katika masomo 57 ya kitaaluma yakiwemo
hisabati, historia, sheria, dawa, na sayansi ya kompyuta. Inajumuisha
maswali ya chaguo-nyingi yanayotokana na mitihani halisi ya ngazi ya chuo kikuu. Alama ya
70% ni takribani ngazi ya shahada ya kwanza ya binadamu; GPT-4 na Claude 3 alama zaidi ya 86%.
Alama za Phi-3-mini karibu 69% licha ya ukubwa wake mdogo.
###HumanEval
HumanEval ni kigezo cha OpenAI cha kutengeneza msimbo. Inajumuisha 164 Python
matatizo ya programu na kesi za mtihani otomatiki. Mifano hupimwa
pass@k - uwezekano kwamba angalau moja ya suluhu zinazozalishwa na k hupitisha zote
vipimo. Alama za GPT-4 ~87% (pasi@1); muundo wa 7B uliopangwa vizuri unaweza kufikia ~ 50-60%.
### HellaSwag
HellaSwag ni kipimo cha hoja za kawaida. Mifano hupewa sentensi
kuelezea shughuli ya kawaida na lazima uchague mwendelezo unaowezekana zaidi kutoka
chaguzi nne. Chaguzi zisizo sahihi zimeundwa mahsusi kuwa plausible lakini
hila vibaya. Inajaribu ikiwa mfano una uelewa wa msingi wa mwili
na hali za kijamii.
### ARC (Changamoto ya AI2 ya Kutoa Sababu)
ARC ni kigezo kutoka Taasisi ya Allen ya AI. Inajumuisha shule ya daraja
maswali ya sayansi, yamegawanywa katika seti za "Rahisi" na "Changamoto". Seti ya Changamoto
ina maswali ambayo mbinu kulingana na urejeshaji na miundo rahisi ya takwimu
mapambano na, yanayohitaji hoja za hatua nyingi.
---

## Dhana za Msingi za AI/ML
### RAG (Retrieval-Augmented Generation)
RAG ni mbinu inayochanganya mfumo wa kurejesha (kawaida vekta
hifadhidata) na modeli ya lugha. Badala ya kutegemea mfano tu
maarifa parametric, RAG kwanza inapata nyaraka muhimu kutoka nje
msingi wa maarifa na kisha kuwajumuisha katika muktadha wa mfano. Hii inaruhusu
mfano wa kujibu maswali kuhusu habari iliyosasishwa au mahususi ya kikoa
bila kujizoeza tena. Potato.ai hutumia aina ya RAG - inapata kutoka kwa KB yake
na inajumuisha matokeo katika muktadha kabla ya kutoa jibu.
### Urekebishaji mzuri
Urekebishaji mzuri ni mchakato wa kuendelea kutoa mafunzo kwa modeli iliyofunzwa mapema kwenye a
seti ndogo ya data, maalum ya kikoa. Hii inabadilisha uzani wa mfano kwa a
kazi fulani au kikoa. Kwa mfano, LLM ya msingi inaweza kusasishwa vizuri
rekodi za matibabu ili kuunda msaidizi wa Maswali na Majibu ya matibabu. Urekebishaji mzuri ni
gharama ya hesabu lakini nafuu zaidi kuliko mafunzo kutoka mwanzo.
### Ukadiriaji
Ukadiriaji hupunguza usahihi wa nambari wa uzani wa mfano (k.m. kutoka 32-bit
kuelea hadi nambari 4-bit). Hii inapunguza kwa kiasi kikubwa alama ya kumbukumbu - mfano wa 7B
kwa usahihi wa biti-16 inahitaji ~ 14GB VRAM; mfano sawa katika 4-bit (umbizo la GGUF)
inahitaji ~4GB. Ukadiriaji kwa kawaida husababisha usahihi mdogo lakini unaokubalika
uharibifu na ndio mbinu kuu inayowezesha miundo mikubwa kuendeshwa kwa watumiaji
vifaa au hata vifaa vya rununu.
### Dirisha la Muktadha
Dirisha la muktadha ni idadi ya juu ya ishara ambazo mtindo unaweza kusindika mara moja,
ikijumuisha majibu ya haraka na yanayotokana. GPT-3.5 ilikuwa na ishara 4,096
dirisha; GPT-4 Turbo na Claude 3 inasaidia tokeni 128,000; Gemini 1.5 Pro
inasaidia tokeni 1,000,000. Dirisha kubwa la muktadha huruhusu mtindo "kuona"
zaidi ya mazungumzo au hati mara moja, kuboresha uwiano kwa muda mrefu
kubadilishana.
### RLHF (Kuimarisha Mafunzo kutoka kwa Maoni ya Binadamu)
RLHF ni mbinu ya mafunzo inayobadilisha modeli ya lugha ya msingi (ambayo
inatabiri tu ishara inayofuata) kuwa msaidizi anayefuata maagizo na
kutenda kwa manufaa. Wakadiriaji wa viwango vya binadamu hupata matokeo ya mfano, mfano wa zawadi umefunzwa
kwa upendeleo wao, na mtindo wa lugha basi huboreshwa dhidi ya hii
mfano wa malipo kwa kutumia ujifunzaji wa kuimarisha. ChatGPT, Claude, na Gemini zote hutumia
lahaja za RLHF au mbinu sawa za upatanishi (k.m. AI ya Kikatiba,
Uboreshaji wa Upendeleo wa Moja kwa moja).
### Usanifu wa Transfoma
Transformer ni usanifu wa mtandao wa neva unaozingatia LLM zote za kisasa.
Ilianzishwa katika karatasi ya 2017 "Makini Ndio Wote Unayohitaji" na Vaswani et al., it
hutumia njia za kujiangalia kuchakata tokeni zote sambamba badala ya
mfululizo. Vibadilishaji Visimbaji pekee (BERT) vinatumika kuelewa kazi;
Vibadilishaji vya dekoda pekee (GPT, Llama, Mistral) hutumiwa kwa kazi za kizazi;
Vibadilishaji vya kusimbuaji-kisimbaji (T5, BART) hutumika kwa tafsiri na muhtasari.
### Upachikaji na Hifadhidata za Vekta
Upachikaji ni uwakilishi mnene wa nambari za maandishi (au picha) zinazotolewa na
mtandao wa neva. Maandishi yanayofanana kisemantiki yana upachikaji ambao upo karibu
nafasi ya vekta. Hifadhidata za Vekta (ChromaDB, Pinecone, Weaviate, Qdrant) duka
upachikaji huu na kuauni utafutaji wa haraka wa takriban wa karibu zaidi. Wao ni
uti wa mgongo wa uhifadhi wa mifumo ya RAG, ikijumuisha safu ya kumbukumbu baridi ya Potato.ai.