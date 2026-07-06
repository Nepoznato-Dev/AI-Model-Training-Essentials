# Prompt Engineering

Prompt engineering 是設計、精煉與最佳化輸入提示詞的實踐，以獲得語言模型的最佳輸出。這既是一門藝術也是一門科學，是在不進行微調的情況下控制 LLM 行為的主要介面。

---

## 核心原則

### 清晰與明確性
清晰的提示詞不留任何模糊空間。精確指定您想要的內容，包括格式、長度和視角。

**模糊：**
> "告訴我關於 Python 的事情。"

**明確：**
> "解釋 Python 的 Global Interpreter Lock (GIL)。描述它對多執行緒的影響，提供一種解決方法，並將答案控制在 200 字以內。"

### 提供上下文
當模型了解角色、受眾和目標時，表現會更好。

**沒有上下文：**
> "撰寫一個排序列表的函數。"

**有上下文：**
> "你是一位資深的 Python 開發者。撰寫一個函數，根據給定鍵值對字典列表進行排序。使用型別提示並處理邊界情況。受眾是初級開發者。"

### 使用正向指令
告訴模型要做什麼，而不是要避免什麼。「不要包含術語」比「使用 10 歲兒童能理解的簡單語言」要弱。

---

## 提示詞結構

### System / User / Assistant 角色
大多數 LLM API 支援多輪對話結構：

- **System message**：設定模型的行為、角色和約束（在整個對話期間持續有效）。
- **User message**：當前的查詢或指令。
- **Assistant message**：模型先前的回應（用於維持連貫性）。

**範例（OpenAI API 風格）：**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
在要求模型執行任務之前，提供 2-3 個期望的輸入輸出格式範例。這會教會模型模式。

**範例：**
User: Convert these sentences to passive voice:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)

### Chain-of-Thought (CoT)
鼓勵模型逐步展示其推理過程。這可以提高算術、邏輯和多步驟任務的準確性。

**沒有 CoT：**
> "24 × 37 等於多少？"

**有 CoT：**
> "計算 24 × 37。逐步展示你的推理過程。"

模型會產生中間步驟，減少算術錯誤。

### 結構化輸出
要求特定格式，如 JSON、YAML 或 markdown 表格，使解析更可靠。
User: List three pros and three cons of microservices. Return only a valid JSON object with keys "pros" and "cons", each an array of strings.

---

## 進階技術

### Self-Consistency
為相同提示詞生成多個回應（temperature > 0），然後對最終答案進行多數投票。這對推理任務特別有效。

### Tree-of-Thoughts
並行探索多個推理路徑，評估每一個，然後選擇最佳的。這是研究級技術，但可以通過要求模型「探索替代方案」來近似實現。

### ReAct (Reasoning + Acting)
讓模型將推理與工具呼叫交錯進行。它可以先思考，然後行動（例如，搜尋網路、執行程式碼），然後根據結果再次思考。

**提示詞結構：**
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### 角色指派
指派特定角色來框定回應。

**範例：**
- "You are a Linux kernel developer explaining memory management to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## 參數調整

- **Temperature**（0.0 – 1.0+）：控制隨機性。較低 = 更確定性，較高 = 更有創造力。對事實性答案使用 0.0–0.3；對創意寫作使用 0.7–1.0。
- **Top-p**（nucleus sampling）：在某個累積閾值處截斷機率質量。0.9 表示模型從前 90% 可能的 token 中採樣。通常只調整 temperature 或 top-p 其中之一，而非兩者都調整。
- **Max tokens**：設定最大輸出長度。記得在上下文視窗內為回應保留空間。
- **Frequency penalty**：減少相同 token 的重複。
- **Presence penalty**：鼓勵模型引入新主題。

---

## 常見陷阱與修正

| 問題 | 可能原因 | 修正方法 |
|---------|--------------|-----|
| 模型忽略部分提示詞 | 提示詞過長或超載 | 縮短；將最重要的指令放在最後 |
| 輸出過於冗長 | 沒有長度限制 | 加入「限制在 3 句話內」或設定 max_tokens |
| 輸出過於簡短 | 過度限制 | 加入「詳細解釋」或降低 temperature |
| 事實幻覺 | 上下文不足或問題模糊 | 加入「如果不確定，請說『我不知道』」並提供 RAG 上下文 |
| 格式不一致 | 沒有明確的格式指令 | 要求 JSON、markdown 表格或項目符號列表 |
| 模型以錯誤語言回答 | 沒有語言指令 | 明確說明「以英文回應」（或您的目標語言） |

---

## 常見任務的提示詞範本

### 摘要
Summarise the following text in 3 bullet points. Focus on the main arguments and avoid details.

Text: [insert text]


### 程式碼生成
Write a [language] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### 解釋
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### 腦力激盪
Generate 10 ideas for [topic]. For each idea, give a one-sentence description and one potential challenge.

text

### 分類
Classify the following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) and a brief reason.

Feedback: [insert text]

### 帶風格的翻譯
Translate the following English text to Spanish. Use an informal tone suitable for a social media post.
Text: [insert text]

---

## 提示詞評估

將提示詞視為程式碼：進行版本控制、測試並迭代。

- **A/B 測試**在預留的查詢集上測試不同的提示詞變體。
- **衡量成功**透過人工評估或自動化指標（例如精確匹配、BLEU、自訂評分）。
- **維護提示詞註冊表**（簡單的文字檔案或試算表），記錄提示詞、版本和觀察到的效能。

---