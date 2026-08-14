---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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
# Pag-optimize at Deployment ng Modelo
Ang pagsasanay sa isang malaking modelo ng AI ay isang makabuluhang tagumpay, ngunit ang pag-deploy nito nang mahusay ay kung saan ang karamihan sa pagsisikap sa engineering ay kinakailangan. Ang isang modelo na tumatagal ng 10 segundo upang tumugon o nangangailangan ng walong A100 GPU ay hindi praktikal para sa karamihan ng mga real-world na application. Ang pag-optimize ng modelo ay ang proseso ng paggawa ng mga modelo na mas maliit, mas mabilis, at mas cost-effective — habang pinapanatili ang katanggap-tanggap na kalidad. Sinasaklaw ng file na ito ang quantization, pruning, distillation, at ang mga praktikal na tool para sa pag-deploy ng mga modelo sa produksyon.
---

## Bakit Mag-optimize?
| Pag-aalala | Epekto |
|---------|--------|
| **Latency** | Inaasahan ng mga user ang mga tugon sa wala pang 1 segundo; bawat dagdag na 100ms ay nawawalan ng engagement |
| **Gastos** | Ang hinuha ng GPU ay mahal; ang isang 70B na modelo ay nagkakahalaga ng ~$0.05-0.15 bawat 1M token sa cloud hardware |
| **Memory** | Ang isang 7B na modelo sa FP32 ay nangangailangan ng 28 GB ng VRAM; karamihan sa mga consumer GPU ay may 8-24 GB |
| **Enerhiya** | Ang pagpapatakbo ng malalaking modelo ay kumonsumo ng malaking kuryente; mahalaga para sa mobile at edge |
| **Scale** | Ang paglilingkod sa milyun-milyong user ay nangangailangan ng mga modelong akma sa available na hardware |
---

## Quantization
Binabawasan ng quantization ang katumpakan ng mga timbang ng modelo mula sa 32-bit na floating point (FP32) patungo sa mas maliliit na format tulad ng INT8, INT4, o mas mababa pa.
### Mga Format ng Katumpakan
| Format | Bits bawat Timbang | Memory para sa 7B Model | Kalidad |
|---------|----------------|---------------------|---------|
| **FP32** | 32 | 28 GB | Baseline (buong katumpakan) |
| **FP16 / BF16** | 16 | 14 GB | Halos magkapareho sa FP32 |
| **INT8** | 8 | 7 GB | Napakaliit na pagkawala ng kalidad |
| **INT4** | 4 | 3.5 GB | Katamtamang pagkawala ng kalidad; magagamit pa rin |
| **INT3 / INT2** | 3-2 | 2.6-1.75 GB | Makabuluhang pagkawala ng kalidad; yugto ng pananaliksik |
### Paraan ng Quantization
| Paraan | Kapag Nangyari | Paano Ito Gumagana | Kalidad |
|--------|----------------|--------------|---------|
| **Pagkatapos ng Pagsasanay Quantization (PTQ)** | Pagkatapos makumpleto ang pagsasanay | I-calibrate ang modelo sa isang maliit na dataset; mahanap ang pinakamainam na kaliskis | Mabuti para sa INT8; bumababa sa INT4 |
| **GPTQ** | Pagkatapos ng pagsasanay | GPU-friendly na INT4 quantization gamit ang tinatayang pangalawang-order na impormasyon | Magandang kalidad sa INT4 |
| **AWQ** (Activation-aware Weight Quantization) | Pagkatapos ng pagsasanay | Protektahan ang mga kapansin-pansing timbang batay sa mga magnitude ng activation | Mas mahusay kaysa sa GPTQ sa INT4 |
| **GGUF** (llama.cpp format) | Pagkatapos ng pagsasanay | CPU-friendly na quantization; halo-halong katumpakan bawat layer | Na-optimize para sa CPU inference |
| **Quantization-Aware Training (QAT)** | Sa panahon ng pagsasanay | Gayahin ang quantization sa panahon ng pagsasanay upang matutunan ng modelo na makayanan | Pinakamahusay na kalidad; nangangailangan ng muling pagsasanay |
### Praktikal na Epekto
| Modelo | Laki ng FP16 | Sukat ng INT4 | Bilis | Pagkawala ng Kalidad |
|-------|-----------|-----------|---------|-------------|
| **LLaMA 7B** | 14 GB | 3.5 GB | 2-4x | ~1-2% sa mga benchmark |
| **LLaMA 70B** | 140 GB | 35 GB | 2-3x | ~2-3% sa mga benchmark |
---

