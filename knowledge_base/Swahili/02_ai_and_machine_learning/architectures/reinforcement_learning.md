<!--
---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [reinforcement, learning, ai-and-machine-learning]
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

-->
# Kuimarisha Mafunzo
Kujifunza kwa kuimarisha (RL) ni jinsi mashine hujifunza kufanya mfuatano wa maamuzi kwa majaribio na makosa. Tofauti na mafunzo yanayosimamiwa, ambapo jibu sahihi hutolewa kwa kila mfano, RL humpa wakala ishara ya zawadi pekee - na wakala lazima atambue ni hatua gani zitakazoleta matokeo bora zaidi kwa wakati. Ni mbinu nyuma ya AlphaGo, udhibiti wa roboti, AI ya kucheza mchezo, na - kwa umakinifu - RLHF, mbinu inayotumiwa kuoanisha miundo ya kisasa ya lugha kubwa na mapendeleo ya wanadamu.
---

## Dhana za Msingi
RL inaweka ufanyaji maamuzi kama kitanzi kati ya **wakala** na **mazingira**.
| Sehemu | Jukumu | Mfano |
|-----------|------|---------|
| **Wakala** | Mwenye maamuzi | Mpango wa chess, roboti, mtindo wa lugha |
| **Mazingira** | Ulimwengu wakala hutangamana na | Ubao wa chess, ghala, mazungumzo |
| **Jimbo** | Hali ya sasa | Nafasi ya ubao, usomaji wa kihisi cha roboti, historia ya gumzo |
| **Kitendo** | Nini wakala anaweza kufanya | Sogeza kipande, pinduka kushoto, toa ishara |
| **Tuzo** | Maoni ya ishara (nambari ya scalar) | +1 kwa kushinda, -1 kwa kushindwa, alama ya upendeleo wa binadamu |
| **Sera** | Mkakati wa kuchora majimbo kwa vitendo | "Ikiwa mfalme anatishiwa, isogeze" |
| **Kitendaji cha thamani** | Zawadi ya jumlishi inayotarajiwa kutoka kwa jimbo | "Nafasi hii ya ubao ina thamani ya takriban pointi +3" |
### Kitanzi cha RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Lengo la wakala ni kuongeza **zawadi iliyolimbikizwa** baada ya muda, si tu zawadi ya papo hapo. Hili ndilo linalofanya RL kuwa tofauti kabisa na ujifunzaji unaosimamiwa.
---

## Tofauti Muhimu kutoka kwa Vigezo Vingine vya Kujifunza
| Kipengele | Mafunzo Yanayosimamiwa | Kujifunza Bila Kusimamiwa | Mafunzo ya Kuimarisha |
|--------|--------------------------------------------------------------|
| **Ishara** | Lebo sahihi kwa kila mfano | Hakuna lebo; Tafuta muundo | Tuzo ya Scalar, mara nyingi hucheleweshwa |
| **Maoni** | Mara moja | Hakuna | Imechelewa na chache |
| **Msururu** | Kila mfano ni huru | Kila mfano ni huru | Vitendo huathiri majimbo yajayo |
| **Lengo** | Punguza hitilafu ya utabiri | Gundua mifumo | Ongeza zawadi limbikizo |
---

