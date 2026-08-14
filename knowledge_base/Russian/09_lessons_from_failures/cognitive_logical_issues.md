---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Когнитивные искажения и логические заблуждения
В этом документе объединены когнитивные предубеждения, логические заблуждения и ошибки рассуждения, которые влияют как на принятие решений человеком, так и на результаты системы ИИ.
---

## Когнитивные искажения
Когнитивные искажения — это систематические отклонения от рациональности в суждениях и принятии решений. В разработке программного обеспечения и системах искусственного интеллекта это может привести к неправильным проектным решениям, ошибочным требованиям и предвзятому поведению модели.
### Предвзятость подтверждения
**Что это такое:** Тенденция искать, интерпретировать и вспоминать информацию таким образом, чтобы подтвердить ранее существовавшие убеждения.
**Плохой пример в разработке:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**В обзорах кода:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Устранение последствий:**
- Активно искать опровергающие доказательства.
- Используйте слепые проверки кода.
- Поощрять инакомыслие.
- Четко документируйте предположения.
### Смещение привязки
**Что это такое:** слишком сильно полагаться на первую попавшуюся информацию.
**Плохой пример:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Устранение последствий:**
- Получите несколько независимых оценок
- Используйте покер планирования для оценки
- Рассмотрите диапазоны вместо точечных оценок.
- Справочные исторические данные
### Заблуждение о невозвратных издержках
**Что это такое:** Продолжение начинания с использованием ранее вложенных ресурсов (время, деньги, усилия), даже если лучше отказаться от него.
**Плохой пример:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Устранение последствий:**
- Оценивать решения на основе будущей стоимости, а не прошлых инвестиций.
- Регулярно переоценивать жизнеспособность проекта.
- Создать психологическую безопасность при повороте
- Используйте объективные критерии для принятия решений о продолжении/остановке
### Эвристика доступности
**Что это**: переоценка важности легкодоступной или свежей информации.
**Плохой пример:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Устранение последствий:**
- Используйте принятие решений на основе данных.
- Ознакомьтесь с комплексными моделями угроз.
- Посмотрите базовые ставки и статистику
- Избегайте предвзятости в отношении новизны при расстановке приоритетов.
### Эффект Даннинга-Крюгера
**Что это такое:** Люди с низкими способностями к выполнению задачи переоценивают свои способности; эксперты могут недооценивать свои.
**Плохой пример:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Устранение последствий:**
- Поощрять непрерывное обучение
- Внедрить процессы экспертной оценки
- Создавать программы наставничества.
- Воспитывать смирение и любознательность.
---

## Логические ошибки
Логические ошибки — это ошибки в рассуждениях, которые подрывают достоверность аргументов. Модели ИИ могут выдавать результаты, содержащие эти заблуждения.
### Ad Hominem (Нападение на личность)
**Что это такое:** Нападение на человека, выдвигающего аргумент, а не на сам аргумент.
**Плохой пример:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Почему это плохо.** Действительность отзыва зависит от его содержания, а не от стажа рецензента.
### Обращение к властям
**Что это такое:** Утверждение о чем-то является правдой, потому что так говорит авторитетный деятель, без каких-либо доказательств.
**Плохой пример:**```markdown
"This architecture must be correct because Google uses it."
```

**Почему это плохо.** То, что работает для Google в их масштабе, может не подойти для вашего варианта использования.
### Ложная дихотомия (черно-белое мышление)
**Что это такое:** представлены только два варианта, если их существует больше.
**Плохой пример:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Реальность:** Между этими крайностями существует множество вариантов (оптимизировать «горячие пути», использовать Rust для конкретных компонентов, улучшить код Python и т. д.).
### Скользкий склон
**Что это такое:** Утверждение, что одно событие неизбежно приведет к цепочке негативных последствий.
**Плохой пример:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Почему это плохо:** предполагает неизбежное прогрессирование без каких-либо доказательств; игнорирует смягчающие факторы.
### Круговое рассуждение
**Что это такое:** использование вывода в качестве предпосылки.
**Плохой пример:**```markdown
"Our code is high quality because we write good code."
```

### Post hoc Ergo Propter Hoc (ложная причина)
**Что это такое:** Предположим, что, поскольку B последовал за A, A вызвало B.
**Плохой пример:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Реальность:** Корреляция не подразумевает причинно-следственной связи. Другие факторы могут быть ответственными.
### Соломенный человечек
**Что это такое:** Искажение чьих-либо аргументов с целью облегчить атаку.
**Плохой пример:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Заблуждение о победе
**Что это такое:** Спорить о чем-то правильно, потому что многие люди в это верят.
**Плохой пример:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Почему это плохо:** Популярность не гарантирует соответствия вашим конкретным потребностям.
---

