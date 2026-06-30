<!-- 
This file was automatically translated from English to Turkish.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Teknoloji Glossary

A referans glossary coveriçiçindedeg AI models, hardware, benchmarks, ve core concepts
içiçindede bu modern AI ve computiçiçindedeg lvescape.

---

# # AI Dil Models ve Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released içiçindede November 2022.
It is powered by bu GPT series içiçindede large dil models (LLMs). ChatGPT is one
içiçindede bu fastest-growiçiçindedeg consumer AI products içiçindede tarih, reachiçiçindedeg 100 million
users ileiçiçindede two months içiçindede launch. It supports text-based conversation, code
generation, summarisation, ve creative writiçiçindedeg. Paid tiers provide access to
more powerful models such as GPT-4 ve GPT-4o.

# ## GPT (Generative Pre-traiçiçindedeed Transiçinmer)
GPT is a family içiçindede large dil models created by OpenAI. The mimari
uses a decoder-only Transiçinmer traiçiçindedeed ile a next-token prediction objective on
massive text corpora. Key versions içiçindedeclude GPT-2 (2019, 1.5B parameters, notable
için "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via bu API), GPT-3.5 (bu backbone içiçindede bu origiçiçindedeal ChatGPT), ve GPT-4
(2023, multimodal, periçinmance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, bu founder içiçindede içiçindedeiçinmation buory. Anthropic was founded by içinmer
OpenAI researchers ve focuses on "constitutional AI" — a technique to make
models güvenlir by traiçiçindedeiçiçindedeg bum to follow a set içiçindede priçiçindedeciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known için long context wiçiçindededows (up
to 200,000 tokens), nuanced reasoniçiçindedeg, ve reduced harmful output compared to
baseliçiçindedee LLMs.

# ## Gemiçiçindedei
Gemiçiçindedei is Google DeepMiçiçindeded's family içiçindede multimodal AI models, announced içiçindede
December 2023. Gemiçiçindedei is natively multimodal — traiçiçindedeed from bu ground up on
text, images, audio, ve video simultaneously, unlike earlier models that had
modalities added via fiçiçindedee-tuniçiçindedeg. Versions içiçindedeclude Gemiçiçindedei Nano (on-device),
Gemiçiçindedei Flash (fast, cost-efficient), ve Gemiçiçindedei Ultra (highest-capability).
Gemiçiçindedei powers Google's AI chatbot Bard (renamed Gemiçiçindedei) ve Google Search AI
Genel Bakışs.

# ## Phi-3-miçiçindedei
Phi-3-miçiçindedei is a small dil model (SLM) developed by Microsiçiçindedet ile 3.8B
parameters. It was released içiçindede April 2024. Unlike most large models, Phi-3-miçiçindedei
was traiçiçindedeed on a carefully curated "textbook-quality" veriset — a technique
pioneered by Microsiçiçindedet Research — that prioritises veri quality over raw volume.
Despite beiçiçindedeg far smaller than GPT-4 or Claude 3 Opus, Phi-3-miçiçindedei matches or
outperiçinms models several times larger on reasoniçiçindedeg benchmarks such as MMLU ve
HumanEval. It supports a 4k token context wiçiçindededow içiçindede its base variant ve a 128k
wiçiçindededow içiçindede bu long-context variant. Phi-3-miçiçindedei can run on a siçiçindedegle consumer GPU
or even on-device on a modern smartphone ile sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Dil Model Meta AI) is an open-weights family içiçindede models
released by Meta. Llama 2 (2023) was released için research ve commercial use
ile sizes rangiçiçindedeg from 7B to 70B parameters. Llama 3 (2024) improved
periçinmance significantly, ile models rangiçiçindedeg from 8B to 70B (ve later 400B+).
Because bu weights are publicly downloadable, Llama models are bu foundation
için a large ecosystem içiçindede fiçiçindedee-tuned variants (Mistral, Alpaca, Vicuna, etc.)
ve are widely used için local/private AI dağıtıms.

# ## Mistral
Mistral AI is a French AI company that develops open ve proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match bu
periçinmance içiçindede much larger models usiçiçindedeg efficient techniques such as slidiçiçindedeg
wiçiçindededow attention ve grouped-query attention. Mixtral 8x7B (2024) is a mixture-
içiçindede-experts model — it routes each token to a subset içiçindede 8 expert ağs,
achieviçiçindedeg GPT-3.5-level periçinmance while beiçiçindedeg computationally cheaper.
Mistral's models are fully open-weight ve can be run locally.

---

# # GPU Hardware ve Graphics Cards

# ## GPU (Graphics Processiçiçindedeg Unit)
A GPU is a processor designed için massively parallel computation. Origiçiçindedeally
built için renderiçiçindedeg 3D graphics, GPUs have become essential için AI/ML traiçiçindedeiçiçindedeg
ve içiçindedeference because buy can periçinm thousves içiçindede floatiçiçindedeg-poiçiçindedet operations
simultaneously usiçiçindedeg thousves içiçindede small cores. The two maiçiçindede GPU manufacturers
için AI are NVIDIA ve AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Traciçiçindedeg Texel eXtreme) series is NVIDIA's consumer GPU liçiçindedee. RTX
30xx (Ampere, 2020) ve RTX 40xx (Ada Lovelace, 2022) generations içiçindedeclude
dedicated Tensor Cores için acceleratiçiçindedeg AI operations. VRAM (video RAM) is
critical için runniçiçindedeg AI models locally — an 8GB GPU can hvele 7B parameter
models içiçindede 4-bit quantisation; a 24GB GPU can hvele 70B models içiçindede 4-bit.