## Mchakato wa Maamuzi ya Markov (MDPs)
MDPs ni mfumo wa hisabati wa RL. Wanafikiria siku zijazo inategemea tu hali ya sasa, sio historia ya jinsi ulivyofika (*mali ya Markov**).
| Sehemu | Nukuu | Maana |
|-----------|----------|----------|
| **Majimbo** | S | Hali zote zinazowezekana wakala anaweza kuwa |
| **Vitendo** | A | Mambo yote ambayo wakala anaweza kufanya |
| **Kitendaji cha mpito** | P(s' \| s, a) | Uwezekano wa kufikia hali s' baada ya kuchukua hatua katika hali s |
| **Kazi ya zawadi** | R(s, a, s') | Zawadi imepokelewa kwa mabadiliko |
| **Kipengele cha punguzo** | γ (gamma) | Kiasi gani cha kuthamini zawadi za siku zijazo dhidi ya za sasa hivi (0 hadi 1) |
**rejesho** (jumla ya zawadi iliyopunguzwa) ni:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Kipengele cha punguzo la juu (γ karibu na 1) inamaanisha kuwa wakala ana maono ya mbali. Mtu wa chini anamaanisha kuwa hana macho.
---

## Kanuni za Kawaida za RL
### Mbinu Zinazozingatia Thamani
Hizi hujifunza jinsi kila jimbo (au jozi ya hatua ya serikali) ilivyo nzuri.
| Algorithm | Wazo Muhimu | Kizuizi |
|-----------|----------|------------|
| **Q-Kujifunza** | Jifunze jedwali la maadili ya Q: Q(hali, hatua) = zawadi inayotarajiwa | Hailingani na nafasi kubwa za serikali |
| **Mtandao wa Q-Kina (DQN)** | Tumia mtandao wa neva kukadiria thamani za Q | Hushughulikia tu vitendo vya kipekee; inaweza kutokuwa thabiti |
| **DQN Mbili** | Rekebisha upendeleo wa kukadiria kupita kiasi wa Q-kujifunza | Bado ni mdogo kwa vitendo tofauti |
Sheria ya kusasisha mafunzo ya Q:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Mbinu Zinazotegemea Sera
Hawa hujifunza sera (mkakati) moja kwa moja bila kukadiria maadili.
| Algorithm | Wazo Muhimu | Faida |
|-----------|----------|-----------|
| **IMARISHA** | gradient ya sera ya Monte Carlo; sasisha sera katika mwelekeo wa matokeo mazuri | Rahisi; inafanya kazi kwa vitendo mfululizo |
| **PPO** (Uboreshaji wa Sera ya Karibu) | Klipu ya masasisho ya sera ili kuzuia mabadiliko makubwa na ya kuleta utulivu | Imara; kutumika sana; chaguo-msingi nzuri |
| **TRPO** | Mbinu ya eneo la imani kwa masasisho ya sera | Kanuni zaidi kuliko PPO; ngumu zaidi kutekeleza |
### Mbinu za Ukosoaji wa Mwigizaji
Changanya bora kati ya zote mbili: ** mwigizaji** (sera) na **mkosoaji** (utendaji wa thamani).
| Algorithm | Wazo Muhimu |
|-----------|----------|
| **A2C / A3C** | Faida Mwigizaji-Mkosoaji; hutumia ukadiriaji wa faida kupunguza tofauti |
| **SAC** (Mkosoaji Mpole) | Ongeza zawadi huku ukidumisha uchunguzi (udhibiti wa entropy) |
| **TD3** (Pacha Imechelewa DDPG) | Shughulikia makadirio ya kupita kiasi katika nafasi za vitendo zinazoendelea |
---

## RLHF: Kuimarisha Mafunzo kutoka kwa Maoni ya Binadamu
RLHF ndiyo mbinu iliyowezesha ChatGPT. Inaweka pengo kati ya modeli inayoweza kutabiri maandishi na ile inayotoa matokeo ambayo wanadamu hupata msaada.
### Hatua Tatu
| Hatua | Nini Kinatokea | Pato |
|------|-------------|---------|
| **1. Urekebishaji Uzuri Unaosimamiwa (SFT)** | Boresha muundo uliofunzwa mapema juu ya mifano ya hali ya juu iliyoandikwa na binadamu | Mfano unaofuata maagizo vizuri |
| **2. Mafunzo ya Mfano wa Zawadi** | Wanadamu hulinganisha jozi za matokeo ya mfano; fundisha mtindo wa kutabiri mapendeleo ya wanadamu | Muundo wa zawadi unaopata ubora wa matokeo |
| **3. Uboreshaji wa RL** | Tumia PPO kusawazisha muundo wa SFT ili kuongeza alama za muundo wa zawadi | Mfano unaoendana na matakwa ya binadamu |
### Kwa Nini RLHF Ni Muhimu
Bila RLHF, mtindo wa lugha ni kama mwanafunzi ambaye amesoma kila kitabu lakini hajui jinsi ya kuishi katika mazungumzo. Inaweza kutoa maandishi, lakini maandishi yanaweza kuwa yasiyofaa, sumu, au kukosa uhakika kabisa. RLHF inafundisha modeli *kile binadamu wanataka* — si tu jinsi maandishi yanavyoonekana.
### Vibadala na Vibadala
| Mbinu | Maelezo | Faida |
|--------|-------------|-----------|
| **DPO** (Uboreshaji wa Mapendeleo ya Moja kwa Moja) | Ruka mfano wa malipo; boresha sera moja kwa moja kutoka kwa mapendeleo ya binadamu | Rahisi zaidi; hakuna mfano tofauti wa malipo wa kutoa mafunzo |
| **RLAIF** | Tumia AI (badala ya wanadamu) kutengeneza lebo za upendeleo | Nafuu kuliko kuweka lebo kwa binadamu |
| **Kikatiba AI** | Tumia seti ya kanuni kuongoza tabia ya kielelezo bila lebo za kibinadamu | Zaidi scalable; Mbinu ya Anthropic |
| **GRPO** (Uboreshaji wa Sera Husika ya Kundi) | Linganisha matokeo ndani ya kikundi badala ya dhidi ya mtindo tofauti | Inatumika katika DeepSeek-R1; inapunguza hitaji la mtandao wa thamani |
---

## Ugunduzi dhidi ya Unyonyaji
Huu ni mvutano wa kati katika RL. **Unyonyaji** unamaanisha kuchagua vitendo unavyojua hufanya kazi vizuri. **Ugunduzi** unamaanisha kujaribu vitu vipya ili kugundua mbinu bora zaidi.
| Mkakati | Jinsi Inavyofanya Kazi | Biashara |
|----------|-------------------------|
| **ε-choyo** | Chagua kitendo bora zaidi wakati mwingi; kitendo nasibu chenye uwezekano ε | Rahisi lakini isiyofaa |
| **Uchunguzi wa Boltzmann** | Chagua vitendo kwa uwezekano kulingana na thamani zao zilizokadiriwa | Laini kuliko ε-choyo |
| **UCB** (Upper Confidence Bound) | Pendelea vitendo vyenye kutokuwa na uhakika wa hali ya juu (matumaini katika uso wa kutokuwa na uhakika) | Dhamana nzuri za kinadharia |
| **Udhibiti wa entropy** | Ongeza bonasi kwa kutembelea majimbo mbalimbali (inatumika katika SAC, PPO) | Inahimiza uchunguzi wa asili |
---

## Masomo ya Uimarishaji wa Wakala Mbalimbali
Wakati mawakala wengi hujifunza kwa wakati mmoja, mienendo inakuwa ngumu zaidi.
| Hali | Changamoto | Mfano |
|----------|-----------|----------|
| **Ushirika** | Mawakala lazima waratibu; kazi ya mkopo ni ngumu | timu za mpira wa roboti; mitandao ya kihisi iliyosambazwa |
| **Ushindani** | Wapinzani kukabiliana; mazingira si ya stationary | Mchezo AI (poker, Starcraft); usalama wa mtandao |
| **Mchanganyiko** | Baadhi ya mawakala hushirikiana, wengine hushindana | Masoko ya mnada; mifumo ya trafiki |
| Algorithm | Maelezo |
|-----------|-------------|
| **MADDPG** | Toleo la wakala mbalimbali la DDPG; mkosoaji mkuu, waigizaji waliogatuliwa |
| **MAPPO** | PPO ya wakala mbalimbali; kutumika sana katika mazoezi |
| **Jicheze** | Mawakala hufanya mazoezi dhidi ya nakala zao (AlphaGo, AlphaStar) |
---

## Uhamisho wa Sim-hadi-Halisi
Kufundisha roboti katika ulimwengu wa kweli ni polepole na hatari. Badala yake, mawakala hufunza katika uigaji na kuhamisha kwa ukweli.
| Changamoto | Suluhisho |
|-----------|----------|
| **Pengo la ukweli** (kuiga ≠ ulimwengu halisi) | Ubadilishaji wa kikoa: badilisha vigezo vya fizikia wakati wa mafunzo |
| **Uzembe wa mfano** | Tumia RL kulingana na muundo au treni kwenye uigaji mkubwa sambamba |
| **Usalama** | RL iliyozuiliwa: toa adhabu kwa vitendo visivyo salama wakati wa mafunzo |
| **Kuzingatiwa kwa sehemu** | Treni yenye vihisi kelele na uchunguzi uliochelewa |
Kampuni kama vile Boston Dynamics na Tesla hutumia uigaji kwa kiasi kikubwa, lakini pengo kati ya utendakazi ulioigizwa na wa kimwili unasalia kuwa mojawapo ya changamoto kubwa zaidi katika nyanja hii.
---

## Zana na Mifumo
| Zana | Kusudi | Bora Kwa |
|------|---------------------|
| **Misingi-Imara3** | Safisha Python utekelezaji wa PPO, SAC, TD3, DQN | Kujifunza na prototyping |
| **RLlib** | Maktaba ya Scalable RL iliyojengwa juu ya Ray | Mafunzo yaliyosambazwa kwa kiasi kikubwa |
| **SafiRL** | Utekelezaji wa faili moja kwa utafiti | Kuelewa algorithms kwa undani |
| **Gymnasium (OpenAI)** | Kiolesura sanifu cha mazingira | Kufafanua matatizo ya RL |
| **Gym ya Isaac / Isaac Lab** | Uigaji wa fizikia unaoharakishwa na GPU | Roboti, sim-to-halisi |
| **TRL** (Maktaba ya Transformer RL) | RLHF, DPO, PPO kwa miundo ya lugha | Kupanga LLM |
| **FunguaRLHF** | Mfumo wa RLHF uliosambazwa | Kufundisha mifano mikubwa na RLHF |
---

## Vidokezo Vitendo
- **Anza na PPO.** Ni algoriti inayotegemewa zaidi ya madhumuni ya jumla. Ikiwa huna uhakika wa kutumia, PPO ndiyo chaguomsingi.
- **Rekebisha zawadi zako.** Kuongeza zawadi huathiri sana uthabiti wa mafunzo.
- **Tumia mazingira yaliyo na vekta.** Kuendesha mazingira mengi sawia (k.m., 8–64) huimarisha makadirio ya upinde rangi na kuongeza kasi ya mafunzo kwa kiasi kikubwa.
- **Fuatilia zawadi na entropy.** Entropy ikishuka hadi sifuri, wakala wako ameacha kuchunguza na anaweza kukwama katika kiwango bora cha ndani.
- **Uundaji wa zawadi ni sanaa.** Kubuni utendakazi sahihi wa zawadi mara nyingi ndilo jambo gumu zaidi. Zawadi chache (mwisho tu) hufanya kujifunza kuwa polepole sana. Zawadi nyingi na zenye umbo zuri huongoza wakala lakini zinaweza kutambulisha tabia isiyotarajiwa.
- **RLHF ni tete.** Mabadiliko madogo kwenye muundo wa zawadi au vigezo vya PPO vinaweza kusababisha kushuka kwa ubora mkubwa. DPO ni mbadala thabiti zaidi ikiwa hauitaji bomba kamili la RLHF.
---

## Muhtasari
Kujifunza kwa uimarishaji ni utafiti wa jinsi mawakala hujifunza kufanya maamuzi kupitia mwingiliano. Inaanzia katika algoriti za kitamaduni kama vile mafunzo ya Q hadi mbinu za kisasa za kina za RL kama vile PPO na SAC, na inasisitiza baadhi ya maendeleo muhimu ya hivi majuzi katika AI - kutoka kucheza mchezo hadi upangaji wa modeli ya lugha. Changamoto kuu inasalia kuwa ile ile: unawezaje kujifunza tabia bora wakati maoni yanapochelewa, machache, na kelele? Jibu - jaribio na hitilafu, likiongozwa na hisabati wajanja - linageuka kuwa mojawapo ya mawazo yenye nguvu zaidi katika akili zote za bandia.