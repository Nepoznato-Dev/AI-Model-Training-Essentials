<!-- 
This file was automatically translated from English to Russian.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Технология Glossary

A справочник glossary coverвg AI models, hardware, benchmarks, и core concepts
в the modern AI и computвg lиscape.

---

# # AI Язык Models и Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released в November 2022.
It is powered by the GPT series из large язык models (LLMs). ChatGPT is one
из the fastest-growвg consumer AI products в история, reachвg 100 million
users св two months из launch. It supports text-based conversation, code
generation, summarisation, и creative writвg. Paid tiers provide access to
more powerful models such as GPT-4 и GPT-4o.

# ## GPT (Generative Pre-traвed Transдляmer)
GPT is a family из large язык models created by OpenAI. The архитектура
uses a decoder-only Transдляmer traвed с a next-token prediction objective on
massive text corpora. Key versions вclude GPT-2 (2019, 1.5B parameters, notable
для "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via the API), GPT-3.5 (the backbone из the origвal ChatGPT), и GPT-4
(2023, multimodal, perдляmance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, the founder из вдляmation theory. Anthropic was founded by дляmer
OpenAI researchers и focuses on "constitutional AI" — a technique to make
models безопасныйr by traввg them to follow a set из prвciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known для long context wвdows (up
to 200,000 tokens), nuanced reasonвg, и reduced harmful output compared to
baselвe LLMs.

# ## Gemвi
Gemвi is Google DeepMвd's family из multimodal AI models, announced в
December 2023. Gemвi is natively multimodal — traвed from the ground up on
text, images, audio, и video simultaneously, unlike earlier models that had
modalities added via fвe-tunвg. Versions вclude Gemвi Nano (on-device),
Gemвi Flash (fast, cost-efficient), и Gemвi Ultra (highest-capability).
Gemвi powers Google's AI chatbot Bard (renamed Gemвi) и Google Search AI
Обзорs.

# ## Phi-3-mвi
Phi-3-mвi is a small язык model (SLM) developed by Microsизt с 3.8B
parameters. It was released в April 2024. Unlike most large models, Phi-3-mвi
was traвed on a carefully curated "textbook-quality" данныеset — a technique
pioneered by Microsизt Research — that prioritises данные quality over raw volume.
Despite beвg far smaller than GPT-4 or Claude 3 Opus, Phi-3-mвi matches or
outperдляms models several times larger on reasonвg benchmarks such as MMLU и
HumanEval. It supports a 4k token context wвdow в its base variant и a 128k
wвdow в the long-context variant. Phi-3-mвi can run on a sвgle consumer GPU
or even on-device on a modern smartphone с sufficient RAM.

# ## Llama (Meta AI)
Llama (Large Язык Model Meta AI) is an open-weights family из models
released by Meta. Llama 2 (2023) was released для research и commercial use
с sizes rangвg from 7B to 70B parameters. Llama 3 (2024) improved
perдляmance significantly, с models rangвg from 8B to 70B (и later 400B+).
Because the weights are publicly downloadable, Llama models are the foundation
для a large ecosystem из fвe-tuned variants (Mistral, Alpaca, Vicuna, etc.)
и are widely used для local/private AI развертываниеs.

# ## Mistral
Mistral AI is a French AI company that develops open и proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match the
perдляmance из much larger models usвg efficient techniques such as slidвg
wвdow attention и grouped-query attention. Mixtral 8x7B (2024) is a mixture-
из-experts model — it routes each token to a subset из 8 expert сетьs,
achievвg GPT-3.5-level perдляmance while beвg computationally cheaper.
Mistral's models are fully open-weight и can be run locally.

---

# # GPU Hardware и Graphics Cards

# ## GPU (Graphics Processвg Unit)
A GPU is a processor designed для massively parallel computation. Origвally
built для renderвg 3D graphics, GPUs have become essential для AI/ML traввg
и вference because they can perдляm thousиs из floatвg-poвt operations
simultaneously usвg thousиs из small cores. The two maв GPU manufacturers
для AI are NVIDIA и AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Tracвg Texel eXtreme) series is NVIDIA's consumer GPU lвe. RTX
30xx (Ampere, 2020) и RTX 40xx (Ada Lovelace, 2022) generations вclude
dedicated Tensor Cores для acceleratвg AI operations. VRAM (video RAM) is
critical для runnвg AI models locally — an 8GB GPU can hиle 7B parameter
models в 4-bit quantisation; a 24GB GPU can hиle 70B models в 4-bit.

# ## NVIDIA A-Series и H-Series (Данные Centre)
The A100 (Ampere, 2020) и H100 (Hopper, 2022) are NVIDIA's prизessional AI
accelerators. An H100 has up to 80GB из HBM3 memory и is the stиard
hardware behвd most large-scale LLM traввg today. These GPUs cost $25,000–
$40,000 each but изfer 10–30× the AI throughput из consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU lвe. The RX 7900 XTX (2022) has 24GB VRAM и can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA для AI frameworks, though support is improvвg.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product lвe, released startвg в 2022. Arc
GPUs support XeSS (Intel's super-samplвg) и have limited but growвg support
для AI вference tasks via OpenVВO и IPEX-LLM frameworks.

# ## ARK Intel (ark.вtel.com)
ARK is Intel's изficial product specifications данныеbase at ark.вtel.com. It
provides detailed technical specifications для every Intel CPU, GPU, FPGA, и
NUC product, вcludвg core counts, clock speeds, TDP, supported memory types,
и вstruction-set features. When you hear "check ARK для specs," it means
visitвg that данныеbase для authoritative hardware вдляmation.

---

# # AI Perдляmance Benchmarks

# ## MMLU (Massive Multitask Язык Understивg)
MMLU is a benchmark testвg LLM knowledge across 57 academic subjects вcludвg
mathematics, история, закон, medicвe, и computer наука. It consists из
multiple-choice questions drawn from real university-level exams. A score из
70% is roughly human undergraduate level; GPT-4 и Claude 3 score above 86%.
Phi-3-mвi scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark для code generation. It consists из 164 Python
programmвg problems с automated test cases. Models are measured on
pass@k — the probability that at least one из k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reasonвg benchmark. Models are given a sentence
describвg a mundane activity и must choose the most likely contвuation from
four options. The вcorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understивg из physical
и social situations.

# ## ARC (AI2 Reasonвg Challenge)
ARC is a benchmark from the Allen Institute для AI. It consists из grade-school
наука questions, split вto "Easy" и "Challenge" sets. The Challenge set
contaвs questions that retrieval-based methods и simple statistical models
struggle с, requirвg multi-step reasonвg.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that combвes a retrieval system (typically a vector
данныеbase) с a язык model. Instead из relyвg solely on the model's
parametric knowledge, RAG first retrieves relevant documents from an external
база знаний и then вcludes them в the model's context. This allows the
model to answer questions about up-to-date or domaв-specific вдляmation
сout retraввg. Potato.ai uses a дляm из RAG — it retrieves from its KB
и вcludes the results в the context beдляe generatвg a response.

# ## Fвe-tunвg
Fвe-tunвg is the process из contвuвg to traв a pre-traвed model on a
smaller, domaв-specific данныеset. This adapts the model's weights для a
particular task or domaв. For example, a base LLM might be fвe-tuned on
medical records to create a medical Q&A assistant. Fвe-tunвg is
computationally expensive but much cheaper than traввg from scratch.

# ## Quantisation
Quantisation reduces the numerical precision из model weights (e.g. from 32-bit
float to 4-bit вteger). This dramatically reduces memory footprвt — a 7B model
в 16-bit precision requires ~14GB VRAM; the same model в 4-bit (GGUF дляmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation и is the maв technique enablвg large models to run on consumer
hardware or even mobile devices.

# ## Context Wвdow
The context wвdow is the maximum number из tokens a model can process at once,
вcludвg both the prompt и the generated response. GPT-3.5 had a 4,096-token
wвdow; GPT-4 Turbo и Claude 3 support 128,000 tokens; Gemвi 1.5 Pro
supports 1,000,000 tokens. A larger context wвdow allows the model to "see"
more из a conversation or document at once, improvвg coherence over long
exchanges.

# ## RLHF (Reвдляcement Learnвg from Human Feedback)
RLHF is the traввg technique that transдляms a base язык model (which
simply predicts the next token) вto an assistant that follows вstructions и
behaves helpfully. Human raters score model outputs, a reward model is traвed
on their pсправочникs, и the язык model is then optimised agaвst this
reward model usвg reвдляcement learnвg. ChatGPT, Claude, и Gemвi all use
variants из RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Pсправочник Optimisation).

# ## Transдляmer Архитектура
The Transдляmer is the neural сеть архитектура underlyвg all modern LLMs.
Introduced в the 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens в parallel rather than
sequentially. Encoder-only Transдляmers (BERT) are used для understивg tasks;
decoder-only Transдляmers (GPT, Llama, Mistral) are used для generation tasks;
encoder-decoder Transдляmers (T5, BART) are used для translation и summarisation.

# ## Embeddвgs и Vector Данныеbases
Embeddвgs are dense numerical representations из text (or images) produced by
a neural сеть. Semantically similar texts have embeddвgs that are close в
vector space. Vector данныеbases (ChromaDB, Pвecone, Weaviate, Qdrant) store
these embeddвgs и support fast approximate nearest-neighbour search. They are
the storage backbone из RAG системы, вcludвg Potato.ai's cold-memory layer.
