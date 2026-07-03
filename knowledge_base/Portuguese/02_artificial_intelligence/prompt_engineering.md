<!-- 
This file was automatically translated from English to Portuguese.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is o/a practice de designing, refining, e optimising input prompts to get o/a best possible output from a Idioma model. It is both an art e a Ciência, e it is o/a primary interface para controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity e Specificity
A clear prompt leaves no room para ambiguity. Specify exactly what you want, including format, length, e perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, e keep your answer under 200 words."

### Provide Context
Models perform better when they know o/a role, audience, e goal.

**Without context:**
> "Write a function to sort a list."

**com context:**
> "You are a senior Python developer. Write a function to sort a list de dictionaries by a given key. Use type hints e handle edge cases. o/a audience is junior developers."

### Use Positive Instructions
Tell o/a model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple Idioma accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs Suporte a multi-turn structure:

- **System message**: Sets o/a model's behaviour, persona, e constraints (persists para o/a whole session).
- **User message**: o/a current query or instruction.
- **Assistant message**: o/a model's previous responses (used para continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply com concise code Exemplos e brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 Exemplos de o/a desired input-output format before asking o/a model to perform o/a task. This teaches o/a pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: o/a cat chased o/a mouse.
Output: o/a mouse was chased by o/a cat.
Input: o/a chef cooked o/a meal.
Output: o/a meal was cooked by o/a chef.
Input: o/a storm destroyed o/a house.
Output: (model completes)

### Chain-de-Thought (CoT)
Encourage o/a model to show its reasoning step by step. This improves accuracy on arithmetic, logic, e multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**com CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

o/a model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros e three cons de microservices. Return only a valid JSON object com keys "pros" e "cons", each an array de strings.

---

## Avançado Techniques

### Self-Consistency
Generate multiple responses para o/a same prompt (com a temperature > 0) e take a majority vote on o/a final answer. This is especially effective para reasoning tasks.

### Tree-de-Thoughts
Explore multiple reasoning paths em parallel, evaluate each, e choose o/a best one. This is a research-level technique but can be approximated by asking o/a model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let o/a model interleave reasoning com tool calls. It can think, then act (e.g., search o/a Web, run code), then think again based on o/a result.

**Prompt structure:**
You have access to a calculator e a search engine. para each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have o/a final answer.

### Persona Assignment
Assign a specific persona to frame o/a response.

**Exemplos:**
- "You are a Linux kernel developer explaining memory Gerenciamento to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 para factual answers; 0.7–1.0 para creative writing.
- **Top-p** (nucleus sampling): Cuts off o/a probability mass at a certain cumulative threshold. 0.9 means o/a model samples from o/a top 90% de likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets o/a maximum output length. Remember to reserve space para o/a response within o/a context window.
- **Frequency penalty**: Reduces repetition de o/a same tokens.
- **Presence penalty**: Encourages o/a model to introduce new topics.

---

## Common Pitfalls e Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts de prompt | Prompt too long or overloaded | Shorten; put o/a most important instruction at o/a end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain em detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" e provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask para JSON, markdown table, or bullet list |
| Model answers em wrong Idioma | No Idioma instruction | Explicitly state "Respond em Inglês" (or your target Idioma) |

---

## Prompt Templates para Common Tasks

### Summarisation
Summarise o/a following text em 3 bullet points. Focus on o/a main arguments e avoid details.

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
Generate 10 ideas para [topic]. para each idea, give a one-sentence description e one potential challenge.

text

### Classification
Classify o/a following customer Feedback as [positive, neutral, negative].
Provide a confidence score (0-100) e a brief reason.

Feedback: [insert text]

### Translation com Style
Translate o/a following Inglês text to Spanish. Use an informal tone suitable para a social media post.
Text: [insert text]

---

## Evaluation de Prompts

Treat prompts as code: version them, test them, e iterate.

- **A/B test** different prompt variants on a held-out set de queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) com o/a prompt, version, e observed Desempenho.

---