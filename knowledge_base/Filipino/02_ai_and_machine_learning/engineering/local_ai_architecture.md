<!--
---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Lokal na Arkitektura ng AI
Isang praktikal na gabay sa pagpapatakbo ng malalaking modelo ng wika na ganap na nasa device — mga pagsasaalang-alang sa hardware, inference engine, pag-optimize ng memorya, at disenyo ng system para sa edge deployment.
---

## Bakit Lokal na Patakbuhin ang AI?
- **Privacy**: Walang data na umalis sa device.
- **Gastos**: Walang mga bayarin sa API bawat token.
- **Latency**: Mahuhulaan, walang network na hinuha.
- **Offline availability**: Gumagana nang walang internet.
- **Control**: Ganap na kontrol sa bersyon ng modelo, pag-customize, at fine-tuning.
---

## Mga Kinakailangan sa Hardware
### GPU Memory (VRAM)
Ang pinaka-kritikal na mapagkukunan. Laki ng modelo sa memorya ≈ **mga parameter × byte bawat parameter**.
| Katumpakan | Byte bawat parameter | 3.8B na modelo | 7B na modelo | 13B na modelo | 70B na modelo |
|-----------|---------------------|------------|----------|----------|-----------|
| FP32 | 4 | ~15 GB | ~28 GB | ~52 GB | ~280 GB |
| FP16 | 2 | ~7.6 GB | ~14 GB | ~26 GB | ~140 GB |
| INT8 (8-bit) | 1 | ~3.8 GB | ~7 GB | ~13 GB | ~70 GB |
| INT4 (4-bit) | 0.5 | ~1.9 GB | ~3.5 GB | ~6.5 GB | ~35 GB |
**Mga praktikal na alituntunin:**
- 8GB VRAM → hanggang sa 7B na mga modelo sa 4-bit.
- 12GB VRAM → hanggang sa 13B na mga modelo sa 4-bit.
- 24GB VRAM → hanggang sa 70B na mga modelo sa 4-bit (o 13B sa 8-bit).
- Ang Apple Silicon (pinag-isang memorya) ay maaaring magpatakbo ng 70B na mga modelo sa 64GB+ na mga system.
### RAM (System Memory)
- Para sa hinuha ng CPU, kailangan mo ng sapat na RAM ng system upang mai-load ang modelo (katulad ng mga numero ng VRAM).
- Para sa GPU inference, mahalaga ang system RAM para sa pag-load ng modelo sa memorya bago i-offload sa VRAM.
### Imbakan
- Ang mga quantised model weight ay tumatagal ng ilang GB (hal., 4-bit 7B ≈ 4 GB sa disk). Tiyaking libre ang hindi bababa sa 20–50 GB para sa maraming modelo.
### CPU
- Para sa agarang pagpoproseso (prefill) at CPU-offloading, nakakatulong ang modernong multi-core na CPU.
- Ang Apple M-series chips ay may mahusay na pagganap para sa mga LLM dahil sa pinag-isang memorya at Neural Engine.
---

## Quantization
Binabawasan ng quantization ang numerical precision ng mga timbang, kapansin-pansing pagputol ng memorya at pagtaas ng bilis sa isang maliit na halaga ng katumpakan.
### Mga Sikat na Format
| Format | Bits | Paglalarawan | Karaniwang paggamit |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp na format, na-optimize para sa CPU/GPU hybrid | Pinakamahusay para sa lokal na hinuha |
| **GPTQ** | 4–8 | GPU-only, mahusay sa CUDA | Pinakamahusay para sa mga NVIDIA GPU |
| **AWQ** | 4 | Aktibo-alam, GPU-lamang | Mabuti para sa batch inference sa mga GPU |
| **ONNX** | variable | Standardised, cross-platform | Paghahatid ng produksyon |
### Pagpili ng Quantization Level
- **Q8_0** (8-bit): kaunting pagkawala ng kalidad, pinakamalaking laki.
- **Q6_K** (6-bit): magandang kalidad, disenteng compression.
- **Q5_K_M** (5-bit): karaniwang sweet spot.
- **Q4_K_M** (4-bit): pinakamaliit, katanggap-tanggap na kalidad para sa karamihan ng mga gawain.
- **IQ4_XS** / **IQ3_XS**: Pinahusay na quantization na may mas magandang perplexity sa 4/3 bits.
**Rule of thumb:** Gamitin ang Q4_K_M para sa magandang balanse ng kalidad at laki. Kung mayroon kang dagdag na VRAM, gamitin ang Q5 o Q6.
---

