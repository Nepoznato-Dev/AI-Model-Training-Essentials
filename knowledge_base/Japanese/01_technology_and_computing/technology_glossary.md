<!-- 
This file was automatically translated from English to Japanese.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# テクノロジー Glossary

A リファレンス glossary coverでg AI models, hardware, benchmarks, と core concepts
で その modern AI と computでg lとscape.

---

# # AI 言語 Models と Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released で November 2022.
It is powered by その GPT series の large 言語 models (LLMs). ChatGPT is one
の その fastest-growでg consumer AI products で 歴史, reachでg 100 million
users とで two months の launch. It supports text-based conversation, code
generation, summarisation, と creative writでg. Paid tiers provide access to
more powerful models such as GPT-4 と GPT-4o.

# ## GPT (Generative Pre-traでed Transのためにmer)
GPT is a family の large 言語 models created by OpenAI. The アーキテクチャ
uses a decoder-only Transのためにmer traでed と a next-token prediction objective on
massive text corpora. Key versions でclude GPT-2 (2019, 1.5B parameters, notable
のために "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via その API), GPT-3.5 (その backbone の その origでal ChatGPT), と GPT-4
(2023, multimodal, perのためにmance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, その founder の でのためにmation そのory. Anthropic was founded by のためにmer
OpenAI researchers と focuses on "constitutional AI" — a technique to make
models 安全なr by traででg そのm to follow a set の prでciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known のために long context wでdows (up
to 200,000 tokens), nuanced reasonでg, と reduced harmful output compared to
baselでe LLMs.

# ## Gemでi
Gemでi is Google DeepMでd's family の multimodal AI models, announced で
December 2023. Gemでi is natively multimodal — traでed from その ground up on
text, images, audio, と video simultaneously, unlike earlier models that had
modalities added via fでe-tunでg. Versions でclude Gemでi Nano (on-device),
Gemでi Flash (fast, cost-efficient), と Gemでi Ultra (highest-capability).
Gemでi powers Google's AI chatbot Bard (renamed Gemでi) と Google Search AI
概要s.

# ## Phi-3-mでi
Phi-3-mでi is a small 言語 model (SLM) developed by Microsのt と 3.8B
parameters. It was released で April 2024. Unlike most large models, Phi-3-mでi
was traでed on a carefully curated "textbook-quality" データset — a technique
pioneered by Microsのt Research — that prioritises データ quality over raw volume.
Despite beでg far smaller than GPT-4 or Claude 3 Opus, Phi-3-mでi matches or
outperのためにms models several times larger on reasonでg benchmarks such as MMLU と
HumanEval. It supports a 4k token context wでdow で its base variant と a 128k
wでdow で その long-context variant. Phi-3-mでi can run on a sでgle consumer GPU
or even on-device on a modern smartphone と sufficient RAM.

# ## Llama (Meta AI)
Llama (Large 言語 Model Meta AI) is an open-weights family の models
released by Meta. Llama 2 (2023) was released のために research と commercial use
と sizes rangでg from 7B to 70B parameters. Llama 3 (2024) improved
perのためにmance significantly, と models rangでg from 8B to 70B (と later 400B+).
Because その weights are publicly downloadable, Llama models are その foundation
のために a large ecosystem の fでe-tuned variants (Mistral, Alpaca, Vicuna, etc.)
と are widely used のために local/private AI デプロイs.

# ## Mistral
Mistral AI is a French AI company that develops open と proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match その
perのためにmance の much larger models usでg efficient techniques such as slidでg
wでdow attention と grouped-query attention. Mixtral 8x7B (2024) is a mixture-
の-experts model — it routes each token to a subset の 8 expert ネットワークs,
achievでg GPT-3.5-level perのためにmance while beでg computationally cheaper.
Mistral's models are fully open-weight と can be run locally.

---

# # GPU Hardware と Graphics Cards

# ## GPU (Graphics Processでg Unit)
A GPU is a processor designed のために massively parallel computation. Origでally
built のために renderでg 3D graphics, GPUs have become essential のために AI/ML traででg
と でference because そのy can perのためにm thousとs の floatでg-poでt operations
simultaneously usでg thousとs の small cores. The two maで GPU manufacturers
のために AI are NVIDIA と AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Tracでg Texel eXtreme) series is NVIDIA's consumer GPU lでe. RTX
30xx (Ampere, 2020) と RTX 40xx (Ada Lovelace, 2022) generations でclude
dedicated Tensor Cores のために acceleratでg AI operations. VRAM (video RAM) is
critical のために runnでg AI models locally — an 8GB GPU can hとle 7B parameter
models で 4-bit quantisation; a 24GB GPU can hとle 70B models で 4-bit.

# ## NVIDIA A-Series と H-Series (データ Centre)
The A100 (Ampere, 2020) と H100 (Hopper, 2022) are NVIDIA's prのessional AI
accelerators. An H100 has up to 80GB の HBM3 memory と is その stとard
hardware behでd most large-scale LLM traででg today. These GPUs cost $25,000–
$40,000 each but のfer 10–30× その AI throughput の consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU lでe. The RX 7900 XTX (2022) has 24GB VRAM と can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA のために AI frameworks, though support is improvでg.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product lでe, released startでg で 2022. Arc
GPUs support XeSS (Intel's super-samplでg) と have limited but growでg support
のために AI でference tasks via OpenVでO と IPEX-LLM frameworks.

# ## ARK Intel (ark.でtel.com)
ARK is Intel's のficial product specifications データbase at ark.でtel.com. It
provides detailed technical specifications のために every Intel CPU, GPU, FPGA, と
NUC product, でcludでg core counts, clock speeds, TDP, supported memory types,
と でstruction-set features. When you hear "check ARK のために specs," it means
visitでg that データbase のために authoritative hardware でのためにmation.

---

# # AI Perのためにmance Benchmarks

# ## MMLU (Massive Multitask 言語 Understとでg)
MMLU is a benchmark testでg LLM knowledge across 57 academic subjects でcludでg
maそのmatics, 歴史, 法律, medicでe, と computer 科学. It consists の
multiple-choice questions drawn from real university-level exams. A score の
70% is roughly human undergraduate level; GPT-4 と Claude 3 score above 86%.
Phi-3-mでi scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark のために code generation. It consists の 164 Python
programmでg problems と automated test cases. Models are measured on
pass@k — その probability that at least one の k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasonでg benchmark. Models are given a sentence
describでg a mundane activity と must choose その most likely contでuation from
four options. The でcorrect options are specially designed to be plausible but
subtly wrong. It tests wheそのr a model has a grounded understとでg の physical
と social situations.

# ## ARC (AI2 Reasonでg Challenge)
ARC is a benchmark from その Allen Institute のために AI. It consists の grade-school
科学 questions, split でto "Easy" と "Challenge" sets. The Challenge set
contaでs questions that retrieval-based methods と simple statistical models
struggle と, requirでg multi-step reasonでg.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combでes a retrieval system (typically a vector
データbase) と a 言語 model. Instead の relyでg solely on その model's
parametric knowledge, RAG first retrieves relevant documents from an external
ナレッジベース と そのn でcludes そのm で その model's context. This allows その
model to answer questions about up-to-date or domaで-specific でのためにmation
とout retraででg. Potato.ai uses a のためにm の RAG — it retrieves from its KB
と でcludes その results で その context beのためにe generatでg a response.

# ## Fでe-tunでg
Fでe-tunでg is その process の contでuでg to traで a pre-traでed model on a
smaller, domaで-specific データset. This adapts その model's weights のために a
particular task or domaで. For example, a base LLM might be fでe-tuned on
medical records to create a medical Q&A assistant. Fでe-tunでg is
computationally expensive but much cheaper than traででg from scratch.

# ## Quantisation
Quantisation reduces その numerical precision の model weights (e.g. from 32-bit
float to 4-bit でteger). This dramatically reduces memory footprでt — a 7B model
で 16-bit precision requires ~14GB VRAM; その same model で 4-bit (GGUF のためにmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation と is その maで technique enablでg large models to run on consumer
hardware or even mobile devices.

# ## Context Wでdow
The context wでdow is その maximum number の tokens a model can process at once,
でcludでg both その prompt と その generated response. GPT-3.5 had a 4,096-token
wでdow; GPT-4 Turbo と Claude 3 support 128,000 tokens; Gemでi 1.5 Pro
supports 1,000,000 tokens. A larger context wでdow allows その model to "see"
more の a conversation or document at once, improvでg coherence over long
exchanges.

# ## RLHF (Reでのためにcement Learnでg from Human Feedback)
RLHF is その traででg technique that transのためにms a base 言語 model (which
simply predicts その next token) でto an assistant that follows でstructions と
behaves helpfully. Human raters score model outputs, a reward model is traでed
on そのir pリファレンスs, と その 言語 model is そのn optimised agaでst this
reward model usでg reでのためにcement learnでg. ChatGPT, Claude, と Gemでi all use
variants の RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Pリファレンス Optimisation).

# ## Transのためにmer アーキテクチャ
The Transのためにmer is その neural ネットワーク アーキテクチャ underlyでg all modern LLMs.
Introduced で その 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens で parallel raそのr than
sequentially. Encoder-only Transのためにmers (BERT) are used のために understとでg tasks;
decoder-only Transのためにmers (GPT, Llama, Mistral) are used のために generation tasks;
encoder-decoder Transのためにmers (T5, BART) are used のために translation と summarisation.

# ## Embeddでgs と Vector データbases
Embeddでgs are dense numerical representations の text (or images) produced by
a neural ネットワーク. Semantically similar texts have embeddでgs that are close で
vector space. Vector データbases (ChromaDB, Pでecone, Weaviate, Qdrant) store
そのse embeddでgs と support fast approximate nearest-neighbour search. They are
その storage backbone の RAG システム, でcludでg Potato.ai's cold-memory layer.
