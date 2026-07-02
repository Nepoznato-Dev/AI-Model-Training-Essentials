<!-- 
This file was automatically translated from English to Korean.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 Glossary

A 참조 glossary covering AI models, hardware, benchmarks, 와 core concepts
에서 그 modern AI 와 컴퓨팅 landscape.

---

## AI 언어 Models 와 Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released 에서 November 2022.
It is powered by 그 GPT series 의 large 언어 models (LLMs). ChatGPT is one
의 그 fastest-growing consumer AI products 에서 역사, reaching 100 million
users within two months 의 launch. It supports text-based conversation, code
generation, summarisation, 와 creative writing. Paid tiers provide access to
more powerful models such as GPT-4 와 GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family 의 large 언어 models created by OpenAI. 그 아키텍처
uses a decoder-only Transformer trained 와 함께 a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
위한 "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via 그 API), GPT-3.5 (그 backbone 의 그 original ChatGPT), 와 GPT-4
(2023, multimodal, 성능 close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, 그 founder 의 information theory. Anthropic was founded by former
OpenAI researchers 와 focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set 의 principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known 위한 long context windows (up
to 200,000 tokens), nuanced reasoning, 와 reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family 의 multimodal AI models, announced 에서
December 2023. Gemini is natively multimodal — trained from 그 ground up on
text, images, audio, 와 video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), 와 Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) 와 Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small 언어 model (SLM) developed by Microsoft 와 함께 3.8B
parameters. It was released 에서 April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises 데이터 quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU 와
HumanEval. It supports a 4k token context window 에서 its base variant 와 a 128k
window 에서 그 long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone 와 함께 sufficient RAM.

### Llama (Meta AI)
Llama (Large 언어 Model Meta AI) is an open-weights family 의 models
released by Meta. Llama 2 (2023) was released 위한 research 와 commercial use
와 함께 sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
성능 significantly, 와 함께 models ranging from 8B to 70B (와 later 400B+).
Because 그 weights are publicly downloadable, Llama models are 그 foundation
위한 a large ecosystem 의 fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
와 are widely used 위한 local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open 와 proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 그
성능 의 much larger models using efficient techniques such as sliding
window attention 와 grouped-query attention. Mixtral 8x7B (2024) is a mixture-
의-experts model — it routes each token to a subset 의 8 expert networks,
achieving GPT-3.5-level 성능 while being computationally cheaper.
Mistral's models are fully open-weight 와 can be run locally.

---

## GPU Hardware 와 Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed 위한 massively parallel computation. Originally
built 위한 rendering 3D graphics, GPUs have become essential 위한 AI/ML training
와 inference because they can perform thousands 의 floating-point operations
simultaneously using thousands 의 small cores. 그 two main GPU manufacturers
위한 AI are NVIDIA 와 AMD.

### NVIDIA GeForce RTX Series
그 RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) 와 RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores 위한 accelerating AI operations. VRAM (video RAM) is
critical 위한 running AI models locally — an 8GB GPU can handle 7B parameter
models 에서 4-bit quantisation; a 24GB GPU can handle 70B models 에서 4-bit.

### NVIDIA A-Series 와 H-Series (데이터 Centre)
그 A100 (Ampere, 2020) 와 H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB 의 HBM3 memory 와 is 그 standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× 그 AI throughput 의 consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. 그 RX 7900 XTX (2022) has 24GB VRAM 와 can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA 위한 AI frameworks, though support is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting 에서 2022. Arc
GPUs support XeSS (Intel's super-sampling) 와 have limited but growing support
위한 AI inference tasks via OpenVINO 와 IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications 데이터베이스 at ark.intel.com. It
provides detailed technical specifications 위한 every Intel CPU, GPU, FPGA, 와
NUC product, including core counts, clock speeds, TDP, supported memory types,
와 instruction-set features. When you hear "check ARK 위한 specs," it means
visiting that 데이터베이스 위한 authoritative hardware information.

---

## AI 성능 Benchmarks

### MMLU (Massive Multitask 언어 Understanding)
MMLU is a benchmark 테스트 LLM knowledge across 57 academic subjects including
mathematics, 역사, 법률, 의학, 와 computer 과학. It consists 의
multiple-choice questions drawn from real university-level exams. A score 의
70% is roughly human undergraduate level; GPT-4 와 Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark 위한 code generation. It consists 의 164 Python
programming problems 와 함께 automated test cases. Models are measured on
pass@k — 그 probability that at least one 의 k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity 와 must choose 그 most likely continuation from
four options. 그 incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding 의 physical
와 social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from 그 Allen Institute 위한 AI. It consists 의 grade-school
과학 questions, split into "Easy" 와 "Challenge" sets. 그 Challenge set
contains questions that retrieval-based methods 와 simple statistical models
struggle 와 함께, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
데이터베이스) 와 함께 a 언어 model. Instead 의 relying solely on 그 model's
parametric knowledge, RAG first retrieves relevant documents from an external
지식 기반 와 then includes them 에서 그 model's context. This allows 그
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form 의 RAG — it retrieves from its KB
와 includes 그 results 에서 그 context before generating a response.

### Fine-tuning
Fine-tuning is 그 process 의 continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts 그 model's weights 위한 a
particular task or domain. 위한 example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces 그 numerical precision 의 model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
에서 16-bit precision requires ~14GB VRAM; 그 same model 에서 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation 와 is 그 main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
그 context window is 그 maximum number 의 tokens a model can process at once,
including both 그 prompt 와 그 generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo 와 Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows 그 model to "see"
more 의 a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF is 그 training technique that transforms a base 언어 model (which
simply predicts 그 next token) into an assistant that follows instructions 와
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, 와 그 언어 model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, 와 Gemini all use
variants 의 RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer 아키텍처
그 Transformer is 그 neural 네트워크 아키텍처 underlying all modern LLMs.
Introduced 에서 그 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens 에서 parallel rather than
sequentially. Encoder-only Transformers (BERT) are used 위한 understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used 위한 generation tasks;
encoder-decoder Transformers (T5, BART) are used 위한 translation 와 summarisation.

### Embeddings 와 Vector Databases
Embeddings are dense numerical representations 의 text (or images) produced by
a neural 네트워크. Semantically similar texts have embeddings that are close 에서
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings 와 support fast approximate nearest-neighbour search. They are
그 storage backbone 의 RAG 시스템, including Potato.ai's cold-memory layer.
