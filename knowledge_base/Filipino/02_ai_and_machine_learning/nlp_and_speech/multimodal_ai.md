---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
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
tags: [multimodal, ai, ai-and-machine-learning]
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

# Multimodal AI
Pinoproseso at pinagsasama-sama ng mga multimodal AI system ang impormasyon mula sa maraming uri ng data — teksto, mga larawan, audio, video, at higit pa — nang sabay-sabay. Habang ang mga naunang AI system ay karaniwang single-modality (text-only, image-only), ang pinaka-may kakayahang modernong system ay multimodal. Binabasa ng GPT-4V ang mga larawan at teksto nang magkasama; Pinoproseso ng Gemini ang text, mga larawan, audio, at video nang native; at ang mga system tulad ng Sora ay bumubuo ng video mula sa mga paglalarawan ng teksto. Sinasaklaw ng file na ito kung paano gumagana ang multimodal AI, ang mga arkitektura sa likod nito, at kung bakit napakalakas ng pagsasama-sama ng mga modalidad.
---

## Bakit Multimodal?
| Benepisyo | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Mas mayamang pag-unawa** | Ang iba't ibang mga modalidad ay nagbibigay ng pantulong na impormasyon | Ang isang video ay naghahatid ng galaw, tunog, at konteksto na hindi kayang |
| **Mas mahusay na paglalahat** | Ang pag-aaral sa iba't ibang modalidad ay lumilikha ng mas matatag na representasyon | Ang isang modelo na nakakita ng parehong mga larawan at mga paglalarawan ng teksto ng "pusa" ay mas nauunawaan ang konsepto |
| **Higit pang natural na pakikipag-ugnayan** | Ang mga tao ay nakikipag-usap sa pamamagitan ng maraming channel | Mga voice assistant na nakikita kung ano ang iyong itinuturo |
| **Cross-modal transfer** | Ang kaalaman mula sa isang modality ay nakakatulong sa isa pang | Ang pag-unawa sa imahe ay nagpapabuti sa pagbuo ng teksto, at kabaliktaran |
---

## Mga Pangunahing Arkitektura
### Mga Modelo ng Vision-Language (Mga VLM)
Mga modelo na nagpoproseso ng parehong mga imahe at teksto nang magkasama.
| Arkitektura | Paano Ito Gumagana | Mga halimbawa |
|-------------|-------------|---------|
| **Dual encoder** | Paghiwalayin ang mga encoder para sa imahe at teksto; pagsamahin sa susunod na yugto | CLIP, I-ALIGN |
| **Fusion encoder** | Ang mga token ng imahe at teksto ay pinagsama at pinoproseso nang magkasama | Flamingo, Gemini |
| **Cross-attention** | Ang mga text token ay dumadalo sa mga feature ng imahe (o vice versa) | Flamingo, CoCa |
| **Pinag-isang tokenizer** | Ang mga imahe ay kino-convert sa mga token at pinoproseso kasama ng mga text token | Gemini, Chameleon |
### Paano Gumagana ang Mga Modelo sa Pananaw-Wika
| Hakbang | Paglalarawan |
|------|-------------|
| **1. I-encode ang larawan** | Kino-convert ng vision encoder (ViT, SigLIP) ang imahe sa isang set ng mga feature vectors |
| **2. Encode text** | Pinoproseso ng isang language encoder ang mga text token |
| **3. Fuse modalities** | Ang mga feature ng larawan ay ipino-project sa embedding space ng modelo ng wika |
| **4. Bumuo** | Ang modelo ng wika ay gumagawa ng text na nakakondisyon sa parehong imahe at text input |
### Pangunahing Paningin-Mga Modelo sa Wika
| Modelo | Developer | Arkitektura | Kapansin-pansing Tampok |
|-------|-----------|-------------|----------------|
| **CLIP** | OpenAI | Dual encoder (ViT + text encoder) | Zero-shot na pag-uuri ng imahe sa pamamagitan ng text |
| **LLaVA** | Open-source | LLaMA + CLIP visual encoder | Open-source na VLM; malakas na komunidad |
| **GPT-4V / 4o** | OpenAI | Pinag-isang multimodal | Pinoproseso ang teksto, mga larawan, audio nang magkasama |
| **Gemini** | Google DeepMind | Katutubong multimodal mula sa pagsasanay | Binuo para sa multimodal mula sa simula |
| **Claude** | Antropiko | Paningin + teksto | Malakas sa pag-unawa sa dokumento at tsart |
| **Qwen-VL** | Alibaba | Open-weight na VLM | Mapagkumpitensya sa mga saradong modelo |
| **InternVL** | Open-source | Multi-scale vision encoder | Malakas na open-source na opsyon |
---

