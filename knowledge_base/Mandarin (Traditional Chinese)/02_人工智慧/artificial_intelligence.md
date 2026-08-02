# 人工智慧

## 什麼是人工智慧？

人工智慧（Artificial Intelligence, AI）是指在機器中模擬人類智慧的技術，這些機器被程式化以進行思考、學習和解決問題。AI 系統能夠執行通常需要人類智慧的任務，例如語音識別、決策制定、語言翻譯和圖像中的物體識別。這個術語由 John McCarthy 於 1956 年在達特茅斯會議（Dartmouth Conference）上創造，該會議被廣泛認為是 AI 作為一個領域的創立事件。

現代 AI 大致分為窄域人工智慧（Narrow AI，也稱為弱人工智慧），專門設計用於特定任務；以及理論上的通用人工智慧（Artificial General Intelligence, AGI），其將在所有領域中匹配或超越人類的認知能力。目前所有的 AI 系統都是窄域人工智慧。

## AI 的歷史

AI 的歷史跨越近八十年。早期的理論基礎由 Alan Turing 奠定，他在 1950 年的論文《計算機器與智慧》（Computing Machinery and Intelligence）中提出了圖靈測試（Turing Test）——一種衡量機器是否能展現與人類無異的智慧行為的標準。1956 年的達特茅斯會議正式確立了 AI 作為學術學科的地位。

1950 年代至 1970 年代出現了樂觀的早期程式，如 ELIZA（一個簡單的聊天機器人）和 LISP（一種為 AI 設計的程式語言）。1970 年代和 1980 年代的「AI 寒冬」是因未達預期而導致資金和興趣減少的時期。1980 年代隨著專家系統——基於規則的程式，編碼人類專業知識——的出現而復甦。2000 年代帶來了由網路和不斷增長的資料集推動的機器學習突破。2010 年代見證了深度學習的崛起，變革了電腦視覺、自然語言處理（NLP）和強化學習。

## 機器學習

機器學習（Machine Learning, ML）是 AI 的一個子集，使系統能夠從資料中學習而無需被明確程式化。主要的 ML 類別包括：

**監督式學習（Supervised Learning）**：模型在標記的輸入-輸出對上進行訓練。範例包括垃圾郵件檢測和圖像分類。演算法包括線性迴歸、決策樹、支援向量機和神經網路。

**非監督式學習（Unsupervised Learning）**：模型在未標記的資料中尋找模式。範例包括客戶分群和異常檢測。演算法包括 k-means 聚類和主成分分析（PCA）。

**強化學習（Reinforcement Learning）**：代理透過與環境互動來學習，接收獎勵或懲罰。應用於遊戲 AI（AlphaGo、AlphaZero）、機器人技術和推薦系統。

**半監督式學習與自監督式學習（Semi-Supervised and Self-Supervised Learning）**：結合少量標記資料與大量未標記資料集。GPT 模型在預訓練期間使用自監督方法。

## 深度學習

深度學習（Deep Learning）是機器學習的一個子集，使用具有多層（深層網路）的人工神經網路。這些網路受到大腦神經結構的啟發，學習資料的層次化表示。深度學習驅動：

- **電腦視覺（Computer Vision）**：圖像識別、物體檢測、醫學影像
- **自然語言處理（Natural Language Processing）**：機器翻譯、情感分析、問答系統
- **語音識別（Speech Recognition）**：語音助理如 Siri、Alexa、Google Assistant
- **生成式 AI（Generative AI）**：圖像生成（DALL-E、Stable Diffusion）、文字生成（GPT）

關鍵的深度學習架構包括用於圖像的卷積神經網路（CNNs）、用於序列的循環神經網路（RNNs）和 LSTMs、用於語言的 transformers，以及用於合成的生成對抗網路（GANs）。

## 大型語言模型（LLMs）

大型語言模型（Large Language Models, LLMs）是在大量文字資料上訓練的 AI 系統，用於理解和生成人類語言。它們基於 Transformer 架構，由 Vaswani 等人在 2017 年的論文《Attention is All You Need》中提出。LLMs 預測序列中的下一個 token（詞片段），使它們能夠生成連貫的文字、回答問題、撰寫程式碼並執行推理任務。

