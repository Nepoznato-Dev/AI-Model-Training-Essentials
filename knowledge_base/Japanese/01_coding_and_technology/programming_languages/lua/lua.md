---
# Metadata
title: "Lua"
description: "Comprehensive reference for the Lua programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [lua, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "26 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

#ルア
Lua は、アプリケーションを拡張するために設計された軽量の埋め込み可能なスクリプト言語です。 Lua は、ブラジルのリオデジャネイロ教皇庁カトリック大学で 1993 年に作成された、最も高速なスクリプト言語の 1 つです。フットプリントが小さく (インタプリタは約 120 KB)、シンプルであるため、ゲーム開発スクリプト、組み込みシステム、構成に最適です。
Lua は、Roblox (月間ユーザー数 2 億人以上のゲーム プラットフォーム)、World of Warcraft アドオン、および多数のゲーム エンジン (Love2D、Defold、Corona SDK) の背後にあるスクリプト言語として最もよく知られています。 Nginx (OpenResty)、Redis、Wireshark でも使用されます。
---

## Lua が重要な理由
- **埋め込み可能**: 他のアプリケーションに埋め込まれるように設計されており、ホストが機能を提供します。
- **小さなフットプリント**: インタプリタ全体は約 120KB に収まります。組み込みシステムに最適です。
- **高速**: 最も高速に解釈されるスクリプト言語の 1 つ。
- **シンプル**: キーワードは最大 20 個のみです。学習と統合が簡単です。
- **ゲーム開発**: 多くのゲーム エンジンおよびプラットフォームの標準スクリプト言語。
- **Roblox**: ユーザーが作成した何百万ものゲームなど、Roblox エコシステム全体を強化します。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **限定された標準ライブラリ** |最小限の組み込み機能 | C/C++ で拡張するか、LuaRocks パッケージを使用する |
| **1 ベースのインデックス付け** |配列はインデックス 1 から始まります (プログラマにとっては珍しいことです)。デザインの選択として受け入れます。全体を通して一貫性がある |
| **授業はありません** |テーブルとメタテーブルのみ - OOP は手動で実装する必要があります。メタテーブルまたは OOP ライブラリを使用する |
| **ニッチなゲーム外** | Web、データ サイエンス、またはエンタープライズでの限定的な使用 |スクリプト/埋め込みに使用します。アプリケーション用の他の言語 |
| **小規模な雇用市場** |主にゲーム開発と組み込みの役割 | Roblox 開発は成長するニッチ市場です |
---

## 構文の基礎
```lua
-- Variables
local name = "Alice"
local age = 30
local score = 9.5

-- Tables (the only data structure — used as arrays, maps, objects)
local user = {name = "Alice", age = 30}
local fruits = {"apple", "banana", "cherry"}  -- Array (1-indexed!)

print(user.name)        -- "Alice"
print(fruits[1])        -- "apple" (Lua arrays start at 1)

-- Functions
local function greet(name, greeting)
    greeting = greeting or "Hello"  -- Default value
    return greeting .. ", " .. name .. "!"
end

-- Higher-order functions
local function apply(fn, value)
    return fn(value)
end

local double = function(x) return x * 2 end
print(apply(double, 5))  -- 10

-- Conditionals and loops
if age >= 18 then
    print("Adult")
elseif age >= 13 then
    print("Teenager")
else
    print("Child")
end

for i = 1, 10 do
    print(i)
end

for index, fruit in ipairs(fruits) do
    print(index, fruit)
end

-- Metatables (OOP-like behaviour)
local Animal = {}
Animal.__index = Animal

function Animal.new(name)
    local self = setmetatable({}, Animal)
    self.name = name
    return self
end

function Animal:speak()
    return self.name .. " makes a sound"
end

local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
    local self = Animal.new(name)
    return setmetatable(self, Dog)
end

function Dog:speak()
    return self.name .. " says woof"
end

local rex = Dog.new("Rex")
print(rex:speak())  -- "Rex says woof"
```

---

