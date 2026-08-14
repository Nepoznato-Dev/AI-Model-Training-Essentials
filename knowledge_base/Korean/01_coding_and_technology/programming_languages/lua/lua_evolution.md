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

# Lua — 버전 기록 및 진화
## 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 1.0 | 1994년 | 최초 출시(브라질 PUC-Rio) |
| 2.1 | 1995 | 테이블이 유일한 데이터 구조가 됨 |
| 3.0 | 1997 | C API, 태그 메소드(초기 메타메소드) |
| 3.1 | 1998 | 시맨틱 컨트롤러(upvalues) |
| 4.0 | 2000 | **Lua 4**: 참조 계산 + GC, 향상된 C API |
| 5.0 | 2003년 | **주요**: 적절한 어휘 범위 지정, 코루틴, 메타테이블, 부울 |
| 5.1 | 2006년 | **증분 GC**,`#`길이 연산자,`goto`제거,`module()`|
| 5.2 | 2011 | `_ENV`,`_G`변경,`goto`다시 추가, 에페메론 테이블 |
| 5.3 | 2015 | **정수 유형**, 비트 연산자, UTF-8 지원 |
| 5.4 | 2020 | **세대 GC**,`const`/`close`변수,`tostring`메타메서드 |
| 5.4.x | 2020-25 | 점진적인 개선, 경고 시스템 |
| 5.5 | 미정 | (향후) 추가 GC 개선 |
## 주요 이정표
### 루아 1~3: 초기(1994~1999)
- **1994**: Roberto Ierusalimschy, Waldemar Celes, Luiz Henrique de Figueiredo가 PUC-Rio(리우데자네이루 교황청 가톨릭 대학교)에서 창설함
- **목표**: 데이터 입력을 위한 내장형 스크립트 언어(독립형 언어 아님)
- **2.1**: 테이블이 유일한 데이터 구조가 됨 — 획기적인 단순성
- **3.0**: C API가 강화되어 Lua를 C/C++ 애플리케이션에 포함할 수 있게 되었습니다.
- **3.1**: Upvalues — 클로저에 대한 어휘 범위 지정
### 루아 4: 성숙(2000)
- 참조 카운팅 + 가비지 컬렉션(하이브리드)
- 향상된 C API —`luaL_*`보조 라이브러리
- 아직 전역에 대한 적절한 어휘 범위 지정이 없습니다.
### Lua 5.0: 최신 Lua(2003)
- **적절한 어휘 범위 지정** —`local`변수
- **코루틴** — 협력적 멀티태스킹
- **메타테이블** — 연산자 오버로딩, 사용자 정의 동작
- **부울** — 적절한 값인`true`/ `false`
- **클로저**가 제대로 완료됨 - 가치 상승이 일반화됨
- Lua를 게임에 널리 채택하게 만든 버전입니다.
### Lua 5.1: 표준(2006)
- **증분 가비지 수집기**
-`#`길이 연산자
-`module()`기능
- 글로벌 환경 작동 방식 변경
- **이 버전은 가장 널리 포함된 버전이 됩니다**(LuaJIT는 5.1을 목표로 함)
### Lua 5.2: 개선(2011)
-`_ENV`— 청크별 환경(더 깨끗한 전역)
-`goto`문이 반환됩니다.
- 에페메론 테이블(GC 개선)
- 패키지 시스템 개선
### Lua 5.3: 정수 및 비트(2015)
- **정수 하위 유형** — 부동 소수점과 구별됨
- **비트 연산자** —`&`,`|`,`~`,`<<`,`>>`
- **UTF-8 지원** — 내장`utf8`라이브러리
- 바닥구분`//`
- 바이너리 데이터의 경우 문자열`pack`/ `unpack`
### Lua 5.4: 세대별 GC(2020)
- **세대 가비지 수집기** — 훨씬 더 나은 GC 일시 중지
- **`<const>`변수** — 실제 상수
- **`<close>`변수** — 닫힐 변수(`defer`또는`with`와 같은 리소스 관리)
-`tostring`메타메서드
- 문자열 하위 유형(다르게 최적화된 짧은 문자열과 긴 문자열)
## 구문 진화
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

## 기능 진화
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

## 게임 분야의 Lua
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

## 주요 디자인 원칙
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## 생태계 성장
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
