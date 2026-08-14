---
# Metadata
title: "Erlang & Elixir — Version History & Evolution"
description: "Comprehensive version history and evolution of Erlang and Elixir from 1986 to modern."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Erlang & Elixir — История версий и эволюция
## Временная шкала Эрланга
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| Эрланг 1 | 1986 | **Первый Эрланг** (Джо Армстронг, Ericsson) |
| Эрланг 4 | 1991 | Первый публичный релиз |
| Эрланг 5 (R1) | 1998 | **Релиз с открытым исходным кодом** |
| Р9Б | 2002 | База данных Mnesia, улучшенная производительность |
| Р12Б | 2006 | Диализатор (проверка типа) |
| Р13Б | 2008 | Улучшения записей, улучшения`fun`|
| Р14Б | 2010 | Двоичное понимание, улучшенный GC |
| Р15Б | 2012 | Карты (экспериментальные) |
| Р16Б | 2013 | **Карты** стабильно |
| 17,0 | 2014 | **Основное**: Карты, улучшения`receive`|
| 18,0 | 2015 | **Основное**: API времени, операции `maps`, улучшения`ssl`|
| 19,0 | 2016 |  Улучшения`try`/ `catch`, улучшения`binary`|
| 20,0 | 2017 | **Основное**: улучшения `maps`, улучшения`ssl`|
| 21,0 | 2018 | **Основное**: улучшения `ssl`,`logger`(заменяет`error_logger`) |
| 22,0 | 2019 | **Основное**: улучшения распространения, улучшения`ssl`|
| 23,0 | 2020 | **Основное**: улучшения `maps`, улучшения`ssl`|
| 24,0 | 2021 | **Основное**: улучшения `ssl`, улучшения`maps`|
| 25,0 | 2022 | **Основное**: улучшения `ssl`, улучшения`maps`|
| 26,0 | 2023 | **Основное**: улучшения `ssl`, улучшения`maps`|
| 27,0 | 2024 | **Основное**: улучшения `ssl`, улучшения`maps`|
## Временная шкала эликсира
| Версия | Год | Ключевая тема |
|---------|------|-----------|
| 0,1 | 2011 | Первоначальный выпуск (Хосе Валим) |
| 0,12 | 2013 | Первая стабильная версия до 1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Улучшенные сообщения об ошибках |
| 0,15 | 2014 |  Улучшения `Stream`,`Enum`|
| 1.0 | 2014 | **Первая стабильная версия** |
| 1.1 | 2015 |  Заявление `with`, улучшения`Logger`|
| 1,2 | 2016 | `Multi-call`ГенСервер,`MapSet`|
| 1,3 | 2016 |  Типы `Calendar`, улучшения`Mix`|
| 1,4 | 2017 |  Улучшения `Registry`,`Supervisor`|
| 1,5 | 2017 |  Улучшения `Calendar`, улучшения`Logger`|
| 1,6 | 2018 | **`mix format`** (форматер кода), улучшения`Registry`|
| 1,7 | 2019 |  Улучшения `defstruct`, улучшения`mix`|
| 1,8 | 2019 |  Улучшения `Calendar`, улучшения`Logger`|
| 1,9 | 2019 | **`mix release`** (автономные выпуски) |
| 1.10 | 2020 |  Улучшения `Calendar`, улучшения`Logger`|
| 1.11 | 2020 |  Улучшения `defdelegate`, улучшения`mix`|
| 1.12 | 2021 |  Улучшения `struct`, улучшения`mix`|
| 1.13 | 2021 |  Улучшения `mix`, улучшения`Logger`|
| 1.14 | 2022 |  Улучшения `def`, улучшения`mix`|
| 1,15 | 2023 |  Улучшения `mix`, улучшения`Logger`|
| 1.16 | 2024 |  Улучшения `mix`, улучшения`Logger`|
| 1.17 | 2024 | Постоянное развитие |
## Основные вехи
### Эрланг: язык телекоммуникаций (1986–2000)
- **1986**: Джо Армстронг, Роберт Вирдинг и Майк Уильямс из Ericsson создают Erlang.
- **Цель**: создать надежные телекоммуникационные системы — философия «пусть выйдет из строя».
- **Основные функции**: модель актеров, горячая замена кода, распределенные вычисления.
- **1998**: Открытый исходный код (R1) — Erlang выходит в более широкий мир.
- **Используется**: банкоматный коммутатор Ericsson AXD301 (время безотказной работы 99,9999999% — «девять девяток»)
### Зрелость Erlang/OTP (2000–2013 гг.)
- **OTP** (Открытая телекоммуникационная платформа) — фреймворки, библиотеки, инструменты.
- **Мнезия** — распределенная база данных
- **Диализатор** — анализ статического типа.
- **R16B (2013 г.)**: Карты — структура данных «ключ-значение».
### Эрланг Современная Эра (2014 – настоящее время)
- **17.0 (2014 г.)**: Карты — основная языковая функция.
- **18.0 (2015 г.)**: Новый API времени, операции с картами.
- **21.0 (2018 г.)**: новый`logger`(заменяет`error_logger`)
- **22.0–27.0**: Постоянное улучшение SSL, распространения и производительности.
### Эликсир: Erlang для сообщества Ruby (2011 – настоящее время)
- **2011**: Хосе Валим создает Elixir — компилируется в Erlang BEAM.
- **Цель**: Производительность Ruby + надежность Erlang.
- **Основные функции**: метапрограммирование, каналы `|>`, макросы, инструмент сборки `mix`.
- **1.0 (2014 г.)**: первый стабильный выпуск.
- **1.6 (2018)**:`mix format`— встроенный форматировщик кода.
- **1.9 (2019)**:`mix release`— автономные выпуски (эрланг не требуется)
## Эволюция синтаксиса
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

## Ключевые принципы проектирования
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

## Рост экосистемы
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
