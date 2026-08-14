---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
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
tags: [speech, audio, processing, ai-and-machine-learning]
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

# Pagproseso ng Pagsasalita at Audio
Sinasaklaw ng pagpoproseso ng pagsasalita at audio ang mga teknolohiyang nagbibigay-daan sa mga makina na marinig, maunawaan, bumuo, at magmanipula ng tunog. Kabilang dito ang speech recognition (paggagawa ng mga sinasalitang salita sa teksto), speech synthesis (pagpalit ng teksto sa pasalitang salita), pagkakakilanlan ng tagapagsalita, pagbuo ng musika, at pag-unawa sa tunog sa kapaligiran. Ang larangan ay binago sa pamamagitan ng malalim na pag-aaral — ang mga modernong sistema ay lumalapit sa katumpakan sa antas ng tao para sa pagkilala sa pagsasalita at gumawa ng mga nakakatakot na natural na sintetikong boses.
---

## Digital Audio Fundamentals
Ang tunog ay isang pressure wave. Para iproseso ito nang digital, nagsa-sample kami ng wave sa mga regular na pagitan.
| Konsepto | Paglalarawan | Karaniwang Halaga |
|---------|-------------|--------------|
| **Sample rate** | Ilang beses bawat segundo sinusukat ang tunog | 8 kHz (telepono), 16 kHz (speech), 44.1 kHz (CD), 48 kHz (propesyonal) |
| **Bit depth** | Katumpakan ng bawat sample | 16-bit (CD), 24-bit (propesyonal), 32-bit float (pagproseso) |
| **Mga Channel** | Mono (1), stereo (2), surround (5.1, 7.1) | Stereo para sa musika; mono para sa pagsasalita |
| **Tagal** | Haba ng audio | Nag-iiba |
Isang 1 minutong mono recording sa 16 kHz, 16-bit = 1.92 MB. Isang 3 minutong stereo na kanta sa 44.1 kHz, 16-bit = 30.3 MB.
---

## Audio Feature Extraction
Ang mga raw audio waveform ay mahirap para sa mga modelo na direktang gumana. Kinukuha namin ang mga feature na kumukuha ng mahahalagang katangian ng tunog.
| Tampok | Ano ang Kinukuha Nito | Use Case |
|---------|-----------------|----------|
| **Mel spectrogram** | Ang dalas ng nilalaman sa paglipas ng panahon, nakamapang sa pandama ng pandinig ng tao | Pagkilala sa pananalita, pag-uuri ng musika |
| **MFCC** (Mel-Frequency Cepstral Coefficients) | Compact na representasyon ng spectral envelope | Tradisyunal na pagkilala sa pagsasalita |
| **Chromagram** | Pamamahagi ng pitch class (kung aling mga tala ang tumutugtog) | Pagsusuri ng musika, pagtuklas ng chord |
| **Zero-crossing rate** | Gaano kadalas tumawid sa zero ang signal | Voiced vs unvoiced detection |
| **RMS energy** | Lakas ng signal sa paglipas ng panahon | Pag-detect ng aktibidad ng boses |
| **Pitch (F0)** | Pangunahing dalas | Pagkakakilanlan ng speaker, transkripsyon ng musika |
### Mel Spectrogram
Ang pinakakaraniwang representasyon ng audio para sa malalim na pag-aaral. Kino-convert nito ang audio sa isang 2D image-like format:
| Axis | Kumakatawan sa |
|------|-----------|
| **X-axis** | Oras |
| **Y-axis** | Dalas (sa Mel scale — perceptually spaced) |
| **Kulay/intensity** | Enerhiya sa dalas at oras na iyon |
Ang sukat ng Mel ay tinatantya ang pandinig ng tao: mas mahusay tayong makilala ang mga mababang frequency kaysa sa mataas.
---

