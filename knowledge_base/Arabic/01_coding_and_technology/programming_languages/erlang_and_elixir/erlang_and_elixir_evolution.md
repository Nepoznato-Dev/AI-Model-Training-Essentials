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
# Erlang & Elixir — تاريخ الإصدار وتطوره
## الجدول الزمني إيرلانج
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| إرلانج 1 | 1986 | **فيرست إيرلانج** (جو أرمسترونج، إريكسون) |
| إرلانج 4 | 1991 | الإصدار العام الأول |
| إرلانج 5 (R1) | 1998 | **مفتوح المصدر** الإصدار |
| R9B | 2002 | قاعدة بيانات Mnesia، تحسين الأداء |
| R12B | 2006 | جهاز غسيل الكلى (مدقق النوع) |
| R13B | 2008 | تحسينات السجلات، تحسينات`fun`|
| R14B | 2010 | الفهم الثنائي، تحسين GC |
| R15B | 2012 | خرائط (تجريبية) |
| R16B | 2013 | **الخرائط** مستقرة |
| 17.0 | 2014 | **الرئيسي**: الخرائط، تحسينات`receive`|
| 18.0 | 2015 | **التخصص**: Time API وعمليات`maps`وتحسينات`ssl`|
| 19.0 | 2016 |  تحسينات`try`/ `catch`، تحسينات`binary`|
| 20.0 | 2017 | **الرئيسية**: تحسينات `maps`، تحسينات`ssl`|
| 21.0 | 2018 | **الرئيسية**: تحسينات `ssl`،`logger`(يحل محل `error_logger`) |
| 22.0 | 2019 | **الرئيسية**: تحسينات التوزيع، تحسينات`ssl`|
| 23.0 | 2020 | **الرئيسية**: تحسينات `maps`، تحسينات`ssl`|
| 24.0 | 2021 | **الرئيسية**: تحسينات `ssl`، تحسينات`maps`|
| 25.0 | 2022 | **الرئيسية**: تحسينات `ssl`، تحسينات`maps`|
| 26.0 | 2023 | **الرئيسية**: تحسينات `ssl`، تحسينات`maps`|
| 27.0 | 2024 | **الرئيسية**: تحسينات `ssl`، تحسينات`maps`|
## الجدول الزمني إكسير
| النسخة | سنة | الموضوع الرئيسي |
|---------|------|-----------|
| 0.1 | 2011 | الإصدار الأولي (خوسيه فاليم) |
| 0.12 | 2013 | أول مستقر قبل 1.0 |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | تحسين رسائل الخطأ |
| 0.15 | 2014 |  تحسينات`Stream`,`Enum`|
| 1.0 | 2014 | **الإصدار المستقر الأول** |
| 1.1 | 2015 |  بيان `with`، تحسينات`Logger`|
| 1.2 | 2016 | `Multi-call`جينسيرفر،`MapSet`|
| 1.3 | 2016 |  أنواع `Calendar`، تحسينات`Mix`|
| 1.4 | 2017 |  تحسينات`Registry`و`Supervisor` |
| 1.5 | 2017 |  تحسينات `Calendar`، تحسينات`Logger`|
| 1.6 | 2018 | **`mix format`** (منسق الكود)، تحسينات`Registry`|
| 1.7 | 2019 |  تحسينات `defstruct`، تحسينات`mix`|
| 1.8 | 2019 |  تحسينات `Calendar`، تحسينات`Logger`|
| 1.9 | 2019 | **`mix release`** (إصدارات قائمة بذاتها) |
| 1.10 | 2020 |  تحسينات `Calendar`، تحسينات`Logger`|
| 1.11 | 2020 |  تحسينات `defdelegate`، تحسينات`mix`|
| 1.12 | 2021 |  تحسينات `struct`، تحسينات`mix`|
| 1.13 | 2021 |  تحسينات `mix`، تحسينات`Logger`|
| 1.14 | 2022 |  تحسينات `def`، تحسينات`mix`|
| 1.15 | 2023 |  تحسينات `mix`، تحسينات`Logger`|
| 1.16 | 2024 |  تحسينات `mix`، تحسينات`Logger`|
| 1.17 | 2024 | التطوير المستمر |
## المعالم الرئيسية
### إيرلانج: لغة الاتصالات (1986-2000)
- **1986**: أنشأ جو أرمسترونج وروبرت فيردينج ومايك ويليامز في إريكسون شركة إرلانج
- **الهدف**: بناء أنظمة اتصالات موثوقة — فلسفة "دعها تتعطل".
- **الميزات الرئيسية**: نموذج الممثل، وتبديل التعليمات البرمجية السريعة، والحوسبة الموزعة
- **1998**: مفتوح المصدر (R1) — يدخل Erlang إلى العالم الأوسع
- **المستخدم بواسطة**: محول الصراف الآلي من Ericsson AXD301 (وقت تشغيل بنسبة 99.9999999% - "تسع تسعات")
### استحقاق إيرلانج/OTP (2000-2013)
- **OTP** (منصة الاتصالات المفتوحة) — الأطر والمكتبات والأدوات
- **Mnesia** — قاعدة بيانات موزعة
- **جهاز غسيل الكلى** — تحليل النوع الثابت
- **R16B (2013)**: الخرائط — بنية بيانات القيمة الرئيسية
### عصر إرلانج الحديث (2014 إلى الوقت الحاضر)
- **17.0 (2014)**: الخرائط — ميزة اللغة الرئيسية
- **18.0 (2015)**: واجهة برمجة التطبيقات للوقت الجديد، وعمليات الخرائط
- **21.0 (2018)**:`logger`الجديد (يحل محل `error_logger`)
- **22.0–27.0**: تحسينات مستمرة لطبقة المقابس الآمنة (SSL) والتوزيع والأداء
### الإكسير: إرلانج لمجتمع روبي (2011 إلى الوقت الحاضر)
- **2011**: قام خوسيه فاليم بإنشاء Elixir - وتم تجميعه إلى Erlang BEAM
- **الهدف**: إنتاجية روبي + موثوقية إرلانج
- **الميزات الرئيسية**: البرمجة الفوقية، والأنابيب `|>`، ووحدات الماكرو، وأداة بناء `mix`
- **1.0 (2014)**: أول إصدار مستقر
- **1.6 (2018)**:`mix format`— منسق التعليمات البرمجية المدمج
- **1.9 (2019)**:`mix release`— إصدارات قائمة بذاتها (لا حاجة إلى Erlang)
## تطور بناء الجملة
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

## مبادئ التصميم الرئيسية
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

## نمو النظام البيئي
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
