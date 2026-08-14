---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 認知偏誤與邏輯謬誤
該文件整合了影響人類決策和人工智慧系統輸出的認知偏差、邏輯謬誤和推理錯誤。
---

## 認知偏差
認知偏誤是判斷和決策中偏離理性的系統模式。在軟體開發和人工智慧系統中，這些可能會導致糟糕的設計決策、有缺陷的需求和偏見的模型行為。
### 確認偏誤
**它是什麼：** 以證實先前存在的信念的方式搜尋、解釋和回憶訊息的傾向。
**開發中的壞例子：**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**在程式碼審查中：**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**緩解措施：**
- 積極尋找反駁證據
- 使用盲碼審查
- 鼓勵不同意見
- 明確記錄假設
### 錨定偏差
**它是什麼：** 過度依賴遇到的第一個訊息。
**錯誤的例子：**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**緩解措施：**
- 獲得多個獨立的估計
- 使用計劃撲克進行估算
- 考慮範圍而不是點估計
- 參考歷史數據
### 沉沒成本謬論
**它是什麼：** 由於先前投入的資源（時間、金錢、精力）而繼續努力，即使放棄會更好。
**錯誤的例子：**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**緩解措施：**
- 根據未來價值而不是過去的投資來評估決策
- 定期重新評估專案可行性
- 為轉型創造心理安全感
- 使用客觀標準做出繼續/停止決策
### 可用性啟發式
**它是什麼：** 高估現有或最新資訊的重要性。
**錯誤的例子：**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**緩解措施：**
- 使用數據驅動的決策
- 查閱全面的威脅模型
- 查看基本費率和統計數據
- 避免優先順序中的新近偏差
### 鄧寧-克魯格效應
**它是什麼：** 在某項任務上能力較低的人會高估自己的能力；專家可能會低估他們的水平。
**錯誤的例子：**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**緩解措施：**
- 鼓勵持續學習
- 實施同儕審查流程
- 建立導師計劃
- 培養謙遜和好奇心
---

## 邏輯謬誤
邏輯謬誤是破壞論證有效性的推理錯誤。人工智慧模型可以產生包含這些謬誤的輸出。
### Ad Hominem（人身攻擊）
**它是什麼：** 攻擊提出論點的人而不是論點本身。
**錯誤的例子：**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**為什麼不好：** 回饋的有效性取決於其內容，而不是審查者的資歷。
### 訴諸權威
**它是什麼：** 聲稱某件事是真的，因為權威人物這麼說，沒有證據。
**錯誤的例子：**```markdown
"This architecture must be correct because Google uses it."
```

**為什麼不好：** 適用於 Google 規模的方法可能不適用於您的用例。
### 錯誤的二分法（非黑即白的思考）
**它是什麼：** 當存在更多選項時僅呈現兩個選項。
**錯誤的例子：**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**現實：** 在這些極端之間存在許多選擇（優化熱路徑、對特定元件使用 Rust、改進 Python 程式碼等）
### 滑坡
**它是什麼：** 認為一個事件將不可避免地導致一系列負面後果。
**錯誤的例子：**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**為什麼不好：** 在沒有證據的情況下假設不可避免的進展；忽略緩解因素。
### 循環推理
**它是什麼：** 使用結論作為前提。
**錯誤的例子：**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc（虛假原因）
**它是什麼：** 假設因為 B 跟隨 A，所以 A 導致了 B。
**錯誤的例子：**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**現實：**相關性並不意味著因果關係。其他因素也可能是造成這種情況的原因。
### 稻草人
**它是什麼：** 歪曲某人的論點以使其更容易攻擊。
**錯誤的例子：**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### 從眾謬誤
**它是什麼：** 認為某件事是正確的，因為很多人相信它。
**錯誤的例子：**```markdown
"Everyone is using Kubernetes, so we should too."
```

**為什麼不好：** 受歡迎程度並不能保證適合您的特定需求。
---

