<!-- 
This file was automatically translated from English to Japanese.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# テクノロジー Glossary

A リファレンス glossary cover 人工知能 models, hardware, benchmarks, core concepts
 modern 人工知能 comput lscape.

---

# # 人工知能 言語 Models Assistants

# ## ChatGPT
ChatGPT is an 人工知能 chatbot developed by Open人工知能, first released November 2022.
It is powered by GPT series large 言語 models (大規模言語モデル). ChatGPT is one
 fastest-grow consumer 人工知能 products 歴史, reach 100 million
users two months launch. It supports text-based conversation, code
generation, summarisation, creative writ. Paid tiers provide access to
more powerful models such as GPT-4 GPT-4o.

# ## GPT (Generative Pre-traed Transにmer)
GPT is a family large 言語 models created by Open人工知能. The アーキテクチャ
uses a decoder-only Transにmer traed a next-token prediction objective on
massive text corpora. Key versions 含む GPT-2 (2019, 1.5B parameters, notable
に "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via API), GPT-3.5 ( backbone origal ChatGPT), GPT-4
(2023, multimodal, perにmance close to human expert level on many benchmarks).

# ## Claude
Claude is an 人工知能 assistant developed by Anthropic. It is named after Claude
Shannon, founder にmation ory. Anthropic was founded by にmer
Open人工知能 researchers focuses on "constitutional 人工知能" — a technique to make
models 安全なr by tra m to follow a set prciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known に long context wdows (up
to 200,000 tokens), nuanced reason, reduced harmful output compared to
basele 大規模言語モデル.

# ## Gemi
Gemi is Google DeepMd's family multimodal 人工知能 models, announced 
December 2023. Gemi is natively multimodal — traed from ground up on
text, images, audio, video simultaneously, unlike earlier models that had
modalities added via fe-tun. Versions 含む Gemi Nano (on-device),
Gemi Flash (fast, cost-efficient), Gemi Ultra (highest-capability).
Gemi powers Google's 人工知能 chatbot Bard (renamed Gemi) Google Search 人工知能
概要s.

# ## Phi-3-mi
Phi-3-mi is a small 言語 model (SLM) developed by Microst 3.8B
parameters. It was released April 2024. Unlike most large models, Phi-3-mi
was traed on a carefully curated "textbook-quality" データset — a technique
pioneered by Microst Research — that prioritises データ quality over raw volume.
Despite be far smaller than GPT-4 or Claude 3 Opus, Phi-3-mi matches or
outperにms models several times larger on reason benchmarks such as M機械学習U 
HumanEval. It supports a 4k token context wdow its base variant a 128k
wdow long-context variant. Phi-3-mi can run on a sle consumer GPU
or even on-device on a modern smartphone sufficient RAM.

# ## Llama (Meta 人工知能)
Llama (Large 言語 Model Meta 人工知能) is an open-weights family models
released by Meta. Llama 2 (2023) was released に research commercial use
 sizes rang from 7B to 70B parameters. Llama 3 (2024) improved
perにmance significantly, models rang from 8B to 70B ( later 400B+).
Because weights are publicly downloadable, Llama models are foundation
に a large ecosystem fe-tuned variants (Mistral, Alpaca, Vicuna, etc.)
 are widely used に local/private 人工知能 デプロイs.

# ## Mistral
Mistral 人工知能 is a French 人工知能 company that develops open proprietary 大規模言語モデル.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 
perにmance much larger models us efficient techniques such as slid
wdow attention grouped-query attention. Mixtral 8x7B (2024) is a mixture-
-experts model — it routes each token to a subset 8 expert ネットワークs,
achiev GPT-3.5-level perにmance while be computationally cheaper.
Mistral's models are fully open-weight can be run locally.

---

# # GPU Hardware Graphics Cards

# ## GPU (Graphics Process Unit)
A GPU is a processor designed に massively parallel computation. Origally
built に render 3D graphics, GPUs have become essential に 人工知能/機械学習 tra
 ference because y can perにm thouss float-pot operations
simultaneously us thouss small cores. The two ma GPU manufacturers
に 人工知能 are NVIDIA AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Trac Texel eXtreme) series is NVIDIA's consumer GPU le. RTX
30xx (Ampere, 2020) RTX 40xx (Ada Lovelace, 2022) generations 含む
dedicated Tensor Cores に accelerat 人工知能 operations. VRAM (video RAM) is
critical に runn 人工知能 models locally — an 8GB GPU can hle 7B parameter
models 4-bit quantisation; a 24GB GPU can hle 70B models 4-bit.

