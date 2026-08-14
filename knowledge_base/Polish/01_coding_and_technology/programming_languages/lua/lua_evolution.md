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
# Lua — Historia wersji i ewolucja
## Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 1,0 | 1994 | Pierwsze wydanie (PUC-Rio, Brazylia) |
| 2.1 | 1995 | Tabele stają się jedyną strukturą danych |
| 3,0 | 1997 | API C, metody tagów (wczesne metametody) |
| 3.1 | 1998 | Kontrolery semantyczne (wartości up) |
| 4,0 | 2000 | **Lua 4**: zliczanie refów + GC, ulepszone API C |
| 5,0 | 2003 | **Główne**: właściwy zakres leksykalny, współprogramy, metatabele, wartości logiczne |
| 5.1 | 2006 | **Przyrostowe GC**, operator długości `#`, usunięto `goto`,`module()`|
| 5.2 | 2011 |  Zmiany`_ENV`, `_G`, dodano ponownie `goto`, tablice efemeronów |
| 5.3 | 2015 | **Typ całkowity**, operatory bitowe, obsługa UTF-8 |
| 5.4 | 2020 | **Generacyjne GC**, zmienne`const`/ `close`, metametoda`tostring`|
| 5.4.x | 2020–25 | Stopniowe ulepszenia, system ostrzegania |
| 5,5 | do ustalenia | (przyszłość) Dalsze ulepszenia GC |
## Główne kamienie milowe
### Lua 1–3: Wczesne lata (1994–1999)
- **1994**: Utworzono w PUC-Rio (Papieski Katolicki Uniwersytet w Rio de Janeiro) przez Roberto Ierusalimschy, Waldemara Celesa, Luiza Henrique de Figueiredo
- **Cel**: Wbudowany język skryptowy do wprowadzania danych (nie samodzielny język)
- **2.1**: Tabele stają się jedyną strukturą danych — radykalna prostota
- **3.0**: Udoskonalone API C — umożliwia osadzanie Lua w aplikacjach C/C++
- **3.1**: Upvalues — zakres leksykalny domknięć
### Lua 4: Dojrzewanie (2000)
- Liczenie referencji + zbieranie śmieci (hybryda)
- Ulepszone API C — biblioteka pomocnicza `luaL_*`
- Nadal nie ma odpowiedniego zakresu leksykalnego dla słów globalnych
### Lua 5.0: Nowoczesna Lua (2003)
- **Właściwy zakres leksykalny** — Zmienne `local`
- **Współprogramy** — wielozadaniowość w trybie współpracy
- **Metatables** — przeciążanie operatora, zachowanie niestandardowe
- **Booleany** —`true`/`false`jako wartości prawidłowe
- **Zamknięcia** wykonane prawidłowo – uogólniono wzrosty
- To jest wersja, która sprawiła, że Lua została powszechnie przyjęta w grach
### Lua 5.1: Standard (2006)
- **Przyrostowy moduł zbierający śmieci**
- Operator długości `#`
- Funkcja `module()`
- Zmieniono sposób działania środowiska globalnego
- **Ta wersja staje się najczęściej osadzaną wersją** (LuaJIT docelowo 5.1)
### Lua 5.2: Udoskonalenia (2011)
-`_ENV`— środowisko per-porcja (czystsze globale)
- Zwraca instrukcję `goto`
- Tabele efemeronów (ulepszenie GC)
- Ulepszenia systemu pakietów
### Lua 5.3: Liczba całkowita i bity (2015)
- **Podtyp całkowity** — różni się od typu zmiennoprzecinkowego
- **Operatory bitowe** —`&`,`|`,`~`,`<<`,`>>`
- **Obsługa UTF-8** — wbudowana biblioteka `utf8`
- Podział piętra`//`
- String`pack`/`unpack`dla danych binarnych
### Lua 5.4: Pokoleniowe GC (2020)
- **Pokoleniowy moduł zbierający śmieci** — znacznie lepsze pauzy GC
- ** Zmienne `<const>`** — stałe prawdziwe
- ** Zmienne `<close>`** — zmienne do zamknięcia (zarządzanie zasobami, np.`defer`lub`with`)
- Metametoda `tostring`
- Podtypy ciągów (krótkie i długie ciągi zoptymalizowane w różny sposób)
## Ewolucja składni
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

## Ewolucja funkcji
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

## Lua w grach
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

## Kluczowe zasady projektowania
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Rozwój ekosystemu
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
