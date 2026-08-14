<!--
---
# Metadata
title: "Erlang & Elixir — Version History & Evolution"
description: "Comprehensive version history and evolution of Erlang and Elixir from 1986 to modern."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [erlang, elixir, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Erlang 和 Elixir — 版本歷史和演變
## Erlang 時間軸
|版本 |年份|關鍵主題 |
|--------|------|------------|
| Erlang 1 | 1986 | **第一個 Erlang**（喬·阿姆斯特朗，愛立信）|
| Erlang 4 | 1991 |首次公開發布 |
| Erlang 5（R1）| 1998 | **開源**發布 |
| R9B | 2002 | Mnesia 資料庫，效能提升 |
| R12B | 2006 |透析器（類型檢查器）|
| R13B | 2008 |記錄改進，`fun` 改進 |
| R14B | 2010 |二元理解，改進的 GC |
| R15B | 2012 |地圖（實驗）|
| R16B | 2013 | **地圖** 穩定 |
| 17.0 | 17.0 2014年| **主要**：地圖、`receive` 改進 |
| 18.0 | 2015 | 2015 **主要**：時間 API、`maps` 操作、`ssl` 改進 |
| 19.0 | 2016 | 2016`try`/`catch`改進、`binary` 改進 |
| 20.0 | 20.0 2017 | 2017 **主要**：`maps` 改進、`ssl` 改進 |
| 21.0 | 21.0 2018 | **主要**：`ssl` 改進、`logger`（取代`error_logger`）|
| 22.0 | 22.0 2019 | 2019 **主要**：發行版改進、`ssl` 改進 |
| 23.0 | 23.0 2020 | **主要**：`maps` 改進、`ssl` 改進 |
| 24.0 | 24.0 2021 | **主要**：`ssl` 改進、`maps` 改進 |
| 25.0 | 25.0 2022 | 2022 **主要**：`ssl` 改進、`maps` 改進 |
| 26.0 | 26.0 2023 | **主要**：`ssl` 改進、`maps` 改進 |
| 27.0 | 27.0 2024 | 2024 **主要**：`ssl` 改進、`maps` 改進 |
## 長生不老藥時間線
|版本 |年份|關鍵主題 |
|--------|------|------------|
| 0.1 | 0.1 2011 |初始版本（José Valim）|
| 0.12 | 0.12 2013 | 1.0 之前的第一個穩定版 |
| 0.13 | 0.13 2014年|`defprotocol`,`defimpl`|
| 0.14 | 0.14 2014年|改進的錯誤訊息 |
| 0.15 | 0.15 2014年| `Stream`、`Enum` 改進 |
| 1.0 | 2014年| **第一個穩定版本** |
| 1.1| 2015 | 2015`with`聲明、`Logger` 改進 |
| 1.2 | 1.2 2016 | 2016`Multi-call`GenServer、`MapSet` |
| 1.3 | 1.3 2016 | 2016`Calendar`類型、`Mix` 改進 |
| 1.4 | 1.4 2017 | 2017 `Registry`、`Supervisor` 改進 |
| 1.5 | 1.5 2017 | 2017`Calendar`改進、`Logger` 改進 |
| 1.6 | 1.6 2018 | **`mix format`**（程式碼格式化程式）、`Registry` 改進 |
| 1.7 | 1.7 2019 | 2019`defstruct`改進、`mix` 改進 |
| 1.8 | 1.8 2019 | 2019`Calendar`改進、`Logger` 改進 |
| 1.9 | 1.9 2019 | 2019 **`mix release`**（獨立版）|
| 1.10 | 1.10 2020 |`Calendar`改進、`Logger` 改進 |
| 1.11 | 1.11 2020 |`defdelegate`改進、`mix` 改進 |
| 1.12 | 1.12 2021 |`struct`改進、`mix` 改進 |
| 1.13 | 1.13 2021 |`mix`改進、`Logger` 改進 |
| 1.14 | 1.14 2022 | 2022`def`改進、`mix` 改進 |
| 1.15 | 1.15 2023 |`mix`改進、`Logger` 改進 |
| 1.16 | 1.16 2024 | 2024`mix`改進、`Logger` 改進 |
| 1.17 | 1.17 2024 | 2024持續發展|
## 主要里程碑
### Erlang：電信語言（1986-2000）
- **1986**：愛立信的 Joe Armstrong、Robert Virding、Mike Williams 創建了 Erlang
- **目標**：建立可靠的電信系統－「讓它崩潰」概念
- **主要特點**：Actor模型、熱代碼交換、分散式計算
- **1998**：開源（R1）－Erlang 進入更廣闊的世界
- **使用者**：愛立信 AXD301 ATM 交換器（99.9999999% 正常運作時間 — “九個九”）
### Erlang/OTP 成熟度 (2000–2013)
- **OTP**（開放電信平台）－框架、函式庫、工具
- **Mnesia** — 分散式資料庫
- **Dialyzer** — 靜態類型分析
- **R16B (2013)**：地圖 — 鍵值資料結構
### Erlang 現代時代（2014 年至今）
- **17.0 (2014)**：地圖 — 主要語言功能
- **18.0 (2015)**：新時間 API、地圖操作
- **21.0 (2018)**：新`logger`（替換`error_logger`）
- **22.0–27.0**：持續改善 SSL、分發、效能
### Elixir：Ruby 社群的 Erlang（2011 年至今）
- **2011**：José Valim 創建 Elixir — 編譯為 Erlang BEAM
- **目標**：Ruby 的生產力 + Erlang 的可靠性
- **主要功能**：元程式設計、管道`|>`、巨集、`mix` 建置工具
- **1.0 (2014)**：第一個穩定版本
- **1.6 (2018)**：`mix format` — 內建程式碼格式化程序
- **1.9 (2019)**：`mix release` — 獨立版本（不需要 Erlang）
## 語法演變
```erlang
%% Erlang R1: Basic Actor model
-module(hello).
-export([start/0, loop/0]).

start() ->
    Pid = spawn(hello, loop, []),
    Pid ! {hello, self()},
    receive
        Response -> io:format("~p~n", [Response])
    end.

loop() ->
    receive
        {hello, From} ->
            From ! {hello_from, node()},
            loop()
    end.

%% Erlang 17+: Maps
Person = #{name => "Alice", age => 30},
Name = maps:get(name, Person),
Person2 = Person#{email => "alice@example.com"}.

%% Erlang: Pattern matching + recursion
factorial(0) -> 1;
factorial(N) -> N * factorial(N - 1).

%% Erlang: List comprehension
[X * 2 || X <- [1, 2, 3, 4, 5], X rem 2 =:= 0].
```

```elixir
# Elixir: Pipe operator
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")

# Elixir: Pattern matching
{:ok, result} = SomeModule.compute()

# Elixir: Macros (metaprogramming)
defmodule MyMacro do
  defmacro say_hello do
    quote do
      IO.puts("Hello!")
    end
  end
end

# Elixir: GenServer (OTP behavior)
defmodule Counter do
  use GenServer

  def start_link(initial), do: GenServer.start_link(__MODULE__, initial)
  def inc(pid), do: GenServer.cast(pid, :inc)
  def get(pid), do: GenServer.call(pid, :get)

  @impl true
  def init(initial), do: {:ok, initial}

  @impl true
  def handle_cast(:inc, count), do: {:noreply, count + 1}

  @impl true
  def handle_call(:get, _from, count), do: {:reply, count, count}
end

# Elixir: Comprehensions
for x <- 1..10, rem(x, 2) == 0, do: x * x

# Elixir: with (error handling)
with {:ok, user} <- find_user(id),
     {:ok, perms} <- check_permissions(user) do
  {:ok, perms}
else
  {:error, reason} -> {:error, reason}
end
```

## 關鍵設計原則
```
Erlang:
1. "Let it crash" — isolate failures, restart processes
2. "Share nothing" — processes communicate via messages only
3. "Hot code swapping" — update code without stopping
4. "Distributed" — built for multi-node systems
5. "Fault-tolerant" — supervisor trees, automatic restart
6. "Nine nines" — 99.9999999% uptime is achievable

Elixir:
7. "Productive" — Ruby-like syntax, pipes, macros
8. "Metaprogramming" — extend the language itself
9. "Tooling" — mix (build), format (style), hex (packages)
10. "Compatible" — runs on Erlang BEAM, uses Erlang libraries
```

## 生態系成長
```
1986: Erlang created at Ericsson (telecom)
1998: Erlang open-sourced (R1)
2000s: Erlang/OTP matures — Mnesia, Dialyzer
2007: RabbitMQ (message broker) — Erlang-based
2011: Elixir created by José Valim
2014: Elixir 1.0 — stable release
2015: Phoenix framework — web development
2018: Elixir 1.6 — mix format
2019: Elixir 1.9 — mix release
2025: Erlang/Elixir power:
       - WhatsApp (Erlang, 2M+ concurrent connections per server)
       - Discord (Elixir, handles millions of users)
       - RabbitMQ, CouchDB, EMQX (Erlang)
       - Phoenix (Elixir web framework)
       - Used by: WhatsApp, Discord, Bleacher Report, Pinterest
```
