---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# C — История версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| К&Р С | 1972–78 | Оригинал C (Керниган и Ричи) |
| С89/С90 | 1989/90 | Первый стандарт ANSI/ISO |
| С95 | 1995 | Поправка 1:`wchar.h`, орграфы |
| С99 | 1999 |  Комментарии `//`, `inline`, `bool`, VLA, назначенные инициализаторы |
| С11 | 2011 | Атомы, потоки, `_Static_assert`, анонимные структуры/объединения |
| С17 | 2018 | Исправления дефектов (новых функций нет) |
| С23 | 2024 |  `nullptr`, `typeof`, `constexpr`, `#embed`, атрибуты |
## Основные вехи
### К&Р Ц (1972–1989)
- **1972**: Деннис Ритчи создает C в Bell Labs для Unix.
- **1978**: Керниган и Ритчи публикуют «Язык программирования C».
- Основные возможности: `struct`, `int`, `char`, указатели, функции, `#include`. 
- Нет `void`, нет `enum`, нет `unsigned`, нет `const`
### C89/C90 — Стандарт (1989)
- Первый стандарт ANSI (ANSI X3.159-1989).
- Добавлены: `void`, `enum`, `const`, `volatile`, прототипы функций, `signed`. 
- «Золотой век» — портативный, широко распространенный
- По-прежнему является основой для многих встроенных систем.
### C99 — Современный C (1999)
-`//`однострочные комментарии
- Функции `inline`
-`bool`через`<stdbool.h>`
- Массивы переменной длины (VLA).
- Назначенные инициализаторы: `struct Point p = {.x = 1, .y = 2};`. 
-`for (int i = 0; ...)`— объявления в цикле
- `<stdint.h>`: `int32_t`,`uint64_t`и т. д.
- Ключевое слово `restrict`
- Вариативные макросы
- Составные литералы
### C11 — Безопасность и параллелизм (2011)
-`<stdatomic.h>`— атомарные операции
-`<threads.h>`— поддержка потоков
-`_Static_assert`— утверждения времени компиляции.
- Анонимные структуры/объединения во вложенных структурах.
-`_Alignof`,`_Alignas`— контроль выравнивания
- Общие параметры: `_Generic(x, int: ..., default: ...)`. 
- Поддержка Юникод: `<uchar.h>`. 
- Дополнительная поддержка VLA (стала необязательной из-за встроенных проблем)
### C23 — Возрождение (2024)
-`nullptr`— константа нулевого указателя (заменяет макрос `NULL`)
-`typeof`— вывод типа
-`constexpr`— константные выражения
-`#embed`— встраивание двоичных данных во время компиляции.
- Синтаксис`[[attribute]]`(атрибуты в стиле C23)
- `true`/`false` в качестве ключевых слов (`<stdbool.h>` больше не требуется)
- Вывод типа `auto`
-`static_assert`(без подчеркивания)
-`alignof`(без подчеркивания)
- Удален возврат по умолчанию `int`.
## Процесс стандартизации
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Философия совместимости
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Эволюция препроцессора
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Эволюция системы типов
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Воздействие на экосистему
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
