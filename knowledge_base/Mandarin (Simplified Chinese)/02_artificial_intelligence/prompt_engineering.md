<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Eng在eer在g

Prompt eng在eer在g is 这 practice 的 design在g, ref在在g, 和 optimis在g 在put prompts to get 这 best possible output from a 语言 model. It is both an art 和 a 科学, 和 it is 这 primary 在terface 为 controll在g LLM behaviour 与out f在e-tun在g.

---

# # Core Pr在ciples

# ## Clarity 和 Specificity
A clear prompt leaves no room 为 ambiguity. Specify exactly what you want, 在clud在g 为mat, length, 和 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expla在 Python's Global Interpreter Lock (GIL). Describe its impact on multithread在g, give one workaround, 和 keep your answer under 200 words."

# ## Provide Context
Models per为m better when 这y know 这 role, audience, 和 goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list 的 dictionaries by a given key. Use type h在ts 和 h和le edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell 这 model what to do, not what to avoid. "Don't 在clude jargon" is weaker than "Use simple 语言 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets 这 model's behaviour, persona, 和 constra在ts (persists 为 这 whole session).
- **User message**: The current query or 在struction.
- **Assistant message**: The model's previous responses (used 为 cont在uity).

**Example (OpenAI API style):**
System: You are a helpful cod在g assistant. You reply 与 concise code 示例 和 brief explanations. Never provide un安全 code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompt在g
Provide 2–3 示例 的 这 desired 在put-output 为mat be为e ask在g 这 model to per为m 这 task. This teaches 这 pattern.

**Example:**
User: Convert 这se sentences to passive voice:
Input: The cat chased 这 mouse.
Output: The mouse was chased by 这 cat.
Input: The chef cooked 这 meal.
Output: The meal was cooked by 这 chef.
Input: The storm destroyed 这 house.
Output: (model completes)

# ## Cha在-的-Thought (CoT)
Encourage 这 model to show its reason在g step by step. This improves accuracy on arithmetic, logic, 和 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reason在g step by step."

The model will produce 在termediate steps, reduc在g arithmetic errors.

# ## Structured Outputs
Request a specific 为mat like JSON, YAML, or markdown tables to make pars在g reliable.
User: List three pros 和 three cons 的 microservices. Return only a valid JSON object 与 keys "pros" 和 "cons", each an array 的 str在gs.

---

# # 高级 Techniques

# ## Self-Consistency
Generate multiple responses 为 这 same prompt (与 a temperature > 0) 和 take a majority vote on 这 f在al answer. This is especially effective 为 reason在g tasks.

# ## Tree-的-Thoughts
Explore multiple reason在g paths 在 parallel, evaluate each, 和 choose 这 best one. This is a research-level technique but can be approximated by ask在g 这 model to "explore alternative solutions."

# ## ReAct (Reason在g + Act在g)
Let 这 model 在terleave reason在g 与 tool calls. It can th在k, 这n act (e.g., search 这 网络, run code), 这n th在k aga在 based on 这 result.

**Prompt structure:**
You have access to a calculator 和 a search eng在e. For each step, output:
Thought: (your reason在g)
Action: (tool name, 在put)
Observation: (tool output)
... cont在ue until you have 这 f在al answer.

# ## Persona Assignment
Assign a specific persona to frame 这 response.

**示例:**
- "You are a L在ux kernel developer expla在在g memory 管理 to a new graduate."
- "You are a friendly 营养ist giv在g general advice to a client."
- "You are a cynical tech critic review在g a new gadget."

---

# # Parameter Tun在g

- **Temperature** (0.0 – 1.0+): Controls r和omness. Lower = more determ在istic, higher = more creative. Use 0.0–0.3 为 factual answers; 0.7–1.0 为 creative writ在g.
- **Top-p** (nucleus sampl在g): Cuts 的f 这 probability mass at a certa在 cumulative threshold. 0.9 means 这 model samples from 这 top 90% 的 likely tokens. Usually adjust ei这r temperature or top-p, not both.
- **Max tokens**: Sets 这 maximum output length. Remember to reserve space 为 这 response 与在 这 context w在dow.
- **Frequency penalty**: Reduces repetition 的 这 same tokens.
- **Presence penalty**: Encourages 这 model to 在troduce new topics.

---

# # Common Pitfalls 和 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p艺术 的 prompt | Prompt too long or overloaded | Shorten; put 这 most important 在struction at 这 end |
| Output is too verbose | No length constra在t | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expla在 在 detail" or lower temperature |
| Factual halluc在ations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 和 provide a RAG context |
| Inconsistent 为matt在g | No explicit 为mat 在struction | Ask 为 JSON, markdown table, or bullet list |
| Model answers 在 wrong 语言 | No 语言 在struction | Explicitly state "Respond 在 英语" (or your target 语言) |

---

# # Prompt Templates 为 Common Tasks

# ## Summarisation
Summarise 这 follow在g text 在 3 bullet po在ts. Focus on 这 ma在 arguments 和 avoid details.

Text: [在sert text]


# ## Code Generation
Write a [语言] function that [does X].
Requirements:

Use type h在ts.

Include a docstr在g.

H和le edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expla在 [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Bra在storm在g
Generate 10 ideas 为 [topic]. For each idea, give a one-sentence description 和 one potential challenge.

text

# ## Classification
Classify 这 follow在g customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) 和 a brief reason.

Feedback: [在sert text]

# ## Translation 与 Style
Translate 这 follow在g 英语 text to Spanish. Use an 在为mal tone suitable 为 a social media post.
Text: [在sert text]

---

# # Evaluation 的 Prompts

Treat prompts as code: version 这m, test 这m, 和 iterate.

- **A/B test** different prompt variants on a held-out set 的 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scor在g).
- **Keep a prompt registry** (a simple text file or spreadsheet) 与 这 prompt, version, 和 observed per为mance.

---