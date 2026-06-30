<!-- 
This file was automatically translated from English to German.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie Glossary

A referenz glossary covering AI models, hardware, benchmarks, und core concepts
in der/die/das modern AI und datenverarbeitung lundscape.

---

# # AI Sprache Models und Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released in November 2022.
It is powered by der/die/das GPT series von large sprache models (LLMs). ChatGPT is one
von der/die/das fastest-growing consumer AI products in geschichte, reaching 100 million
users mitin two months von launch. It supports text-based conversation, code
generation, summarisation, und creative writing. Paid tiers provide access to
more powerful models such as GPT-4 und GPT-4o.

# ## GPT (Generative Pre-trained Transfürmer)
GPT is a family von large sprache models created by OpenAI. The architektur
uses a decoder-only Transfürmer trained mit a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
für "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via der/die/das API), GPT-3.5 (der/die/das backbone von der/die/das original ChatGPT), und GPT-4
(2023, multimodal, perfürmance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, der/die/das founder von infürmation der/die/dasory. Anthropic was founded by fürmer
OpenAI researchers und focuses on "constitutional AI" — a technique to make
models sicherr by training der/die/dasm to follow a set von principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known für long context windows (up
to 200,000 tokens), nuanced reasoning, und reduced harmful output compared to
baseline LLMs.

# ## Gemini
Gemini is Google DeepMind's family von multimodal AI models, announced in
December 2023. Gemini is natively multimodal — trained from der/die/das ground up on
text, images, audio, und video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), und Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) und Google Search AI
Übersichts.

# ## Phi-3-mini
Phi-3-mini is a small sprache model (SLM) developed by Microsvont mit 3.8B
parameters. It was released in April 2024. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" datenset — a technique
pioneered by Microsvont Research — that prioritises daten quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperfürms models several times larger on reasoning benchmarks such as MMLU und
HumanEval. It supports a 4k token context window in its base variant und a 128k
window in der/die/das long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone mit sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Sprache Model Meta AI) is an open-weights family von models
released by Meta. Llama 2 (2023) was released für research und commercial use
mit sizes ranging from 7B to 70B parameters. Llama 3 (2024) improved
perfürmance significantly, mit models ranging from 8B to 70B (und later 400B+).
Because der/die/das weights are publicly downloadable, Llama models are der/die/das foundation
für a large ecosystem von fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
und are widely used für local/private AI bereitstellungs.

# ## Mistral
Mistral AI is a French AI company that develops open und proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match der/die/das
perfürmance von much larger models using efficient techniques such as sliding
window attention und grouped-query attention. Mixtral 8x7B (2024) is a mixture-
von-experts model — it routes each token to a subset von 8 expert netzwerks,
achieving GPT-3.5-level perfürmance while being computationally cheaper.
Mistral's models are fully open-weight und can be run locally.

---

# # GPU Hardware und Graphics Cards

# ## GPU (Graphics Processing Unit)
A GPU is a processor designed für massively parallel computation. Originally
built für rendering 3D graphics, GPUs have become essential für AI/ML training
und inference because der/die/dasy can perfürm thousunds von floating-point operations
simultaneously using thousunds von small cores. The two main GPU manufacturers
für AI are NVIDIA und AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) und RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores für accelerating AI operations. VRAM (video RAM) is
critical für running AI models locally — an 8GB GPU can hundle 7B parameter
models in 4-bit quantisation; a 24GB GPU can hundle 70B models in 4-bit.