## Awtomatikong Speech Recognition (ASR)
Kino-convert ng ASR ang pasalitang wika sa teksto. Isa ito sa pinakamahalagang komersyal na application ng audio AI.
### Ebolusyon ng ASR
| Era | Diskarte | Limitasyon |
|-----|----------|------------|
| **Pre-2010** | Mga Nakatagong Markov Models + Gaussian Mixture Models | Kinakailangan ang malawak na hand-engineering; mahirap sa maingay na kondisyon |
| **2010-2015** | DNN-HMM hybrid | Pinalitan ng mga neural network ang mga GMM; makabuluhang pagpapabuti |
| **2015-2020** | Mga end-to-end na modelo (Deep Speech, LAS) | Isang neural network mula sa audio hanggang sa text |
| **2020+** | Nakabatay sa Transformer (Bulong, Conformer) | Makabagong katumpakan; multilinggwal; matatag |
### Mga Pangunahing Modelong ASR
| Modelo | Arkitektura | Data ng Pagsasanay | Kapansin-pansing Tampok |
|-------|-------------|----------------|----------------|
| **Bulong** (OpenAI) | Encoder-decoder Transformer | 680,000 oras, 99 na wika | Multilingual; matatag sa mga accent at ingay; open-source |
| **Conformer** | Convolution + pansin sa sarili | Iba't ibang | Pinagsasama ang lokal (conv) at pandaigdigang (pansin) na mga feature |
| **wav2vec 2.0** | Self-supervised Transformer | Walang label na pananalita | Natututo mula sa hilaw na audio nang walang mga transkripsyon |
| **USM** (Google) | Pangkalahatang modelo ng pagsasalita | 2 milyong oras, 300+ wika | Karamihan sa mga wikang sakop |
| **MMS** (Meta) | Massively Multilingual Speech | 1,400+ wika | Pinapalawak ang saklaw sa mga wikang mababa ang mapagkukunan |
### Mga Sukatan ng ASR
| Sukatan | Paglalarawan |
|--------|--------------|
| **WER** (Word Error Rate) | Porsiyento ng mga salita na mali ang pagkaka-transcribe. Mas mabuti ang ibaba. Ang pagganap ng tao ay ~4-5% para sa malinis na Ingles. |
| **CER** (Character Error Rate) | Pareho sa WER ngunit nasa antas ng karakter. Ginagamit para sa mga wikang walang hangganan ng salita (Chinese, Japanese). |
### Mga Karaniwang Hamon sa ASR
| Hamon | Paglalarawan |
|-----------|-------------|
| **Mga accent at dialect** | Malaki ang pagbaba ng performance para sa mga hindi karaniwang accent |
| ** ingay sa background** | Musika, trapiko, iba pang mga speaker ay nagpapababa sa katumpakan |
| **Pagpalit ng code** | Ang mga nagsasalita ay nagpapalipat-lipat sa pagitan ng mga wika sa kalagitnaan ng pangungusap |
| **Mga Homophone** | "Ayan" vs "kanila" vs "sila" — nangangailangan ng konteksto |
| **Bantas at pag-format** | Karaniwang walang bantas ang output ng ASR; nangangailangan ng post-processing |
| **Mga wikang mababa ang mapagkukunan** | Karamihan sa mga modelo ay hindi mahusay na gumaganap para sa mga wikang may kaunting data ng pagsasanay |
---

