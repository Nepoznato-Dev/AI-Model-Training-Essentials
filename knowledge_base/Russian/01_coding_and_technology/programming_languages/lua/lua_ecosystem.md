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

# Lua — Руководство по экосистеме и инструментам
В этом руководстве рассматриваются основные инструменты, библиотеки и инфраструктура экосистемы Lua.
---

## Версии и реализации Lua
| Реализация | Заметки |
|---------------|-------|
| **Луа 5.4** | Текущая стабильная версия |
| **LuaJIT** | Высокопроизводительный JIT-компилятор |
| **Луа 5.1** | Широко используется (совместим с LuaJIT) |
| **Рави** | JIT с дополнительной типизацией |
| **Бирюзовый** | Типизированный диалект Lua |
| **фенхель** | Lisp, который компилируется в Lua |
```bash
lua -v                    # check version
lua script.lua            # run script
luajit script.lua         # run with LuaJIT
lua -e "print('Hello')"   # inline execution
```

---

## Управление пакетами
| Инструмент | Цель |
|------|---------|
| **ЛуаРокс** | Стандартный менеджер пакетов |
| **luarocks.org** | Репозиторий пакетов |
| **горит** | Менеджер пакетов LuaJIT |
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

## Веб-фреймворки
| Рамочная | Тип | Лучшее для |
|-----------|------|----------|
| **ОткрытьРести** | Нгинкс + Луа | Высокопроизводительный веб |
| **Лювит** | Node.js-подобный | Асинхронный ввод-вывод (libuv) |
| **Орбита** | Веб-страница MVC | Простые веб-приложения |
| **Матрос** | Полный стек | MVC-фреймворк |
| **ляпис** | На основе OpenResty | Веб-сайт MoonScript/Lua |
| **Пегас** | Легкий | Простой HTTP-сервер |
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

## База данных
| Технология | Тип |
|------------|------|
| **луаsql** | Привязки баз данных (SQLite, PostgreSQL, MySQL) |
| **lua-resty-mysql** | MySQL (OpenResty) |
| **lua-resty-redis** | Redis (OpenResty) |
| **lsqlite3** | Привязки SQLite3 |
| **пгмун** | PostgreSQL (чистый Lua) |
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

## Тестирование
| Рамочная | Цель |
|-----------|---------|
| **разорван** | Тестирование в стиле BDD (самое популярное) |
| **луассерт** | Библиотека утверждений (разрушена) |
| **похоть** | Минимальное тестирование |
| **лунный тест** | Тестирование в стиле xUnit |
| **бирюзовый** | Проверка типа (бирюзовый диалект) |
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

## Качество кода
| Инструмент | Цель |
|------|---------|
| **луачек** | Линтинг и статический анализ |
| **формат lua** | Форматирование кода |
| **стилус** | Средство форматирования кода (на основе Rust, быстрое) |
| **бирюзовый** | Типизированный диалект Lua |
| **луаков** | Покрытие кода |
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

## Ключевые библиотеки
| Библиотека | Цель |
|---------|---------|
| **луасокет** | Сеть TCP/UDP/HTTP |
| **lua-cjson / cjson** | Разбор JSON |
| **лпег** | Сопоставление с образцом (на основе PEG) |
| **Фонарик (pl)** | Библиотека утилит (например, Python stdlib) |
| **копас** | Сокет на основе сопрограммы |
| **вызов рулевого** | Защищенные звонки |
| **lua-resty-* | Экосистема OpenResty |
| **лфс** | Доступ к файловой системе |
| **лзлиб** | Сжатие |
| **lbase64** | Кодировка Base64 |
| **проверить** | Настольный красочно-полиграфический |
| **классический** | система классов ООП |
| **средний класс** | библиотека ООП |
| **усы** | Шаблоны усов |
| **аргпарс** | Анализ аргументов CLI |
---

## Разработка игр
| Двигатель | Заметки |
|--------|-------|
| **ЛЮБОВЬ (Love2D)** | Фреймворк для 2D-игр (самый популярный) |
| **Развернуть** | Игровой движок (скрипты Lua) |
| **Корона SDK** | Мобильный игровой движок |
| **Роблокс** | Игровая платформа (диалект Луау) |
| **Мир Warcraft** | Скрипты пользовательского интерфейса (Lua) |
| **Неовим** | Редактор (скрипты Lua) |
| **Редис** | Lua-скрипты в Redis |
| **Nginx/OpenResty** | Lua-скрипты в Nginx |
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

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS Code + Lua (сумнеко)** | Лучший Lua LSP |
| **Студия ZeroBrane** | IDE для Lua |
| **Неовим** | Конфигурация Lua (первоклассная) |
| **IntelliJ + ЭммиЛуа** | Поддержка Lua в JetBrains |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Автономный** | Объединить Lua с приложением |
| **ЛуаРокс** | Упаковать и распространить |
| **ОткрытьРести** | Развертывание Nginx + Lua |
| **Докер** | Контейнерный |
| **Встроенный** | В приложения C/C++ |
| **Игровые платформы** | ЛЮБОВЬ, Дефолд, Роблокс |
---

## Краткое содержание
Экосистема Lua небольшая, но сосредоточена на внедрении и написании сценариев. Стандартная цепочка инструментов: **Lua 5.4** или **LuaJIT** в качестве среды выполнения, **LuaRocks** для пакетов, **busted** для тестирования, **luacheck** для проверки, **stylua** для форматирования. Lua превосходен в качестве встроенного языка в играх (LÖVE, Defold, Roblox), серверах (OpenResty, Nginx), базах данных (Redis) и редакторах (Neovim). LuaJIT обеспечивает производительность, близкую к C, для сценариев с интенсивными вычислениями. Сильными сторонами Lua являются его небольшой размер (около 25 КБ), простой синтаксис и превосходный API-интерфейс для интеграции C/C++.