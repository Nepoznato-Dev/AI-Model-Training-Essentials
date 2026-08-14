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
# Erlang & Elixir — সংস্করণ ইতিহাস এবং বিবর্তন
## এরলাং টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| Erlang 1 | 1986 | **প্রথম এরলাং** (জো আর্মস্ট্রং, এরিকসন) |
| Erlang 4 | 1991 | প্রথম পাবলিক রিলিজ |
| Erlang 5 (R1) | 1998 | **ওপেন সোর্স** রিলিজ |
| R9B | 2002 | Mnesia ডাটাবেস, উন্নত কর্মক্ষমতা |
| R12B | 2006 | ডায়ালাইজার (টাইপ চেকার) |
| R13B | 2008 | রেকর্ড উন্নতি,`fun`উন্নতি |
| R14B | 2010 | বাইনারি বোধগম্যতা, উন্নত জিসি |
| R15B | 2012 | মানচিত্র (পরীক্ষামূলক) |
| R16B | 2013 | **মানচিত্র** স্থিতিশীল |
| 17.0 | 2014 | **প্রধান**: মানচিত্র,`receive`উন্নতি |
| 18.0 | 2015 | **মেজর**: টাইম API,`maps`অপারেশন,`ssl`উন্নতি |
| 19.0 | 2016 | `try`/`catch`উন্নতি,`binary`উন্নতি |
| 20.0 | 2017 | **প্রধান**:`maps`উন্নতি,`ssl`উন্নতি |
| 21.0 | 2018 | **প্রধান**:`ssl`উন্নতি,`logger`(`error_logger` প্রতিস্থাপন করে) |
| 22.0 | 2019 | **প্রধান**: বিতরণের উন্নতি,`ssl`উন্নতি |
| 23.0 | 2020 | **প্রধান**:`maps`উন্নতি,`ssl`উন্নতি |
| 24.0 | 2021 | **প্রধান**:`ssl`উন্নতি,`maps`উন্নতি |
| 25.0 | 2022 | **প্রধান**:`ssl`উন্নতি,`maps`উন্নতি |
| 26.0 | 2023 | **প্রধান**:`ssl`উন্নতি,`maps`উন্নতি |
| 27.0 | 2024 | **প্রধান**:`ssl`উন্নতি,`maps`উন্নতি |
## এলিক্সির টাইমলাইন
| সংস্করণ | বছর | মূল থিম |
|---------|------|------------|
| 0.1 | 2011 | প্রাথমিক রিলিজ (জোসে ভ্যালিম) |
| 0.12 | 2013 | প্রথম স্থিতিশীল পূর্ব-1.0 |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | উন্নত ত্রুটি বার্তা |
| 0.15 | 2014 | `Stream`,`Enum`উন্নতি |
| 1.0 | 2014 | **প্রথম স্থিতিশীল প্রকাশ** |
| 1.1 | 2015 | `with`বিবৃতি,`Logger`উন্নতি |
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 | `Calendar`প্রকার,`Mix`উন্নতি |
| 1.4 | 2017 | `Registry`,`Supervisor`উন্নতি |
| 1.5 | 2017 | `Calendar`উন্নতি,`Logger`উন্নতি |
| 1.6 | 2018 | **`mix format`** (কোড ফর্ম্যাটার),`Registry`উন্নতি |
| 1.7 | 2019 | `defstruct`উন্নতি,`mix`উন্নতি |
| 1.8 | 2019 | `Calendar`উন্নতি,`Logger`উন্নতি |
| 1.9 | 2019 | **`mix release`** (স্বয়ংসম্পূর্ণ রিলিজ) |
| 1.10 | 2020 | `Calendar`উন্নতি,`Logger`উন্নতি |
| 1.11 | 2020 | `defdelegate`উন্নতি,`mix`উন্নতি |
| 1.12 | 2021 | `struct`উন্নতি,`mix`উন্নতি |
| 1.13 | 2021 | `mix`উন্নতি,`Logger`উন্নতি |
| 1.14 | 2022 | `def`উন্নতি,`mix`উন্নতি |
| 1.15 | 2023 | `mix`উন্নতি,`Logger`উন্নতি |
| 1.16 | 2024 | `mix`উন্নতি,`Logger`উন্নতি |
| 1.17 | 2024 | চলমান উন্নয়ন |
## প্রধান মাইলফলক
### এরল্যাং: টেলিকম ভাষা (1986-2000)
- **1986**: জো আর্মস্ট্রং, রবার্ট ভার্ডিং, এরিকসনের মাইক উইলিয়ামস এরলাং তৈরি করেন
- **লক্ষ্য**: নির্ভরযোগ্য টেলিকম সিস্টেম তৈরি করুন - "এটি বিপর্যস্ত হতে দিন" দর্শন
- **প্রধান বৈশিষ্ট্য**: অভিনেতা মডেল, হট কোড অদলবদল, বিতরণ করা কম্পিউটিং
- **1998**: ওপেন সোর্সড (R1) — এরলাং বিস্তৃত বিশ্বে প্রবেশ করেছে
- **ব্যবহার করেছেন**: এরিকসন AXD301 ATM সুইচ (99.9999999% আপটাইম — "নয় নাইন")
### Erlang/OTP পরিপক্কতা (2000-2013)
- **OTP** (ওপেন টেলিকম প্ল্যাটফর্ম) — ফ্রেমওয়ার্ক, লাইব্রেরি, টুল
- **Mnesia** — বিতরণ করা ডাটাবেস
- **ডায়ালাইজার** — স্ট্যাটিক টাইপ বিশ্লেষণ
- **R16B (2013): মানচিত্র — কী-মান ডেটা স্ট্রাকচার
### এরলাং আধুনিক যুগ (2014-বর্তমান)
- **17.0 (2014): মানচিত্র — প্রধান ভাষা বৈশিষ্ট্য
- **18.0 (2015): নতুন সময় API, মানচিত্র অপারেশন
- **21.0 (2018): নতুন`logger`(`error_logger` প্রতিস্থাপন করে)
- **22.0–27.0**: SSL, ডিস্ট্রিবিউশন, পারফরম্যান্সের ক্রমাগত উন্নতি
### ইলিক্সির: রুবি সম্প্রদায়ের জন্য এরল্যাং (2011-বর্তমান)
- **2011**: জোসে ভ্যালিম এলিক্সির তৈরি করেছেন — এরল্যাং বিম-এ কম্পাইল করেছেন
- **লক্ষ্য**: রুবির উৎপাদনশীলতা + Erlang এর নির্ভরযোগ্যতা
- **প্রধান বৈশিষ্ট্য**: মেটাপ্রোগ্রামিং, পাইপ `|>`, ম্যাক্রো,`mix`বিল্ড টুল
- **1.0 (2014): প্রথম স্থিতিশীল প্রকাশ
- **1.6 (2018):`mix format`— অন্তর্নির্মিত কোড ফর্ম্যাটার
- **1.9 (2019):`mix release`— স্বয়ংসম্পূর্ণ রিলিজ (কোন এরল্যাং প্রয়োজন নেই)
## সিনট্যাক্স বিবর্তন
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

## মূল ডিজাইনের নীতি
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

## ইকোসিস্টেম বৃদ্ধি
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
