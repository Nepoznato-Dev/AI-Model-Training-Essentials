# Teknoloji Glossary

A Referans glossary covering AI models, hardware, benchmarks, ve core concepts
içinde bu modern AI ve Bilişim landscape.

---

## AI Dil Models ve Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released içinde November 2022.
It is powered by bu GPT series içinde large Dil models (LLMs). ChatGPT is one
içinde bu fastest-growing consumer AI products içinde Tarih, reaching 100 million
users within two months içinde launch. It supports text-based conversation, code
generation, summarisation, ve creative writing. Paid tiers provide access to
more powerful models such as GPT-4 ve GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family içinde large Dil models created by OpenAI. bu Mimari
uses a decoder-only Transformer trained ile a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
için "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via bu API), GPT-3.5 (bu backbone içinde bu original ChatGPT), ve GPT-4
(2023, multimodal, Performans close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, bu founder içinde information theory. Anthropic was founded by former
OpenAI researchers ve focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set içinde principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known için long context windows (up
to 200,000 tokens), nuanced reasoning, ve reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family içinde multimodal AI models, announced içinde
December 2023. Gemini is natively multimodal — trained from bu ground up on
text, images, audio, ve video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), ve Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) ve Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small Dil model (SLM) developed by Microsoft ile 3.8B
parameters. It was released içinde April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises Veri quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU ve
HumanEval. It supports a 4k token context window içinde its base variant ve a 128k
window içinde bu long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone ile sufficient RAM.

### Llama (Meta AI)
Llama (Large Dil Model Meta AI) is an open-weights family içinde models
released by Meta. Llama 2 (2023) was released için research ve commercial use
ile sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
Performans significantly, ile models ranging from 8B to 70B (ve later 400B+).
Because bu weights are publicly downloadable, Llama models are bu foundation
için a large ecosystem içinde fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
ve are widely used için local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open ve proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match bu
Performans içinde much larger models using efficient techniques such as sliding
window attention ve grouped-query attention. Mixtral 8x7B (2024) is a mixture-
içinde-experts model — it routes each token to a subset içinde 8 expert networks,
achieving GPT-3.5-level Performans while being computationally cheaper.
Mistral's models are fully open-weight ve can be run locally.

---

## GPU Hardware ve Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed için massively parallel computation. Originally
built için rendering 3D graphics, GPUs have become essential için AI/ML training
ve inference because they can perform thousands içinde floating-point operations
simultaneously using thousands içinde small cores. bu two main GPU manufacturers
için AI are NVIDIA ve AMD.

### NVIDIA GeForce RTX Series
bu RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) ve RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores için accelerating AI operations. VRAM (video RAM) is
critical için running AI models locally — an 8GB GPU can handle 7B parameter
models içinde 4-bit quantisation; a 24GB GPU can handle 70B models içinde 4-bit.

### NVIDIA A-Series ve H-Series (Veri Centre)
bu A100 (Ampere, 2020) ve H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB içinde HBM3 memory ve is bu standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× bu AI throughput içinde consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. bu RX 7900 XTX (2022) has 24GB VRAM ve can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA için AI frameworks, though Destek is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting içinde 2022. Arc
GPUs Destek XeSS (Intel's super-sampling) ve have limited but growing Destek
için AI inference tasks via OpenVINO ve IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications Veritabanı at ark.intel.com. It
provides detailed technical specifications için every Intel CPU, GPU, FPGA, ve
NUC product, including core counts, clock speeds, TDP, supported memory types,
ve instruction-set features. When you hear "check ARK için specs," it means
visiting that Veritabanı için authoritative hardware information.

---

## AI Performans Benchmarks

### MMLU (Massive Multitask Dil Understanding)
MMLU is a benchmark Test Etme LLM knowledge across 57 academic subjects including
mathematics, Tarih, Hukuk, Tıp, ve computer Bilim. It consists içinde
multiple-choice questions drawn from real university-level exams. A score içinde
70% is roughly human undergraduate level; GPT-4 ve Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark için code generation. It consists içinde 164 Python
programming problems ile automated test cases. Models are measured on
pass@k — bu probability that at least one içinde k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity ve must choose bu most likely continuation from
four options. bu incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding içinde physical
ve social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from bu Allen Institute için AI. It consists içinde grade-school
Bilim questions, split into "Easy" ve "Challenge" sets. bu Challenge set
contains questions that retrieval-based methods ve simple statistical models
struggle ile, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
Veritabanı) ile a Dil model. Instead içinde relying solely on bu model's
parametric knowledge, RAG first retrieves relevant documents from an external
Bilgi Tabanı ve then includes them içinde bu model's context. This allows bu
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form içinde RAG — it retrieves from its KB
ve includes bu results içinde bu context before generating a response.

### Fine-tuning
Fine-tuning is bu process içinde continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts bu model's weights için a
particular task or domain. için example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces bu numerical precision içinde model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
içinde 16-bit precision requires ~14GB VRAM; bu same model içinde 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation ve is bu main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
bu context window is bu maximum number içinde tokens a model can process at once,
including both bu prompt ve bu generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo ve Claude 3 Destek 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows bu model to "see"
more içinde a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Geri Bildirim)
RLHF is bu training technique that transforms a base Dil model (which
simply predicts bu next token) into an assistant that follows instructions ve
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, ve bu Dil model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, ve Gemini all use
variants içinde RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer Mimari
bu Transformer is bu neural Ağ Mimari underlying all modern LLMs.
Introduced içinde bu 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens içinde parallel rather than
sequentially. Encoder-only Transformers (BERT) are used için understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used için generation tasks;
encoder-decoder Transformers (T5, BART) are used için translation ve summarisation.

### Embeddings ve Vector Databases
Embeddings are dense numerical representations içinde text (or images) produced by
a neural Ağ. Semantically similar texts have embeddings that are close içinde
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings ve Destek fast approximate nearest-neighbour search. They are
bu storage backbone içinde RAG Sistemler, including Potato.ai's cold-memory layer.
