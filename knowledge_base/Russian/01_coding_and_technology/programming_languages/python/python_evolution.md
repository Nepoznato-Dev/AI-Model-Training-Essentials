---
# Metadata
title: "Python — Version History & Evolution"
description: "Comprehensive version history and evolution of Python from 1.x to modern Python."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [python, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Python — история версий и эволюция
## Временная шкала
| Версия | Дата выпуска | Ключевая тема |
|---------|-------------|-----------|
| 1.0 | январь 1994 г. | Первоначальный выпуск |
| 1,5 | декабрь 1997 г. | Классы, исключения, модули |
| 2.0 | октябрь 2000 г. | Понимание списков, сборка мусора |
| 2.2 | декабрь 2001 г. | Унифицированные типы (типы/классы), генераторы |
| 2,5 | Сентябрь 2006 г. |  Оператор `with`,`yield`как выражение |
| 2,6 | Октябрь 2008 г. | `bytes`, импорт `future`, переход на 3 |
| 2,7 | июль 2010 г. | Понимание Dict/Set,`argparse`|
| 3.0 | декабрь 2008 г. | **Нарушение**:`print()`,`str`/`bytes`, итераторы |
| 3.3 | Сентябрь 2012 г. | `yield from`, пакеты пространства имен |
| 3,4 | март 2014 г. | `asyncio`,`pathlib`,`enum`|
| 3,5 | Сентябрь 2015 г. | `async/await`, подсказки типа (PEP 484), распаковка`**`|
| 3,6 | декабрь 2016 г. | f-строки, `async`, упорядоченные словари |
| 3,7 | июнь 2018 г. |  `dataclasses`, `contextvars`, зарезервировано`async`|
| 3,8 | октябрь 2019 г. | Оператор Моржа`:=`, только позиционные параметры |
| 3,9 | октябрь 2020 г. | Объединение Dict `|`, универсальные типы`list[int]`|
| 3.10 | октябрь 2021 г. | `match/case`, сопоставление структурного образца |
| 3.11 | октябрь 2022 г. | Группы исключений, тип `Self`, более быстрый CPython |
| 3.12 | октябрь 2023 г. | Подготовка GIL для каждого интерпретатора, синтаксис параметра типа |
| 3.13 | октябрь 2024 г. | Свободнопоточный режим (экспериментальный), улучшенный REPL |
| 3.14 | октябрь 2025 г. | Стабильная версия без GIL, отложенная оценка аннотаций |
## Основные вехи
### Эра Python 2.x (2000–2020 гг.)
- **2.0**: понимание списков, вдохновленное Haskell; циклический ГХ
- **2.2**: базовый класс `object`;  Ключевое слово`yield`(генераторы)
- **2.5**: оператор `with`; `yield`становится выражением
- **2.7**: финальная версия 2.x; понимание диктовок; `argparse`
- **Окончание срока действия**: 1 января 2020 г.
### Революция Python 3.x (2008 – настоящее время)
- **3.0**: чистый разрыв —`print`как функция,`str`против `bytes`, все итераторы возвращают представления.
- **3.5**: синтаксис `async`/`await`; введите подсказки с помощью модуля `typing`
- **3.6**: фа-струны (наиболее востребованная функция); `asyncio`стабилизирован
- **3.8**: оператор Walrus для встроенного назначения.
- **3.10**: Сопоставление структурного шаблона (`match`/`case`)
- **3.11**: на 10–60 % быстрее; группы исключений с`except*`
- **3.13**: Экспериментальный режим со свободной резьбой (без GIL).
## Эволюция философии дизайна
```
1994: "There should be one — and preferably only one — obvious way to do it"
2004: "Batteries included" (extensive stdlib)
2011: "Beautiful is better than ugly" (Zen of Python, PEP 20)
2015: Gradual typing accepted (Guido's compromise)
2018: "Black" formatter — consistency over preference
2023: Performance becomes priority (faster CPython, Shannon plan)
```

## Ключевые политические деятели, которые сформировали Python
| ПЭП | Год | Особенность |
|------|------|---------|
| 20 | 2004 | Дзен Python |
| 257 | 2001 | Соглашения о строках документации |
| 279 | 2002 | `enumerate()`|
| 289 | 2002 | Генератор выражений |
| 342 | 2005 | `yield`как выражение,`send()`|
| 380 | 2009 | `yield from`|
| 484 | 2014 | Тип подсказки |
| 492 | 2014 | `async`/`await`|
| 498 | 2015 | фа-струны |
| 572 | 2018 | Оператор-морж`:=`|
| 622 | 2020 | Структурное сопоставление с образцом |
| 654 | 2021 | Группы исключений |
| 684 | 2022 | Индивидуальный переводчик GIL |
| 703 | 2023 | Сделать GIL необязательным |
## Эволюция производительности
```
Python 3.10:  baseline
Python 3.11:  ~1.25x faster (Faster CPython project)
Python 3.12:  ~1.3x faster (specializing adaptive interpreter)
Python 3.13:  ~1.4x faster (JIT compiler experiment)
Target 3.14:  5x faster than 3.10 (Shannon plan goal)
```

## Рост сообщества и экосистемы
```
2004: PyPI launches (7,000+ packages by 2010)
2008: First PyCon (300 attendees)
2012: pip replaces easy_install
2018: Python overtakes Java in popularity (Stack Overflow)
2020: Python 2 end-of-life; 3.x migration completes
2023: 500,000+ packages on PyPI
2025: #1 most used language (multiple surveys)
```
