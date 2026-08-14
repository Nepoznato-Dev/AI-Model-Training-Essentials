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

# 技術術語
涵蓋人工智慧模型、硬體、基準測試和核心概念的參考術語表
在現代人工智慧和計算領域。
---

## AI 語言模型和助手
### 聊天GPT
ChatGPT 是 OpenAI 開發的人工智慧聊天機器人，於 2022 年 11 月首次發布。
它由 GPT 系列大型語言模型 (LLM) 提供支援。 ChatGPT 就是其中之一
史上成長最快的消費性人工智慧產品數量達 1 億
發布後兩個月內的用戶。它支援基於文字的對話、程式碼
生成、總結和創意寫作。付費等級可讓您訪問
更強大的模型，如 GPT-4 和 GPT-4o。
### GPT（生成式預訓練變壓器）
GPT 是由 OpenAI 創建的一系列大型語言模型。架構
使用僅解碼器的 Transformer，並透過下一個令牌預測目標進行訓練
海量文本語料庫。關鍵版本包括GPT-2（2019，1.5B參數，值得注意
因「釋放太危險」宣傳），GPT-3（2020，175B參數，廣泛
透過 API 使用）、GPT-3.5（原始 ChatGPT 的骨幹）和 GPT-4
（2023 年，多模式，在許多基準上的性能接近人類專家水平）。
### 克勞德
Claude 是 Anthropic 開發的人工智慧助理。它以克勞德的名字命名
香農，資訊理論的創始人。 Anthropic 的創始人是前
OpenAI 研究人員並專注於「憲法人工智慧」——一種製造
透過訓練他們遵循一系列原則來使模型更安全。克勞德模型
（克勞德 1、2、3 俳句/十四行詩/作品）以長上下文窗口（向上）而聞名
到 200,000 個代幣），細緻入微的推理，並與相比減少了有害輸出
基線法學碩士。
### 雙子座
Gemini 是 Google DeepMind 的多模式 AI 模型系列，於
2023 年 12 月。 Gemini 天生就是多式聯運的－從頭開始接受訓練
文字、圖像、音訊和視訊同時播放，這與早期的模型不同
透過微調添加的模式。版本包括 Gemini Nano（設備上）、
Gemini Flash（快速、經濟高效）和 Gemini Ultra（最高功能）。
Gemini 為 Google 的 AI 聊天機器人 Bard（更名為 Gemini）和 Google Search AI 提供支持
概述。
### Phi-3-迷你
Phi-3-mini是微軟用3.8B開發的小語言模型（SLM）
參數。它於 2024 年 4 月發布。與大多數大型型號不同，Phi-3-mini
接受了精心策劃的「教科書品質」資料集的培訓——一種技術
由微軟研究院首創－數據品質優先於原始資料量。
儘管比 GPT-4 或 Claude 3 Opus 小得多，但 Phi-3-mini 匹配或
在 MMLU 等推理基準上，其表現比模型大幾倍
人類評估。它的基本變體支援 4k 令牌上下文視窗和 128k
長上下文變體中的視窗。 Phi-3-mini 可在單一消費級 GPU 上執行
甚至是具有足夠 RAM 的現代智慧型手機上的裝置。
### 駱駝（元人工智慧）
Llama（大型語言模型元 AI）是一個開放權重模型系列
由 Meta 發布。 Llama 2 (2023) 發布用於研究和商業用途
參數尺寸範圍從 7B 到 70B。羊駝 3 (2024) 改進
性能顯著提高，型號範圍從 8B 到 70B（以及後來的 400B+）。
由於權重可公開下載，因此 Llama 模型是基礎
用於微調變種的大型生態系（Mistral、Alpaca、Vicuna 等）
並廣泛用於本地/私有人工智慧部署。
### 米斯特拉爾
Mistral AI 是一家法國人工智慧公司，開發開放和專有的法學碩士。
Mistral 7B (2023) 證明 7B 參數模型可以匹配
使用滑動等有效技術實現更大模型的性能
視窗注意力和分組查詢注意力。 Mixtral 8x7B (2023) 是一種混合物-
of-experts 模型－它將每個 token 路由到 8 個專家網路的子集，
實現 GPT-3.5 等級的效能，同時計算成本更低。
Mistral 的模型是完全開放式的，可以在本地運行。
---

## GPU 硬體和顯示卡
### GPU（圖形處理單元）
GPU 是專為大規模平行運算而設計的處理器。本來
GPU 專為渲染 3D 圖形而設計，已成為 AI/ML 訓練的必需品
和推理，因為它們可以執行數千個浮點運算
同時使用數千個小核心。兩大GPU廠商
AI 領域有 NVIDIA 和 AMD。
### NVIDIA GeForce RTX 系列
RTX（光線追蹤 Texel eXtreme）系列是 NVIDIA 的消費性 GPU 系列。 RTX
30xx（Ampere，2020 年）和 RTX 40xx（Ada Lovelace，2022 年）幾代包括
用於加速 AI 操作的專用 Tensor Core。 VRAM（視訊 RAM）是
對於本地運行 AI 模型至關重要 - 8GB GPU 可以處理 7B 參數
4 位元量化模型； 24GB GPU 可以處理 4 位元 70B 模型。
### NVIDIA A 系列和 H 系列（資料中心）
A100（Ampere，2020）和 H100（Hopper，2022）是 NVIDIA 的專業 AI
加速器。 H100 具有高達 80GB 的 HBM3 內存，並且是標準配置
當今大多數大規模法學碩士培訓背後的硬體。這些 GPU 的成本為 25,000 美元——
每張售價 40,000 美元，但提供的 AI 吞吐量是消費性 RTX 卡的 10-30 倍。
### AMD Radeon RX 系列
AMD 的消費級 GPU 系列。 RX 7900 XTX (2022) 具有 24GB VRAM，可運行
透過 ROCm（AMD 的 GPU 運算堆疊）獲得本地法學碩士。 AMD GPU普遍較少
儘管支援正在改善，但對 AI 框架的支援比 NVIDIA 更好。
### 英特爾弧
Intel Arc是Intel的獨立GPU產品線，於2022年開始發表。 Arc
GPU 支援 XeSS（英特爾的超級採樣）並且支援有限但不斷增長
透過 OpenVINO 和 IPEX-LLM 框架執行 AI 推理任務。
### ARK 英特爾 (ark.intel.com)
ARK 是英特爾的官方產品規格資料庫，位於 ark.intel.com。它
提供每個 Intel CPU、GPU、FPGA 和的詳細技術規格
NUC 產品，包括核心數量、時脈速度、TDP、支援的記憶體類型、
和指令集功能。當您聽到“檢查 ARK 的規格”時，這意味著
訪問該資料庫以獲取權威的硬體資訊。
---

