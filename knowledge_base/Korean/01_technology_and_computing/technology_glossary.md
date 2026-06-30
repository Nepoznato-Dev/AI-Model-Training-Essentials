<!-- 
This file was automatically translated from English to Korean.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 Glossary

A 참조 glossary cover에서g AI models, hardware, benchmarks, 와 core concepts
에서 그 modern AI 와 comput에서g l와scape.

---

# # AI 언어 Models 와 Assistants

# ## ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released 에서 November 2022.
It is powered by 그 GPT series 의 large 언어 models (LLMs). ChatGPT is one
의 그 fastest-grow에서g consumer AI products 에서 역사, reach에서g 100 million
users 와 함께에서 two months 의 launch. It supports text-based conversation, code
generation, summarisation, 와 creative writ에서g. Paid tiers provide access to
more powerful models such as GPT-4 와 GPT-4o.

# ## GPT (Generative Pre-tra에서ed Trans위한mer)
GPT is a family 의 large 언어 models created by OpenAI. The 아키텍처
uses a decoder-only Trans위한mer tra에서ed 와 함께 a next-token prediction objective on
massive text corpora. Key versions 에서clude GPT-2 (2019, 1.5B parameters, notable
위한 "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via 그 API), GPT-3.5 (그 backbone 의 그 orig에서al ChatGPT), 와 GPT-4
(2023, multimodal, per위한mance close to human expert level on many benchmarks).

# ## Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, 그 founder 의 에서위한mation 그ory. Anthropic was founded by 위한mer
OpenAI researchers 와 focuses on "constitutional AI" — a technique to make
models 안전한r by tra에서에서g 그m to follow a set 의 pr에서ciples. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known 위한 long context w에서dows (up
to 200,000 tokens), nuanced reason에서g, 와 reduced harmful output compared to
basel에서e LLMs.

# ## Gem에서i
Gem에서i is Google DeepM에서d's family 의 multimodal AI models, announced 에서
December 2023. Gem에서i is natively multimodal — tra에서ed from 그 ground up on
text, images, audio, 와 video simultaneously, unlike earlier models that had
modalities added via f에서e-tun에서g. Versions 에서clude Gem에서i Nano (on-device),
Gem에서i Flash (fast, cost-efficient), 와 Gem에서i Ultra (highest-capability).
Gem에서i powers Google's AI chatbot Bard (renamed Gem에서i) 와 Google Search AI
개요s.

# ## Phi-3-m에서i
Phi-3-m에서i is a small 언어 model (SLM) developed by Micros의t 와 함께 3.8B
parameters. It was released 에서 April 2024. Unlike most large models, Phi-3-m에서i
was tra에서ed on a carefully curated "textbook-quality" 데이터set — a technique
pioneered by Micros의t Research — that prioritises 데이터 quality over raw volume.
Despite be에서g far smaller than GPT-4 or Claude 3 Opus, Phi-3-m에서i matches or
outper위한ms models several times larger on reason에서g benchmarks such as MMLU 와
HumanEval. It supports a 4k token context w에서dow 에서 its base variant 와 a 128k
w에서dow 에서 그 long-context variant. Phi-3-m에서i can run on a s에서gle consumer GPU
or even on-device on a modern smartphone 와 함께 sufficient RAM.

# ## Llama (Meta AI)
Llama (Large 언어 Model Meta AI) is an open-weights family 의 models
released by Meta. Llama 2 (2023) was released 위한 research 와 commercial use
와 함께 sizes rang에서g from 7B to 70B parameters. Llama 3 (2024) improved
per위한mance significantly, 와 함께 models rang에서g from 8B to 70B (와 later 400B+).
Because 그 weights are publicly downloadable, Llama models are 그 foundation
위한 a large ecosystem 의 f에서e-tuned variants (Mistral, Alpaca, Vicuna, etc.)
와 are widely used 위한 local/private AI 배포s.

# ## Mistral
Mistral AI is a French AI company that develops open 와 proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match 그
per위한mance 의 much larger models us에서g efficient techniques such as slid에서g
w에서dow attention 와 grouped-query attention. Mixtral 8x7B (2024) is a mixture-
의-experts model — it routes each token to a subset 의 8 expert 네트워크s,
achiev에서g GPT-3.5-level per위한mance while be에서g computationally cheaper.
Mistral's models are fully open-weight 와 can be run locally.

---

# # GPU Hardware 와 Graphics Cards

# ## GPU (Graphics Process에서g Unit)
A GPU is a processor designed 위한 massively parallel computation. Orig에서ally
built 위한 render에서g 3D graphics, GPUs have become essential 위한 AI/ML tra에서에서g
와 에서ference because 그y can per위한m thous와s 의 float에서g-po에서t operations
simultaneously us에서g thous와s 의 small cores. The two ma에서 GPU manufacturers
위한 AI are NVIDIA 와 AMD.

# ## NVIDIA GeForce RTX Series
The RTX (Ray Trac에서g Texel eXtreme) series is NVIDIA's consumer GPU l에서e. RTX
30xx (Ampere, 2020) 와 RTX 40xx (Ada Lovelace, 2022) generations 에서clude
dedicated Tensor Cores 위한 accelerat에서g AI operations. VRAM (video RAM) is
critical 위한 runn에서g AI models locally — an 8GB GPU can h와le 7B parameter
models 에서 4-bit quantisation; a 24GB GPU can h와le 70B models 에서 4-bit.

# ## NVIDIA A-Series 와 H-Series (데이터 Centre)
The A100 (Ampere, 2020) 와 H100 (Hopper, 2022) are NVIDIA's pr의essional AI
accelerators. An H100 has up to 80GB 의 HBM3 memory 와 is 그 st와ard
hardware beh에서d most large-scale LLM tra에서에서g today. These GPUs cost $25,000–
$40,000 each but 의fer 10–30× 그 AI throughput 의 consumer RTX cards.

# ## AMD Radeon RX Series
AMD's consumer GPU l에서e. The RX 7900 XTX (2022) has 24GB VRAM 와 can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA 위한 AI frameworks, though support is improv에서g.

# ## Intel Arc
Intel Arc is Intel's discrete GPU product l에서e, released start에서g 에서 2022. Arc
GPUs support XeSS (Intel's super-sampl에서g) 와 have limited but grow에서g support
위한 AI 에서ference tasks via OpenV에서O 와 IPEX-LLM frameworks.

# ## ARK Intel (ark.에서tel.com)
ARK is Intel's 의ficial product specifications 데이터base at ark.에서tel.com. It
provides detailed technical specifications 위한 every Intel CPU, GPU, FPGA, 와
NUC product, 에서clud에서g core counts, clock speeds, TDP, supported memory types,
와 에서struction-set features. When you hear "check ARK 위한 specs," it means
visit에서g that 데이터base 위한 authoritative hardware 에서위한mation.

---

# # AI Per위한mance Benchmarks

# ## MMLU (Massive Multitask 언어 Underst와에서g)
MMLU is a benchmark test에서g LLM knowledge across 57 academic subjects 에서clud에서g
ma그matics, 역사, 법률, medic에서e, 와 computer 과학. It consists 의
multiple-choice questions drawn from real university-level exams. A score 의
70% is roughly human undergraduate level; GPT-4 와 Claude 3 score above 86%.
Phi-3-m에서i scores around 70% despite its small size.

# ## HumanEval
HumanEval is OpenAI's benchmark 위한 code generation. It consists 의 164 Python
programm에서g problems 와 함께 automated test cases. Models are measured on
pass@k — 그 probability that at least one 의 k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

# ## HellaSwag
HellaSwag is a commonsense reason에서g benchmark. Models are given a sentence
describ에서g a mundane activity 와 must choose 그 most likely cont에서uation from
four options. The 에서correct options are specially designed to be plausible but
subtly wrong. It tests whe그r a model has a grounded underst와에서g 의 physical
와 social situations.

# ## ARC (AI2 Reason에서g Challenge)
ARC is a benchmark from 그 Allen Institute 위한 AI. It consists 의 grade-school
과학 questions, split 에서to "Easy" 와 "Challenge" sets. The Challenge set
conta에서s questions that retrieval-based methods 와 simple statistical models
struggle 와 함께, requir에서g multi-step reason에서g.

---

# # Core AI/ML Concepts

# ## RAG (Retrieval-Augmented Generation)
RAG is a technique that comb에서es a retrieval system (typically a vector
데이터base) 와 함께 a 언어 model. Instead 의 rely에서g solely on 그 model's
parametric knowledge, RAG first retrieves relevant documents from an external
지식 기반 와 그n 에서cludes 그m 에서 그 model's context. This allows 그
model to answer questions about up-to-date or doma에서-specific 에서위한mation
와 함께out retra에서에서g. Potato.ai uses a 위한m 의 RAG — it retrieves from its KB
와 에서cludes 그 results 에서 그 context be위한e generat에서g a response.

# ## F에서e-tun에서g
F에서e-tun에서g is 그 process 의 cont에서u에서g to tra에서 a pre-tra에서ed model on a
smaller, doma에서-specific 데이터set. This adapts 그 model's weights 위한 a
particular task or doma에서. For example, a base LLM might be f에서e-tuned on
medical records to create a medical Q&A assistant. F에서e-tun에서g is
computationally expensive but much cheaper than tra에서에서g from scratch.

# ## Quantisation
Quantisation reduces 그 numerical precision 의 model weights (e.g. from 32-bit
float to 4-bit 에서teger). This dramatically reduces memory footpr에서t — a 7B model
에서 16-bit precision requires ~14GB VRAM; 그 same model 에서 4-bit (GGUF 위한mat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation 와 is 그 ma에서 technique enabl에서g large models to run on consumer
hardware or even mobile devices.

# ## Context W에서dow
The context w에서dow is 그 maximum number 의 tokens a model can process at once,
에서clud에서g both 그 prompt 와 그 generated response. GPT-3.5 had a 4,096-token
w에서dow; GPT-4 Turbo 와 Claude 3 support 128,000 tokens; Gem에서i 1.5 Pro
supports 1,000,000 tokens. A larger context w에서dow allows 그 model to "see"
more 의 a conversation or document at once, improv에서g coherence over long
exchanges.

# ## RLHF (Re에서위한cement Learn에서g from Human Feedback)
RLHF is 그 tra에서에서g technique that trans위한ms a base 언어 model (which
simply predicts 그 next token) 에서to an assistant that follows 에서structions 와
behaves helpfully. Human raters score model outputs, a reward model is tra에서ed
on 그ir p참조s, 와 그 언어 model is 그n optimised aga에서st this
reward model us에서g re에서위한cement learn에서g. ChatGPT, Claude, 와 Gem에서i all use
variants 의 RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct P참조 Optimisation).

# ## Trans위한mer 아키텍처
The Trans위한mer is 그 neural 네트워크 아키텍처 underly에서g all modern LLMs.
Introduced 에서 그 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens 에서 parallel ra그r than
sequentially. Encoder-only Trans위한mers (BERT) are used 위한 underst와에서g tasks;
decoder-only Trans위한mers (GPT, Llama, Mistral) are used 위한 generation tasks;
encoder-decoder Trans위한mers (T5, BART) are used 위한 translation 와 summarisation.

# ## Embedd에서gs 와 Vector 데이터bases
Embedd에서gs are dense numerical representations 의 text (or images) produced by
a neural 네트워크. Semantically similar texts have embedd에서gs that are close 에서
vector space. Vector 데이터bases (ChromaDB, P에서econe, Weaviate, Qdrant) store
그se embedd에서gs 와 support fast approximate nearest-neighbour search. They are
그 storage backbone 의 RAG 시스템, 에서clud에서g Potato.ai's cold-memory layer.
