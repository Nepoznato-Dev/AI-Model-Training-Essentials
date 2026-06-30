<!-- 
This file was automatically translated from English to Korean.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engeer

Prompt engeer is practice design, ref, optimis put prompts to get best possible output from a 언어 model. It is both an art a 과 학, it is primary terface controll LLM behaviour 함께out fe-tun.

---

# # Core Prciples

# ## Clarity Specificity
A clear prompt leaves no room ambiguity. Specify exactly what you want, clud mat, length, perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expla Python's Global Interpreter Lock (GIL). Describe its impact on multithread, give one workaround, keep your answer under 200 words."

# ## Provide Context
Models perm better when y know role, 독자, goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list dictionaries by a given key. Use type hts hle edge cases. The 독자 is junior developers."

# ## Use Positive Instructions
Tell model what to do, not what to avoid. "Don't 포함하다 jargon" is weaker than "Use simple 언어 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets model's behaviour, persona, constrats (persists whole session).
- **User message**: The current query or struction.
- **Assistant message**: The model's previous responses (used contuity).

**Example (Open인공 지능 API style):**
System: You are a helpful cod assistant. You reply 함께 concise 코드 예시 brief explanations. Never provide un안전한 code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompt
Provide 2–3 예시 desired put-output mat 전에 ask model to perm task. This teaches pattern.

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
Request a specific mat like JSON, YA기계 학습, or markdown 표 to make pars reliable.
User: List three pros three cons microservices. Return only a valid JSON object 함께 keys "pros" "cons", each an array strs.

---

# # 고급 Techniques

# ## Self-Consistency
Generate multiple responses same prompt ( 함께 a temperature > 0) take a majority vote on fal answer. This is especially effective reason tasks.

# ## Tree--Thoughts
탐색 multiple reason paths parallel, evaluate each, choose best one. This is a research-level technique but can be approximated by ask model to "explore alternative solutions."

# ## ReAct (Reason + Act)
Let model terleave reason 함께 tool calls. It can thk, n act (e.g., search 웹, run code), n thk aga based on result.

**Prompt structure:**
You have access to a calculator a search enge. For each step, output:
Thought: (your reason)
Action: (tool name, put)
Observation: (tool output)
... contue until you have fal answer.

# ## Persona Assignment
Assign a specific persona to frame response.

**예시:**
- "You are a Lux kernel developer expla memory 관리 to a new graduate."
- "You are a friendly 영양ist giv general advice to a client."
- "You are a cynical tech critic review a new gadget."

---

# # Parameter Tun

- **Temperature** (0.0 – 1.0+): Controls romness. Lower = more determistic, higher = more creative. Use 0.0–0.3 factual answers; 0.7–1.0 creative writ.
- **Top-p** (nucleus sampl): Cuts f probability mass at a certa cumulative threshold. 0.9 means model samples from top 90% likely tokens. Usually adjust eir temperature or top-p, not both.
- **Max tokens**: Sets maximum output length. Remember to reserve space response 함께 context wdow.
- **Frequency penalty**: Reduces repetition same tokens.
- **Presence penalty**: Encourages model to troduce new topics.

---

# # Common Pitfalls Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p예술 prompt | Prompt too long or overloaded | Shorten; put most important struction at end |
| Output is too verbose | No length constrat | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expla detail" or lower temperature |
| Factual hallucations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" provide a RAG context |
| Inconsistent matt | No explicit mat struction | Ask JSON, markdown table, or bullet list |
| Model answers wrong 언어 | No 언어 struction | Explicitly state "Respond 영어" (or your target 언어) |

---

# # Prompt Templates Common Tasks

# ## Summarisation
Summarise follow text 3 bullet pots. Focus on ma arguments avoid details.

Text: [sert text]


# ## Code Generation
Write a [언어] function that [does X].
Requirements:

Use type hts.

Include a docstr.

Hle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expla [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Brastorm
Generate 10 ideas [topic]. For each idea, give a one-sentence description one potential challenge.

text

# ## Classification
Classify follow customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) a brief reason.

피드백: [sert text]

# ## Translation 함께 Style
Translate follow 영어 text to Spanish. Use an mal tone suitable a social media post.
Text: [sert text]

---

# # Evaluation Prompts

Treat prompts as code: version m, test m, iterate.

- **A/B test** different prompt variants on a held-out set queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scor).
- **Keep a prompt registry** (a simple text file or spreadsheet) 함께 prompt, version, observed permance.

---