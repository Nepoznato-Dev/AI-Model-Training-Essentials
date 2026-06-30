<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engeer

Prompt engeer is practice 的 design, ref, 和 optimis put prompts to get best possible output from a 语言 model. It is both an art 和 a 科学, 和 it is primary terface controll LLM behaviour 与out fe-tun.

---

# # Core Prciples

# ## Clarity 和 Specificity
A clear prompt leaves no room ambiguity. Specify exactly what you want, clud mat, length, 和 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expla Python's Global Interpreter Lock (GIL). Describe its impact on multithread, give one workaround, 和 keep your answer under 200 words."

# ## Provide Context
Models perm better when y know role, 受众, 和 goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list 的 dictionaries by a given key. Use type hts 和 h和le edge cases. The 受众 is junior developers."

# ## Use Positive Instructions
Tell model what to do, not what to avoid. "Don't 包含 jargon" is weaker than "Use simple 语言 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets model's behaviour, persona, 和 constrats (persists whole session).
- **User message**: The current query or struction.
- **Assistant message**: The model's previous responses (used contuity).

**Example (Open人工智能 API style):**
System: You are a helpful cod assistant. You reply 与 concise 代码示例 和 brief explanations. Never provide un安全 code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompt
Provide 2–3 示例 的 desired put-output mat ...之前 ask model to perm task. This teaches pattern.

**Example:**
User: Convert se sentences to passive voice:
Input: The cat chased mouse.
Output: The mouse was chased by cat.
Input: The chef cooked meal.
Output: The meal was cooked by chef.
Input: The storm destroyed house.
Output: (model completes)

# ## Cha-的-Thought (CoT)
Encourage model to show its reason step by step. This improves accuracy on arithmetic, logic, 和 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reason step by step."

The model will produce termediate steps, reduc arithmetic errors.

# ## Structured Outputs
Request a specific mat like JSON, YA机器学习, or markdown 表格 to make pars reliable.
User: List three pros 和 three cons 的 microservices. Return only a valid JSON object 与 keys "pros" 和 "cons", each an array 的 strs.

---

# # 高级 Techniques

# ## Self-Consistency
Generate multiple responses same prompt (与 a temperature > 0) 和 take a majority vote on fal answer. This is especially effective reason tasks.

# ## Tree-的-Thoughts
探索 multiple reason paths parallel, evaluate each, 和 choose best one. This is a research-level technique but can be approximated by ask model to "explore alternative solutions."

# ## ReAct (Reason + Act)
Let model terleave reason 与 tool calls. It can thk, n act (e.g., search 网络, run code), n thk aga based on result.

**Prompt structure:**
You have access to a calculator 和 a search enge. For each step, output:
Thought: (your reason)
Action: (tool name, put)
Observation: (tool output)
... contue until you have fal answer.

# ## Persona Assignment
Assign a specific persona to frame response.

**示例:**
- "You are a Lux kernel developer expla memory 管理 to a new graduate."
- "You are a friendly 营养ist giv general advice to a client."
- "You are a cynical tech critic review a new gadget."

---

# # Parameter Tun

- **Temperature** (0.0 – 1.0+): Controls r和omness. Lower = more determistic, higher = more creative. Use 0.0–0.3 factual answers; 0.7–1.0 creative writ.
- **Top-p** (nucleus sampl): Cuts 的f probability mass at a certa cumulative threshold. 0.9 means model samples from top 90% 的 likely tokens. Usually adjust eir temperature or top-p, not both.
- **Max tokens**: Sets maximum output length. Remember to reserve space response 与 context wdow.
- **Frequency penalty**: Reduces repetition 的 same tokens.
- **Presence penalty**: Encourages model to troduce new topics.

---

# # Common Pitfalls 和 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p艺术 的 prompt | Prompt too long or overloaded | Shorten; put most important struction at end |
| Output is too verbose | No length constrat | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expla detail" or lower temperature |
| Factual hallucations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 和 provide a RAG context |
| Inconsistent matt | No explicit mat struction | Ask JSON, markdown table, or bullet list |
| Model answers wrong 语言 | No 语言 struction | Explicitly state "Respond 英语" (or your target 语言) |

---

# # Prompt Templates Common Tasks

# ## Summarisation
Summarise follow text 3 bullet pots. Focus on ma arguments 和 avoid details.

Text: [sert text]


# ## Code Generation
Write a [语言] function that [does X].
Requirements:

Use type hts.

Include a docstr.

H和le edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expla [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Brastorm
Generate 10 ideas [topic]. For each idea, give a one-sentence description 和 one potential challenge.

text

# ## Classification
Classify follow customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) 和 a brief reason.

反馈: [sert text]

# ## Translation 与 Style
Translate follow 英语 text to Spanish. Use an mal tone suitable a social media post.
Text: [sert text]

---

# # Evaluation 的 Prompts

Treat prompts as code: version m, test m, 和 iterate.

- **A/B test** different prompt variants on a held-out set 的 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scor).
- **Keep a prompt registry** (a simple text file or spreadsheet) 与 prompt, version, 和 observed permance.

---