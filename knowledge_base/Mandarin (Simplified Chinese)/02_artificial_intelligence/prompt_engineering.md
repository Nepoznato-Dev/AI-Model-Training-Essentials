<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is 这 practice 的 designing, refining, 和 optimising input prompts to get 这 best possible output from a 语言 model. It is both an art 和 a 科学, 和 it is 这 primary interface 为 controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity 和 Specificity
A clear prompt leaves no room 为 ambiguity. Specify exactly what you want, including format, length, 和 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, 和 keep your answer under 200 words."

### Provide Context
Models perform better when they know 这 role, audience, 和 goal.

**Without context:**
> "Write a function to sort a list."

**与 context:**
> "You are a senior Python developer. Write a function to sort a list 的 dictionaries by a given key. Use type hints 和 handle edge cases. 这 audience is junior developers."

### Use Positive Instructions
Tell 这 model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple 语言 accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs 支持 a multi-turn structure:

- **System message**: Sets 这 model's behaviour, persona, 和 constraints (persists 为 这 whole session).
- **User message**: 这 current query or instruction.
- **Assistant message**: 这 model's previous responses (used 为 continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply 与 concise code 示例 和 brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 示例 的 这 desired input-output format before asking 这 model to perform 这 task. This teaches 这 pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: 这 cat chased 这 mouse.
Output: 这 mouse was chased by 这 cat.
Input: 这 chef cooked 这 meal.
Output: 这 meal was cooked by 这 chef.
Input: 这 storm destroyed 这 house.
Output: (model completes)

### Chain-的-Thought (CoT)
Encourage 这 model to show its reasoning step by step. This improves accuracy on arithmetic, logic, 和 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**与 CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

这 model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros 和 three cons 的 microservices. Return only a valid JSON object 与 keys "pros" 和 "cons", each an array 的 strings.

---

## 高级 Techniques

### Self-Consistency
Generate multiple responses 为 这 same prompt (与 a temperature > 0) 和 take a majority vote on 这 final answer. This is especially effective 为 reasoning tasks.

### Tree-的-Thoughts
Explore multiple reasoning paths 在 parallel, evaluate each, 和 choose 这 best one. This is a research-level technique but can be approximated by asking 这 model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let 这 model interleave reasoning 与 tool calls. It can think, then act (e.g., search 这 网络, run code), then think again based on 这 result.

**Prompt structure:**
You have access to a calculator 和 a search engine. 为 each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have 这 final answer.

### Persona Assignment
Assign a specific persona to frame 这 response.

**示例:**
- "You are a Linux kernel developer explaining memory 管理 to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 为 factual answers; 0.7–1.0 为 creative writing.
- **Top-p** (nucleus sampling): Cuts off 这 probability mass at a certain cumulative threshold. 0.9 means 这 model samples from 这 top 90% 的 likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets 这 maximum output length. Remember to reserve space 为 这 response within 这 context window.
- **Frequency penalty**: Reduces repetition 的 这 same tokens.
- **Presence penalty**: Encourages 这 model to introduce new topics.

---

## Common Pitfalls 和 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts 的 prompt | Prompt too long or overloaded | Shorten; put 这 most important instruction at 这 end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain 在 detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 和 provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask 为 JSON, markdown table, or bullet list |
| Model answers 在 wrong 语言 | No 语言 instruction | Explicitly state "Respond 在 英语" (or your target 语言) |

---

## Prompt Templates 为 Common Tasks

### Summarisation
Summarise 这 following text 在 3 bullet points. Focus on 这 main arguments 和 avoid details.

Text: [insert text]


### Code Generation
Write a [语言] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas 为 [topic]. 为 each idea, give a one-sentence description 和 one potential challenge.

text

### Classification
Classify 这 following customer 反馈 as [positive, neutral, negative].
Provide a confidence score (0-100) 和 a brief reason.

反馈: [insert text]

### Translation 与 Style
Translate 这 following 英语 text to Spanish. Use an informal tone suitable 为 a social media post.
Text: [insert text]

---

## Evaluation 的 Prompts

Treat prompts as code: version them, test them, 和 iterate.

- **A/B test** different prompt variants on a held-out set 的 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) 与 这 prompt, version, 和 observed 性能.

---