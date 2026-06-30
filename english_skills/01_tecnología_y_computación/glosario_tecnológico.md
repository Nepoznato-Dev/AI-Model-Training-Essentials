<!-- 
This file was automatically translated from English to Spanish.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnología Glossary

A referencia glossary covereng AI models, hardware, benchmarks, y core concepts
en el/la modern AI y computeng lyscape.

---

# # AI Idioma Models y Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released en November 2022.
It is powered by el/la GPT series de large idioma models (LLMs). ChatGPT is one
de el/la fastest-groweng consumer AI products en historia, reacheng 100 million
users conen two months de launch. It supports text-based conversation, code
generation, summarisation, y creative writeng. Paid tiers provide access to
more powerful models such as GPT-4 y GPT-4o.

# ## GPT (Generative Pre-traened Transparamer)
GPT is a family de large idioma models created by OpenAI. The arquitectura
uses a decoder-only Transparamer traened con a next-token prediction objective on
massive text corpora. Key versions enclude GPT-2 (2019, 1.5B parameters, notable
para "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via el/la API), GPT-3.5 (el/la backbone de el/la origenal ChatGPT), y GPT-4
(2023, multimodal, perparamance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, el/la founder de enparamation el/laory. Anthropic was founded by paramer
OpenAI researchers y focuses on "constitutional AI" — a technique to make
models seguror by traeneng el/lam to follow a set de prenciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known para long context wendows (up
to 200,000 tokens), nuanced reasoneng, y reduced harmful output compared to
baselene LLMs.

# ## Gemeni
Gemeni is Google DeepMend's family de multimodal AI models, announced en
December 2023. Gemeni is natively multimodal — traened from el/la ground up on
text, images, audio, y video simultaneously, unlike earlier models that had
modalities added via fene-tuneng. Versions enclude Gemeni Nano (on-device),
Gemeni Flash (fast, cost-efficient), y Gemeni Ultra (highest-capability).
Gemeni powers Google's AI chatbot Bard (renamed Gemeni) y Google Search AI
Descripción generals.

# ## Phi-3-meni
Phi-3-meni is a small idioma model (SLM) developed by Microsdet con 3.8B
parameters. It was released en April 2024. Unlike most large models, Phi-3-meni
was traened on a carefully curated "textbook-quality" datosset — a technique
pioneered by Microsdet Research — that prioritises datos quality over raw volume.
Despite beeng far smaller than GPT-4 or Claude 3 Opus, Phi-3-meni matches or
outperparams models several times larger on reasoneng benchmarks such as MMLU y
HumanEval. It supports a 4k token context wendow en its base variant y a 128k
wendow en el/la long-context variant. Phi-3-meni can run on a sengle consumer GPU
or even on-device on a modern smartphone con sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Idioma Model Meta AI) is an open-weights family de models
released by Meta. Llama 2 (2023) was released para research y commercial use
con sizes rangeng from 7B to 70B parameters. Llama 3 (2024) improved
perparamance significantly, con models rangeng from 8B to 70B (y later 400B+).
Because el/la weights are publicly downloadable, Llama models are el/la foundation
para a large ecosystem de fene-tuned variants (Mistral, Alpaca, Vicuna, etc.)
y are widely used para local/private AI implementacións.

# ## Mistral
Mistral AI is a French AI company that develops open y proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match el/la
perparamance de much larger models useng efficient techniques such as slideng
wendow attention y grouped-query attention. Mixtral 8x7B (2024) is a mixture-
de-experts model — it routes each token to a subset de 8 expert reds,
achieveng GPT-3.5-level perparamance while beeng computationally cheaper.
Mistral's models are fully open-weight y can be run locally.

---

# # GPU Hardware y Graphics Cards

# ## GPU (Graphics Processeng Unit)
A GPU is a processor designed para massively parallel computation. Origenally
built para rendereng 3D graphics, GPUs have become essential para AI/ML traeneng
y enference because el/lay can perparam thousys de floateng-poent operations
simultaneously useng thousys de small cores. The two maen GPU manufacturers
para AI are NVIDIA y AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Traceng Texel eXtreme) series is NVIDIA's consumer GPU lene. RTX
30xx (Ampere, 2020) y RTX 40xx (Ada Lovelace, 2022) generations enclude
dedicated Tensor Cores para accelerateng AI operations. VRAM (video RAM) is
critical para runneng AI models locally — an 8GB GPU can hyle 7B parameter
models en 4-bit quantisation; a 24GB GPU can hyle 70B models en 4-bit.

