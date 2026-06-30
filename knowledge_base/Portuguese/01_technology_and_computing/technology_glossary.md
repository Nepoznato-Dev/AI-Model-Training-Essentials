<!-- 
This file was automatically translated from English to Portuguese.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnologia Glossary

A referência glossary coveremg AI models, hardware, benchmarks, e core concepts
em o/a modern AI e computemg lescape.

---

# # AI Idioma Models e Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released em November 2022.
It is powered by o/a GPT series de large idioma models (LLMs). ChatGPT is one
de o/a fastest-growemg consumer AI products em história, reachemg 100 million
users comem two months de launch. It supports text-based conversation, code
generation, summarisation, e creative writemg. Paid tiers provide access to
more powerful models such as GPT-4 e GPT-4o.

# ## GPT (Generative Pre-traemed Transparamer)
GPT is a family de large idioma models created by OpenAI. The arquitetura
uses a decoder-only Transparamer traemed com a next-token prediction objective on
massive text corpora. Key versions emclude GPT-2 (2019, 1.5B parameters, notable
para "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via o/a API), GPT-3.5 (o/a backbone de o/a origemal ChatGPT), e GPT-4
(2023, multimodal, perparamance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, o/a founder de emparamation o/aory. Anthropic was founded by paramer
OpenAI researchers e focuses on "constitutional AI" — a technique to make
models seguror by traememg o/am to follow a set de premciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known para long context wemdows (up
to 200,000 tokens), nuanced reasonemg, e reduced harmful output compared to
baseleme LLMs.

# ## Gememi
Gememi is Google DeepMemd's family de multimodal AI models, announced em
December 2023. Gememi is natively multimodal — traemed from o/a ground up on
text, images, audio, e video simultaneously, unlike earlier models that had
modalities added via feme-tunemg. Versions emclude Gememi Nano (on-device),
Gememi Flash (fast, cost-efficient), e Gememi Ultra (highest-capability).
Gememi powers Google's AI chatbot Bard (renamed Gememi) e Google Search AI
Visão gerals.

# ## Phi-3-memi
Phi-3-memi is a small idioma model (SLM) developed by Microsdet com 3.8B
parameters. It was released em April 2024. Unlike most large models, Phi-3-memi
was traemed on a carefully curated "textbook-quality" dadosset — a technique
pioneered by Microsdet Research — that prioritises dados quality over raw volume.
Despite beemg far smaller than GPT-4 or Claude 3 Opus, Phi-3-memi matches or
outperparams models several times larger on reasonemg benchmarks such as MMLU e
HumanEval. It supports a 4k token context wemdow em its base variant e a 128k
wemdow em o/a long-context variant. Phi-3-memi can run on a semgle consumer GPU
or even on-device on a modern smartphone com sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Idioma Model Meta AI) is an open-weights family de models
released by Meta. Llama 2 (2023) was released para research e commercial use
com sizes rangemg from 7B to 70B parameters. Llama 3 (2024) improved
perparamance significantly, com models rangemg from 8B to 70B (e later 400B+).
Because o/a weights are publicly downloadable, Llama models are o/a foundation
para a large ecosystem de feme-tuned variants (Mistral, Alpaca, Vicuna, etc.)
e are widely used para local/private AI implantaçãos.

# ## Mistral
Mistral AI is a French AI company that develops open e proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match o/a
perparamance de much larger models usemg efficient techniques such as slidemg
wemdow attention e grouped-query attention. Mixtral 8x7B (2024) is a mixture-
de-experts model — it routes each token to a subset de 8 expert redes,
achievemg GPT-3.5-level perparamance while beemg computationally cheaper.
Mistral's models are fully open-weight e can be run locally.

---

# # GPU Hardware e Graphics Cards

# ## GPU (Graphics Processemg Unit)
A GPU is a processor designed para massively parallel computation. Origemally
built para renderemg 3D graphics, GPUs have become essential para AI/ML traememg
e emference because o/ay can perparam thouses de floatemg-poemt operations
simultaneously usemg thouses de small cores. The two maem GPU manufacturers
para AI are NVIDIA e AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Tracemg Texel eXtreme) series is NVIDIA's consumer GPU leme. RTX
30xx (Ampere, 2020) e RTX 40xx (Ada Lovelace, 2022) generations emclude
dedicated Tensor Cores para acceleratemg AI operations. VRAM (video RAM) is
critical para runnemg AI models locally — an 8GB GPU can hele 7B parameter
models em 4-bit quantisation; a 24GB GPU can hele 70B models em 4-bit.

