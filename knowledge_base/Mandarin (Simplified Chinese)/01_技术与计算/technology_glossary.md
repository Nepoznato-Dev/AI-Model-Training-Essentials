# 技术术语表

这是一份参考性术语表，涵盖现代 AI 与计算领域中的 AI 模型、硬件、基准测试和核心概念。

---

## AI 语言模型与助手

### ChatGPT
ChatGPT 是 OpenAI 开发的一款 AI 聊天机器人，首次发布于 2022 年 11 月。它由 GPT 系列大型语言模型（LLM）驱动。ChatGPT 是历史上增长速度最快的消费级 AI 产品之一，在发布后的两个月内用户数就达到 1 亿。它支持文本对话、代码生成、摘要总结和创意写作。付费版本可使用 GPT-4 和 GPT-4o 等更强大的模型。

### GPT (Generative Pre-trained Transformer)
GPT 是 OpenAI 创建的大型语言模型家族。其架构采用仅解码器（decoder-only）的 Transformer，并在海量文本语料上以“预测下一个 token”为目标进行训练。关键版本包括 GPT-2（2019 年，15 亿参数，因“危险到不宜发布”的舆论而知名）、GPT-3（2020 年，1750 亿参数，通过 API 被广泛使用）、GPT-3.5（最初版 ChatGPT 的核心模型）以及 GPT-4（2023 年，多模态，在许多基准测试中的表现接近人类专家水平）。

### Claude
Claude 是 Anthropic 开发的 AI 助手，名称来自信息论创始人 Claude Shannon。Anthropic 由前 OpenAI 研究人员创立，重点研究“宪法式 AI（constitutional AI）”——这是一种通过训练模型遵循一组原则来提升安全性的技术。Claude 系列模型（Claude 1、2、3 Haiku / Sonnet / Opus）以超长上下文窗口（最高可达 200,000 tokens）、细腻的推理能力，以及相较基础 LLM 更少的有害输出而闻名。

### Gemini
Gemini 是 Google DeepMind 的多模态 AI 模型家族，于 2023 年 12 月发布。Gemini 原生支持多模态——从一开始就同时基于文本、图像、音频和视频进行训练，而不是像早期模型那样通过微调后续添加模态能力。其版本包括 Gemini Nano（端侧）、Gemini Flash（速度快、成本效率高）和 Gemini Ultra（能力最强）。Gemini 驱动着 Google 的 AI 聊天机器人 Bard（后更名为 Gemini）以及 Google Search AI Overviews。

### Phi-3-mini
Phi-3-mini 是 Microsoft 开发的一款小型语言模型（SLM），参数规模为 38 亿，于 2026 年 4 月发布。与大多数大型模型不同，Phi-3-mini 训练所用的是经过精心筛选的“教科书级质量”数据集——这是 Microsoft Research 开创的一种方法，强调数据质量高于原始数据量。尽管规模远小于 GPT-4 或 Claude 3 Opus，Phi-3-mini 在 MMLU 和 HumanEval 等推理基准上仍能达到或超过若干体量大出数倍的模型。其基础版本支持 4k token 上下文窗口，长上下文版本支持 128k。Phi-3-mini 可在单张消费级 GPU 上运行，若现代智能手机具备足够 RAM，甚至也能在端侧运行。

### Llama (Meta AI)
Llama（Large Language Model Meta AI）是 Meta 发布的开放权重模型家族。Llama 2（2023）面向研究和商业用途发布，参数规模从 7B 到 70B 不等。Llama 3（2026）显著提升了性能，模型规模从 8B 到 70B（后续还有 400B+）。由于权重可公开下载，Llama 模型成为庞大微调生态的基础（如 Mistral、Alpaca、Vicuna 等），也被广泛用于本地化/私有化 AI 部署。

### Mistral
Mistral AI 是一家法国 AI 公司，开发开放及专有的 LLM。Mistral 7B（2023）证明，借助滑动窗口注意力（sliding window attention）和分组查询注意力（grouped-query attention）等高效技术，70 亿参数模型也能达到远大于其体量的模型性能。Mixtral 8x7B（2026）是一种混合专家（mixture-of-experts）模型——它会将每个 token 路由到 8 个专家网络中的一个子集，从而以更低的计算成本实现接近 GPT-3.5 水平的性能。Mistral 的模型权重完全开放，也可以在本地运行。

---

## GPU 硬件与显卡

### GPU (Graphics Processing Unit)
GPU 是一种面向大规模并行计算设计的处理器。它最初用于渲染 3D 图形，如今已成为 AI/ML 训练和推理的关键硬件，因为它能够利用成千上万个小型核心并行执行大量浮点运算。AI 领域的两大 GPU 厂商主要是 NVIDIA 和 AMD。

### NVIDIA GeForce RTX Series
RTX（Ray Tracing Texel eXtreme）系列是 NVIDIA 的消费级 GPU 产品线。RTX 30xx（Ampere，2020）和 RTX 40xx（Ada Lovelace，2022）两代产品都包含专门用于加速 AI 运算的 Tensor Cores。对于本地运行 AI 模型来说，VRAM（显存）至关重要——8GB 显存的 GPU 可以在 4-bit 量化下运行 7B 参数模型；24GB 显存的 GPU 则可以在 4-bit 量化下运行 70B 模型。

### NVIDIA A-Series and H-Series（数据中心）
A100（Ampere，2020）和 H100（Hopper，2022）是 NVIDIA 的专业级 AI 加速器。H100 最多配备 80GB HBM3 内存，是当前大多数大规模 LLM 训练背后的标准硬件。这类 GPU 单价通常在 25,000–40,000 美元之间，但 AI 吞吐量可达到消费级 RTX 显卡的 10–30 倍。

