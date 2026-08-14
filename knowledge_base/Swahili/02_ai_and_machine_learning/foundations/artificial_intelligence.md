<!--
---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
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
tags: [artificial, intelligence, ai-and-machine-learning]
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
# Akili Bandia
Akili ya Bandia ni jaribio la kuunda mashine zinazoweza kufanya mambo ambayo yangehitaji akili ikiwa mwanadamu angeyafanya: kutambua nyuso, kuelewa usemi, kufanya maamuzi, kuandika maandishi, kucheza michezo, kuendesha magari, kutambua magonjwa. Sehemu ni ya zamani kama kompyuta yenyewe - Alan Turing alikuwa akiuliza "Je, mashine zinaweza kufikiria?" mnamo 1950 - lakini mlipuko wa hivi karibuni wa uwezo (miaka ya 2020) umefanya AI kuwa moja ya teknolojia muhimu na iliyoshindaniwa katika historia ya mwanadamu.
---

## Historia Fupi
AI imepitia mizunguko ya hype na tamaa kwa miongo kadhaa. Kuelewa historia hii hukusaidia kuelewa ni kwa nini watu wanachangamka na wana shaka.
| Enzi | Nini Kilitokea | Matokeo |
|-----|---------------|----------|
| **Miaka ya 1950-1960** | Matumaini ya mapema. Mtihani wa Turing ulipendekezwa (1950). Sarafu za Mkutano wa Dartmouth "Akili ya Bandia" (1956). Mipango ya awali kama vile ELIZA (chatbot) na SHRDLU (uelewa wa lugha). | Msisimko: "Tutakuwa na AGI katika kizazi!" |
| **Miaka ya 1970** | Majira ya baridi ya kwanza ya AI. Mapungufu ya mbinu za mapema huwa wazi. Ufadhili unakauka. | Kukatishwa tamaa: ahadi ambazo hazijatimizwa |
| **Miaka ya 1980** | Mifumo ya kitaalam inaongezeka - programu zinazotegemea sheria ambazo zilisimba maarifa ya kitaalam ya wanadamu. Mradi wa Kizazi cha Tano wa Japan. | Msisimko tena: uwekezaji wa ushirika wa AI |
| **1987-1993** | Majira ya baridi ya AI ya pili. Mifumo ya wataalam inathibitisha kuwa brittle na gharama kubwa kudumisha. | Kukata tamaa tena |
| **Miaka ya 2000** | Kujifunza kwa mashine kunapata nguvu. Data zaidi inapatikana (mtandao). Mbinu za takwimu hubadilisha sheria zilizowekwa kwa mkono. | Maendeleo thabiti |
| **2012+** | Mapinduzi ya kujifunza kwa kina. AlexNet inashinda shindano la ImageNet kwa kutumia GPU. Mitandao ya neva huanza kufanya vyema zaidi mbinu za kimapokeo kwenye maono, usemi na lugha. | Mabadiliko ya haraka |
| **2017** | Karatasi ya "Tahadhari Ndio Wote Unaohitaji" inatanguliza usanifu wa Transfoma. | Msingi wa kila kitu kinachofuata |
| **2020-2026** | Mifano kubwa ya lugha (GPT-3, GPT-4, Claude, Gemini, LLaMA). AI inazalisha maandishi, msimbo, picha, video. Kupitishwa kwa biashara kunaharakisha. | AI inakuwa sehemu ya maisha ya kila siku |
---

