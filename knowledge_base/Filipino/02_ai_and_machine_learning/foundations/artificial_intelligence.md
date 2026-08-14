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
# Artipisyal na Katalinuhan
Ang artificial intelligence ay ang pagtatangka na bumuo ng mga makina na maaaring gumawa ng mga bagay na mangangailangan ng katalinuhan kung ang isang tao ay gumawa ng mga ito: makilala ang mga mukha, maunawaan ang pananalita, gumawa ng mga desisyon, magsulat ng teksto, maglaro, magmaneho ng mga kotse, mag-diagnose ng mga sakit. Ang field ay kasingtanda ng pag-compute mismo — nagtatanong si Alan Turing ng "Maaari bang mag-isip ang mga makina?" noong 1950 — ngunit ang kamakailang pagsabog sa kakayahan (2020s) ay ginawa ang AI na isa sa pinakamahalaga at pinagtatalunang teknolohiya sa kasaysayan ng tao.
---

## Isang Maikling Kasaysayan
Ang AI ay dumaan sa mga siklo ng hype at pagkabigo sa loob ng mga dekada. Ang pag-unawa sa kasaysayang ito ay nakakatulong sa iyo na maunawaan kung bakit ang mga tao ay parehong nasasabik at nag-aalinlangan.
| Era | Ano ang Nangyari | Kinalabasan |
|-----|----------------|---------|
| **1950s-1960s** | Maagang optimismo. Iminungkahi ang Turing Test (1950). Mga barya ng Dartmouth Conference na "Artificial Intelligence" (1956). Mga naunang programa tulad ng ELIZA (chatbot) at SHRDLU (pag-unawa sa wika). | Excitement: "Magkakaroon tayo ng AGI sa isang henerasyon!" |
| **1970s** | Unang AI taglamig. Ang mga limitasyon ng maagang paglapit ay nagiging malinaw. Natutuyo ang pondo. | Pagkadismaya: mga pangakong hindi natupad |
| **1980s** | Expert systems boom — mga programang nakabatay sa panuntunan na nag-encode ng kaalaman sa espesyalista ng tao. Proyekto ng Fifth Generation ng Japan. | Agaw muli: corporate AI investments |
| **1987-1993** | Pangalawang taglamig ng AI. Ang mga ekspertong sistema ay nagpapatunay na malutong at mahal upang mapanatili. | Pagkadismaya muli |
| **2000s** | Nakakakuha ng traksyon ang machine learning. Higit pang data na magagamit (internet). Pinapalitan ng mga istatistikal na pamamaraan ang mga panuntunang naka-code sa kamay. | Panay na pag-unlad |
| **2012+** | Malalim na rebolusyon sa pag-aaral. Nanalo ang AlexNet sa kumpetisyon ng ImageNet gamit ang mga GPU. Ang mga neural network ay nagsisimulang lumampas sa mga tradisyonal na pamamaraan sa paningin, pananalita, at wika. | Mabilis na pagbabago |
| **2017** | Ang papel na "Attention Is All You Need" ay nagpapakilala sa arkitektura ng Transformer. | Foundation para sa lahat ng sumusunod |
| **2020-2026** | Mga modelo ng malalaking wika (GPT-3, GPT-4, Claude, Gemini, LLaMA). Bumubuo ang AI ng text, code, mga larawan, video. Bumibilis ang pag-aampon ng negosyo. | Ang AI ay naging bahagi ng pang-araw-araw na buhay |
---