著名的 LLMs 包括：
- **GPT 系列**（OpenAI）：GPT-3、GPT-4 及其後續版本——廣泛用於聊天和程式碼生成
- **Claude**（Anthropic）：專注於安全性和有用性
- **Gemini**（Google DeepMind）：多模態，整合文字、圖像和程式碼
- **LLaMA / Llama 3**（Meta）：開放權重模型，用於研究和本地部署
- **Mistral**（Mistral AI）：高效的開放模型，可與更大的 LLMs 競爭

LLMs 的訓練分為兩個階段：預訓練（在大型文本語料庫上進行非監督式學習）和微調（監督式學習或透過人類反饋的強化學習，RLHF）。上下文視窗描述了 LLM 一次可以處理多少文字，從 4K tokens（早期的 GPT-3）到 2026 年最先進模型的超過 100 萬 tokens。

## AI 倫理與安全

AI 提出了重要的倫理問題，包括偏見、隱私、工作替代和濫用風險。演算法偏見發生在訓練資料反映歷史不平等時，導致 AI 系統產生歧視性輸出。臉部識別系統對膚色較深的個人顯示出更高的錯誤率。招聘演算法被發現偏好男性候選人。

AI 安全是致力於確保 AI 系統按預期行為而不造成意外傷害的領域。主要關注點包括：
- **對齊（Alignment）**：確保 AI 目標符合人類價值觀
- **可解釋性／可說明性（Interpretability / Explainability）**：理解 AI 為何做出某個決定（在醫學、法律、金融領域至關重要）
- **濫用（Misuse）**：AI 生成的 deepfakes、假訊息、網路攻擊
- **存在性風險（Existential risk）**：理論上的擔憂，即未來的 AGI 可能追求與人類生存不一致的目標

從事 AI 安全工作的組織包括 OpenAI 的安全團隊、Anthropic（由前 OpenAI 安全研究人員創立）、DeepMind 的安全團隊，以及 MIRI 和 ARC 等獨立機構。

## AI 在社會中的應用

AI 正在改變幾乎每個產業：

- **醫療保健**：AI 協助從醫學影像診斷癌症、預測病患結果、加速藥物發現（AlphaFold 解決了蛋白質摺疊結構預測）並個人化治療計劃。
- **金融**：詐騙檢測、演算法交易、信用評分和機器人顧問使用 ML 模型。
- **交通運輸**：自動駕駛車輛使用電腦視覺、光達和強化學習。Tesla Autopilot、Waymo 和 Cruise 是領先的計畫。
- **教育**：個人化學習平台根據個別學生的節奏和學習風格調整內容。
- **創意領域**：AI 生成音樂、藝術和寫作；像 Midjourney、DALL-E 和 GitHub Copilot 這樣的工具已經改變了創意工作流程。
- **網路安全**：AI 檢測異常、識別威脅，並驅動攻擊和防禦。

## 機器人技術與具身 AI

機器人技術將 AI 與實體機器結合。現代機器人使用感知（相機、光達）、規劃和控制來導航和操作環境。Boston Dynamics 的 Atlas 展示了先進的雙足運動。來自 ABB 和 FANUC 等公司的工業機器人自動化製造。家用機器人（Roomba）和手術機器人（da Vinci System）將 AI 應用於日常和醫療環境。具身 AI 研究專注於透過與世界互動學習物理技能的代理，彌合模擬與真實環境之間的差距。

## 當前 AI 趨勢（2020 年代）

- **多模態 AI（Multimodal AI）**：同時處理文字、圖像、音訊和視訊的系統（GPT-4V、Gemini）
- **代理與代理式 AI（Agents and agentic AI）**：可以使用工具、瀏覽網路、撰寫程式碼並採取多步驟行動的 LLMs（OpenAI 的 Operator、Anthropic Computer Use）
- **開放權重模型（Open-weight models）**：Meta 的 LLaMA 使研究人員能夠民主化地存取大型模型
- **裝置端 AI（On-device AI）**：在手機和筆記型電腦上本地運行 AI 模型，無需雲端連接（Apple Intelligence、Qualcomm NPUs）
- **AI 法規（AI regulation）**：歐盟 AI 法案（2026）是世界上第一部全面的 AI 法律，按風險等級對 AI 系統進行分類
