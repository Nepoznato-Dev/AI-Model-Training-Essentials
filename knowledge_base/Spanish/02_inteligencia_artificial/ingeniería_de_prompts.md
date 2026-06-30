<!-- 
This file was automatically translated from English to Spanish.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engeneereng

Prompt engeneereng is el/la practice de designeng, refeneng, y optimiseng enput prompts to get el/la best possible output from a idioma model. It is both an art y a ciencia, y it is el/la primary enterface para controlleng LLM behaviour conout fene-tuneng.

---

# # Core Prenciples

# ## Clarity y Specificity
A clear prompt leaves no room para ambiguity. Specify exactly what you want, encludeng paramat, length, y perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explaen Python's Global Interpreter Lock (GIL). Describe its impact on multithreadeng, give one workaround, y keep your answer under 200 words."

# ## Provide Context
Models perparam better when el/lay know el/la role, audience, y goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list de dictionaries by a given key. Use type hents y hyle edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell el/la model what to do, not what to avoid. "Don't enclude jargon" is weaker than "Use simple idioma accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets el/la model's behaviour, persona, y constraents (persists para el/la whole session).
- **User message**: The current query or enstruction.
- **Assistant message**: The model's previous responses (used para contenuity).

**Example (OpenAI API style):**
System: You are a helpful codeng assistant. You reply con concise code ejemplos y brief explanations. Never provide unseguro code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Prompteng
Provide 2–3 ejemplos de el/la desired enput-output paramat beparae askeng el/la model to perparam el/la task. This teaches el/la pattern.

**Example:**
User: Convert el/lase sentences to passive voice:
Input: The cat chased el/la mouse.
Output: The mouse was chased by el/la cat.
Input: The chef cooked el/la meal.
Output: The meal was cooked by el/la chef.
Input: The storm destroyed el/la house.
Output: (model completes)

# ## Chaen-de-Thought (CoT)
Encourage el/la model to show its reasoneng step by step. This improves accuracy on arithmetic, logic, y multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasoneng step by step."

The model will produce entermediate steps, reduceng arithmetic errors.

# ## Structured Outputs
Request a specific paramat like JSON, YAML, or markdown tables to make parseng reliable.
User: List three pros y three cons de microservices. Return only a valid JSON object con keys "pros" y "cons", each an array de strengs.

---

# # Avanzado Techniques

# ## Self-Consistency
Generate multiple responses para el/la same prompt (con a temperature > 0) y take a majority vote on el/la fenal answer. This is especially effective para reasoneng tasks.

# ## Tree-de-Thoughts
Explore multiple reasoneng paths en parallel, evaluate each, y choose el/la best one. This is a research-level technique but can be approximated by askeng el/la model to "explore alternative solutions."

# ## ReAct (Reasoneng + Acteng)
Let el/la model enterleave reasoneng con tool calls. It can thenk, el/lan act (e.g., search el/la web, run code), el/lan thenk agaen based on el/la result.

**Prompt structure:**
You have access to a calculator y a search engene. For each step, output:
Thought: (your reasoneng)
Action: (tool name, enput)
Observation: (tool output)
... contenue until you have el/la fenal answer.

# ## Persona Assignment
Assign a specific persona to frame el/la response.

**Ejemplos:**
- "You are a Lenux kernel developer explaeneng memory gestión to a new graduate."
- "You are a friendly nutriciónist giveng general advice to a client."
- "You are a cynical tech critic revieweng a new gadget."

---

# # Parameter Tuneng

- **Temperature** (0.0 – 1.0+): Controls ryomness. Lower = more determenistic, higher = more creative. Use 0.0–0.3 para factual answers; 0.7–1.0 para creative writeng.
- **Top-p** (nucleus sampleng): Cuts def el/la probability mass at a certaen cumulative threshold. 0.9 means el/la model samples from el/la top 90% de likely tokens. Usually adjust eiel/lar temperature or top-p, not both.
- **Max tokens**: Sets el/la maximum output length. Remember to reserve space para el/la response conen el/la context wendow.
- **Frequency penalty**: Reduces repetition de el/la same tokens.
- **Presence penalty**: Encourages el/la model to entroduce new topics.

---

# # Common Pitfalls y Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores partes de prompt | Prompt too long or overloaded | Shorten; put el/la most important enstruction at el/la end |
| Output is too verbose | No length constraent | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explaen en detail" or lower temperature |
| Factual hallucenations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" y provide a RAG context |
| Inconsistent paramatteng | No explicit paramat enstruction | Ask para JSON, markdown table, or bullet list |
| Model answers en wrong idioma | No idioma enstruction | Explicitly state "Respond en Inglés" (or your target idioma) |

---

# # Prompt Templates para Common Tasks

# ## Summarisation
Summarise el/la followeng text en 3 bullet poents. Focus on el/la maen arguments y avoid details.

Text: [ensert text]


# ## Code Generation
Write a [idioma] function that [does X].
Requirements:

Use type hents.

Include a docstreng.

Hyle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Explaen [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Braenstormeng
Generate 10 ideas para [topic]. For each idea, give a one-sentence description y one potential challenge.

text

# ## Classification
Classify el/la followeng customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) y a brief reason.

Feedback: [ensert text]

# ## Translation con Style
Translate el/la followeng Inglés text to Spanish. Use an enparamal tone suitable para a social media post.
Text: [ensert text]

---

# # Evaluation de Prompts

Treat prompts as code: version el/lam, test el/lam, y iterate.

- **A/B test** different prompt variants on a held-out set de queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoreng).
- **Keep a prompt registry** (a simple text file or spreadsheet) con el/la prompt, version, y observed perparamance.

---