# ## NVIDIA A-Series H-Series (データ Centre)
The A100 (Ampere, 2020) H100 (Hopper, 2022) are NVIDIA's 専門的な 人工知能
accelerators. An H100 has up to 80GB HBM3 memory is stard
hardware behd most large-scale LLM tra today. These GPUs cost $25,000–
$40,000 each but fer 10–30× 人工知能 throughput consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU le. The RX 7900 XTX (2022) has 24GB VRAM can run
local 大規模言語モデル via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA に 人工知能 frameworks, though support is improv.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product le, released start 2022. Arc
GPUs support XeSS (Intel's super-sampl) have limited but grow support
に 人工知能 ference tasks via OpenVO IPEX-LLM frameworks.

# ## ARK Intel (ark.tel.com)
ARK is Intel's ficial product specifications データbase at ark.tel.com. It
provides detailed technical specifications に every Intel CPU, GPU, FPGA, 
NUC product, clud core counts, clock speeds, TDP, supported memory types,
 struction-set features. When you hear "check ARK に specs," it means
visit that データbase に authoritative hardware にmation.

---

# # 人工知能 Perにmance Benchmarks

# ## M機械学習U (Massive Multitask 言語 Underst)
M機械学習U is a benchmark test LLM knowledge across 57 academic subjects clud
mamatics, 歴史, 法律, medice, computer 科学. It consists 
multiple-choice questions drawn from real university-level exams. A score 
70% is roughly human undergraduate level; GPT-4 Claude 3 score above 86%.
Phi-3-mi scores around 70% despite its small size.

# ## HumanEval
HumanEval is Open人工知能's benchmark に code generation. It consists 164 Python
programm problems automated test cases. Models are measured on
pass@k — probability that at least one k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reason benchmark. Models are given a sentence
describ a mundane activity must choose most likely contuation from
four options. The correct options are specially designed to be plausible but
subtly wrong. It tests wher a model has a grounded underst physical
 social situations.

# ## ARC (人工知能2 Reason Challenge)
ARC is a benchmark from Allen Institute に 人工知能. It consists grade-school
科学 questions, split へ "Easy" "Challenge" sets. The Challenge set
含む questions that retrieval-based methods simple statistical models
struggle , requir multi-step reason.

---

# # Core 人工知能/機械学習 Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that comb a retrieval system (typically a vector
データbase) a 言語 model. Instead rely solely on model's
parametric knowledge, RAG first retrieves relevant documents from an external
ナレッジベース n 含むs m model's context. This allows 
model to answer questions about up-to-date or doma-specific にmation
out retra. Potato.ai uses a にm RAG — it retrieves from its KB
 含むs results context 前に generat a response.

# ## Fe-tun
Fe-tun is process contu to tra a pre-traed model on a
smaller, doma-specific データset. This adapts model's weights に a
particular task or doma. For example, a base LLM might be fe-tuned on
medical records to create a medical Q&A assistant. Fe-tun is
computationally expensive but much cheaper than tra from scratch.

# ## Quantisation
Quantisation reduces numerical precision model weights (e.g. from 32-bit
float to 4-bit teger). This dramatically reduces memory footprt — a 7B model
 16-bit precision requires ~14GB VRAM; same model 4-bit (GGUF にmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation is ma technique enabl large models to run on consumer
hardware or even mobile devices.

# ## Context Wdow
The context wdow is maximum number tokens a model can process at once,
clud both prompt generated response. GPT-3.5 had a 4,096-token
wdow; GPT-4 Turbo Claude 3 support 128,000 tokens; Gemi 1.5 Pro
supports 1,000,000 tokens. A larger context wdow allows model to "see"
more a conversation or document at once, improv coherence over long
exchanges.

# ## RLHF (Reにcement Learn from Human フィードバック)
RLHF is tra technique that transにms a base 言語 model (which
simply predicts next token) へ an assistant that follows structions 
behaves helpfully. Human raters score model outputs, a reward model is traed
on ir pリファレンスs, 言語 model is n optimised 対照 this
reward model us reにcement learn. ChatGPT, Claude, Gemi all use
variants RLHF or similar alignment techniques (e.g. Constitutional 人工知能,
Direct Pリファレンス Optimisation).

# ## Transにmer アーキテクチャ
The Transにmer is neural ネットワーク アーキテクチャ underly all modern 大規模言語モデル.
Introduced 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens parallel rar than
sequentially. Encoder-only Transにmers (BERT) are used に underst tasks;
decoder-only Transにmers (GPT, Llama, Mistral) are used に generation tasks;
encoder-decoder Transにmers (T5, BART) are used に translation summarisation.

# ## Embedds Vector データbases
Embedds are dense numerical representations text (or images) produced by
a neural ネットワーク. Semantically similar texts have embedds that are close 
vector space. Vector データbases (ChromaDB, Pecone, Weaviate, Qdrant) store
se embedds support fast approximate nearest-neighbour search. They are
 storage backbone RAG システム, clud Potato.ai's cold-memory layer.
