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

# 本地AI架構
完全在設備上運行大型語言模型的實用指南 - 硬體注意事項、推理引擎、記憶體優化和邊緣部署的系統設計。
---

## 為什麼要在本地運行人工智慧？
- **隱私**：沒有資料離開設備。
- **成本**：每個代幣沒有 API 費用。
- **延遲**：可預測、無網路推理。
- **離線可用性**：無需網路即可運作。
- **控制**：完全控制模型版本、自訂和微調。
---

## 硬體需求
### GPU 記憶體 (VRAM)
最關鍵的資源。記憶體中的模型大小 ≈ **參數 × 每個參數的位元組**。
|精密|每個參數的位元組數 | 3.8B型號| 7B型號| 13B型號| 70B型|
|------------|----------|------------|---------|------------|-----------|
| FP32 | 4 | 〜15 GB | 〜28 GB | 〜52 GB | 〜280 GB |
| FP16 | 2 | 〜7.6 GB | 〜14 GB | 〜26 GB | 〜140 GB |
| INT8（8 位元）| 1 | 〜3.8 GB | 〜7 GB | 〜13 GB | 〜70 GB |
| INT4（4 位元）| 0.5 | 0.5 〜1.9 GB | 〜3.5 GB | 〜6.5 GB | 〜35 GB |
**實用指南：**
- 8GB VRAM → 4 位元時最多 7B 型號。
- 12GB VRAM → 4 位元時最多 13B 型號。
- 24GB VRAM → 4 位元時高達 70B 型號（8 位元時高達 13B）。
- Apple Silicon（統一記憶體）可在 64GB+ 系統上運行 70B 型號。
### RAM（系統記憶體）
- 對於 CPU 推理，您需要足夠的系統 RAM 來載入模型（類似於 VRAM 數量）。
- 對於 GPU 推理，系統 RAM 對於在卸載到 VRAM 之前將模型載入到記憶體中很重要。
### 存儲
- 量化模型權重佔用數 GB（例如，磁碟上的 4 位元 7B ≈ 4 GB）。確保多個型號至少有 20–50 GB 可用空間。
###CPU
- 對於即時處理（預先填充）和 CPU 卸載，現代多核心 CPU 會有所幫助。
- 由於統一的記憶體和神經引擎，Apple M 系列晶片對於 LLM 具有出色的性能。
---

## 量化
量化會降低權重的數值精度，從而顯著減少記憶體並以較小的精度成本提高速度。
### 流行格式
|格式|比特|描述 |典型用途|
|--------|------|-------------|------------|
| **GGUF** | 4–8 | llama.cpp 格式，針對 CPU/GPU 混合進行了最佳化 |最適合本地推理 |
| **GPTQ** | 4–8 |僅 GPU，在 CUDA 上高效能 |最適合 NVIDIA GPU |
| **AWQ** | 4 |激活感知，僅 GPU |適合在 GPU 上進行批量推理 |
| **ONNX** |變數|標準化、跨平台|生產服務|
### 選擇量化級別
- **Q8_0**（8 位元）：最小的質量損失，最大的尺寸。
- **Q6_K**（6 位元）：品質好，壓縮不錯。
- **Q5_K_M**（5 位元）：常見最佳點。
- **Q4_K_M**（4 位元）：對於大多數任務來說最小、可接受的品質。
- **IQ4_XS** / **IQ3_XS**：改進了量化，在 4/3 位元時具有更好的困惑度。
**經驗法則：** 使用 Q4_K_M 可以實現品質和尺寸的良好平衡。如果您有額外的 VRAM，請使用 Q5 或 Q6。
---

## 推理引擎（本地）
### 駱駝.cpp
- 用 C++ 編寫。
- 支援GGUF格式。
- 針對 CPU 和 GPU 進行了最佳化（透過 CUDA、Metal、OpenCL）。
- 非常快，尤其是在 CPU 上。
- 命令列、伺服器模式和 Python 綁定。
**命令範例：**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### 奧拉馬
- 使用簡單的 CLI 和 REST API 包裝 llama.cpp。
- 自動下載模型並進行管理。
- 非常適合原型設計和桌面應用程式。
- 支援系統提示的自訂模型檔案。
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM工作室
- 適用於 Windows、macOS、Linux 的圖形桌面應用程式。
- 一鍵下載和聊天介面。
- 內建本機伺服器，具有相容 OpenAI 的 API。
- 適合非技術用戶和快速測試。
### 擁抱臉部變形金剛+bitsandbytes
- HF 模型的標準 Python 函式庫。
- 使用`bitsandbytes`進行 4 位元量化 (`load_in_4bit=True`)。
- 微調更靈活，但推理速度比 llama.cpp 慢。
### ExLlamaV2
- GPTQ 和 AWQ 的 GPU 推理速度非常快。
- NVIDIA GPU 上的最佳效能。
- 支援批量生成。
### mlx（蘋果）
- Apple M 系列晶片的框架。
- 針對 Apple Silicon 進行了高度最佳化。
- Python API。
---

