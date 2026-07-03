<!-- 
This file was automatically translated from English to Spanish.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnología Glossary

A Referencia glossary covering AI models, hardware, benchmarks, y core concepts
en el/la modern AI y Informática landscape.

---

## AI Idioma Models y Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released en November 2022.
It is powered by el/la GPT series de large Idioma models (LLMs). ChatGPT is one
de el/la fastest-growing consumer AI products en Historia, reaching 100 million
users within two months de launch. It supports text-based conversation, code
generation, summarisation, y creative writing. Paid tiers provide access to
more powerful models such as GPT-4 y GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family de large Idioma models created by OpenAI. el/la Arquitectura
uses a decoder-only Transformer trained con a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
para "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via el/la API), GPT-3.5 (el/la backbone de el/la original ChatGPT), y GPT-4
(2023, multimodal, Rendimiento close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, el/la founder de information theory. Anthropic was founded by former
OpenAI researchers y focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set de principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known para long context windows (up
to 200,000 tokens), nuanced reasoning, y reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family de multimodal AI models, announced en
December 2023. Gemini is natively multimodal — trained from el/la ground up on
text, images, audio, y video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), y Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) y Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small Idioma model (SLM) developed by Microsoft con 3.8B
parameters. It was released en April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises Datos quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU y
HumanEval. It supports a 4k token context window en its base variant y a 128k
window en el/la long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone con sufficient RAM.

### Llama (Meta AI)
Llama (Large Idioma Model Meta AI) is an open-weights family de models
released by Meta. Llama 2 (2023) was released para research y commercial use
con sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
Rendimiento significantly, con models ranging from 8B to 70B (y later 400B+).
Because el/la weights are publicly downloadable, Llama models are el/la foundation
para a large ecosystem de fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
y are widely used para local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open y proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match el/la
Rendimiento de much larger models using efficient techniques such as sliding
window attention y grouped-query attention. Mixtral 8x7B (2024) is a mixture-
de-experts model — it routes each token to a subset de 8 expert networks,
achieving GPT-3.5-level Rendimiento while being computationally cheaper.
Mistral's models are fully open-weight y can be run locally.

---

## GPU Hardware y Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed para massively parallel computation. Originally
built para rendering 3D graphics, GPUs have become essential para AI/ML training
y inference because they can perform thousands de floating-point operations
simultaneously using thousands de small cores. el/la two main GPU manufacturers
para AI are NVIDIA y AMD.

### NVIDIA GeForce RTX Series
el/la RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) y RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores para accelerating AI operations. VRAM (video RAM) is
critical para running AI models locally — an 8GB GPU can handle 7B parameter
models en 4-bit quantisation; a 24GB GPU can handle 70B models en 4-bit.

### NVIDIA A-Series y H-Series (Datos Centre)
el/la A100 (Ampere, 2020) y H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB de HBM3 memory y is el/la standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× el/la AI throughput de consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. el/la RX 7900 XTX (2022) has 24GB VRAM y can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA para AI frameworks, though Soporte is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting en 2022. Arc
GPUs Soporte XeSS (Intel's super-sampling) y have limited but growing Soporte
para AI inference tasks via OpenVINO y IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications Base de datos at ark.intel.com. It
provides detailed technical specifications para every Intel CPU, GPU, FPGA, y
NUC product, including core counts, clock speeds, TDP, supported memory types,
y instruction-set features. When you hear "check ARK para specs," it means
visiting that Base de datos para authoritative hardware information.

---

## AI Rendimiento Benchmarks

### MMLU (Massive Multitask Idioma Understanding)
MMLU is a benchmark Pruebas LLM knowledge across 57 academic subjects including
mathematics, Historia, Derecho, Medicina, y computer Ciencia. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 y Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark para code generation. It consists de 164 Python
programming problems con automated test cases. Models are measured on
pass@k — el/la probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity y must choose el/la most likely continuation from
four options. el/la incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding de physical
y social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from el/la Allen Institute para AI. It consists de grade-school
Ciencia questions, split into "Easy" y "Challenge" sets. el/la Challenge set
contains questions that retrieval-based methods y simple statistical models
struggle con, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
Base de datos) con a Idioma model. Instead de relying solely on el/la model's
parametric knowledge, RAG first retrieves relevant documents from an external
Base de conocimientos y then includes them en el/la model's context. This allows el/la
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form de RAG — it retrieves from its KB
y includes el/la results en el/la context before generating a response.

### Fine-tuning
Fine-tuning is el/la process de continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts el/la model's weights para a
particular task or domain. para example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces el/la numerical precision de model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
en 16-bit precision requires ~14GB VRAM; el/la same model en 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation y is el/la main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
el/la context window is el/la maximum number de tokens a model can process at once,
including both el/la prompt y el/la generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo y Claude 3 Soporte 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows el/la model to "see"
more de a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Comentarios)
RLHF is el/la training technique that transforms a base Idioma model (which
simply predicts el/la next token) into an assistant that follows instructions y
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, y el/la Idioma model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, y Gemini all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer Arquitectura
el/la Transformer is el/la neural Red Arquitectura underlying all modern LLMs.
Introduced en el/la 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens en parallel rather than
sequentially. Encoder-only Transformers (BERT) are used para understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used para generation tasks;
encoder-decoder Transformers (T5, BART) are used para translation y summarisation.

### Embeddings y Vector Databases
Embeddings are dense numerical representations de text (or images) produced by
a neural Red. Semantically similar texts have embeddings that are close en
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings y Soporte fast approximate nearest-neighbour search. They are
el/la storage backbone de RAG Sistemas, including Potato.ai's cold-memory layer.