## Обоснование ошибок в искусственном интеллекте
### Многоэтапные логические ошибки
**Плохой пример:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Почему это плохо:**
- Совершает ошибку, утверждая следствие
- Алиса могла писать код, не будучи программистом
- Логическая структура: (P→Q, Q) ⊬ P
**Правильное рассуждение:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Ошибки в математических рассуждениях
**Плохой пример:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Реальность:** Если мяч стоит 0,10 доллара, а бита стоит на 1 доллар больше (1,10 доллара), общая сумма составит 1,20 доллара. Правильный ответ: 0,05 доллара за мяч и 1,05 доллара за биту.
### Причинно-следственные ошибки
**Плохой пример:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Реальность:** Оба заболевания вызваны третьим фактором (жаркой погодой), а не друг другом.
---

## Стратегии улучшения
### Для принятия решений человеком
1. **Тренинг по повышению осведомленности**: научитесь распознавать распространенные предубеждения.
2. **Использование контрольных списков**. Используйте контрольные списки для принятия решений, чтобы противодействовать предвзятости.
3. **Разнообразные команды**. Включайте людей с разными точками зрения.
4. **Предварительный анализ**: представьте себе неудачу и действуйте в обратном направлении, чтобы выявить причины.
5. **Документация**: запишите обоснование для последующего рассмотрения.
### Для систем искусственного интеллекта
1. **Подсказка по цепочке мыслей**: попросите модель показать этапы рассуждения.
2. **Самокоррекция**. Попросите модель просмотреть и критически оценить свои ответы.
3. **Формальная проверка**. Используйте инструменты символического рассуждения для критической логики.
4. **Декомпозиция**: разбивайте сложные проблемы на более мелкие этапы.
5. **Внешние инструменты**: используйте калькуляторы и решатели для решения математических задач.
6. **Несколько образцов**: создайте несколько ответов и сравните их.
---

## Похожие темы
- **Ошибки AI/LLM**: информацию о галлюцинациях и проблемах с рассуждением см. в `ai_llm_failures.md`.
- **Противоречивые источники**: см. документацию по оценке противоречивой информации.
- **Критическое мышление**: применяйте эти концепции для оценки аргументов и доказательств.
- **Быстрое проектирование**: см. `../02_artificial_intelligence/prompt_engineering.md`, чтобы узнать о методах уменьшения ошибок в рассуждениях.
---

## Дополнительные когнитивные искажения при разработке программного обеспечения
### Предвзятость статус-кво
**Что это такое:** предпочтение сохранения текущего состояния; любое изменение воспринимается как потеря.
**Плохой пример:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Устранение последствий:**
- Количественно оценить затраты, связанные с отсутствием изменений.
- Установите регулярные графики обновлений.
- Создать безопасную среду для экспериментов.
- Воспринимайте изменения как возможности, а не угрозы.
### Предвзятость оптимизма
**Что это такое:** недооценка времени, затрат и рисков при переоценке выгод.
**Плохой пример:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Устранение последствий:**
- Используйте прогнозирование эталонного класса (сравните с аналогичными прошлыми проектами)
- Добавьте резервы на случай непредвиденных обстоятельств (20-50%)
- Провести предсмертные исследования.
- Отслеживание точности оценки с течением времени
### Предвзятость выжившего
**Что это такое:** Сосредоточьтесь на успешных примерах, игнорируя неудачи.
**Плохой пример:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Устранение последствий:**
- Изучите как успехи, так и неудачи.
- Ищите базовые ставки и статистику
- Учитывайте невидимые данные
- Избегайте выборочных примеров.
### Фундаментальная ошибка атрибуции
**Что это такое:** приписывание поведения других людям характеру, а не обстоятельствам.
**Плохой пример:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Устранение последствий:**
- Учитывайте ситуационные факторы.
- Практикуйте сочувствие
- Сосредоточьтесь на системах, а не на отдельных людях.
- Используйте безупречные вскрытия
### Предвзятость ретроспективного взгляда
**Что это такое:** после того, как событие произошло, вера в то, что оно было предсказуемо с самого начала.
**Плохой пример:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Устранение последствий:**
- Документируйте прогнозы до результатов
- Анализируйте контекст решения, а не только результаты.
- Избегайте культуры «Я же вам говорил»
- Сосредоточьтесь на улучшении процессов, а не на обвинении
---

