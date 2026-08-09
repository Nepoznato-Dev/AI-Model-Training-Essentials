---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 本地AI架构
完全在设备上运行大型语言模型的实用指南 - 硬件注意事项、推理引擎、内存优化和边缘部署的系统设计。
---

## 为什么要在本地运行人工智能？
- **隐私**：没有数据离开设备。
- **成本**：每个代币没有 API 费用。
- **延迟**：可预测、无网络推理。
- **离线可用性**：无需互联网即可工作。
- **控制**：完全控制模型版本、定制和微调。
---

## 硬件要求
### GPU 内存 (VRAM)
最关键的资源。内存中的模型大小 ≈ **参数 × 每个参数的字节**。
|精密|每个参数的字节数 | 3.8B型号| 7B型号| 13B型号| 70B型|
|------------|----------|------------|---------|------------|-----------|
| FP32 | 4 | 〜15 GB | 〜28 GB | 〜52 GB | 〜280 GB |
| FP16 | 2 | 〜7.6 GB | 〜14 GB | 〜26 GB | 〜140 GB |
| INT8（8 位）| 1 | 〜3.8 GB | 〜7 GB | 〜13 GB | 〜70 GB |
| INT4（4 位）| 0.5 | 0.5 〜1.9 GB | 〜3.5 GB | 〜6.5 GB | 〜35 GB |
**实用指南：**
- 8GB VRAM → 4 位时最多 7B 型号。
- 12GB VRAM → 4 位时最多 13B 型号。
- 24GB VRAM → 4 位时高达 70B 型号（8 位时高达 13B）。
- Apple Silicon（统一内存）可以在 64GB+ 系统上运行 70B 型号。
### RAM（系统内存）
- 对于 CPU 推理，您需要足够的系统 RAM 来加载模型（类似于 VRAM 数量）。
- 对于 GPU 推理，系统 RAM 对于在卸载到 VRAM 之前将模型加载到内存中很重要。
### 存储
- 量化模型权重占用几 GB（例如，磁盘上的 4 位 7B ≈ 4 GB）。确保多个型号至少有 20–50 GB 可用空间。
###CPU
- 对于即时处理（预填充）和 CPU 卸载，现代多核 CPU 会有所帮助。
- 由于统一的内存和神经引擎，Apple M 系列芯片对于 LLM 具有出色的性能。
---

## 量化
量化会降低权重的数值精度，从而显着减少内存并以较小的精度成本提高速度。
### 流行格式
|格式|比特|描述 |典型用途|
|--------|------|-------------|------------|
| **GGUF** | 4–8 | llama.cpp 格式，针对 CPU/GPU 混合进行了优化 |最适合本地推理 |
| **GPTQ** | 4–8 |仅 GPU，在 CUDA 上高效 |最适合 NVIDIA GPU |
| **AWQ** | 4 |激活感知，仅 GPU |适合在 GPU 上进行批量推理 |
| **ONNX** |变量|标准化、跨平台|生产服务|
### 选择量化级别
- **Q8_0**（8 位）：最小的质量损失，最大的尺寸。
- **Q6_K**（6 位）：质量好，压缩不错。
- **Q5_K_M**（5 位）：常见最佳点。
- **Q4_K_M**（4 位）：对于大多数任务来说最小、可接受的质量。
- **IQ4_XS** / **IQ3_XS**：改进了量化，在 4/3 位时具有更好的困惑度。
**经验法则：** 使用 Q4_K_M 可以实现质量和尺寸的良好平衡。如果您有额外的 VRAM，请使用 Q5 或 Q6。
---

## 推理引擎（本地）
### 骆驼.cpp
- 用 C++ 编写。
- 支持GGUF格式。
- 针对 CPU 和 GPU 进行了优化（通过 CUDA、Metal、OpenCL）。
- 非常快，尤其是在 CPU 上。
- 命令行、服务器模式和 Python 绑定。
**命令示例：**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### 奥拉马
- 使用简单的 CLI 和 REST API 包装 llama.cpp。
- 自动下载模型并进行管理。
- 非常适合原型设计和桌面应用程序。
- 支持系统提示的自定义模型文件。
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM工作室
- 适用于 Windows、macOS、Linux 的图形桌面应用程序。
- 一键下载和聊天界面。
- 内置本地服务器，具有兼容 OpenAI 的 API。
- 适合非技术用户和快速测试。
### 拥抱脸部变形金刚+bitsandbytes
- HF 模型的标准 Python 库。
- 使用`bitsandbytes`进行 4 位量化 (`load_in_4bit=True`)。
- 微调更灵活，但推理速度比 llama.cpp 慢。
### ExLlamaV2
- GPTQ 和 AWQ 的 GPU 推理速度非常快。
- NVIDIA GPU 上的最佳性能。
- 支持批量生成。
### mlx（苹果）
- Apple M 系列芯片的框架。
- 针对 Apple Silicon 进行了高度优化。
- Python API。
---

