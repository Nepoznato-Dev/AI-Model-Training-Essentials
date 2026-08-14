---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
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

Multimodal AI systems process and combine information from multiple types of data — text, images, audio, video, and more — simultaneously. While earlier AI systems were typically single-modality (text-only, image-only), the most capable modern systems are multimodal. GPT-4V reads images and text together; Gemini processes text, images, audio, and video natively; and systems like Sora generate video from text descriptions. This file covers how multimodal AI works, the architectures behind it, and why combining modalities is so powerful.

---

## Why Multimodal?

| Benefit | Description | Example |
|---------|-------------|---------|
| **Richer understanding** | Different modalities provide complementary information | A video conveys motion, sound, and context that text alone cannot |
| **Better generalisation** | Learning across modalities creates more robust representations | A model that has seen both images and text descriptions of "cat" understands the concept better |
| **More natural interaction** | Humans communicate through multiple channels | Voice assistants that see what you're pointing at |
| **Cross-modal transfer** | Knowledge from one modality helps with another | Image understanding improves text generation, and vice versa |

---

## Core Architectures

### Vision-Language Models (VLMs)

Models that process both images and text together.

| Architecture | How It Works | Examples |
|-------------|-------------|---------|
| **Dual encoder** | Separate encoders for image and text; combine at a later stage | CLIP, ALIGN |
| **Fusion encoder** | Image and text tokens are interleaved and processed together | Flamingo, Gemini |
| **Cross-attention** | Text tokens attend to image features (or vice versa) | Flamingo, CoCa |
| **Unified tokeniser** | Images are converted to tokens and processed alongside text tokens | Gemini, Chameleon |

### How Vision-Language Models Work

| Step | Description |
|------|-------------|
| **1. Encode image** | A vision encoder (ViT, SigLIP) converts the image into a set of feature vectors |
| **2. Encode text** | A language encoder processes the text tokens |
| **3. Fuse modalities** | Image features are projected into the language model's embedding space |
| **4. Generate** | The language model produces text conditioned on both image and text inputs |

### Key Vision-Language Models

| Model | Developer | Architecture | Notable Feature |
|-------|-----------|-------------|-----------------|
| **CLIP** | OpenAI | Dual encoder (ViT + text encoder) | Zero-shot image classification via text |
| **LLaVA** | Open-source | LLaMA + CLIP visual encoder | Open-source VLM; strong community |
| **GPT-4V / 4o** | OpenAI | Unified multimodal | Processes text, images, audio together |
| **Gemini** | Google DeepMind | Natively multimodal from training | Built for multimodal from the ground up |
| **Claude** | Anthropic | Vision + text | Strong at document and chart understanding |
| **Qwen-VL** | Alibaba | Open-weight VLM | Competitive with closed models |
| **InternVL** | Open-source | Multi-scale vision encoder | Strong open-source option |

---

## Audio and Speech Models

### Speech Recognition (ASR)

| Model | Architecture | Notable Feature |
|-------|-------------|-----------------|
| **Whisper** (OpenAI) | Encoder-decoder Transformer | Trained on 680K hours of multilingual audio; robust |
| **Conformer** | Convolution + self-attention | Combines local and global features |
| **wav2vec 2.0** | Self-supervised | Learns from unlabelled speech |
| **USM** (Google) | Universal speech model | 2M hours of labelled data; 300+ languages |

### Text-to-Speech (TTS)

| Model | Approach | Notable Feature |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Neural codec | Voice cloning from 3-second sample |
| **Bark** (Suno) | Transformer-based | Multilingual; includes non-speech sounds |
| **ElevenLabs** | Commercial | High-quality voice cloning |
| **ChatTTS** | Open-source | Conversational speech with natural prosody |
| **Fish Speech** | Open-source | Multilingual; fast inference |

### Audio Understanding

| Model | Capability |
|-------|-----------|
| **AudioLDM** | Sound effect generation from text |
| **MusicGen** (Meta) | Text-to-music generation |
| **Qwen-Audio** | Audio understanding (speech, music, environmental sounds) |
| **SALMONN** | Speech, audio, language, music, and noise understanding |

---

## Video Models

Video combines images, audio, text, and time — making it the most complex modality.