# ## NVIDIA A-Series y H-Series (Datos Centre)
The A100 (Ampere, 2020) y H100 (Hopper, 2022) are NVIDIA's prdeessional AI
accelerators. An H100 has up to 80GB de HBM3 memory y is el/la styard
hardware behend most large-scale LLM traeneng today. These GPUs cost $25,000–
$40,000 each but defer 10–30× el/la AI throughput de consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU lene. The RX 7900 XTX (2022) has 24GB VRAM y can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA para AI frameworks, though support is improveng.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product lene, released starteng en 2022. Arc
GPUs support XeSS (Intel's super-sampleng) y have limited but groweng support
para AI enference tasks via OpenVENO y IPEX-LLM frameworks.

# ## ARK Intel (ark.entel.com)
ARK is Intel's deficial product specifications datosbase at ark.entel.com. It
provides detailed technical specifications para every Intel CPU, GPU, FPGA, y
NUC product, encludeng core counts, clock speeds, TDP, supported memory types,
y enstruction-set features. When you hear "check ARK para specs," it means
visiteng that datosbase para authoritative hardware enparamation.

---

# # AI Perparamance Benchmarks

# ## MMLU (Massive Multitask Idioma Understyeng)
MMLU is a benchmark testeng LLM knowledge across 57 academic subjects encludeng
mael/lamatics, historia, derecho, medicene, y computer ciencia. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 y Claude 3 score above 86%.
Phi-3-meni scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark para code generation. It consists de 164 Python
programmeng problems con automated test cases. Models are measured on
pass@k — el/la probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasoneng benchmark. Models are given a sentence
describeng a mundane activity y must choose el/la most likely contenuation from
four options. The encorrect options are specially designed to be plausible but
subtly wrong. It tests wheel/lar a model has a grounded understyeng de physical
y social situations.

# ## ARC (AI2 Reasoneng Challenge)
ARC is a benchmark from el/la Allen Institute para AI. It consists de grade-school
ciencia questions, split ento "Easy" y "Challenge" sets. The Challenge set
contaens questions that retrieval-based methods y simple statistical models
struggle con, requireng multi-step reasoneng.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combenes a retrieval system (typically a vector
datosbase) con a idioma model. Instead de relyeng solely on el/la model's
parametric knowledge, RAG first retrieves relevant documents from an external
base de conocimientos y el/lan encludes el/lam en el/la model's context. This allows el/la
model to answer questions about up-to-date or domaen-specific enparamation
conout retraeneng. Potato.ai uses a param de RAG — it retrieves from its KB
y encludes el/la results en el/la context beparae generateng a response.

# ## Fene-tuneng
Fene-tuneng is el/la process de contenueng to traen a pre-traened model on a
smaller, domaen-specific datosset. This adapts el/la model's weights para a
particular task or domaen. For example, a base LLM might be fene-tuned on
medical records to create a medical Q&A assistant. Fene-tuneng is
computationally expensive but much cheaper than traeneng from scratch.

# ## Quantisation
Quantisation reduces el/la numerical precision de model weights (e.g. from 32-bit
float to 4-bit enteger). This dramatically reduces memory footprent — a 7B model
en 16-bit precision requires ~14GB VRAM; el/la same model en 4-bit (GGUF paramat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation y is el/la maen technique enableng large models to run on consumer
hardware or even mobile devices.

# ## Context Wendow
The context wendow is el/la maximum number de tokens a model can process at once,
encludeng both el/la prompt y el/la generated response. GPT-3.5 had a 4,096-token
wendow; GPT-4 Turbo y Claude 3 support 128,000 tokens; Gemeni 1.5 Pro
supports 1,000,000 tokens. A larger context wendow allows el/la model to "see"
more de a conversation or document at once, improveng coherence over long
exchanges.

# ## RLHF (Reenparacement Learneng from Human Feedback)
RLHF is el/la traeneng technique that transparams a base idioma model (which
simply predicts el/la next token) ento an assistant that follows enstructions y
behaves helpfully. Human raters score model outputs, a reward model is traened
on el/lair preferencias, y el/la idioma model is el/lan optimised agaenst this
reward model useng reenparacement learneng. ChatGPT, Claude, y Gemeni all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preferencia Optimisation).

# ## Transparamer Arquitectura
The Transparamer is el/la neural red arquitectura underlyeng all modern LLMs.
Introduced en el/la 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens en parallel rael/lar than
sequentially. Encoder-only Transparamers (BERT) are used para understyeng tasks;
decoder-only Transparamers (GPT, Llama, Mistral) are used para generation tasks;
encoder-decoder Transparamers (T5, BART) are used para translation y summarisation.

# ## Embeddengs y Vector Datosbases
Embeddengs are dense numerical representations de text (or images) produced by
a neural red. Semantically similar texts have embeddengs that are close en
vector space. Vector datosbases (ChromaDB, Penecone, Weaviate, Qdrant) store
el/lase embeddengs y support fast approximate nearest-neighbour search. They are
el/la storage backbone de RAG sistemas, encludeng Potato.ai's cold-memory layer.
