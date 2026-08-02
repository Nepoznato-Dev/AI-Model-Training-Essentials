<!-- 
This file was automatically translated from English to Japanese.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# テクノロジー Glossary

A リファレンス glossary covering AI models, hardware, benchmarks, と core concepts
で その modern AI と コンピューティング landscape.

---

## AI 言語 Models と Assistants

### ChatGPT
ChatGPT is an AI chatbot developed by OpenAI, first released で November 2022.
It is powered by その GPT series の large 言語 models (LLMs). ChatGPT is one
の fastest-growing consumer AI products で 歴史, reaching 100 million
users within two months の launch. It supports text-based conversation, code
generation, summarisation, と creative writing. Paid tiers provide access to
more powerful models such as GPT-4 と GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT is a family の large 言語 models created by OpenAI. その アーキテクチャ
uses a decoder-only Transformer trained と a next-token prediction objective on
massive text corpora. Key versions include GPT-2 (2019, 1.5B parameters, notable
のために "too dangerous to release" publicity), GPT-3 (2020, 175B parameters, widely
used via その API), GPT-3.5 (その backbone の original ChatGPT), と GPT-4
(2023, multimodal, パフォーマンス close to human expert level on many benchmarks).

### Claude
Claude is an AI assistant developed by Anthropic. It is named after Claude
Shannon, その founder の information theory. Anthropic was founded by former
OpenAI researchers と focuses on "constitutional AI" — a technique to make
models safer by training them to follow a set の principles. Claude models
(Claude 1, 2, 3 Haiku / Sonnet / Opus) are known のために long context windows (up
to 200,000 tokens), nuanced reasoning, と reduced harmful output compared to
baseline LLMs.

### Gemini
Gemini is Google DeepMind's family の multimodal AI models, announced で
December 2023. Gemini is natively multimodal — trained from その ground up on
text, images, audio, と video simultaneously, unlike earlier models that had
modalities added via fine-tuning. Versions include Gemini Nano (on-device),
Gemini Flash (fast, cost-efficient), と Gemini Ultra (highest-capability).
Gemini powers Google's AI chatbot Bard (renamed Gemini) と Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini is a small 言語 model (SLM) developed by Microsoft と 3.8B
parameters. It was released で April 2026. Unlike most large models, Phi-3-mini
was trained on a carefully curated "textbook-quality" dataset — a technique
pioneered by Microsoft Research — that prioritises データ quality over raw volume.
Despite being far smaller than GPT-4 or Claude 3 Opus, Phi-3-mini matches or
outperforms models several times larger on reasoning benchmarks such as MMLU と
HumanEval. It supports a 4k token context window で its base variant と a 128k
window で その long-context variant. Phi-3-mini can run on a single consumer GPU
or even on-device on a modern smartphone と sufficient RAM.

### Llama (Meta AI)
Llama (Large 言語 Model Meta AI) is an open-weights family の models
released by Meta. Llama 2 (2023) was released のために research と commercial use
と sizes ranging from 7B to 70B parameters. Llama 3 (2026) improved
パフォーマンス significantly, と models ranging from 8B to 70B (と later 400B+).
Because その weights are publicly downloadable, Llama models are その foundation
のために a large ecosystem の fine-tuned variants (Mistral, Alpaca, Vicuna, etc.)
と are widely used のために local/private AI deployments.

### Mistral
Mistral AI is a French AI company that develops open と proprietary LLMs.
Mistral 7B (2023) demonstrated that a 7B-parameter model can match その
パフォーマンス の much larger models using efficient techniques such as sliding
window attention と grouped-query attention. Mixtral 8x7B (2026) is a mixture-
の-experts model — it routes each token to a subset の 8 expert networks,
achieving GPT-3.5-level パフォーマンス while being computationally cheaper.
Mistral's models are fully open-weight と can be run locally.

---

## GPU Hardware と Graphics Cards

### GPU (Graphics Processing Unit)
A GPU is a processor designed のために massively parallel computation. Originally
built のために rendering 3D graphics, GPUs have become essential のために AI/ML training
と inference because they can perform thousands の floating-point operations
simultaneously using thousands の small cores. その two main GPU manufacturers
のために AI are NVIDIA と AMD.

### NVIDIA GeForce RTX Series
その RTX (Ray Tracing Texel eXtreme) series is NVIDIA's consumer GPU line. RTX
30xx (Ampere, 2020) と RTX 40xx (Ada Lovelace, 2022) generations include
dedicated Tensor Cores のために accelerating AI operations. VRAM (video RAM) is
critical のために running AI models locally — an 8GB GPU can handle 7B parameter
models で 4-bit quantisation; a 24GB GPU can handle 70B models で 4-bit.

