<!-- 
This file was automatically translated from English to Korean.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 Glossary

A 참조 glossary cover 인공 지능 models, hardware, benchmarks, core concepts
 modern 인공 지능 comput lscape.

---

# # 인공 지능 언어 Models Assistants

# ## ChatGPT
ChatGPT is an 인공 지능 chatbot developed by Open인공 지능, first released November 2022.
It is powered by GPT series large 언어 models (대규모 언어 모델). ChatGPT is one
 fastest-grow consumer 인공 지능 products 역사, reach 100 million
users 함께 two months launch. It supports text-based conversation, code
generation, summarisation, creative writ. Paid tiers provide access to
more powerful models such as GPT-4 GPT-4o.

# ## GPT (Generative Pre-traed Transmer)
GPT is a family large 언어 models created by Open인공 지능. The 아키텍처
uses a decoder-only Transmer traed 함께 a next-token prediction objective on
massive text corpora. Key versions 포함하다 GPT-2 (2019, 1.5B parameters, notable
 "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via API), GPT-3.5 ( backbone origal ChatGPT), GPT-4
(2023, multimodal, permance close to human expert level on many benchmarks).

# ## Claude
Claude is an 인공 지능 assistant developed by Anthropic. It is named after Claude
Shannon, founder mation ory. Anthropic was founded by mer
Open인공 지능 researchers focuses on "constitutional 인공 지능" — a technique to make
models 안전한r by tra m to follow a set prciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known long context wdows (up
to 200,000 tokens), nuanced reason, reduced harmful output compared to
basele 대규모 언어 모델.

# ## Gemi
Gemi is Google DeepMd's family multimodal 인공 지능 models, announced 
December 2023. Gemi is natively multimodal — traed from ground up on
text, images, audio, video simultaneously, unlike earlier models that had
modalities added via fe-tun. Versions 포함하다 Gemi Nano (on-device),
Gemi Flash (fast, cost-efficient), Gemi Ultra (highest-capability).
Gemi powers Google's 인공 지능 chatbot Bard (renamed Gemi) Google Search 인공 지능
개요s.

# ## Phi-3-mi
Phi-3-mi is a small 언어 model (SLM) developed by Microst 함께 3.8B
parameters. It was released April 2024. Unlike most large models, Phi-3-mi
was traed on a carefully curated "textbook-quality" 데이 터set — a technique
pioneered by Microst Research — that prioritises 데이 터 quality over raw volume.
Despite be far smaller than GPT-4 or Claude 3 Opus, Phi-3-mi matches or
outperms models several times larger on reason benchmarks such as M기계 학습U 
HumanEval. It supports a 4k token context wdow its base variant a 128k
wdow long-context variant. Phi-3-mi can run on a sle consumer GPU
or even on-device on a modern smartphone 함께 sufficient RAM.

# ## Llama (Meta 인공 지능)
Llama (Large 언어 Model Meta 인공 지능) is an open-weights family models
released by Meta. Llama 2 (2023) was released research commercial use
 함께 sizes rang from 7B to 70B parameters. Llama 3 (2024) improved
permance significantly, 함께 models rang from 8B to 70B ( later 400B+).
Because weights are publicly downloadable, Llama models are foundation
 a large ecosystem fe-tuned variants (Mistral, Alpaca, Vicuna, etc.)
 are widely used local/private 인공 지능 배포s.

# ## Mistral
Mistral 인공 지능 is a French 인공 지능 company that develops open proprietary 대규모 언어 모델.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 
permance much larger models us efficient techniques such as slid
wdow attention grouped-query attention. Mixtral 8x7B (2024) is a mixture-
-experts model — it routes each token to a subset 8 expert 네트워크s,
achiev GPT-3.5-level permance while be computationally cheaper.
Mistral's models are fully open-weight can be run locally.

---

# # GPU Hardware Graphics Cards

# ## GPU (Graphics Process Unit)
A GPU is a processor designed massively parallel computation. Origally
built render 3D graphics, GPUs have become essential 인공 지능/기계 학습 tra
 ference because y can perm thouss float-pot operations
simultaneously us thouss small cores. The two ma GPU manufacturers
 인공 지능 are NVIDIA AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Trac Texel eXtreme) series is NVIDIA's consumer GPU le. RTX
30xx (Ampere, 2020) RTX 40xx (Ada Lovelace, 2022) generations 포함하다
dedicated Tensor Cores accelerat 인공 지능 operations. VRAM (video RAM) is
critical runn 인공 지능 models locally — an 8GB GPU can hle 7B parameter
models 4-bit quantisation; a 24GB GPU can hle 70B models 4-bit.

