# Prompt Engineering

Prompt engineering वह प्रक्रिया है जिसमें input prompts को इस तरह डिज़ाइन, परिष्कृत और optimise किया जाता है कि language model से सर्वोत्तम संभव output प्राप्त हो सके। यह कला भी है और विज्ञान भी, और fine-tuning किए बिना LLM behaviour को नियंत्रित करने का यह प्रमुख interface है।

---

## मूल सिद्धांत

### स्पष्टता और विशिष्टता
एक स्पष्ट prompt अस्पष्टता की गुंजाइश नहीं छोड़ता। आप क्या चाहते हैं, इसे ठीक-ठीक बताएँ — format, length और perspective सहित।

**अस्पष्ट:**
> "मुझे Python के बारे में बताओ।"

**विशिष्ट:**
> "Python के Global Interpreter Lock (GIL) को समझाइए। Multithreading पर उसके प्रभाव का वर्णन कीजिए, एक workaround दीजिए, और उत्तर 200 शब्दों से कम रखिए।"

### संदर्भ प्रदान करें
जब models को role, audience और goal पता होता है, तब वे बेहतर प्रदर्शन करते हैं।

**संदर्भ के बिना:**
> "एक function लिखो जो list को sort करे।"

**संदर्भ के साथ:**
> "आप एक senior Python developer हैं। एक function लिखिए जो किसी दिए गए key के आधार पर dictionaries की list को sort करे। type hints का उपयोग करें और edge cases को handle करें। श्रोता junior developers हैं।"

### सकारात्मक निर्देशों का उपयोग करें
मॉडल को यह बताइए कि क्या करना है, यह नहीं कि क्या टालना है। "जटिल शब्दों का उपयोग मत करो" की तुलना में "10 साल के बच्चे के लिए सरल भाषा का उपयोग करो" अधिक प्रभावी है।

---

## Prompt संरचनाएँ

### System / User / Assistant Roles
अधिकांश LLM APIs multi-turn structure को support करती हैं:

- **System message**: model का behaviour, persona और constraints सेट करता है (पूरे session के लिए बना रहता है)।
- **User message**: वर्तमान query या instruction।
- **Assistant message**: model के पिछले responses (continuity के लिए उपयोग किए जाते हैं)।

**उदाहरण (OpenAI API style):**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
कार्य करवाने से पहले इच्छित input-output format के 2–3 examples दें। इससे pattern सिखाया जाता है।

**उदाहरण:**
User: इन वाक्यों को passive voice में बदलिए:
Input: बिल्ली ने चूहे का पीछा किया।
Output: चूहे का पीछा बिल्ली द्वारा किया गया।
Input: रसोइए ने भोजन पकाया।
Output: भोजन रसोइए द्वारा पकाया गया।
Input: तूफ़ान ने घर को नष्ट कर दिया।
Output: (model completes)

### Chain-of-Thought (CoT)
मॉडल को step by step अपनी reasoning दिखाने के लिए प्रोत्साहित करें। इससे arithmetic, logic और multi-step tasks में accuracy सुधरती है।

**CoT के बिना:**
> "24 × 37 कितना है?"

**CoT के साथ:**
> "24 × 37 की गणना कीजिए। अपनी reasoning step by step दिखाइए।"

मॉडल intermediate steps उत्पन्न करेगा, जिससे arithmetic errors कम होंगे।

### Structured Outputs
Parsing को reliable बनाने के लिए JSON, YAML, या markdown tables जैसा विशिष्ट format माँगें।
User: microservices के तीन pros और तीन cons सूचीबद्ध करें। केवल एक valid JSON object लौटाएँ, जिसमें keys "pros" और "cons" हों, और दोनों strings की arrays हों।

---

## उन्नत तकनीकें

### Self-Consistency
एक ही prompt के लिए कई responses उत्पन्न करें (temperature > 0 के साथ) और final answer पर majority vote लें। यह reasoning tasks के लिए विशेष रूप से प्रभावी है।

### Tree-of-Thoughts
कई reasoning paths को parallel में explore करें, प्रत्येक का मूल्यांकन करें, और सबसे बेहतर चुनें। यह research-level technique है, लेकिन model से "alternative solutions explore करें" कहकर इसका लगभग उपयोग किया जा सकता है।

