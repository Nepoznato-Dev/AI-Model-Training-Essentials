---
# Metadata
title: "Lua — Version History & Evolution"
description: "Comprehensive version history and evolution of Lua from 1.0 to modern Lua."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# लुआ - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| 1.0 | 1994 | आरंभिक रिलीज़ (पीयूसी-रियो, ब्राज़ील) |
| 2.1 | 1995 | तालिकाएँ ही एकमात्र डेटा संरचना बन जाती हैं |
| 3.0 | 1997 | सी एपीआई, टैग विधियां (प्रारंभिक मेटामेथड्स) |
| 3.1 | 1998 | सिमेंटिक कंट्रोलर (अपवैल्यू) |
| 4.0 | 2000 | **लुआ 4**: रेफरी-काउंटिंग + जीसी, बेहतर सी एपीआई |
| 5.0 | 2003 | **प्रमुख**: उचित लेक्सिकल स्कोपिंग, कोरटाइन्स, मेटाटेबल्स, बूलियन्स |
| 5.1 | 2006 | **वृद्धिशील GC**,`#`लंबाई ऑपरेटर,`goto`हटा दिया गया,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`परिवर्तन,`goto`वापस जोड़ा गया, क्षणिक तालिकाएँ |
| 5.3 | 2015 | **पूर्णांक प्रकार**, बिटवाइज़ ऑपरेटर, यूटीएफ-8 समर्थन |
| 5.4 | 2020 | **जेनरेशनल GC**,`const`/`close`वेरिएबल्स,`tostring`मेटामेथोड |
| 5.4.x | 2020–25 | वृद्धिशील सुधार, चेतावनी प्रणाली |
| 5.5 | टीबीडी | (भविष्य) आगे जीसी सुधार |
## प्रमुख मील के पत्थर
### लुआ 1-3: प्रारंभिक वर्ष (1994-1999)
- **1994**: पीयूसी-रियो (रियो डी जनेरियो की पोंटिफिकल कैथोलिक यूनिवर्सिटी) में रॉबर्टो इरुसलीम्स्की, वाल्डेमर सेलेस, लुइज़ हेनरिक डी फिगुएरेडो द्वारा बनाया गया
- **लक्ष्य**: डेटा प्रविष्टि के लिए एंबेडेबल स्क्रिप्टिंग भाषा (स्टैंडअलोन भाषा नहीं)
- **2.1**: तालिकाएँ एकमात्र डेटा संरचना बन जाती हैं - मौलिक सरलता
- **3.0**: सी एपीआई ठोस - लुआ को सी/सी++ अनुप्रयोगों में एम्बेड करने योग्य बनाता है
- **3.1**: अपवैल्यू - समापन के लिए शाब्दिक दायरा
### लुआ 4: परिपक्वता (2000)
- संदर्भ गणना + कचरा संग्रहण (हाइब्रिड)
- बेहतर सी एपीआई -`luaL_*`सहायक लाइब्रेरी
- ग्लोबल्स के लिए अभी भी कोई उचित शाब्दिक दायरा नहीं है
### लुआ 5.0: मॉडर्न लुआ (2003)
- **उचित शाब्दिक दायरा** -`local`चर
- **कोरटाइन्स** - सहकारी मल्टीटास्किंग
- **मेटाटेबल्स** - ऑपरेटर ओवरलोडिंग, कस्टम व्यवहार
- **बूलियन्स** -`true`/`false`उचित मान के रूप में
- **क्लोजर** सही ढंग से किया गया - अपवैल्यू को सामान्यीकृत किया गया
- यह वह संस्करण है जिसने लुआ को खेलों में व्यापक रूप से अपनाया
### लुआ 5.1: द स्टैंडर्ड (2006)
- **वृद्धिशील कचरा संग्रहकर्ता**
-`#`लंबाई ऑपरेटर
-`module()`फ़ंक्शन
- वैश्विक पर्यावरण के काम करने के तरीके में बदलाव आया
- **यह संस्करण सबसे व्यापक रूप से एम्बेडेड संस्करण बन गया है** (LuaJIT लक्ष्य 5.1)
### लुआ 5.2: परिशोधन (2011)
-`_ENV`- प्रति-चंक वातावरण (स्वच्छ वैश्विक)
-`goto`स्टेटमेंट रिटर्न
- एफेमेरॉन टेबल (जीसी सुधार)
- पैकेज सिस्टम में सुधार
### लुआ 5.3: पूर्णांक और बिट्स (2015)
- **पूर्णांक उपप्रकार** - फ़्लोट से भिन्न
- **बिटवाइज ऑपरेटर** -`&`,`|`,`~`,`<<`,`>>`
- **UTF-8 समर्थन** — अंतर्निहित`utf8`लाइब्रेरी
- फ़्लोर डिवीजन`//`
- बाइनरी डेटा के लिए स्ट्रिंग`pack`/ `unpack`
### लुआ 5.4: जेनरेशनल जीसी (2020)
- **पीढ़ीगत कचरा संग्रहकर्ता** - बहुत बेहतर जीसी विराम
- **`<const>`चर** - वास्तविक स्थिरांक
- **`<close>`वेरिएबल** - बंद होने वाले वेरिएबल (संसाधन प्रबंधन, जैसे`defer`या `with`)
-`tostring`मेटामेथड
- स्ट्रिंग उपप्रकार (छोटी बनाम लंबी स्ट्रिंग अलग-अलग अनुकूलित)
## सिंटेक्स इवोल्यूशन
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

## फ़ीचर इवोल्यूशन
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

## गेमिंग में लुआ
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

## मुख्य डिज़ाइन सिद्धांत
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## पारिस्थितिकी तंत्र का विकास
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
