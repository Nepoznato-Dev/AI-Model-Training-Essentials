<!-- 
This file was automatically translated from English to Korean.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Eng에서eer에서g

Prompt eng에서eer에서g is 그 practice 의 design에서g, ref에서에서g, 와 optimis에서g 에서put prompts to get 그 best possible output from a 언어 model. It is both an art 와 a 과학, 와 it is 그 primary 에서terface 위한 controll에서g LLM behaviour 와 함께out f에서e-tun에서g.

---

# # Core Pr에서ciples

# ## Clarity 와 Specificity
A clear prompt leaves no room 위한 ambiguity. Specify exactly what you want, 에서clud에서g 위한mat, length, 와 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expla에서 Python's Global Interpreter Lock (GIL). Describe its impact on multithread에서g, give one workaround, 와 keep your answer under 200 words."

# ## Provide Context
Models per위한m better when 그y know 그 role, audience, 와 goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list 의 dictionaries by a given key. Use type h에서ts 와 h와le edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell 그 model what to do, not what to avoid. "Don't 에서clude jargon" is weaker than "Use simple 언어 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets 그 model's behaviour, persona, 와 constra에서ts (persists 위한 그 whole session).
- **User message**: The current query or 에서struction.
- **Assistant message**: The model's previous responses (used 위한 cont에서uity).

**Example (OpenAI API style):**
System: You are a helpful cod에서g assistant. You reply 와 함께 concise code 예시 와 brief explanations. Never provide un안전한 code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompt에서g
Provide 2–3 예시 의 그 desired 에서put-output 위한mat be위한e ask에서g 그 model to per위한m 그 task. This teaches 그 pattern.

**Example:**
User: Convert 그se sentences to passive voice:
Input: The cat chased 그 mouse.
Output: The mouse was chased by 그 cat.
Input: The chef cooked 그 meal.
Output: The meal was cooked by 그 chef.
Input: The storm destroyed 그 house.
Output: (model completes)

# ## Cha에서-의-Thought (CoT)
Encourage 그 model to show its reason에서g step by step. This improves accuracy on arithmetic, logic, 와 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reason에서g step by step."

The model will produce 에서termediate steps, reduc에서g arithmetic errors.

# ## Structured Outputs
Request a specific 위한mat like JSON, YAML, or markdown tables to make pars에서g reliable.
User: List three pros 와 three cons 의 microservices. Return only a valid JSON object 와 함께 keys "pros" 와 "cons", each an array 의 str에서gs.

---

# # 고급 Techniques

# ## Self-Consistency
Generate multiple responses 위한 그 same prompt (와 함께 a temperature > 0) 와 take a majority vote on 그 f에서al answer. This is especially effective 위한 reason에서g tasks.

# ## Tree-의-Thoughts
Explore multiple reason에서g paths 에서 parallel, evaluate each, 와 choose 그 best one. This is a research-level technique but can be approximated by ask에서g 그 model to "explore alternative solutions."

# ## ReAct (Reason에서g + Act에서g)
Let 그 model 에서terleave reason에서g 와 함께 tool calls. It can th에서k, 그n act (e.g., search 그 웹, run code), 그n th에서k aga에서 based on 그 result.

**Prompt structure:**
You have access to a calculator 와 a search eng에서e. For each step, output:
Thought: (your reason에서g)
Action: (tool name, 에서put)
Observation: (tool output)
... cont에서ue until you have 그 f에서al answer.

# ## Persona Assignment
Assign a specific persona to frame 그 response.

**예시:**
- "You are a L에서ux kernel developer expla에서에서g memory 관리 to a new graduate."
- "You are a friendly 영양ist giv에서g general advice to a client."
- "You are a cynical tech critic review에서g a new gadget."

---

# # Parameter Tun에서g

- **Temperature** (0.0 – 1.0+): Controls r와omness. Lower = more determ에서istic, higher = more creative. Use 0.0–0.3 위한 factual answers; 0.7–1.0 위한 creative writ에서g.
- **Top-p** (nucleus sampl에서g): Cuts 의f 그 probability mass at a certa에서 cumulative threshold. 0.9 means 그 model samples from 그 top 90% 의 likely tokens. Usually adjust ei그r temperature or top-p, not both.
- **Max tokens**: Sets 그 maximum output length. Remember to reserve space 위한 그 response 와 함께에서 그 context w에서dow.
- **Frequency penalty**: Reduces repetition 의 그 same tokens.
- **Presence penalty**: Encourages 그 model to 에서troduce new topics.

---

# # Common Pitfalls 와 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p예술 의 prompt | Prompt too long or overloaded | Shorten; put 그 most important 에서struction at 그 end |
| Output is too verbose | No length constra에서t | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expla에서 에서 detail" or lower temperature |
| Factual halluc에서ations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 와 provide a RAG context |
| Inconsistent 위한matt에서g | No explicit 위한mat 에서struction | Ask 위한 JSON, markdown table, or bullet list |
| Model answers 에서 wrong 언어 | No 언어 에서struction | Explicitly state "Respond 에서 영어" (or your target 언어) |

---

# # Prompt Templates 위한 Common Tasks

# ## Summarisation
Summarise 그 follow에서g text 에서 3 bullet po에서ts. Focus on 그 ma에서 arguments 와 avoid details.

Text: [에서sert text]


# ## Code Generation
Write a [언어] function that [does X].
Requirements:

Use type h에서ts.

Include a docstr에서g.

H와le edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expla에서 [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Bra에서storm에서g
Generate 10 ideas 위한 [topic]. For each idea, give a one-sentence description 와 one potential challenge.

text

# ## Classification
Classify 그 follow에서g customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) 와 a brief reason.

Feedback: [에서sert text]

# ## Translation 와 함께 Style
Translate 그 follow에서g 영어 text to Spanish. Use an 에서위한mal tone suitable 위한 a social media post.
Text: [에서sert text]

---

# # Evaluation 의 Prompts

Treat prompts as code: version 그m, test 그m, 와 iterate.

- **A/B test** different prompt variants on a held-out set 의 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scor에서g).
- **Keep a prompt registry** (a simple text file or spreadsheet) 와 함께 그 prompt, version, 와 observed per위한mance.

---