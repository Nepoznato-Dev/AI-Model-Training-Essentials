<!-- 
This file was automatically translated from English to Spanish.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is el/la practice de designing, refining, y optimising input prompts to get el/la best possible output from a Idioma model. It is both an art y a Ciencia, y it is el/la primary interface para controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity y Specificity
A clear prompt leaves no room para ambiguity. Specify exactly what you want, including format, length, y perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, y keep your answer under 200 words."

### Provide Context
Models perform better when they know el/la role, audience, y goal.

**Without context:**
> "Write a function to sort a list."

**con context:**
> "You are a senior Python developer. Write a function to sort a list de dictionaries by a given key. Use type hints y handle edge cases. el/la audience is junior developers."

### Use Positive Instructions
Tell el/la model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple Idioma accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets el/la model's behaviour, persona, y constraints (persists para el/la whole session).
- **User message**: el/la current query or instruction.
- **Assistant message**: el/la model's previous responses (used para continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply con concise code Ejemplos y brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 Ejemplos de el/la desired input-output format before asking el/la model to perform el/la task. This teaches el/la pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: el/la cat chased el/la mouse.
Output: el/la mouse was chased by el/la cat.
Input: el/la chef cooked el/la meal.
Output: el/la meal was cooked by el/la chef.
Input: el/la storm destroyed el/la house.
Output: (model completes)

### Chain-de-Thought (CoT)
Encourage el/la model to show its reasoning step by step. This improves accuracy on arithmetic, logic, y multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**con CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

el/la model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros y three cons de microservices. Return only a valid JSON object con keys "pros" y "cons", each an array de strings.

---

## Avanzado Techniques

### Self-Consistency
Generate multiple responses para el/la same prompt (con a temperature > 0) y take a majority vote on el/la final answer. This is especially effective para reasoning tasks.

### Tree-de-Thoughts
Explore multiple reasoning paths en parallel, evaluate each, y choose el/la best one. This is a research-level technique but can be approximated by asking el/la model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let el/la model interleave reasoning con tool calls. It can think, then act (e.g., search el/la Web, run code), then think again based on el/la result.

**Prompt structure:**
You have access to a calculator y a search engine. para each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have el/la final answer.

### Persona Assignment
Assign a specific persona to frame el/la response.

**Ejemplos:**
- "You are a Linux kernel developer explaining memory Gestión to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 para factual answers; 0.7–1.0 para creative writing.
- **Top-p** (nucleus sampling): Cuts off el/la probability mass at a certain cumulative threshold. 0.9 means el/la model samples from el/la top 90% de likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets el/la maximum output length. Remember to reserve space para el/la response within el/la context window.
- **Frequency penalty**: Reduces repetition de el/la same tokens.
- **Presence penalty**: Encourages el/la model to introduce new topics.

---

## Common Pitfalls y Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts de prompt | Prompt too long or overloaded | Shorten; put el/la most important instruction at el/la end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain en detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" y provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask para JSON, markdown table, or bullet list |
| Model answers en wrong Idioma | No Idioma instruction | Explicitly state "Respond en Inglés" (or your target Idioma) |

---

## Prompt Templates para Common Tasks

### Summarisation
Summarise el/la following text en 3 bullet points. Focus on el/la main arguments y avoid details.

Text: [insert text]


### Code Generation
Write a [Idioma] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas para [topic]. para each idea, give a one-sentence description y one potential challenge.

text

### Classification
Classify el/la following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) y a brief reason.

Feedback: [insert text]

### Translation con Style
Translate el/la following Inglés text to Spanish. Use an informal tone suitable para a social media post.
Text: [insert text]

---

## Evaluation de Prompts

Treat prompts as code: version them, test them, y iterate.

- **A/B test** different prompt variants on a held-out set de queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) con el/la prompt, version, y observed Rendimiento.

---