## 人工智慧中的推理失敗
### 多步驟邏輯錯誤
**錯誤的例子：**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**為什麼不好：**
- 犯了肯定後果的謬誤
- Alice 無需成為程式設計師即可編寫程式碼
- 邏輯結構：(P→Q, Q) ⊬ P
**正確推理：**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### 數學推理失敗
**錯誤的例子：**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**現實：** 如果球的成本為 0.10 美元，球棒的成本多 1 美元 (1.10 美元)，則總計為 1.20 美元。正確答案是球 0.05 美元，球棒 1.05 美元。
### 因果推理錯誤
**錯誤的例子：**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**現實：** 兩者都是由第三個因素（炎熱的天氣）引起的，而不是彼此造成的。
---

## 改進策略
### 對於人類決策
1. **意識訓練**：學會辨識常見偏見
2. **清單使用**：使用決策清單來抵銷偏見
3. **多元化團隊**：包括不同觀點的人
4. **事前剖析**：想像失敗並回溯找出原因
5. **文件**：記錄推理以供以後審查
### 對於人工智慧系統
1. **思路提示**：請模型顯示推理步驟
2. **自我修正**：讓模型審查並批評其答案
3. **形式驗證**：使用符號推理工具進行關鍵邏輯
4. **分解**：將複雜的問題分解為較小的步驟
5. **外部工具**：使用計算機和解算器完成數學任務
6. **多個樣本**：產生多個回應並進行比較
---

## 相關主題
- **AI/LLM 失敗**：有關幻覺和推理問題，請參閱 `ai_llm_failures.md`
- **矛盾的來源**：請參閱有關評估衝突資訊的文檔
- **批判性思考**：應用這些概念來評估論點和證據
- **提示工程**：請參閱`../02_artificial_intelligence/prompt_engineering.md`以了解減少推理錯誤的技術
---

## 軟體開發中的其他認知偏差
### 現狀偏見
**它是什麼：** 維持當前狀態的偏好；任何改變都被視為損失。
**錯誤的例子：**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**緩解措施：**
- 量化不改變的成本
- 設定定期升級時間表
- 創造安全的實驗環境
- 將變化視為機遇，而不是威脅
### 樂觀偏見
**它是什麼：** 低估時間、成本和風險，同時高估收益。
**錯誤的例子：**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**緩解措施：**
- 使用參考類別預測（與過去的類似項目相比）
- 添加应急缓冲（20-50%）
- 進行事前剖析
- 随着时间的推移跟踪估计准确性
### 倖存者偏差
**它是什麼：** 專注於成功的例子，而忽略失敗。
**錯誤的例子：**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**緩解措施：**
- 研究成功與失敗
- 尋找基本費率和統計數據
- 考慮不可見的數據
- 避免挑選例子
### 基本歸因錯誤
**它是什麼：** 將他人的行為歸因於性格而不是環境。
**錯誤的例子：**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**緩解措施：**
- 考慮情境因素
- 練習同理心
- 專注於系統，而不是個人
- 使用無可指責的事後分析
### 事後諸葛亮偏見
**它是什麼：** 事件發生後，相信它一直是可以預測的。
**錯誤的例子：**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**緩解措施：**
- 在結果之前記錄預測
- 檢視決策背景，而不僅僅是結果
- 避免「我告訴過你了」文化
- 專注於改善流程，而不是指責
---

