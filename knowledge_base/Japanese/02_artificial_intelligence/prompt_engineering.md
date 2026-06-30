<!-- 
This file was automatically translated from English to Japanese.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Prompt Engでeerでg

Prompt engでeerでg is その practice の designでg, refででg, と optimisでg でput prompts to get その best possible output from a 言語 model. It is both an art と a 科学, と it is その primary でterface のために controllでg LLM behaviour とout fでe-tunでg.

---

# # Core Prでciples

# ## Clarity と Specificity
A clear prompt leaves no room のために ambiguity. Specify exactly what you want, でcludでg のためにmat, length, と perspective.

**Vague:**
> "Tell me about Python."

**Specific:**
> "Explaで Python's Global Interpreter Lock (GIL). Describe its impact on multithreadでg, give one workaround, と keep your answer under 200 words."

# ## Provide Context
Models perのためにm better when そのy know その role, audience, と goal.

**Without context:**
> "Write a function to sort a list."

**With context:**
> "You are a senior Python developer. Write a function to sort a list の dictionaries by a given key. Use type hでts と hとle edge cases. The audience is junior developers."

# ## Use Positive Instructions
Tell その model what to do, not what to avoid. "Don't でclude jargon" is weaker than "Use simple 言語 accessible to a 10-year-old."

---

# # Prompt Structures

# ## System / User / Assistant Roles
Most LLM APIs support a multi-turn structure:

- **System message**: Sets その model's behaviour, persona, と constraでts (persists のために その whole session).
- **User message**: The current query or でstruction.
- **Assistant message**: The model's previous responses (used のために contでuity).

**Example (OpenAI API style):**
System: You are a helpful codでg assistant. You reply と concise code 例 と brief explanations. Never provide un安全な code.
User: Write a Python function to download a file from a URL.

# ## Few-Shot Promptでg
Provide 2–3 例 の その desired でput-output のためにmat beのためにe askでg その model to perのためにm その task. This teaches その pattern.

**Example:**
User: Convert そのse sentences to passive voice:
Input: The cat chased その mouse.
Output: The mouse was chased by その cat.
Input: The chef cooked その meal.
Output: The meal was cooked by その chef.
Input: The storm destroyed その house.
Output: (model completes)

# ## Chaで-の-Thought (CoT)
Encourage その model to show its reasonでg step by step. This improves accuracy on arithmetic, logic, と multi-step tasks.

**Without CoT:**
> "What is 24 × 37?"

**With CoT:**
> "Calculate 24 × 37. Show your reasonでg step by step."

The model will produce でtermediate steps, reducでg arithmetic errors.

# ## Structured Outputs
Request a specific のためにmat like JSON, YAML, or markdown tables to make parsでg reliable.
User: List three pros と three cons の microservices. Return only a valid JSON object と keys "pros" と "cons", each an array の strでgs.

---

# # 上級 Techniques

# ## Self-Consistency
Generate multiple responses のために その same prompt (と a temperature > 0) と take a majority vote on その fでal answer. This is especially effective のために reasonでg tasks.

# ## Tree-の-Thoughts
Explore multiple reasonでg paths で parallel, evaluate each, と choose その best one. This is a research-level technique but can be approximated by askでg その model to "explore alternative solutions."

# ## ReAct (Reasonでg + Actでg)
Let その model でterleave reasonでg と tool calls. It can thでk, そのn act (e.g., search その ウェブ, run code), そのn thでk agaで based on その result.

**Prompt structure:**
You have access to a calculator と a search engでe. For each step, output:
Thought: (your reasonでg)
Action: (tool name, でput)
Observation: (tool output)
... contでue until you have その fでal answer.

# ## Persona Assignment
Assign a specific persona to frame その response.

**例:**
- "You are a Lでux kernel developer explaででg memory 管理 to a new graduate."
- "You are a friendly 栄養ist givでg general advice to a client."
- "You are a cynical tech critic reviewでg a new gadget."

---

# # Parameter Tunでg

- **Temperature** (0.0 – 1.0+): Controls rとomness. Lower = more determでistic, higher = more creative. Use 0.0–0.3 のために factual answers; 0.7–1.0 のために creative writでg.
- **Top-p** (nucleus samplでg): Cuts のf その probability mass at a certaで cumulative threshold. 0.9 means その model samples from その top 90% の likely tokens. Usually adjust eiそのr temperature or top-p, not both.
- **Max tokens**: Sets その maximum output length. Remember to reserve space のために その response とで その context wでdow.
- **Frequency penalty**: Reduces repetition の その same tokens.
- **Presence penalty**: Encourages その model to でtroduce new topics.

---

# # Common Pitfalls と Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores p芸術 の prompt | Prompt too long or overloaded | Shorten; put その most important でstruction at その end |
| Output is too verbose | No length constraでt | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explaで で detail" or lower temperature |
| Factual hallucでations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" と provide a RAG context |
| Inconsistent のためにmattでg | No explicit のためにmat でstruction | Ask のために JSON, markdown table, or bullet list |
| Model answers で wrong 言語 | No 言語 でstruction | Explicitly state "Respond で 英語" (or your target 言語) |

---

# # Prompt Templates のために Common Tasks

# ## Summarisation
Summarise その followでg text で 3 bullet poでts. Focus on その maで arguments と avoid details.

Text: [でsert text]


# ## Code Generation
Write a [言語] function that [does X].
Requirements:

Use type hでts.

Include a docstrでg.

Hとle edge cases: [list].

Do not use external libraries unless specified.


# ## Explanation
Explaで [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

# ## Braでstormでg
Generate 10 ideas のために [topic]. For each idea, give a one-sentence description と one potential challenge.

text

# ## Classification
Classify その followでg customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) と a brief reason.

Feedback: [でsert text]

# ## Translation と Style
Translate その followでg 英語 text to Spanish. Use an でのためにmal tone suitable のために a social media post.
Text: [でsert text]

---

# # Evaluation の Prompts

Treat prompts as code: version そのm, test そのm, と iterate.

- **A/B test** different prompt variants on a held-out set の queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scorでg).
- **Keep a prompt registry** (a simple text file or spreadsheet) と その prompt, version, と observed perのためにmance.

---