| Model | Type | Capability |
|-------|------|-------------|
| **Sora** (OpenAI) | Text-to-video | Up to 1080p; understands physics |
| **Gemini** | Video understanding | Can analyse long videos with audio |
| **Video-LLaVA** | Video + text | Open-source video understanding |
| **Runway Gen-3** | Text/image-to-video | Commercial video generation |
| **Kling** | Text-to-video | Long-form video generation |

### Video Understanding Challenges

| Challenge | Description |
|-----------|-------------|
| **Temporal reasoning** | Understanding events that unfold over time |
| **Long context** | Videos can be hours long; processing all frames is expensive |
| **Audio-visual sync** | Connecting what's said with what's shown |
| **Causality** | Understanding cause and effect in video sequences |

---

## Cross-Modal Retrieval

Finding relevant content across different modalities.

| Task | Description | Example |
|------|-------------|---------|
| **Text → Image** | Find images matching a text query | Search "sunset over mountains" in a photo library |
| **Image → Text** | Find text relevant to an image | Generating captions for images |
| **Text → Audio** | Find sounds matching a description | Sound design: "footsteps on gravel" |
| **Image → Image** | Find visually similar images | Product search by image |

### CLIP for Cross-Modal Retrieval

CLIP's shared embedding space enables zero-shot cross-modal retrieval:

| Step | Description |
|------|-------------|
| 1 | Encode all images with the vision encoder |
| 2 | Encode the text query with the text encoder |
| 3 | Compute cosine similarity between text embedding and all image embeddings |
| 4 | Return the images with highest similarity |

This works without any task-specific training — a property called **zero-shot** capability.

---

## Embodied AI

Embodied AI combines multimodal perception with physical action.

| System | Modality | Application |
|--------|----------|-------------|
| **RT-2** (Google) | Vision + language → robot actions | General-purpose robot control from text instructions |
| **Octo** | Open-source robot policy | Trained on diverse robot data |
| **Tesla Optimus** | Vision + language → physical tasks | Humanoid robot for general tasks |
| **Figure 01** | Vision + language + speech | Humanoid robot with conversational ability |

### Challenges in Embodied AI

| Challenge | Why It's Hard |
|-----------|--------------|
| **Sim-to-real gap** | Simulation doesn't perfectly capture real-world physics |
| **Dexterity** | Fine motor control (hands, fingers) is extremely difficult |
| **Safety** | Physical robots can cause real harm |
| **Real-time processing** | Must perceive, decide, and act in milliseconds |
| **Generalisation** | A robot trained to pick up red cups may fail on blue ones |

---

## Data and Training

### Multimodal Training Data

| Dataset | Modalities | Size |
|---------|-----------|------|
| **LAION-5B** | Image-text pairs | 5.85 billion pairs |
| **DataComp** | Curated image-text | Benchmark for dataset design |
| **WIT** (Wikipedia) | Image-text from Wikipedia | 11.5 million pairs |
| **HowTo100M** | Video-text (how-to videos) | 100 million clips |
| **LibriSpeech** | Speech-text | 1,000 hours of English |
| **Common Voice** | Speech-text | Multilingual; community-contributed |

### Training Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Joint training** | Train on all modalities simultaneously | When you have aligned multimodal data |
| **Curriculum learning** | Start with easy examples; increase difficulty | Improves convergence |
| **Contrastive learning** | Learn to match related pairs across modalities (CLIP-style) | Building shared representations |
| **Instruction tuning** | Train on multimodal instruction-response pairs | Making models follow multimodal instructions |

---

## Evaluation

| Benchmark | Modalities | What It Tests |
|-----------|-----------|---------------|
| **MMLU** | Text | Knowledge across 57 subjects |
| **MMMU** | Text + images | College-level reasoning with diagrams |
| **MathVista** | Text + images | Mathematical reasoning with visual data |
| **Video-MME** | Text + video | Video understanding and temporal reasoning |
| **HELMET** | Text + audio | Long-context multimodal evaluation |
| **SWE-bench** | Text + code | Real-world software engineering tasks |

---

## Summary

Multimodal AI represents the shift from single-purpose models to systems that perceive and reason across all forms of data. Vision-language models like GPT-4V and Gemini can understand images and text together; speech models like Whisper and VALL-E handle audio; video models are beginning to process the full complexity of moving images with sound. The trend is clear: the most capable AI systems of the future will be natively multimodal, processing all types of information simultaneously. The challenges — data alignment, computational cost, evaluation, and embodied deployment — are significant, but the progress in 2024–2026 has been rapid.
