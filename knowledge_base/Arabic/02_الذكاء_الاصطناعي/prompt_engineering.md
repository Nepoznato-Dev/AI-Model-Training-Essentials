<!-- 
This file was automatically translated from English to Arabic.
Source: prompt_engineering.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# هندسة الـ Prompt

هندسة الـ Prompt هي ممارسة تصميم prompts الإدخال وتنقيحها وتحسينها للحصول على أفضل مخرجات ممكنة من نموذج لغوي. وهي تجمع بين الفن والعلم، وتمثل الواجهة الأساسية للتحكم في سلوك LLMs دون الحاجة إلى fine-tuning.

---

## المبادئ الأساسية

### الوضوح والتحديد
يترك الـ prompt الواضح مساحة قليلة للغموض. حدد ما تريده بدقة، بما في ذلك الصيغة، والطول، والمنظور.

**غامض:**
> "Tell me about Python."

**محدد:**
> "Explain Python's Global Interpreter Lock (GIL). Describe its impact on multithreading, give one workaround, and keep your answer under 200 words."

### تقديم السياق
تؤدي النماذج أداءً أفضل عندما تعرف الدور، والجمهور، والهدف.

**دون سياق:**
> "Write a function to sort a list."

**مع سياق:**
> "You are a senior Python developer. Write a function to sort a list of dictionaries by a given key. Use type hints and handle edge cases. The audience is junior developers."

### استخدام التعليمات الإيجابية
أخبر النموذج بما يجب فعله، لا بما يجب تجنبه فقط. عبارة "Don't include jargon" أضعف من "Use simple language accessible to a 10-year-old."

---

## هياكل الـ Prompt

### أدوار System / User / Assistant
تدعم معظم واجهات LLMs بنية محادثة متعددة الأدوار:

- **System message**: يحدد سلوك النموذج، وشخصيته، وقيوده، ويستمر عادة طوال الجلسة.
- **User message**: الاستعلام أو التعليمة الحالية.
- **Assistant message**: ردود النموذج السابقة، وتستخدم للحفاظ على الاستمرارية.

**مثال بأسلوب OpenAI API:**
```text
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.
```

### Few-Shot Prompting
قدّم مثالين أو ثلاثة من صيغة الإدخال والمخرجات المطلوبة قبل أن تطلب من النموذج تنفيذ المهمة. يعلّم ذلك النموذج النمط المطلوب.

**مثال:**
```text
User: Convert these sentences to passive voice:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)
```

### Chain-of-Thought (CoT)
شجّع النموذج على عرض تفكيره خطوة بخطوة. يحسّن ذلك الدقة في الحساب، والمنطق، والمهام متعددة الخطوات.

**دون CoT:**
> "What is 24 × 37?"

**مع CoT:**
> "Calculate 24 × 37. Show your reasoning step by step."

سينتج النموذج خطوات وسيطة، مما يقلل أخطاء الحساب.

### المخرجات المنظمة
اطلب صيغة محددة مثل JSON أو YAML أو جداول Markdown لجعل التحليل الآلي للمخرجات أكثر موثوقية.

```text
User: List three pros and three cons of microservices. Return only a valid JSON object with keys "pros" and "cons", each an array of strings.
```

---

## تقنيات متقدمة

### Self-Consistency
ولّد عدة إجابات للـ prompt نفسه، مع `temperature > 0`، ثم استخدم تصويت الأغلبية على الإجابة النهائية. تكون هذه التقنية فعالة خصوصاً في مهام الاستدلال.

### Tree-of-Thoughts
استكشف عدة مسارات استدلالية بالتوازي، وقيّم كلاً منها، ثم اختر الأفضل. هذه تقنية بحثية متقدمة، لكن يمكن تقريبها بطلب "explore alternative solutions" من النموذج.