### AMD Radeon RX Series
这是 AMD 的消费级 GPU 产品线。RX 7900 XTX（2022）拥有 24GB VRAM，可通过 ROCm（AMD 的 GPU 计算栈）运行本地 LLM。与 NVIDIA 相比，AMD GPU 对 AI 框架的支持通常仍较弱，但正在持续改善。

### Intel Arc
Intel Arc 是 Intel 自 2022 年起推出的独立显卡产品线。Arc GPU 支持 XeSS（Intel 的超级采样技术），并通过 OpenVINO 和 IPEX-LLM 框架，对 AI 推理任务提供有限但不断增强的支持。

### ARK Intel (ark.intel.com)
ARK 是 Intel 在 ark.intel.com 上提供的官方产品规格数据库。它为每一款 Intel CPU、GPU、FPGA 和 NUC 产品提供详细技术规格，包括核心数量、主频、TDP、支持的内存类型以及指令集特性。当你听到“去 ARK 查参数”时，指的就是访问这个数据库以获取权威的硬件信息。

---

## AI 性能基准

### MMLU（大规模多任务语言理解）
MMLU 是一个用于测试 LLM 知识面的基准，覆盖数学、历史、法律、医学和计算机科学等 57 个学术科目。它由来自真实大学水平考试的选择题组成。70% 的得分大致相当于人类本科生水平；GPT-4 和 Claude 3 的得分都高于 86%。尽管体量很小，Phi-3-mini 的得分也在 70% 左右。

### HumanEval
HumanEval 是 OpenAI 用于代码生成的基准测试。它包含 164 道带有自动化测试用例的 Python 编程题。模型通过 pass@k 指标进行评估——即在生成的 k 个解答中，至少有一个通过全部测试的概率。GPT-4 的得分约为 87%（pass@1）；经过良好调优的 7B 模型可达到约 50–60%。

### HellaSwag
HellaSwag 是一个常识推理基准。模型会收到一句描述日常活动的句子，然后必须从四个选项中选出最可能的后续内容。错误选项经过专门设计，看起来可信却存在细微错误。它用于测试模型是否真正理解物理和社会情境。

### ARC (AI2 Reasoning Challenge)
ARC 是 Allen Institute for AI 推出的一个基准。它由小学科学题目组成，分为 "Easy" 和 "Challenge" 两个集合。Challenge 集合中的问题让基于检索的方法和简单统计模型都难以应对，因此需要多步推理。

---

## AI/ML 核心概念

### RAG (Retrieval-Augmented Generation)
RAG 是一种将检索系统（通常是向量数据库）与语言模型结合起来的技术。它不是只依赖模型的参数化知识，而是先从外部知识库中检索相关文档，再将这些内容加入模型上下文中。这样，模型无需重新训练，也能回答最新或特定领域的信息。Potato.ai 使用的就是一种 RAG 形式——它先从自身 KB 中检索内容，再将结果放入上下文后生成回答。

### Fine-tuning
Fine-tuning（微调）是指在一个预训练模型的基础上，继续使用更小、面向特定领域的数据集进行训练。这样可以调整模型权重，使其适配某项特定任务或领域。例如，一个基础 LLM 可以通过医疗记录进行微调，从而变成医疗问答助手。微调的计算成本较高，但远低于从零开始训练。

### Quantisation
Quantisation（量化）是指降低模型权重的数值精度（例如从 32-bit float 降到 4-bit integer）。这会显著降低内存占用——一个 7B 模型在 16-bit 精度下约需 14GB VRAM；同一个模型在 4-bit（GGUF 格式）下约需 4GB。量化通常只会带来较小且可接受的精度下降，也是让大模型能够在消费级硬件甚至移动设备上运行的关键技术。

### Context Window
上下文窗口（context window）是模型一次能够处理的最大 token 数量，其中既包括提示词，也包括生成的回复。GPT-3.5 的上下文窗口为 4,096 tokens；GPT-4 Turbo 和 Claude 3 支持 128,000 tokens；Gemini 1.5 Pro 则支持 1,000,000 tokens。更大的上下文窗口意味着模型能够一次“看到”更多对话或文档内容，从而在长篇交互中保持更好的连贯性。

### RLHF（基于人类反馈的强化学习）
RLHF 是一种训练技术，用于将基础语言模型（它本来只是预测下一个 token）转变为能够遵循指令并提供有帮助回答的助手。具体过程是：由人工标注者对模型输出打分，基于这些偏好训练奖励模型，然后再用强化学习让语言模型针对该奖励模型进行优化。ChatGPT、Claude 和 Gemini 都使用了 RLHF 或类似的对齐技术变体（例如 Constitutional AI、Direct Preference Optimisation）。

### Transformer Architecture
Transformer 是支撑所有现代 LLM 的神经网络架构。它由 Vaswani 等人在 2017 年论文《Attention Is All You Need》中提出，采用自注意力机制并行处理所有 token，而不是按顺序逐个处理。仅编码器 Transformer（BERT）主要用于理解类任务；仅解码器 Transformer（GPT、Llama、Mistral）主要用于生成类任务；编码器—解码器 Transformer（T5、BART）则主要用于翻译和摘要。

### Embeddings 与向量数据库
Embeddings（嵌入）是神经网络生成的文本（或图像）稠密数值表示。语义相近的文本，其 embedding 在向量空间中也彼此接近。向量数据库（ChromaDB、Pinecone、Weaviate、Qdrant）负责存储这些 embeddings，并支持快速的近似最近邻搜索。它们是 RAG 系统的存储基础设施，Potato.ai 的冷记忆层也建立在此之上。
