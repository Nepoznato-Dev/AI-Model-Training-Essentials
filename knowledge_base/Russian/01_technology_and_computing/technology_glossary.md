<!-- 
This file was automatically translated from English to Russian.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Технология Glossary

A Справочник glossary covering AI models, hardware, benchmarks, и core concepts
в the modern AI и Вычисления landscape.

---

## AI Язык Models и Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released в November 2022.
It is powered by the GPT series из large Язык models (LLMs). ChatGPT is one
из the fastest-growing consumer AI products в История, reaching 100 million
users within two months из launch. It supports text-based conversation, code
generation, summarisation, и creative writing. Paid tiers provide access to
more powerful models such as GPT-4 и GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family из large Язык models created by OpenAI. the Архитектура
uses a decoder-only Transformer trained с a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
для "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via the API), GPT-3.5 (the backbone из the original ChatGPT), и GPT-4
(2023, multimodal, Производительность close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, the founder из information theory. Anthropic was founded by former
OpenAI researchers и focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set из principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known для long context windows (up
to 200,000 tokens), nuanced reasoning, и reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family из multimodal AI models, announced в
December 2023. Gemini is natively multimodal — trained from the ground up on
text, images, audio, и video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), и Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) и Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small Язык model (SLM) developed by Microsoft с 3.8B
parameters. It was released в April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises Данные quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU и
HumanEval. It supports a 4k token context window в its base variant и a 128k
window в the long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone с sufficient RAM.

### Llama (Meta AI)
Llama (Large Язык Model Meta AI) is an open-weights family из models
released by Meta. Llama 2 (2023) was released для research и commercial use
с sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
Производительность significantly, с models ranging from 8B to 70B (и later 400B+).
Because the weights are publicly downloadable, Llama models are the foundation
для a large ecosystem из fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
и are widely used для local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open и proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match the
Производительность из much larger models using efficient techniques such as sliding
window attention и grouped-query attention. Mixtral 8x7B (2024) is a mixture-
из-experts model — it routes each token to a subset из 8 expert networks,
achieving GPT-3.5-level Производительность while being computationally cheaper.
Mistral's models are fully open-weight и can be run locally.

---

## GPU Hardware и Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed для massively parallel computation. Originally
built для rendering 3D graphics, GPUs have become essential для AI/ML training
и inference because they can perform thousands из floating-point operations
simultaneously using thousands из small cores. the two main GPU manufacturers
для AI are NVIDIA и AMD.

### NVIDIA GeForce RTX Series
the RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) и RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores для accelerating AI operations. VRAM (video RAM) is
critical для running AI models locally — an 8GB GPU can handle 7B parameter
models в 4-bit quantisation; a 24GB GPU can handle 70B models в 4-bit.

### NVIDIA A-Series и H-Series (Данные Centre)
the A100 (Ampere, 2020) и H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB из HBM3 memory и is the standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× the AI throughput из consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. the RX 7900 XTX (2022) has 24GB VRAM и can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA для AI frameworks, though Поддержка is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting в 2022. Arc
GPUs Поддержка XeSS (Intel's super-sampling) и have limited but growing Поддержка
для AI inference tasks via OpenVINO и IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications База данных at ark.intel.com. It
provides detailed technical specifications для every Intel CPU, GPU, FPGA, и
NUC product, including core counts, clock speeds, TDP, supported memory types,
и instruction-set features. When you hear "check ARK для specs," it means
visiting that База данных для authoritative hardware information.

---

## AI Производительность Benchmarks

### MMLU (Massive Multitask Язык Understanding)
MMLU is a benchmark Тестирование LLM knowledge across 57 academic subjects including
mathematics, История, Закон, Медицина, и computer Наука. It consists из
multiple-choice questions drawn from real university-level exams. A score из
70% is roughly human undergraduate level; GPT-4 и Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark для code generation. It consists из 164 Python
programming problems с automated test cases. Models are measured on
pass@k — the probability that at least one из k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity и must choose the most likely continuation from
four options. the incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding из physical
и social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from the Allen Institute для AI. It consists из grade-school
Наука questions, split into "Easy" и "Challenge" sets. the Challenge set
contains questions that retrieval-based methods и simple statistical models
struggle с, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
База данных) с a Язык model. Instead из relying solely on the model's
parametric knowledge, RAG first retrieves relevant documents from an external
База знаний и then includes them в the model's context. This allows the
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form из RAG — it retrieves from its KB
и includes the results в the context before generating a response.

### Fine-tuning
Fine-tuning is the process из continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts the model's weights для a
particular task or domain. для example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces the numerical precision из model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
в 16-bit precision requires ~14GB VRAM; the same model в 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation и is the main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
the context window is the maximum number из tokens a model can process at once,
including both the prompt и the generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo и Claude 3 Поддержка 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows the model to "see"
more из a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human Обратная связь)
RLHF is the training technique that transforms a base Язык model (which
simply predicts the next token) into an assistant that follows instructions и
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, и the Язык model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, и Gemini all use
variants из RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer Архитектура
the Transformer is the neural Сеть Архитектура underlying all modern LLMs.
Introduced в the 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens в parallel rather than
sequentially. Encoder-only Transformers (BERT) are used для understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used для generation tasks;
encoder-decoder Transformers (T5, BART) are used для translation и summarisation.

### Embeddings и Vector Databases
Embeddings are dense numerical representations из text (or images) produced by
a neural Сеть. Semantically similar texts have embeddings that are close в
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings и Поддержка fast approximate nearest-neighbour search. They are
the storage backbone из RAG Системы, including Potato.ai's cold-memory layer.
