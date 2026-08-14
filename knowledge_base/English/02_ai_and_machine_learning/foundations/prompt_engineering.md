<!--
---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.1"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prompt, engineering, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Prompt Engineering

Prompt engineering is the practice of designing, refining, and optimising input prompts to get the best possible output from a language model. It is both an art and a science, and it is the primary interface for controlling LLM behaviour without fine-tuning.

---

## Core Principles

### Clarity and Specificity
A clear prompt leaves no room for ambiguity. Specify exactly what you want, including format, length, and perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, and keep your answer under 200 words."

### Provide Context
Models perform better when they know the role, audience, and goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list of dictionaries by a given key. Use type hints and handle edge cases. The audience is junior developers."

### Use Positive Instructions
Tell the model what to do, not what to avoid. "Don't include jargon" is weaker than "Use simple language accessible to a 10-year-old."

---

## Prompt Structures

### System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets the model's behaviour, persona, and constraints (persists for the whole session).
- **User message**: The current query or instruction.
- **Assistant message**: The model's previous responses (used for continuity).

**Example (OpenAI API style):**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Provide 2–3 examples of the desired input-output format before asking the model to perform the task. This teaches the pattern.

**Example:**
User: Convert these sentences to passive voice:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)

### Chain-of-Thought (CoT)
Encourage the model to show its reasoning step by step. This improves accuracy on arithmetic, logic, and multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

The model will produce intermediate steps, reducing arithmetic errors.

### Structured Outputs
Request a specific format like JSON, YAML, or markdown tables to make parsing reliable.
User: List three pros and three cons of microservices. Return only a valid JSON object with keys "pros" and "cons", each an array of strings.

---

## Advanced Techniques

### Self-Consistency
Generate multiple responses for the same prompt (with a temperature > 0) and take a majority vote on the final answer. This is especially effective for reasoning tasks.

### Tree-of-Thoughts
Explore multiple reasoning paths in parallel, evaluate each, and choose the best one. This is a research-level technique but can be approximated by asking the model to "explore alternative solutions."

### ReAct (Reasoning + Acting)
Let the model interleave reasoning with tool calls. It can think, then act (e.g., search the web, run code), then think again based on the result.

**Prompt structure:**
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### Persona Assignment
Assign a specific persona to frame the response.

**Examples:**
- "You are a Linux kernel developer explaining memory management to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 for factual answers; 0.7–1.0 for creative writing.
- **Top-p** (nucleus sampling): Cuts off the probability mass at a certain cumulative threshold. 0.9 means the model samples from the top 90% of likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets the maximum output length. Remember to reserve space for the response within the context window.
- **Frequency penalty**: Reduces repetition of the same tokens.
- **Presence penalty**: Encourages the model to introduce new topics.

---

## Common Pitfalls and Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts of prompt | Prompt too long or overloaded | Shorten; put the most important instruction at the end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain in detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" and provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask for JSON, markdown table, or bullet list |
| Model answers in wrong language | No language instruction | Explicitly state "Respond in English" (or your target language) |

---

## Prompt Templates for Common Tasks

### Summarisation
Summarise the following text in 3 bullet points. Focus on the main arguments and avoid details.

Text: [insert text]


### Code Generation
Write a [language] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas for [topic]. For each idea, give a one-sentence description and one potential challenge.

text

### Classification
Classify the following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) and a brief reason.

Feedback: [insert text]

### Translation with Style
Translate the following English text to Spanish. Use an informal tone suitable for a social media post.
Text: [insert text]

---

## Evaluation of Prompts

Treat prompts as code: version them, test them, and iterate.

- **A/B test** different prompt variants on a held-out set of queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) with the prompt, version, and observed performance.

---