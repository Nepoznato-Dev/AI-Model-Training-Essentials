<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is 這 practice 的 designing, refining, 和 optimising input prompts to get 這 best possible output from a 語言 model. It is both an art 和 a 科學, 和 it is 這 primary interface 為 controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity 和 Specificity
A clear prompt leaves no room 為 ambiguity. Specify exactly what you want, including format, length, 和 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, 和 keep your answer under 200 words."

### Provide Context
Models perform better when they know 這 role, audience, 和 goal.

**Without context:**
> "Write a function to sort a list."

**與 context:**
> "You are a senior Python developer. Write a function to sort a list 的 dictionaries by a given key. Use type hints 和 handle edge cases. 這 audience is junior developers."

### Use Positive Instructions
Tell 這 model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple 語言 accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs 支援 a multi-turn structure:

- **System message**: Sets 這 model's behaviour, persona, 和 constraints (persists 為 這 whole session).
- **User message**: 這 current query or instruction.
- **Assistant message**: 這 model's previous responses (used 為 continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply 與 concise code 範例 和 brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 範例 的 這 desired input-output format before asking 這 model to perform 這 task. This teaches 這 pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: 這 cat chased 這 mouse.
Output: 這 mouse was chased by 這 cat.
Input: 這 chef cooked 這 meal.
Output: 這 meal was cooked by 這 chef.
Input: 這 storm destroyed 這 house.
Output: (model completes)

### Chain-的-Thought (CoT)
Encourage 這 model to show its reasoning step by step. This improves accuracy on arithmetic, logic, 和 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**與 CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

這 model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros 和 three cons 的 microservices. Return only a valid JSON object 與 keys "pros" 和 "cons", each an array 的 strings.

---

## 高級 Techniques

### Self-Consistency
Generate multiple responses 為 這 same prompt (與 a temperature > 0) 和 take a majority vote on 這 final answer. This is especially effective 為 reasoning tasks.

### Tree-的-Thoughts
Explore multiple reasoning paths 在 parallel, evaluate each, 和 choose 這 best one. This is a research-level technique but can be approximated by asking 這 model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let 這 model interleave reasoning 與 tool calls. It can think, then act (e.g., search 這 網路, run code), then think again based on 這 result.

**Prompt structure:**
You have access to a calculator 和 a search engine. 為 each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have 這 final answer.

### Persona Assignment
Assign a specific persona to frame 這 response.

**範例:**
- "You are a Linux kernel developer explaining memory 管理 to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 為 factual answers; 0.7–1.0 為 creative writing.
- **Top-p** (nucleus sampling): Cuts off 這 probability mass at a certain cumulative threshold. 0.9 means 這 model samples from 這 top 90% 的 likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets 這 maximum output length. Remember to reserve space 為 這 response within 這 context window.
- **Frequency penalty**: Reduces repetition 的 這 same tokens.
- **Presence penalty**: Encourages 這 model to introduce new topics.

---

## Common Pitfalls 和 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts 的 prompt | Prompt too long or overloaded | Shorten; put 這 most important instruction at 這 end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain 在 detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 和 provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask 為 JSON, markdown table, or bullet list |
| Model answers 在 wrong 語言 | No 語言 instruction | Explicitly state "Respond 在 英語" (or your target 語言) |

---

## Prompt Templates 為 Common Tasks

### Summarisation
Summarise 這 following text 在 3 bullet points. Focus on 這 main arguments 和 avoid details.

Text: [insert text]


### Code Generation
Write a [語言] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas 為 [topic]. 為 each idea, give a one-sentence description 和 one potential challenge.

text

### Classification
Classify 這 following customer 回饋 as [positive, neutral, negative].
Provide a confidence score (0-100) 和 a brief reason.

回饋: [insert text]

### Translation 與 Style
Translate 這 following 英語 text to Spanish. Use an informal tone suitable 為 a social media post.
Text: [insert text]

---

## Evaluation 的 Prompts

Treat prompts as code: version them, test them, 和 iterate.

- **A/B test** different prompt variants on a held-out set 的 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) 與 這 prompt, version, 和 observed 效能.

---