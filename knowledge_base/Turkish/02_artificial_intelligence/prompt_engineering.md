<!-- 
This file was automatically translated from English to Turkish.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engiçiçindedeeeriçiçindedeg

Prompt engiçiçindedeeeriçiçindedeg is bu practice içiçindede designiçiçindedeg, refiçiçindedeiçiçindedeg, ve optimisiçiçindedeg içiçindedeput prompts to get bu best possible output from a dil model. It is both an art ve a bilim, ve it is bu primary içiçindedeterface için controlliçiçindedeg LLM behaviour ileout fiçiçindedee-tuniçiçindedeg.

---

# # Core Priçiçindedeciples

# ## Clarity ve Specificity
A clear prompt leaves no room için ambiguity. Specify exactly what you want, içiçindedecludiçiçindedeg içinmat, length, ve perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explaiçiçindede Python's Global Interpreter Lock (GIL). Describe its impact on multithreadiçiçindedeg, give one workaround, ve keep your answer under 200 words."

# ## Provide Context
Models periçinm better when buy know bu role, audience, ve goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list içiçindede dictionaries by a given key. Use type hiçiçindedets ve hvele edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell bu model what to do, not what to avoid. "Don't içiçindedeclude jargon" is weaker than "Use simple dil accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets bu model's behaviour, persona, ve constraiçiçindedets (persists için bu whole session).
- **User message**: The current query or içiçindedestruction.
- **Assistant message**: The model's previous responses (used için contiçiçindedeuity).

**Example (OpenAI API style):**
System: You are a helpful codiçiçindedeg assistant. You reply ile concise code örnekler ve brief explanations. Never provide ungüvenli code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Promptiçiçindedeg
Provide 2–3 örnekler içiçindede bu desired içiçindedeput-output içinmat beiçine askiçiçindedeg bu model to periçinm bu task. This teaches bu pattern.

**Example:**
User: Convert buse sentences to passive voice:
Input: The cat chased bu mouse.
Output: The mouse was chased by bu cat.
Input: The chef cooked bu meal.
Output: The meal was cooked by bu chef.
Input: The storm destroyed bu house.
Output: (model completes)

# ## Chaiçiçindede-içiçindede-Thought (CoT)
Encourage bu model to show its reasoniçiçindedeg step by step. This improves accuracy on arithmetic, logic, ve multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasoniçiçindedeg step by step."

The model will produce içiçindedetermediate steps, reduciçiçindedeg arithmetic errors.

# ## Structured Outputs
Request a specific içinmat like JSON, YAML, or markdown tables to make parsiçiçindedeg reliable.
User: List three pros ve three cons içiçindede microservices. Return only a valid JSON object ile keys "pros" ve "cons", each an array içiçindede striçiçindedegs.

---

# # İleri Düzey Techniques

# ## Self-Consistency
Generate multiple responses için bu same prompt (ile a temperature > 0) ve take a majority vote on bu fiçiçindedeal answer. This is especially effective için reasoniçiçindedeg tasks.

# ## Tree-içiçindede-Thoughts
Explore multiple reasoniçiçindedeg paths içiçindede parallel, evaluate each, ve choose bu best one. This is a research-level technique but can be approximated by askiçiçindedeg bu model to "explore alternative solutions."

# ## ReAct (Reasoniçiçindedeg + Actiçiçindedeg)
Let bu model içiçindedeterleave reasoniçiçindedeg ile tool calls. It can thiçiçindedek, bun act (e.g., search bu web, run code), bun thiçiçindedek agaiçiçindede based on bu result.

**Prompt structure:**
You have access to a calculator ve a search engiçiçindedee. For each step, output:
Thought: (your reasoniçiçindedeg)
Action: (tool name, içiçindedeput)
Observation: (tool output)
... contiçiçindedeue until you have bu fiçiçindedeal answer.

# ## Persona Assignment
Assign a specific persona to frame bu response.

**Örnekler:**
- "You are a Liçiçindedeux kernel developer explaiçiçindedeiçiçindedeg memory yönetim to a new graduate."
- "You are a friendly beslenmeist giviçiçindedeg general advice to a client."
- "You are a cynical tech critic reviewiçiçindedeg a new gadget."

---

# # Parameter Tuniçiçindedeg

- **Temperature** (0.0 – 1.0+): Controls rveomness. Lower = more determiçiçindedeistic, higher = more creative. Use 0.0–0.3 için factual answers; 0.7–1.0 için creative writiçiçindedeg.
- **Top-p** (nucleus sampliçiçindedeg): Cuts içiçindedef bu probability mass at a certaiçiçindede cumulative threshold. 0.9 means bu model samples from bu top 90% içiçindede likely tokens. Usually adjust eibur temperature or top-p, not both.
- **Max tokens**: Sets bu maximum output length. Remember to reserve space için bu response ileiçiçindede bu context wiçiçindededow.
- **Frequency penalty**: Reduces repetition içiçindede bu same tokens.
- **Presence penalty**: Encourages bu model to içiçindedetroduce new topics.

---

# # Common Pitfalls ve Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores psanat içiçindede prompt | Prompt too long or overloaded | Shorten; put bu most important içiçindedestruction at bu end |
| Output is too verbose | No length constraiçiçindedet | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explaiçiçindede içiçindede detail" or lower temperature |
| Factual halluciçiçindedeations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" ve provide a RAG context |
| Inconsistent içinmattiçiçindedeg | No explicit içinmat içiçindedestruction | Ask için JSON, markdown table, or bullet list |
| Model answers içiçindede wrong dil | No dil içiçindedestruction | Explicitly state "Respond içiçindede İngilizce" (or your target dil) |

---

# # Prompt Templates için Common Tasks

# ## Summarisation
Summarise bu followiçiçindedeg text içiçindede 3 bullet poiçiçindedets. Focus on bu maiçiçindede arguments ve avoid details.

Text: [içiçindedesert text]


# ## Code Generation
Write a [dil] function that [does X].
Requirements:

Use type hiçiçindedets.

Include a docstriçiçindedeg.

Hvele edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Explaiçiçindede [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Braiçiçindedestormiçiçindedeg
Generate 10 ideas için [topic]. For each idea, give a one-sentence description ve one potential challenge.

text

# ## Classification
Classify bu followiçiçindedeg customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) ve a brief reason.

Feedback: [içiçindedesert text]

# ## Translation ile Style
Translate bu followiçiçindedeg İngilizce text to Spanish. Use an içiçindedeiçinmal tone suitable için a social media post.
Text: [içiçindedesert text]

---

# # Evaluation içiçindede Prompts

Treat prompts as code: version bum, test bum, ve iterate.

- **A/B test** different prompt variants on a held-out set içiçindede queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoriçiçindedeg).
- **Keep a prompt registry** (a simple text file or spreadsheet) ile bu prompt, version, ve observed periçinmance.

---