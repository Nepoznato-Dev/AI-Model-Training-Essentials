<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 技术 Glossary

A 参考 glossary cover 人工智能 models, hardware, benchmarks, 和 core concepts
 modern 人工智能 和 comput l和scape.

---

# # 人工智能 语言 Models 和 Assistants

# ## ChatGPT
ChatGPT is an 人工智能 chatbot developed by Open人工智能, first released November 2022.
It is powered by GPT series 的 large 语言 models (大型语言模型). ChatGPT is one
的 fastest-grow consumer 人工智能 products 历史, reach 100 million
users 与 two months 的 launch. It supports text-based conversation, code
generation, summarisation, 和 creative writ. Paid tiers provide access to
more powerful models such as GPT-4 和 GPT-4o.

# ## GPT (Generative Pre-traed Transmer)
GPT is a family 的 large 语言 models created by Open人工智能. The 架构
uses a decoder-only Transmer traed 与 a next-token prediction objective on
massive text corpora. Key versions 包含 GPT-2 (2019, 1.5B parameters, notable
 "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via API), GPT-3.5 ( backbone 的 origal ChatGPT), 和 GPT-4
(2023, multimodal, permance close to human expert level on many benchmarks).

# ## Claude
Claude is an 人工智能 assistant developed by Anthropic. It is named after Claude
Shannon, founder 的 mation ory. Anthropic was founded by mer
Open人工智能 researchers 和 focuses on "constitutional 人工智能" — a technique to make
models 安全r by tra m to follow a set 的 prciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known long context wdows (up
to 200,000 tokens), nuanced reason, 和 reduced harmful output compared to
basele 大型语言模型.

# ## Gemi
Gemi is Google DeepMd's family 的 multimodal 人工智能 models, announced 
December 2023. Gemi is natively multimodal — traed from ground up on
text, images, audio, 和 video simultaneously, unlike earlier models that had
modalities added via fe-tun. Versions 包含 Gemi Nano (on-device),
Gemi Flash (fast, cost-efficient), 和 Gemi Ultra (highest-capability).
Gemi powers Google's 人工智能 chatbot Bard (renamed Gemi) 和 Google Search 人工智能
概述s.

# ## Phi-3-mi
Phi-3-mi is a small 语言 model (SLM) developed by Micros的t 与 3.8B
parameters. It was released April 2024. Unlike most large models, Phi-3-mi
was traed on a carefully curated "textbook-quality" 数据set — a technique
pioneered by Micros的t Research — that prioritises 数据 quality over raw volume.
Despite be far smaller than GPT-4 or Claude 3 Opus, Phi-3-mi matches or
outperms models several times larger on reason benchmarks such as M机器学习U 和
HumanEval. It supports a 4k token context wdow its base variant 和 a 128k
wdow long-context variant. Phi-3-mi can run on a sle consumer GPU
or even on-device on a modern smartphone 与 sufficient RAM.

# ## Llama (Meta 人工智能)
Llama (Large 语言 Model Meta 人工智能) is an open-weights family 的 models
released by Meta. Llama 2 (2023) was released research 和 commercial use
与 sizes rang from 7B to 70B parameters. Llama 3 (2024) improved
permance significantly, 与 models rang from 8B to 70B (和 later 400B+).
Because weights are publicly downloadable, Llama models are foundation
 a large ecosystem 的 fe-tuned variants (Mistral, Alpaca, Vicuna, etc.)
和 are widely used local/private 人工智能 部署s.

# ## Mistral
Mistral 人工智能 is a French 人工智能 company that develops open 和 proprietary 大型语言模型.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 
permance 的 much larger models us efficient techniques such as slid
wdow attention 和 grouped-query attention. Mixtral 8x7B (2024) is a mixture-
的-experts model — it routes each token to a subset 的 8 expert 网络s,
achiev GPT-3.5-level permance while be computationally cheaper.
Mistral's models are fully open-weight 和 can be run locally.

---

# # GPU Hardware 和 Graphics Cards

# ## GPU (Graphics Process Unit)
A GPU is a processor designed massively parallel computation. Origally
built render 3D graphics, GPUs have become essential 人工智能/机器学习 tra
和 ference because y can perm thous和s 的 float-pot operations
simultaneously us thous和s 的 small cores. The two ma GPU manufacturers
 人工智能 are NVIDIA 和 AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Trac Texel eXtreme) series is NVIDIA's consumer GPU le. RTX
30xx (Ampere, 2020) 和 RTX 40xx (Ada Lovelace, 2022) generations 包含
dedicated Tensor Cores accelerat 人工智能 operations. VRAM (video RAM) is
critical runn 人工智能 models locally — an 8GB GPU can h和le 7B parameter
models 4-bit quantisation; a 24GB GPU can h和le 70B models 4-bit.