### ReAct (Reasoning + Acting)
मॉडल को reasoning को tool calls के साथ interleave करने दें। यह सोच सकता है, फिर act कर सकता है (उदा., web search, code run), और फिर परिणाम के आधार पर दोबारा सोच सकता है।

**Prompt structure:**
आपके पास एक calculator और एक search engine की पहुँच है। प्रत्येक step के लिए output दें:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### Persona Assignment
उत्तर की शैली निर्धारित करने के लिए एक विशिष्ट persona असाइन करें।

**उदाहरण:**
- "आप एक Linux kernel developer हैं जो memory management को एक नए graduate को समझा रहे हैं।"
- "आप एक friendly nutritionist हैं जो किसी client को सामान्य सलाह दे रहे हैं।"
- "आप एक cynical tech critic हैं जो एक नए gadget की समीक्षा कर रहे हैं।"

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): randomness नियंत्रित करता है। कम = अधिक deterministic, अधिक = अधिक creative। तथ्यात्मक उत्तरों के लिए 0.0–0.3; creative writing के लिए 0.7–1.0 का उपयोग करें।
- **Top-p** (nucleus sampling): probability mass को एक निश्चित cumulative threshold पर काट देता है। 0.9 का अर्थ है कि model सबसे संभावित 90% tokens में से sample करता है। सामान्यतः temperature या top-p में से किसी एक को समायोजित करें, दोनों को नहीं।
- **Max tokens**: अधिकतम output length सेट करता है। ध्यान रखें कि context window के भीतर response के लिए पर्याप्त space सुरक्षित हो।
- **Frequency penalty**: एक ही tokens की पुनरावृत्ति कम करता है।
- **Presence penalty**: model को नए topics प्रस्तुत करने के लिए प्रोत्साहित करता है।

---

## सामान्य समस्याएँ और समाधान

| Problem | संभावित कारण | समाधान |
|---------|--------------|--------|
| Model prompt के कुछ हिस्सों को नज़रअंदाज़ करता है | Prompt बहुत लंबा या overload है | इसे छोटा करें; सबसे महत्वपूर्ण instruction अंत में रखें |
| Output बहुत verbose है | Length constraint नहीं है | "Limit to 3 sentences" जोड़ें या `max_tokens` सेट करें |
| Output बहुत terse है | अत्यधिक restrictive prompt | "Explain in detail" जोड़ें या temperature कम करें |
| Factual hallucinations | अपर्याप्त context या अस्पष्ट प्रश्न | "If you are unsure, say 'I don't know'" जोड़ें और RAG context दें |
| Formatting असंगत है | Format instruction स्पष्ट नहीं है | JSON, markdown table, या bullet list माँगें |
| Model गलत भाषा में उत्तर देता है | Language instruction नहीं है | स्पष्ट रूप से "Respond in English" (या अपनी target language) लिखें |

---

## सामान्य कार्यों के लिए Prompt Templates

### Summarisation
निम्नलिखित text का 3 bullet points में सारांश दीजिए। मुख्य तर्कों पर ध्यान दें और विवरणों से बचें।

Text: [insert text]


### Code Generation
एक [language] function लिखिए जो [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
[concept] को [non-expert / university student / child] को समझाइए। जहाँ उपयुक्त हो, analogy का उपयोग करें।

### Brainstorming
[topic] के लिए 10 ideas उत्पन्न कीजिए। प्रत्येक idea के लिए एक एक-वाक्य description और एक संभावित challenge दीजिए।

पाठ

### Classification
निम्नलिखित customer feedback को [positive, neutral, negative] के रूप में classify करें।
Confidence score (0-100) और एक संक्षिप्त reason दें।

Feedback: [insert text]

### Translation with Style
निम्न English text का Spanish में अनुवाद करें। social media post के लिए उपयुक्त informal tone का उपयोग करें।
Text: [insert text]

---

## Prompts का मूल्यांकन

Prompts को code की तरह मानें: उन्हें version करें, test करें, और iterate करें।

- **A/B test** अलग-अलग prompt variants को queries के एक held-out set पर करें।
- **Measure success** human evaluation या automated metrics (उदा., exact match, BLEU, custom scoring) के माध्यम से करें।
- **Keep a prompt registry** (एक simple text file या spreadsheet) जिसमें prompt, version और observed performance दर्ज हो।

---