### ReAct (Reasoning + Acting)
اسمح للنموذج بالمزج بين الاستدلال واستدعاءات الأدوات. يمكنه أن يفكر، ثم ينفذ إجراءً مثل البحث في الويب أو تشغيل كود، ثم يعيد التفكير بناءً على النتيجة.

**بنية الـ prompt:**
```text
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.
```

### إسناد شخصية
امنح النموذج شخصية محددة لتأطير الإجابة.

**أمثلة:**
- "You are a Linux kernel developer explaining memory management to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## ضبط المعاملات

- **Temperature** (0.0 – 1.0+): يتحكم في العشوائية. القيم الأقل أكثر حتمية، والقيم الأعلى أكثر إبداعاً. استخدم 0.0–0.3 للإجابات الواقعية، و0.7–1.0 للكتابة الإبداعية.
- **Top-p** (nucleus sampling): يقتطع كتلة الاحتمالات عند عتبة تراكمية معينة. تعني 0.9 أن النموذج يختار من أعلى 90% من tokens المرجحة. عادةً اضبط إما temperature أو top-p، لا كليهما.
- **Max tokens**: يحدد الحد الأقصى لطول المخرجات. تذكّر حجز مساحة للإجابة ضمن نافذة السياق.
- **Frequency penalty**: يقلل تكرار tokens نفسها.
- **Presence penalty**: يشجع النموذج على إدخال موضوعات جديدة.

---

## أخطاء شائعة وإصلاحاتها

| المشكلة | السبب المحتمل | الإصلاح |
|---------|--------------|-----|
| يتجاهل النموذج أجزاء من الـ prompt | الـ prompt طويل جداً أو محمّل بتعليمات كثيرة | اختصره؛ وضع أهم تعليمة في النهاية |
| المخرجات مطولة جداً | لا يوجد قيد على الطول | أضف "Limit to 3 sentences" أو اضبط `max_tokens` |
| المخرجات مقتضبة جداً | القيود صارمة أكثر من اللازم | أضف "Explain in detail" أو خفّض temperature |
| هلوسات معرفية | سياق غير كافٍ أو سؤال ملتبس | أضف "If you are unsure, say 'I don't know'" ووفّر سياق RAG |
| تنسيق غير متسق | لا توجد تعليمة صريحة للتنسيق | اطلب JSON أو جدول Markdown أو قائمة نقطية |
| يجيب النموذج بلغة خاطئة | لا توجد تعليمة لغة | اذكر صراحة "Respond in English" أو اللغة المطلوبة |

---

## قوالب Prompt لمهام شائعة

### التلخيص
```text
Summarise the following text in 3 bullet points. Focus on the main arguments and avoid details.

Text: [insert text]
```

### توليد الكود
```text
Write a [language] function that [does X].
Requirements:
- Use type hints.
- Include a docstring.
- Handle edge cases: [list].
- Do not use external libraries unless specified.
```

### الشرح
```text
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.
```

### العصف الذهني
```text
Generate 10 ideas for [topic]. For each idea, give a one-sentence description and one potential challenge.
```

### التصنيف
```text
Classify the following customer feedback as [positive, neutral, negative].
Provide a confidence score (0-100) and a brief reason.

Feedback: [insert text]
```

### الترجمة مع الأسلوب
```text
Translate the following English text to Spanish. Use an informal tone suitable for a social media post.
Text: [insert text]
```

---

## تقييم الـ Prompts

عامل prompts كما تعامل الكود: ضع لها إصدارات، واختبرها، وكرر تحسينها.

- **اختبار A/B**: جرّب نسخاً مختلفة من الـ prompt على مجموعة محفوظة من الاستعلامات.
- **قياس النجاح**: استخدم التقييم البشري أو مقاييس آلية مثل exact match وBLEU أو مقاييس مخصصة.
- **الاحتفاظ بسجل prompts**: استخدم ملفاً نصياً بسيطاً أو جدولاً يضم الـ prompt، والإصدار، والأداء المرصود.
