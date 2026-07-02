<!-- 
This file was automatically translated from English to German.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie Glossary

A Referenz glossary covering AI models, hardware, benchmarks, und core concepts
in der/die/das modern AI und Datenverarbeitung landscape.

---

## AI Sprache Models und Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released in November 2022.
It is powered by der/die/das GPT series von large Sprache models (LLMs). ChatGPT is one
von der/die/das fastest-growing consumer AI products in Geschichte, reaching 100 million
users within two months von launch. It supports text-based conversation, code
generation, summarisation, und creative writing. Paid tiers provide access to
more powerful models such as GPT-4 und GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family von large Sprache models created by OpenAI. der/die/das Architektur
uses a decoder-only Transformer trained mit a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
für "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via der/die/das API), GPT-3.5 (der/die/das backbone von der/die/das original ChatGPT), und GPT-4
(2023, multimodal, Leistung close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, der/die/das founder von information theory. Anthropic was founded by former
OpenAI researchers und focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set von principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known für long context windows (up
to 200,000 tokens), nuanced reasoning, und reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family von multimodal AI models, announced in
December 2023. Gemini is natively multimodal — trained from der/die/das ground up on
text, images, audio, und video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), und Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) und Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small Sprache model (SLM) developed by Microsoft mit 3.8B
parameters. It was released in April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises Daten quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU und
HumanEval. It supports a 4k token context window in its base variant und a 128k
window in der/die/das long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone mit sufficient RAM.

### Llama (Meta AI)
Llama (Large Sprache Model Meta AI) is an open-weights family von models
released by Meta. Llama 2 (2023) was released für research und commercial use
mit sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
Leistung significantly, mit models ranging from 8B to 70B (und later 400B+).
Because der/die/das weights are publicly downloadable, Llama models are der/die/das foundation
für a large ecosystem von fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
und are widely used für local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open und proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match der/die/das
Leistung von much larger models using efficient techniques such as sliding
window attention und grouped-query attention. Mixtral 8x7B (2024) is a mixture-
von-experts model — it routes each token to a subset von 8 expert networks,
achieving GPT-3.5-level Leistung while being computationally cheaper.
Mistral's models are fully open-weight und can be run locally.

---

## GPU Hardware und Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed für massively parallel computation. Originally
built für rendering 3D graphics, GPUs have become essential für AI/ML training
und inference because they can perform thousands von floating-point operations
simultaneously using thousands von small cores. der/die/das two main GPU manufacturers
für AI are NVIDIA und AMD.

### NVIDIA GeForce RTX Series
der/die/das RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) und RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores für accelerating AI operations. VRAM (video RAM) is
critical für running AI models locally — an 8GB GPU can handle 7B parameter
models in 4-bit quantisation; a 24GB GPU can handle 70B models in 4-bit.

### NVIDIA A-Series und H-Series (Daten Centre)
der/die/das A100 (Ampere, 2020) und H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB von HBM3 memory und is der/die/das standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× der/die/das AI throughput von consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. der/die/das RX 7900 XTX (2022) has 24GB VRAM und can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA für AI frameworks, though support is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting in 2022. Arc
GPUs support XeSS (Intel's super-sampling) und have limited but growing support
für AI inference tasks via OpenVINO und IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications Datenbank at ark.intel.com. It
provides detailed technical specifications für every Intel CPU, GPU, FPGA, und
NUC product, including core counts, clock speeds, TDP, supported memory types,
und instruction-set features. When you hear "check ARK für specs," it means
visiting that Datenbank für authoritative hardware information.

---

## AI Leistung Benchmarks

### MMLU (Massive Multitask Sprache Understanding)
MMLU is a benchmark Testen LLM knowledge across 57 academic subjects including
mathematics, Geschichte, Recht, Medizin, und computer Wissenschaft. It consists von
multiple-choice questions drawn from real university-level exams. A score von
70% is roughly human undergraduate level; GPT-4 und Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark für code generation. It consists von 164 Python
programming problems mit automated test cases. Models are measured on
pass@k — der/die/das probability that at least one von k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity und must choose der/die/das most likely continuation from
four options. der/die/das incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding von physical
und social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from der/die/das Allen Institute für AI. It consists von grade-school
Wissenschaft questions, split into "Easy" und "Challenge" sets. der/die/das Challenge set
contains questions that retrieval-based methods und simple statistical models
struggle mit, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
Datenbank) mit a Sprache model. Instead von relying solely on der/die/das model's
parametric knowledge, RAG first retrieves relevant documents from an external
Wissensdatenbank und then includes them in der/die/das model's context. This allows der/die/das
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form von RAG — it retrieves from its KB
und includes der/die/das results in der/die/das context before generating a response.

### Fine-tuning
Fine-tuning is der/die/das process von continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts der/die/das model's weights für a
particular task or domain. für example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces der/die/das numerical precision von model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
in 16-bit precision requires ~14GB VRAM; der/die/das same model in 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation und is der/die/das main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
der/die/das context window is der/die/das maximum number von tokens a model can process at once,
including both der/die/das prompt und der/die/das generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo und Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows der/die/das model to "see"
more von a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF is der/die/das training technique that transforms a base Sprache model (which
simply predicts der/die/das next token) into an assistant that follows instructions und
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, und der/die/das Sprache model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, und Gemini all use
variants von RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer Architektur
der/die/das Transformer is der/die/das neural Netzwerk Architektur underlying all modern LLMs.
Introduced in der/die/das 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens in parallel rather than
sequentially. Encoder-only Transformers (BERT) are used für understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used für generation tasks;
encoder-decoder Transformers (T5, BART) are used für translation und summarisation.

### Embeddings und Vector Databases
Embeddings are dense numerical representations von text (or images) produced by
a neural Netzwerk. Semantically similar texts have embeddings that are close in
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings und support fast approximate nearest-neighbour search. They are
der/die/das storage backbone von RAG Systeme, including Potato.ai's cold-memory layer.
