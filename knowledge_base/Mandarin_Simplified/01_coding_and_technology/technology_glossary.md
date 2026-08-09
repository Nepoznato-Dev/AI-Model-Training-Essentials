---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 技术术语
涵盖人工智能模型、硬件、基准测试和核心概念的参考术语表
在现代人工智能和计算领域。
---

## AI 语言模型和助手
### 聊天GPT
ChatGPT 是 OpenAI 开发的人工智能聊天机器人，于 2022 年 11 月首次发布。
它由 GPT 系列大型语言模型 (LLM) 提供支持。 ChatGPT 就是其中之一
史上增长最快的消费类人工智能产品数量达到 1 亿
发布后两个月内的用户。它支持基于文本的对话、代码
生成、总结和创意写作。付费等级可让您访问
更强大的模型，如 GPT-4 和 GPT-4o。
### GPT（生成式预训练变压器）
GPT 是由 OpenAI 创建的一系列大型语言模型。架构
使用仅解码器的 Transformer，并通过下一个令牌预测目标进行训练
海量文本语料库。关键版本包括GPT-2（2019，1.5B参数，值得注意
因“释放太危险”宣传），GPT-3（2020，175B参数，广泛
通过 API 使用）、GPT-3.5（原始 ChatGPT 的骨干）和 GPT-4
（2023 年，多模式，在许多基准上的性能接近人类专家水平）。
### 克劳德
Claude 是 Anthropic 开发的人工智能助手。它以克劳德的名字命名
香农，信息论的创始人。 Anthropic 的创始人是前
OpenAI 研究人员并专注于“宪法人工智能”——一种制造
通过训练他们遵循一系列原则来使模型更安全。克劳德模型
（克劳德 1、2、3 俳句/十四行诗/作品）以长上下文窗口（向上）而闻名
到 200,000 个代币），细致入微的推理，并与相比减少了有害输出
基线法学硕士。
### 双子座
Gemini 是 Google DeepMind 的多模式 AI 模型系列，于
2023 年 12 月。Gemini 天生就是多式联运的——从头开始接受训练
文本、图像、音频和视频同时播放，这与早期的模型不同
通过微调添加的模式。版本包括 Gemini Nano（设备上）、
Gemini Flash（快速、经济高效）和 Gemini Ultra（最高功能）。
Gemini 为 Google 的 AI 聊天机器人 Bard（更名为 Gemini）和 Google Search AI 提供支持
概述。
### Phi-3-迷你
Phi-3-mini是微软用3.8B开发的小语言模型（SLM）
参数。它于 2026 年 4 月发布。与大多数大型型号不同，Phi-3-mini
接受了精心策划的“教科书质量”数据集的培训——一种技术
由微软研究院首创——数据质量优先于原始数据量。
尽管比 GPT-4 或 Claude 3 Opus 小得多，但 Phi-3-mini 匹配或
在 MMLU 等推理基准上，其性能比模型大几倍
人类评估。它的基本变体支持 4k 令牌上下文窗口和 128k
长上下文变体中的窗口。 Phi-3-mini 可以在单个消费级 GPU 上运行
甚至是具有足够 RAM 的现代智能手机上的设备。
### 骆驼（元人工智能）
Llama（大型语言模型元 AI）是一个开放权重模型系列
由 Meta 发布。 Llama 2 (2023) 发布用于研究和商业用途
参数尺寸范围从 7B 到 70B。羊驼 3 (2026) 改进
性能显着提高，型号范围从 8B 到 70B（以及后来的 400B+）。
由于权重可公开下载，因此 Llama 模型是基础
用于微调变种的大型生态系统（Mistral、Alpaca、Vicuna 等）
并广泛用于本地/私有人工智能部署。
### 米斯特拉尔
Mistral AI 是一家法国人工智能公司，开发开放和专有的法学硕士。
Mistral 7B (2023) 证明 7B 参数模型可以匹配
使用滑动等有效技术实现更大模型的性能
窗口注意力和分组查询注意力。 Mixtral 8x7B (2026) 是一种混合物-
of-experts 模型——它将每个 token 路由到 8 个专家网络的子集，
实现 GPT-3.5 级别的性能，同时计算成本更低。
Mistral 的模型是完全开放式的，可以在本地运行。
---