## Mga Inference Engine (Lokal)
### llama.cpp
- Nakasulat sa C++.
- Sinusuportahan ang GGUF format.
- Na-optimize para sa CPU at GPU (sa pamamagitan ng CUDA, Metal, OpenCL).
- Napakabilis, lalo na sa CPU.
- Command-line, server mode, at Python bindings.
**Halimbawang utos:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Binabalot ang llama.cpp ng isang simpleng CLI at REST API.
- Auto-download ng mga modelo, pinamamahalaan ang mga ito.
- Mahusay para sa prototyping at desktop apps.
- Sinusuportahan ang mga custom na Modelfile para sa mga prompt ng system.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Graphical na desktop app para sa Windows, macOS, Linux.
- Isang-click na pag-download at interface ng chat.
- Built-in na lokal na server na may OpenAI-compatible na API.
- Mabuti para sa mga hindi teknikal na gumagamit at mabilis na pagsubok.
### Hugging Face Transformers + bitsandbytes
- Ang karaniwang library ng Python para sa mga modelong HF.
- Gamitin ang`bitsandbytes`para sa 4-bit na quantization (`load_in_4bit=True`).
- Mas flexible para sa fine-tuning ngunit mas mabagal kaysa sa llama.cpp para sa hinuha.
### ExLlamaV2
- Napakabilis na GPU inference para sa GPTQ at AWQ.
- Pinakamahusay na pagganap sa mga NVIDIA GPU.
- Sinusuportahan ang batched na henerasyon.
### mlx (Mansanas)
- Framework ng Apple para sa M-series chips.
- Lubos na na-optimize para sa Apple Silicon.
- Python API.
---

## Pamamahala ng Memory
### Context Window at KV Cache
Ang cache ng KV ay nag-iimbak ng mga pares ng key-value para sa bawat layer at bawat token sa konteksto. Lumalaki ito nang linear na may haba ng konteksto.
Gastos ng memorya ≈ 2 × layer × (KV heads × head dim) × token × byte bawat value
Para sa isang 32-layer na modelo na may 8 KV head at 128 head dim, ang bawat token ay nagkakahalaga ng ~32 × 8 × 128 × 2 bytes = 65 KB bawat token. Para sa 128k token, iyon ay ~8 GB para lang sa cache.
### Mga Diskarte sa Pag-offload
- **Layer offloading**: Maglagay ng ilang layer sa GPU, ang iba sa CPU. Mas mabilis kaysa sa purong CPU, mas mababa ang kinakailangan sa VRAM.
- **Token streaming**: Iproseso ang mga token nang unti-unti kaysa nang sabay-sabay.
### Prompt Caching
Muling gamitin ang mga cache ng KV sa mga katulad na prompt para maiwasan ang muling pag-compute sa yugto ng prefill. Sinusuportahan ito ng ilang frameworks (hal., vLLM, llama.cpp na may`--prompt-cache`).
### Mga File na Naka-Memorya
I-load ang mga timbang ng modelo nang direkta mula sa disk nang hindi ganap na nilo-load ang mga ito sa RAM (kapaki-pakinabang para sa malalaking modelo sa mga system na limitado ang memorya). Ang llama.cpp ay gumagamit ng memory-mapping bilang default.
---

