<!-- 
This file was automatically translated from English to French.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie Glossary

A Référence glossary covering AI models, hardware, benchmarks, et core concepts
dans le/la modern AI et Informatique landscape.

---

# # AI Langue Models et Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released dans November 2022.
It is powered by le/la GPT series de large Langue models (LLMs). ChatGPT is one
de le/la fastest-growing consumer AI products dans Histoire, reaching 100 million
users within two months de launch. It supports text-based conversation, code
generation, summarisation, et creative writing. Paid tiers provide access to
more powerful models such as GPT-4 et GPT-4o.

# ## GPT (Generative Pre-trained Transformer)
GPT is a family de large Langue models created by OpenAI. le/la Architecture
uses a decoder-only Transformer trained avec a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
pour "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via le/la API), GPT-3.5 (le/la backbone de le/la original ChatGPT), et GPT-4
(2023, multimodal, Performance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, le/la founder de information theory. Anthropic was founded by former
OpenAI researchers et focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set de principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known pour long context windows (up
to 200,000 tokens), nuanced reasoning, et reduced harmful output compared to
baseline LLMs.

# ## Gemini
Gemini is Google DeepMind's family de multimodal AI models, announced dans
December 2023. Gemini is natively multimodal — trained from le/la ground up on
text, images, audio, et video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), et Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) et Google Search AI
Overviews.

# ## Phi-3-mini
Phi-3-mini is a small Langue model (SLM) developed by Microsoft avec 3.8B
parameters. It was released dans April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises Données quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU et
HumanEval. It supports a 4k token context window dans its base variant et a 128k
window dans le/la long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone avec sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Langue Model Meta AI) is an open-weights family de models
released by Meta. Llama 2 (2023) was released pour research et commercial use
avec sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
Performance significantly, avec models ranging from 8B to 70B (et later 400B+).
Because le/la weights are publicly downloadable, Llama models are le/la foundation
pour a large ecosystem de fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
et are widely used pour local/private AI deployments.

# ## Mistral
Mistral AI is a French AI company that develops open et proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match le/la
Performance de much larger models using efficient techniques such as sliding
window attention et grouped-query attention. Mixtral 8x7B (2024) is a mixture-
de-experts model — it routes each token to a subset de 8 expert networks,
achieving GPT-3.5-level Performance while being computationally cheaper.
Mistral's models are fully open-weight et can be run locally.

---

# # GPU Hardware et Graphics Cards

# ## GPU (Graphics Processing Unit)
A GPU is a processor designed pour massively parallel computation. Originally
built pour rendering 3D graphics, GPUs have become essential pour AI/ML training
et inference because they can perform thousands de floating-point operations
simultaneously using thousands de small cores. le/la two main GPU manufacturers
pour AI are NVIDIA et AMD.

# ## NVIDIA GeForce RTX Series
le/la RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) et RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores pour accelerating AI operations. VRAM (video RAM) is
critical pour running AI models locally — an 8GB GPU can handle 7B parameter
models dans 4-bit quantisation; a 24GB GPU can handle 70B models dans 4-bit.

# ## NVIDIA A-Series et H-Series (Données Centre)
le/la A100 (Ampere, 2020) et H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB de HBM3 memory et is le/la standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× le/la AI throughput de consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU line. le/la RX 7900 XTX (2022) has 24GB VRAM et can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA pour AI frameworks, though support is improving.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting dans 2022. Arc
GPUs support XeSS (Intel's super-sampling) et have limited but growing support
pour AI inference tasks via OpenVINO et IPEX-LLM frameworks.

# ## ARK Intel (ark.intel.com)
ARK is Intel's official product specifications Base de données at ark.intel.com. It
provides detailed technical specifications pour every Intel CPU, GPU, FPGA, et
NUC product, including core counts, clock speeds, TDP, supported memory types,
et instruction-set features. When you hear "check ARK pour specs," it means
visiting that Base de données pour authoritative hardware information.

---

# # AI Performance Benchmarks

# ## MMLU (Massive Multitask Langue Understanding)
MMLU is a benchmark Test LLM knowledge across 57 academic subjects including
mathematics, Histoire, Droit, Médecine, et computer Science. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 et Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark pour code generation. It consists de 164 Python
programming problems avec automated test cases. Models are measured on
pass@k — le/la probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity et must choose le/la most likely continuation from
four options. le/la incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding de physical
et social situations.

# ## ARC (AI2 Reasoning Challenge)
ARC is a benchmark from le/la Allen Institute pour AI. It consists de grade-school
Science questions, split into "Easy" et "Challenge" sets. le/la Challenge set
contains questions that retrieval-based methods et simple statistical models
struggle avec, requiring multi-step reasoning.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
Base de données) avec a Langue model. Instead de relying solely on le/la model's
parametric knowledge, RAG first retrieves relevant documents from an external
Base de connaissances et then includes them dans le/la model's context. This allows le/la
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form de RAG — it retrieves from its KB
et includes le/la results dans le/la context before generating a response.

# ## Fine-tuning
Fine-tuning is le/la process de continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts le/la model's weights pour a
particular task or domain. pour example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

# ## Quantisation
Quantisation reduces le/la numerical precision de model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
dans 16-bit precision requires ~14GB VRAM; le/la same model dans 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation et is le/la main technique enabling large models to run on consumer
hardware or even mobile devices.

# ## Context Window
le/la context window is le/la maximum number de tokens a model can process at once,
including both le/la prompt et le/la generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo et Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows le/la model to "see"
more de a conversation or document at once, improving coherence over long
exchanges.

# ## RLHF (Reinforcement Learning from Human Feedback)
RLHF is le/la training technique that transforms a base Langue model (which
simply predicts le/la next token) into an assistant that follows instructions et
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, et le/la Langue model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, et Gemini all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

# ## Transformer Architecture
le/la Transformer is le/la neural Réseau Architecture underlying all modern LLMs.
Introduced dans le/la 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens dans parallel rather than
sequentially. Encoder-only Transformers (BERT) are used pour understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used pour generation tasks;
encoder-decoder Transformers (T5, BART) are used pour translation et summarisation.

# ## Embeddings et Vector Databases
Embeddings are dense numerical representations de text (or images) produced by
a neural Réseau. Semantically similar texts have embeddings that are close dans
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings et support fast approximate nearest-neighbour search. They are
le/la storage backbone de RAG Systèmes, including Potato.ai's cold-memory layer.
