<!-- 
This file was automatically translated from English to Japanese.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# プロンプトエンジニアリング

プロンプトエンジニアリングとは、言語モデルからできるだけ良い出力を引き出すために、入力プロンプトを設計・改善・最適化する実践です。これは技術であると同時に職人的な側面もあり、fine-tuning を行わずに LLM の振る舞いを制御するための主要な手段でもあります。

---

## 基本原則

### 明確さと具体性
明確なプロンプトには曖昧さが残りません。必要な形式、長さ、視点まで具体的に指定しましょう。

**曖昧な例:**
> "Tell me about Python."

**具体的な例:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, and keep your answer under 200 words."

### 文脈を与える
モデルは、役割、対象読者、目的が分かっているほど良い応答を返しやすくなります。

**文脈なし:**
> "Write a function to sort a list."

**文脈あり:**
> "You are a senior Python developer. Write a function to sort a list of dictionaries by a given key. Use type hints and handle edge cases. The audience is junior developers."

### 否定より肯定の指示を使う
「何を避けるか」より、「何をしてほしいか」を伝える方が有効です。たとえば "Don't include jargon" よりも、"Use simple language accessible to a 10-year-old." の方が明確です。

---

## プロンプトの構造

### System / User / Assistant の役割
多くの LLM API はマルチターン構造をサポートしています。

- **System message**: モデルの振る舞い、人格、制約を設定する。通常はセッション全体に効き続ける。
- **User message**: 現在の質問や指示。
- **Assistant message**: モデルの過去の応答。文脈の継続に使われる。

**例（OpenAI API 風）:**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
望ましい入出力形式の例を 2〜3 個示してから本題を依頼すると、そのパターンを学習しやすくなります。

**例:**
User: Convert these sentences to passive voice:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)

### Chain-of-Thought（CoT）
推論過程を段階的に示すよう促す手法です。算術、論理、多段階タスクの精度向上に役立ちます。

**CoT なし:**
> "What is 24 × 37?"

**CoT あり:**
> "Calculate 24 × 37. Show your reasoning step by step."

このようにすると、中間ステップが出力されるため計算ミスが減りやすくなります。

### 構造化出力
JSON、YAML、Markdown テーブルなど、特定の形式を要求すると後処理しやすくなります。
User: List three pros and three cons of microservices. Return only a valid JSON object with keys "pros" and "cons", each an array of strings.

---

## 高度なテクニック

### Self-Consistency
同じプロンプトに対して複数の応答を生成し（temperature を 0 より大きくする）、最終回答を多数決で選ぶ方法です。特に推論タスクで効果があります。

### Tree-of-Thoughts
複数の推論経路を並行して探索し、それぞれを評価したうえで最良の経路を選ぶ考え方です。研究寄りの手法ですが、「別解も検討して」と促すことで近い振る舞いを引き出せます。

### ReAct（Reasoning + Acting）
モデルに推論とツール使用を交互に行わせる手法です。考え、行動し（例: ウェブ検索やコード実行）、その結果を踏まえて再び考えます。

**プロンプト構造:**
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### ペルソナ設定
特定の人物像を与えることで、回答の視点や語り口を整えられます。

**例:**
- "You are a Linux kernel developer explaining memory management to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## パラメータ調整

- **Temperature**（0.0〜1.0+）: ランダム性を制御する。低いほど決定的、高いほど創造的。事実ベースの回答には 0.0〜0.3、創作には 0.7〜1.0 が目安。
- **Top-p**（nucleus sampling）: 累積確率が一定値に達するまでの候補だけからサンプリングする。0.9 なら上位 90% の確率質量から選ぶ。通常は temperature と top-p の両方を同時に大きく調整しない。
- **Max tokens**: 出力の最大長を決める。context window 内に応答分の余地を残しておく必要がある。
- **Frequency penalty**: 同じトークンの繰り返しを減らす。
- **Presence penalty**: 新しい話題を出しやすくする。

---

## よくある問題と対処法

| 問題 | 主な原因 | 対処法 |
|---------|--------------|-----|
| モデルがプロンプトの一部を無視する | プロンプトが長すぎる、情報を詰め込みすぎている | 短くする。最重要指示は末尾に置く |
| 出力が冗長すぎる | 長さ制約がない | "Limit to 3 sentences" を追加するか `max_tokens` を設定する |
| 出力が短すぎる | 制約が厳しすぎる | "Explain in detail" を追加するか temperature を調整する |
| 事実誤認や hallucination が多い | 文脈不足、質問が曖昧 | "If you are unsure, say 'I don't know'" を加え、RAG 文脈を与える |
| 形式が安定しない | 出力形式の指定がない | JSON、Markdown テーブル、箇条書きなどを明示する |
| 間違った言語で答える | 言語指定がない | "Respond in English" のように明示する |

---

## よくある用途のプロンプトテンプレート

### 要約
次の文章を 3 つの箇条書きで要約してください。細部よりも主要な論点を重視してください。

Text: [insert text]

### コード生成
[language] で [does X] を行う関数を書いてください。
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.

### 説明
[concept] を [非専門家 / 大学生 / 子ども] に説明してください。適切なら比喩も使ってください。

### ブレインストーミング
[topic] に関するアイデアを 10 個出してください。各アイデアについて、1 文の説明と 1 つの課題も添えてください。

### 分類
次の customer feedback を [positive, neutral, negative] に分類してください。
信頼度（0〜100）と短い理由も示してください。

Feedback: [insert text]

### 翻訳と文体調整
次の English text をスペイン語に翻訳してください。ソーシャルメディア投稿に合うカジュアルな口調で書いてください。
Text: [insert text]

---

## プロンプトの評価

プロンプトはコードと同じように扱い、バージョン管理し、テストし、改善を重ねるべきです。

- **A/B テスト** で複数のプロンプト案を保持しておき、未使用の質問セットで比較する。
- **成功を測定** するには、人手評価や自動指標（exact match、BLEU、独自スコアなど）を使う。
- **プロンプトレジストリ**（簡単なテキストファイルやスプレッドシートでもよい）を作り、プロンプト、バージョン、観測された性能を記録する。

---