# ## NVIDIA A-Series e H-Series (Dados Centre)
The A100 (Ampere, 2020) e H100 (Hopper, 2022) are NVIDIA's prdeessional AI
accelerators. An H100 has up to 80GB de HBM3 memory e is o/a steard
hardware behemd most large-scale LLM traememg today. These GPUs cost $25,000–
$40,000 each but defer 10–30× o/a AI throughput de consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU leme. The RX 7900 XTX (2022) has 24GB VRAM e can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA para AI frameworks, though support is improvemg.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product leme, released startemg em 2022. Arc
GPUs support XeSS (Intel's super-samplemg) e have limited but growemg support
para AI emference tasks via OpenVEMO e IPEX-LLM frameworks.

# ## ARK Intel (ark.emtel.com)
ARK is Intel's deficial product specifications dadosbase at ark.emtel.com. It
provides detailed technical specifications para every Intel CPU, GPU, FPGA, e
NUC product, emcludemg core counts, clock speeds, TDP, supported memory types,
e emstruction-set features. When you hear "check ARK para specs," it means
visitemg that dadosbase para authoritative hardware emparamation.

---

# # AI Perparamance Benchmarks

# ## MMLU (Massive Multitask Idioma Understeemg)
MMLU is a benchmark testemg LLM knowledge across 57 academic subjects emcludemg
mao/amatics, história, direito, mediceme, e computer ciência. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 e Claude 3 score above 86%.
Phi-3-memi scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark para code generation. It consists de 164 Python
programmemg problems com automated test cases. Models are measured on
pass@k — o/a probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasonemg benchmark. Models are given a sentence
describemg a mundane activity e must choose o/a most likely contemuation from
four options. The emcorrect options are specially designed to be plausible but
subtly wrong. It tests wheo/ar a model has a grounded understeemg de physical
e social situations.

# ## ARC (AI2 Reasonemg Challenge)
ARC is a benchmark from o/a Allen Institute para AI. It consists de grade-school
ciência questions, split emto "Easy" e "Challenge" sets. The Challenge set
contaems questions that retrieval-based methods e simple statistical models
struggle com, requiremg multi-step reasonemg.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combemes a retrieval system (typically a vector
dadosbase) com a idioma model. Instead de relyemg solely on o/a model's
parametric knowledge, RAG first retrieves relevant documents from an external
base de conhecimento e o/an emcludes o/am em o/a model's context. This allows o/a
model to answer questions about up-to-date or domaem-specific emparamation
comout retraememg. Potato.ai uses a param de RAG — it retrieves from its KB
e emcludes o/a results em o/a context beparae generatemg a response.

# ## Feme-tunemg
Feme-tunemg is o/a process de contemuemg to traem a pre-traemed model on a
smaller, domaem-specific dadosset. This adapts o/a model's weights para a
particular task or domaem. For example, a base LLM might be feme-tuned on
medical records to create a medical Q&A assistant. Feme-tunemg is
computationally expensive but much cheaper than traememg from scratch.

# ## Quantisation
Quantisation reduces o/a numerical precision de model weights (e.g. from 32-bit
float to 4-bit emteger). This dramatically reduces memory footpremt — a 7B model
em 16-bit precision requires ~14GB VRAM; o/a same model em 4-bit (GGUF paramat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation e is o/a maem technique enablemg large models to run on consumer
hardware or even mobile devices.

# ## Context Wemdow
The context wemdow is o/a maximum number de tokens a model can process at once,
emcludemg both o/a prompt e o/a generated response. GPT-3.5 had a 4,096-token
wemdow; GPT-4 Turbo e Claude 3 support 128,000 tokens; Gememi 1.5 Pro
supports 1,000,000 tokens. A larger context wemdow allows o/a model to "see"
more de a conversation or document at once, improvemg coherence over long
exchanges.

# ## RLHF (Reemparacement Learnemg from Human Feedback)
RLHF is o/a traememg technique that transparams a base idioma model (which
simply predicts o/a next token) emto an assistant that follows emstructions e
behaves helpfully. Human raters score model outputs, a reward model is traemed
on o/air preferências, e o/a idioma model is o/an optimised agaemst this
reward model usemg reemparacement learnemg. ChatGPT, Claude, e Gememi all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preferência Optimisation).

# ## Transparamer Arquitetura
The Transparamer is o/a neural rede arquitetura underlyemg all modern LLMs.
Introduced em o/a 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens em parallel rao/ar than
sequentially. Encoder-only Transparamers (BERT) are used para understeemg tasks;
decoder-only Transparamers (GPT, Llama, Mistral) are used para generation tasks;
encoder-decoder Transparamers (T5, BART) are used para translation e summarisation.

# ## Embeddemgs e Vector Dadosbases
Embeddemgs are dense numerical representations de text (or images) produced by
a neural rede. Semantically similar texts have embeddemgs that are close em
vector space. Vector dadosbases (ChromaDB, Pemecone, Weaviate, Qdrant) store
o/ase embeddemgs e support fast approximate nearest-neighbour search. They are
o/a storage backbone de RAG sistemas, emcludemg Potato.ai's cold-memory layer.