## GPU 硬件和显卡
### GPU（图形处理单元）
GPU 是一种专为大规模并行计算而设计的处理器。本来
GPU 专为渲染 3D 图形而设计，已成为 AI/ML 训练的必需品
和推理，因为它们可以执行数千个浮点运算
同时使用数千个小核心。两大GPU厂商
AI 领域有 NVIDIA 和 AMD。
### NVIDIA GeForce RTX 系列
RTX（光线追踪 Texel eXtreme）系列是 NVIDIA 的消费级 GPU 系列。 RTX
30xx（Ampere，2020 年）和 RTX 40xx（Ada Lovelace，2022 年）几代包括
用于加速 AI 操作的专用 Tensor Core。 VRAM（视频 RAM）是
对于本地运行 AI 模型至关重要 - 8GB GPU 可以处理 7B 参数
4 位量化模型； 24GB GPU 可以处理 4 位 70B 模型。
### NVIDIA A 系列和 H 系列（数据中心）
A100（Ampere，2020）和 H100（Hopper，2022）是 NVIDIA 的专业 AI
加速器。 H100 具有高达 80GB 的 HBM3 内存，并且是标准配置
当今大多数大规模法学硕士培训背后的硬件。这些 GPU 的成本为 25,000 美元——
每张售价 40,000 美元，但提供的 AI 吞吐量是消费类 RTX 卡的 10-30 倍。
### AMD Radeon RX 系列
AMD 的消费级 GPU 系列。 RX 7900 XTX (2022) 具有 24GB VRAM，可以运行
通过 ROCm（AMD 的 GPU 计算堆栈）获得本地法学硕士。 AMD GPU普遍较少
尽管支持正在改善，但对 AI 框架的支持比 NVIDIA 更好。
### 英特尔弧
Intel Arc是Intel的独立GPU产品线，于2022年开始发布。Arc
GPU 支持 XeSS（英特尔的超级采样）并且支持有限但不断增长
通过 OpenVINO 和 IPEX-LLM 框架执行 AI 推理任务。
### ARK 英特尔 (ark.intel.com)
ARK 是英特尔的官方产品规格数据库，位于 ark.intel.com。它
提供每个 Intel CPU、GPU、FPGA 和的详细技术规格
NUC 产品，包括核心数量、时钟速度、TDP、支持的内存类型、
和指令集功能。当您听到“检查 ARK 的规格”时，这意味着
访问该数据库以获取权威的硬件信息。
---

## 人工智能性能基准
### MMLU（大规模多任务语言理解）
MMLU 是测试 LLM 知识的基准，涵盖 57 个学术科目，包括
数学、历史、法律、医学和计算机科学。它包括
来自真实大学水平考试的多项选择题。分数为
70%大致是人类本科水平； GPT-4和Claude 3得分在86%以上。
尽管 Phi-3-mini 尺寸很小，但得分约为 70%。
### 人类评估
HumanEval 是 OpenAI 的代码生成基准。它由164个Python组成
自动化测试用例的编程问题。模型测量于
pass@k — k 生成的解决方案中至少有一个通过所有解决方案的概率
测试。 GPT-4 得分 ~87% (pass@1)；经过良好调整的 7B 模型可以达到 ~50–60%。
### 海拉斯瓦格
HellaSwag 是一个常识推理基准。给模型一个句子
描述一项平凡的活动，必须选择最有可能的延续
四个选项。不正确的选项经过专门设计，看似合理，但
微妙地错误。它测试模型是否对物理有扎实的理解
和社交场合。
### ARC（AI2 推理挑战）
ARC 是艾伦人工智能研究所的基准。它由小学
科学问题，分为“简单”和“挑战”组。挑战集
包含基于检索的方法和简单统计模型的问题
斗争，需要多步骤推理。
---

## 核心 AI/ML 概念
### RAG（检索增强生成）
RAG 是一种结合检索系统（通常是向量
数据库）和语言模型。而不是仅仅依靠模型
参数化知识，RAG首先从外部检索相关文档
知识库，然后将它们包含在模型的上下文中。这允许
模型来回答有关最新或特定领域信息的问题
无需再培训。 Potato.ai 使用一种 RAG 形式 — 它从其 KB 中检索
并在生成响应之前将结果包含在上下文中。
### 微调
微调是在预训练模型上继续训练的过程
较小的、特定领域的数据集。这会调整模型的权重
特定任务或领域。例如，基础法学硕士可能会在以下方面进行微调
医疗记录创建医疗问答助手。微调是
计算成本昂贵，但比从头开始训练便宜得多。
### 量化
量化会降低模型权重的数值精度（例如，从 32 位
浮点到 4 位整数）。这极大地减少了内存占用——7B 模型
16 位精度需要 ~14GB VRAM； 4 位相同模型（GGUF 格式）
需要~4GB。量化通常会产生较小但可接受的精度
退化，是使大型模型能够在消费者上运行的主要技术
硬件甚至移动设备。
### 上下文窗口
上下文窗口是模型一次可以处理的最大标记数，
包括提示和生成的响应。 GPT-3.5 有 4,096 个代币
窗户； GPT-4 Turbo和Claude 3支持128,000个代币；双子座1.5专业版
支持 1,000,000 个代币。更大的上下文窗口允许模型“看到”
一次更多的对话或文档，提高长时间的连贯性
交流。
### RLHF（来自人类反馈的强化学习）
RLHF 是一种转换基本语言模型（其中
只是预测下一个标记）到一个遵循指令的助手中，
表现得乐于助人。人类评分者对模型输出进行评分，训练奖励模型
根据他们的偏好，然后针对此优化语言模型
使用强化学习的奖励模型。 ChatGPT、Claude、Gemini 都使用
RLHF 的变体或类似的对齐技术（例如，Constitutional AI、
直接偏好优化）。
### 变压器架构
Transformer 是所有现代法学硕士的神经网络架构。
Vaswani 等人在 2017 年的论文《Attention Is All You Need》中介绍，
使用自注意力机制并行处理所有令牌，而不是
依次。仅编码器 Transformers (BERT) 用于理解任务；
仅解码器 Transformer（GPT、Llama、Mistral）用于生成任务；
编码器-解码器 Transformer（T5、BART）用于翻译和摘要。
### 嵌入和向量数据库
嵌入是由以下内容生成的文本（或图像）的密集数字表示：
一个神经网络。语义相似的文本具有接近的嵌入
向量空间。矢量数据库（ChromaDB、Pinecone、Weaviate、Qdrant）存储
这些嵌入并支持快速近似最近邻搜索。他们是
RAG 系统的存储主干，包括 Potato.ai 的冷内存层。