## Mga Arkitektura ng Deployment
### Single-Device Mode
Gumagana ang isang modelo sa isang makina (laptop, smartphone, edge device). Ginagamit para sa mga personal na katulong, mga app sa pagkuha ng tala, pagkumpleto ng code.
### Hybrid Edge-Cloud
Pinangangasiwaan ng lokal na modelo ang mga karaniwang query; fallback sa isang cloud model para sa mga kumplikadong tanong. Nagbibigay ito ng pinakamahusay sa parehong mundo — bilis/pribado para sa karamihan, kakayahan para sa mga edge na kaso.
### Naipamahagi na Hinuha (Multi-GPU)
Para sa mas malalaking modelo, hatiin ang mga layer sa maraming GPU (tensor parallelism) o hatiin ang konteksto sa mga device (pipeline parallelism). Gamitin ang llama.cpp sa`-ngl`o ExLlamaV2 sa`--num-gpu-layers`.
### Mobile Deployment
- **Android**: Gamitin ang llama.cpp sa pamamagitan ng JNI bindings o ML Kit.
- **iOS**: Gamitin ang llama.cpp sa pamamagitan ng Swift bindings o mlx.
- **Web**: Gamitin ang WebLLM (tumatakbo sa WebGPU sa pamamagitan ng ONNX runtime) o transformers.js.
---

## Pag-optimize ng Pagganap
### Flash na Pansin
Pinapabilis ang pag-compute ng atensyon at binabawasan ang paggamit ng memorya. Available sa llama.cpp, ExLlamaV2, at mga modernong transformer library.
### Batch Inference
Iproseso ang maraming prompt sa isang solong forward pass. Tumataas nang husto ang throughput. Gamitin ang`llama-batch`o vLLM.
### Maagang Paghinto / Pagbabadyet ng Token
Magtakda ng maximum na token budget para maiwasan ang unbounded generation.
### Speculative Decoding
Gumamit ng maliit na mabilis na modelo (draft) upang mahulaan ang mga token, pagkatapos ay i-verify gamit ang malaking modelo nang magkatulad. Maaaring magbunga ng 2–3× speedup.
---

## Praktikal na Gabay sa Pag-setup
### 1. I-install ang Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Hilahin ang isang Modelo
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Patakbuhin gamit ang API
```bash
ollama serve
```

Pagkatapos ay magpadala ng mga kahilingan sa`http://localhost:11434/api/generate`.
### 4. Pagsasama ng Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternatibong) Direktang gamitin ang llama.cpp
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Pagsubaybay at Pagmamasid
- Subaybayan ang paggamit ng GPU (`nvidia-smi`sa Linux, Activity Monitor sa macOS).
- Subaybayan ang paggamit ng memory (RAM at VRAM).
- Subaybayan ang mga token bawat segundo (throughput).
- Subaybayan ang oras sa unang token (latency).
- Gumamit ng built-in na pag-log mula sa llama.cpp o Ollama.
---

## Mga Limitasyon at Tradeoff
- **Ang agwat sa kalidad**: Ang mga maliliit na lokal na modelo (3.8B–7B) ay karaniwang hindi gumaganap ng malalaking modelo ng ulap (GPT-4, Claude 3.5) sa kumplikadong pangangatwiran.
- **Knowledge cutoff**: Ang kaalaman sa modelo ay nagyelo sa oras ng pagsasanay; gamitin ang RAG upang mag-iniksyon ng kasalukuyang impormasyon.
- **Multilingual**: Ang mas maliliit na modelo ay maaaring magkaroon ng mas kaunting kakayahan sa multilingguwal.
- **Paggamit ng tool**: Maaaring hindi gaanong maaasahan ang mga ahente ng workflow (function calling) sa maliliit na modelo.
Para sa maraming pang-araw-araw na gawain (pagbubuod, Q&A, pagkumpleto ng code, pag-uuri), ang mga lokal na modelo ay sapat na at mabilis na bumubuti.