# ## NVIDIA A-Series ve H-Series (Veri Centre)
The A100 (Ampere, 2020) ve H100 (Hopper, 2022) are NVIDIA's priçiçindedeessional AI
accelerators. An H100 has up to 80GB içiçindede HBM3 memory ve is bu stveard
hardware behiçiçindeded most large-scale LLM traiçiçindedeiçiçindedeg today. These GPUs cost $25,000–
$40,000 each but içiçindedefer 10–30× bu AI throughput içiçindede consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU liçiçindedee. The RX 7900 XTX (2022) has 24GB VRAM ve can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA için AI frameworks, though support is improviçiçindedeg.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product liçiçindedee, released startiçiçindedeg içiçindede 2022. Arc
GPUs support XeSS (Intel's super-sampliçiçindedeg) ve have limited but growiçiçindedeg support
için AI içiçindedeference tasks via OpenVIÇINDEO ve IPEX-LLM frameworks.

# ## ARK Intel (ark.içiçindedetel.com)
ARK is Intel's içiçindedeficial product specifications veribase at ark.içiçindedetel.com. It
provides detailed technical specifications için every Intel CPU, GPU, FPGA, ve
NUC product, içiçindedecludiçiçindedeg core counts, clock speeds, TDP, supported memory types,
ve içiçindedestruction-set features. When you hear "check ARK için specs," it means
visitiçiçindedeg that veribase için authoritative hardware içiçindedeiçinmation.

---

# # AI Periçinmance Benchmarks

# ## MMLU (Massive Multitask Dil Understveiçiçindedeg)
MMLU is a benchmark testiçiçindedeg LLM knowledge across 57 academic subjects içiçindedecludiçiçindedeg
mabumatics, tarih, hukuk, mediciçiçindedee, ve computer bilim. It consists içiçindede
multiple-choice questions drawn from real university-level exams. A score içiçindede
70% is roughly human undergraduate level; GPT-4 ve Claude 3 score above 86%.
Phi-3-miçiçindedei scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark için code generation. It consists içiçindede 164 Python
programmiçiçindedeg problems ile automated test cases. Models are measured on
pass@k — bu probability that at least one içiçindede k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasoniçiçindedeg benchmark. Models are given a sentence
describiçiçindedeg a mundane activity ve must choose bu most likely contiçiçindedeuation from
four options. The içiçindedecorrect options are specially designed to be plausible but
subtly wrong. It tests whebur a model has a grounded understveiçiçindedeg içiçindede physical
ve social situations.

# ## ARC (AI2 Reasoniçiçindedeg Challenge)
ARC is a benchmark from bu Allen Institute için AI. It consists içiçindede grade-school
bilim questions, split içiçindedeto "Easy" ve "Challenge" sets. The Challenge set
contaiçiçindedes questions that retrieval-based methods ve simple statistical models
struggle ile, requiriçiçindedeg multi-step reasoniçiçindedeg.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combiçiçindedees a retrieval system (typically a vector
veribase) ile a dil model. Instead içiçindede relyiçiçindedeg solely on bu model's
parametric knowledge, RAG first retrieves relevant documents from an external
bilgi tabanı ve bun içiçindedecludes bum içiçindede bu model's context. This allows bu
model to answer questions about up-to-date or domaiçiçindede-specific içiçindedeiçinmation
ileout retraiçiçindedeiçiçindedeg. Potato.ai uses a içinm içiçindede RAG — it retrieves from its KB
ve içiçindedecludes bu results içiçindede bu context beiçine generatiçiçindedeg a response.

# ## Fiçiçindedee-tuniçiçindedeg
Fiçiçindedee-tuniçiçindedeg is bu process içiçindede contiçiçindedeuiçiçindedeg to traiçiçindede a pre-traiçiçindedeed model on a
smaller, domaiçiçindede-specific veriset. This adapts bu model's weights için a
particular task or domaiçiçindede. For example, a base LLM might be fiçiçindedee-tuned on
medical records to create a medical Q&A assistant. Fiçiçindedee-tuniçiçindedeg is
computationally expensive but much cheaper than traiçiçindedeiçiçindedeg from scratch.

# ## Quantisation
Quantisation reduces bu numerical precision içiçindede model weights (e.g. from 32-bit
float to 4-bit içiçindedeteger). This dramatically reduces memory footpriçiçindedet — a 7B model
içiçindede 16-bit precision requires ~14GB VRAM; bu same model içiçindede 4-bit (GGUF içinmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation ve is bu maiçiçindede technique enabliçiçindedeg large models to run on consumer
hardware or even mobile devices.

# ## Context Wiçiçindededow
The context wiçiçindededow is bu maximum number içiçindede tokens a model can process at once,
içiçindedecludiçiçindedeg both bu prompt ve bu generated response. GPT-3.5 had a 4,096-token
wiçiçindededow; GPT-4 Turbo ve Claude 3 support 128,000 tokens; Gemiçiçindedei 1.5 Pro
supports 1,000,000 tokens. A larger context wiçiçindededow allows bu model to "see"
more içiçindede a conversation or document at once, improviçiçindedeg coherence over long
exchanges.

# ## RLHF (Reiçiçindedeiçincement Learniçiçindedeg from Human Feedback)
RLHF is bu traiçiçindedeiçiçindedeg technique that transiçinms a base dil model (which
simply predicts bu next token) içiçindedeto an assistant that follows içiçindedestructions ve
behaves helpfully. Human raters score model outputs, a reward model is traiçiçindedeed
on buir preferanss, ve bu dil model is bun optimised agaiçiçindedest this
reward model usiçiçindedeg reiçiçindedeiçincement learniçiçindedeg. ChatGPT, Claude, ve Gemiçiçindedei all use
variants içiçindede RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preferans Optimisation).

# ## Transiçinmer Mimari
The Transiçinmer is bu neural ağ mimari underlyiçiçindedeg all modern LLMs.
Introduced içiçindede bu 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens içiçindede parallel rabur than
sequentially. Encoder-only Transiçinmers (BERT) are used için understveiçiçindedeg tasks;
decoder-only Transiçinmers (GPT, Llama, Mistral) are used için generation tasks;
encoder-decoder Transiçinmers (T5, BART) are used için translation ve summarisation.

# ## Embeddiçiçindedegs ve Vector Veribases
Embeddiçiçindedegs are dense numerical representations içiçindede text (or images) produced by
a neural ağ. Semantically similar texts have embeddiçiçindedegs that are close içiçindede
vector space. Vector veribases (ChromaDB, Piçiçindedeecone, Weaviate, Qdrant) store
buse embeddiçiçindedegs ve support fast approximate nearest-neighbour search. They are
bu storage backbone içiçindede RAG sistemler, içiçindedecludiçiçindedeg Potato.ai's cold-memory layer.
