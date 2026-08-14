<!--
---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.1"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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

-->
# Speech and Audio Processing

Speech and audio processing covers the technologies that let machines hear, understand, generate, and manipulate sound. This includes speech recognition (turning spoken words into text), speech synthesis (turning text into spoken words), speaker identification, music generation, and environmental sound understanding. The field has been transformed by deep learning — modern systems approach human-level accuracy for speech recognition and produce eerily natural synthetic voices.

---

## Digital Audio Fundamentals

Sound is a pressure wave. To process it digitally, we sample the wave at regular intervals.

| Concept | Description | Typical Value |
|---------|-------------|---------------|
| **Sample rate** | How many times per second the sound is measured | 8 kHz (telephone), 16 kHz (speech), 44.1 kHz (CD), 48 kHz (professional) |
| **Bit depth** | Precision of each sample | 16-bit (CD), 24-bit (professional), 32-bit float (processing) |
| **Channels** | Mono (1), stereo (2), surround (5.1, 7.1) | Stereo for music; mono for speech |
| **Duration** | Length of the audio | Varies |

A 1-minute mono recording at 16 kHz, 16-bit = 1.92 MB. A 3-minute stereo song at 44.1 kHz, 16-bit = 30.3 MB.

---

## Audio Feature Extraction

Raw audio waveforms are hard for models to work with directly. We extract features that capture the important characteristics of sound.

| Feature | What It Captures | Use Case |
|---------|-----------------|----------|
| **Mel spectrogram** | Frequency content over time, mapped to human hearing perception | Speech recognition, music classification |
| **MFCC** (Mel-Frequency Cepstral Coefficients) | Compact representation of the spectral envelope | Traditional speech recognition |
| **Chromagram** | Pitch class distribution (which notes are playing) | Music analysis, chord detection |
| **Zero-crossing rate** | How often the signal crosses zero | Voiced vs unvoiced detection |
| **RMS energy** | Signal loudness over time | Voice activity detection |
| **Pitch (F0)** | Fundamental frequency | Speaker identification, music transcription |

### Mel Spectrogram

The most common audio representation for deep learning. It converts the audio into a 2D image-like format:

| Axis | Represents |
|------|-----------|
| **X-axis** | Time |
| **Y-axis** | Frequency (on the Mel scale — perceptually spaced) |
| **Colour/intensity** | Energy at that frequency and time |

The Mel scale approximates human hearing: we're better at distinguishing low frequencies than high ones.

---

## Automatic Speech Recognition (ASR)

ASR converts spoken language into text. It's one of the most commercially important applications of audio AI.

### Evolution of ASR

| Era | Approach | Limitation |
|-----|----------|------------|
| **Pre-2010** | Hidden Markov Models + Gaussian Mixture Models | Required extensive hand-engineering; poor in noisy conditions |
| **2010-2015** | DNN-HMM hybrid | Neural networks replaced GMMs; significant improvement |
| **2015-2020** | End-to-end models (Deep Speech, LAS) | Single neural network from audio to text |
| **2020+** | Transformer-based (Whisper, Conformer) | State-of-the-art accuracy; multilingual; robust |

### Key ASR Models

| Model | Architecture | Training Data | Notable Feature |
|-------|-------------|---------------|-----------------|
| **Whisper** (OpenAI) | Encoder-decoder Transformer | 680,000 hours, 99 languages | Multilingual; robust to accents and noise; open-source |
| **Conformer** | Convolution + self-attention | Various | Combines local (conv) and global (attention) features |
| **wav2vec 2.0** | Self-supervised Transformer | Unlabelled speech | Learns from raw audio without transcriptions |
| **USM** (Google) | Universal speech model | 2 million hours, 300+ languages | Most languages covered |
| **MMS** (Meta) | Massively Multilingual Speech | 1,400+ languages | Extends coverage to low-resource languages |

### ASR Metrics

| Metric | Description |
|--------|-------------|
| **WER** (Word Error Rate) | Percentage of words incorrectly transcribed. Lower is better. Human performance is ~4-5% for clean English. |
| **CER** (Character Error Rate) | Same as WER but at character level. Used for languages without word boundaries (Chinese, Japanese). |

### Common ASR Challenges

| Challenge | Description |
|-----------|-------------|
| **Accents and dialects** | Performance drops significantly for non-standard accents |
| **Background noise** | Music, traffic, other speakers degrade accuracy |
| **Code-switching** | Speakers switching between languages mid-sentence |
| **Homophones** | "There" vs "their" vs "they're" — requires context |
| **Punctuation and formatting** | ASR output is typically unpunctuated; needs post-processing |
| **Low-resource languages** | Most models perform poorly for languages with little training data |

---

## Text-to-Speech (TTS)

TTS converts written text into spoken audio. Modern systems produce speech that is often indistinguishable from human recordings.

### Evolution of TTS

| Era | Approach | Quality |
|-----|----------|---------|
| **Pre-2010** | Concatenative (stitching recorded fragments) | Robotic; limited expressiveness |
| **2010-2017** | Statistical parametric (HMMs, early neural) | Better but still recognisable as synthetic |
| **2017-2020** | Neural (Tacotron, WaveNet) | Near-human quality; expressive |
| **2020+** | Neural codec (VALL-E, Bark) | Voice cloning; few-shot; highly natural |

