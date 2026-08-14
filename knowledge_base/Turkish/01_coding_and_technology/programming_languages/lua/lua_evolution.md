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
# Lua — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 1.0 | 1994 | İlk sürüm (PUC-Rio, Brezilya) |
| 2.1 | 1995 | Tablolar tek veri yapısı haline geliyor |
| 3.0 | 1997 | C API, etiket yöntemleri (erken meta yöntemler) |
| 3.1 | 1998 | Anlamsal denetleyiciler (değer yükseltmeler) |
| 4.0 | 2000 | **Lua 4**: ref sayma + GC, geliştirilmiş C API |
| 5.0 | 2003 | **Ana**: uygun sözcük kapsamı, eşyordamlar, metatablolar, Boolean'lar |
| 5.1 | 2006 | **Artımlı GC**,`#`uzunluk operatörü,`goto`kaldırıldı,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`değişiklikleri,`goto`geri eklendi, efemeron tabloları |
| 5.3 | 2015 | **Tamsayı türü**, bitsel operatörler, UTF-8 desteği |
| 5.4 | 2020 | **Nesil GC**,`const`/`close`değişkenleri,`tostring`meta yöntemi |
| 5.4.x | 2020–25 | Kademeli iyileştirmeler, uyarı sistemi |
| 5.5 | TBD | (gelecek) GC'de daha fazla iyileştirme |
## Önemli Kilometre Taşları
### Lua 1–3: İlk Yıllar (1994–1999)
- **1994**: Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo tarafından PUC-Rio'da (Rio de Janeiro Papalık Katolik Üniversitesi) oluşturuldu
- **Hedef**: Veri girişi için yerleştirilebilir kodlama dili (bağımsız bir dil değil)
- **2.1**: Tablolar tek veri yapısı haline geliyor — radikal basitlik
- **3.0**: C API güçlendirilmiş — Lua'yı C/C++ uygulamalarına yerleştirilebilir hale getirir
- **3.1**: Artan değerler — kapanışlar için sözcüksel kapsam belirleme
### Lua 4: Olgunlaşma (2000)
- Referans sayma + çöp toplama (karma)
- Geliştirilmiş C API —`luaL_*`yardımcı kitaplığı
- Hala küreseller için uygun bir sözcüksel kapsam belirleme yok
### Lua 5.0: Modern Lua (2003)
- **Doğru sözcüksel kapsam belirleme** —`local`değişkenleri
- **Ortak rutinler** — işbirliğine dayalı çoklu görev
- **Metatablolar** — operatör aşırı yüklemesi, özel davranış
- **Boolean** —`true`/`false`uygun değerler olarak
- **Kapanışlar** doğru yapıldı — değer artışları genelleştirildi
- Lua'nın oyunlarda yaygın olarak benimsenmesini sağlayan versiyon budur
### Lua 5.1: Standart (2006)
- **Artımlı çöp toplayıcı**
-`#`uzunluk operatörü
-`module()`işlevi
- Küresel ortamın çalışma şekli değiştirildi
- **Bu sürüm en yaygın yerleşik sürüm haline gelir** (LuaJIT 5.1'i hedefler)
### Lua 5.2: İyileştirmeler (2011)
-`_ENV`— parça başına ortam (daha temiz küreseller)
-`goto`ifadesi geri döner
- Efemeron tabloları (GC iyileştirmesi)
- Paket sistemi iyileştirmeleri
### Lua 5.3: Tamsayı ve Bitler (2015)
- **Tamsayı alt türü** — float'tan farklıdır
- **Bitsel operatörler** —`&`,`|`,`~`,`<<`,`>>`
- **UTF-8 desteği** — yerleşik`utf8`kitaplığı
- Zemin bölümü`//`
- İkili veriler için`pack`/`unpack`dizesi
### Lua 5.4: Nesil GC (2020)
- **Nesil çöp toplayıcı** — çok daha iyi GC duraklamaları
- **`<const>`değişkenleri** — gerçek sabitler
- **`<close>`değişkenleri** — kapatılacak değişkenler (kaynak yönetimi,`defer`veya`with`gibi)
-`tostring`meta yöntemi
- Dize alt türleri (kısa ve uzun dizeler farklı şekilde optimize edilmiştir)
## Söz Dizimi Gelişimi
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

## Özellik Gelişimi
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

## Oyunda Lua
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

## Temel Tasarım İlkeleri
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Ekosistem Büyümesi
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