# ## NVIDIA A-Series und H-Series (Daten Centre)
The A100 (Ampere, 2020) und H100 (Hopper, 2022) are NVIDIA's prvonessional AI
accelerators. An H100 has up to 80GB von HBM3 memory und is der/die/das stundard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but vonfer 10–30× der/die/das AI throughput von consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU line. The RX 7900 XTX (2022) has 24GB VRAM und can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA für AI frameworks, though support is improving.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting in 2022. Arc
GPUs support XeSS (Intel's super-sampling) und have limited but growing support
für AI inference tasks via OpenVINO und IPEX-LLM frameworks.

# ## ARK Intel (ark.intel.com)
ARK is Intel's vonficial product specifications datenbase at ark.intel.com. It
provides detailed technical specifications für every Intel CPU, GPU, FPGA, und
NUC product, including core counts, clock speeds, TDP, supported memory types,
und instruction-set features. When you hear "check ARK für specs," it means
visiting that datenbase für authoritative hardware infürmation.

---

# # AI Perfürmance Benchmarks

# ## MMLU (Massive Multitask Sprache Understunding)
MMLU is a benchmark testen LLM knowledge across 57 academic subjects including
mader/die/dasmatics, geschichte, recht, medizin, und computer wissenschaft. It consists von
multiple-choice questions drawn from real university-level exams. A score von
70% is roughly human undergraduate level; GPT-4 und Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark für code generation. It consists von 164 Python
programming problems mit automated test cases. Models are measured on
pass@k — der/die/das probability that at least one von k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity und must choose der/die/das most likely continuation from
four options. The incorrect options are specially designed to be plausible but
subtly wrong. It tests wheder/die/dasr a model has a grounded understunding von physical
und social situations.

# ## ARC (AI2 Reasoning Challenge)
ARC is a benchmark from der/die/das Allen Institute für AI. It consists von grade-school
wissenschaft questions, split into "Easy" und "Challenge" sets. The Challenge set
contains questions that retrieval-based methods und simple statistical models
struggle mit, requiring multi-step reasoning.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
datenbase) mit a sprache model. Instead von relying solely on der/die/das model's
parametric knowledge, RAG first retrieves relevant documents from an external
wissensdatenbank und der/die/dasn includes der/die/dasm in der/die/das model's context. This allows der/die/das
model to answer questions about up-to-date or domain-specific infürmation
mitout retraining. Potato.ai uses a fürm von RAG — it retrieves from its KB
und includes der/die/das results in der/die/das context befüre generating a response.

# ## Fine-tuning
Fine-tuning is der/die/das process von continuing to train a pre-trained model on a
smaller, domain-specific datenset. This adapts der/die/das model's weights für a
particular task or domain. For example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

# ## Quantisation
Quantisation reduces der/die/das numerical precision von model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
in 16-bit precision requires ~14GB VRAM; der/die/das same model in 4-bit (GGUF fürmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation und is der/die/das main technique enabling large models to run on consumer
hardware or even mobile devices.

# ## Context Window
The context window is der/die/das maximum number von tokens a model can process at once,
including both der/die/das prompt und der/die/das generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo und Claude 3 support 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows der/die/das model to "see"
more von a conversation or document at once, improving coherence over long
exchanges.

# ## RLHF (Reinfürcement Learning from Human Feedback)
RLHF is der/die/das training technique that transfürms a base sprache model (which
simply predicts der/die/das next token) into an assistant that follows instructions und
behaves helpfully. Human raters score model outputs, a reward model is trained
on der/die/dasir preferenzs, und der/die/das sprache model is der/die/dasn optimised against this
reward model using reinfürcement learning. ChatGPT, Claude, und Gemini all use
variants von RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preferenz Optimisation).

# ## Transfürmer Architektur
The Transfürmer is der/die/das neural netzwerk architektur underlying all modern LLMs.
Introduced in der/die/das 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens in parallel rader/die/dasr than
sequentially. Encoder-only Transfürmers (BERT) are used für understunding tasks;
decoder-only Transfürmers (GPT, Llama, Mistral) are used für generation tasks;
encoder-decoder Transfürmers (T5, BART) are used für translation und summarisation.

# ## Embeddings und Vector Datenbases
Embeddings are dense numerical representations von text (or images) produced by
a neural netzwerk. Semantically similar texts have embeddings that are close in
vector space. Vector datenbases (ChromaDB, Pinecone, Weaviate, Qdrant) store
der/die/dasse embeddings und support fast approximate nearest-neighbour search. They are
der/die/das storage backbone von RAG systeme, including Potato.ai's cold-memory layer.