## Paano Gumagana ang Modern AI
### Machine Learning — Pag-aaral mula sa Data
Sa halip na magprograma ng mga tahasang panuntunan, ang machine learning ay nagpapakain ng data sa mga algorithm na naghahanap ng mga pattern nang mag-isa.
| Uri | Paano Ito Gumagana | Halimbawa |
|------|-------------|---------|
| **Sinusubaybayang pag-aaral** | Sanayin ang mga may label na halimbawa (input → tamang output) | Pag-detect ng spam: pakainin ito ng libu-libong email na may label na "spam" o "hindi spam" |
| **Hindi pinangangasiwaang pag-aaral** | Maghanap ng mga pattern sa walang label na data | Pagse-segment ng customer: pangkatin ang mga katulad na customer nang hindi paunang tinukoy ang mga pangkat |
| **Palakasin ang pag-aaral** | Natututo ang ahente sa pamamagitan ng pagsubok at pagkakamali, pagtanggap ng mga gantimpala o parusa | Game-playing AI: subukan ang mga galaw, makakuha ng mga puntos para sa panalo, alamin kung aling mga diskarte ang gumagana |
### Malalim na Pag-aaral — Mga Neural Network
Gumagamit ang malalim na pag-aaral ng mga artipisyal na neural network — mga layer ng simpleng mathematical operations na, pinagsama-sama, ay maaaring matuto ng hindi kapani-paniwalang kumplikadong mga pattern. Ang "malalim" ay tumutukoy sa bilang ng mga layer.
Mga pangunahing arkitektura:
| Arkitektura | Pinakamahusay Sa | Real-World Use |
|-------------|---------|----------------|
| **CNN** (Convolutional Neural Network) | Larawan at spatial na data | Pagkilala sa mukha, medikal na imaging, self-driving na mga kotse |
| **RNN/LSTM** | Sequential data (time series) | Pagkilala sa pananalita, pagbuo ng musika (na higit na pinapalitan ng mga Transformer) |
| **Transformer** | Lahat — teksto, mga larawan, audio, code | GPT, Claude, Gemini, BERT, DALL-E — ang nangingibabaw na arkitektura |
| **GAN** (Generative Adversarial Network) | Pagbuo ng makatotohanang data | Synthesis ng imahe, paglilipat ng istilo (bahagyang pinalitan ng mga modelo ng pagsasabog) |
| **Mga modelo ng pagsasabog** | Mataas na kalidad na pagbuo ng larawan/video | Stable Diffusion, DALL-E 3, Midjourney, Sora |
### Mga Malaking Modelo ng Wika (LLM)
Ang mga LLM ay mga modelong nakabatay sa Transformer na sinanay sa napakalaking dami ng teksto. Natututo silang hulaan ang susunod na token (piraso ng salita) sa isang pagkakasunud-sunod, na lumalabas na nangangailangan ng pag-unawa sa gramatika, katotohanan, pangangatwiran, at kahit isang bagay na kahawig ng "kaalaman."
| Modelo | Developer | Kapansin-pansing Tampok |
|-------|-----------|----------------|
| **GPT-4 / GPT-4o** | OpenAI | Multimodal (teksto + mga larawan); malakas na pangangatwiran |
| **Claude** | Antropiko | Tumutok sa kaligtasan at pagiging matulungin; mahabang context windows |
| **Gemini** | Google DeepMind | Katutubong multimodal; isinama sa mga serbisyo ng Google |
| **LLaMA / Llama 3** | Meta | Bukas-timbang; maaaring patakbuhin nang lokal; malaking komunidad |
| **Mistral** | Mistral AI | Ang mga mahusay na bukas na modelo ay nakikipagkumpitensya sa mga mas malalaking modelo |
**Proseso ng pagsasanay**:
1. **Pre-training**: Matuto mula sa napakalaking data ng text (hulaan ang mga susunod na token). Dito nakakakuha ang modelo ng "kaalaman."
2. **Fine-tuning**: Magsanay sa mga partikular na gawain o ayon sa mga kagustuhan ng tao.
3. **RLHF** (Reinforcement Learning mula sa Human Feedback): Nire-rate ng mga tao ang mga output ng modelo; ang modelo ay natututong gumawa ng mga output na ginusto ng mga tao.
**Mga window ng konteksto** (kung gaano karaming text ang maaaring iproseso ng modelo nang sabay-sabay) mula sa 4K na token (maagang GPT-3) ay naging mahigit 1 milyong token noong 2026 na mga modelo.
---