## Pruning
Tinatanggal ng pruning ang mga hindi kinakailangang timbang o neuron mula sa isang sinanay na modelo.
| Uri | Paglalarawan | Pakinabang | Hamon |
|------|-------------|-----------|-----------|
| **Hindi nakabalangkas** | Alisin ang mga indibidwal na timbang (itakda sa zero) | Pinakamataas na mga ratio ng compression | Nangangailangan ng kalat-kalat na suporta sa hardware |
| **Structured** | Alisin ang buong neuron, attention head, o layer | Direktang binabawasan ang laki ng modelo | Maaaring mawalan ng higit pang kalidad |
| **Batay sa magnitude** | Alisin ang mga timbang na may pinakamaliit na absolute value | Simple; gumagana nang maayos | Maaaring makaligtaan ang mahahalagang maliliit na timbang |
| **Batay sa kahalagahan** | Alisin ang mga timbang batay sa kanilang kontribusyon sa output | Mas mahusay na pangangalaga sa kalidad | Mas mahal ang pag-compute |
### Pruning Pipeline
| Hakbang | Paglalarawan |
|------|-------------|
| 1. Tren | Sanayin ang buong modelo nang normal |
| 2. Iskor | Kalkulahin ang mga marka ng kahalagahan para sa bawat timbang/neuron |
| 3. Prune | Alisin ang hindi gaanong mahahalagang elemento |
| 4. Fine-tune | Muling sanayin upang mabawi ang nawalang katumpakan |
| 5. Ulitin | Ulitin ang pruning at fine-tuning para sa mas mataas na compression |
---

## Paglilinis ng Kaalaman
Pagsasanay ng isang maliit na modelo ng "mag-aaral" upang gayahin ang isang malaking modelo ng "guro".
| Bahagi | Tungkulin |
|-----------|------|
| **Guro** | Malaki, mataas na kalidad na modelo |
| **Mag-aaral** | Maliit na modelo na natututo mula sa guro |
| **Pagkawala ng distillation** | Sinusubukan ng mag-aaral na itugma ang pamamahagi ng output ng guro (mga soft label) |
### Mga Uri ng Distillation
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Batay sa Logit** | Tinutugma ng mag-aaral ang mga probabilidad ng output ng guro | Ang orihinal na distillation ni Hinton |
| **Batay sa tampok** | Tinutugma ng mag-aaral ang mga intermediate na representasyon ng guro | FitNets |
| **Batay sa relasyon** | Tinutugma ng mag-aaral ang mga ugnayan sa pagitan ng mga sample | RKD (Relational Knowledge Distillation) |
| **Walang data** | Walang kinakailangang orihinal na data ng pagsasanay; gamitin ang henerasyon ng guro | DAFL, DeepInversion |
### Mga Kapansin-pansing Halimbawa ng Distillation
| Guro | Mag-aaral | Resulta |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (nabalitaan) | Mas maliit na modelo na may karamihan sa kalidad ng GPT-4 |
| **BERT-Malaki** | DistilBERT | 40% mas maliit, 60% mas mabilis, 97% ng performance ni BERT |
| **LLaMA 70B** | LLaMA 7B (sa pamamagitan ng distillation) | Open-source na maliit na modelo na lumalapit sa malaking kalidad ng modelo |
---

## LLM-Specific Optimisations
### KV-Cache Optimization
Ang mga malalaking modelo ng wika ay nag-cache ng mga pares ng key-value mula sa mga nakaraang token upang maiwasan ang muling pagkalkula.
| Teknik | Paglalarawan | Epekto |
|-----------|-------------|--------|
| **Multi-Query Attention (MQA)** | Ang lahat ng mga pinuno ng atensyon ay nagbabahagi ng isang pares ng KV | Binabawasan ang memorya; bahagyang pagkawala ng kalidad |
| **Grouped-Query Attention (GQA)** | Ang mga pangkat ng mga pinuno ay nagbabahagi ng mga pares ng KV | Balanse sa pagitan ng MQA at karaniwang atensyon |
| **Atensyon sa sliding window** | Dumalo lamang sa mga huling W token | Binabawasan ang laki ng KV-cache para sa mahabang konteksto |
### Speculative Decoding
| Hakbang | Paglalarawan |
|------|-------------|
| 1 | Ang isang maliit na "draft" na modelo ay mabilis na bumubuo ng mga K token |
| 2 | Bine-verify ng malaking modelo ang lahat ng K token sa isang forward pass |
| 3 | Ang mga tinanggap na token ay iniingatan; ang mga tinanggihan ay muling nabuo |
Resulta: 2-3x speedup sa henerasyon na walang pagkawala ng kalidad (ang malaking modelo ay palaging may huling say).
### Flash na Pansin
| Tampok | Paglalarawan |
|---------|-------------|
| **Problema** | Ang karaniwang atensyon ay nangangailangan ng O(n²) na memorya para sa attention matrix |
| **Solusyon** | Kalkulahin ang pansin sa mga bloke; hindi kailanman matutupad ang buong matrix sa memorya |
| **Resulta** | 2-4x na mas mabilis; nagbibigay-daan sa mas mahabang context windows |
| **Mga Variant** | Flash Attention 2 (mas mabilis), FlashDecoding (na-optimize para sa hinuha) |
---