## Mga Modelo ng Audio at Pananalita
### Speech Recognition (ASR)
| Modelo | Arkitektura | Kapansin-pansing Tampok |
|-------|-------------|-----------------|
| **Bulong** (OpenAI) | Encoder-decoder Transformer | Sinanay sa 680K na oras ng multilingguwal na audio; matatag |
| **Conformer** | Convolution + pansin sa sarili | Pinagsasama ang mga lokal at pandaigdigang tampok |
| **wav2vec 2.0** | Self-supervised | Natututo mula sa walang label na pananalita |
| **USM** (Google) | Pangkalahatang modelo ng pagsasalita | 2M na oras ng may label na data; 300+ wika |
### Text-to-Speech (TTS)
| Modelo | Diskarte | Kapansin-pansing Tampok |
|-------|----------|----------------|
| **VALL-E** (Microsoft) | Neural codec | Pag-clone ng boses mula sa 3 segundong sample |
| **Bark** (Suno) | Nakabatay sa transformer | Multilingual; may kasamang mga tunog na hindi nagsasalita |
| **ElevenLabs** | Komersyal | Mataas na kalidad na voice cloning |
| **ChatTTS** | Open-source | Pagsasalita sa pakikipag-usap na may natural na prosody |
| **Pagsasalita ng Isda** | Open-source | Multilingual; mabilis na hinuha |
### Pag-unawa sa Audio
| Modelo | Kakayahan |
|-------|-----------|
| **AudioLDM** | Pagbuo ng sound effect mula sa text |
| **MusicGen** (Meta) | Text-to-music generation |
| **Qwen-Audio** | Pag-unawa sa audio (pagsasalita, musika, mga tunog sa kapaligiran) |
| **SALMON** | Pag-unawa sa pagsasalita, audio, wika, musika, at ingay |
---

## Mga Modelo ng Video
Pinagsasama ng video ang mga larawan, audio, teksto, at oras — ginagawa itong pinakamasalimuot na modality.
| Modelo | Uri | Kakayahan |
|-------|------|-------------|
| **Sora** (OpenAI) | Text-to-video | Hanggang 1080p; nakakaintindi ng physics |
| **Gemini** | Pag-unawa sa video | Maaaring suriin ang mahahabang video na may audio |
| **Video-LLaVA** | Video + text | Pag-unawa sa open-source na video |
| **Runway Gen-3** | Text/image-to-video | Pagbuo ng komersyal na video |
| **Kling** | Text-to-video | Long-form na pagbuo ng video |
### Mga Hamon sa Pag-unawa sa Video
| Hamon | Paglalarawan |
|-----------|-------------|
| **Temporal na pangangatwiran** | Pag-unawa sa mga kaganapang naganap sa paglipas ng panahon |
| **Mahabang konteksto** | Ang mga video ay maaaring tumagal ng ilang oras; ang pagproseso ng lahat ng mga frame ay mahal |
| **Audio-visual sync** | Pag-uugnay sa kung ano ang sinabi sa kung ano ang ipinapakita |
| **Cusality** | Pag-unawa sa sanhi at epekto sa mga sequence ng video |
---

## Cross-Modal Retrieval
Paghahanap ng may-katuturang nilalaman sa iba't ibang mga modalidad.
| Gawain | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Text → Larawan** | Maghanap ng mga larawang tumutugma sa isang text query | Hanapin ang "paglubog ng araw sa ibabaw ng mga bundok" sa isang library ng larawan |
| **Larawan → Teksto** | Maghanap ng tekstong nauugnay sa isang larawan | Bumubuo ng mga caption para sa mga larawan |
| **Text → Audio** | Maghanap ng mga tunog na tumutugma sa isang paglalarawan | Disenyo ng tunog: "mga yapak sa graba" |
| **Larawan → Larawan** | Maghanap ng mga visual na katulad na larawan | Paghahanap ng produkto ayon sa larawan |
### CLIP para sa Cross-Modal Retrieval
Ang nakabahaging espasyo sa pag-embed ng CLIP ay nagbibigay-daan sa zero-shot na cross-modal retrieval:
| Hakbang | Paglalarawan |
|------|-------------|
| 1 | I-encode ang lahat ng larawan gamit ang vision encoder |
| 2 | I-encode ang text query gamit ang text encoder |
| 3 | I-compute ang pagkakatulad ng cosine sa pagitan ng pag-embed ng text at lahat ng mga pag-embed ng larawan |
| 4 | Ibalik ang mga larawang may pinakamataas na pagkakatulad |
Gumagana ito nang walang anumang pagsasanay na partikular sa gawain — isang property na tinatawag na **zero-shot** na kakayahan.
---