### Key TTS Models

| Model | Architecture | Notable Feature |
|-------|-------------|-----------------|
| **WaveNet** (DeepMind) | Autoregressive generative model | First truly natural-sounding TTS |
| **Tacotron 2** (Google) | Seq2seq + vocoder | End-to-end; high quality |
| **VITS** | Variational inference + adversarial training | Fast; good quality; widely used |
| **VALL-E** (Microsoft) | Neural codec language model | Voice cloning from 3-second sample |
| **Bark** (Suno) | Transformer-based | Multilingual; non-speech sounds (laughter, music) |
| **ElevenLabs** | Commercial | Industry-leading voice cloning |
| **ChatTTS** | Open-source | Optimised for conversational speech |
| **Fish Speech** | Open-source | Fast; multilingual |

### Voice Cloning

Voice cloning creates a synthetic voice that sounds like a specific person from a short audio sample.

| Method | Data Needed | Quality |
|--------|------------|---------|
| **Fine-tuning** | 10-60 minutes of speech | High quality; speaker-specific |
| **Few-shot** | 3-30 seconds of speech | Good quality; fast setup |
| **Zero-shot** | No target speaker data | Uses reference audio at inference time |

**Ethical concern**: voice cloning can be used for impersonation, fraud, and deepfakes. Most commercial providers require voice consent.

---

## Speaker Recognition

| Task | Description | Application |
|------|-------------|-------------|
| **Speaker verification** | "Is this person who they claim to be?" | Phone banking, device unlock |
| **Speaker identification** | "Who is speaking?" | Meeting transcription, forensics |
| **Speaker diarisation** | "Who spoke when?" (in multi-speaker audio) | Meeting summaries, subtitle generation |

| Model | Approach |
|-------|----------|
| **ECAPA-TDNN** | Embedding-based; state-of-the-art for verification |
| **d-vector** | Simple speaker embeddings from DNN |
| **x-vector** | Improved speaker embeddings; widely used |

---

## Music Information Retrieval

| Task | Description | Tools/Models |
|------|-------------|-------------|
| **Music transcription** | Convert audio to sheet music / MIDI | Spotify Basic Pitch, Spleeter |
| **Source separation** | Isolate individual instruments or vocals | Demucs, Spleeter, Music Source Separation |
| **Genre classification** | Categorise music by genre | CNNs on spectrograms |
| **Beat tracking** | Detect tempo and beat positions | Librosa, Madmom |
| **Chord recognition** | Identify chords in music | Chord-CNN, CRF models |
| **Music generation** | Create new music | MusicGen, MuseNet, AIVA |

---

## Environmental Sound Detection

| Task | Description | Application |
|------|-------------|-------------|
| **Sound event detection** | Identify sounds in an environment | Smart home (glass breaking, baby crying) |
| **Acoustic scene classification** | Classify the environment (office, park, traffic) | Context-aware devices |
| **Anomaly detection** | Detect unusual sounds | Industrial monitoring (machineæ•…éšœ) |

| Dataset | Sounds | Size |
|---------|--------|------|
| **AudioSet** | 632 sound classes | 2M+ YouTube clips |
| **ESC-50** | 50 environmental sound classes | 2,000 clips |
| **UrbanSound8K** | Urban sounds | 8,732 clips |

---

## Tools and Frameworks

| Tool | Purpose |
|------|---------|
| **Librosa** | Python library for audio analysis (features, effects, visualisation) |
| **Pydub** | Simple audio manipulation (cut, concatenate, export) |
| **FFmpeg** | Command-line audio/video processing (the Swiss Army knife) |
| **Torchaudio** | PyTorch audio processing (transforms, datasets, models) |
| **Hugging Face (transformers)** | Pre-trained ASR and TTS models |
| **Whisper (OpenAI)** | Speech recognition (open-source) |
| **Coqui TTS** | Open-source TTS toolkit |
| **Demucs** | Music source separation |
| **SpeechBrain** | All-in-one speech toolkit (ASR, TTS, speaker recognition) |

---

## Practical Tips

- **Always listen to your data.** Before training anything, listen to sample audio. Note the sample rate, noise level, and speaker characteristics.
- **Match sample rates.** Whisper expects 16 kHz. If your audio is 44.1 kHz, resample it — but be aware that downsampling loses information.
- **Augment audio data.** Add background noise, vary speed and pitch, simulate different microphones. This dramatically improves robustness.
- **Use pre-trained models.** Whisper for ASR and VITS/Bark for TTS are excellent starting points. Fine-tuning is almost always better than training from scratch.
- **Handle silence.** Voice Activity Detection (VAD) removes silence before processing, saving compute and improving accuracy. Silero VAD and WebRTC VAD are popular choices.
- **Normalise volume.** Different recordings have very different loudness levels. Normalise to a consistent level before processing.

---

## Summary

Speech and audio processing has been revolutionised by deep learning. Modern ASR systems like Whisper approach human-level accuracy across dozens of languages. TTS systems produce speech that is increasingly indistinguishable from human recordings. Voice cloning works from seconds of audio. Music generation, source separation, and environmental sound detection are all advancing rapidly. The field faces ongoing challenges — low-resource languages, noisy environments, ethical concerns around voice cloning — but the trajectory is clear: machines are becoming as good as humans at hearing, understanding, and producing sound.