## Mga Framework ng Paghahatid
| Balangkas | Pinakamahusay Para sa | Pangunahing Tampok |
|-----------|----------|-------------|
| **vLLM** | LLM paghahatid | PagedAttention; tuluy-tuloy na batching; mataas na throughput |
| **TensorRT-LLM** | NVIDIA GPU inference | Pinakamataas na pagganap sa NVIDIA hardware |
| **llama.cpp** | CPU at consumer GPU inference | Nagpapatakbo ng mga quantised na modelo sa mga laptop at telepono |
| **Ollama** | Lokal na modelo na tumatakbo | User-friendly na wrapper sa paligid ng llama.cpp |
| **Triton Inference Server** | Multi-framework serving | Sinusuportahan ang TensorFlow, PyTorch, ONNX, TensorRT |
| **TorchServe** | PyTorch model serving | Native PyTorch integration |
| **ONNX Runtime** | Cross-platform inference | Na-optimize na pagpapatupad sa buong hardware |
| **BentoML** | Pag-deploy ng produksyon | Framework-agnostic; humahawak ng packaging at paghahatid |
---

## Mga Pattern ng Deployment
| Pattern | Paglalarawan | Kailan Gagamitin |
|---------|-------------|-------------|
| **Pag-deploy sa gilid** | Magpatakbo ng mga modelo sa mga telepono, IoT device, o naka-embed na hardware | Mababang latency; offline; privacy |
| **Cloud API** | Mag-host ng mga modelo sa cloud GPU; maglingkod sa pamamagitan ng API | Pinakamataas na pagkalkula; pay per use |
| **Hybrid** | Maliit na modelo sa device; malaking modelo sa cloud | Pinakamahusay sa parehong mundo |
| **Walang Server** | I-scale sa zero; magbayad lamang kapag ginamit | Kalat-kalat na trapiko; sensitibo sa gastos |
| **Batch inference** | Iproseso ang data nang maramihan sa isang iskedyul | Kapag hindi kailangan ang real-time |
---

## Pag-benchmark
| Sukatan | Ang Sinusukat Nito |
|--------|-----------------|
| **Mga Token bawat segundo** | Generation throughput (mas mataas ay mas mahusay) |
| **Oras sa unang token (TTFT)** | Latency bago lumabas ang unang token ng output |
| **Latency bawat kahilingan** | Kabuuang oras mula sa input hanggang sa kumpletong output |
| **Paggamit ng memory** | VRAM o RAM na natupok sa panahon ng hinuha |
| ** Throughput** | Mga kahilingang inihain bawat segundo |
| **Gastos sa bawat 1M token** | Dolyar na halaga ng pagproseso ng 1 milyong token |
---

## Mga Praktikal na Tip
- **Magsimula sa quantization.** Ang INT4 quantization (AWQ o GPTQ) ay nagbibigay ng pinakamahusay na kalidad-sa-laki na trade-off. Karamihan sa mga modelong 7B ay kumportableng tumatakbo sa isang consumer GPU sa INT4.
- **Gumamit ng vLLM para sa paghahatid ng LLM.** Ito ang pinakamabilis na opsyong open-source para sa high-throughput na LLM inference.
- **Profile bago mag-optimize.** Sukatin kung saan aktwal na ginugugol ang oras. Madalas memory bandwidth, hindi compute, yun ang bottleneck.
- **Itugma ang modelo sa gawain.** Ang isang 7B na modelo ay mainam para sa karamihan ng mga gawain. Huwag gumamit ng 70B kapag gagawin ang 7B.
- **Isaalang-alang ang distillation.** Kung kailangan mo ng maliit, mabilis na modelo para sa produksyon, distil mula sa mas malaking modelo sa halip na magsanay mula sa simula.
- **Patuloy na subaybayan.** Maaaring bumaba ang pagganap ng modelo sa paglipas ng panahon habang nagbabago ang mga pamamahagi ng data. Subaybayan ang latency, throughput, at mga sukatan ng kalidad.
---

## Buod
Ang pag-optimize ng modelo ay ang tulay sa pagitan ng pananaliksik at produksyon. Pinaliit ng quantization ang mga modelo ng 4-8x na may kaunting pagkawala ng kalidad. Tinatanggal ng pruning ang patay na timbang. Ang distillation ay naglilipat ng kaalaman mula sa malaki patungo sa maliliit na modelo. Ang Flash Attention at KV-cache trick ay nagpapabilis ng hinuha. Magkasama, ginagawa ng mga diskarteng ito ang isang modelo na nangangailangan ng data center sa isa na tumatakbo sa isang laptop o telepono. Mabilis ang takbo ng field — ang kailangan ng walong A100 noong nakaraang taon ay tumatakbo sa isang consumer GPU ngayon.