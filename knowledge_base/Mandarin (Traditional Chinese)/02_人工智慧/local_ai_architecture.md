# 本地 AI 架構

完全在裝置上執行大型語言模型的實用指南 — 硬體考量、推論引擎、記憶體最佳化,以及邊緣部署的系統設計。

---

## 為什麼要在本地執行 AI?

- **隱私**:資料不會離開裝置。
- **成本**:無需按 Token 支付 API 費用。
- **延遲**:可預測的無網路推論。
- **離線可用性**:無需網路連線即可運作。
- **控制**:完全控制模型版本、客製化與微調。

---

## 硬體需求

### GPU 記憶體(VRAM)
最關鍵的資源。記憶體中的模型大小 ≈ **參數數量 × 每個參數的位元組數**。

| 精度 | 每個參數的位元組數 | 3.8B 模型 | 7B 模型 | 13B 模型 | 70B 模型 |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8位元) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4位元) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**實用指南:**
- 8GB VRAM → 最多 7B 模型(4位元)。
- 12GB VRAM → 最多 13B 模型(4位元)。
- 24GB VRAM → 最多 70B 模型(4位元)或 13B 模型(8位元)。
- Apple Silicon(統一記憶體)可在 64GB+ 系統上執行 70B 模型。

### RAM (系統記憶體)
- 對於 CPU 推論,您需要足夠的系統 RAM 來載入模型(類似於 VRAM 數字)。
- 對於 GPU 推論,系統 RAM 在將模型載入記憶體然後卸載到 VRAM 時很重要。

### 儲存空間
- 量化模型權重佔用幾 GB(例如,4位元 7B ≈ 磁碟上 4 GB)。確保至少有 20–50 GB 可用空間用於多個模型。

### CPU
- 對於提示處理(預填充)和 CPU 卸載,現代多核心 CPU 會有所幫助。
- Apple M 系列晶片由於統一記憶體和神經引擎,在 LLM 上具有出色的效能。

---

## 量化

量化降低權重的數值精度,大幅減少記憶體並提高速度,但準確度損失很小。

### 熱門格式

| 格式 | 位元數 | 說明 | 典型用途 |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | llama.cpp 格式,針對 CPU/GPU 混合最佳化 | 本地推論最佳 |
| **GPTQ** | 4–8 | 僅 GPU,在 CUDA 上高效 | NVIDIA GPU 最佳 |
| **AWQ** | 4 | 激活感知,僅 GPU | GPU 批次推論良好 |
| **ONNX** | 可變 | 標準化,跨平台 | 生產服務 |

### 選擇量化級別
- **Q8_0**(8位元):最小品質損失,最大尺寸。
- **Q6_K**(6位元):良好品質,適當壓縮。
- **Q5_K_M**(5位元):常見的最佳平衡點。
- **Q4_K_M**(4位元):最小,對大多數任務可接受的品質。
- **IQ4_XS** / **IQ3_XS**:改進的量化,在 4/3 位元時具有更好的困惑度。

**經驗法則:**使用 Q4_K_M 來取得品質與大小的良好平衡。如果您有額外的 VRAM,請使用 Q5 或 Q6。

---

## 推論引擎(本地)

### llama.cpp
- 用 C++ 編寫。
- 支援 GGUF 格式。
- 針對 CPU 和 GPU(透過 CUDA、Metal、OpenCL)最佳化。
- 非常快,尤其是在 CPU 上。
- 命令列、伺服器模式和 Python 綁定。

