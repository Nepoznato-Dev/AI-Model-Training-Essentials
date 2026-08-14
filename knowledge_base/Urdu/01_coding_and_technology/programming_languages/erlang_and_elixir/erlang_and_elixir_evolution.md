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
# ایرلنگ اور ایلیکسیر - ورژن کی تاریخ اور ارتقاء
## ایرلنگ ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| ایرلنگ 1 | 1986 | **پہلا ایرلنگ** (جو آرمسٹرانگ، ایرکسن) |
| ایرلنگ 4 | 1991 | پہلی عوامی ریلیز |
| Erlang 5 (R1) | 1998 | **اوپن سورس** ریلیز |
| R9B | 2002 | Mnesia ڈیٹا بیس، بہتر کارکردگی |
| R12B | 2006 | ڈائلائزر (ٹائپ چیکر) |
| R13B | 2008 | ریکارڈ میں بہتری،`fun`بہتری |
| R14B | 2010 | بائنری فہم، بہتر GC |
| R15B | 2012 | نقشے (تجرباتی) |
| R16B | 2013 | **نقشے** مستحکم |
| 17.0 | 2014 | **بڑا**: نقشے،`receive`بہتری |
| 18.0 | 2015 | **بڑا**: ٹائم API،`maps`آپریشنز،`ssl`بہتری |
| 19.0 | 2016 | `try`/`catch`بہتری،`binary`بہتری |
| 20.0 | 2017 | **بڑا**:`maps`بہتری،`ssl`بہتری |
| 21.0 | 2018 | **بڑا**:`ssl`بہتری،`logger`(`error_logger` کی جگہ لے لیتا ہے) |
| 22.0 | 2019 | **بڑا**: تقسیم میں بہتری،`ssl`بہتری |
| 23.0 | 2020 | **بڑا**:`maps`بہتری،`ssl`بہتری |
| 24.0 | 2021 | **بڑا**:`ssl`بہتری،`maps`بہتری |
| 25.0 | 2022 | **بڑا**:`ssl`بہتری،`maps`بہتری |
| 26.0 | 2023 | **بڑا**:`ssl`بہتری،`maps`بہتری |
| 27.0 | 2024 | **بڑا**:`ssl`بہتری،`maps`بہتری |
## ایلیکسیر ٹائم لائن
| ورژن | سال | کلیدی تھیم |
|---------|------|------------|
| 0.1 | 2011 | ابتدائی ریلیز (جوس ویلیم) |
| 0.12 | 2013 | پہلا مستحکم پری 1.0 |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | خرابی کے بہتر پیغامات |
| 0.15 | 2014 | `Stream`,`Enum`بہتری |
| 1.0 | 2014 | **پہلی مستحکم ریلیز** |
| 1.1 | 2015 | `with`بیان،`Logger`بہتری |
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 | `Calendar`اقسام،`Mix`بہتری |
| 1.4 | 2017 | `Registry`,`Supervisor`بہتری |
| 1.5 | 2017 | `Calendar`بہتری،`Logger`بہتری |
| 1.6 | 2018 | **`mix format`** (کوڈ فارمیٹر)،`Registry`بہتری |
| 1.7 | 2019 | `defstruct`بہتری،`mix`بہتری |
| 1.8 | 2019 | `Calendar`بہتری،`Logger`بہتری |
| 1.9 | 2019 | **`mix release`** (خود پر مشتمل ریلیز) |
| 1.10 | 2020 | `Calendar`بہتری،`Logger`بہتری |
| 1.11 | 2020 | `defdelegate`بہتری،`mix`بہتری |
| 1.12 | 2021 | `struct`بہتری،`mix`بہتری |
| 1.13 | 2021 | `mix`بہتری،`Logger`بہتری |
| 1.14 | 2022 | `def`بہتری،`mix`بہتری |
| 1.15 | 2023 | `mix`بہتری،`Logger`بہتری |
| 1.16 | 2024 | `mix`بہتری،`Logger`بہتری |
| 1.17 | 2024 | جاری ترقی |
## اہم سنگ میل
### ایرلنگ: دی ٹیلی کام لینگویج (1986–2000)
- **1986**: ایرکسن میں جو آرمسٹرانگ، رابرٹ ورڈنگ، مائیک ولیمز نے ایرلنگ تخلیق کیا۔
- **مقصد**: قابل اعتماد ٹیلی کام سسٹم بنائیں - "اسے کریش ہونے دو" فلسفہ
- **اہم خصوصیات**: اداکار ماڈل، ہاٹ کوڈ کی تبدیلی، تقسیم شدہ کمپیوٹنگ
- **1998**: اوپن سورس (R1) - ایرلنگ وسیع دنیا میں داخل ہوا۔
- **استعمال شدہ **: Ericsson AXD301 ATM سوئچ (99.9999999% اپ ٹائم - "نائن نائنز")
### Erlang/OTP پختگی (2000–2013)
- **OTP** (اوپن ٹیلی کام پلیٹ فارم) — فریم ورک، لائبریریاں، ٹولز
- **Mnesia** — تقسیم شدہ ڈیٹا بیس
- **ڈائلائزر** - جامد قسم کا تجزیہ
- **R16B (2013)**: Maps — کلیدی قدر ڈیٹا کا ڈھانچہ
### ایرلنگ جدید دور (2014–موجودہ)
- **17.0 (2014): Maps — اہم زبان کی خصوصیت
- **18.0 (2015): نیو ٹائم API، نقشہ جات کے آپریشنز
- **21.0 (2018)**: نیا`logger`(`error_logger` کی جگہ لے لیتا ہے)
- **22.0–27.0**: SSL، تقسیم، کارکردگی میں مسلسل بہتری
### ایلیکسیر: ایرلنگ فار دی روبی کمیونٹی (2011–موجودہ)
- **2011**: جوس ویلیم نے ایلیکسیر تخلیق کیا - ایرلنگ بیم کو مرتب کیا
- **مقصد**: روبی کی پیداواریت + ایرلنگ کی وشوسنییتا
- **اہم خصوصیات**: میٹاپروگرامنگ، پائپس `|>`، میکروز،`mix`تعمیر کا آلہ
- **1.0 (2014): پہلی مستحکم ریلیز
- **1.6 (2018)**:`mix format`— بلٹ ان کوڈ فارمیٹر
- **1.9 (2019)**:`mix release`— خود ساختہ ریلیزز (کوئی ایرلنگ کی ضرورت نہیں)
## نحوی ارتقاء
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

## ڈیزائن کے کلیدی اصول
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

## ماحولیاتی نظام کی نمو
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
