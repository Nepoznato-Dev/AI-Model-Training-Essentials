<!-- 
This file was automatically translated from English to Russian.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is the practice из designing, refining, и optimising input prompts to get the best possible output from a Язык model. It is both an art и a Наука, и it is the primary interface для controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity и Specificity
A clear prompt leaves no room для ambiguity. Specify exactly what you want, including format, length, и perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, и keep your answer under 200 words."

### Provide Context
Models perform better when they know the role, audience, и goal.

**Without context:**
> "Write a function to sort a list."

**с context:**
> "You are a senior Python developer. Write a function to sort a list из dictionaries by a given key. Use type hints и handle edge cases. the audience is junior developers."

### Use Positive Instructions
Tell the model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple Язык accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs Поддержка a multi-turn structure:

- **System message**: Sets the model's behaviour, persona, и constraints (persists для the whole session).
- **User message**: the current query or instruction.
- **Assistant message**: the model's previous responses (used для continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply с concise code Примеры и brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 Примеры из the desired input-output format before asking the model to perform the task. This teaches the pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: the cat chased the mouse.
Output: the mouse was chased by the cat.
Input: the chef cooked the meal.
Output: the meal was cooked by the chef.
Input: the storm destroyed the house.
Output: (model completes)

### Chain-из-Thought (CoT)
Encourage the model to show its reasoning step by step. This improves accuracy on arithmetic, logic, и multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**с CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

the model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros и three cons из microservices. Return only a valid JSON object с keys "pros" и "cons", each an array из strings.

---

## Продвинутый Techniques

### Self-Consistency
Generate multiple responses для the same prompt (с a temperature > 0) и take a majority vote on the final answer. This is especially effective для reasoning tasks.

### Tree-из-Thoughts
Explore multiple reasoning paths в parallel, evaluate each, и choose the best one. This is a research-level technique but can be approximated by asking the model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let the model interleave reasoning с tool calls. It can think, then act (e.g., search the Веб, run code), then think again based on the result.

**Prompt structure:**
You have access to a calculator и a search engine. для each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### Persona Assignment
Assign a specific persona to frame the response.

**Примеры:**
- "You are a Linux kernel developer explaining memory Управление to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 для factual answers; 0.7–1.0 для creative writing.
- **Top-p** (nucleus sampling): Cuts off the probability mass at a certain cumulative threshold. 0.9 means the model samples from the top 90% из likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets the maximum output length. Remember to reserve space для the response within the context window.
- **Frequency penalty**: Reduces repetition из the same tokens.
- **Presence penalty**: Encourages the model to introduce new topics.

---

## Common Pitfalls и Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts из prompt | Prompt too long or overloaded | Shorten; put the most important instruction at the end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain в detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" и provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask для JSON, markdown table, or bullet list |
| Model answers в wrong Язык | No Язык instruction | Explicitly state "Respond в Английский" (or your target Язык) |

---

## Prompt Templates для Common Tasks

### Summarisation
Summarise the following text в 3 bullet points. Focus on the main arguments и avoid details.

Text: [insert text]


### Code Generation
Write a [Язык] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas для [topic]. для each idea, give a one-sentence description и one potential challenge.

text

### Classification
Classify the following customer Обратная связь as [positive, neutral, negative].
Provide a confidence score (0-100) и a brief reason.

Обратная связь: [insert text]

### Translation с Style
Translate the following Английский text to Spanish. Use an informal tone suitable для a social media post.
Text: [insert text]

---

## Evaluation из Prompts

Treat prompts as code: version them, test them, и iterate.

- **A/B test** different prompt variants on a held-out set из queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) с the prompt, version, и observed Производительность.

---