## Ano ang Nagagawa at Hindi Nagagawa ng AI
### Mga Kasalukuyang Kakayahan
| Gawain | Pagganap | Mga Limitasyon |
|------|-------------|-------------|
| **Pagbuo ng teksto** | Napakahusay — magkakaugnay, ayon sa konteksto, sari-saring istilo | Maaaring mag-hallucinate (bumuo ng maling impormasyon nang may kumpiyansa) |
| **Pagbuo ng code** | Napakahusay para sa karaniwang mga pattern; maaaring magsulat ng buong mga programa | Mga pakikibaka sa mga nobelang arkitektura; maaaring magpakilala ng mga banayad na bug |
| **Pagbuo ng larawan** | Photorealistic; artistikong istilo; pag-edit | Ang mga kamay at teksto ay hindi pa rin perpekto; nakikipagpunyagi sa tumpak na spatial na pangangatwiran |
| **Pagsasalin** | Near-human para sa mga pangunahing pares ng wika | Hindi gaanong tumpak ang mga wikang mababa ang mapagkukunan; cultural nuance ay maaaring mawala |
| **Pagkilala sa pagsasalita** | Malapit sa tao sa malinis na audio | Mga pakikibaka sa mabibigat na accent, ingay sa background |
| **Pangangatuwiran** | Mabilis na pagpapabuti; kayang lutasin ang maraming lohikal na problema | Nabigo sa mga nobelang problema na nangangailangan ng tunay na pag-unawa |
| **Matematika** | Mahusay sa karaniwang mga problema | Gumagawa ng mga pagkakamali sa mga nobelang patunay; hindi isang kapalit para sa pormal na pag-verify |
| **Pagpaplano at paggamit ng tool** | Umuusbong (mga ahente) | Hindi pa rin maaasahan para sa mga kumplikadong multi-step na gawain nang walang pangangasiwa ng tao |
### Ano ang Hindi Nagagawa ng AI (sa 2026)
- **Tunay na maunawaan** ang anumang bagay sa paraang ginagawa ng tao — pinoproseso nito ang mga pattern, hindi kahulugan
- **Garantiyahin ang katumpakan ng katotohanan** — nananatiling hindi nalutas na problema ang guni-guni
- **Palitan ang paghatol ng tao** sa mga desisyong may mataas na taya nang walang pangangasiwa
- **I-generalize nang perpekto** sa mga domain na ibang-iba sa data ng pagsasanay
- **Magsasarili sa pagpapatakbo** sa hindi mahulaan na pisikal na kapaligiran (mahirap pa rin ang robotics)
---

## Etika at Kaligtasan ng AI
Ang AI ay hindi neutral. Sinasalamin nito ang data kung saan ito sinanay, ang mga pagpipilian ng mga developer nito, at ang mga insentibo ng mga organisasyong nagde-deploy nito.
### Mga Pangunahing Alalahanin
| Isyu | Ano ang Mangyayari | Halimbawa |
|-------|-------------|---------|
| **Pagkiling** | Ang mga AI system ay nagpaparami at nagpapalaki ng mga bias sa data ng pagsasanay | Pag-hire ng mga algorithm na pinapaboran ang mga lalaking kandidato; pagkilala sa mukha na may mas mataas na rate ng error para sa mas maitim na balat |
| **Privacy** | Sinanay ang AI sa personal na data; mga kakayahan sa pagsubaybay | Pagsasanay sa mga naka-copyright na gawa; pagkilala sa mukha sa mga pampublikong espasyo |
| **Maling Paggamit** | Mga Deepfake, disinformation, awtomatikong phishing | AI-generated pekeng video ng mga pulitiko; mga awtomatikong tawag sa scam |
| **Paglipat ng trabaho** | Automation ng mga gawain na dati nang ginawa ng mga tao | Paglikha ng nilalaman, serbisyo sa customer, pagpasok ng data, ilang programming |
| **Paghahanay** | Pagtiyak na tumutugma ang mga layunin ng AI sa mga halaga ng tao | Ang isang AI na sinabihan na "i-maximize ang paggawa ng paperclip" ay maaaring i-convert ang lahat ng bagay sa mga paperclip |
| **Eksistensyal na panganib** | Teoretikal na pag-aalala tungkol sa hinaharap na AGI | Debate sa mga mananaliksik — nakikita ng ilan bilang apurahan, ang iba ay napaaga |
### Sino ang Nagtatrabaho sa Kaligtasan
- **Anthropic** — itinatag ng mga dating mananaliksik ng OpenAI na partikular na nakatuon sa kaligtasan ng AI
- **DeepMind Safety** — research team sa loob ng Google DeepMind
- **MIRI** (Machine Intelligence Research Institute) — teoretikal na pananaliksik sa kaligtasan
- **ARC** (AI Research Center) — empirical na pananaliksik sa kaligtasan
- **Mga katawan ng pamahalaan** — EU AI Act (2026), US executive orders, international frameworks
---

