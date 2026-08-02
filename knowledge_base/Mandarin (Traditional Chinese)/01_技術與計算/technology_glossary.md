# 技術術語表

這是一份參考性術語表，涵蓋現代 AI 與計算領域中的 AI 模型、硬體、基準測試和核心概念。

---

## AI 語言模型與助手

### ChatGPT
ChatGPT 是 OpenAI 開發的一款 AI 聊天機器人，首次發布於 2022 年 11 月。它由 GPT 系列大型語言模型（LLM）驅動。ChatGPT 是歷史上成長速度最快的消費級 AI 產品之一，在發布後兩個月內使用者數就達到 1 億。它支援文字對話、程式碼生成、摘要總結和創意寫作。付費版本可使用 GPT-4 和 GPT-4o 等更強大的模型。

### GPT (Generative Pre-trained Transformer)
GPT 是 OpenAI 建立的大型語言模型家族。其架構採用僅解碼器（decoder-only）的 Transformer，並在海量文字語料上以“預測下一個 token”為目標進行訓練。關鍵版本包括 GPT-2（2019 年，15 億參數，因“危險到不宜發布”的輿論而知名）、GPT-3（2020 年，1750 億參數，透過 API 被廣泛使用）、GPT-3.5（最初版 ChatGPT 的核心模型）以及 GPT-4（2023 年，多模態，在許多基準測試中的表現接近人類專家水平）。

### Claude
Claude 是 Anthropic 開發的 AI 助手，名稱來自資訊理論創始人 Claude Shannon。Anthropic 由前 OpenAI 研究人員創立，重點研究“憲法式 AI（constitutional AI）”——這是一種透過訓練模型遵循一組原則來提升安全性的技術。Claude 系列模型（Claude 1、2、3 Haiku / Sonnet / Opus）以超長上下文視窗（最高可達 200,000 tokens）、細膩的推理能力，以及相較基礎 LLM 更少的有害輸出而聞名。

### Gemini
Gemini 是 Google DeepMind 的多模態 AI 模型家族，於 2023 年 12 月發布。Gemini 原生支援多模態——從一開始就同時基於文字、影像、音訊和影片進行訓練，而不是像早期模型那樣透過微調後續新增模態能力。其版本包括 Gemini Nano（裝置端）、Gemini Flash（速度快、成本效率高）和 Gemini Ultra（能力最強）。Gemini 驅動著 Google 的 AI 聊天機器人 Bard（後更名為 Gemini）以及 Google Search AI Overviews。

### Phi-3-mini
Phi-3-mini 是 Microsoft 開發的一款小型語言模型（SLM），參數規模為 38 億，於 2026 年 4 月發布。與大多數大型模型不同，Phi-3-mini 訓練所用的是經過精心篩選的“教科書級品質”資料集——這是 Microsoft Research 開創的一種方法，強調資料品質高於原始資料量。儘管規模遠小於 GPT-4 或 Claude 3 Opus，Phi-3-mini 在 MMLU 和 HumanEval 等推理基準上仍能達到或超過若干體量大出數倍的模型。其基礎版本支援 4k token 上下文視窗，長上下文版本支援 128k。Phi-3-mini 可在單張消費級 GPU 上執行，若現代智慧型手機具備足夠 RAM，甚至也能在裝置端執行。

### Llama (Meta AI)
Llama（Large Language Model Meta AI）是 Meta 發布的開放權重模型家族。Llama 2（2023）面向研究和商業用途發布，參數規模從 7B 到 70B 不等。Llama 3（2026）顯著提升了效能，模型規模從 8B 到 70B（後續還有 400B+）。由於權重可公開下載，Llama 模型成為龐大微調生態的基礎（如 Mistral、Alpaca、Vicuna 等），也被廣泛用於本地化/私有化 AI 部署。

