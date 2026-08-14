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
# Lua — Historial de versiones y evolución
## Línea de tiempo
| Versión | Año | Tema clave |
|---------|------|-----------|
| 1.0 | 1994 | Lanzamiento inicial (PUC-Rio, Brasil) |
| 2.1 | 1995 | Las tablas se convierten en la única estructura de datos |
| 3.0 | 1997 | API C, métodos de etiquetas (primeros metamétodos) |
| 3.1 | 1998 | Controladores semánticos (valores ascendentes) |
| 4.0 | 2000 | **Lua 4**: recuento de referencias + GC, API C mejorada |
| 5.0 | 2003 | **Principal**: alcance léxico adecuado, corrutinas, metatablas, booleanos |
| 5.1 | 2006 | **GC incremental**, operador de longitud `#`,`goto`eliminado,`module()`|
| 5.2 | 2011 |  `_ENV`, cambios `_G`,`goto`agregado nuevamente, tablas de efemérides |
| 5.3 | 2015 | **Tipo entero**, operadores bit a bit, compatibilidad con UTF-8 |
| 5.4 | 2020 | **GC generacional**, variables`const`/ `close`, metamétodo`tostring`|
| 5.4.x | 2020-25 | Mejoras incrementales, sistema de alerta |
| 5.5 | Por determinar | (futuro) Otras mejoras del GC |
## Hitos importantes
### Lua 1–3: Los primeros años (1994–1999)
- **1994**: Creado en la PUC-Rio (Pontificia Universidad Católica de Río de Janeiro) por Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Objetivo**: lenguaje de secuencias de comandos integrable para la entrada de datos (no es un lenguaje independiente)
- **2.1**: Las tablas se convierten en la única estructura de datos: simplicidad radical
- **3.0**: API de C solidificada: hace que Lua se pueda integrar en aplicaciones C/C++
- **3.1**: Valores mejorados: alcance léxico para cierres
### Lua 4: Maduración (2000)
- Recuento de referencias + recolección de basura (híbrido)
- API C mejorada: biblioteca auxiliar `luaL_*`
- Todavía no hay un alcance léxico adecuado para las palabras globales.
### Lua 5.0: Lua moderna (2003)
- **Alcance léxico adecuado** — variables `local`
- **Corrutinas**: multitarea cooperativa
- **Metatables**: sobrecarga de operadores, comportamiento personalizado
- **Booleanos** —`true`/`false`como valores adecuados
- **Cierres** bien hechos: aumentos de valor generalizados
- Esta es la versión que hizo que Lua fuera ampliamente adoptada en los juegos.
### Lua 5.1: El estándar (2006)
- **Recolector de basura incremental**
- Operador de longitud `#`
- Función `module()`
- Cambió cómo funciona el entorno global.
- **Esta versión se convierte en la versión más integrada** (LuaJIT apunta a 5.1)
### Lua 5.2: Refinamientos (2011)
- `_ENV`: entorno por fragmento (globales más limpios)
- Devuelve la declaración `goto`
- Tablas Ephemeron (mejora de GC)
- Mejoras en el sistema de paquetes.
### Lua 5.3: enteros y bits (2015)
- **Subtipo entero**: distinto de flotante
- **Operadores bit a bit**: `&`, `|`, `~`, `<<`,`>>`
- **Soporte UTF-8** — biblioteca`utf8`incorporada
- División del suelo`//`
- Cadena`pack`/`unpack`para datos binarios
### Lua 5.4: GC generacional (2020)
- **Recolector de basura generacional**: pausas de GC mucho mejores
- ** variables`<const>`** — constantes verdaderas
- ** variables`<close>`** — variables por cerrar (gestión de recursos, como`defer`o `with`)
- Metamétodo `tostring`
- Subtipos de cadenas (cadenas cortas y largas optimizadas de forma diferente)
## Evolución de la sintaxis
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

## Evolución de funciones
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

## Lua en juegos
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

## Principios clave de diseño
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Crecimiento del ecosistema
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
