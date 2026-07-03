<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 技术 Glossary

A 参考 glossary covering AI models, hardware, benchmarks, 和 core concepts
在 这 modern AI 和 计算 landscape.

---

## AI 语言 Models 和 Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released 在 November 2022.
It is powered by 这 GPT series 的 large 语言 models (LLMs). ChatGPT is one
的 这 fastest-growing consumer AI products 在 历史, reaching 100 million
users within two months 的 launch. It supports text-based conversation, code
generation, summarisation, 和 creative writing. Paid tiers provide access to
more powerful models such as GPT-4 和 GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family 的 large 语言 models created by OpenAI. 这 架构
uses a decoder-only Transformer trained 与 a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
为 "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via 这 API), GPT-3.5 (这 backbone 的 这 original ChatGPT), 和 GPT-4
(2023, multimodal, 性能 close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, 这 founder 的 information theory. Anthropic was founded by former
OpenAI researchers 和 focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set 的 principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known 为 long context windows (up
to 200,000 tokens), nuanced reasoning, 和 reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family 的 multimodal AI models, announced 在
December 2023. Gemini is natively multimodal — trained from 这 ground up on
text, images, audio, 和 video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), 和 Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) 和 Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small 语言 model (SLM) developed by Microsoft 与 3.8B
parameters. It was released 在 April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises 数据 quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU 和
HumanEval. It supports a 4k token context window 在 its base variant 和 a 128k
window 在 这 long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone 与 sufficient RAM.

### Llama (Meta AI)
Llama (Large 语言 Model Meta AI) is an open-weights family 的 models
released by Meta. Llama 2 (2023) was released 为 research 和 commercial use
与 sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
性能 significantly, 与 models ranging from 8B to 70B (和 later 400B+).
Because 这 weights are publicly downloadable, Llama models are 这 foundation
为 a large ecosystem 的 fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
和 are widely used 为 local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open 和 proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 这
性能 的 much larger models using efficient techniques such as sliding
window attention 和 grouped-query attention. Mixtral 8x7B (2024) is a mixture-
的-experts model — it routes each token to a subset 的 8 expert networks,
achieving GPT-3.5-level 性能 while being computationally cheaper.
Mistral's models are fully open-weight 和 can be run locally.

---

## GPU Hardware 和 Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed 为 massively parallel computation. Originally
built 为 rendering 3D graphics, GPUs have become essential 为 AI/ML training
和 inference because they can perform thousands 的 floating-point operations
simultaneously using thousands 的 small cores. 这 two main GPU manufacturers
为 AI are NVIDIA 和 AMD.

### NVIDIA GeForce RTX Series
这 RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) 和 RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores 为 accelerating AI operations. VRAM (video RAM) is
critical 为 running AI models locally — an 8GB GPU can handle 7B parameter
models 在 4-bit quantisation; a 24GB GPU can handle 70B models 在 4-bit.

### NVIDIA A-Series 和 H-Series (数据 Centre)
这 A100 (Ampere, 2020) 和 H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB 的 HBM3 memory 和 is 这 standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× 这 AI throughput 的 consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. 这 RX 7900 XTX (2022) has 24GB VRAM 和 can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA 为 AI frameworks, though 支持 is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting 在 2022. Arc
GPUs 支持 XeSS (Intel's super-sampling) 和 have limited but growing 支持
为 AI inference tasks via OpenVINO 和 IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications 数据库 at ark.intel.com. It
provides detailed technical specifications 为 every Intel CPU, GPU, FPGA, 和
NUC product, including core counts, clock speeds, TDP, supported memory types,
和 instruction-set features. When you hear "check ARK 为 specs," it means
visiting that 数据库 为 authoritative hardware information.

---

## AI 性能 Benchmarks

### MMLU (Massive Multitask 语言 Understanding)
MMLU is a benchmark 测试 LLM knowledge across 57 academic subjects including
mathematics, 历史, 法律, 医学, 和 computer 科学. It consists 的
multiple-choice questions drawn from real university-level exams. A score 的
70% is roughly human undergraduate level; GPT-4 和 Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark 为 code generation. It consists 的 164 Python
programming problems 与 automated test cases. Models are measured on
pass@k — 这 probability that at least one 的 k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity 和 must choose 这 most likely continuation from
four options. 这 incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding 的 physical
和 social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from 这 Allen Institute 为 AI. It consists 的 grade-school
科学 questions, split into "Easy" 和 "Challenge" sets. 这 Challenge set
contains questions that retrieval-based methods 和 simple statistical models
struggle 与, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
数据库) 与 a 语言 model. Instead 的 relying solely on 这 model's
parametric knowledge, RAG first retrieves relevant documents from an external
知识库 和 then includes them 在 这 model's context. This allows 这
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form 的 RAG — it retrieves from its KB
和 includes 这 results 在 这 context before generating a response.

### Fine-tuning
Fine-tuning is 这 process 的 continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts 这 model's weights 为 a
particular task or domain. 为 example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces 这 numerical precision 的 model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
在 16-bit precision requires ~14GB VRAM; 这 same model 在 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation 和 is 这 main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
这 context window is 这 maximum number 的 tokens a model can process at once,
including both 这 prompt 和 这 generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo 和 Claude 3 支持 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows 这 model to "see"
more 的 a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human 反馈)
RLHF is 这 training technique that transforms a base 语言 model (which
simply predicts 这 next token) into an assistant that follows instructions 和
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, 和 这 语言 model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, 和 Gemini all use
variants 的 RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer 架构
这 Transformer is 这 neural 网络 架构 underlying all modern LLMs.
Introduced 在 这 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens 在 parallel rather than
sequentially. Encoder-only Transformers (BERT) are used 为 understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used 为 generation tasks;
encoder-decoder Transformers (T5, BART) are used 为 translation 和 summarisation.

### Embeddings 和 Vector Databases
Embeddings are dense numerical representations 的 text (or images) produced by
a neural 网络. Semantically similar texts have embeddings that are close 在
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings 和 支持 fast approximate nearest-neighbour search. They are
这 storage backbone 的 RAG 系统, including Potato.ai's cold-memory layer.
