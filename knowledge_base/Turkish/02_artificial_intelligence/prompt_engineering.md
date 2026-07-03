# Prompt Engineering

Prompt engineering is bu practice içinde designing, refining, ve optimising input prompts to get bu best possible output from a Dil model. It is both an art ve a Bilim, ve it is bu primary interface için controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity ve Specificity
A clear prompt leaves no room için ambiguity. Specify exactly what you want, including format, length, ve perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, ve keep your answer under 200 words."

### Provide Context
Models perform better when they know bu role, audience, ve goal.

**Without context:**
> "Write a function to sort a list."

**ile context:**
> "You are a senior Python developer. Write a function to sort a list içinde dictionaries by a given key. Use type hints ve handle edge cases. bu audience is junior developers."

### Use Positive Instructions
Tell bu model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple Dil accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs Destek a multi-turn structure:

- **System message**: Sets bu model's behaviour, persona, ve constraints (persists için bu whole session).
- **User message**: bu current query or instruction.
- **Assistant message**: bu model's previous responses (used için continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply ile concise code Örnekler ve brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 Örnekler içinde bu desired input-output format before asking bu model to perform bu task. This teaches bu pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: bu cat chased bu mouse.
Output: bu mouse was chased by bu cat.
Input: bu chef cooked bu meal.
Output: bu meal was cooked by bu chef.
Input: bu storm destroyed bu house.
Output: (model completes)

### Chain-içinde-Thought (CoT)
Encourage bu model to show its reasoning step by step. This improves accuracy on arithmetic, logic, ve multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**ile CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

bu model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros ve three cons içinde microservices. Return only a valid JSON object ile keys "pros" ve "cons", each an array içinde strings.

---

## İleri Düzey Techniques

### Self-Consistency
Generate multiple responses için bu same prompt (ile a temperature > 0) ve take a majority vote on bu final answer. This is especially effective için reasoning tasks.

### Tree-içinde-Thoughts
Explore multiple reasoning paths içinde parallel, evaluate each, ve choose bu best one. This is a research-level technique but can be approximated by asking bu model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let bu model interleave reasoning ile tool calls. It can think, then act (e.g., search bu Web, run code), then think again based on bu result.

**Prompt structure:**
You have access to a calculator ve a search engine. için each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have bu final answer.

### Persona Assignment
Assign a specific persona to frame bu response.

**Örnekler:**
- "You are a Linux kernel developer explaining memory Yönetim to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 için factual answers; 0.7–1.0 için creative writing.
- **Top-p** (nucleus sampling): Cuts off bu probability mass at a certain cumulative threshold. 0.9 means bu model samples from bu top 90% içinde likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets bu maximum output length. Remember to reserve space için bu response within bu context window.
- **Frequency penalty**: Reduces repetition içinde bu same tokens.
- **Presence penalty**: Encourages bu model to introduce new topics.

---

## Common Pitfalls ve Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts içinde prompt | Prompt too long or overloaded | Shorten; put bu most important instruction at bu end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain içinde detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" ve provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask için JSON, markdown table, or bullet list |
| Model answers içinde wrong Dil | No Dil instruction | Explicitly state "Respond içinde İngilizce" (or your target Dil) |

---

## Prompt Templates için Common Tasks

### Summarisation
Summarise bu following text içinde 3 bullet points. Focus on bu main arguments ve avoid details.

Text: [insert text]


### Code Generation
Write a [Dil] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas için [topic]. için each idea, give a one-sentence description ve one potential challenge.

text

### Classification
Classify bu following customer Geri Bildirim as [positive, neutral, negative].
Provide a confidence score (0-100) ve a brief reason.

Geri Bildirim: [insert text]

### Translation ile Style
Translate bu following İngilizce text to Spanish. Use an informal tone suitable için a social media post.
Text: [insert text]

---

## Evaluation içinde Prompts

Treat prompts as code: version them, test them, ve iterate.

- **A/B test** different prompt variants on a held-out set içinde queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) ile bu prompt, version, ve observed Performans.

---