**範例命令:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# (-ngl 32 將 32 層卸載到 GPU)
```

### Ollama
- 用簡單的 CLI 和 REST API 封裝 llama.cpp。
- 自動下載和管理模型。
- 非常適合原型設計和桌面應用程式。
- 支援自訂 Modelfile 用於系統提示。

**使用方式:**
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Windows、macOS、Linux 的圖形化桌面應用程式。
- 一鍵下載和聊天介面。
- 內建本地伺服器,具有 OpenAI 相容的 API。
- 非常適合非技術使用者和快速測試。

### Hugging Face Transformers + bitsandbytes
- HF 模型的標準 Python 函式庫。
- 使用 bitsandbytes 進行 4 位元量化(`load_in_4bit=True`)。
- 在微調方面更靈活,但推論速度比 llama.cpp 慢。

### ExLlamaV2
- 用於 GPTQ 和 AWQ 的超快 GPU 推論。
- NVIDIA GPU 上的最佳效能。
- 支援批次生成。

### mlx (Apple)
- Apple 為 M 系列晶片打造的框架。
- 針對 Apple Silicon 高度最佳化。
- Python API。

---

## 記憶體管理

### 上下文視窗與 KV 快取
KV 快取為上下文中的每一層和每個 Token 儲存鍵值對。它隨著上下文長度線性增長。

**記憶體成本** ≈ 2 × 層數 × (KV 頭數 × 頭維度) × Token 數 × 每個值的位元組數

對於具有 8 個 KV 頭和 128 頭維度的 32 層模型,每個 Token 成本約 32 × 8 × 128 × 2 位元組 = 65 KB。對於 128k Token,僅快取就需要約 8 GB。

### 卸載策略
- **層卸載**:將部分層放在 GPU 上,其他層放在 CPU 上。比純 CPU 快,VRAM 需求更低。
- **Token 串流**:逐步處理 Token 而非一次全部處理。

### 提示快取
在類似的提示之間重複使用 KV 快取,以避免重新計算預填充階段。某些框架支援此功能(例如 vLLM、llama.cpp 搭配 `--prompt-cache`)。

### 記憶體映射檔案
直接從磁碟載入模型權重,而不將它們完全載入 RAM(對於記憶體受限系統上的龐大模型很有用)。llama.cpp 預設使用記憶體映射。

---

## 部署架構

### 單裝置模式
一個模型在一台機器上執行(筆記型電腦、智慧型手機、邊緣裝置)。用於個人助理、筆記應用程式、程式碼補全。

### 混合邊緣-雲端
本地模型處理常見查詢;回退到雲端模型處理複雜問題。這提供了兩全其美的效果 — 大多數情況下速度快/私密,邊緣情況下功能強大。

### 分散式推論(多 GPU)
對於較大的模型,在多個 GPU 之間分割層(張量並行)或在裝置之間分割上下文(管道並行)。使用 llama.cpp 搭配 `-ngl` 或 ExLlamaV2 搭配 `--num-gpu-layers`。

### 行動部署
- **Android**:透過 JNI 綁定或 ML Kit 使用 llama.cpp。
- **iOS**:透過 Swift 綁定或 mlx 使用 llama.cpp。
- **Web**:使用 WebLLM(透過 ONNX runtime 在 WebGPU 上執行)或 transformers.js。

---

## 效能最佳化

### Flash Attention
加速注意力計算並減少記憶體使用。在 llama.cpp、ExLlamaV2 和現代 Transformers 函式庫中可用。

### 批次推論
在單一前向傳遞中處理多個提示。大幅提高吞吐量。使用 llama-batch 或 vLLM。

### 提前停止 / Token 預算
設定最大 Token 預算以防止無限制生成。

### 推測解碼
使用小型快速模型(草稿)來預測 Token,然後與大型模型並行驗證。可產生 2–3× 加速。

---

## 實用設定指南

### 1. 安裝 Ollama
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
然後將請求傳送到 `http://localhost:11434/api/generate`。

### 4. Python 整合
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (替代方案)直接使用 llama.cpp
```bash
# 從 Hugging Face 下載 GGUF
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# 執行伺服器
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## 監控與可觀察性
- 追蹤 GPU 使用率(Linux 上的 `nvidia-smi`,macOS 上的活動監視器)。
- 追蹤記憶體使用量(RAM 和 VRAM)。
- 追蹤每秒 Token 數(吞吐量)。
- 追蹤首個 Token 時間(延遲)。
- 使用 llama.cpp 或 Ollama 的內建日誌記錄。

---

## 限制與權衡

**品質差距**:小型本地模型(3.8B–7B)在複雜推理上通常不如大型雲端模型(GPT-4、Claude 3.5)。

**知識截止**:模型知識在訓練時凍結;使用 RAG 注入當前資訊。

**多語言**:較小的模型可能多語言能力較差。

**工具使用**:代理工作流程(函式呼叫)在小型模型上可能較不可靠。

對於許多日常任務(摘要、問答、程式碼補全、分類),本地模型已經足夠並且正在快速改進。
