<!--
---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lua, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Lua — История версий и эволюция
## Временная шкала
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 1.0 | 1994 | Первоначальный выпуск (PUC-Рио, Бразилия) |
| 2.1 | 1995 | Таблицы становятся единственной структурой данных |
| 3.0 | 1997 | C API, методы тегов (ранние метаметоды) |
| 3.1 | 1998 | Семантические контроллеры (повышение значений) |
| 4.0 | 2000 | **Lua 4**: подсчет ссылок + сборщик мусора, улучшенный C API |
| 5.0 | 2003 | **Основное**: правильная лексическая область видимости, сопрограммы, метатаблицы, логические значения |
| 5.1 | 2006 | **Инкрементный сборщик мусора**, оператор длины `#`,`goto`удален,`module()`|
| 5.2 | 2011 | `_ENV`, изменения `_G`, добавление`goto`обратно, таблицы эфемеронов |
| 5.3 | 2015 | **Целый тип**, побитовые операторы, поддержка UTF-8 |
| 5.4 | 2020 | **Поколенный сборщик мусора**, переменные `const`/`close`, метаметод`tostring`|
| 5.4.х | 2020–25 | Постепенные улучшения, система оповещений |
| 5,5 | подлежит уточнению | (в будущем) Дальнейшие улучшения GC |
## Основные вехи
### Луа 1–3: Ранние годы (1994–1999)
- **1994**: Создано в PUC-Rio (Папском католическом университете Рио-де-Жанейро) Роберто Иерусалимским, Вальдемаром Селесом, Луисом Энрике де Фигейредо.
- **Цель**: встроенный язык сценариев для ввода данных (не отдельный язык).
- **2.1**: Таблицы становятся единственной структурой данных — радикальная простота.
- **3.0**: усовершенствованный API C — делает Lua встраиваемым в приложения C/C++.
- **3.1**: Upvalues — лексическая область видимости замыканий.
### Lua 4: Созревание (2000)
- Подсчет ссылок + сборка мусора (гибрид)
- Улучшен C API — вспомогательная библиотека `luaL_*`.
- До сих пор нет правильной лексической области видимости для глобальных переменных.
### Lua 5.0: Современный Lua (2003)
- **Правильное лексическое определение** — переменные `local`.
- **Сопрограммы** — совместная многозадачность.
- **Метатаблицы** — перегрузка операторов, пользовательское поведение.
- **Логические значения** —`true`/`false`как правильные значения.
– **Замыкания** выполнены правильно: общие значения повышены.
- Это версия, благодаря которой Lua получил широкое распространение в играх.
### Lua 5.1: Стандарт (2006)
- **Инкрементальный сборщик мусора**
- Оператор длины `#`
- Функция `module()`
- Изменено, как работает глобальная среда.
- **Эта версия становится наиболее широко внедряемой** (LuaJIT нацелен на 5.1)
### Lua 5.2: Уточнения (2011)
-`_ENV`— среда для каждого фрагмента (более чистые глобальные переменные)
- Оператор`goto`возвращает
- Таблицы эфемеронов (улучшение GC)
- Улучшения системы пакетов.
### Lua 5.3: Целые числа и биты (2015)
- **Подтип целого числа** — отличается от типа с плавающей запятой.
- **Побитовые операторы** — `&`, `|`, `~`, `<<`, `>>`. 
- **Поддержка UTF-8** — встроенная библиотека `utf8`.
- Разделение этажей`//`
— Строка `pack`/`unpack` для двоичных данных.
### Lua 5.4: Сборщик мусора для поколений (2020)
- **Сборщик мусора для поколений** — гораздо лучше делает паузу в сборе мусора
- ** Переменные `<const>`** — настоящие константы.
- ** Переменные `<close>`** — переменные, подлежащие закрытию (управление ресурсами, например`defer`или`with`)
- Метаметод `tostring`
- Подтипы строк (короткие и длинные строки оптимизированы по-разному)
## Эволюция синтаксиса
```lua
-- Lua 4.0: No local scoping for globals
x = 10  -- always global unless in a function

-- Lua 5.0: Proper lexical scoping
local x = 10  -- local to block
do
  local y = 20
  print(x + y)  -- 30
end

-- Lua 5.1: Length operator, module
local t = {1, 2, 3}
print(#t)  -- 3
module("mymodule", package.seeall)

-- Lua 5.3: Integer type, bitwise
local a = 10    -- integer
local b = 10.0  -- float
print(a & 0xFF) -- bitwise AND: 10
print(a >> 1)   -- right shift: 5

-- Lua 5.4: const and close variables
local x <const> = 42  -- constant, cannot change
local f <close> = io.open("file.txt")  -- auto-closed at scope end
```

## Эволюция функций
```
Lua 1.0:  Tables, functions, strings, numbers, C API
Lua 2.1:  Tables as only data structure
Lua 3.0:  Tag methods (predecessor to metatables)
Lua 3.1:  Upvalues (closures)
Lua 4.0:  Hybrid GC (ref counting + cycle collection)
Lua 5.0:  Coroutines, metatables, proper lexical scoping, booleans
Lua 5.1:  Incremental GC, # operator, module()
Lua 5.2:  _ENV, goto, ephemeron tables
Lua 5.3:  Integer type, bitwise ops, UTF-8, //, pack/unpack
Lua 5.4:  Generational GC, <const>, <close>, tostring metamethod
```

## Lua в играх
```
1997: LucasArts uses Lua in game scripting (Grim Fandango)
2003: Lua 5.0 — game industry adoption accelerates
2005: World of Warcraft uses Lua for UI addons
2006: LuaJIT (Mike Pall) — JIT-compiled Lua 5.1, extremely fast
2010: Love2D game framework (Lua-based)
2012: Defold game engine (Lua scripting)
2015: Roblox adopts Luau (Lua dialect with types)
2020: Lua 5.4 — continued game engine integration
2025: Lua remains the #1 embedded scripting language in games
       Used in: Unity (via plugins), WoW, Garry's Mod, Factorio,
       Civilization, Adobe Lightroom, Nginx (OpenResty), Redis
```

## Ключевые принципы проектирования
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Рост экосистемы
```
1994: Lua created at PUC-Rio (Brazil)
1997: First game industry use (LucasArts)
2003: Lua 5.0 — widespread game adoption
2005: LuaJIT — JIT-compiled Lua
2006: Lua 5.1 — the "standard" embedded version
2010: OpenResty (Nginx + Lua) — web development
2015: Luau (Roblox) — typed Lua dialect
2020: Lua 5.4 — modern GC, resource management
2025: Lua is the dominant embedded scripting language
       Powers: games, Nginx, Redis, Wireshark, Lightroom, more
```