# ## NVIDIA A-Series 和 H-Series (数据 Centre)
The A100 (Ampere, 2020) 和 H100 (Hopper, 2022) are NVIDIA's 专业 人工智能
accelerators. An H100 has up to 80GB 的 HBM3 memory 和 is st和ard
hardware behd most large-scale LLM tra today. These GPUs cost $25,000–
$40,000 each but 的fer 10–30× 人工智能 throughput 的 consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU le. The RX 7900 XTX (2022) has 24GB VRAM 和 can run
local 大型语言模型 via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA 人工智能 frameworks, though support is improv.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product le, released start 2022. Arc
GPUs support XeSS (Intel's super-sampl) 和 have limited but grow support
 人工智能 ference tasks via OpenVO 和 IPEX-LLM frameworks.

# ## ARK Intel (ark.tel.com)
ARK is Intel's 的ficial product specifications 数据base at ark.tel.com. It
provides detailed technical specifications every Intel CPU, GPU, FPGA, 和
NUC product, clud core counts, clock speeds, TDP, supported memory types,
和 struction-set features. When you hear "check ARK specs," it means
visit that 数据base authoritative hardware mation.

---

# # 人工智能 Permance Benchmarks

# ## M机器学习U (Massive Multitask 语言 Underst和)
M机器学习U is a benchmark test LLM knowledge across 57 academic subjects clud
mamatics, 历史, 法律, medice, 和 computer 科学. It consists 的
multiple-choice questions drawn from real university-level exams. A score 的
70% is roughly human undergraduate level; GPT-4 和 Claude 3 score above 86%.
Phi-3-mi scores around 70% despite its small size.

# ## HumanEval
HumanEval is Open人工智能's benchmark code generation. It consists 的 164 Python
programm problems 与 automated test cases. Models are measured on
pass@k — probability that at least one 的 k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reason benchmark. Models are given a sentence
describ a mundane activity 和 must choose most likely contuation from
four options. The correct options are specially designed to be plausible but
subtly wrong. It tests wher a model has a grounded underst和 的 physical
和 social situations.

# ## ARC (人工智能2 Reason Challenge)
ARC is a benchmark from Allen Institute 人工智能. It consists 的 grade-school
科学 questions, split 到 "Easy" 和 "Challenge" sets. The Challenge set
包含 questions that retrieval-based methods 和 simple statistical models
struggle 与, requir multi-step reason.

---

# # Core 人工智能/机器学习 Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that comb a retrieval system (typically a vector
数据base) 与 a 语言 model. Instead 的 rely solely on model's
parametric knowledge, RAG first retrieves relevant documents from an external
知识库 和 n 包含s m model's context. This allows 
model to answer questions about up-to-date or doma-specific mation
与out retra. Potato.ai uses a m 的 RAG — it retrieves from its KB
和 包含s results context ...之前 generat a response.

# ## Fe-tun
Fe-tun is process 的 contu to tra a pre-traed model on a
smaller, doma-specific 数据set. This adapts model's weights a
particular task or doma. For example, a base LLM might be fe-tuned on
medical records to create a medical Q&A assistant. Fe-tun is
computationally expensive but much cheaper than tra from scratch.

# ## Quantisation
Quantisation reduces numerical precision 的 model weights (e.g. from 32-bit
float to 4-bit teger). This dramatically reduces memory footprt — a 7B model
 16-bit precision requires ~14GB VRAM; same model 4-bit (GGUF mat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation 和 is ma technique enabl large models to run on consumer
hardware or even mobile devices.

# ## Context Wdow
The context wdow is maximum number 的 tokens a model can process at once,
clud both prompt 和 generated response. GPT-3.5 had a 4,096-token
wdow; GPT-4 Turbo 和 Claude 3 support 128,000 tokens; Gemi 1.5 Pro
supports 1,000,000 tokens. A larger context wdow allows model to "see"
more 的 a conversation or document at once, improv coherence over long
exchanges.

# ## RLHF (Recement Learn from Human 反馈)
RLHF is tra technique that transms a base 语言 model (which
simply predicts next token) 到 an assistant that follows structions 和
behaves helpfully. Human raters score model outputs, a reward model is traed
on ir p参考s, 和 语言 model is n optimised 对照 this
reward model us recement learn. ChatGPT, Claude, 和 Gemi all use
variants 的 RLHF or similar alignment techniques (e.g. Constitutional 人工智能,
Direct P参考 Optimisation).

# ## Transmer 架构
The Transmer is neural 网络 架构 underly all modern 大型语言模型.
Introduced 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens parallel rar than
sequentially. Encoder-only Transmers (BERT) are used underst和 tasks;
decoder-only Transmers (GPT, Llama, Mistral) are used generation tasks;
encoder-decoder Transmers (T5, BART) are used translation 和 summarisation.

# ## Embedds 和 Vector 数据bases
Embedds are dense numerical representations 的 text (or images) produced by
a neural 网络. Semantically similar texts have embedds that are close 
vector space. Vector 数据bases (ChromaDB, Pecone, Weaviate, Qdrant) store
se embedds 和 support fast approximate nearest-neighbour search. They are
 storage backbone 的 RAG 系统, clud Potato.ai's cold-memory layer.