### Mistral
Mistral AI 是一家法國 AI 公司，開發開放及專有的 LLM。Mistral 7B（2023）證明，藉助滑動視窗注意力（sliding window attention）和分組查詢注意力（grouped-query attention）等高效技術，70 億參數模型也能達到遠大於其體量的模型效能。Mixtral 8x7B（2026）是一種混合專家（mixture-of-experts）模型——它會將每個 token 路由到 8 個專家網路中的一個子集，從而以更低的計算成本實現接近 GPT-3.5 水平的效能。Mistral 的模型權重完全開放，也可以在本地執行。

---

## GPU 硬體與顯示卡

### GPU (Graphics Processing Unit)
GPU 是一種面向大規模平行計算設計的處理器。它最初用於渲染 3D 圖形，如今已成為 AI/ML 訓練和推理的關鍵硬體，因為它能夠利用成千上萬個小型核心並行執行大量浮點運算。AI 領域的兩大 GPU 廠商主要是 NVIDIA 和 AMD。

### NVIDIA GeForce RTX Series
RTX（Ray Tracing Texel eXtreme）系列是 NVIDIA 的消費級 GPU 產品線。RTX 30xx（Ampere，2020）和 RTX 40xx（Ada Lovelace，2022）兩代產品都包含專門用於加速 AI 運算的 Tensor Cores。對於本地執行 AI 模型來說，VRAM（顯示記憶體）至關重要——8GB 顯示記憶體的 GPU 可以在 4-bit 量化下執行 7B 參數模型；24GB 顯示記憶體的 GPU 則可以在 4-bit 量化下執行 70B 模型。

### NVIDIA A-Series and H-Series（資料中心）
A100（Ampere，2020）和 H100（Hopper，2022）是 NVIDIA 的專業級 AI 加速器。H100 最多配備 80GB HBM3 記憶體，是當前大多數大規模 LLM 訓練背後的標準硬體。這類 GPU 單價通常在 25,000–40,000 美元之間，但 AI 吞吐量可達到消費級 RTX 顯示卡的 10–30 倍。

### AMD Radeon RX Series
這是 AMD 的消費級 GPU 產品線。RX 7900 XTX（2022）擁有 24GB VRAM，可透過 ROCm（AMD 的 GPU 計算棧）執行本地 LLM。與 NVIDIA 相比，AMD GPU 對 AI 框架的支援通常仍較弱，但正在持續改善。

### Intel Arc
Intel Arc 是 Intel 自 2022 年起推出的獨立顯示卡產品線。Arc GPU 支援 XeSS（Intel 的超級取樣技術），並透過 OpenVINO 和 IPEX-LLM 框架，對 AI 推理任務提供有限但不斷增強的支援。

### ARK Intel (ark.intel.com)
ARK 是 Intel 在 ark.intel.com 上提供的官方產品規格資料庫。它為每一款 Intel CPU、GPU、FPGA 和 NUC 產品提供詳細技術規格，包括核心數量、主頻、TDP、支援的記憶體型別以及指令集特性。當你聽到“去 ARK 查參數”時，指的就是存取這個資料庫以獲取權威的硬體資訊。

---

## AI 效能基準

### MMLU（大規模多工語言理解）
MMLU 是一個用於測試 LLM 知識面的基準，覆蓋數學、歷史、法律、醫學和電腦科學等 57 個學術科目。它由來自真實大學水平考試的選擇題組成。70% 的得分大致相當於人類本科生水平；GPT-4 和 Claude 3 的得分都高於 86%。儘管體量很小，Phi-3-mini 的得分也在 70% 左右。

### HumanEval
HumanEval 是 OpenAI 用於程式碼生成的基準測試。它包含 164 道帶有自動化測試用例的 Python 程式設計題。模型透過 pass@k 指標進行評估——即在生成的 k 個解答中，至少有一個透過全部測試的機率。GPT-4 的得分約為 87%（pass@1）；經過良好調優的 7B 模型可達到約 50–60%。