## Jinsi AI ya Kisasa Inavyofanya Kazi
### Kujifunza kwa Mashine — Kujifunza kutoka kwa Data
Badala ya kuweka sheria wazi za programu, kujifunza kwa mashine hulisha data kwa algoriti zinazopata ruwaza zenyewe.
| Aina | Jinsi Inavyofanya Kazi | Mfano |
|------|-------------|----------|
| **Mafunzo yanayosimamiwa** | Treni juu ya mifano iliyo na lebo (ingizo → pato sahihi) | Ugunduzi wa barua taka: lipe maelfu ya barua pepe zilizoandikwa "spam" au "sio barua taka" |
| **Kujifunza bila kusimamiwa** | Tafuta ruwaza katika data isiyo na lebo | Mgawanyiko wa wateja: panga wateja sawa bila kufafanua mapema vikundi |
| **Kujifunza kuimarisha ** | Wakala hujifunza kwa kujaribu na makosa, kupokea thawabu au adhabu | AI ya kucheza mchezo: jaribu hatua, pata pointi za kushinda, jifunze mikakati inayofanya kazi |
### Kujifunza kwa Kina — Mitandao ya Neural
Kujifunza kwa kina hutumia mitandao ya neva bandia - safu za shughuli rahisi za hisabati ambazo, zikiwa zimepangwa pamoja, zinaweza kujifunza ruwaza changamano sana. "Kina" inahusu idadi ya tabaka.
Usanifu muhimu:
| Usanifu | Bora Kwa | Matumizi Halisi ya Ulimwengu |
|----------------------------------------|
| **CNN** (Mtandao wa Mabadiliko ya Neural) | Picha na data ya anga | Utambuzi wa uso, picha za matibabu, magari yanayojiendesha |
| **RNN/LSTM** | Data mfuatano (msururu wa saa) | Utambuzi wa usemi, kizazi cha muziki (kinachobadilishwa kwa kiasi kikubwa na Transfoma) |
| **Kibadilishaji** | Kila kitu - maandishi, picha, sauti, msimbo | GPT, Claude, Gemini, BERT, DALL-E - usanifu mkuu |
| **GAN** (Generative Adversarial Network) | Inazalisha data ya kweli | Usanisi wa picha, uhamishaji wa mitindo (imebadilishwa kwa sehemu na mifano ya uenezaji) |
| **Miundo ya uenezi** | Uzalishaji wa ubora wa picha/video | Usambazaji Imara, DALL-E 3, Midjourney, Sora |
### Miundo Kubwa ya Lugha (LLMs)
LLM ni miundo inayotegemea Transfoma iliyofunzwa juu ya idadi kubwa ya maandishi. Wanajifunza kutabiri ishara inayofuata (kipande cha neno) katika mlolongo, ambayo inageuka kuhitaji kuelewa sarufi, ukweli, hoja, na hata kitu kinachofanana na "maarifa."
| Mfano | Msanidi | Kipengele Mashuhuri |
|-------|-----------|-----------------|
| **GPT-4 / GPT-4o** | OpenAI | Multimodal (maandishi + picha); hoja kali |
| **Claude** | Anthropic | Kuzingatia usalama na usaidizi; madirisha ya muktadha mrefu |
| **Gemini** | Google DeepMind | Natively multimodal; imeunganishwa na huduma za Google |
| **LLaMA / Llama 3** | Meta | Uzito wazi; inaweza kuendeshwa ndani ya nchi; jamii kubwa |
| **Mistral** | Mistral AI | Mitindo ya wazi yenye ufanisi inayoshindana na kubwa zaidi |
**Mchakato wa mafunzo**:
1. **Mafunzo ya awali**: Jifunze kutokana na data kubwa ya maandishi (kutabiri ishara zinazofuata). Hapa ndipo mfano hupata "maarifa."
2. **Urekebishaji mzuri**: Jifunze kuhusu kazi maalum au upendeleo wa kibinadamu.
3. **RLHF** (Kuimarisha Mafunzo kutoka kwa Maoni ya Binadamu): Wanadamu wanakadiria matokeo ya modeli; mtindo hujifunza kutoa matokeo ambayo wanadamu wanapendelea.
**Madirisha ya muktadha** (muda wa maandishi ambao muundo unaweza kuchakata mara moja) yameongezeka kutoka tokeni za 4K (GPT-3 ya awali) hadi zaidi ya tokeni milioni 1 katika miundo ya 2026.
---

