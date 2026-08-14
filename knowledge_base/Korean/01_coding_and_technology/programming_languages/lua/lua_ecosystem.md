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

# Lua — 생태계 및 툴링 가이드
이 가이드에서는 Lua 생태계의 필수 도구, 라이브러리 및 인프라를 다룹니다.
---

## Lua 버전 및 구현
| 구현 | 메모 |
|---------------|-------|
| **루아 5.4** | 현재 안정 버전 |
| **루아짓** | 고성능 JIT 컴파일러 |
| **루아 5.1** | 널리 사용됨(LuaJIT 호환) |
| **라비** | 선택적 입력이 포함된 JIT |
| **청록색** | 루아의 타이핑 방언 |
| **회향** | Lua로 컴파일되는 Lisp |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **루아록스** | 표준 패키지 관리자 |
| **luarocks.org** | 패키지 저장소 |
| **점등** | LuaJIT 패키지 관리자 |
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

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **오픈레스티** | Nginx + 루아 | 고성능 웹 |
| **루빛** | Node.js와 유사한 | 비동기 I/O(libuv) |
| **궤도** | MVC 웹 | 간단한 웹 앱 |
| **선원** | 풀스택 | MVC 프레임워크 |
| **라피스** | OpenResty 기반 | 문스크립트/루아 웹 |
| **페가수스** | 경량 | 간단한 HTTP 서버 |
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

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **루아SQL** | 데이터베이스 바인딩(SQLite, PostgreSQL, MySQL) |
| **루아-레스티-mysql** | MySQL(오픈레스티) |
| **lua-resty-redis** | Redis(오픈레스티) |
| **lsqlite3** | SQLite3 바인딩 |
| **pgmoon** | PostgreSQL(순수 Lua) |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **파괴됨** | BDD 스타일 테스트(가장 인기 있음) |
| **루어설트** | 어설션 라이브러리(파괴됨) |
| **욕망** | 최소한의 테스트 |
| **가장 미치광이** | xUnit 스타일 테스트 |
| **청록색** | 유형 확인(Teal 방언) |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **루아체크** | 린팅 및 정적 분석 |
| **lua 형식** | 코드 서식 |
| **스타일루아** | 코드 포맷터(Rust 기반, 빠른) |
| **청록색** | 루아 방언 |
| **루아코프** | 코드 적용 범위 |
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

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **루아소켓** | TCP/UDP/HTTP 네트워킹 |
| **lua-cjson / cjson** | JSON 구문 분석 |
| **LPEG** | 패턴 매칭(PEG 기반) |
| **펜라이트(pl)** | 유틸리티 라이브러리(예: Python stdlib) |
| **코파스** | 코루틴 기반 소켓 |
| **콕스콜** | 보호된 통화 |
| **lua-resty-* | OpenResty 생태계 |
| **lfs** | 파일 시스템 액세스 |
| **lzlib** | 압축 |
| **lbase64** | Base64 인코딩 |
| **검사** | 테이블 예쁘게 프린팅 |
| **클래식** | OOP 수업 시스템 |
| **중산층** | OOP 라이브러리 |
| **루스타치** | 콧수염 템플릿 |
| **인수 분석** | CLI 인수 구문 분석 |
---

## 게임 개발
| 엔진 | 메모 |
|---------|-------|
| **러브(Love2D)** | 2D 게임 프레임워크(가장 인기) |
| **디폴드** | 게임 엔진(Lua 스크립팅) |
| **코로나 SDK** | 모바일 게임 엔진 |
| **로블록스** | 게임 플랫폼(루아우 방언) |
| **월드 오브 워크래프트** | UI 스크립팅(Lua) |
| **네오빔** | 편집기(Lua 스크립팅) |
| **레디스** | Redis의 Lua 스크립팅 |
| **Nginx/OpenResty** | Nginx의 Lua 스크립팅 |
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

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + 루아(sumneko)** | 최고의 루아 LSP |
| **제로브레인 스튜디오** | Lua 관련 IDE |
| **네오빔** | Lua 구성(일급) |
| **IntelliJ + EmmyLua** | JetBrains Lua 지원 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **독립형** | Lua를 앱과 번들로 묶기 |
| **루아록스** | 패키지 및 배포 |
| **오픈레스티** | Nginx + Lua 배포 |
| **도커** | 컨테이너화 |
| **내장형** | C/C++ 애플리케이션으로 |
| **게임 플랫폼** | 러브, 디폴드, 로블록스 |
---

## 요약
Lua의 생태계는 작지만 임베딩과 스크립팅에 중점을 둡니다. 표준 툴체인은 런타임의 경우 **Lua 5.4** 또는 **LuaJIT**, 패키지의 경우 **LuaRocks**, 테스트의 경우 **busted**, Linting의 경우 **luacheck**, 서식 지정의 경우 **stylua**입니다. Lua는 게임(LÖVE, Defold, Roblox), 서버(OpenResty, Nginx), 데이터베이스(Redis) 및 편집기(Neovim)에 내장된 언어로서 탁월합니다. LuaJIT는 컴퓨팅 집약적인 스크립트에 C에 가까운 성능을 제공합니다. Lua의 강점은 작은 설치 공간(~25KB), 간단한 구문, C/C++ 통합을 위한 뛰어난 임베딩 API입니다.