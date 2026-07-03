# Промпт-инжиниринг

Prompt engineering — это практика проектирования, доработки и оптимизации входных prompts, чтобы получать от языковой модели максимально качественный результат. Это одновременно и искусство, и наука, а также основной интерфейс управления поведением LLM без fine-tuning.

---

## Основные принципы

### Ясность и конкретность
Чёткий prompt не оставляет места для неоднозначности. Точно указывайте, что именно вы хотите получить, включая формат, длину и перспективу изложения.

**Расплывчато:**
> "Расскажи мне о Python."

**Конкретно:**
> "Объясни Global Interpreter Lock (GIL) в Python. Опиши, как он влияет на multithreading, приведи один способ обхода и уложись в 200 слов."

### Предоставляйте контекст
Модели работают лучше, когда знают роль, аудиторию и цель.

**Без контекста:**
> "Напиши функцию для сортировки списка."

**С контекстом:**
> "Ты senior Python developer. Напиши функцию для сортировки списка словарей по заданному ключу. Используй type hints и обработай edge cases. Аудитория — junior developers."

### Используйте позитивные инструкции
Говорите модели, что нужно сделать, а не только чего избегать. Формулировка "Don't include jargon" слабее, чем "Use simple language accessible to a 10-year-old."

---

## Структуры prompts

### Роли System / User / Assistant
Большинство LLM APIs поддерживают многошаговую структуру:

- **System message**: задаёт поведение модели, persona и ограничения (сохраняется на всю сессию).
- **User message**: текущий запрос или инструкция.
- **Assistant message**: предыдущие ответы модели (используются для continuity).

**Пример (в стиле OpenAI API):**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Перед тем как просить модель выполнить задачу, приведите 2–3 примера желаемого формата «вход-выход». Так вы обучаете её нужному шаблону.

**Пример:**
User: Convert these sentences to passive voice:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)

### Chain-of-Thought (CoT)
Попросите модель показывать ход рассуждений шаг за шагом. Это повышает точность в арифметике, логике и многошаговых задачах.

**Без CoT:**
> "Сколько будет 24 × 37?"

**С CoT:**
> "Вычисли 24 × 37. Покажи ход рассуждений шаг за шагом."

Модель будет выдавать промежуточные шаги, уменьшая количество арифметических ошибок.

### Structured Outputs
Запрашивайте конкретный формат, например JSON, YAML или markdown tables, чтобы разбор результата был надёжным.
User: List three pros and three cons of microservices. Return only a valid JSON object with keys "pros" and "cons", each an array of strings.

---

## Продвинутые техники

### Self-Consistency
Сгенерируйте несколько ответов на один и тот же prompt (с temperature > 0), а затем выберите итоговый ответ большинством голосов. Это особенно эффективно для задач на рассуждение.

### Tree-of-Thoughts
Исследуйте несколько путей рассуждения параллельно, оцените каждый и выберите лучший. Это техника исследовательского уровня, но её можно приблизительно воспроизвести, попросив модель "explore alternative solutions."

### ReAct (Reasoning + Acting)
Позвольте модели чередовать рассуждение с вызовами инструментов. Она может подумать, затем выполнить действие (например, поискать в web или запустить код), а затем снова рассуждать на основе результата.

**Структура prompt:**
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### Назначение persona
Задайте конкретную persona, чтобы определить рамку ответа.

**Примеры:**
- "You are a Linux kernel developer explaining memory management to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Настройка параметров

- **Temperature** (0.0 – 1.0+): управляет случайностью. Ниже = более детерминированно, выше = более креативно. Используйте 0.0–0.3 для фактических ответов; 0.7–1.0 для творческого письма.
- **Top-p** (nucleus sampling): отсекает распределение вероятностей на заданном накопленном пороге. 0.9 означает, что модель выбирает из верхних 90% наиболее вероятных tokens. Обычно настраивают либо temperature, либо top-p, но не оба сразу.
- **Max tokens**: задаёт максимальную длину вывода. Не забывайте оставлять место для ответа внутри context window.
- **Frequency penalty**: уменьшает повторение одних и тех же tokens.
- **Presence penalty**: побуждает модель вводить новые темы.

---

## Типичные проблемы и способы исправления

| Проблема | Вероятная причина | Исправление |
|---------|--------------|-------------|
| Модель игнорирует части prompt | Prompt слишком длинный или перегружен | Сократите его; самую важную инструкцию поместите в конец |
| Вывод слишком многословный | Нет ограничения по длине | Добавьте "Limit to 3 sentences" или задайте `max_tokens` |
| Вывод слишком краткий | Слишком жёсткие ограничения | Добавьте "Explain in detail" или уменьшите temperature |
| Фактические hallucinations | Недостаточно контекста или вопрос двусмысленный | Добавьте "If you are unsure, say 'I don't know'" и предоставьте RAG-контекст |
| Непоследовательное форматирование | Нет явного указания формата | Попросите JSON, markdown table или bullet list |
| Модель отвечает не на том языке | Нет указания языка | Явно напишите "Respond in English" (или на нужном языке) |

---

## Шаблоны prompts для типовых задач

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

## Оценка prompts

Относитесь к prompts как к коду: версионируйте их, тестируйте и итеративно улучшайте.

- **A/B test** разные варианты prompts на отложенном наборе запросов.
- **Measure success** через human evaluation или автоматические метрики (например, exact match, BLEU, custom scoring).
- **Keep a prompt registry** (простой текстовый файл или spreadsheet) с самим prompt, версией и наблюдаемой производительностью.

---