## Kile AI Inaweza na Siwezi Kufanya
### Uwezo wa Sasa
| Kazi | Utendaji | Mapungufu |
|------|-------------|-------------|
| **Kizazi cha maandishi** | Bora zaidi - thabiti, kimuktadha, tofauti za kimtindo | Inaweza kushawishi (kutoa habari za uwongo kwa ujasiri) |
| **Uzalishaji wa kanuni** | Nzuri sana kwa mifumo ya kawaida; unaweza kuandika programu nzima | Mapambano na usanifu wa riwaya; inaweza kuanzisha hila hila |
| **Kizazi cha picha** | Photorealistic; mitindo ya kisanii; kuhariri | Mikono na maandishi bado hayajakamilika; mapambano na hoja sahihi za anga |
| **Tafsiri** | Karibu na binadamu kwa jozi kuu za lugha | Lugha za rasilimali chache zisizo sahihi; nuance ya kitamaduni inaweza kupotea |
| **Utambuzi wa usemi** | Karibu na binadamu katika sauti safi | Mapambano na lafudhi nzito, kelele ya mandharinyuma |
| **Kujadili** | Kuboresha haraka; inaweza kutatua matatizo mengi ya kimantiki | Hushindwa katika masuala ya riwaya yanayohitaji uelewa wa kweli |
| **Hisabati** | Nzuri katika matatizo ya kawaida | Hufanya makosa kwenye uthibitisho wa riwaya; sio mbadala wa uthibitishaji rasmi |
| **Kupanga na kutumia zana** | Wanaojitokeza (mawakala) | Bado siwezi kutegemewa kwa kazi ngumu za hatua nyingi bila uangalizi wa kibinadamu |
### Kile AI Siwezi Kufanya (kuanzia 2026)
- **Kweli kuelewa** jambo lolote katika jinsi wanadamu wanavyofanya - linachakata mifumo, sio maana
- **Dhakikisha usahihi wa ukweli** — kuona maono bado ni tatizo ambalo halijatatuliwa
- **Badilisha hukumu ya binadamu** katika maamuzi ya hali ya juu bila uangalizi
- **Weka jumla kikamilifu** kwa vikoa tofauti sana na data ya mafunzo
- **Fanya kazi kwa uhuru** katika mazingira ya kimwili yasiyotabirika (roboti bado ni ngumu)
---

## Maadili na Usalama wa AI
AI sio upande wowote. Inaonyesha data ambayo ilifunzwa, chaguo za wasanidi wake, na motisha ya mashirika yanayoitumia.
### Mambo Muhimu
| Suala | Nini Kinatokea | Mfano |
|-------|-------------|----------|
| **Upendeleo** | Mifumo ya AI huzalisha na kukuza upendeleo katika data ya mafunzo | Kukodisha algorithms kupendelea wagombea wa kiume; utambuzi wa uso na viwango vya juu vya makosa kwa ngozi nyeusi |
| **Faragha** | AI iliyofunzwa kwenye data ya kibinafsi; uwezo wa ufuatiliaji | Mafunzo juu ya kazi zilizo na hakimiliki; utambuzi wa uso katika maeneo ya umma |
| **Matumizi mabaya** | Deepfakes, disinformation, hadaa otomatiki | Video ghushi zinazozalishwa na AI za wanasiasa; simu za kashfa za kiotomatiki |
| **Uhamisho wa kazi** | Uendeshaji wa kazi zilizofanywa hapo awali na wanadamu | Uundaji wa maudhui, huduma kwa wateja, ingizo la data, baadhi ya programu |
| **Mpangilio** | Kuhakikisha malengo ya AI yanalingana na maadili ya binadamu | AI iliyoambiwa "kuongeza uzalishaji wa karatasi" inaweza kubadilisha vitu vyote kuwa vipande vya karatasi |
| **Hatari iliyopo** | Wasiwasi wa kinadharia kuhusu AGI ya baadaye | Mjadala kati ya watafiti - wengine wanaona kuwa wa dharura, wengine kama wa mapema |
### Nani Anashughulikia Usalama
- **Anthropic** - iliyoanzishwa na watafiti wa zamani wa OpenAI ililenga hasa usalama wa AI
- **DeepMind Safety** - timu ya watafiti ndani ya Google DeepMind
- **MIRI** (Taasisi ya Utafiti wa Ujasusi wa Mashine) — utafiti wa usalama wa kinadharia
- **ARC** (Kituo cha Utafiti cha AI) — utafiti wa usalama wa majaribio
- **Miili ya serikali** - Sheria ya EU AI (2026), maagizo ya utendaji ya Marekani, mifumo ya kimataifa
---

## AI Katika Mazoezi - Sekta kwa Viwanda
| Viwanda | Maombi | Ukomavu |
|----------|------------------------|
| **Huduma za afya** | Utambuzi wa saratani kutoka kwa picha; ugunduzi wa madawa ya kulevya (AlphaFold); kutabiri matokeo ya mgonjwa | Imesambazwa na kupanuliwa |
| **Fedha** | Utambuzi wa ulaghai, biashara ya algoriti, alama za mkopo, washauri wa robo | Imesambazwa kwa wingi |
| **Usafiri** | Magari ya kujiendesha (Waymo, Tesla Autopilot); uboreshaji wa njia | Imetumwa kwa sehemu; uhuru kamili bado mdogo |
| **Elimu** | Kujifunza kwa kibinafsi; Mafunzo ya AI; uwekaji daraja otomatiki | Inakua kwa kasi |
| **Nga za ubunifu** | Kizazi cha picha (Midjourney, DALL-E); muziki; usaidizi wa kuandika; kukamilika kwa nambari | Kubadilisha mtiririko wa kazi sasa |
| **Usalama mtandao** | Utambuzi wa tishio; kitambulisho kisicho sawa; mashambulizi na ulinzi | Mbio za silaha zinaendelea |
| **Kisheria** | Uchambuzi wa mikataba; ukaguzi wa hati; utafiti wa kisheria | Kupitishwa; masuala ya usahihi |
| **Kilimo** | Ufuatiliaji wa mazao kupitia satelaiti/drone; kunyunyizia kwa usahihi; utabiri wa mavuno | Kukua |
| **Utengenezaji** | ukaguzi wa ubora; matengenezo ya utabiri; uboreshaji wa mnyororo wa usambazaji | Imesambazwa kwa wingi |
---