### HellaSwag
HellaSwag 是一個常識推理基準。模型會收到一句描述日常活動的句子，然後必須從四個選項中選出最可能的後續內容。錯誤選項經過專門設計，看起來可信卻存在細微錯誤。它用於測試模型是否真正理解物理和社會情境。

### ARC (AI2 Reasoning Challenge)
ARC 是 Allen Institute for AI 推出的一個基準。它由小學科學題目組成，分為 "Easy" 和 "Challenge" 兩個集合。Challenge 集合中的問題讓基於檢索的方法和簡單統計模型都難以應對，因此需要多步推理。

---

## AI/ML 核心概念

### RAG (Retrieval-Augmented Generation)
RAG 是一種將檢索系統（通常是向量資料庫）與語言模型結合起來的技術。它不是隻依賴模型的參數化知識，而是先從外部知識庫中檢索相關文件，再將這些內容加入模型上下文中。這樣，模型無需重新訓練，也能回答最新或特定領域的資訊。Potato.ai 使用的就是一種 RAG 形式——它先從自身 KB 中檢索內容，再將結果放入上下文後生成回答。

### Fine-tuning
Fine-tuning（微調）是指在一個預訓練模型的基礎上，繼續使用更小、面向特定領域的資料集進行訓練。這樣可以調整模型權重，使其適配某項特定任務或領域。例如，一個基礎 LLM 可以透過醫療記錄進行微調，從而變成醫療問答助手。微調的計算成本較高，但遠低於從零開始訓練。

### Quantisation
Quantisation（量化）是指降低模型權重的數值精度（例如從 32-bit float 降到 4-bit integer）。這會顯著降低記憶體佔用——一個 7B 模型在 16-bit 精度下約需 14GB VRAM；同一個模型在 4-bit（GGUF 格式）下約需 4GB。量化通常只會帶來較小且可接受的精度下降，也是讓大模型能夠在消費級硬體甚至移動裝置上執行的關鍵技術。

### Context Window
上下文視窗（context window）是模型一次能夠處理的最大 token 數量，其中既包括提示詞，也包括生成的回覆。GPT-3.5 的上下文視窗為 4,096 tokens；GPT-4 Turbo 和 Claude 3 支援 128,000 tokens；Gemini 1.5 Pro 則支援 1,000,000 tokens。更大的上下文視窗意味著模型能夠一次“看到”更多對話或文件內容，從而在長篇互動中保持更好的連貫性。

### RLHF（基於人類反饋的強化學習）
RLHF 是一種訓練技術，用於將基礎語言模型（它本來只是預測下一個 token）轉變為能夠遵循指令並提供有幫助回答的助手。具體過程是：由人工標註者對模型輸出打分，基於這些偏好訓練獎勵模型，然後再用強化學習讓語言模型針對該獎勵模型進行最佳化。ChatGPT、Claude 和 Gemini 都使用了 RLHF 或類似的對齊技術變體（例如 Constitutional AI、Direct Preference Optimisation）。

### Transformer Architecture
Transformer 是支撐所有現代 LLM 的神經網路架構。它由 Vaswani 等人在 2017 年論文《Attention Is All You Need》中提出，採用自注意力機制並行處理所有 token，而不是按順序逐個處理。僅編碼器 Transformer（BERT）主要用於理解類任務；僅解碼器 Transformer（GPT、Llama、Mistral）主要用於生成類任務；編碼器—解碼器 Transformer（T5、BART）則主要用於翻譯和摘要。

### Embeddings 與向量資料庫
Embeddings（嵌入）是神經網路生成的文字（或影像）稠密數值表示。語義相近的文字，其 embedding 在向量空間中也彼此接近。向量資料庫（ChromaDB、Pinecone、Weaviate、Qdrant）負責儲存這些 embeddings，並支援快速的近似最近鄰搜尋。它們是 RAG 系統的儲存基礎設施，Potato.ai 的冷記憶層也建立在此之上。
