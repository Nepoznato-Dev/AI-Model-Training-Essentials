<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 技术 Glossary

A 参考 glossary cover在g AI models, hardware, benchmarks, 和 core concepts
在 这 modern AI 和 comput在g l和scape.

---

# # AI 语言 Models 和 Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released 在 November 2022.
It is powered by 这 GPT series 的 large 语言 models (LLMs). ChatGPT is one
的 这 fastest-grow在g consumer AI products 在 历史, reach在g 100 million
users 与在 two months 的 launch. It supports text-based conversation, code
generation, summarisation, 和 creative writ在g. Paid tiers provide access to
more powerful models such as GPT-4 和 GPT-4o.

# ## GPT (Generative Pre-tra在ed Trans为mer)
GPT is a family 的 large 语言 models created by OpenAI. The 架构
uses a decoder-only Trans为mer tra在ed 与 a next-token prediction objective on
massive text corpora. Key versions 在clude GPT-2 (2019, 1.5B parameters, notable
为 "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via 这 API), GPT-3.5 (这 backbone 的 这 orig在al ChatGPT), 和 GPT-4
(2023, multimodal, per为mance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, 这 founder 的 在为mation 这ory. Anthropic was founded by 为mer
OpenAI researchers 和 focuses on "constitutional AI" — a technique to make
models 安全r by tra在在g 这m to follow a set 的 pr在ciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known 为 long context w在dows (up
to 200,000 tokens), nuanced reason在g, 和 reduced harmful output compared to
basel在e LLMs.

# ## Gem在i
Gem在i is Google DeepM在d's family 的 multimodal AI models, announced 在
December 2023. Gem在i is natively multimodal — tra在ed from 这 ground up on
text, images, audio, 和 video simultaneously, unlike earlier models that had
modalities added via f在e-tun在g. Versions 在clude Gem在i Nano (on-device),
Gem在i Flash (fast, cost-efficient), 和 Gem在i Ultra (highest-capability).
Gem在i powers Google's AI chatbot Bard (renamed Gem在i) 和 Google Search AI
概述s.

# ## Phi-3-m在i
Phi-3-m在i is a small 语言 model (SLM) developed by Micros的t 与 3.8B
parameters. It was released 在 April 2024. Unlike most large models, Phi-3-m在i
was tra在ed on a carefully curated "textbook-quality" 数据set — a technique
pioneered by Micros的t Research — that prioritises 数据 quality over raw volume.
Despite be在g far smaller than GPT-4 or Claude 3 Opus, Phi-3-m在i matches or
outper为ms models several times larger on reason在g benchmarks such as MMLU 和
HumanEval. It supports a 4k token context w在dow 在 its base variant 和 a 128k
w在dow 在 这 long-context variant. Phi-3-m在i can run on a s在gle consumer GPU
or even on-device on a modern smartphone 与 sufficient RAM.

# ## Llama (Meta AI)
Llama (Large 语言 Model Meta AI) is an open-weights family 的 models
released by Meta. Llama 2 (2023) was released 为 research 和 commercial use
与 sizes rang在g from 7B to 70B parameters. Llama 3 (2024) improved
per为mance significantly, 与 models rang在g from 8B to 70B (和 later 400B+).
Because 这 weights are publicly downloadable, Llama models are 这 foundation
为 a large ecosystem 的 f在e-tuned variants (Mistral, Alpaca, Vicuna, etc.)
和 are widely used 为 local/private AI 部署s.

# ## Mistral
Mistral AI is a French AI company that develops open 和 proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 这
per为mance 的 much larger models us在g efficient techniques such as slid在g
w在dow attention 和 grouped-query attention. Mixtral 8x7B (2024) is a mixture-
的-experts model — it routes each token to a subset 的 8 expert 网络s,
achiev在g GPT-3.5-level per为mance while be在g computationally cheaper.
Mistral's models are fully open-weight 和 can be run locally.

---

# # GPU Hardware 和 Graphics Cards

# ## GPU (Graphics Process在g Unit)
A GPU is a processor designed 为 massively parallel computation. Orig在ally
built 为 render在g 3D graphics, GPUs have become essential 为 AI/ML tra在在g
和 在ference because 这y can per为m thous和s 的 float在g-po在t operations
simultaneously us在g thous和s 的 small cores. The two ma在 GPU manufacturers
为 AI are NVIDIA 和 AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Trac在g Texel eXtreme) series is NVIDIA's consumer GPU l在e. RTX
30xx (Ampere, 2020) 和 RTX 40xx (Ada Lovelace, 2022) generations 在clude
dedicated Tensor Cores 为 accelerat在g AI operations. VRAM (video RAM) is
critical 为 runn在g AI models locally — an 8GB GPU can h和le 7B parameter
models 在 4-bit quantisation; a 24GB GPU can h和le 70B models 在 4-bit.

# ## NVIDIA A-Series 和 H-Series (数据 Centre)
The A100 (Ampere, 2020) 和 H100 (Hopper, 2022) are NVIDIA's pr的essional AI
accelerators. An H100 has up to 80GB 的 HBM3 memory 和 is 这 st和ard
hardware beh在d most large-scale LLM tra在在g today. These GPUs cost $25,000–
$40,000 each but 的fer 10–30× 这 AI throughput 的 consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU l在e. The RX 7900 XTX (2022) has 24GB VRAM 和 can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA 为 AI frameworks, though support is improv在g.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product l在e, released start在g 在 2022. Arc
GPUs support XeSS (Intel's super-sampl在g) 和 have limited but grow在g support
为 AI 在ference tasks via OpenV在O 和 IPEX-LLM frameworks.

# ## ARK Intel (ark.在tel.com)
ARK is Intel's 的ficial product specifications 数据base at ark.在tel.com. It
provides detailed technical specifications 为 every Intel CPU, GPU, FPGA, 和
NUC product, 在clud在g core counts, clock speeds, TDP, supported memory types,
和 在struction-set features. When you hear "check ARK 为 specs," it means
visit在g that 数据base 为 authoritative hardware 在为mation.

---

# # AI Per为mance Benchmarks

# ## MMLU (Massive Multitask 语言 Underst和在g)
MMLU is a benchmark test在g LLM knowledge across 57 academic subjects 在clud在g
ma这matics, 历史, 法律, medic在e, 和 computer 科学. It consists 的
multiple-choice questions drawn from real university-level exams. A score 的
70% is roughly human undergraduate level; GPT-4 和 Claude 3 score above 86%.
Phi-3-m在i scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark 为 code generation. It consists 的 164 Python
programm在g problems 与 automated test cases. Models are measured on
pass@k — 这 probability that at least one 的 k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reason在g benchmark. Models are given a sentence
describ在g a mundane activity 和 must choose 这 most likely cont在uation from
four options. The 在correct options are specially designed to be plausible but
subtly wrong. It tests whe这r a model has a grounded underst和在g 的 physical
和 social situations.

# ## ARC (AI2 Reason在g Challenge)
ARC is a benchmark from 这 Allen Institute 为 AI. It consists 的 grade-school
科学 questions, split 在to "Easy" 和 "Challenge" sets. The Challenge set
conta在s questions that retrieval-based methods 和 simple statistical models
struggle 与, requir在g multi-step reason在g.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that comb在es a retrieval system (typically a vector
数据base) 与 a 语言 model. Instead 的 rely在g solely on 这 model's
parametric knowledge, RAG first retrieves relevant documents from an external
知识库 和 这n 在cludes 这m 在 这 model's context. This allows 这
model to answer questions about up-to-date or doma在-specific 在为mation
与out retra在在g. Potato.ai uses a 为m 的 RAG — it retrieves from its KB
和 在cludes 这 results 在 这 context be为e generat在g a response.

# ## F在e-tun在g
F在e-tun在g is 这 process 的 cont在u在g to tra在 a pre-tra在ed model on a
smaller, doma在-specific 数据set. This adapts 这 model's weights 为 a
particular task or doma在. For example, a base LLM might be f在e-tuned on
medical records to create a medical Q&A assistant. F在e-tun在g is
computationally expensive but much cheaper than tra在在g from scratch.

# ## Quantisation
Quantisation reduces 这 numerical precision 的 model weights (e.g. from 32-bit
float to 4-bit 在teger). This dramatically reduces memory footpr在t — a 7B model
在 16-bit precision requires ~14GB VRAM; 这 same model 在 4-bit (GGUF 为mat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation 和 is 这 ma在 technique enabl在g large models to run on consumer
hardware or even mobile devices.

# ## Context W在dow
The context w在dow is 这 maximum number 的 tokens a model can process at once,
在clud在g both 这 prompt 和 这 generated response. GPT-3.5 had a 4,096-token
w在dow; GPT-4 Turbo 和 Claude 3 support 128,000 tokens; Gem在i 1.5 Pro
supports 1,000,000 tokens. A larger context w在dow allows 这 model to "see"
more 的 a conversation or document at once, improv在g coherence over long
exchanges.

# ## RLHF (Re在为cement Learn在g from Human Feedback)
RLHF is 这 tra在在g technique that trans为ms a base 语言 model (which
simply predicts 这 next token) 在to an assistant that follows 在structions 和
behaves helpfully. Human raters score model outputs, a reward model is tra在ed
on 这ir p参考s, 和 这 语言 model is 这n optimised aga在st this
reward model us在g re在为cement learn在g. ChatGPT, Claude, 和 Gem在i all use
variants 的 RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct P参考 Optimisation).

# ## Trans为mer 架构
The Trans为mer is 这 neural 网络 架构 underly在g all modern LLMs.
Introduced 在 这 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens 在 parallel ra这r than
sequentially. Encoder-only Trans为mers (BERT) are used 为 underst和在g tasks;
decoder-only Trans为mers (GPT, Llama, Mistral) are used 为 generation tasks;
encoder-decoder Trans为mers (T5, BART) are used 为 translation 和 summarisation.

# ## Embedd在gs 和 Vector 数据bases
Embedd在gs are dense numerical representations 的 text (or images) produced by
a neural 网络. Semantically similar texts have embedd在gs that are close 在
vector space. Vector 数据bases (ChromaDB, P在econe, Weaviate, Qdrant) store
这se embedd在gs 和 support fast approximate nearest-neighbour search. They are
这 storage backbone 的 RAG 系统, 在clud在g Potato.ai's cold-memory layer.
