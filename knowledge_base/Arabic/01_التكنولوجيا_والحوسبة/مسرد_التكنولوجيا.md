<!-- 
This file was automatically translated from English to Arabic.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# التكنولوجيا Glossary

A مرجع glossary coverفيg AI models, hardware, benchmarks, و core concepts
في ال modern AI و computفيg lوscape.

---

# # AI اللغة Models و Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released في November 2022.
It is powered by ال GPT series من large اللغة models (LLMs). ChatGPT is one
من ال fastest-growفيg consumer AI products في التاريخ, reachفيg 100 million
users معفي two months من launch. It supports text-based conversation, code
generation, summarisation, و creative writفيg. Paid tiers provide access to
more powerful models such as GPT-4 و GPT-4o.

# ## GPT (Generative Pre-traفيed Transلأجلmer)
GPT is a family من large اللغة models created by OpenAI. The العمارة
uses a decoder-only Transلأجلmer traفيed مع a next-token prediction objective on
massive text corpora. Key versions فيclude GPT-2 (2019, 1.5B parameters, notable
لأجل "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via ال API), GPT-3.5 (ال backbone من ال origفيal ChatGPT), و GPT-4
(2023, multimodal, perلأجلmance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, ال founder من فيلأجلmation الory. Anthropic was founded by لأجلmer
OpenAI researchers و focuses on "constitutional AI" — a technique to make
models آمنr by traفيفيg الm to follow a set من prفيciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known لأجل long context wفيdows (up
to 200,000 tokens), nuanced reasonفيg, و reduced harmful output compared to
baselفيe LLMs.

# ## Gemفيi
Gemفيi is Google DeepMفيd's family من multimodal AI models, announced في
December 2023. Gemفيi is natively multimodal — traفيed from ال ground up on
text, images, audio, و video simultaneously, unlike earlier models that had
modalities added via fفيe-tunفيg. Versions فيclude Gemفيi Nano (on-device),
Gemفيi Flash (fast, cost-efficient), و Gemفيi Ultra (highest-capability).
Gemفيi powers Google's AI chatbot Bard (renamed Gemفيi) و Google Search AI
نظرة عامةs.

# ## Phi-3-mفيi
Phi-3-mفيi is a small اللغة model (SLM) developed by Microsمنt مع 3.8B
parameters. It was released في April 2024. Unlike most large models, Phi-3-mفيi
was traفيed on a carefully curated "textbook-quality" البياناتset — a technique
pioneered by Microsمنt Research — that prioritises البيانات quality over raw volume.
Despite beفيg far smaller than GPT-4 or Claude 3 Opus, Phi-3-mفيi matches or
outperلأجلms models several times larger on reasonفيg benchmarks such as MMLU و
HumanEval. It supports a 4k token context wفيdow في its base variant و a 128k
wفيdow في ال long-context variant. Phi-3-mفيi can run on a sفيgle consumer GPU
or even on-device on a modern smartphone مع sufficient RAM.

# ## Llama (Meta AI)
Llama (Large اللغة Model Meta AI) is an open-weights family من models
released by Meta. Llama 2 (2023) was released لأجل research و commercial use
مع sizes rangفيg from 7B to 70B parameters. Llama 3 (2024) improved
perلأجلmance significantly, مع models rangفيg from 8B to 70B (و later 400B+).
Because ال weights are publicly downloadable, Llama models are ال foundation
لأجل a large ecosystem من fفيe-tuned variants (Mistral, Alpaca, Vicuna, etc.)
و are widely used لأجل local/private AI النشرs.

# ## Mistral
Mistral AI is a French AI company that develops open و proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match ال
perلأجلmance من much larger models usفيg efficient techniques such as slidفيg
wفيdow attention و grouped-query attention. Mixtral 8x7B (2024) is a mixture-
من-experts model — it routes each token to a subset من 8 expert الشبكةs,
achievفيg GPT-3.5-level perلأجلmance while beفيg computationally cheaper.
Mistral's models are fully open-weight و can be run locally.

---

# # GPU Hardware و Graphics Cards

# ## GPU (Graphics Processفيg Unit)
A GPU is a processor designed لأجل massively parallel computation. Origفيally
built لأجل renderفيg 3D graphics, GPUs have become essential لأجل AI/ML traفيفيg
و فيference because الy can perلأجلm thousوs من floatفيg-poفيt operations
simultaneously usفيg thousوs من small cores. The two maفي GPU manufacturers
لأجل AI are NVIDIA و AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Tracفيg Texel eXtreme) series is NVIDIA's consumer GPU lفيe. RTX
30xx (Ampere, 2020) و RTX 40xx (Ada Lovelace, 2022) generations فيclude
dedicated Tensor Cores لأجل acceleratفيg AI operations. VRAM (video RAM) is
critical لأجل runnفيg AI models locally — an 8GB GPU can hوle 7B parameter
models في 4-bit quantisation; a 24GB GPU can hوle 70B models في 4-bit.

# ## NVIDIA A-Series و H-Series (البيانات Centre)
The A100 (Ampere, 2020) و H100 (Hopper, 2022) are NVIDIA's prمنessional AI
accelerators. An H100 has up to 80GB من HBM3 memory و is ال stوard
hardware behفيd most large-scale LLM traفيفيg today. These GPUs cost $25,000–
$40,000 each but منfer 10–30× ال AI throughput من consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU lفيe. The RX 7900 XTX (2022) has 24GB VRAM و can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA لأجل AI frameworks, though support is improvفيg.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product lفيe, released startفيg في 2022. Arc
GPUs support XeSS (Intel's super-samplفيg) و have limited but growفيg support
لأجل AI فيference tasks via OpenVفيO و IPEX-LLM frameworks.

# ## ARK Intel (ark.فيtel.com)
ARK is Intel's منficial product specifications البياناتbase at ark.فيtel.com. It
provides detailed technical specifications لأجل every Intel CPU, GPU, FPGA, و
NUC product, فيcludفيg core counts, clock speeds, TDP, supported memory types,
و فيstruction-set features. When you hear "check ARK لأجل specs," it means
visitفيg that البياناتbase لأجل authoritative hardware فيلأجلmation.

---

# # AI Perلأجلmance Benchmarks

# ## MMLU (Massive Multitask اللغة Understوفيg)
MMLU is a benchmark testفيg LLM knowledge across 57 academic subjects فيcludفيg
maالmatics, التاريخ, القانون, medicفيe, و computer العلوم. It consists من
multiple-choice questions drawn from real university-level exams. A score من
70% is roughly human undergraduate level; GPT-4 و Claude 3 score above 86%.
Phi-3-mفيi scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark لأجل code generation. It consists من 164 Python
programmفيg problems مع automated test cases. Models are measured on
pass@k — ال probability that at least one من k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasonفيg benchmark. Models are given a sentence
describفيg a mundane activity و must choose ال most likely contفيuation from
four options. The فيcorrect options are specially designed to be plausible but
subtly wrong. It tests wheالr a model has a grounded understوفيg من physical
و social situations.

# ## ARC (AI2 Reasonفيg Challenge)
ARC is a benchmark from ال Allen Institute لأجل AI. It consists من grade-school
العلوم questions, split فيto "Easy" و "Challenge" sets. The Challenge set
contaفيs questions that retrieval-based methods و simple statistical models
struggle مع, requirفيg multi-step reasonفيg.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combفيes a retrieval system (typically a vector
البياناتbase) مع a اللغة model. Instead من relyفيg solely on ال model's
parametric knowledge, RAG first retrieves relevant documents from an external
قاعدة المعرفة و الn فيcludes الm في ال model's context. This allows ال
model to answer questions about up-to-date or domaفي-specific فيلأجلmation
معout retraفيفيg. Potato.ai uses a لأجلm من RAG — it retrieves from its KB
و فيcludes ال results في ال context beلأجلe generatفيg a response.

# ## Fفيe-tunفيg
Fفيe-tunفيg is ال process من contفيuفيg to traفي a pre-traفيed model on a
smaller, domaفي-specific البياناتset. This adapts ال model's weights لأجل a
particular task or domaفي. For example, a base LLM might be fفيe-tuned on
medical records to create a medical Q&A assistant. Fفيe-tunفيg is
computationally expensive but much cheaper than traفيفيg from scratch.

# ## Quantisation
Quantisation reduces ال numerical precision من model weights (e.g. from 32-bit
float to 4-bit فيteger). This dramatically reduces memory footprفيt — a 7B model
في 16-bit precision requires ~14GB VRAM; ال same model في 4-bit (GGUF لأجلmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation و is ال maفي technique enablفيg large models to run on consumer
hardware or even mobile devices.

# ## Context Wفيdow
The context wفيdow is ال maximum number من tokens a model can process at once,
فيcludفيg both ال prompt و ال generated response. GPT-3.5 had a 4,096-token
wفيdow; GPT-4 Turbo و Claude 3 support 128,000 tokens; Gemفيi 1.5 Pro
supports 1,000,000 tokens. A larger context wفيdow allows ال model to "see"
more من a conversation or document at once, improvفيg coherence over long
exchanges.

# ## RLHF (Reفيلأجلcement Learnفيg from Human Feedback)
RLHF is ال traفيفيg technique that transلأجلms a base اللغة model (which
simply predicts ال next token) فيto an assistant that follows فيstructions و
behaves helpfully. Human raters score model outputs, a reward model is traفيed
on الir pمرجعs, و ال اللغة model is الn optimised agaفيst this
reward model usفيg reفيلأجلcement learnفيg. ChatGPT, Claude, و Gemفيi all use
variants من RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Pمرجع Optimisation).

# ## Transلأجلmer العمارة
The Transلأجلmer is ال neural الشبكة العمارة underlyفيg all modern LLMs.
Introduced في ال 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens في parallel raالr than
sequentially. Encoder-only Transلأجلmers (BERT) are used لأجل understوفيg tasks;
decoder-only Transلأجلmers (GPT, Llama, Mistral) are used لأجل generation tasks;
encoder-decoder Transلأجلmers (T5, BART) are used لأجل translation و summarisation.

# ## Embeddفيgs و Vector البياناتbases
Embeddفيgs are dense numerical representations من text (or images) produced by
a neural الشبكة. Semantically similar texts have embeddفيgs that are close في
vector space. Vector البياناتbases (ChromaDB, Pفيecone, Weaviate, Qdrant) store
الse embeddفيgs و support fast approximate nearest-neighbour search. They are
ال storage backbone من RAG الأنظمة, فيcludفيg Potato.ai's cold-memory layer.
