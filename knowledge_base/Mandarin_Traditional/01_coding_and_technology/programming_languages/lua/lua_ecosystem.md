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

# Lua — 生態系與工具指南
本指南涵蓋了 Lua 生態系統中的基本工具、庫和基礎設施。
---

## Lua 版本和實現
|實施 |筆記|
|----------------|--------|
| **Lua 5.4** |目前穩定版本 |
| **LuaJIT** |高效能JIT編譯器|
| **Lua 5.1** |廣泛使用（相容於LuaJIT）|
| **拉維** |帶有可選類型的 JIT |
| **青色** | Lua 的類型化方言 |
| **茴香** |編譯為 Lua 的 Lisp |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## 套件管理
|工具|目的|
|------|---------|
| **LuaRocks** |標準包管理器 |
| **luarocks.org** |套件儲存庫 |
| **點亮** | LuaJIT 套件管理器 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **OpenResty** | Nginx + Lua |高效能網路|
| **盧維特** |類似 Node.js |非同步 I/O (libuv) |
| **軌道** | MVC 網頁 |簡單的網頁應用程式 |
| **水手** |全端| MVC框架|
| **青金石** |基於 OpenResty | MoonScript/Lua 網頁 |
| **飛馬座** |輕量化|簡單的HTTP伺服器|
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

## 資料庫
|技術 |類型 |
|------------|------|
| **luasql** |数据库绑定（SQLite、PostgreSQL、MySQL）|
| **lua-resty-mysql** | MySQL（OpenResty）|
| **lua-resty-redis** | Redis（OpenResty）|
| **lsqlite3** | SQLite3 綁定 |
| **pgmoon** | PostgreSQL（純Lua）|
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

## 測試
|框架|目的|
|------------|---------|
| **被抓** | BDD 式測驗（最受歡迎）|
| **luassert** |斷言庫（已破解）|
| **慾望** |最少的測試 |
| **月球測試** | xUnit 式測試 |
| **青色** |類型檢查（青色方言）|
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

## 程式碼品質
|工具|目的|
|------|---------|
| **luacheck** | Linting 與靜態分析 |
| **lua 格式** |程式碼格式化 |
| **手寫筆** |程式碼格式化程式（基於 Rust，快速）|
| **青色** |輸入 Lua 方言 |
| **盧亞科夫** |代碼覆蓋率|
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **luasocket** | TCP/UDP/HTTP 網路 |
| **lua-cjson / cjson** | JSON解析|
| **LPEG** |模式匹配（基於 PEG）|
| **筆燈（pl）** |實用程式庫（如Python stdlib）|
| **科帕斯** |基於協程的套接字 |
| **coxpcall** |受保護的通話 |
| **lua-resty-* | OpenResty 生態系 |
| **lfs** |檔案系統存取 |
| **lzlib** |壓縮|
| **lbase64** | Base64 編碼 |
| **檢查** |表格漂亮印刷|
| **古典** | OOP類系統|
| **中產階級** |物件導向程式庫 |
| **盧斯塔切** |鬍子模板 |
| **argparse** | CLI 參數解析 |
---

## 遊戲開發
|引擎|筆記|
|--------|--------|
| **愛（Love2D）** | 2D遊戲框架（最受歡迎）|
| **解折疊** |遊戲引擎（Lua腳本）|
| **Corona SDK** |手機遊戲引擎|
| **羅布樂士** |遊戲平台（盧奧方言）|
| **魔獸世界** | UI 腳本（Lua）|
| **Neovim** |編輯器（Lua 腳本）|
| **Redis** | Redis 中的 Lua 腳本 |
| **Nginx/OpenResty** | Nginx 中的 Lua 腳本 |
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

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + Lua (sumneko)** |最佳 Lua LSP |
| **ZeroBrane 工作室** | Lua 专用 IDE |
| **Neovim** | Lua配置（一流）|
| **IntelliJ + EmmyLua** | JetBrains Lua 支援 |
---

## 部署
|方法|筆記|
|--------|--------|
| **獨立** |將 Lua 與應用程式捆綁在一起 |
| **LuaRocks** |打包與分發 |
| **OpenResty** | Nginx + Lua 部署 |
| **碼頭工人** |貨櫃式|
| **嵌入式** |深入 C/C++ 應用程式 |
| **遊戲平台** | LÖVE、Defold、Roblox |
---

＃＃ 概括
Lua 的生態系統很小，但專注於嵌入和腳本編寫。標準工具鍊是：**Lua 5.4** 或 **LuaJIT** 作為運行時，**LuaRocks** 用於包，**busted** 用於測試，**luacheck** 用於 linting，**stylua** 用於格式化。 Lua 在遊戲（LÖVE、Defold、Roblox）、伺服器（OpenResty、Nginx）、資料庫（Redis）和編輯器（Neovim）中的嵌入式語言表現出色。 LuaJIT 為運算密集型腳本提供接近 C 的效能。 Lua 的優勢在於其佔用空間小（約 25KB）、簡單的語法以及用於 C/C++ 整合的出色嵌入 API。