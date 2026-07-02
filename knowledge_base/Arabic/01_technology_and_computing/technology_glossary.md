<!-- 
This file was automatically translated from English to Arabic.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# التكنولوجيا Glossary

A مرجع glossary covering AI models, hardware, benchmarks, و core concepts
في ال modern AI و الحوسبة landscape.

---

# # AI اللغة Models و Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released في November 2022.
It is powered by ال GPT series من large اللغة models (LLMs). ChatGPT is one
من ال fastest-growing consumer AI products في التاريخ, reaching 100 million
users within two months من launch. It supports text-based conversation, code
generation, summarisation, و creative writing. Paid tiers provide access to
more powerful models such as GPT-4 و GPT-4o.

# ## GPT (Generative Pre-trained Transformer)
GPT is a family من large اللغة models created by OpenAI. ال العمارة
uses a decoder-only Transformer trained مع a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
لأجل "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via ال API), GPT-3.5 (ال backbone من ال original ChatGPT), و GPT-4
(2023, multimodal, الأداء close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, ال founder من information theory. Anthropic was founded by former
OpenAI researchers و focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set من principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known لأجل long context windows (up
to 200,000 tokens), nuanced reasoning, و reduced harmful output compared to
baseline LLMs.

# ## Gemini
Gemini is Google DeepMind's family من multimodal AI models, announced في
December 2023. Gemini is natively multimodal — trained from ال ground up on
text, images, audio, و video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), و Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) و Google Search AI
Overviews.

# ## Phi-3-mini
Phi-3-mini is a small اللغة model (SLM) developed by Microsoft مع 3.8B
parameters. It was released في April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises البيانات quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU و
HumanEval. It supports a 4k token context window في its base variant و a 128k
window في ال long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone مع sufficient RAM.

# ## Llama (Meta AI)
Llama (Large اللغة Model Meta AI) is an open-weights family من models
released by Meta. Llama 2 (2023) was released لأجل research و commercial use
مع sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
الأداء significantly, مع models ranging from 8B to 70B (و later 400B+).
Because ال weights are publicly downloadable, Llama models are ال foundation
لأجل a large ecosystem من fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
و are widely used لأجل local/private AI deployments.

# ## Mistral
Mistral AI is a French AI company that develops open و proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match ال
الأداء من much larger models using efficient techniques such as sliding
window attention و grouped-query attention. Mixtral 8x7B (2024) is a mixture-
من-experts model — it routes each token to a subset من 8 expert networks,
achieving GPT-3.5-level الأداء while being computationally cheaper.
Mistral's models are fully open-weight و can be run locally.

---

# # GPU Hardware و Graphics Cards

# ## GPU (Graphics Processing Unit)
A GPU is a processor designed لأجل massively parallel computation. Originally
built لأجل rendering 3D graphics, GPUs have become essential لأجل AI/ML training
و inference because they can perform thousands من floating-point operations
simultaneously using thousands من small cores. ال two main GPU manufacturers
لأجل AI are NVIDIA و AMD.

# ## NVIDIA GeForce RTX Series
ال RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) و RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores لأجل accelerating AI operations. VRAM (video RAM) is
critical لأجل running AI models locally — an 8GB GPU can handle 7B parameter
models في 4-bit quantisation; a 24GB GPU can handle 70B models في 4-bit.

# ## NVIDIA A-Series و H-Series (البيانات Centre)
ال A100 (Ampere, 2020) و H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB من HBM3 memory و is ال standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× ال AI throughput من consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU line. ال RX 7900 XTX (2022) has 24GB VRAM و can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA لأجل AI frameworks, though support is improving.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting في 2022. Arc
GPUs support XeSS (Intel's super-sampling) و have limited but growing support
لأجل AI inference tasks via OpenVINO و IPEX-LLM frameworks.

# ## ARK Intel (ark.intel.com)
ARK is Intel's official product specifications قاعدة البيانات at ark.intel.com. It
provides detailed technical specifications لأجل every Intel CPU, GPU, FPGA, و
NUC product, including core counts, clock speeds, TDP, supported memory types,
و instruction-set features. When you hear "check ARK لأجل specs," it means
visiting that قاعدة البيانات لأجل authoritative hardware information.

---

# # AI الأداء Benchmarks

# ## MMLU (Massive Multitask اللغة Understanding)
MMLU is a benchmark الاختبار LLM knowledge across 57 academic subjects including
mathematics, التاريخ, القانون, الطب, و computer العلوم. It consists من
multiple-choice questions drawn from real university-level exams. A score من
70% is roughly human undergraduate level; GPT-4 و Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark لأجل code generation. It consists من 164 Python
programming problems مع automated test cases. Models are measured on
pass@k — ال probability that at least one من k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity و must choose ال most likely continuation from
four options. ال incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding من physical
و social situations.

# ## ARC (AI2 Reasoning Challenge)
ARC is a benchmark from ال Allen Institute لأجل AI. It consists من grade-school
العلوم questions, split into "Easy" و "Challenge" sets. ال Challenge set
contains questions that retrieval-based methods و simple statistical models
struggle مع, requiring multi-step reasoning.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
قاعدة البيانات) مع a اللغة model. Instead من relying solely on ال model's
parametric knowledge, RAG first retrieves relevant documents from an external
قاعدة المعرفة و then includes them في ال model's context. This allows ال
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form من RAG — it retrieves from its KB
و includes ال results في ال context before generating a response.

# ## Fine-tuning
Fine-tuning is ال process من continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts ال model's weights لأجل a
particular task or domain. لأجل example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

# ## Quantisation
Quantisation reduces ال numerical precision من model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
في 16-bit precision requires ~14GB VRAM; ال same model في 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation و is ال main technique enabling large models to run on consumer
hardware or even mobile devices.

# ## Context Window
ال context window is ال maximum number من tokens a model can process at once,
including both ال prompt و ال generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo و Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows ال model to "see"
more من a conversation or document at once, improving coherence over long
exchanges.

# ## RLHF (Reinforcement Learning from Human Feedback)
RLHF is ال training technique that transforms a base اللغة model (which
simply predicts ال next token) into an assistant that follows instructions و
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, و ال اللغة model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, و Gemini all use
variants من RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

# ## Transformer العمارة
ال Transformer is ال neural الشبكة العمارة underlying all modern LLMs.
Introduced في ال 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens في parallel rather than
sequentially. Encoder-only Transformers (BERT) are used لأجل understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used لأجل generation tasks;
encoder-decoder Transformers (T5, BART) are used لأجل translation و summarisation.

# ## Embeddings و Vector Databases
Embeddings are dense numerical representations من text (or images) produced by
a neural الشبكة. Semantically similar texts have embeddings that are close في
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings و support fast approximate nearest-neighbour search. They are
ال storage backbone من RAG الأنظمة, including Potato.ai's cold-memory layer.
