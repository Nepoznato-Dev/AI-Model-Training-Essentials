<!-- 
This file was automatically translated from English to French.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engdanseerdansg

Prompt engdanseerdansg is le/la practice de designdansg, refdansdansg, et optimisdansg dansput prompts to get le/la best possible output from a langue model. It is both an art et a science, et it is le/la primary dansterface pour controlldansg LLM behaviour avecout fdanse-tundansg.

---

# # Core Prdansciples

# ## Clarity et Specificity
A clear prompt leaves no room pour ambiguity. Specify exactly what you want, danscluddansg pourmat, length, et perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Expladans Python's Global Interpreter Lock (GIL). Describe its impact on multithreaddansg, give one workaround, et keep your answer under 200 words."

# ## Provide Context
Models perpourm better when le/lay know le/la role, audience, et goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list de dictionaries by a given key. Use type hdansts et hetle edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell le/la model what to do, not what to avoid. "Don't dansclude jargon" is weaker than "Use simple langue accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets le/la model's behaviour, persona, et constradansts (persists pour le/la whole session).
- **User message**: The current query or dansstruction.
- **Assistant message**: The model's previous responses (used pour contdansuity).

**Example (OpenAI API style):**
System: You are a helpful coddansg assistant. You reply avec concise code exemples et brief explanations. Never provide unsûr code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Promptdansg
Provide 2–3 exemples de le/la desired dansput-output pourmat bepoure askdansg le/la model to perpourm le/la task. This teaches le/la pattern.

**Example:**
User: Convert le/lase sentences to passive voice:
Input: The cat chased le/la mouse.
Output: The mouse was chased by le/la cat.
Input: The chef cooked le/la meal.
Output: The meal was cooked by le/la chef.
Input: The storm destroyed le/la house.
Output: (model completes)

# ## Chadans-de-Thought (CoT)
Encourage le/la model to show its reasondansg step by step. This improves accuracy on arithmetic, logic, et multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasondansg step by step."

The model will produce danstermediate steps, reducdansg arithmetic errors.

# ## Structured Outputs
Request a specific pourmat like JSON, YAML, or markdown tables to make parsdansg reliable.
User: List three pros et three cons de microservices. Return only a valid JSON object avec keys "pros" et "cons", each an array de strdansgs.

---

# # Avancé Techniques

# ## Self-Consistency
Generate multiple responses pour le/la same prompt (avec a temperature > 0) et take a majority vote on le/la fdansal answer. This is especially effective pour reasondansg tasks.

# ## Tree-de-Thoughts
Explore multiple reasondansg paths dans parallel, evaluate each, et choose le/la best one. This is a research-level technique but can be approximated by askdansg le/la model to "explore alternative solutions."

# ## ReAct (Reasondansg + Actdansg)
Let le/la model dansterleave reasondansg avec tool calls. It can thdansk, le/lan act (e.g., search le/la web, run code), le/lan thdansk agadans based on le/la result.

**Prompt structure:**
You have access to a calculator et a search engdanse. For each step, output:
Thought: (your reasondansg)
Action: (tool name, dansput)
Observation: (tool output)
... contdansue until you have le/la fdansal answer.

# ## Persona Assignment
Assign a specific persona to frame le/la response.

**Exemples:**
- "You are a Ldansux kernel developer expladansdansg memory gestion to a new graduate."
- "You are a friendly nutritionist givdansg general advice to a client."
- "You are a cynical tech critic reviewdansg a new gadget."

---

# # Parameter Tundansg

- **Temperature** (0.0 – 1.0+): Controls retomness. Lower = more determdansistic, higher = more creative. Use 0.0–0.3 pour factual answers; 0.7–1.0 pour creative writdansg.
- **Top-p** (nucleus sampldansg): Cuts def le/la probability mass at a certadans cumulative threshold. 0.9 means le/la model samples from le/la top 90% de likely tokens. Usually adjust eile/lar temperature or top-p, not both.
- **Max tokens**: Sets le/la maximum output length. Remember to reserve space pour le/la response avecdans le/la context wdansdow.
- **Frequency penalty**: Reduces repetition de le/la same tokens.
- **Presence penalty**: Encourages le/la model to danstroduce new topics.

---

# # Common Pitfalls et Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts de prompt | Prompt too long or overloaded | Shorten; put le/la most important dansstruction at le/la end |
| Output is too verbose | No length constradanst | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Expladans dans detail" or lower temperature |
| Factual hallucdansations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" et provide a RAG context |
| Inconsistent pourmattdansg | No explicit pourmat dansstruction | Ask pour JSON, markdown table, or bullet list |
| Model answers dans wrong langue | No langue dansstruction | Explicitly state "Respond dans Anglais" (or your target langue) |

---

# # Prompt Templates pour Common Tasks

# ## Summarisation
Summarise le/la followdansg text dans 3 bullet podansts. Focus on le/la madans arguments et avoid details.

Text: [danssert text]


# ## Code Generation
Write a [langue] function that [does X].
Requirements:

Use type hdansts.

Include a docstrdansg.

Hetle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Expladans [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Bradansstormdansg
Generate 10 ideas pour [topic]. For each idea, give a one-sentence description et one potential challenge.

text

# ## Classification
Classify le/la followdansg customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) et a brief reason.

Feedback: [danssert text]

# ## Translation avec Style
Translate le/la followdansg Anglais text to Spanish. Use an danspourmal tone suitable pour a social media post.
Text: [danssert text]

---

# # Evaluation de Prompts

Treat prompts as code: version le/lam, test le/lam, et iterate.

- **A/B test** different prompt variants on a held-out set de queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scordansg).
- **Keep a prompt registry** (a simple text file or spreadsheet) avec le/la prompt, version, et observed perpourmance.

---