## 高度な構文とパターン
### メタテーブル — Lua のパワーの基盤
```lua
-- Metatables allow custom behaviour for tables
local Vector = {}
Vector.__index = Vector

function Vector.new(x, y)
    return setmetatable({x = x, y = y}, Vector)
end

-- Operator overloading via metamethods
function Vector.__add(a, b)
    return Vector.new(a.x + b.x, a.y + b.y)
end

function Vector.__mul(a, b)
    if type(b) == "number" then
        return Vector.new(a.x * b, a.y * b)
    end
    return a.x * b.x + a.y * b.y  -- Dot product
end

function Vector.__tostring(v)
    return string.format("Vector(%.1f, %.1f)", v.x, v.y)
end

function Vector.__eq(a, b)
    return a.x == b.x and a.y == b.y
end

function Vector:magnitude()
    return math.sqrt(self.x^2 + self.y^2)
end

local v1 = Vector.new(3, 4)
local v2 = Vector.new(1, 2)
print(v1 + v2)          -- Vector(4.0, 6.0)
print(v1 * 2)           -- Vector(6.0, 8.0)
print(v1 * v2)          -- 11 (dot product)
print(v1:magnitude())   -- 5.0
print(v1 == Vector.new(3, 4))  -- true
```

### クロージャーと機能パターン
```lua
-- Closures — functions capture upvalues
local function make_counter()
    local count = 0
    return function()
        count = count + 1
        return count
    end
end

local counter = make_counter()
print(counter())  -- 1
print(counter())  -- 2
print(counter())  -- 3

-- Functional utilities
local function map(t, fn)
    local result = {}
    for i, v in ipairs(t) do
        result[i] = fn(v)
    end
    return result
end

local function filter(t, fn)
    local result = {}
    for _, v in ipairs(t) do
        if fn(v) then result[#result + 1] = v end
    end
    return result
end

local function reduce(t, fn, init)
    local acc = init
    for _, v in ipairs(t) do
        acc = fn(acc, v)
    end
    return acc
end

local numbers = {1, 2, 3, 4, 5}
local doubled = map(numbers, function(x) return x * 2 end)
local evens = filter(numbers, function(x) return x % 2 == 0 end)
local sum = reduce(numbers, function(a, b) return a + b end, 0)
```

### 複数の戻り値と構造化
```lua
-- Lua functions can return multiple values
local function minmax(t)
    local min, max = math.huge, -math.huge
    for _, v in ipairs(t) do
        if v < min then min = v end
        if v > max then max = v end
    end
    return min, max
end

local lo, hi = minmax({5, 2, 8, 1, 9, 3})
print(lo, hi)  -- 1  9

-- Variadic functions
local function sum(...)
    local total = 0
    for _, v in ipairs({...}) do
        total = total + v
    end
    return total
end

print(sum(1, 2, 3, 4, 5))  -- 15

-- Table unpacking
local a, b, c = table.unpack({10, 20, 30})
print(a, b, c)  -- 10  20  30
```

### 文字列パターン (Lua の正規表現の代替)
```lua
-- Lua patterns — simpler than regex but powerful
local text = "Error 404: Page not found on 2024-01-15"

-- Basic matching
local code, msg = text:match("Error (%d+): (.+)")
print(code)  -- "404"
print(msg)   -- "Page not found on 2024-01-15"

-- Find and replace
local replaced = text:gsub("not found", "missing")

-- Pattern character classes
-- %a = letters, %d = digits, %w = alphanumeric
-- %s = whitespace, %p = punctuation
local email = "user@example.com"
local valid = email:match("^[%w%.%-]+@[%w%.%-]+%.%a+$")

-- Capture groups
local date = "2024-01-15"
local year, month, day = date:match("(%d+)-(%d+)-(%d+)")
```

---

## 同時実行性と並列処理
### コルーチン — 協調的なマルチタスク
```lua
-- Coroutines — Lua's built-in cooperative concurrency
local function producer()
    local items = {"apple", "banana", "cherry"}
    for _, item in ipairs(items) do
        print("Producing: " .. item)
        coroutine.yield(item)
    end
    return "done"
end

local co = coroutine.create(producer)

print(coroutine.status(co))  -- "suspended"
local ok, value = coroutine.resume(co)
print("Got:", value)         -- Got: apple
print(coroutine.status(co))  -- "suspended"

coroutine.resume(co)  -- banana
coroutine.resume(co)  -- cherry
print(coroutine.status(co))  -- "dead"
```