## 内存管理
### 上下文窗口和KV缓存
KV 缓存存储上下文中每个层和每个令牌的键值对。它随着上下文长度线性增长。
内存成本 ≈ 2 × 层 × (KV 头 × 头暗) × 令牌 × 每个值的字节数
对于具有 8 KV head 和 128 head dim 的 32 层模型，每个令牌的成本约为 32 × 8 × 128 × 2 字节 = 每个令牌 65 KB。对于 128k 令牌，大约 8 GB 仅用于缓存。
### 卸载策略
- **层卸载**：将一些层放在 GPU 上，其他层放在 CPU 上。比纯 CPU 更快，VRAM 要求更低。
- **令牌流**：增量处理令牌而不是一次性处理所有令牌。
### 提示缓存
在类似的提示中重用 KV 缓存，以避免重新计算预填充阶段。一些框架支持这一点（例如 vLLM、带有`--prompt-cache`的 llama.cpp ）。
### 内存映射文件
直接从磁盘加载模型权重，而不将它们完全加载到 RAM 中（对于内存有限的系统上的大型模型很有用）。 llama.cpp 默认使用内存映射。
---

## 部署架构
### 单设备模式
一种模型在一台机器上运行（笔记本电脑、智能手机、边缘设备）。用于个人助理、笔记应用程序、代码完成。
### 混合边缘云
本地模型处理常见查询；对于复杂问题，回退到云模型。这提供了两全其美的效果——大多数人的速度/私密性，以及边缘情况的能力。
### 分布式推理（多 GPU）
对于较大的模型，跨多个 GPU 分割层（张量并行性）或跨设备分割上下文（管道并行性）。将 llama.cpp 与`-ngl`或 ExLlamaV2 与`--num-gpu-layers`结合使用。
### 移动部署
- **Android**：通过 JNI 绑定或 ML Kit 使用 llama.cpp。
- **iOS**：通过 Swift 绑定或 mlx 使用 llama.cpp。
- **Web**：使用 WebLLM（通过 ONNX 运行时在 WebGPU 上运行）或 Transformers.js。
---

## 性能优化
### 闪光注意
加速注意力计算并减少内存使用。可在 llama.cpp、ExLlamaV2 和现代 Transformers 库中使用。
### 批量推理
在一次前向传递中处理多个提示。显着提高吞吐量。使用`llama-batch`或 vLLM。
### 提前停止/代币预算
设置最大代币预算以防止无限生成。
### 推测解码
使用小型快速模型（草稿）来预测标记，然后使用大型模型并行进行验证。可以产生 2–3 倍的加速。
---

## 实用设置指南
### 1.安装Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. 拉取模型
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. 使用 API 运行
```bash
ollama serve
```

然后将请求发送到`http://localhost:11434/api/generate`。
### 4.Python 集成
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5.（替代）直接使用llama.cpp
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## 监控和可观察性
- 跟踪 GPU 利用率（Linux 上为 `nvidia-smi`，macOS 上为活动监视器）。
- 跟踪内存使用情况（RAM 和 VRAM）。
- 跟踪每秒令牌数（吞吐量）。
- 跟踪第一个令牌的时间（延迟）。
- 使用 llama.cpp 或 Ollama 的内置日志记录。
---

## 限制和权衡
- **质量差距**：小型本地模型（3.8B–7B）在复杂推理上通常表现不佳大型云模型（GPT-4，Claude 3.5）。
- **知识截止**：模型知识在训练时被冻结；使用 RAG 注入当前信息。
- **多语言**：较小的型号可能具有较少的多语言功能。
- **工具使用**：代理工作流程（函数调用）在小型模型上可能不太可靠。
对于许多日常任务（摘要、问答、代码完成、分类），本地模型已经足够并且正在快速改进。