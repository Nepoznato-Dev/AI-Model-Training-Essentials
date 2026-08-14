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
# एरलांग और अमृत - संस्करण इतिहास और विकास
## एरलांग टाइमलाइन
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| एरलांग 1 | 1986 | **प्रथम एरलांग** (जो आर्मस्ट्रांग, एरिक्सन) |
| एरलांग 4 | 1991 | पहली सार्वजनिक रिलीज़ |
| एरलांग 5 (आर1) | 1998 | **खुला स्रोत** रिलीज |
| आर9बी | 2002 | मेनेशिया डेटाबेस, बेहतर प्रदर्शन |
| आर12बी | 2006 | डायलाइजर (टाइप चेकर) |
| आर13बी | 2008 | रिकॉर्ड सुधार,`fun`सुधार |
| आर14बी | 2010 | बाइनरी समझ, बेहतर जीसी |
| आर15बी | 2012 | मानचित्र (प्रयोगात्मक) |
| आर16बी | 2013 | **मानचित्र** स्थिर |
| 17.0 | 2014 | **प्रमुख**: मानचित्र,`receive`सुधार |
| 18.0 | 2015 | **प्रमुख**: समय एपीआई,`maps`संचालन,`ssl`सुधार |
| 19.0 | 2016 | `try`/`catch`सुधार,`binary`सुधार |
| 20.0 | 2017 | **प्रमुख**:`maps`सुधार,`ssl`सुधार |
| 21.0 | 2018 | **प्रमुख**:`ssl`सुधार,`logger`(`error_logger` की जगह) |
| 22.0 | 2019 | **प्रमुख**: वितरण सुधार,`ssl`सुधार |
| 23.0 | 2020 | **प्रमुख**:`maps`सुधार,`ssl`सुधार |
| 24.0 | 2021 | **प्रमुख**:`ssl`सुधार,`maps`सुधार |
| 25.0 | 2022 | **प्रमुख**:`ssl`सुधार,`maps`सुधार |
| 26.0 | 2023 | **प्रमुख**:`ssl`सुधार,`maps`सुधार |
| 27.0 | 2024 | **प्रमुख**:`ssl`सुधार,`maps`सुधार |
## अमृत समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| 0.1 | 2011 | आरंभिक रिलीज़ (जोस वालिम) |
| 0.12 | 2013 | प्रथम स्थिर प्री-1.0 |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | बेहतर त्रुटि संदेश |
| 0.15 | 2014 | `Stream`,`Enum`सुधार |
| 1.0 | 2014 | **पहली स्थिर रिलीज़** |
| 1.1 | 2015 | `with`कथन,`Logger`सुधार |
| 1.2 | 2016 | `Multi-call`जेनसर्वर,`MapSet`|
| 1.3 | 2016 | `Calendar`प्रकार,`Mix`सुधार |
| 1.4 | 2017 | `Registry`,`Supervisor`सुधार |
| 1.5 | 2017 | `Calendar`सुधार,`Logger`सुधार |
| 1.6 | 2018 | **`mix format`** (कोड फ़ॉर्मेटर),`Registry`सुधार |
| 1.7 | 2019 | `defstruct`सुधार,`mix`सुधार |
| 1.8 | 2019 | `Calendar`सुधार,`Logger`सुधार |
| 1.9 | 2019 | **`mix release`** (स्वयं निहित रिलीज) |
| 1.10 | 2020 | `Calendar`सुधार,`Logger`सुधार |
| 1.11 | 2020 | `defdelegate`सुधार,`mix`सुधार |
| 1.12 | 2021 | `struct`सुधार,`mix`सुधार |
| 1.13 | 2021 | `mix`सुधार,`Logger`सुधार |
| 1.14 | 2022 | `def`सुधार,`mix`सुधार |
| 1.15 | 2023 | `mix`सुधार,`Logger`सुधार |
| 1.16 | 2024 | `mix`सुधार,`Logger`सुधार |
| 1.17 | 2024 | निरंतर विकास |
## प्रमुख मील के पत्थर
### एरलांग: द टेलीकॉम लैंग्वेज (1986-2000)
- **1986**: एरिक्सन में जो आर्मस्ट्रांग, रॉबर्ट विर्डिंग, माइक विलियम्स ने एर्लैंग का निर्माण किया
- **लक्ष्य**: विश्वसनीय दूरसंचार प्रणाली का निर्माण - "इसे क्रैश होने दें" दर्शन
- **मुख्य विशेषताएं**: अभिनेता मॉडल, हॉट कोड स्वैपिंग, वितरित कंप्यूटिंग
- **1998**: ओपन सोर्स (आर1) - एरलांग व्यापक दुनिया में प्रवेश करता है
- **उपयोगकर्ता**: एरिक्सन AXD301 एटीएम स्विच (99.9999999% अपटाइम - "नाइन नाइन")
### एर्लांग/ओटीपी परिपक्वता (2000-2013)
- **ओटीपी** (ओपन टेलीकॉम प्लेटफॉर्म) - फ्रेमवर्क, लाइब्रेरी, टूल
- **मेनेशिया** — वितरित डेटाबेस
- **डायलाइज़र** - स्थैतिक प्रकार का विश्लेषण
- **आर16बी (2013)**: मानचित्र — कुंजी-मूल्य डेटा संरचना
### एर्लांग आधुनिक युग (2014-वर्तमान)
- **17.0 (2014)**: मानचित्र — प्रमुख भाषा सुविधा
- **18.0 (2015)**: नया समय एपीआई, मानचित्र संचालन
- **21.0 (2018)**: नया`logger`(`error_logger` की जगह)
- **22.0–27.0**: एसएसएल, वितरण, प्रदर्शन में निरंतर सुधार
### अमृत: रूबी समुदाय के लिए एरलांग (2011-वर्तमान)
- **2011**: जोस वालिम ने एलिक्सिर बनाया - एरलांग बीम में संकलित किया
- **लक्ष्य**: रूबी की उत्पादकता + एरलांग की विश्वसनीयता
- **मुख्य विशेषताएं**: मेटाप्रोग्रामिंग, पाइप `|>`, मैक्रोज़,`mix`बिल्ड टूल
- **1.0 (2014)**: पहली स्थिर रिलीज़
- **1.6 (2018)**:`mix format`— अंतर्निहित कोड फ़ॉर्मेटर
- **1.9 (2019)**:`mix release`- स्व-निहित रिलीज़ (कोई एर्लैंग की आवश्यकता नहीं)
## सिंटेक्स इवोल्यूशन
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

## मुख्य डिज़ाइन सिद्धांत
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

## पारिस्थितिकी तंत्र का विकास
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
