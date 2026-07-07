<!-- 
This file was automatically translated from English to French.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Ingenierie des prompts

Prompt engineering is le/la practice de designing, refining, et optimising input prompts to get le/la best possible output from a Langue model. It is both an art et a Science, et it is le/la primary interface pour controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity et Specificity
A clear prompt leaves no room pour ambiguity. Specify exactly what you want, including format, length, et perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, et keep your answer under 200 words."

### Provide Context
Models perform better when they know le/la role, audience, et goal.

**Without context:**
> "Write a function to sort a list."

**avec context:**
> "You are a senior Python developer. Write a function to sort a list de dictionaries by a given key. Use type hints et handle edge cases. le/la audience is junior developers."

### Use Positive Instructions
Tell le/la model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple Langue accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs Assistance a multi-turn structure:

- **System message**: Sets le/la model's behaviour, persona, et constraints (persists pour le  whole session).
- **User message**: le/la current query or instruction.
- **Assistant message**: le/la model's previous responses (used pour continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply avec concise code Exemples et brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 Exemples du  desired input-output format before asking le/la model to perform le/la task. This teaches le/la pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: le/la cat chased le/la mouse.
Output: le/la mouse was chased by le/la cat.
Input: le/la chef cooked le/la meal.
Output: le/la meal was cooked by le/la chef.
Input: le/la storm destroyed le/la house.
Output: (model completes)

### Chain-de-Thought (CoT)
Encourage le/la model to show its reasoning step by step. This improves accuracy on arithmetic, logic, et multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**avec CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

le/la model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros et three cons de microservices. Return only a valid JSON object avec keys "pros" et "cons", each an array de strings.

---

## Avancé Techniques

### Self-Consistency
Generate multiple responses pour le  same prompt (avec a temperature > 0) et take a majority vote on le/la final answer. This is especially effective pour reasoning tasks.

### Tree-de-Thoughts
Explore multiple reasoning paths dans parallel, evaluate each, et choose le/la best one. This is a research-level technique but can be approximated by asking le/la model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let le/la model interleave reasoning avec tool calls. It can think, then act (e.g., search le/la Web, run code), then think again based on le/la result.

**Prompt structure:**
You have access to a calculator et a search engine. pour each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have le/la final answer.

### Persona Assignment
Assign a specific persona to frame le/la response.

**Exemples:**
- "You are a Linux kernel developer explaining memory gestion to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 pour factual answers; 0.7–1.0 pour creative writing.
- **Top-p** (nucleus sampling): Cuts off le/la probability mass at a certain cumulative threshold. 0.9 means le/la model samples from le/la top 90% de likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets le/la maximum output length. Remember to reserve space pour le  response within le/la context window.
- **Frequency penalty**: Reduces repetition du  same tokens.
- **Presence penalty**: Encourages le/la model to introduce new topics.

---

## Common Pitfalls et Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts de prompt | Prompt too long or overloaded | Shorten; put le/la most important instruction at le/la end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain dans detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" et provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask pour JSON, markdown table, or bullet list |
| Model answers dans wrong Langue | No Langue instruction | Explicitly state "Respond dans Anglais" (or your target Langue) |

---

## Prompt Templates pour Common Tasks

### Summarisation
Summarise le/la following text dans 3 bullet points. Focus on le/la main arguments et avoid details.

Text: [insert text]


### Code Generation
Write a [Langue] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas pour [topic]. pour each idea, give a one-sentence description et one potential challenge.

text

### Classification
Classify le/la following customer Retour as [positive, neutral, negative].
Provide a confidence score (0-100) et a brief reason.

Retour: [insert text]

### Translation avec Style
Translate le/la following Anglais text to Spanish. Use an informal tone suitable pour a social media post.
Text: [insert text]

---

## Evaluation de Prompts

Treat prompts as code: version them, test them, et iterate.

- **A/B test** different prompt variants on a held-out set de queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) avec le  prompt, version, et observed Performance.

---