<!-- 
This file was automatically translated from English to Japanese.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is その practice の designing, refining, と optimising input prompts to get その best possible output from a 言語 model. It is both an art と a 科学, と it is その primary interface のために controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity と Specificity
A clear prompt leaves no room のために ambiguity. Specify exactly what you want, including format, length, と perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, と keep your answer under 200 words."

### Provide Context
Models perform better when they know その role, audience, と goal.

**Without context:**
> "Write a function to sort a list."

**と context:**
> "You are a senior Python developer. Write a function to sort a list の dictionaries by a given key. Use type hints と handle edge cases. その audience is junior developers."

### Use Positive Instructions
Tell その model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple 言語 accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets その model's behaviour, persona, と constraints (persists のために その whole session).
- **User message**: その current query or instruction.
- **Assistant message**: その model's previous responses (used のために continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply と concise code 例 と brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 例 の その desired input-output format before asking その model to perform その task. This teaches その pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: その cat chased その mouse.
Output: その mouse was chased by その cat.
Input: その chef cooked その meal.
Output: その meal was cooked by その chef.
Input: その storm destroyed その house.
Output: (model completes)

### Chain-の-Thought (CoT)
Encourage その model to show its reasoning step by step. This improves accuracy on arithmetic, logic, と multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**と CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

その model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros と three cons の microservices. Return only a valid JSON object と keys "pros" と "cons", each an array の strings.

---

## 上級 Techniques

### Self-Consistency
Generate multiple responses のために その same prompt (と a temperature > 0) と take a majority vote on その final answer. This is especially effective のために reasoning tasks.

### Tree-の-Thoughts
Explore multiple reasoning paths で parallel, evaluate each, と choose その best one. This is a research-level technique but can be approximated by asking その model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let その model interleave reasoning と tool calls. It can think, then act (e.g., search その ウェブ, run code), then think again based on その result.

**Prompt structure:**
You have access to a calculator と a search engine. のために each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have その final answer.

### Persona Assignment
Assign a specific persona to frame その response.

**例:**
- "You are a Linux kernel developer explaining memory 管理 to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 のために factual answers; 0.7–1.0 のために creative writing.
- **Top-p** (nucleus sampling): Cuts off その probability mass at a certain cumulative threshold. 0.9 means その model samples from その top 90% の likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets その maximum output length. Remember to reserve space のために その response within その context window.
- **Frequency penalty**: Reduces repetition の その same tokens.
- **Presence penalty**: Encourages その model to introduce new topics.

---

## Common Pitfalls と Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts の prompt | Prompt too long or overloaded | Shorten; put その most important instruction at その end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain で detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" と provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask のために JSON, markdown table, or bullet list |
| Model answers で wrong 言語 | No 言語 instruction | Explicitly state "Respond で 英語" (or your target 言語) |

---

## Prompt Templates のために Common Tasks

### Summarisation
Summarise その following text で 3 bullet points. Focus on その main arguments と avoid details.

Text: [insert text]


### Code Generation
Write a [言語] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas のために [topic]. のために each idea, give a one-sentence description と one potential challenge.

text

### Classification
Classify その following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) と a brief reason.

Feedback: [insert text]

### Translation と Style
Translate その following 英語 text to Spanish. Use an informal tone suitable のために a social media post.
Text: [insert text]

---

## Evaluation の Prompts

Treat prompts as code: version them, test them, と iterate.

- **A/B test** different prompt variants on a held-out set の queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) と その prompt, version, と observed パフォーマンス.

---