## 人工智慧效能基準
### MMLU（大規模多工語言理解）
MMLU 是測試 LLM 知識的基準，涵蓋 57 個學術科目，包括
數學、歷史、法律、醫學和電腦科學。它包括
來自真實大學程度考試的多項選擇題。分數為
70%大致是人類大學本科生； GPT-4和Claude 3得分在86%以上。
儘管 Phi-3-mini 尺寸很小，但得分約為 70%。
### 人類評估
HumanEval 是 OpenAI 的程式碼產生基準。它由164個Python組成
自動化測試用例的程式設計問題。模型測量於
pass@k — k 產生的解中至少有一個通過所有解的機率
測試。 GPT-4 分數 ~87% (pass@1)；經過良好調整的 7B 模型可以達到 ~50–60%。
### 海拉斯瓦格
HellaSwag 是一個常識推理基準。給模型一個句子
描述一項平凡的活動，必須選擇最有可能的延續
四個選項。不正確的選項經過專門設計，看似合理，但
微妙地錯誤。它測試模型是否對物理有紮實的理解
和社交場合。
### ARC（AI2 推理挑戰）
ARC 是艾倫人工智慧研究所的基準。它由小學
科學問題，分為「簡單」和「挑戰」組。挑戰集
包含基於檢索的方法和簡單統計模型的問題
鬥爭，需要多步驟推理。
---

## 核心 AI/ML 概念
### RAG（檢索增強生成）
RAG 是一種結合檢索系統（通常是向量
資料庫）和語言模型。而不是僅僅依靠模型
參數化知識，RAG首先從外部檢索相關文檔
知識庫，然後將它們包含在模型的上下文中。這允許
模型來回答有關最新或特定領域資訊的問題
無需再培訓。 Potato.ai 使用一種 RAG 形式 — 它從其 KB 中檢索
並在生成回應之前將結果包含在上下文中。
### 微調
微調是在預訓練模型上繼續訓練的過程
較小的、特定領域的資料集。這會調整模型的權重
特定任務或領域。例如，基礎法學碩士可能會在以下方面進行微調
醫療記錄建立醫療問答助理。微調是
計算成本昂貴，但比從頭開始訓練便宜得多。
### 量化
量化會降低模型權重的數值精確度（例如，從 32 位元
浮點到 4 位整數）。這大大減少了記憶體佔用——7B 模型
16 位元精確度需要 ~14GB VRAM；4 位元相同機型（GGUF 格式）
需要~4GB。量化通常會產生較小但可接受的精度
退化，是使大型模型能夠在消費者上運行的主要技術
硬體甚至行動裝置。
### 上下文視窗
上下文視窗是模型一次可以處理的最大標記數，
包括提示和產生的回應。 GPT-3.5 有 4,096 個代幣
窗戶； GPT-4 Turbo和Claude 3支援128,000個代幣；雙子座1.5專業版
支援 1,000,000 個代幣。更大的上下文視窗允許模型“看到”
一次更多的對話或文檔，提高長時間的連貫性
交流。
### RLHF（來自人類回饋的強化學習）
RLHF 是一種轉換基本語言模型（其中
只是預測下一個標記）到一個遵循指令的助手中，
表現得樂於助人。人類評分者對模型輸出進行評分，訓練獎勵模型
根據他們的偏好，然後針對此優化語言模型
使用強化學習的獎勵模型。 ChatGPT、Claude、Gemini 都使用
RLHF 的變體或類似的對齊技術（例如，Constitutional AI、
直接偏好優化）。
### 變壓器架構
Transformer 是所有現代法學碩士的神經網路架構。
Vaswani 等人在 2017 年的論文《Attention Is All You Need》中介紹，
使用自註意力機制並行處理所有令牌，而不是
依次。僅編碼器 Transformers (BERT) 用於理解任務；
僅解碼器 Transformer（GPT、Llama、Mistral）用於產生任務；
編碼器-解碼器 Transformer（T5、BART）用於翻譯和摘要。
### 嵌入與向量資料庫
嵌入是由以下內容產生的文字（或圖像）的密集數字表示：
一個神經網路。語意相似的文本具有接近的嵌入
向量空間。向量資料庫（ChromaDB、Pinecone、Weaviate、Qdrant）存儲
這些嵌入並支援快速近似最近鄰搜尋。他們是
RAG 系統的儲存主幹，包括 Potato.ai 的冷內存層。