## Text-to-Speech (TTS)
Kino-convert ng TTS ang nakasulat na teksto sa pasalitang audio. Ang mga makabagong sistema ay gumagawa ng pananalita na kadalasang hindi naiiba sa mga rekording ng tao.
### Ebolusyon ng TTS
| Era | Diskarte | Kalidad |
|-----|----------|---------|
| **Pre-2010** | Concatenative (pagtahi ng mga naitalang fragment) | Robotic; limitadong pagpapahayag |
| **2010-2017** | Statistical parametric (mga HMM, maagang neural) | Mas mahusay ngunit nakikilala pa rin bilang synthetic |
| **2017-2020** | Neural (Tacotron, WaveNet) | Malapit sa kalidad ng tao; nagpapahayag |
| **2020+** | Neural codec (VALL-E, Bark) | Pag-clone ng boses; ilang-shot; napaka natural |
### Mga Pangunahing Modelong TTS
| Modelo | Arkitektura | Kapansin-pansing Tampok |
|-------|-------------|-----------------|
| **WaveNet** (DeepMind) | Autoregressive generative model | Unang tunay na natural na tunog TTS |
| **Tacotron 2** (Google) | Seq2seq + vocoder | End-to-end; mataas na kalidad |
| **VITS** | Variational inference + adversarial training | Mabilis; magandang kalidad; malawakang ginagamit |
| **VALL-E** (Microsoft) | Modelo ng wikang neural codec | Pag-clone ng boses mula sa 3 segundong sample |
| **Bark** (Suno) | Nakabatay sa transformer | Multilingual; mga di-speech na tunog (tawa, musika) |
| **ElevenLabs** | Komersyal | Pag-clone ng boses na nangunguna sa industriya |
| **ChatTTS** | Open-source | Na-optimize para sa pakikipag-usap na pagsasalita |
| **Pagsasalita ng Isda** | Open-source | Mabilis; multilinggwal |
### Voice Cloning
Ang voice cloning ay lumilikha ng isang synthetic na boses na parang isang partikular na tao mula sa isang maikling audio sample.
| Paraan | Kailangan ng Data | Kalidad |
|--------|------------|---------|
| **Fine-tuning** | 10-60 minuto ng pagsasalita | Mataas na kalidad; tukoy sa speaker |
| **Few-shot** | 3-30 segundo ng pagsasalita | Magandang kalidad; mabilis na pag-setup |
| **Zero-shot** | Walang data ng target na speaker | Gumagamit ng reference na audio sa oras ng hinuha |
**Etikal na alalahanin**: ang voice cloning ay maaaring gamitin para sa pagpapanggap, panloloko, at deepfakes. Karamihan sa mga komersyal na provider ay nangangailangan ng pahintulot ng boses.
---

## Pagkilala sa Tagapagsalita
| Gawain | Paglalarawan | Application |
|------|-------------|-------------|
| **Pag-verify ng speaker** | "Ito ba ang taong sinasabi nila?" | Phone banking, pag-unlock ng device |
| **Pagkilala sa tagapagsalita** | "Sino ang nagsasalita?" | Transkripsyon ng pulong, forensics |
| **Speaker diarisation** | "Sino ang nagsalita kailan?" (sa multi-speaker na audio) | Mga buod ng pulong, pagbuo ng subtitle |
| Modelo | Diskarte |
|-------|----------|
| **ECAPA-TDNN** | Nakabatay sa pag-embed; state-of-the-art para sa pag-verify |
| **d-vector** | Mga simpleng pag-embed ng speaker mula sa DNN |
| **x-vector** | Pinahusay na pag-embed ng speaker; malawakang ginagamit |
---

## Pagkuha ng Impormasyon sa Musika
| Gawain | Paglalarawan | Mga Tool/Modelo |
|------|-------------|-------------|
| **Transkripsyon ng musika** | I-convert ang audio sa sheet music / MIDI | Spotify Basic Pitch, Spleeter |
| **Source separation** | Ihiwalay ang mga indibidwal na instrumento o vocal | Demucs, Spleeter, Music Source Separation |
| **Pag-uuri ng genre** | Ikategorya ang musika ayon sa genre | Mga CNN sa spectrograms |
| **Beat tracking** | I-detect ang mga posisyon ng tempo at beat | Librosa, Madmom |
| **Chord recognition** | Tukuyin ang mga chord sa musika | Chord-CNN, CRF na mga modelo |
| **Henerasyon ng musika** | Lumikha ng bagong musika | MusicGen, MuseNet, AIVA |
---