### コルーチンベースの反復子パターン
```lua
-- Coroutine wrapping for clean iteration
local function coroutine_iterator(body)
    local co = coroutine.create(body)
    return function()
        local ok, value = coroutine.resume(co)
        if not ok or coroutine.status(co) == "dead" then
            return nil
        end
        return value
    end
end

-- Usage: generate fibonacci numbers lazily
local fib = coroutine_iterator(function()
    local a, b = 0, 1
    while true do
        coroutine.yield(a)
        a, b = b, a + b
    end
end)

for i = 1, 10 do
    io.write(fib() .. " ")  -- 0 1 1 2 3 5 8 13 21 34
end

-- Coroutine-based async I/O (with Copas or OpenResty)
local copas = require("copas")

local function fetch_url(url)
    local sock = copas.tcp()
    sock:connect(url, 80)
    sock:send("GET / HTTP/1.1\r\nHost: " .. url .. "\r\n\r\n")
    local response = sock:receive("*a")
    sock:close()
    return response
end

-- Multiple concurrent connections
copas.addthread(fetch_url, "example.com")
copas.addthread(fetch_url, "example.org")
copas.loop()
```

---

## プロジェクトの構成とシステムの構築
### プロジェクトの構造
```
my-lua-project/
├── src/
│   ├── main.lua
│   ├── config.lua
│   ├── models/
│   ├── utils/
│   └── game/
├── spec/
│   └── test_main.lua
├── rocks/           -- LuaRocks packages
├── .luacheckrc      -- Linting config
├── Makefile
└── rockspec         -- Package spec
```

### LuaRocks — パッケージ管理
```bash
# Install packages
luarocks install luasocket       # Networking
luarocks install lua-cjson       # JSON parsing
luarocks install busted          # Testing framework
luarocks install luacheck        -- Linting

# Project dependencies via rockspec
# myproject-1.0-1.rockspec
```

### Rockspec — パッケージ仕様
```lua
-- myproject-1.0-1.rockspec
package = "myproject"
version = "1.0-1"

source = {
    url = "git+https://github.com/user/myproject.git",
    tag = "v1.0",
}

dependencies = {
    "lua >= 5.3",
    "luasocket",
    "lua-cjson",
}

build = {
    type = "builtin",
    modules = {
        ["myproject.core"] = "src/core.lua",
        ["myproject.utils"] = "src/utils.lua",
    },
}
```

### CI/CD パイプライン (GitHub アクション)
```yaml
name: Lua CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    strategy:
      matrix:
        lua-version: ['5.3', '5.4', 'luajit']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: leafo/gh-actions-lua@v10
        with:
          luaVersion: ${{ matrix.lua-version }}
      - uses: leafo/gh-actions-luarocks@v4
      - run: luarocks install busted
      - run: luarocks install luacheck
      - run: luacheck src/
      - run: busted spec/
```
---

## テスト
### バステッド — テストフレームワーク
```lua
-- spec/utils_spec.lua
local utils = require("src.utils")

describe("utils", function()
    describe("add", function()
        it("adds two positive numbers", function()
            assert.are.equal(utils.add(2, 3), 5)
        end)
        it("handles negative numbers", function()
            assert.are.equal(utils.add(-1, 1), 0)
        end)
    end)
    describe("format_name", function()
        it("capitalizes first letter", function()
            assert.are.equal(utils.format_name("alice"), "Alice")
        end)
    end)
end)
```

### luassert によるモッキング
```lua
describe("UserService", function()
    local service, mock_repo
    before_each(function()
        mock_repo = {
            save = spy.new(function() return true end),
            find = spy.new(function(id) return {id=id, name="Alice"} end),
        }
        service = require("src.user_service").new(mock_repo)
    end)
    it("saves user via repository", function()
        service:create("Alice", "alice@example.com")
        assert.spy(mock_repo.save).was_called(1)
    end)
end)
```

