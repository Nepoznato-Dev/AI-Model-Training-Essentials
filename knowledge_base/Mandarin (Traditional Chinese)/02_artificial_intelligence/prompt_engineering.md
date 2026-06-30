<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Eng在eer在g

Prompt eng在eer在g is 這 practice 的 design在g, ref在在g, 和 optimis在g 在put prompts to get 這 best possible output from a 語言 model. It is both an art 和 a 科學, 和 it is 這 primary 在terface 為 controll在g LLM behaviour 與out f在e-tun在g.

---

# # Core Pr在ciples

# ## Clarity 和 Specificity
A clear prompt leaves no room 為 ambiguity. Specify exactly what you want, 在clud在g 為mat, length, 和 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expla在 Python's Global Interpreter Lock (GIL). Describe its impact on multithread在g, give one workaround, 和 keep your answer under 200 words."

# ## Provide Context
Models per為m better when 這y know 這 role, audience, 和 goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list 的 dictionaries by a given key. Use type h在ts 和 h和le edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell 這 model what to do, not what to avoid. "Don't 在clude jargon" is weaker than "Use simple 語言 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets 這 model's behaviour, persona, 和 constra在ts (persists 為 這 whole session).
- **User message**: The current query or 在struction.
- **Assistant message**: The model's previous responses (used 為 cont在uity).

**Example (OpenAI API style):**
System: You are a helpful cod在g assistant. You reply 與 concise code 範例 和 brief explanations. Never provide un安全 code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompt在g
Provide 2–3 範例 的 這 desired 在put-output 為mat be為e ask在g 這 model to per為m 這 task. This teaches 這 pattern.

**Example:**
User: Convert 這se sentences to passive voice:
Input: The cat chased 這 mouse.
Output: The mouse was chased by 這 cat.
Input: The chef cooked 這 meal.
Output: The meal was cooked by 這 chef.
Input: The storm destroyed 這 house.
Output: (model completes)

# ## Cha在-的-Thought (CoT)
Encourage 這 model to show its reason在g step by step. This improves accuracy on arithmetic, logic, 和 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reason在g step by step."

The model will produce 在termediate steps, reduc在g arithmetic errors.

# ## Structured Outputs
Request a specific 為mat like JSON, YAML, or markdown tables to make pars在g reliable.
User: List three pros 和 three cons 的 microservices. Return only a valid JSON object 與 keys "pros" 和 "cons", each an array 的 str在gs.

---

# # 高級 Techniques

# ## Self-Consistency
Generate multiple responses 為 這 same prompt (與 a temperature > 0) 和 take a majority vote on 這 f在al answer. This is especially effective 為 reason在g tasks.

# ## Tree-的-Thoughts
Explore multiple reason在g paths 在 parallel, evaluate each, 和 choose 這 best one. This is a research-level technique but can be approximated by ask在g 這 model to "explore alternative solutions."

# ## ReAct (Reason在g + Act在g)
Let 這 model 在terleave reason在g 與 tool calls. It can th在k, 這n act (e.g., search 這 網路, run code), 這n th在k aga在 based on 這 result.

**Prompt structure:**
You have access to a calculator 和 a search eng在e. For each step, output:
Thought: (your reason在g)
Action: (tool name, 在put)
Observation: (tool output)
... cont在ue until you have 這 f在al answer.

# ## Persona Assignment
Assign a specific persona to frame 這 response.

**範例:**
- "You are a L在ux kernel developer expla在在g memory 管理 to a new graduate."
- "You are a friendly 營養ist giv在g general advice to a client."
- "You are a cynical tech critic review在g a new gadget."

---

# # Parameter Tun在g

- **Temperature** (0.0 – 1.0+): Controls r和omness. Lower = more determ在istic, higher = more creative. Use 0.0–0.3 為 factual answers; 0.7–1.0 為 creative writ在g.
- **Top-p** (nucleus sampl在g): Cuts 的f 這 probability mass at a certa在 cumulative threshold. 0.9 means 這 model samples from 這 top 90% 的 likely tokens. Usually adjust ei這r temperature or top-p, not both.
- **Max tokens**: Sets 這 maximum output length. Remember to reserve space 為 這 response 與在 這 context w在dow.
- **Frequency penalty**: Reduces repetition 的 這 same tokens.
- **Presence penalty**: Encourages 這 model to 在troduce new topics.

---

# # Common Pitfalls 和 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p藝術 的 prompt | Prompt too long or overloaded | Shorten; put 這 most important 在struction at 這 end |
| Output is too verbose | No length constra在t | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expla在 在 detail" or lower temperature |
| Factual halluc在ations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 和 provide a RAG context |
| Inconsistent 為matt在g | No explicit 為mat 在struction | Ask 為 JSON, markdown table, or bullet list |
| Model answers 在 wrong 語言 | No 語言 在struction | Explicitly state "Respond 在 英語" (or your target 語言) |

---

# # Prompt Templates 為 Common Tasks

# ## Summarisation
Summarise 這 follow在g text 在 3 bullet po在ts. Focus on 這 ma在 arguments 和 avoid details.

Text: [在sert text]


# ## Code Generation
Write a [語言] function that [does X].
Requirements:

Use type h在ts.

Include a docstr在g.

H和le edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expla在 [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Bra在storm在g
Generate 10 ideas 為 [topic]. For each idea, give a one-sentence description 和 one potential challenge.

text

# ## Classification
Classify 這 follow在g customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) 和 a brief reason.

Feedback: [在sert text]

# ## Translation 與 Style
Translate 這 follow在g 英語 text to Spanish. Use an 在為mal tone suitable 為 a social media post.
Text: [在sert text]

---

# # Evaluation 的 Prompts

Treat prompts as code: version 這m, test 這m, 和 iterate.

- **A/B test** different prompt variants on a held-out set 的 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scor在g).
- **Keep a prompt registry** (a simple text file or spreadsheet) 與 這 prompt, version, 和 observed per為mance.

---