## Nakapaloob na AI
Pinagsasama ng Embodied AI ang multimodal na perception sa pisikal na pagkilos.
| System | Modalidad | Application |
|--------|----------|-------------|
| **RT-2** (Google) | Paningin + wika → mga pagkilos ng robot | Pangkalahatang layunin na kontrol ng robot mula sa mga tagubilin sa teksto |
| **Octo** | Patakaran sa open-source na robot | Sinanay sa magkakaibang data ng robot |
| **Tesla Optimus** | Paningin + wika → mga pisikal na gawain | Humanoid robot para sa mga pangkalahatang gawain |
| **Figure 01** | Paningin + wika + pananalita | Humanoid robot na may kakayahang makipag-usap |
### Mga Hamon sa Embodied AI
| Hamon | Bakit Mahirap |
|-----------|--------------|
| **Sim-to-real gap** | Hindi perpektong nakukuha ng simulation ang real-world physics |
| **Kagalingan** | Ang kontrol ng pinong motor (mga kamay, mga daliri) ay napakahirap |
| **Kaligtasan** | Ang mga pisikal na robot ay maaaring magdulot ng tunay na pinsala |
| **Real-time na pagproseso** | Dapat madama, magpasya, at kumilos sa milliseconds |
| **Paglalahat** | Ang isang robot na sinanay upang kunin ang mga pulang tasa ay maaaring mabigo sa mga asul na tasa |
---

## Data at Pagsasanay
### Data ng Multimodal na Pagsasanay
| Dataset | Mga Modal | Sukat |
|---------|-----------|------|
| **LAION-5B** | Mga pares ng imahe-text | 5.85 bilyong pares |
| **DataComp** | Na-curate na imahe-text | Benchmark para sa disenyo ng dataset |
| **WIT** (Wikipedia) | Image-text mula sa Wikipedia | 11.5 milyong pares |
| **HowTo100M** | Video-text (how-to na mga video) | 100 milyong mga clip |
| **LibriSpeech** | Text-speech | 1,000 oras ng English |
| **Karaniwang Boses** | Text-speech | Multilingual; inambag ng komunidad |
### Mga Istratehiya sa Pagsasanay
| Diskarte | Paglalarawan | Kailan Gagamitin |
|----------|-------------|-------------|
| **Pinagsanib na pagsasanay** | Magsanay sa lahat ng mga modalidad nang sabay-sabay | Kapag na-align mo ang multimodal data |
| **Pag-aaral ng Kurikulum** | Magsimula sa mga madaling halimbawa; dagdagan ang kahirapan | Nagpapabuti ng convergence |
| **Contrastive na pag-aaral** | Matutong tumugma sa mga magkakaugnay na pares sa iba't ibang modalidad (CLIP-style) | Pagbuo ng mga nakabahaging representasyon |
| **Pag-tune ng tagubilin** | Magsanay sa multimodal na mga pares ng pagtuturo-tugon | Ang paggawa ng mga modelo ay sumusunod sa mga multimodal na tagubilin |
---

## Pagsusuri
| Benchmark | Mga Modal | Ano ang Sinusubok Nito |
|-----------|-----------|--------------|
| **MMLU** | Text | Kaalaman sa 57 paksa |
| **MMMU** | Teksto + mga larawan | Pangatwiran sa antas ng kolehiyo na may mga diagram |
| **MathVista** | Teksto + mga larawan | Pang-matematikong pangangatwiran na may visual na data |
| **Video-MME** | Text + video | Pag-unawa sa video at temporal na pangangatwiran |
| **HELMET** | Text + audio | Mahabang-konteksto na multimodal na pagsusuri |
| **SWE-bench** | Text + code | Mga gawain sa real-world software engineering |
---

## Buod
Kinakatawan ng Multimodal AI ang paglipat mula sa mga single-purpose na modelo patungo sa mga system na nakikita at nangangatuwiran sa lahat ng anyo ng data. Ang mga modelo ng vision-language tulad ng GPT-4V at Gemini ay makakaintindi ng mga larawan at text nang magkasama; ang mga modelo ng pagsasalita tulad ng Whisper at VALL-E ay humahawak ng audio; nagsisimula nang iproseso ng mga modelo ng video ang buong pagiging kumplikado ng mga gumagalaw na larawan na may tunog. Ang trend ay malinaw: ang pinaka-may kakayahang AI system sa hinaharap ay magiging katutubong multimodal, na pinoproseso ang lahat ng uri ng impormasyon nang sabay-sabay. Ang mga hamon — pag-align ng data, gastos sa computational, pagsusuri, at pag-deploy ng katawan — ay makabuluhan, ngunit mabilis ang pag-unlad noong 2024–2026.