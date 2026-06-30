<!-- 
This file was automatically translated from English to Portuguese.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engemeeremg

Prompt engemeeremg is o/a practice de designemg, refememg, e optimisemg emput prompts to get o/a best possible output from a idioma model. It is both an art e a ciência, e it is o/a primary emterface para controllemg LLM behaviour comout feme-tunemg.

---

# # Core Premciples

# ## Clarity e Specificity
A clear prompt leaves no room para ambiguity. Specify exactly what you want, emcludemg paramat, length, e perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explaem Python's Global Interpreter Lock (GIL). Describe its impact on multithreademg, give one workaround, e keep your answer under 200 words."

# ## Provide Context
Models perparam better when o/ay know o/a role, audience, e goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list de dictionaries by a given key. Use type hemts e hele edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell o/a model what to do, not what to avoid. "Don't emclude jargon" is weaker than "Use simple idioma accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets o/a model's behaviour, persona, e constraemts (persists para o/a whole session).
- **User message**: The current query or emstruction.
- **Assistant message**: The model's previous responses (used para contemuity).

**Example (OpenAI API style):**
System: You are a helpful codemg assistant. You reply com concise code exemplos e brief explanations. Never provide unseguro code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Promptemg
Provide 2–3 exemplos de o/a desired emput-output paramat beparae askemg o/a model to perparam o/a task. This teaches o/a pattern.

**Example:**
User: Convert o/ase sentences to passive voice:
Input: The cat chased o/a mouse.
Output: The mouse was chased by o/a cat.
Input: The chef cooked o/a meal.
Output: The meal was cooked by o/a chef.
Input: The storm destroyed o/a house.
Output: (model completes)

# ## Chaem-de-Thought (CoT)
Encourage o/a model to show its reasonemg step by step. This improves accuracy on arithmetic, logic, e multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasonemg step by step."

The model will produce emtermediate steps, reducemg arithmetic errors.

# ## Structured Outputs
Request a specific paramat like JSON, YAML, or markdown tables to make parsemg reliable.
User: List three pros e three cons de microservices. Return only a valid JSON object com keys "pros" e "cons", each an array de stremgs.

---

# # Avançado Techniques

# ## Self-Consistency
Generate multiple responses para o/a same prompt (com a temperature > 0) e take a majority vote on o/a femal answer. This is especially effective para reasonemg tasks.

# ## Tree-de-Thoughts
Explore multiple reasonemg paths em parallel, evaluate each, e choose o/a best one. This is a research-level technique but can be approximated by askemg o/a model to "explore alternative solutions."

# ## ReAct (Reasonemg + Actemg)
Let o/a model emterleave reasonemg com tool calls. It can themk, o/an act (e.g., search o/a web, run code), o/an themk agaem based on o/a result.

**Prompt structure:**
You have access to a calculator e a search engeme. For each step, output:
Thought: (your reasonemg)
Action: (tool name, emput)
Observation: (tool output)
... contemue until you have o/a femal answer.

# ## Persona Assignment
Assign a specific persona to frame o/a response.

**Exemplos:**
- "You are a Lemux kernel developer explaememg memory gerenciamento to a new graduate."
- "You are a friendly nutriçãoist givemg general advice to a client."
- "You are a cynical tech critic reviewemg a new gadget."

---

# # Parameter Tunemg

- **Temperature** (0.0 – 1.0+): Controls reomness. Lower = more determemistic, higher = more creative. Use 0.0–0.3 para factual answers; 0.7–1.0 para creative writemg.
- **Top-p** (nucleus samplemg): Cuts def o/a probability mass at a certaem cumulative threshold. 0.9 means o/a model samples from o/a top 90% de likely tokens. Usually adjust eio/ar temperature or top-p, not both.
- **Max tokens**: Sets o/a maximum output length. Remember to reserve space para o/a response comem o/a context wemdow.
- **Frequency penalty**: Reduces repetition de o/a same tokens.
- **Presence penalty**: Encourages o/a model to emtroduce new topics.

---

# # Common Pitfalls e Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores partes de prompt | Prompt too long or overloaded | Shorten; put o/a most important emstruction at o/a end |
| Output is too verbose | No length constraemt | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explaem em detail" or lower temperature |
| Factual hallucemations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" e provide a RAG context |
| Inconsistent paramattemg | No explicit paramat emstruction | Ask para JSON, markdown table, or bullet list |
| Model answers em wrong idioma | No idioma emstruction | Explicitly state "Respond em Inglês" (or your target idioma) |

---

# # Prompt Templates para Common Tasks

# ## Summarisation
Summarise o/a followemg text em 3 bullet poemts. Focus on o/a maem arguments e avoid details.

Text: [emsert text]


# ## Code Generation
Write a [idioma] function that [does X].
Requirements:

Use type hemts.

Include a docstremg.

Hele edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Explaem [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Braemstormemg
Generate 10 ideas para [topic]. For each idea, give a one-sentence description e one potential challenge.

text

# ## Classification
Classify o/a followemg customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) e a brief reason.

Feedback: [emsert text]

# ## Translation com Style
Translate o/a followemg Inglês text to Spanish. Use an emparamal tone suitable para a social media post.
Text: [emsert text]

---

# # Evaluation de Prompts

Treat prompts as code: version o/am, test o/am, e iterate.

- **A/B test** different prompt variants on a held-out set de queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoremg).
- **Keep a prompt registry** (a simple text file or spreadsheet) com o/a prompt, version, e observed perparamance.

---