## AI sa Practice — Industriya ayon sa Industriya
| Industriya | Application | Maturity |
|----------|-------------|----------|
| **Pangangalaga sa kalusugan** | Pag-diagnose ng kanser mula sa mga larawan; pagtuklas ng droga (AlphaFold); paghula ng mga resulta ng pasyente | Na-deploy at lumalawak |
| **Pananalapi** | Pag-detect ng panloloko, algorithmic trading, credit scoring, robo-advisors | Malawakang na-deploy |
| **Transportasyon** | Mga sasakyang self-driving (Waymo, Tesla Autopilot); pag-optimize ng ruta | Bahagyang na-deploy; limitado pa rin ang buong awtonomiya |
| **Edukasyon** | Personalized na pag-aaral; AI pagtuturo; awtomatikong pagmamarka | Mabilis na lumalago |
| **Mga creative na field** | Pagbuo ng larawan (Midjourney, DALL-E); musika; tulong sa pagsulat; pagkumpleto ng code | Pagbabago ng mga daloy ng trabaho ngayon |
| **Cybersecurity** | Pagtuklas ng banta; pagkakakilanlan ng anomalya; parehong pag-atake at depensa | Nagpapatuloy ang karera ng armas |
| **Legal** | Pagsusuri ng kontrata; pagsusuri ng dokumento; legal na pananaliksik | Inaampon; mga alalahanin sa katumpakan |
| **Agrikultura** | Pagsubaybay sa crop sa pamamagitan ng satellite/drone; pag-spray ng katumpakan; hula ng ani | Lumalago |
| **Paggawa** | Inspeksyon ng kalidad; predictive na pagpapanatili; pag-optimize ng supply chain | Malawakang na-deploy |
---

## Robotics at Embodied AI
Pinagsasama ng Robotics ang AI sa mga pisikal na makina. Sa kabila ng mga dekada ng pag-unlad, ang pisikal na pakikipag-ugnayan sa mundo ay nananatiling mas mahirap kaysa sa digital intelligence.
- **Boston Dynamics' Atlas** — advanced bipedal movement; parkour; mga gawain sa bodega
- **Mga robot na pang-industriya** (ABB, FANUC, KUKA) — i-automate ang pagmamanupaktura; hinang; pagpupulong
- **Mga surgical robot** (da Vinci System) — minimally invasive na operasyon na may katumpakan na lampas sa mga kamay ng tao
- **Mga robot ng sambahayan** (Roomba) — simple ngunit matagumpay sa komersyo
- **Humanoid robot** (Tesla Optimus, Figure AI) — umuusbong; napakahirap pa rin ng pangkalahatang layuning pisikal na gawain
Ang agwat sa pagitan ng digital AI (na gumawa ng napakalaking pag-unlad) at pisikal na AI (na nakikipagpunyagi sa kagalingan ng kamay, balanse, at hindi mahuhulaan na mga kapaligiran) ay isa sa mga malalaking hamon ng larangan.
---

## Mga Kasalukuyang Trend (2020s)
| Uso | Ano ang Nangyayari |
|-------|-------------------|
| **Multimodal AI** | Mga system na magkasamang nagpoproseso ng text, mga larawan, audio, at video (GPT-4V, Gemini) |
| **Mga Ahente** | Mga LLM na maaaring gumamit ng mga tool, mag-browse sa web, magsulat ng code, at gumawa ng maraming hakbang na aksyon |
| **Mga modelong bukas ang timbang** | Ang LLaMA ng Meta at iba pa ay nagde-demokrasya ng access sa malalaking modelo |
| **Nasa-device AI** | Gumagamit ng mga modelo nang lokal sa mga telepono at laptop (Apple Intelligence, Qualcomm NPUs) |
| **Regulasyon ng AI** | EU AI Act (2026) — unang komprehensibong batas ng AI; pag-uuri ng mga sistema ayon sa antas ng panganib |
| **AI sa agham** | Pagtitiklop ng protina (AlphaFold), pagtuklas ng mga materyales, pagmomodelo ng klima, mga patunay sa matematika |
| **Mga modelo ng maliliit na wika** | Mga mahuhusay na modelo na tumatakbo sa hardware ng consumer; kalidad na lumalapit sa mas malalaking modelo |
---

## Buod
Ang AI ang pinakamahalagang pag-unlad ng teknolohiya sa ika-21 siglo sa ngayon. Ito ay hindi magic — ito ay pattern na tumutugma sa sukat, na pinagana ng napakalaking data, malakas na hardware, at matalinong mga arkitektura. Ang nakapagpapabago nito ay ang pagtutugma ng pattern, na ginawa nang maayos, ay maaaring magtiklop ng maraming gawain na dati nang nangangailangan ng katalinuhan ng tao. Ang mga hamon ay pare-parehong makabuluhan: guni-guni, pagkiling, paglilipat ng trabaho, maling paggamit, at ang bukas na tanong kung ang landas mula sa makitid na AI patungo sa pangkalahatang katalinuhan ay maikli o imposibleng mahaba. Ang malinaw ay muling bubuo ng AI ang bawat industriya, bawat propesyon, at bawat aspeto ng pang-araw-araw na buhay. Ang pag-unawa sa kung paano ito gumagana — at kung ano ang hindi nito magagawa — ay mahalaga para sa pag-navigate sa mundong ating binuo.