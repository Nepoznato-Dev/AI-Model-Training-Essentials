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
# Lua — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 1.0 | 1994 | Rilis awal (PUC-Rio, Brasil) |
| 2.1 | 1995 | Tabel menjadi satu-satunya struktur data |
| 3.0 | 1997 | C API, metode tag (metode awal) |
| 3.1 | 1998 | Pengontrol semantik (nilai naik) |
| 4.0 | 2000 | **Lua 4**: penghitungan ref + GC, peningkatan C API |
| 5.0 | 2003 | **Mayor**: pelingkupan leksikal yang tepat, coroutine, metatabel, Boolean |
| 5.1 | 2006 | **GC tambahan**, operator panjang `#`,`goto`dihapus,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`berubah,`goto`ditambahkan kembali, tabel ephemeron |
| 5.3 | 2015 | **Jenis bilangan bulat**, operator bitwise, dukungan UTF-8 |
| 5.4 | 2020 | **GC Generasi**, variabel`const`/ `close`, metametode`tostring`|
| 5.4.x | 2020–25 | Peningkatan bertahap, sistem peringatan |
| 5.5 | TBD | (masa depan) Peningkatan GC lebih lanjut |
## Tonggak Penting
### Lua 1–3: Tahun-Tahun Awal (1994–1999)
- **1994**: Dibuat di PUC-Rio (Universitas Katolik Kepausan Rio de Janeiro) oleh Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo
- **Sasaran**: Bahasa skrip yang dapat disematkan untuk entri data (bukan bahasa mandiri)
- **2.1**: Tabel menjadi satu-satunya struktur data — kesederhanaan yang radikal
- **3.0**: C API dipadatkan — membuat Lua dapat disematkan dalam aplikasi C/C++
- **3.1**: Nilai tambah — pelingkupan leksikal untuk penutupan
### Lua 4: Pematangan (2000)
- Penghitungan referensi + pengumpulan sampah (hibrida)
- Peningkatan C API — perpustakaan tambahan `luaL_*`
- Masih belum ada pelingkupan leksikal yang tepat untuk global
### Lua 5.0: Lua Modern (2003)
- **Pelingkupan leksikal yang tepat** — variabel `local`
- **Coroutine** — multitasking kooperatif
- **Metatables** — kelebihan operator, perilaku khusus
- **Boolean** —`true`/`false`sebagai nilai yang sesuai
- **Penutupan** dilakukan dengan benar — peningkatan nilai digeneralisasikan
- Ini adalah versi yang membuat Lua diadopsi secara luas dalam permainan
### Lua 5.1: Standar (2006)
- **Pengumpul sampah tambahan**
- Operator panjang `#`
- Fungsi `module()`
- Mengubah cara kerja lingkungan global
- **Versi ini menjadi versi yang paling banyak disematkan** (LuaJIT menargetkan 5.1)
### Lua 5.2: Penyempurnaan (2011)
-`_ENV`— lingkungan per bagian (global yang lebih bersih)
- Pernyataan`goto`kembali
- Tabel Ephemeron (peningkatan GC)
- Perbaikan sistem paket
### Lua 5.3: Integer & Bit (2015)
- **Subtipe bilangan bulat** — berbeda dari float
- **Operator bitwise** —`&`,`|`,`~`,`<<`,`>>`
- **Dukungan UTF-8** — pustaka`utf8`bawaan
- Divisi lantai`//`
- String`pack`/`unpack`untuk data biner
### Lua 5.4: GC Generasi (2020)
- **Pengumpul sampah generasi** — jeda GC yang jauh lebih baik
- ** Variabel `<const>`** — konstanta sebenarnya
- ** Variabel `<close>`** — variabel yang akan ditutup (manajemen sumber daya, seperti`defer`atau`with`)
- Metametode `tostring`
- Subtipe string (string pendek vs. panjang dioptimalkan secara berbeda)
## Evolusi Sintaks
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

## Evolusi Fitur
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

## Lua dalam Permainan
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

## Prinsip Desain Utama
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## Pertumbuhan Ekosistem
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
