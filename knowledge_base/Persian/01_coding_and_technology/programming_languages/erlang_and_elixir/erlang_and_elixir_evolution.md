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
# Erlang & Elixir - تاریخچه نسخه و تکامل
## جدول زمانی Erlang
| نسخه | سال | تم کلید |
|---------|------|-----------|
| Erlang 1 | 1986 | **اولین ارلنگ** (جو آرمسترانگ، اریکسون) |
| Erlang 4 | 1991 | اولین انتشار عمومی |
| Erlang 5 (R1) | 1998 | **متن باز** انتشار |
| R9B | 2002 | پایگاه داده منزیا، بهبود عملکرد |
| R12B | 2006 | دیالیز (چکگر تایپ) |
| R13B | 2008 | بهبود رکوردها، بهبودهای`fun`|
| R14B | 2010 | درک باینری، GC بهبود یافته |
| R15B | 2012 | نقشه ها (تجربی) |
| R16B | 2013 | **نقشه** پایدار |
| 17.0 | 2014 | **عمده**: نقشه ها، بهبودهای`receive`|
| 18.0 | 2015 | **عمده**: Time API، عملیات `maps`، بهبودهای`ssl`|
| 19.0 | 2016 |  بهبودهای`try`/ `catch`، بهبودهای`binary`|
| 20.0 | 2017 | **عمده**: بهبودهای `maps`، بهبودهای`ssl`|
| 21.0 | 2018 | **عمده**: بهبودهای `ssl`،`logger`(جایگزین`error_logger`) |
| 22.0 | 2019 | **عمده**: بهبودهای توزیع، بهبودهای`ssl`|
| 23.0 | 2020 | **عمده**: بهبودهای `maps`، بهبودهای`ssl`|
| 24.0 | 2021 | **عمده**: بهبودهای `ssl`، بهبودهای`maps`|
| 25.0 | 2022 | **عمده**: بهبودهای `ssl`، بهبودهای`maps`|
| 26.0 | 2023 | **عمده**: بهبودهای `ssl`، بهبودهای`maps`|
| 27.0 | 2024 | **عمده**: بهبودهای `ssl`، بهبودهای`maps`|
## جدول زمانی اکسیر
| نسخه | سال | تم کلید |
|---------|------|-----------|
| 0.1 | 2011 | انتشار اولیه (José Valim) |
| 0.12 | 2013 | اولین پایدار قبل از 1.0 |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | پیام های خطای بهبود یافته |
| 0.15 | 2014 |  بهبودهای `Stream`،`Enum`|
| 1.0 | 2014 | **اولین انتشار پایدار** |
| 1.1 | 2015 |  بیانیه `with`، بهبودهای`Logger`|
| 1.2 | 2016 | `Multi-call`GenServer،`MapSet`|
| 1.3 | 2016 |  انواع `Calendar`، بهبودهای`Mix`|
| 1.4 | 2017 |  بهبودهای `Registry`،`Supervisor`|
| 1.5 | 2017 |  بهبودهای `Calendar`، بهبودهای`Logger`|
| 1.6 | 2018 | **`mix format`** (فرمت ساز کد)، بهبود`Registry`|
| 1.7 | 2019 |  بهبودهای `defstruct`، بهبودهای`mix`|
| 1.8 | 2019 |  بهبودهای `Calendar`، بهبودهای`Logger`|
| 1.9 | 2019 | **`mix release`** (نسخه های مستقل) |
| 1.10 | 2020 |  بهبودهای `Calendar`، بهبودهای`Logger`|
| 1.11 | 2020 |  بهبودهای `defdelegate`، بهبودهای`mix`|
| 1.12 | 2021 |  بهبودهای `struct`، بهبودهای`mix`|
| 1.13 | 2021 |  بهبودهای `mix`، بهبودهای`Logger`|
| 1.14 | 2022 |  بهبودهای `def`، بهبودهای`mix`|
| 1.15 | 2023 |  بهبودهای `mix`، بهبودهای`Logger`|
| 1.16 | 2024 |  بهبودهای `mix`، بهبودهای`Logger`|
| 1.17 | 2024 | توسعه در حال انجام |
## نقاط عطف اصلی
### Erlang: The Telecom Language (1986–2000)
- **1986**: جو آرمسترانگ، رابرت ویردینگ، مایک ویلیامز در اریکسون ارلنگ را ایجاد کردند.
- **هدف**: سیستم های مخابراتی قابل اعتماد بسازید - فلسفه "بگذارید خراب شود".
- **ویژگی های کلیدی**: مدل بازیگر، مبادله کد داغ، محاسبات توزیع شده
- **1998**: منبع باز (R1) - Erlang وارد دنیای گسترده تر می شود
- **استفاده شده توسط**: سوئیچ ATM Ericsson AXD301 (99.9999999% uptime — "nine nines")
### سررسید Erlang/OTP (2000–2013)
- **OTP** (پلتفرم مخابراتی باز) - چارچوب ها، کتابخانه ها، ابزارها
- **Mnesia** - پایگاه داده توزیع شده
- ** دیالیزور ** - آنالیز نوع استاتیک
- **R16B (2013)**: نقشه ها - ساختار داده کلید-مقدار
### عصر مدرن Erlang (2014–اکنون)
- **17.0 (2014)**: نقشه ها - ویژگی اصلی زبان
- **18.0 (2015)**: API زمان جدید، عملیات نقشه ها
- **21.0 (2018)**:`logger`جدید (جایگزین `error_logger`)
- **22.0–27.0**: بهبود مستمر در SSL، توزیع، عملکرد
### اکسیر: Erlang برای جامعه روبی (2011–اکنون)
- **2011**: خوزه والیم اکسیر را ایجاد می کند — کامپایل به Erlang BEAM
- **هدف**: بهره وری روبی + قابلیت اطمینان ارلنگ
- **ویژگی های کلیدی**: فرابرنامه ریزی، لوله های `|>`، ماکروها، ابزار ساخت `mix`
- **1.0 (2014)**: اولین نسخه پایدار
- **1.6 (2018)**:`mix format`- قالب‌کننده کد داخلی
- **1.9 (2019)**:`mix release`- نسخه های مستقل (بدون نیاز به Erlang)
## تکامل نحو
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

## اصول کلیدی طراحی
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

## رشد اکوسیستم
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
