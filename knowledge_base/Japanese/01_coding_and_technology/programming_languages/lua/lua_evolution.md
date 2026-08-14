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
# Lua — バージョンの歴史と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| 1.0 | 1994年 |初期リリース (PUC-リオ、ブラジル) |
| 2.1 | 1995年 |テーブルが唯一のデータ構造になります |
| 3.0 | 1997年 | C API、タグメソッド (初期のメタメソッド) |
| 3.1 | 1998年 |セマンティック コントローラー (上位値) |
| 4.0 | 2000年 | **Lua 4**: 参照カウント + GC、C API の改善 |
| 5.0 | 2003年 | **主要**: 適切な字句スコープ、コルーチン、メタテーブル、ブール値 |
| 5.1 | 2006年 | **インクリメンタル GC**、`#` 長さ演算子、`goto` が削除、`module()` |
| 5.2 | 2011年 | `_ENV`、`_G`の変更、`goto`の追加、エフェメロン テーブル |
| 5.3 | 2015年 | **整数型**、ビットごとの演算子、UTF-8 サポート |
| 5.4 | 2020年 | **世代 GC**、`const` /`close`変数、`tostring` メタメソッド |
| 5.4.x | 2020–25 |段階的な改善、警告システム |
| 5.5 |未定 | (将来) GC のさらなる改善 |
## 主要なマイルストーン
### ルア 1 ～ 3: 初期の頃 (1994 ～ 1999 年)
- **1994**: PUC-Rio (リオデジャネイロ教皇庁カトリック大学) で、Roberto Ierusalimschy、Waldemar Celes、Luiz Henrique de Figueiredo によって作成されました。
- **目標**: データ入力用の埋め込み可能なスクリプト言語 (スタンドアロン言語ではありません)
- **2.1**: テーブルが唯一のデータ構造になる - 大幅な簡素化
- **3.0**: C API の固定化 — Lua を C/C++ アプリケーションに埋め込み可能にします
- **3.1**: Upvalues — クロージャの字句スコープ設定
### Lua 4: 成熟 (2000)
- 参照カウント + ガベージ コレクション (ハイブリッド)
- 改善された C API —`luaL_*`補助ライブラリ
- グローバルに対する適切な語彙スコープがまだありません
### Lua 5.0: モダンな Lua (2003)
- **適切な字句スコープ** —`local`変数
- **コルーチン** — 協調的なマルチタスク
- **メタテーブル** — 演算子のオーバーロード、カスタム動作
- **ブール値** —`true`/`false`を適切な値として
- **クロージャ**は適切に行われ、上位値が一般化されました
- これは、Lua をゲームに広く採用したバージョンです
### Lua 5.1: スタンダード (2006)
- **増分ガベージ コレクター**
-`#`長さ演算子
- `module()`関数
- 地球環境の仕組みが変わりました
- **このバージョンは最も広く埋め込まれているバージョンになります** (LuaJIT は 5.1 をターゲットとしています)
### Lua 5.2: 改良 (2011)
-`_ENV`— チャンクごとの環境 (よりクリーンなグローバル)
-`goto`ステートメントが返す
- Ephemeron テーブル (GC の改善)
- パッケージシステムの改善
### Lua 5.3: 整数とビット (2015)
- **整数のサブタイプ** — 浮動小数点とは異なります
- **ビット演算子** —`&`、`|`、`~`、`<<`、`>>`
- **UTF-8 サポート** — 組み込み`utf8`ライブラリ
- フロア区分`//`
- バイナリデータの場合は文字列`pack`/ `unpack`
### Lua 5.4: 世代別 GC (2020)
- **世代別ガベージ コレクター** — GC 一時停止が大幅に改善されました
- **`<const>`変数** — 真の定数
- **`<close>`変数** — クローズされる変数 (`defer`や`with`などのリソース管理)
-`tostring`メタメソッド
- 文字列サブタイプ (異なる方法で最適化された短い文字列と長い文字列)
## 構文の進化
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

## 機能の進化
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

## ゲームにおける Lua
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

## 主要な設計原則
```
1. "Simple, embeddable, extensible" — designed to be hosted
2. "Mechanism, not policy" — provide tools, don't enforce patterns
3. "Small footprint" — core interpreter is ~200KB
4. "One data structure" — tables do everything (arrays, maps, objects, modules)
5. "Portable" — ANSI C, runs everywhere
6. "Efficient" — LuaJIT is one of the fastest dynamic languages
```

## エコシステムの成長
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
