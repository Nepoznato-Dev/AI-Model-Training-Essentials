<!-- 
This file was automatically translated from English to French.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie Glossary

A référence glossary coverdansg AI models, hardware, benchmarks, et core concepts
dans le/la modern AI et computdansg letscape.

---

# # AI Langue Models et Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released dans November 2022.
It is powered by le/la GPT series de large langue models (LLMs). ChatGPT is one
de le/la fastest-growdansg consumer AI products dans histoire, reachdansg 100 million
users avecdans two months de launch. It supports text-based conversation, code
generation, summarisation, et creative writdansg. Paid tiers provide access to
more powerful models such as GPT-4 et GPT-4o.

# ## GPT (Generative Pre-tradansed Transpourmer)
GPT is a family de large langue models created by OpenAI. The architecture
uses a decoder-only Transpourmer tradansed avec a next-token prediction objective on
massive text corpora. Key versions dansclude GPT-2 (2019, 1.5B parameters, notable
pour "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via le/la API), GPT-3.5 (le/la backbone de le/la origdansal ChatGPT), et GPT-4
(2023, multimodal, perpourmance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, le/la founder de danspourmation le/laory. Anthropic was founded by pourmer
OpenAI researchers et focuses on "constitutional AI" — a technique to make
models sûrr by tradansdansg le/lam to follow a set de prdansciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known pour long context wdansdows (up
to 200,000 tokens), nuanced reasondansg, et reduced harmful output compared to
baseldanse LLMs.

# ## Gemdansi
Gemdansi is Google DeepMdansd's family de multimodal AI models, announced dans
December 2023. Gemdansi is natively multimodal — tradansed from le/la ground up on
text, images, audio, et video simultaneously, unlike earlier models that had
modalities added via fdanse-tundansg. Versions dansclude Gemdansi Nano (on-device),
Gemdansi Flash (fast, cost-efficient), et Gemdansi Ultra (highest-capability).
Gemdansi powers Google's AI chatbot Bard (renamed Gemdansi) et Google Search AI
Aperçus.

# ## Phi-3-mdansi
Phi-3-mdansi is a small langue model (SLM) developed by Microsdet avec 3.8B
parameters. It was released dans April 2024. Unlike most large models, Phi-3-mdansi
was tradansed on a carefully curated "textbook-quality" donnéesset — a technique
pioneered by Microsdet Research — that prioritises données quality over raw volume.
Despite bedansg far smaller than GPT-4 or Claude 3 Opus, Phi-3-mdansi matches or
outperpourms models several times larger on reasondansg benchmarks such as MMLU et
HumanEval. It supports a 4k token context wdansdow dans its base variant et a 128k
wdansdow dans le/la long-context variant. Phi-3-mdansi can run on a sdansgle consumer GPU
or even on-device on a modern smartphone avec sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Langue Model Meta AI) is an open-weights family de models
released by Meta. Llama 2 (2023) was released pour research et commercial use
avec sizes rangdansg from 7B to 70B parameters. Llama 3 (2024) improved
perpourmance significantly, avec models rangdansg from 8B to 70B (et later 400B+).
Because le/la weights are publicly downloadable, Llama models are le/la foundation
pour a large ecosystem de fdanse-tuned variants (Mistral, Alpaca, Vicuna, etc.)
et are widely used pour local/private AI déploiements.

# ## Mistral
Mistral AI is a French AI company that develops open et proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match le/la
perpourmance de much larger models usdansg efficient techniques such as sliddansg
wdansdow attention et grouped-query attention. Mixtral 8x7B (2024) is a mixture-
de-experts model — it routes each token to a subset de 8 expert réseaus,
achievdansg GPT-3.5-level perpourmance while bedansg computationally cheaper.
Mistral's models are fully open-weight et can be run locally.

---

# # GPU Hardware et Graphics Cards

# ## GPU (Graphics Processdansg Unit)
A GPU is a processor designed pour massively parallel computation. Origdansally
built pour renderdansg 3D graphics, GPUs have become essential pour AI/ML tradansdansg
et dansference because le/lay can perpourm thousets de floatdansg-podanst operations
simultaneously usdansg thousets de small cores. The two madans GPU manufacturers
pour AI are NVIDIA et AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Tracdansg Texel eXtreme) series is NVIDIA's consumer GPU ldanse. RTX
30xx (Ampere, 2020) et RTX 40xx (Ada Lovelace, 2022) generations dansclude
dedicated Tensor Cores pour acceleratdansg AI operations. VRAM (video RAM) is
critical pour runndansg AI models locally — an 8GB GPU can hetle 7B parameter
models dans 4-bit quantisation; a 24GB GPU can hetle 70B models dans 4-bit.

