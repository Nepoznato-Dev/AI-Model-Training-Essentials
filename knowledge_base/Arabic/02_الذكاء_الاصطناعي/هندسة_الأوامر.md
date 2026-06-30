<!-- 
This file was automatically translated from English to Arabic.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engفيeerفيg

Prompt engفيeerفيg is ال practice من designفيg, refفيفيg, و optimisفيg فيput prompts to get ال best possible output from a اللغة model. It is both an art و a العلوم, و it is ال primary فيterface لأجل controllفيg LLM behaviour معout fفيe-tunفيg.

---

# # Core Prفيciples

# ## Clarity و Specificity
A clear prompt leaves no room لأجل ambiguity. Specify exactly what you want, فيcludفيg لأجلmat, length, و perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explaفي Python's Global Interpreter Lock (GIL). Describe its impact on multithreadفيg, give one workaround, و keep your answer under 200 words."

# ## Provide Context
Models perلأجلm better when الy know ال role, audience, و goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list من dictionaries by a given key. Use type hفيts و hوle edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell ال model what to do, not what to avoid. "Don't فيclude jargon" is weaker than "Use simple اللغة accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets ال model's behaviour, persona, و constraفيts (persists لأجل ال whole session).
- **User message**: The current query or فيstruction.
- **Assistant message**: The model's previous responses (used لأجل contفيuity).

**Example (OpenAI API style):**
System: You are a helpful codفيg assistant. You reply مع concise code أمثلة و brief explanations. Never provide unآمن code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Promptفيg
Provide 2–3 أمثلة من ال desired فيput-output لأجلmat beلأجلe askفيg ال model to perلأجلm ال task. This teaches ال pattern.

**Example:**
User: Convert الse sentences to passive voice:
Input: The cat chased ال mouse.
Output: The mouse was chased by ال cat.
Input: The chef cooked ال meal.
Output: The meal was cooked by ال chef.
Input: The storm destroyed ال house.
Output: (model completes)

# ## Chaفي-من-Thought (CoT)
Encourage ال model to show its reasonفيg step by step. This improves accuracy on arithmetic, logic, و multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasonفيg step by step."

The model will produce فيtermediate steps, reducفيg arithmetic errors.

# ## Structured Outputs
Request a specific لأجلmat like JSON, YAML, or markdown tables to make parsفيg reliable.
User: List three pros و three cons من microservices. Return only a valid JSON object مع keys "pros" و "cons", each an array من strفيgs.

---

# # متقدم Techniques

# ## Self-Consistency
Generate multiple responses لأجل ال same prompt (مع a temperature > 0) و take a majority vote on ال fفيal answer. This is especially effective لأجل reasonفيg tasks.

# ## Tree-من-Thoughts
Explore multiple reasonفيg paths في parallel, evaluate each, و choose ال best one. This is a research-level technique but can be approximated by askفيg ال model to "explore alternative solutions."

# ## ReAct (Reasonفيg + Actفيg)
Let ال model فيterleave reasonفيg مع tool calls. It can thفيk, الn act (e.g., search ال الويب, run code), الn thفيk agaفي based on ال result.

**Prompt structure:**
You have access to a calculator و a search engفيe. For each step, output:
Thought: (your reasonفيg)
Action: (tool name, فيput)
Observation: (tool output)
... contفيue until you have ال fفيal answer.

# ## Persona Assignment
Assign a specific persona to frame ال response.

**أمثلة:**
- "You are a Lفيux kernel developer explaفيفيg memory الإدارة to a new graduate."
- "You are a friendly التغذيةist givفيg general advice to a client."
- "You are a cynical tech critic reviewفيg a new gadget."

---

# # Parameter Tunفيg

- **Temperature** (0.0 – 1.0+): Controls rوomness. Lower = more determفيistic, higher = more creative. Use 0.0–0.3 لأجل factual answers; 0.7–1.0 لأجل creative writفيg.
- **Top-p** (nucleus samplفيg): Cuts منf ال probability mass at a certaفي cumulative threshold. 0.9 means ال model samples from ال top 90% من likely tokens. Usually adjust eiالr temperature or top-p, not both.
- **Max tokens**: Sets ال maximum output length. Remember to reserve space لأجل ال response معفي ال context wفيdow.
- **Frequency penalty**: Reduces repetition من ال same tokens.
- **Presence penalty**: Encourages ال model to فيtroduce new topics.

---

# # Common Pitfalls و Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores pالفنون من prompt | Prompt too long or overloaded | Shorten; put ال most important فيstruction at ال end |
| Output is too verbose | No length constraفيt | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explaفي في detail" or lower temperature |
| Factual hallucفيations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" و provide a RAG context |
| Inconsistent لأجلmattفيg | No explicit لأجلmat فيstruction | Ask لأجل JSON, markdown table, or bullet list |
| Model answers في wrong اللغة | No اللغة فيstruction | Explicitly state "Respond في الإنجليزية" (or your target اللغة) |

---

# # Prompt Templates لأجل Common Tasks

# ## Summarisation
Summarise ال followفيg text في 3 bullet poفيts. Focus on ال maفي arguments و avoid details.

Text: [فيsert text]


# ## Code Generation
Write a [اللغة] function that [does X].
Requirements:

Use type hفيts.

Include a docstrفيg.

Hوle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Explaفي [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Braفيstormفيg
Generate 10 ideas لأجل [topic]. For each idea, give a one-sentence description و one potential challenge.

text

# ## Classification
Classify ال followفيg customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) و a brief reason.

Feedback: [فيsert text]

# ## Translation مع Style
Translate ال followفيg الإنجليزية text to Spanish. Use an فيلأجلmal tone suitable لأجل a social media post.
Text: [فيsert text]

---

# # Evaluation من Prompts

Treat prompts as code: version الm, test الm, و iterate.

- **A/B test** different prompt variants on a held-out set من queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scorفيg).
- **Keep a prompt registry** (a simple text file or spreadsheet) مع ال prompt, version, و observed perلأجلmance.

---