## Roboti na Iliyojumuishwa AI
Roboti inachanganya AI na mashine za kimwili. Licha ya miongo kadhaa ya maendeleo, mwingiliano wa kimwili na ulimwengu unasalia kuwa mgumu zaidi kuliko akili ya kidijitali.
- **Atlasi ya Boston Dynamics'** - harakati ya hali ya juu ya miguu miwili; parkour; kazi za ghala
- **Roboti za viwandani** (ABB, FANUC, KUKA) — tengeneza utengenezaji kiotomatiki; kulehemu; mkusanyiko
- **Roboti za upasuaji** (Mfumo wa da Vinci) - upasuaji usiovamizi kwa usahihi zaidi ya mikono ya binadamu
- **Roboti za nyumbani** (Roomba) — rahisi lakini zimefanikiwa kibiashara
- ** robots za Humanoid ** (Tesla Optimus, Kielelezo AI) - zinazojitokeza; kazi za kimwili za kusudi la jumla bado ni ngumu sana
Pengo kati ya AI ya kidijitali (ambayo imepata maendeleo makubwa) na AI ya kimwili (ambayo inapambana na ustadi, usawaziko, na mazingira yasiyotabirika) ni mojawapo ya changamoto kubwa za nyanja hiyo.
---

## Mitindo ya Sasa (2020)
| Mitindo | Nini Kinatokea |
|-------|-------------------|
| **Multimodal AI** | Mifumo inayochakata maandishi, picha, sauti na video pamoja (GPT-4V, Gemini) |
| **Mawakala** | LLM zinazoweza kutumia zana, kuvinjari wavuti, kuandika msimbo, na kuchukua hatua za hatua nyingi |
| **Miundo ya uzani huria** | LLaMA ya Meta na zingine zinazoweka kidemokrasia ufikiaji wa aina kubwa |
| **Kwenye kifaa AI** | Miundo inayoendesha ndani ya nchi kwenye simu na kompyuta ndogo (Apple Intelligence, Qualcomm NPUs) |
| **Udhibiti wa AI** | Sheria ya AI ya EU (2026) - sheria ya kwanza ya kina ya AI; kuainisha mifumo kwa kiwango cha hatari |
| **AI katika sayansi** | Kukunja protini (AlphaFold), ugunduzi wa nyenzo, muundo wa hali ya hewa, uthibitisho wa hisabati |
| **Miundo ya lugha ndogo** | Mifano ya ufanisi inayoendesha vifaa vya watumiaji; ubora inakaribia mifano kubwa |
---

## Muhtasari
AI ndio maendeleo muhimu zaidi ya teknolojia ya karne ya 21 hadi sasa. Sio uchawi - ni ulinganifu wa muundo kwa kiwango, unaowezeshwa na data kubwa, maunzi yenye nguvu, na usanifu mahiri. Kinachoifanya iwe mageuzi ni kwamba ulinganishaji wa muundo, unaofanywa vizuri vya kutosha, unaweza kuiga kazi nyingi ambazo hapo awali zilihitaji akili ya mwanadamu. Changamoto ni muhimu vile vile: kuona ndoto, upendeleo, uhamisho wa kazi, matumizi mabaya, na swali la wazi la kama njia kutoka kwa AI nyembamba hadi kwa akili ya jumla ni fupi au ndefu isiyowezekana. Kilicho wazi ni kwamba AI itaunda upya kila tasnia, kila taaluma, na kila nyanja ya maisha ya kila siku. Kuelewa jinsi inavyofanya kazi - na kile ambacho haiwezi kufanya - ni muhimu kwa kuabiri ulimwengu tunaounda.