## Environmental Sound Detection
| Gawain | Paglalarawan | Application |
|------|-------------|-------------|
| **Pag-detect ng sound event** | Tukuyin ang mga tunog sa isang kapaligiran | Smart home (pagbabasag ng salamin, pag-iyak ng sanggol) |
| **Pag-uuri ng acoustic scene** | Uriin ang kapaligiran (opisina, parke, trapiko) | Mga device na may kamalayan sa konteksto |
| **Pagtukoy ng anomalya** | I-detect ang mga hindi pangkaraniwang tunog | Industrial monitoring (machineæ•…éšœ) |
| Dataset | Mga Tunog | Sukat |
|---------|--------|------|
| **AudioSet** | 632 sound classes | 2M+ clip sa YouTube |
| **ESC-50** | 50 mga klase ng tunog sa kapaligiran | 2,000 clip |
| **UrbanSound8K** | Mga tunog sa lungsod | 8,732 clip |
---

## Mga Tool at Framework
| Tool | Layunin |
|------|---------|
| **Librosa** | Python library para sa audio analysis (features, effects, visualization) |
| **Pydub** | Simpleng pagmamanipula ng audio (cut, concatenate, export) |
| **FFmpeg** | Pagproseso ng audio/video ng command-line (ang kutsilyo ng Swiss Army) |
| **Torchaudio** | Pagproseso ng audio ng PyTorch (mga pagbabago, mga dataset, mga modelo) |
| **Hugging Face (transformers)** | Mga pre-trained na modelo ng ASR at TTS |
| **Bulong (OpenAI)** | Pagkilala sa pagsasalita (open-source) |
| **Coqui TTS** | Open-source TTS toolkit |
| **Demucs** | Paghihiwalay ng pinagmulan ng musika |
| **SpeechBrain** | All-in-one speech toolkit (ASR, TTS, speaker recognition) |
---

## Mga Praktikal na Tip
- **Palaging makinig sa iyong data.** Bago magsanay ng anuman, makinig sa sample na audio. Tandaan ang sample rate, antas ng ingay, at mga katangian ng speaker.
- **Mga sample na rate ng tugma.** Inaasahan ng Whisper ang 16 kHz. Kung ang iyong audio ay 44.1 kHz, i-resample ito — ngunit tandaan na ang pag-downsampling ay nawawalan ng impormasyon.
- **Palakihin ang data ng audio.** Magdagdag ng ingay sa background, iba-iba ang bilis at pitch, gayahin ang iba't ibang mikropono. Ito ay kapansin-pansing nagpapabuti sa katatagan.
- **Gumamit ng mga pre-trained na modelo.** Ang Whisper para sa ASR at VITS/Bark para sa TTS ay mahusay na mga panimulang punto. Ang fine-tuning ay halos palaging mas mahusay kaysa sa pagsasanay mula sa simula.
- **Hasiwaan ang katahimikan.** Ang Voice Activity Detection (VAD) ay nag-aalis ng katahimikan bago iproseso, i-save ang compute at pagpapabuti ng katumpakan. Silero VAD at WebRTC VAD ay mga sikat na pagpipilian.
- **I-normalize ang volume.** Iba't ibang mga pag-record ay may ibang-iba na antas ng loudness. Normalize sa isang pare-parehong antas bago iproseso.
---

## Buod
Ang pagpoproseso ng pagsasalita at audio ay binago ng malalim na pag-aaral. Ang mga modernong sistema ng ASR tulad ng Whisper ay lumalapit sa katumpakan sa antas ng tao sa dose-dosenang mga wika. Ang mga sistema ng TTS ay gumagawa ng pagsasalita na lalong hindi nakikilala sa mga pag-record ng tao. Gumagana ang voice cloning mula sa mga segundo ng audio. Ang pagbuo ng musika, paghihiwalay ng pinagmulan, at pagtuklas ng tunog sa kapaligiran ay mabilis na umuunlad. Ang larangan ay nahaharap sa patuloy na mga hamon — mga wikang mababa ang mapagkukunan, maingay na kapaligiran, mga etikal na alalahanin tungkol sa pag-clone ng boses — ngunit malinaw ang trajectory: ang mga makina ay nagiging kasinghusay ng mga tao sa pandinig, pag-unawa, at paggawa ng tunog.