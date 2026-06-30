<!-- 
This file was automatically translated from English to Japanese.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engeer

Prompt engeer is practice design, ref, optimis put prompts to get best possible output from a 言語 model. It is both an art a 科学, it is primary terface に controll LLM behaviour out fe-tun.

---

# # Core Prciples

# ## Clarity Specificity
A clear prompt leaves no room に ambiguity. Specify exactly what you want, clud にmat, length, perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expla Python's Global Interpreter Lock (GIL). Describe its impact on multithread, give one workaround, keep your answer under 200 words."

# ## Provide Context
Models perにm better when y know role, 読者, goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list dictionaries by a given key. Use type hts hle edge cases. The 読者 is junior developers."

# ## Use Positive Instructions
Tell model what to do, not what to avoid. "Don't 含む jargon" is weaker than "Use simple 言語 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets model's behaviour, persona, constrats (persists に whole session).
- **User message**: The current query or struction.
- **Assistant message**: The model's previous responses (used に contuity).

**Example (Open人工知能 API style):**
System: You are a helpful cod assistant. You reply concise コード例 brief explanations. Never provide un安全な code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompt
Provide 2–3 例 desired put-output にmat 前に ask model to perにm task. This teaches pattern.

**Example:**
User: Convert se sentences to passive voice:
Input: The cat chased mouse.
Output: The mouse was chased by cat.
Input: The chef cooked meal.
Output: The meal was cooked by chef.
Input: The storm destroyed house.
Output: (model completes)

# ## Cha--Thought (CoT)
Encourage model to show its reason step by step. This improves accuracy on arithmetic, logic, multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reason step by step."

The model will produce termediate steps, reduc arithmetic errors.

# ## Structured Outputs
Request a specific にmat like JSON, YA機械学習, or markdown 表 to make pars reliable.
User: List three pros three cons microservices. Return only a valid JSON object keys "pros" "cons", each an array strs.

---

# # 上級 Techniques

# ## Self-Consistency
Generate multiple responses に same prompt ( a temperature > 0) take a majority vote on fal answer. This is especially effective に reason tasks.

# ## Tree--Thoughts
探索 multiple reason paths parallel, evaluate each, choose best one. This is a research-level technique but can be approximated by ask model to "explore alternative solutions."

# ## ReAct (Reason + Act)
Let model terleave reason tool calls. It can thk, n act (e.g., search ウェブ, run code), n thk aga based on result.

**Prompt structure:**
You have access to a calculator a search enge. For each step, output:
Thought: (your reason)
Action: (tool name, put)
Observation: (tool output)
... contue until you have fal answer.

# ## Persona Assignment
Assign a specific persona to frame response.

**例:**
- "You are a Lux kernel developer expla memory 管理 to a new graduate."
- "You are a friendly 栄養ist giv general advice to a client."
- "You are a cynical tech critic review a new gadget."

---

# # Parameter Tun

- **Temperature** (0.0 – 1.0+): Controls romness. Lower = more determistic, higher = more creative. Use 0.0–0.3 に factual answers; 0.7–1.0 に creative writ.
- **Top-p** (nucleus sampl): Cuts f probability mass at a certa cumulative threshold. 0.9 means model samples from top 90% likely tokens. Usually adjust eir temperature or top-p, not both.
- **Max tokens**: Sets maximum output length. Remember to reserve space に response context wdow.
- **Frequency penalty**: Reduces repetition same tokens.
- **Presence penalty**: Encourages model to troduce new topics.

---

# # Common Pitfalls Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p芸術 prompt | Prompt too long or overloaded | Shorten; put most important struction at end |
| Output is too verbose | No length constrat | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expla detail" or lower temperature |
| Factual hallucations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" provide a RAG context |
| Inconsistent にmatt | No explicit にmat struction | Ask に JSON, markdown table, or bullet list |
| Model answers wrong 言語 | No 言語 struction | Explicitly state "Respond 英語" (or your target 言語) |

---

# # Prompt Templates に Common Tasks

# ## Summarisation
Summarise follow text 3 bullet pots. Focus on ma arguments avoid details.

Text: [sert text]


# ## Code Generation
Write a [言語] function that [does X].
Requirements:

Use type hts.

Include a docstr.

Hle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expla [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Brastorm
Generate 10 ideas に [topic]. For each idea, give a one-sentence description one potential challenge.

text

# ## Classification
Classify follow customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) a brief reason.

フィードバック: [sert text]

# ## Translation Style
Translate follow 英語 text to Spanish. Use an にmal tone suitable に a social media post.
Text: [sert text]

---

# # Evaluation Prompts

Treat prompts as code: version m, test m, iterate.

- **A/B test** different prompt variants on a held-out set queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scor).
- **Keep a prompt registry** (a simple text file or spreadsheet) prompt, version, observed perにmance.

---