### テストコマンド
```bash
busted spec/                    # Run all tests
busted spec/utils_spec.lua      # Run specific file
busted --verbose spec/          # Verbose output
```

---

## 相互運用性
### C API — C への Lua の埋め込み
```c
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

int main(void) {
    lua_State *L = luaL_newstate();
    luaL_openlibs(L);
    luaL_dofile(L, "script.lua");
    lua_getglobal(L, "greet");
    lua_pushstring(L, "World");
    lua_pcall(L, 1, 1, 0);
    printf("Lua says: %s\n", lua_tostring(L, -1));
    lua_close(L);
    return 0;
}
// Compile: gcc -o host host.c -llua5.4
```

### LuaJIT FFI — 直接 C 呼び出し
```lua
local ffi = require("ffi")
ffi.cdef[[
    double sqrt(double x);
    int abs(int n);
]]
local C = ffi.C
print(C.sqrt(144))   -- 12.0
print(C.abs(-42))    -- 42
```

---

## デザインパターン
### モジュール パターン (シングルトン)
```lua
-- config.lua — modules are singletons by design
local config = {
    debug = false,
    version = "1.0.0",
}
function config.get(key) return config[key] end
function config.set(key, value) config[key] = value end
return config
```

### オブザーバー / イベント システム
```lua
local EventBus = {}
EventBus.__index = EventBus

function EventBus.new()
    return setmetatable({listeners = {}}, EventBus)
end

function EventBus:on(event, callback)
    self.listeners[event] = self.listeners[event] or {}
    table.insert(self.listeners[event], callback)
end

function EventBus:emit(event, ...)
    if self.listeners[event] then
        for _, cb in ipairs(self.listeners[event]) do cb(...) end
    end
end

local bus = EventBus.new()
bus:on("player_died", function(p) print(p.name .. " died!") end)
bus:emit("player_died", {name = "Hero"})
```

### コマンドパターン
```lua
local Command = {}
Command.__index = Command

function Command.new(name, exec, undo)
    return setmetatable({name=name, execute=exec, undo=undo}, Command)
end

local history = {}
local cmd = Command.new("move",
    function() print("Moving") end,
    function() print("Undoing move") end)
cmd.execute()
table.insert(history, cmd)
if #history > 0 then table.remove(history).undo() end
```
---

## パフォーマンスと最適化
```bash
luajit -jp=v script.lua
luajit -jv script.lua
```

```lua
local sqrt = math.sqrt
local tconcat = table.concat
local parts = {}
for i = 1, 1000 do parts[#parts + 1] = tostring(i) end
local result = tconcat(parts, ',')
```

---

## デプロイメント
### Docker のデプロイメント
```dockerfile
FROM alpine:3.19
RUN apk add --no-cache lua5.4
WORKDIR /app
COPY . .
CMD lua5.4 src/main.lua
```

---

## Lua を使用する場合
|シナリオ |なぜ Lua |より良い代替案 |
|----------|----------|----------|
|ゲームスクリプト |軽量、高速、組み込み可能 | — |
| Roblox開発 |唯一の選択肢 | — |
|組み込みシステム |設置面積が小さい | C、マイクロPython |
|アプリケーション拡張機能 |埋め込み用に設計 | Python (大きい)、JavaScript (V8) |
|設定ファイル |シンプルで速い | JSON、TOML、YAML |
|ウェブ開発 | OpenResty は存在しますが、ニッチです | JavaScript、Python、Go |
|一般的なアプリケーション開発 |スタンドアロン アプリ用に設計されていません | Python、Go、Java |
|データサイエンス |エコシステムではありません |パイソン、R |
---