## 記憶體管理
### 上下文視窗和KV緩存
KV 快取儲存上下文中每個層和每個令牌的鍵值對。它隨著上下文長度線性增長。
記憶體成本 ≈ 2 × 層 × (KV 頭 × 頭暗) × 令牌 × 每個值的位元組數
對於具有 8 KV head 和 128 head dim 的 32 層模型，每個令牌的成本約為 32 × 8 × 128 × 2 位元組 = 每個令牌 65 KB。對於 128k 令牌，大約 8 GB 僅用於快取。
### 卸載策略
- **層卸載**：將一些層放在 GPU 上，其他層放在 CPU 上。比純 CPU 更快，VRAM 要求更低。
- **令牌流**：增量處理令牌而不是一次處理所有令牌。
### 提示快取
在類似的提示中重複使用 KV 快取，以避免重新計算預填充階段。一些框架支援這一點（例如 vLLM、帶有`--prompt-cache`的 llama.cpp ）。
### 記憶體映射文件
直接從磁碟載入模型權重，而不將它們完全載入到 RAM 中（對於記憶體有限的系統上的大型模型很有用）。 llama.cpp 預設使用記憶體映射。
---

## 部署架構
### 單設備模式
一種模型在一台機器上運作（筆記型電腦、智慧型手機、邊緣設備）。用於個人助理、筆記應用程式、代碼完成。
### 混合邊緣雲
本機模型處理常見查詢；對於複雜問題，回退到雲端模型。這提供了兩全其美的效果——大多數人的速度/私密性，以及邊緣情況的能力。
### 分散式推理（多 GPU）
對於較大的模型，跨多個 GPU 分割層（張量並行性）或跨裝置分割上下文（管道並行性）。將 llama.cpp 與`-ngl`或 ExLlamaV2 與`--num-gpu-layers`結合使用。
### 行動部署
- **Android**：透過 JNI 綁定或 ML Kit 使用 llama.cpp。
- **iOS**：透過 Swift 綁定或 mlx 使用 llama.cpp。
- **Web**：使用 WebLLM（透過 ONNX 執行時間在 WebGPU 上運行）或 Transformers.js。
---

## 效能優化
### 閃光注意
加速注意力計算並減少記憶體使用。可在 llama.cpp、ExLlamaV2 和現代 Transformers 庫中使用。
### 批量推理
在一次前向傳遞中處理多個提示。顯著提高吞吐量。使用`llama-batch`或 vLLM。
### 提前停止/代幣預算
設定最大代幣預算以防止無限生成。
### 推測解碼
使用小型快速模型（草稿）來預測標記，然後使用大型模型並行進行驗證。可以產生 2–3 倍的加速。
---

## 實用設定指南
### 1.安裝Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. 拉取模型
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. 使用 API 執行
```bash
ollama serve
```

然後將請求傳送到`http://localhost:11434/api/generate`。
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

## 監控和可觀察性
- 追蹤 GPU 使用率（Linux 上為 `nvidia-smi`，macOS 上為活動監視器）。
- 追蹤記憶體使用情況（RAM 和 VRAM）。
- 追蹤每秒令牌數（吞吐量）。
- 追蹤第一個令牌的時間（延遲）。
- 使用 llama.cpp 或 Ollama 的內建日誌記錄。
---

## 限制和權衡
- **品質差距**：小型本地模型（3.8B–7B）在複雜推理上通常表現不佳大型雲模型（GPT-4，Claude 3.5）。
- **知識截止**：模型知識在訓練時被凍結；使用 RAG 注入當前資訊。
- **多語言**：較小的型號可能具有較少的多語言功能。
- **工具使用**：代理程式工作流程（函數呼叫）在小型模型上可能不太可靠。
對於許多日常任務（摘要、問答、程式碼完成、分類），本地模型已經足夠並且正在快速改進。