### NVIDIA A-Series と H-Series (データ Centre)
その A100 (Ampere, 2020) と H100 (Hopper, 2022) are NVIDIA's professional AI
accelerators. An H100 has up to 80GB の HBM3 memory と is その standard
hardware behind most large-scale LLM training today. These GPUs cost $25,000–
$40,000 each but offer 10–30× その AI throughput の consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU line. その RX 7900 XTX (2022) has 24GB VRAM と can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA のために AI frameworks, though サポート is improving.

### Intel Arc
Intel Arc is Intel's discrete GPU product line, released starting で 2022. Arc
GPUs サポート XeSS (Intel's super-sampling) と have limited but growing サポート
のために AI inference tasks via OpenVINO と IPEX-LLM frameworks.

### ARK Intel (ark.intel.com)
ARK is Intel's official product specifications データベース at ark.intel.com. It
provides detailed technical specifications のために every Intel CPU, GPU, FPGA, と
NUC product, including core counts, clock speeds, TDP, supported memory types,
と instruction-set features. When you hear "check ARK のために specs," it means
visiting that データベース のために authoritative hardware information.

---

## AI パフォーマンス Benchmarks

### MMLU (Massive Multitask 言語 Understanding)
MMLU is a benchmark テスト LLM knowledge across 57 academic subjects including
mathematics, 歴史, 法律, 医学, と computer 科学. It consists の
multiple-choice questions drawn from real university-level exams. A score の
70% is roughly human undergraduate level; GPT-4 と Claude 3 score above 86%.
Phi-3-mini scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark のために code generation. It consists の 164 Python
programming problems と automated test cases. Models are measured on
pass@k — その probability that at least one の k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasoning benchmark. Models are given a sentence
describing a mundane activity と must choose その most likely continuation from
four options. その incorrect options are specially designed to be plausible but
subtly wrong. It tests whether a model has a grounded understanding の physical
と social situations.

### ARC (AI2 Reasoning Challenge)
ARC is a benchmark from その Allen Institute のために AI. It consists の grade-school
科学 questions, split into "Easy" と "Challenge" sets. その Challenge set
contains questions that retrieval-based methods と simple statistical models
struggle と, requiring multi-step reasoning.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combines a retrieval system (typically a vector
データベース) と a 言語 model. Instead の relying solely on その model's
parametric knowledge, RAG first retrieves relevant documents from an external
ナレッジベース と then includes them で その model's context. This allows その
model to answer questions about up-to-date or domain-specific information
without retraining. Potato.ai uses a form の RAG — it retrieves from its KB
と includes その results で その context before generating a response.

### Fine-tuning
Fine-tuning is その process の continuing to train a pre-trained model on a
smaller, domain-specific dataset. This adapts その model's weights のために a
particular task or domain. のために example, a base LLM might be fine-tuned on
medical records to create a medical Q&A assistant. Fine-tuning is
computationally expensive but much cheaper than training from scratch.

### Quantisation
Quantisation reduces その numerical precision の model weights (e.g. from 32-bit
float to 4-bit integer). This dramatically reduces memory footprint — a 7B model
で 16-bit precision requires ~14GB VRAM; その same model で 4-bit (GGUF format)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation と is その main technique enabling large models to run on consumer
hardware or even mobile devices.

### Context Window
その context window is その maximum number の tokens a model can process at once,
including both その prompt と その generated response. GPT-3.5 had a 4,096-token
window; GPT-4 Turbo と Claude 3 サポート 128,000 tokens; Gemini 1.5 Pro
supports 1,000,000 tokens. A larger context window allows その model to "see"
more の a conversation or document at once, improving coherence over long
exchanges.

### RLHF (Reinforcement Learning from Human フィードバック)
RLHF is その training technique that transforms a base 言語 model (which
simply predicts その next token) into an assistant that follows instructions と
behaves helpfully. Human raters score model outputs, a reward model is trained
on their preferences, と その 言語 model is then optimised against this
reward model using reinforcement learning. ChatGPT, Claude, と Gemini all use
variants の RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Preference Optimisation).

### Transformer アーキテクチャ
その Transformer is その neural ネットワーク アーキテクチャ underlying all modern LLMs.
Introduced で その 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens で parallel rather than
sequentially. Encoder-only Transformers (BERT) are used のために understanding tasks;
decoder-only Transformers (GPT, Llama, Mistral) are used のために generation tasks;
encoder-decoder Transformers (T5, BART) are used のために translation と summarisation.

### Embeddings と Vector Databases
Embeddings are dense numerical representations の text (or images) produced by
a neural ネットワーク. Semantically similar texts have embeddings that are close で
vector space. Vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) store
these embeddings と サポート fast approximate nearest-neighbour search. They are
その storage backbone の RAG システム, including Potato.ai's cold-memory layer.