# ## NVIDIA A-Series et H-Series (Données Centre)
The A100 (Ampere, 2020) et H100 (Hopper, 2022) are NVIDIA's prdeessional AI
accelerators. An H100 has up to 80GB de HBM3 memory et is le/la stetard
hardware behdansd most large-scale LLM tradansdansg today. These GPUs cost $25,000–
$40,000 each but defer 10–30× le/la AI throughput de consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU ldanse. The RX 7900 XTX (2022) has 24GB VRAM et can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA pour AI frameworks, though support is improvdansg.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product ldanse, released startdansg dans 2022. Arc
GPUs support XeSS (Intel's super-sampldansg) et have limited but growdansg support
pour AI dansference tasks via OpenVDANSO et IPEX-LLM frameworks.

# ## ARK Intel (ark.danstel.com)
ARK is Intel's deficial product specifications donnéesbase at ark.danstel.com. It
provides detailed technical specifications pour every Intel CPU, GPU, FPGA, et
NUC product, danscluddansg core counts, clock speeds, TDP, supported memory types,
et dansstruction-set features. When you hear "check ARK pour specs," it means
visitdansg that donnéesbase pour authoritative hardware danspourmation.

---

# # AI Perpourmance Benchmarks

# ## MMLU (Massive Multitask Langue Understetdansg)
MMLU is a benchmark testdansg LLM knowledge across 57 academic subjects danscluddansg
male/lamatics, histoire, droit, medicdanse, et computer science. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 et Claude 3 score above 86%.
Phi-3-mdansi scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark pour code generation. It consists de 164 Python
programmdansg problems avec automated test cases. Models are measured on
pass@k — le/la probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasondansg benchmark. Models are given a sentence
describdansg a mundane activity et must choose le/la most likely contdansuation from
four options. The danscorrect options are specially designed to be plausible but
subtly wrong. It tests whele/lar a model has a grounded understetdansg de physical
et social situations.

# ## ARC (AI2 Reasondansg Challenge)
ARC is a benchmark from le/la Allen Institute pour AI. It consists de grade-school
science questions, split dansto "Easy" et "Challenge" sets. The Challenge set
contadanss questions that retrieval-based methods et simple statistical models
struggle avec, requirdansg multi-step reasondansg.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combdanses a retrieval system (typically a vector
donnéesbase) avec a langue model. Instead de relydansg solely on le/la model's
parametric knowledge, RAG first retrieves relevant documents from an external
base de connaissances et le/lan danscludes le/lam dans le/la model's context. This allows le/la
model to answer questions about up-to-date or domadans-specific danspourmation
avecout retradansdansg. Potato.ai uses a pourm de RAG — it retrieves from its KB
et danscludes le/la results dans le/la context bepoure generatdansg a response.

# ## Fdanse-tundansg
Fdanse-tundansg is le/la process de contdansudansg to tradans a pre-tradansed model on a
smaller, domadans-specific donnéesset. This adapts le/la model's weights pour a
particular task or domadans. For example, a base LLM might be fdanse-tuned on
medical records to create a medical Q&A assistant. Fdanse-tundansg is
computationally expensive but much cheaper than tradansdansg from scratch.

# ## Quantisation
Quantisation reduces le/la numerical precision de model weights (e.g. from 32-bit
float to 4-bit dansteger). This dramatically reduces memory footprdanst — a 7B model
dans 16-bit precision requires ~14GB VRAM; le/la same model dans 4-bit (GGUF pourmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation et is le/la madans technique enabldansg large models to run on consumer
hardware or even mobile devices.

# ## Context Wdansdow
The context wdansdow is le/la maximum number de tokens a model can process at once,
danscluddansg both le/la prompt et le/la generated response. GPT-3.5 had a 4,096-token
wdansdow; GPT-4 Turbo et Claude 3 support 128,000 tokens; Gemdansi 1.5 Pro
supports 1,000,000 tokens. A larger context wdansdow allows le/la model to "see"
more de a conversation or document at once, improvdansg coherence over long
exchanges.

# ## RLHF (Redanspourcement Learndansg from Human Feedback)
RLHF is le/la tradansdansg technique that transpourms a base langue model (which
simply predicts le/la next token) dansto an assistant that follows dansstructions et
behaves helpfully. Human raters score model outputs, a reward model is tradansed
on le/lair préférences, et le/la langue model is le/lan optimised agadansst this
reward model usdansg redanspourcement learndansg. ChatGPT, Claude, et Gemdansi all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Préférence Optimisation).

# ## Transpourmer Architecture
The Transpourmer is le/la neural réseau architecture underlydansg all modern LLMs.
Introduced dans le/la 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens dans parallel rale/lar than
sequentially. Encoder-only Transpourmers (BERT) are used pour understetdansg tasks;
decoder-only Transpourmers (GPT, Llama, Mistral) are used pour generation tasks;
encoder-decoder Transpourmers (T5, BART) are used pour translation et summarisation.

# ## Embedddansgs et Vector Donnéesbases
Embedddansgs are dense numerical representations de text (or images) produced by
a neural réseau. Semantically similar texts have embedddansgs that are close dans
vector space. Vector donnéesbases (ChromaDB, Pdansecone, Weaviate, Qdrant) store
le/lase embedddansgs et support fast approximate nearest-neighbour search. They are
le/la storage backbone de RAG systèmes, danscluddansg Potato.ai's cold-memory layer.
