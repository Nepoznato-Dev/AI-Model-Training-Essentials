<!-- 
This file was automatically translated from English to Arabic.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is ال practice من designing, refining, و optimising input prompts to get ال best possible output from a اللغة model. It is both an art و a العلوم, و it is ال primary interface لأجل controlling LLM behaviour without fine-tuning.

---

# # Core Principles

# ## Clarity و Specificity
A clear prompt leaves no room لأجل ambiguity. Specify exactly what you want, including format, length, و perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, و keep your answer under 200 words."

# ## Provide Context
Models perform better when they know ال role, audience, و goal.

**Without context:**
> "Write a function to sort a list."

**مع context:**
> "You are a senior Python developer. Write a function to sort a list من dictionaries by a given key. Use type hints و handle edge cases. ال audience is junior developers."

# ## Use Positive Instructions
Tell ال model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple اللغة accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets ال model's behaviour, persona, و constraints (persists لأجل ال whole session).
- **User message**: ال current query or instruction.
- **Assistant message**: ال model's previous responses (used لأجل continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply مع concise code أمثلة و brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompting
Provide 2–3 أمثلة من ال desired input-output format before asking ال model to perform ال task. This teaches ال pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: ال cat chased ال mouse.
Output: ال mouse was chased by ال cat.
Input: ال chef cooked ال meal.
Output: ال meal was cooked by ال chef.
Input: ال storm destroyed ال house.
Output: (model completes)

# ## Chain-من-Thought (CoT)
Encourage ال model to show its reasoning step by step. This improves accuracy on arithmetic, logic, و multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**مع CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

ال model will produce intermediate steps, reducing arithmetic errors.

# ## Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros و three cons من microservices. Return only a valid JSON object مع keys "pros" و "cons", each an array من strings.

---

# # متقدم Techniques

# ## Self-Consistency
Generate multiple responses لأجل ال same prompt (مع a temperature > 0) و take a majority vote on ال final answer. This is especially effective لأجل reasoning tasks.

# ## Tree-من-Thoughts
Explore multiple reasoning paths في parallel, evaluate each, و choose ال best one. This is a research-level technique but can be approximated by asking ال model to "explore alternative solutions."

# ## ReAct (Reasoning + Acting)
Let ال model interleave reasoning مع tool calls. It can think, then act (e.g., search ال الويب, run code), then think again based on ال result.

**Prompt structure:**
You have access to a calculator و a search engine. لأجل each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have ال final answer.

# ## Persona Assignment
Assign a specific persona to frame ال response.

**أمثلة:**
- "You are a Linux kernel developer explaining memory الإدارة to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

# # Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 لأجل factual answers; 0.7–1.0 لأجل creative writing.
- **Top-p** (nucleus sampling): Cuts off ال probability mass at a certain cumulative threshold. 0.9 means ال model samples from ال top 90% من likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets ال maximum output length. Remember to reserve space لأجل ال response within ال context window.
- **Frequency penalty**: Reduces repetition من ال same tokens.
- **Presence penalty**: Encourages ال model to introduce new topics.

---

# # Common Pitfalls و Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts من prompt | Prompt too long or overloaded | Shorten; put ال most important instruction at ال end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain في detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" و provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask لأجل JSON, markdown table, or bullet list |
| Model answers في wrong اللغة | No اللغة instruction | Explicitly state "Respond في الإنجليزية" (or your target اللغة) |

---

# # Prompt Templates لأجل Common Tasks

# ## Summarisation
Summarise ال following text في 3 bullet points. Focus on ال main arguments و avoid details.

Text: [insert text]


# ## Code Generation
Write a [اللغة] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Brainstorming
Generate 10 ideas لأجل [topic]. لأجل each idea, give a one-sentence description و one potential challenge.

text

# ## Classification
Classify ال following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) و a brief reason.

Feedback: [insert text]

# ## Translation مع Style
Translate ال following الإنجليزية text to Spanish. Use an informal tone suitable لأجل a social media post.
Text: [insert text]

---

# # Evaluation من Prompts

Treat prompts as code: version them, test them, و iterate.

- **A/B test** different prompt variants on a held-out set من queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) مع ال prompt, version, و observed الأداء.

---