## 総合的な Q&A
### Q1: Lua はなぜ 0 ベースではなく 1 ベースのインデックスを使用するのですか?
**A:** Lua はプログラマ以外のユーザー向けに設計されており、自然なカウント規則に従っています。`#`演算子、`ipairs`、および文字列関数はすべて 1 から始まるインデックスを使用します。
```lua
local items = {"a", "b", "c"}
print(items[1])  -- "a" (first element)
print(#items)    -- 3

-- String functions are also 1-based
print(string.sub("hello", 1, 3))  -- "hel"
print(string.find("hello", "ll")) -- 3 (starts at position 3)
```

これは標準ライブラリ全体で一貫しています。 C (0 ベース) とインターフェイスする場合は、オフセットに注意してください。
### Q2: Lua でオブジェクト指向パターンを実装するにはどうすればよいですか?
**A:** Lua は OOP にテーブルとメタテーブルを使用します。`__index`メタメソッドにより、プロトタイプのメソッド検索が可能になります。
```lua
-- Class-like pattern
local Animal = {}
Animal.__index = Animal

function Animal.new(name, sound)
  return setmetatable({name = name, sound = sound}, Animal)
end

function Animal:speak()
  print(self.name .. " says " .. self.sound)
end

-- Inheritance
local Dog = setmetatable({}, {__index = Animal})
Dog.__index = Dog

function Dog.new(name)
  return Animal.new(name, "Woof!")
end

function Dog:fetch()
  print(self.name .. " fetches the ball!")
end

local rex = Dog.new("Rex")
rex:speak()   -- "Rex says Woof!"
rex:fetch()   -- "Rex fetches the ball!"
```

### Q3: コルーチンはどのように機能し、いつ使用する必要がありますか?
**A:** コルーチンは、実行を一時停止したり再開したりできる協調的なスレッドです。これらはイテレータ、非同期パターン、ゲーム ロジックに最適です。
```lua
-- Producer coroutine
function produce()
  for i = 1, 5 do
    coroutine.yield(i)  -- suspend, returning value
  end
end

local co = coroutine.create(produce)
print(coroutine.resume(co))  -- true, 1
print(coroutine.resume(co))  -- true, 2
print(coroutine.resume(co))  -- true, 3

-- Iterator pattern
function range(from, to)
  return coroutine.wrap(function()
    for i = from, to do
      coroutine.yield(i)
    end
  end)
end

for n in range(1, 5) do
  print(n)  -- 1, 2, 3, 4, 5
end
```

### Q4: Lua でエラーを処理する最善の方法は何ですか?
**A:**`pcall`/`xpcall`を使用してエラーを検出し、成功/失敗パターンの複数の値を返します。
```lua
-- pcall — protected call
local ok, result = pcall(function()
  return risky_operation()
end)
if not ok then
  print("Error: " .. result)  -- result is the error message
end

-- xpcall — with custom error handler
local ok, result = xpcall(
  function() return process() end,
  function(err) return debug.traceback(err) end
)

-- Idiomatic: return nil + message on failure
function read_config(path)
  local f = io.open(path, "r")
  if not f then return nil, "Cannot open: " .. path end
  local content = f:read("*a")
  f:close()
  return content
end

local config, err = read_config("app.conf")
if not config then error(err) end
```

### Q5: ゲームや組み込みシステムの Lua パフォーマンスを最適化するにはどうすればよいですか?
**A:** 主な実践方法:
- すべての変数に`local`を使用します。グローバル アクセスは大幅に遅くなります。
- 頻繁にアクセスされるテーブルフィールドをローカルにキャッシュする
- サイズがわかっている場合にテーブルを事前に割り当てます:`local t = {}; for i = 1, 1000 do t[i] = 0 end`
- ホットループでの一時テーブルの作成を避ける
- 多くの文字列を結合するには、`..` の代わりに`table.concat`を使用します
-`os.clock()`またはデバッグフックを使用したプロファイル
- LuaJIT では、C API の代わりに FFI を C 相互運用に使用します
---