## Больше логических ошибок
### Обращение к новизне
**Что это такое:** предположение, что что-то лучше, потому что оно новее.
**Плохой пример:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Обращение к традициям
**Что это такое:** Спорить о чем-то правильно, потому что так делалось всегда.
**Плохой пример:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Обращение к лицемерию)
**Что это такое:** Отклонение критики путем указания на непоследовательность критика.
**Плохой пример:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Загруженный вопрос
**Что это такое:** вопрос, содержащий предположение.
**Плохой пример:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Нет настоящего шотландца
**Что это такое:** Создание исключения из универсального требования, когда оно оспаривается.
**Плохой пример:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Генетическая ошибка
**Что это такое:** оценка чего-либо на основе его происхождения, а не текущих достоинств.
**Плохой пример:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Заблуждение среднего плана
**Что это такое:** Предполагать, что истина всегда находится посередине между двумя крайностями.
**Плохой пример:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Когнитивные искажения в системах искусственного интеллекта
### Смещение обучающих данных
Модели ИИ наследуют предвзятости, присутствующие в их обучающих данных.
**Пример:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Устранение последствий:**
- Аудит данных обучения на предмет предвзятости
- Используйте методы устранения предвзятости.
- Проверка смещенных выходов
- Разнообразный сбор данных
### Предвзятость автоматизации
**Что это такое:** чрезмерная зависимость от автоматизированных систем, даже если они ошибаются.
**Пример:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Устранение последствий:**
- Поддерживать человеческий контроль.
- Поощрять критическую оценку результатов ИИ.
- Не считайте ИИ непогрешимым.
- Внедрить процессы проверки
### Иллюзия понимания
**Что это такое:** Вера в то, что вы понимаете, как работает ИИ, хотя на самом деле это не так.
**Пример:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Устранение последствий:**
- Информируйте пользователей об ограничениях ИИ.
- Будьте прозрачны в отношении того, как работают системы.
- Избегайте антропоморфизации ИИ
- Установите соответствующие ожидания
---

## Тематические исследования
### Пример 1: Предвзятость подтверждения при выборе архитектуры
**Инцидент:** Команда выбрала микросервисную архитектуру для небольшого приложения.
**Основная причина.** Руководитель группы прочитал несколько статей, восхваляющих микросервисы и 
искал только информацию, подтверждающую этот выбор, игнорируя предупреждения о сложности.
**Влияние:**
- Огромные накладные расходы для команды из 3 разработчиков.
- Сложность развертывания увеличена в 10 раз.
- Производительность снизилась из-за сетевых вызовов.
- Проект задерживается на 6 месяцев.
**Урок.** Оценивайте архитектуру на основе вашего конкретного контекста, а не только 
положительные отзывы. Подробно рассмотрите компромиссы.
### Пример 2: Невозвратные затраты в устаревшей системе
**Инцидент:** Компания продолжала поддерживать специальную CRM-систему в течение 5 лет. 
несмотря на лучшие альтернативы.
**Основная причина:** «Мы уже вложили 2 миллиона долларов, сейчас мы не можем от них отказаться».
**Влияние:**
- Ежегодная стоимость обслуживания: 500 тыс. долларов США.
- Альтернативная стоимость: невозможно использовать современные функции.
- Проблемы с удержанием талантов (разработчики хотели работать с современными технологиями)
- Общие затраты на 5 лет: 4,5 млн долларов против 1,5 млн долларов для альтернативы SaaS.
**Урок:** Прошлые инвестиции обанкротились. Принимайте решения, исходя из будущей стоимости.
### Пример 3: Эвристика доступности в сфере безопасности
**Инцидент:** Команда уделяла приоритетное внимание защите от недавно получившей огласку атаки. 
вектор, игнорируя при этом более вероятные угрозы.
**Основная причина.** Недавние новости сделали один тип угроз очень доступным. 
в памяти, искажая оценку риска.
**Влияние:**
- Потратил 100 тысяч долларов на устранение маловероятной угрозы.
- Фактическое нарушение произошло по неучтенному вектору.
- Стоимость восстановления: $500 тыс.+
**Урок:** Используйте моделирование угроз на основе данных, а не расстановку приоритетов на основе давности.
---

## Практические упражнения
### Упражнение по обнаружению предвзятости
Просмотрите недавние решения и спросите:
1. Какие предположения мы сделали?
2. Какие доказательства противоречат нашему выводу?
3. Рассматривали ли мы несколько вариантов или остановились на первой идее?
4. Продолжаем ли мы ради будущей стоимости или прошлых инвестиций?
5. Что бы мы порекомендовали, если бы нас спросили?
### Обнаружение логических ошибок
Попрактикуйтесь в выявлении ошибок в повседневных обсуждениях:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Техника предсмертного исследования
Прежде чем начать проект:
1. Представьте, что это произойдет через 6 месяцев в будущем.
2. Проект с треском провалился
3. Напишите историю о том, почему это не удалось
4. Работайте в обратном направлении, чтобы предотвратить эти виды сбоев.
Это противоречит предвзятости оптимизма и эвристике доступности.
---

## Инструменты и платформы
### Шаблон журнала решений
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Контрольный список предвзятости
Прежде чем принимать важные решения:
- [ ] Искали ли мы опровергающие доказательства?
- [ ] Зависим ли мы от исходной информации?
- [ ] Влияют ли на нас невозвратные издержки?
- [ ] Не слишком ли мы самоуверенны в своих оценках?
- [ ] Учитывали ли мы базовые ставки?
- [ ] Поддаемся ли мы предвзятости доступности/новизны?
- [ ] Сделаем ли мы тот же выбор, если начнем все сначала?
### Упражнение Красной команды
Назначьте кого-нибудь, кто будет аргументировать против предложенного решения:
- Их роль – находить недостатки
- Они должны представлять альтернативные точки зрения
- Команда практикует конструктивное реагирование на критику.
- Проблемы с документами, поднятые и решенные
Это противостоит предвзятости подтверждения и групповому мышлению.