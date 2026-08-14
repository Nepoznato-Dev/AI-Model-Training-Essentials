---
# Metadata
title: "Lua — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lua ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lua, ecosystem, tooling, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Lua — エコシステムとツールのガイド
このガイドでは、Lua エコシステムの重要なツール、ライブラリ、インフラストラクチャについて説明します。
---

## Lua のバージョンと実装
|実装 |メモ |
|---------------|------|
| **ルア 5.4** |現在の安定バージョン |
| **ルアジット** |高性能 JIT コンパイラ |
| **Lua 5.1** |広く使用されています (LuaJIT 互換) |
| **ラヴィ** |オプションの入力を伴う JIT |
| **ティール** | Lua の型付き方言 |
| **フェンネル** | Lua にコンパイルされる Lisp |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **ルアロック** |標準パッケージマネージャー |
| **luarocks.org** |パッケージリポジトリ |
| **点灯** | LuaJIT パッケージマネージャー |
```bash
luarocks install luasocket  # install package
luarocks list               # installed packages
luarocks remove luasocket   # remove package
```

```lua
-- .luarocks configuration
-- luarocks config
rocks_servers = {
    "https://luarocks.org"
}
```

---

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **OpenResty** | Nginx + Lua |高性能ウェブ |
| **ルビット** | Node.js っぽい |非同期 I/O (libuv) |
| **軌道** | MVCウェブ |シンプルなウェブアプリ |
| **セーラー** |フルスタック | MVC フレームワーク |
| **ラピス** | OpenRestyベース | MoonScript/Lua ウェブ |
| **ペガサス** |軽量 |シンプルなHTTPサーバー |
```lua
-- OpenResty / Nginx Lua example
-- nginx.conf
location /hello {
    content_by_lua_block {
        ngx.say("Hello, World!")
    }
}

location /api/users {
    content_by_lua_block {
        local cjson = require "cjson"
        local id = ngx.var.arg_id
        local user = get_user(id)
        ngx.header.content_type = "application/json"
        ngx.say(cjson.encode(user))
    }
}
```

---

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **luasql** |データベース バインディング (SQLite、PostgreSQL、MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | SQLite3バインディング |
| **pgmoon** | PostgreSQL (純粋な Lua) |
```lua
-- SQLite example
local lsqlite3 = require "lsqlite3"

local db = lsqlite3.open("mydb.sqlite")

db:exec[[
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
  )
]]

local stmt = db:prepare("SELECT * FROM users WHERE id = ?")
stmt:bind_values(1)
for row in stmt:nrows() do
    print(row.id, row.name, row.email)
end
```

---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **逮捕されました** | BDD スタイルのテスト (最も一般的) |
| **ルアサート** |アサーション ライブラリ (バスト) |
| **欲望** |最小限のテスト |
| **ルナテスト** | xUnit スタイルのテスト |
| **ティール** |型チェック (ティール方言) |
```lua
-- busted example
describe("UserService", function()
    local service

    before_each(function()
        service = UserService.new()
    end)

    describe("find", function()
        it("returns user when found", function()
            service:add(User.new(1, "Alice"))
            local user = service:find(1)
            assert.is_not_nil(user)
            assert.are.equal("Alice", user.name)
        end)

        it("returns nil when not found", function()
            local user = service:find(999)
            assert.is_nil(user)
        end)
    end)
end)
```

```bash
busted spec/              # run tests
busted --verbose spec/    # verbose output
```

---

## コードの品質
|ツール |目的 |
|-----|----------|
| **ルアチェック** |リンティングと静的分析 |
| **lua 形式** |コードのフォーマット |
| **スタイラ** |コードフォーマッタ (Rust ベース、高速) |
| **ティール** | Lua 方言を入力 |
| **ルアコフ** |コードカバレッジ |
```lua
-- .luacheckrc
std = "lua54"
include_files = {"src/**/*.lua"}
exclude_files = {"spec/**"}

codes = true
ignore = {"631"}  -- ignore line length
```

```bash
luacheck src/           # lint
stylua src/             # format
```

---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **ルアソケット** | TCP/UDP/HTTP ネットワーキング |
| **lua-cjson / cjson** | JSON 解析 |
| **lpeg** |パターン マッチング (PEG ベース) |
| **ペンライト (pl)** |ユーティリティ ライブラリ (Python stdlib など) |
| **コパス** |コルーチンベースのソケット |
| **coxpcall** |保護された通話 |
| **ルア-レスティ-* | OpenRestyエコシステム |
| **lfs** |ファイル システム アクセス |
| **lzlib** |圧縮 |
| **lbase64** | Base64エンコーディング |
| **検査** |テーブルのきれいな印刷 |
| **クラシック** | OOPクラスシステム |
| **中産階級** | OOPライブラリ |
| **食欲** |口ひげテンプレート |
| **argparse** | CLI 引数の解析 |
---

## ゲーム開発
|エンジン |メモ |
|------|------|
| **ラブ (Love2D)** | 2D ゲーム フレームワーク (最も人気のある) |
| **展開** |ゲームエンジン (Lua スクリプト) |
| **コロナ SDK** |モバイル ゲーム エンジン |
| **ロブロックス** |ゲームプラットフォーム（ルアウ方言） |
| **ワールド オブ ウォークラフト** | UI スクリプト (Lua) |
| **ネオビム** |エディター (Lua スクリプト) |
| **Redis** | Redis での Lua スクリプト |
| **Nginx/OpenResty** | Nginx での Lua スクリプト |
```lua
-- LÖVE example
function love.load()
    x, y = 400, 300
end

function love.update(dt)
    if love.keyboard.isDown("left") then x = x - 200 * dt end
    if love.keyboard.isDown("right") then x = x + 200 * dt end
end

function love.draw()
    love.graphics.circle("fill", x, y, 50)
end
```

---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + Lua (すむねこ)** |最高の Lua LSP |
| **ZeroBrane スタジオ** | Lua 固有の IDE |
| **ネオビム** | Lua 構成 (ファーストクラス) |
| **IntelliJ + EmmyLua** | JetBrains Lua サポート |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **スタンドアロン** | Lua をアプリにバンドルする |
| **ルアロック** |パッケージ化して配布する |
| **OpenResty** | Nginx + Lua のデプロイメント |
| **ドッカー** |コンテナ化 |
| **埋め込み** | C/C++ アプリケーションへ |
| **ゲーム プラットフォーム** |ラブ、デフォールド、ロブロックス |
---

＃＃ まとめ
Lua のエコシステムは小さいですが、埋め込みとスクリプトに重点を置いています。標準ツールチェーンは、ランタイムとして **Lua 5.4** または **LuaJIT**、パッケージ用に **LuaRocks**、テスト用に **busted**、lint 用に **luacheck**、フォーマット用に **stylua** です。 Lua は、ゲーム (LÖVE、Defold、Roblox)、サーバー (OpenResty、Nginx)、データベース (Redis)、エディター (Neovim) の組み込み言語として優れています。 LuaJIT は、計算負荷の高いスクリプトに対して C に近いパフォーマンスを提供します。 Lua の強みは、その小さなフットプリント (約 25KB)、シンプルな構文、および C/C++ 統合のための優れた埋め込み API です。