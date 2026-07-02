<!-- 
This file was automatically translated from English to Portuguese.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnologia Glossary

A Referência glossary covering AI models, hardware, benchmarks, e core concepts
em o/a modern AI e Computação landscape.

---

## AI Idioma Models e Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released em November 2022.
It is powered by o/a GPT series de large Idioma models (LLMs). ChatGPT is one
de o/a fastest-growing consumer AI products em História, reaching 100 million
users within two months de launch. It supports text-based conversation, code
generation, summarisation, e creative writing. Paid tiers provide access to
more powerful models such as GPT-4 e GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family de large Idioma models created by OpenAI. o/a Arquitetura
uses a decoder-only Transformer trained com a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
para "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via o/a API), GPT-3.5 (o/a backbone de o/a original ChatGPT), e GPT-4
(2023, multimodal, Desempenho close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, o/a founder de information theory. Anthropic was founded by former
OpenAI researchers e focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set de principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known para long context windows (up
to 200,000 tokens), nuanced reasoning, e reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family de multimodal AI models, announced em
December 2023. Gemini is natively multimodal — trained from o/a ground up on
text, images, audio, e video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), e Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) e Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small Idioma model (SLM) developed by Microsoft com 3.8B
parameters. It was released em April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises Dados quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU e
HumanEval. It supports a 4k token context window em its base variant e a 128k
window em o/a long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone com sufficient RAM.

### Llama (Meta AI)
Llama (Large Idioma Model Meta AI) is an open-weights family de models
released by Meta. Llama 2 (2023) was released para research e commercial use
com sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
Desempenho significantly, com models ranging from 8B to 70B (e later 400B+).
Because o/a weights are publicly downloadable, Llama models are o/a foundation
para a large ecosystem de fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
e are widely used para local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open e proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match o/a
Desempenho de much larger models using efficient techniques such as sliding
window attention e grouped-query attention. Mixtral 8x7B (2024) is a mixture-
de-experts model — it routes each token to a subset de 8 expert networks,
achieving GPT-3.5-level Desempenho while being computationally cheaper.
Mistral's models are fully open-weight e can be run locally.

---

## GPU Hardware e Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed para massively parallel computation. Originally
built para rendering 3D graphics, GPUs have become essential para AI/ML training
e inference because they can perform thousands de floating-point operations
simultaneously using thousands de small cores. o/a two main GPU manufacturers
para AI are NVIDIA e AMD.

### NVIDIA GeForce RTX Series
o/a RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) e RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores para accelerating AI operations. VRAM (video RAM) is
critical para running AI models locally — an 8GB GPU can handle 7B parameter
models em 4-bit quantisation; a 24GB GPU can handle 70B models em 4-bit.

### NVIDIA A-Series e H-Series (Dados Centre)
o/a A100 (Ampere, 2020) e H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB de HBM3 memory e is o/a standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× o/a AI throughput de consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. o/a RX 7900 XTX (2022) has 24GB VRAM e can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA para AI frameworks, though support is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting em 2022. Arc
GPUs support XeSS (Intel's super-sampling) e have limited but growing support
para AI inference tasks via OpenVINO e IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications Banco de dados at ark.intel.com. It
provides detailed technical specifications para every Intel CPU, GPU, FPGA, e
NUC product, including core counts, clock speeds, TDP, supported memory types,
e instruction-set features. When you hear "check ARK para specs," it means
visiting that Banco de dados para authoritative hardware information.

---

## AI Desempenho Benchmarks

### MMLU (Massive Multitask Idioma Understanding)
MMLU is a benchmark Teste LLM knowledge across 57 academic subjects including
mathematics, História, Direito, Medicina, e computer Ciência. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 e Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark para code generation. It consists de 164 Python
programming problems com automated test cases. Models are measured on
pass@k — o/a probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity e must choose o/a most likely continuation from
four options. o/a incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding de physical
e social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from o/a Allen Institute para AI. It consists de grade-school
Ciência questions, split into "Easy" e "Challenge" sets. o/a Challenge set
contains questions that retrieval-based methods e simple statistical models
struggle com, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
Banco de dados) com a Idioma model. Instead de relying solely on o/a model's
parametric knowledge, RAG first retrieves relevant documents from an external
Base de conhecimento e then includes them em o/a model's context. This allows o/a
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form de RAG — it retrieves from its KB
e includes o/a results em o/a context before generating a response.

### Fine-tuning
Fine-tuning is o/a process de continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts o/a model's weights para a
particular task or domain. para example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces o/a numerical precision de model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
em 16-bit precision requires ~14GB VRAM; o/a same model em 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation e is o/a main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
o/a context window is o/a maximum number de tokens a model can process at once,
including both o/a prompt e o/a generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo e Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows o/a model to "see"
more de a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF is o/a training technique that transforms a base Idioma model (which
simply predicts o/a next token) into an assistant that follows instructions e
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, e o/a Idioma model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, e Gemini all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer Arquitetura
o/a Transformer is o/a neural Rede Arquitetura underlying all modern LLMs.
Introduced em o/a 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens em parallel rather than
sequentially. Encoder-only Transformers (BERT) are used para understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used para generation tasks;
encoder-decoder Transformers (T5, BART) are used para translation e summarisation.

### Embeddings e Vector Databases
Embeddings are dense numerical representations de text (or images) produced by
a neural Rede. Semantically similar texts have embeddings that are close em
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings e support fast approximate nearest-neighbour search. They are
o/a storage backbone de RAG Sistemas, including Potato.ai's cold-memory layer.
