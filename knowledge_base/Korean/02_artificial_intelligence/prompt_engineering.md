<!-- 
This file was automatically translated from English to Korean.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engineering

Prompt engineering is 그 practice 의 designing, refining, 와 optimising input prompts to get 그 best possible output from a 언어 model. It is both an art 와 a 과학, 와 it is 그 primary interface 위한 controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity 와 Specificity
A clear prompt leaves no room 위한 ambiguity. Specify exactly what you want, including format, length, 와 perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, 와 keep your answer under 200 words."

### Provide Context
Models perform better when they know 그 role, audience, 와 goal.

**Without context:**
> "Write a function to sort a list."

**와 함께 context:**
> "You are a senior Python developer. Write a function to sort a list 의 dictionaries by a given key. Use type hints 와 handle edge cases. 그 audience is junior developers."

### Use Positive Instructions
Tell 그 model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple 언어 accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs 지원 a multi-turn structure:

- **System message**: Sets 그 model's behaviour, persona, 와 constraints (persists 위한 그 whole session).
- **User message**: 그 current query or instruction.
- **Assistant message**: 그 model's previous responses (used 위한 continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply 와 함께 concise code 예시 와 brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 예시 의 그 desired input-output format before asking 그 model to perform 그 task. This teaches 그 pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: 그 cat chased 그 mouse.
Output: 그 mouse was chased by 그 cat.
Input: 그 chef cooked 그 meal.
Output: 그 meal was cooked by 그 chef.
Input: 그 storm destroyed 그 house.
Output: (model completes)

### Chain-의-Thought (CoT)
Encourage 그 model to show its reasoning step by step. This improves accuracy on arithmetic, logic, 와 multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**와 함께 CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

그 model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros 와 three cons 의 microservices. Return only a valid JSON object 와 함께 keys "pros" 와 "cons", each an array 의 strings.

---

## 고급 Techniques

### Self-Consistency
Generate multiple responses 위한 그 same prompt (와 함께 a temperature > 0) 와 take a majority vote on 그 final answer. This is especially effective 위한 reasoning tasks.

### Tree-의-Thoughts
Explore multiple reasoning paths 에서 parallel, evaluate each, 와 choose 그 best one. This is a research-level technique but can be approximated by asking 그 model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let 그 model interleave reasoning 와 함께 tool calls. It can think, then act (e.g., search 그 웹, run code), then think again based on 그 result.

**Prompt structure:**
You have access to a calculator 와 a search engine. 위한 each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have 그 final answer.

### Persona Assignment
Assign a specific persona to frame 그 response.

**예시:**
- "You are a Linux kernel developer explaining memory 관리 to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 위한 factual answers; 0.7–1.0 위한 creative writing.
- **Top-p** (nucleus sampling): Cuts off 그 probability mass at a certain cumulative threshold. 0.9 means 그 model samples from 그 top 90% 의 likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets 그 maximum output length. Remember to reserve space 위한 그 response within 그 context window.
- **Frequency penalty**: Reduces repetition 의 그 same tokens.
- **Presence penalty**: Encourages 그 model to introduce new topics.

---

## Common Pitfalls 와 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts 의 prompt | Prompt too long or overloaded | Shorten; put 그 most important instruction at 그 end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain 에서 detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 와 provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask 위한 JSON, markdown table, or bullet list |
| Model answers 에서 wrong 언어 | No 언어 instruction | Explicitly state "Respond 에서 영어" (or your target 언어) |

---

## Prompt Templates 위한 Common Tasks

### Summarisation
Summarise 그 following text 에서 3 bullet points. Focus on 그 main arguments 와 avoid details.

Text: [insert text]


### Code Generation
Write a [언어] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas 위한 [topic]. 위한 each idea, give a one-sentence description 와 one potential challenge.

text

### Classification
Classify 그 following customer 피드백 as [positive, neutral, negative].
Provide a confidence score (0-100) 와 a brief reason.

피드백: [insert text]

### Translation 와 함께 Style
Translate 그 following 영어 text to Spanish. Use an informal tone suitable 위한 a social media post.
Text: [insert text]

---

## Evaluation 의 Prompts

Treat prompts as code: version them, test them, 와 iterate.

- **A/B test** different prompt variants on a held-out set 의 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) 와 함께 그 prompt, version, 와 observed 성능.

---