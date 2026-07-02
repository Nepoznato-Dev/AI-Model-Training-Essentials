<!-- 
This file was automatically translated from English to German.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is der/die/das practice von designing, refining, und optimising input prompts to get der/die/das best possible output from a Sprache model. It is both an art und a Wissenschaft, und it is der/die/das primary interface für controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity und Specificity
A clear prompt leaves no room für ambiguity. Specify exactly what you want, including format, length, und perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, und keep your answer under 200 words."

### Provide Context
Models perform better when they know der/die/das role, audience, und goal.

**Without context:**
> "Write a function to sort a list."

**mit context:**
> "You are a senior Python developer. Write a function to sort a list von dictionaries by a given key. Use type hints und handle edge cases. der/die/das audience is junior developers."

### Use Positive Instructions
Tell der/die/das model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple Sprache accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets der/die/das model's behaviour, persona, und constraints (persists für der/die/das whole session).
- **User message**: der/die/das current query or instruction.
- **Assistant message**: der/die/das model's previous responses (used für continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply mit concise code Beispiele und brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 Beispiele von der/die/das desired input-output format before asking der/die/das model to perform der/die/das task. This teaches der/die/das pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: der/die/das cat chased der/die/das mouse.
Output: der/die/das mouse was chased by der/die/das cat.
Input: der/die/das chef cooked der/die/das meal.
Output: der/die/das meal was cooked by der/die/das chef.
Input: der/die/das storm destroyed der/die/das house.
Output: (model completes)

### Chain-von-Thought (CoT)
Encourage der/die/das model to show its reasoning step by step. This improves accuracy on arithmetic, logic, und multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**mit CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

der/die/das model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros und three cons von microservices. Return only a valid JSON object mit keys "pros" und "cons", each an array von strings.

---

## Fortgeschritten Techniques

### Self-Consistency
Generate multiple responses für der/die/das same prompt (mit a temperature > 0) und take a majority vote on der/die/das final answer. This is especially effective für reasoning tasks.

### Tree-von-Thoughts
Explore multiple reasoning paths in parallel, evaluate each, und choose der/die/das best one. This is a research-level technique but can be approximated by asking der/die/das model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let der/die/das model interleave reasoning mit tool calls. It can think, then act (e.g., search der/die/das Web, run code), then think again based on der/die/das result.

**Prompt structure:**
You have access to a calculator und a search engine. für each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have der/die/das final answer.

### Persona Assignment
Assign a specific persona to frame der/die/das response.

**Beispiele:**
- "You are a Linux kernel developer explaining memory Verwaltung to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 für factual answers; 0.7–1.0 für creative writing.
- **Top-p** (nucleus sampling): Cuts off der/die/das probability mass at a certain cumulative threshold. 0.9 means der/die/das model samples from der/die/das top 90% von likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets der/die/das maximum output length. Remember to reserve space für der/die/das response within der/die/das context window.
- **Frequency penalty**: Reduces repetition von der/die/das same tokens.
- **Presence penalty**: Encourages der/die/das model to introduce new topics.

---

## Common Pitfalls und Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts von prompt | Prompt too long or overloaded | Shorten; put der/die/das most important instruction at der/die/das end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain in detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" und provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask für JSON, markdown table, or bullet list |
| Model answers in wrong Sprache | No Sprache instruction | Explicitly state "Respond in Englisch" (or your target Sprache) |

---

## Prompt Templates für Common Tasks

### Summarisation
Summarise der/die/das following text in 3 bullet points. Focus on der/die/das main arguments und avoid details.

Text: [insert text]


### Code Generation
Write a [Sprache] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas für [topic]. für each idea, give a one-sentence description und one potential challenge.

text

### Classification
Classify der/die/das following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) und a brief reason.

Feedback: [insert text]

### Translation mit Style
Translate der/die/das following Englisch text to Spanish. Use an informal tone suitable für a social media post.
Text: [insert text]

---

## Evaluation von Prompts

Treat prompts as code: version them, test them, und iterate.

- **A/B test** different prompt variants on a held-out set von queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) mit der/die/das prompt, version, und observed Leistung.

---