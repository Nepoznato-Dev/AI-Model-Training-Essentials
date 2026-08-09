---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [scratch, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Царапать
Scratch — это визуальный блочный язык программирования, разработанный Медиа-лабораторией Массачусетского технологического института и впервые выпущенный в 2007 году. Вместо написания текстового кода пользователи объединяют цветные блоки для создания программ. Scratch разработан специально для детей в возрасте от 8 до 16 лет (хотя его используют ученики всех возрастов) для обучения фундаментальным концепциям программирования — циклам, условным выражениям, переменным, событиям и функциям — без барьера синтаксических ошибок.
Scratch — наиболее широко используемый вводный язык программирования в мире, с более чем 100 миллионами зарегистрированных пользователей и доступный на более чем 70 языках. Он запускается в веб-браузере и бесплатен.
---

## Почему Scratch имеет значение
- **Лучшее введение в программирование**: полностью устраняет синтаксические барьеры. Концепции преподаются посредством визуальных манипуляций.
- **Вычислительное мышление**: обучает декомпозиции, распознаванию образов, абстракции и разработке алгоритмов.
- **Творческий подход**: дети создают игры, анимации, истории и музыку, а изучение программирования является побочным продуктом создания вещей, которые им интересны.
- **Глобальный охват**: используется в школах по всему миру. Доступно на более чем 70 языках. Бесплатно и через браузер.
- **Сообщество**: онлайн-сообщество Scratch учит совместному использованию, созданию ремиксов и совместному обучению.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Не настоящий язык программирования** | Невозможно создать производственное программное обеспечение, API или системы | Переход на Python, JavaScript или текстовые языки |
| **Ограниченные возможности** | Никакого файлового ввода-вывода, сети или расширенных структур данных | Используйте для обучения; переход на текстовые языки для реальных проектов |
| **Производительность** | Интерпретация, медленная для сложных проектов | Не предназначен для критически важной работы |
| **Восприятие возраста** | Часто рассматривается как «только для детей» | Scratch — это инструмент обучения, а не профессиональный язык |
---

## Как работает Скретч
Программы Scratch (называемые «проектами») состоят из **спрайтов** (символов/объектов), которые реагируют на **блоки**, соединенные вместе в скриптах.
### Основные понятия (обучаются с помощью блоков)
| Концепция | Категория скретч-блоков | Пример |
|---------|----------------------|---------|
| **Последовательности** | Движение, Внешний вид | «Перейди на 10 шагов», затем «Скажи привет» |
| **Петли** | Контроль (желтый) | «Повторить 10», «Навсегда», «Повторить до» |
| **Условные** | Контроль (желтый) | «Если... то», «Если... то... иначе» |
| **Переменные** | Переменные (оранжевый) | «Установить оценку на 0», «Изменить оценку на 1» |
| **События** | События (желтый) | «При нажатии зеленого флажка», «При нажатии клавиши» |
| **Функции** | Мои блоки (по индивидуальному заказу) | Определить повторно используемые последовательности блоков |
| **Списки (массивы)** | Переменные (оранжевый) | «Добавить в список», «Элемент списка» |
| **Вещание** | События | Отправка сообщений между спрайтами |
### Пример: простая игровая логика
```
When green flag clicked:
  Set [score] to 0
  Forever:
    If <touching [enemy]?> then:
      Change [score] by -1
      Play sound [ouch]
    If <touching [coin]?> then:
      Change [score] by 1
      Go to random position
```

---

## Расширенный синтаксис и шаблоны
### Категории блоков в деталях
Scratch 3.0 распределяет блоки по категориям с цветовой кодировкой:
| Категория | Цвет | Типы блоков |
|----------|--------|-------------|
| **Движение** | Синий | перемещение, поворот, переход, скольжение, точка, изменение x/y |
| **Внешность** | Фиолетовый | сказать, подумать, сменить костюм, изменить размер, показать/спрятать |
| **Звук** | Розовый | воспроизвести звук, остановить звуки, изменить громкость, изменить высоту звука |
| **События** | Желтый | при нажатии флага, при нажатии клавиши, при нажатии спрайта, трансляция |
| **Управление** | Золото | подожди, повтори, навсегда, если, если-иначе, повтори, пока, остановись |
| **Ощущение** | Голубой | прикосновение, нажатие клавиши, мышь, расстояние, вопрос/ответ, таймер |
| **Операторы** | Зеленый | математические операции, текстовые операции, сравнение и/или/нет, случайные |
| **Переменные** | Оранжевый | установить/изменить переменную, операции со списками |
| **Мои блоки** | Темно-красный | пользовательские определения блоков (функции) |
### Расширенные шаблоны блоков
```
// Pattern: Timer-based movement (smooth animation)
When green flag clicked:
  Set [speed] to 5
  Forever:
    Change x by (speed)
    If <(x position) > 200> then
      Set [speed] to ((speed) * -1)
    If <(x position) < -200> then
      Set [speed] to ((speed) * -1)

// Pattern: State machine using variables
When green flag clicked:
  Set [game_state] to [menu]
  Forever:
    If <(game_state) = [menu]> then
      Show
      Go to x: 0 y: 0
    If <(game_state) = [playing]> then
      Hide
    If <(game_state) = [game_over]> then
      Say [Game Over!] for 2 secs

// Pattern: Object-oriented sprite (each sprite manages its own state)
When green flag clicked:
  Set [hp] to 100
  Set [max_hp] to 100
  Set [is_alive] to true
  Forever:
    If <(is_alive) = true> then
      If <touching [enemy]?> then
        Change [hp] by -10
        If <(hp) < 1> then
          Set [is_alive] to false
          Broadcast [player_dead]
```

### Пользовательские блоки (функции)
```
// Define a custom block with parameters
Define: Jump (height) times (count)
  Repeat (count):
    Change y by (height)
    Wait 0.2 seconds
    Change y by ((height) * -1)
    Wait 0.2 seconds

// Usage:
When space key pressed:
  Jump height: 50 times: 3

// Custom block with "run without screen refresh" (optimization)
Define: Draw fractal (depth) (size)
  Run without screen refresh: true
  If <(depth) = 0> then
    Move (size) steps
  Else:
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn left 120 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
```

### Операции со списками (массивы)
```
// Creating and using lists
When green flag clicked:
  Delete all of [scores]
  Add [100] to [scores]
  Add [85] to [scores]
  Add [92] to [scores]
  Add [78] to [scores]
  
  // Access items (1-indexed)
  Set [total] to 0
  Set [i] to 1
  Repeat (length of [scores]):
    Change [total] by (item (i) of [scores])
    Change [i] by 1
  
  Set [average] to ((total) / (length of [scores]))
  Say (join [Average: ] (average)) for 2 secs

// Sorting a list (bubble sort)
Define: Sort List
  Set [n] to (length of [scores])
  Repeat (n)
    Set [i] to 1
    Repeat ((n) - 1)
      If <(item (i) of [scores]) > (item ((i) + 1) of [scores])> then
        // Swap
        Set [temp] to (item (i) of [scores])
        Replace item (i) of [scores] with (item ((i) + 1) of [scores])
        Replace item ((i) + 1) of [scores] with (temp)
      Change [i] by 1
```

### Трансляция (межспрайтовая связь)
```
// Sprite 1 (Player):
When space key pressed:
  Broadcast [fire_bullet]

// Sprite 2 (Bullet):
When I receive [fire_bullet]:
  Go to [Player]
  Show
  Repeat 50:
    Change y by 10
  Hide

// Sprite 3 (Enemy):
When I receive [fire_bullet]:
  If <touching [Bullet]?> then
    Change [hp] by -25
    If <(hp) < 1> then
      Broadcast [enemy_destroyed]
      Hide
```

---

## Архитектура и системный дизайн
### Событийно-ориентированный дизайн
Scratch использует событийно-ориентированную архитектуру. Каждый скрипт начинается с блока событий (шапочного блока) и запускается в ответ на это событие.
```
Event Types:
+-------------------------------------------+
| when [green flag] clicked    (startup)     |
| when [space] key pressed     (keyboard)    |
| when this sprite clicked     (mouse)       |
| when [backdrop] switches to  (stage event) |
| when [loudness] > [10]       (sound)       |
| when I receive [message]     (broadcast)   |
| when video motion > [10]     (camera)      |
+-------------------------------------------+
```

### Структура проекта
```
scratch-project/
├── project.sb3              * Saved project file (ZIP format)
├── sprites/
│   ├── Player/              * Player sprite
│   │   ├── costumes/        * Costume images
│   │   └── sounds/          * Sound files
│   ├── Enemy/
│   │   ├── costumes/
│   │   └── sounds/
│   └── Bullet/
├── stage/
│   ├── backdrops/           * Background images
│   └── sounds/              * Stage sounds
└── README.md
```

### Система клонирования (создание объектов)
```
// Creating clones (like creating object instances)
When green flag clicked:
  Forever:
    Wait 1 seconds
    Create clone of [Enemy]

When I start as a clone:
  Go to random position
  Show
  Set [hp] to 3
  Forever:
    Change y by -3
    If <(y position) < -170> then
      Delete this clone
    If <touching [Bullet]?> then
      Change [hp] by -1
      If <(hp) < 1> then
        Change [score] by 10
        Delete this clone
```

---

## Конфигурация проекта и система сборки
### Расширения Scratch
Scratch поддерживает официальные расширения и расширения сообщества, которые добавляют возможности:
| Расширение | Цель |
|-----------|---------|
| **Ручка** | Рисуйте линии и фигуры на сцене |
| **Видеообнаружение** | Использование веб-камеры для обнаружения движения |
| **Преобразование текста в речь** | Преобразование текста в голосовой звук |
| **Перевести** | Перевести текст между языками |
| **Маки-Макей** | Подключите физические объекты в качестве входных данных |
| **микро:бит** | Подключите оборудование BBC micro:bit |
| **LEGO Mindstorms** | Управляйте роботами LEGO |
| **Музыка** | Игра на музыкальных нотах и ​​инструментах |
### Формат файла скретча
```
Scratch 3.0 projects (.sb3) are ZIP archives containing:
├── project.json             * All scripts, sprites, and metadata
├── [md5hash].svg           * Costume images (SVG or PNG)
├── [md5hash].png           * Additional costumes
└── [md5hash].wav           * Sound files

The project.json contains:
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "costumes": [...],
      "sounds": [...],
      "blocks": {...}
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "position": {"x": 0, "y": 0},
      "blocks": {...}
    }
  ],
  "monitors": [...],
  "meta": {"semver": "3.0.0"}
}
```

### Автономный редактор
```
Scratch Desktop (offline editor) available for:
- Windows 10+ (Microsoft Store or direct download)
- macOS 10.13+
- ChromeOS

Installation:
1. Download from https://scratch.mit.edu/download
2. Install and run — no internet required
3. Projects save as .sb3 files locally
```

---

## Тестирование и отладка
### Встроенные инструменты отладки
Scratch предоставляет несколько встроенных инструментов для отладки проектов:
| Инструмент | Как использовать |
|------|-----------|
| **Режим черепахи** | Щелкните правой кнопкой мыши спрайт и выберите «показать отладку», чтобы увидеть координаты |
| **Вариативные мониторы** | Щелкните правой кнопкой мыши переменную и выберите «Показать», чтобы увидеть ее значение в режиме реального времени |
| **Список мониторов** | Просмотр содержимого списка в обычном режиме, в виде строк или столбцов |
| **Турбо-режим** | Удерживайте Shift, нажимая зеленый флажок для более быстрого выполнения |
| **Одношаговый режим** | Щелкните правой кнопкой мыши зеленый флаг для «одного шага» (замедляет выполнение) |
### Отладка шаблонов
```
// Debug: Display variable values on sprite
When green flag clicked:
  Forever:
    Say (join [Score: ] (score))

// Debug: Visual boundary checking
When green flag clicked:
  Forever:
    If <(x position) > 240> then
      Say [TOO FAR RIGHT!] for 0.5 secs
      Set x to 240
    If <(x position) < -240> then
      Say [TOO FAR LEFT!] for 0.5 secs
      Set x to -240

// Debug: Frame counter
When green flag clicked:
  Set [frames] to 0
  Forever:
    Change [frames] by 1
    If <(frames) mod 30 = 0> then
      Say (join [FPS: ] ((frames) / (timer))) for 0.1 secs
```

### Распространенные проблемы
| Проблема | Причина | Решение |
|---------|-------|----------|
| Спрайт не отвечает | Нет шапочного блока событий | Добавить «При нажатии зеленого флажка» или другое событие |
| Клон не работает | Клон создан, но не показан | Добавить блок «Показать» после «Когда я начинаю как клон» |
| Переменная, общая для спрайтов | Путаница между глобальными и локальными переменными | Используйте опцию «Только для этого спрайта» |
| Трансляция не получена | Неверное имя сообщения | Убедитесь, что имена трансляции и приема точно совпадают |
| Бесконечная заморозка цикла | «Навсегда» без ожидания | Добавляйте небольшие блоки «Подождите» в узких циклах |
---

## Совместимость
### Аппаратные расширения
Scratch может подключаться к физическому оборудованию через расширения:
```
Supported Hardware:
├── micro:bit
│   ├── Accelerometer/gyroscope input
│   ├── LED matrix display output
│   ├── Button input
│   └── Radio communication
├── LEGO Education
│   ├── SPIKE Prime / Essential
│   ├── EV3 (older)
│   └── Motors and sensors
├── Makey Makey
│   ├── Capacitive touch input
│   ├── Any conductive object as button
│   └── USB connection (no drivers needed)
├── Arduino (via extensions)
│   ├── GPIO pin control
│   ├── Sensor readings
│   └── Motor control
└── Camera / Webcam
    ├── Video sensing (motion detection)
    └── Face detection (via extensions)
```

### API расширений Scratch (пользовательские расширения)
```javascript
// Custom Scratch extension (JavaScript)
class MyExtension {
  getInfo() {
    return {
      id: 'myExtension',
      name: 'My Extension',
      blocks: [
        {
          opcode: 'greet',
          blockType: Scratch.BlockType.REPORTER,
          text: 'greet [NAME]',
          arguments: {
            NAME: { type: Scratch.ArgumentType.STRING, defaultValue: 'World' }
          }
        },
        {
          opcode: 'addNumbers',
          blockType: Scratch.BlockType.REPORTER,
          text: '[A] + [B]',
          arguments: {
            A: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 },
            B: { type: Scratch.ArgumentType.NUMBER, defaultValue: 2 }
          }
        }
      ]
    };
  }
  greet(args) { return 'Hello, ' + args.NAME + '!'; }
  addNumbers(args) { return Number(args.A) + Number(args.B); }
}
Scratch.extensions.register(new MyExtension());
```
---

## Шаблоны проектирования
### Схема 1: Платформерное движение
```
When green flag clicked:
  Set [gravity] to -1
  Set [velocity_y] to 0
  Set [speed] to 5
  Set [is_jumping] to false
  Forever:
    // Horizontal movement
    If <key [right arrow] pressed?> then
      Change x by (speed)
    If <key [left arrow] pressed?> then
      Change x by ((speed) * -1)
    // Jumping
    If <key [space] pressed?> then
      If <(is_jumping) = false> then
        Set [velocity_y] to 12
        Set [is_jumping] to true
    // Gravity
    Change [velocity_y] by (gravity)
    Change y by (velocity_y)
    // Ground collision
    If <(y position) < -100> then
      Set y to -100
      Set [velocity_y] to 0
      Set [is_jumping] to false
```

### Схема 2: прокрутка фона
```
// Background sprite scrolls left to create side-scrolling effect
When green flag clicked:
  Forever:
    Change x by -5
    If <(x position) < -240> then
      Set x to 240

// Or use two copies for seamless scrolling
When I start as a clone:
  Forever:
    Change x by -5
    If <(x position) < -480> then
      Change x by 960
```

### Схема 3: Следование за спрайтом (погоня за ИИ)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Схема 4: Система инвентаризации со списками
```
When green flag clicked:
  Delete all of [inventory]
  Add [Sword] to [inventory]
  Add [Shield] to [inventory]
  Add [Potion] to [inventory]

When key [i] pressed:
  // Display inventory
  Set [display] to []
  Set [idx] to 1
  Repeat (length of [inventory]):
    Set [display] to (join (display) (join (item (idx) of [inventory]) [
]))
    Change [idx] by 1
  Say (display) for 3 secs

When key [1] pressed:
  // Use first item
  If <(length of [inventory]) > 0> then
    Set [used_item] to (item 1 of [inventory])
    Delete 1 of [inventory]
    Say (join [Used: ] (used_item)) for 1 secs
```

### Паттерн 5: Система частиц с клонами
```
// Create particles on click
When this sprite clicked:
  Repeat 10:
    Create clone of [Particle]

// Each particle moves randomly and fades
When I start as a clone:
  Go to [mouse-pointer]
  Point in direction (pick random 0 to 360)
  Set [size] to (pick random 20 to 50)
  Set [ghost] to 0
  Show
  Repeat 20:
    Move 5 steps
    Change [ghost] by 5
  Hide
  Delete this clone
```

---

## Производительность и оптимизация
### Оптимизация спрайтов
| Техника | Воздействие | Описание |
|-----------|--------|-------------|
| **Свернуть клоны** | Высокий | Каждый клон потребляет память; удалить, когда закончите |
| **Уменьшить количество костюмов** | Средний | Меньше переключений костюмов означает меньше затрат на рендеринг |
| **Используйте «запускать без обновления экрана»** | Высокий | Пользовательские блоки без обновления экрана работают быстрее |
| **Ограничить количество блоков «сказать»** | Средний | Речевые пузыри вызывают накладные расходы при рендеринге |
| **Избегайте слова «навсегда» в каждом спрайте** | Средний | Используйте трансляции и мероприятия вместо постоянных опросов |
### Управление клонами
```
// BAD: Creating clones without cleanup
When green flag clicked:
  Forever:
    Create clone of [Enemy]
    Wait 0.1 secs
    // Clones pile up and slow everything down

// GOOD: Limit active clones
When green flag clicked:
  Set [max_enemies] to 10
  Forever:
    If <(enemy_count) < (max_enemies)> then
      Create clone of [Enemy]
      Change [enemy_count] by 1
    Wait 1 secs

When I start as a clone:
  // ... enemy behaviour ...
  // When done:
  Change [enemy_count] by -1
  Delete this clone
```

### Контрольный список оптимизации
| Техника | Воздействие | Описание |
|-----------|--------|-------------|
| **Запускать без обновления экрана** | Очень высокий | Пользовательские блоки пропускают рендеринг ради скорости |
| **Свернуть активные клоны** | Высокий | Удаляйте клоны, как только они больше не нужны |
| **Используйте трансляции экономно** | Средний | Слишком много трансляций в кадре вызывают задержку |
| **Упрощение костюмов** | Средний | Изображения меньшего размера обрабатываются быстрее |
| **Сокращение операций со списком** | Средний | Избегайте сканирования больших списков в каждом кадре |
| **Используйте блоки ожидания** | Низкий | Предотвратить перегрузку процессора в вечных циклах |
---

## Развертывание и использование в реальных условиях
### Совместное использование проектов
```
Deployment Options:
├── Scratch Community (online)
│   ├── Upload to scratch.mit.edu
│   ├── Share with community
│   └── Allow remixing by others
├── Local sharing
│   ├── Save as .sb3 file
│   ├── Share via email/USB/cloud
│   └── Open in Scratch Desktop or web editor
├── Embedding
│   ├── Embed on websites via iframe
│   └── <iframe src="https://scratch.mit.edu/projects/embed/PROJECT_ID">
└── Standalone apps (via third-party tools)
    ├── TurboWarp (desktop packaging)
    ├── Electron-based wrappers
    └── HTML5 export tools
```

### Реальное использование в образовательных целях
| Контекст | Как используется Scratch | Масштаб |
|---------|-------------------|-------|
| **Школы K-12** | Введение в программирование на занятиях CS | Используется в более чем 190 странах |
| **Клубы программистов** | Мастер-классы Scratch Club / CoderDojo | 3000+ клубов по всему миру |
| **Библиотеки** | Программы внеклассного программирования | Системы публичных библиотек |
| **Домашнее обучение** | Самостоятельное обучение программированию | Миллионы домашних учеников |
| **Университет CS0** | Непрофильные вводные курсы по информатике | Программы университетского моста |
| **Доступность** | Обучение программированию для слабовидящих | Поддержка чтения с экрана |
| **Терапия** | Развитие когнитивных и моторных навыков | Трудотерапия |
### Scratch в исследованиях в области образования
Исследования показали, что Scratch эффективно учит:
- **Последовательное мышление**: разбиение проблем на упорядоченные шаги.
- **Навыки отладки**: поиск и исправление ошибок в логике.
- **Творческое самовыражение**: сочетание искусства, музыки и программирования.
- **Сотрудничество**: создание ремиксов и развитие чужих проектов.
- **Настойчивость**: работа над проектами для их улучшения.
---

## Переход с нуля
После изучения Scratch типичные следующие шаги включают в себя:
| Следующий язык | Почему |
|--------------|-----|
| **Питон** | Самый естественный переход — читаемый синтаксис, схожие логические концепции |
| **JavaScript** | Если интересуетесь вебом/играми — немедленная визуальная обратная связь |
| **Lua (через Roblox/Love2D)** | Если вы заинтересованы в разработке игр |
| **Изобретатель приложений** | Визуальные блоки для приложений Android (та же линия MIT) |
| **Блочно** | Библиотека визуального программирования Google (аналогичные концепции) |
### Картирование концепций: Scratch to Python
| Скретч-концепция | Python-эквивалент |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`|  __ЗАЩИЩЕНО_3__ |
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Вызов функции или система событий |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(индекс 0!) |
| `length of [list]`| `len(list)`|
---

## Когда использовать Scratch
| Сценарий | Зачем царапать | Лучшая альтернатива |
|----------|-----------|-------------------|
| Обучение детей (8–16 лет) программированию | Разработан специально для этого | — |
| Знакомство с вычислительным мышлением | Визуально, без синтаксических ошибок | — |
| Школьные мастер-классы/клубы кодирования | Бесплатно, через браузер, без настройки | — |
| Визуальное прототипирование игровых идей | Быстрая итерация | — |
| Профессиональное развитие | Не предназначен для этого | Python, JavaScript, любой текстовый язык |
| Университетское образование в сфере компьютерных технологий | Слишком просто | Питон, Java, C |
---

## Краткое содержание
Scratch — это не язык программирования в традиционном понимании — это среда обучения. Его гениальность заключается в устранении всех барьеров между ребенком и радостью создания чего-то интерактивного. Сосредоточив внимание на концепциях, а не на синтаксисе, Scratch обучает основам программирования, которые можно перенести на любой язык. Scratch является золотым стандартом для ознакомления юных учащихся с программированием.