## 更多邏輯謬誤
### 追求新奇
**它是什麼：** 假設某事物因為更新而更好。
**錯誤的例子：**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### 訴諸傳統
**它是什麼：** 認為某件事是正確的，因為它一直都是這樣做的。
**錯誤的例子：**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque（訴諸虛偽）
**它是什麼：** 透過指出批評者的不一致來駁回批評。
**錯誤的例子：**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### 載入問題
**它是什麼：**提出一個包含假設的問題。
**錯誤的例子：**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### 沒有真正的蘇格蘭人
**它是什麼：** 在受到挑戰時對普遍主張進行例外處理。
**錯誤的例子：**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### 遺傳謬誤
**它是什麼：** 根據事物的起源而不是當前的優點來判斷事物。
**錯誤的例子：**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### 中間立場謬誤
**它是什麼：** 假設真相總是處於兩個極端的中間。
**錯誤的例子：**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## 人工智慧系統中的認知偏差
### 訓練資料偏差
人工智慧模型繼承了訓練資料中存在的偏差。
**範例：**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**緩解措施：**
- 審核訓練資料是否有偏差
- 使用去偏技術
- 測試有偏差的輸出
- 多樣化的資料收集
### 自動化偏差
**它是什麼：** 過度依賴自動化系統，即使它們是錯誤的。
**範例：**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**緩解措施：**
- 保持人工監督
- 鼓勵對人工智慧輸出進行批判性評估
- 不要認為人工智慧是絕對正確的
- 實施審查流程
### 理解的錯覺
**它是什麼：** 相信您了解人工智慧的工作原理，而實際上您並不了解。
**範例：**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**緩解措施：**
- 教育用戶了解人工智慧的局限性
- 系統如何運作保持透明
- 避免將人工智慧擬人化
- 設定適當的期望
---

## 案例研究
### 案例研究 1：架構選擇中的確認偏誤
**事件：** 一個團隊為小型應用程式選擇了微服務架構。
**根本原因：** 團隊負責人閱讀了幾篇讚揚微服務的文章，並且
僅尋求確認此選擇的信息，忽略有關複雜性的警告。
**影響：**
- 3 名開發人員團隊的巨大開銷
- 部署複雜度增加 10 倍
- 由於網路呼叫而導致效能下降
- 專案延後了6個月
**課程：** 根據您的特定情境評估架構，而不僅僅是
正面的評價。明確考慮權衡。
### 案例研究 2：遺留系統中的沉沒成本
**事件：** 本公司持續維護客製化的 CRM 長達 5 年
儘管有更好的選擇。
**根本原因：** “我們已經投資了 200 萬美元，現在不能放棄。”
**影響：**
- 年度維護成本：50萬美元
- 機會成本：無法使用現代功能
- 人才保留問題（開發人員希望使用現代技術）
- 5 年總成本：450 萬美元，SaaS 替代方案為 150 萬美元
**教訓：** 過去的投資已經沉沒。根據未來價值做出決策。
### 案例研究 3：安全性中的可用性啟發式
**事件：** 團隊優先防禦最近公開的攻擊
向量，同時忽略更可能的威脅。
**根本原因：** 最近的新聞報導使一種威脅類型高度可用
在記憶中，扭曲了風險評估。
**影響：**
- 花費 10 萬美元來緩解低機率威脅
- 實際違規是透過被忽視的媒介發生的
- 恢復成本：50萬美元以上
**教訓：** 使用資料驅動的威脅建模，而不是基於新近度的優先順序。
---

## 實際練習
### 偏差偵測練習
回顧最近的決定並詢問：
1.我們做了什麼假設？
2. 哪些證據與我們的結論相矛盾？
3. 我們是否考慮了多種選擇或以第一個想法為基礎？
4. 我們繼續下去是因為未來的價值還是過去的投資？
5. 如果別人問我們，我們會推薦什麼？
### 發現邏輯謬誤
練習辨識日常討論中的謬誤：
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### 驗屍技術
開始專案之前：
1.想像未來6個月
2. 該項目慘敗
3. 寫出失敗原因的故事
4. 逆向工作以防止這些故障模式
這抵消了樂觀偏見和可用性啟發法。
---

## 工具和框架
### 決策日誌模板
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### 偏見清單
在做出重要決定之前：
- [ ] 我們是否曾尋求反駁證據？
- [ ] 我們是否以初始資訊為基礎？
- [ ] 沉沒成本對我們有影響嗎？
- [ ] 我們對自己的估計是否過於自信？
- [ ] 我們是否考慮過基本費率？
- [ ] 我們是否因可用性/新近度偏差而陷入困境？
- [ ] 如果重新開始，我們會做出同樣的選擇嗎？
### 紅隊練習
指派某人反對擬議的決定：
- 他們的作用是發現缺陷
- 他們必須提出替代觀點
- 團隊實踐建設性地回應批評
- 記錄提出和解決的問題
這抵銷了確認偏誤和群體思維。