# ## NVIDIA A-Series H-Series (데이 터 Centre)
The A100 (Ampere, 2020) H100 (Hopper, 2022) are NVIDIA's 전문적인 인공 지능
accelerators. An H100 has up to 80GB HBM3 memory is stard
hardware behd most large-scale LLM tra today. These GPUs cost $25,000–
$40,000 each but fer 10–30× 인공 지능 throughput consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU le. The RX 7900 XTX (2022) has 24GB VRAM can run
local 대규모 언어 모델 via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA 인공 지능 frameworks, though support is improv.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product le, released start 2022. Arc
GPUs support XeSS (Intel's super-sampl) have limited but grow support
 인공 지능 ference tasks via OpenVO IPEX-LLM frameworks.

# ## ARK Intel (ark.tel.com)
ARK is Intel's ficial product specifications 데이 터base at ark.tel.com. It
provides detailed technical specifications every Intel CPU, GPU, FPGA, 
NUC product, clud core counts, clock speeds, TDP, supported memory types,
 struction-set features. When you hear "check ARK specs," it means
visit that 데이 터base authoritative hardware mation.

---

# # 인공 지능 Permance Benchmarks

# ## M기계 학습U (Massive Multitask 언어 Underst)
M기계 학습U is a benchmark test LLM knowledge across 57 academic subjects clud
mamatics, 역사, 법률, medice, computer 과 학. It consists 
multiple-choice questions drawn from real university-level exams. A score 
70% is roughly human undergraduate level; GPT-4 Claude 3 score above 86%.
Phi-3-mi scores around 70% despite its small size.

# ## HumanEval
HumanEval is Open인공 지능's benchmark code generation. It consists 164 Python
programm problems 함께 automated test cases. Models are measured on
pass@k — probability that at least one k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reason benchmark. Models are given a sentence
describ a mundane activity must choose most likely contuation from
four options. The correct options are specially designed to be plausible but
subtly wrong. It tests wher a model has a grounded underst physical
 social situations.

# ## ARC (인공 지능2 Reason Challenge)
ARC is a benchmark from Allen Institute 인공 지능. It consists grade-school
과 학 questions, split 로 "Easy" "Challenge" sets. The Challenge set
포함하다 questions that retrieval-based methods simple statistical models
struggle 함께, requir multi-step reason.

---

# # Core 인공 지능/기계 학습 Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that comb a retrieval system (typically a vector
데이 터base) 함께 a 언어 model. Instead rely solely on model's
parametric knowledge, RAG first retrieves relevant documents from an external
지식 기반 n 포함하다s m model's context. This allows 
model to answer questions about up-to-date or doma-specific mation
 함께out retra. Potato.ai uses a m RAG — it retrieves from its KB
 포함하다s results context 전에 generat a response.

# ## Fe-tun
Fe-tun is process contu to tra a pre-traed model on a
smaller, doma-specific 데이 터set. This adapts model's weights a
particular task or doma. For example, a base LLM might be fe-tuned on
medical records to create a medical Q&A assistant. Fe-tun is
computationally expensive but much cheaper than tra from scratch.

# ## Quantisation
Quantisation reduces numerical precision model weights (e.g. from 32-bit
float to 4-bit teger). This dramatically reduces memory footprt — a 7B model
 16-bit precision requires ~14GB VRAM; same model 4-bit (GGUF mat)
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

# ## RLHF (Recement Learn from Human 피드백)
RLHF is tra technique that transms a base 언어 model (which
simply predicts next token) 로 an assistant that follows structions 
behaves helpfully. Human raters score model outputs, a reward model is traed
on ir p참조s, 언어 model is n optimised 대조 this
reward model us recement learn. ChatGPT, Claude, Gemi all use
variants RLHF or similar alignment techniques (e.g. Constitutional 인공 지능,
Direct P참조 Optimisation).

# ## Transmer 아키텍처
The Transmer is neural 네트워크 아키텍처 underly all modern 대규모 언어 모델.
Introduced 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens parallel rar than
sequentially. Encoder-only Transmers (BERT) are used underst tasks;
decoder-only Transmers (GPT, Llama, Mistral) are used generation tasks;
encoder-decoder Transmers (T5, BART) are used translation summarisation.

# ## Embedds Vector 데이 터bases
Embedds are dense numerical representations text (or images) produced by
a neural 네트워크. Semantically similar texts have embedds that are close 
vector space. Vector 데이 터bases (ChromaDB, Pecone, Weaviate, Qdrant) store
se embedds support fast approximate nearest-neighbour search. They are
 storage backbone RAG 시스템, clud Potato.ai's cold-memory layer.