## 思考連鎖による問題解決
### 問題 1: 構成パーサーの構築
**ステップ 1: 問題を理解する**
各行が`key = value`である単純なキーと値の構成ファイルを解析します。
**ステップ 2: アプローチを特定する**
行を読み取り、`=`で分割し、空白をトリミングして、テーブルに保存します。
**ステップ 3: 実装**```lua
function parse_config(filename)
  local config = {}
  local f = assert(io.open(filename, "r"))
  for line in f:lines() do
    -- Skip comments and empty lines
    line = line:match("^%s*(.-)%s*$")  -- trim
    if line ~= "" and not line:match("^#") then
      local key, value = line:match("^([^=]+)=(.*)$")
      if key and value then
        -- Trim key and value
        key = key:match("^%s*(.-)%s*$")
        value = value:match("^%s*(.-)%s*$")
        config[key] = value
      end
    end
  end
  f:close()
  return config
end

-- Usage: config = parse_config("app.conf")
-- config["host"] => "localhost"
```

**ステップ 4: 延長**
セクションのサポート (`[section]`)、型強制 (数値、ブール値)、およびネストされたテーブルを追加します。
### 問題 2: 単純なイベント システムの実装
**ステップ 1: 問題を理解する**
名前付きイベントのサブスクライブと発行をサポートするイベント エミッターを作成します。
**ステップ 2: アプローチを特定する**
イベント名をハンドラー関数のリストにマッピングするテーブルを使用します。
**ステップ 3: 実装**```lua
local EventBus = {}
EventBus.__index = EventBus

function EventBus.new()
  return setmetatable({listeners = {}}, EventBus)
end

function EventBus:on(event, handler)
  if not self.listeners[event] then
    self.listeners[event] = {}
  end
  table.insert(self.listeners[event], handler)
  return self  -- chainable
end

function EventBus:emit(event, ...)
  local handlers = self.listeners[event] or {}
  for _, handler in ipairs(handlers) do
    handler(...)
  end
end

function EventBus:off(event, handler)
  local handlers = self.listeners[event] or {}
  for i, h in ipairs(handlers) do
    if h == handler then
      table.remove(handlers, i)
      break
    end
  end
end

-- Usage
local bus = EventBus.new()
bus:on("data", function(msg) print("Got: " .. msg) end)
bus:on("data", function(msg) print("Also: " .. msg) end)
bus:emit("data", "hello")  -- Got: hello / Also: hello
```

**ステップ 4: 確認**
複数のイベント、削除、ハンドラーでのエラー処理を使用してテストします。
### 問題 3: コルーチンベースのパイプラインの作成
**ステップ 1: 問題を理解する**
各ステージがデータをフィルターまたは変換し、コルーチンを介して接続されるデータ処理パイプラインを構築します。
**ステップ 2: アプローチを特定する**
コルーチンをパイプライン ステージとして使用します。各ステージは前のステージからプルし、次のステージにプッシュします。
**ステップ 3: 実装**```lua
-- Source: generates values
function source(t)
  return coroutine.wrap(function()
    for _, v in ipairs(t) do
      coroutine.yield(v)
    end
  end)
end

-- Filter: passes through values matching predicate
function filter(pred, input)
  return coroutine.wrap(function()
    for v in input do
      if pred(v) then coroutine.yield(v) end
    end
  end)
end

-- Map: transforms values
function map(fn, input)
  return coroutine.wrap(function()
    for v in input do
      coroutine.yield(fn(v))
    end
  end)
end

-- Compose pipeline
local data = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
local pipeline = map(
  function(x) return x * x end,
  filter(
    function(x) return x % 2 == 0 end,
    source(data)
  )
)

for v in pipeline do
  print(v)  -- 4, 16, 36, 64, 100
end
```

**ステップ 4: 最適化**
このプルベースのパイプラインは、最小限のメモリ オーバーヘッドで一度に 1 つの要素を処理します。大規模なストリームや無限のストリームに最適です。
---

＃＃ まとめ
Lua は典型的な埋め込み言語です。これは小型、高速、シンプルであり、他のアプリケーション内で動作し、スクリプト機能を提供するように設計されています。ゲーム開発、Roblox、組み込みシステムには、Lua が最適な選択肢です。これは汎用言語ではありませんが、その特定のニッチ分野 (スクリプトと埋め込み) では、ほぼ比類のない言語です。