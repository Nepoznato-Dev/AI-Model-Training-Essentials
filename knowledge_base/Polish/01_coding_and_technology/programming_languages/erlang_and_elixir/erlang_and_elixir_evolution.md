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

# Erlang & Elixir — Historia wersji i ewolucja
## Erlang Oś czasu
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| Erlang 1 | 1986 | **Pierwszy Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Pierwsze publiczne wydanie |
| Erlang 5 (R1) | 1998 | **Wydanie open source** |
| R9B | 2002 | Baza danych Mnesia, poprawiona wydajność |
| R12B | 2006 | Dializer (sprawdzanie typu) |
| R13B | 2008 | Ulepszenia rekordów, ulepszenia`fun`|
| R14B | 2010 | Rozumienie binarne, ulepszone GC |
| R15B | 2012 | Mapy (eksperymentalne) |
| R16B | 2013 | **Mapy** stabilne |
| 17,0 | 2014 | **Główne**: Mapy, ulepszenia`receive`|
| 18,0 | 2015 | **Główne**: Time API, operacje `maps`, ulepszenia`ssl`|
| 19,0 | 2016 |  Ulepszenia`try`/ `catch`, ulepszenia`binary`|
| 20,0 | 2017 | **Główne**: ulepszenia `maps`, ulepszenia`ssl`|
| 21,0 | 2018 | **Główne**: ulepszenia `ssl`,`logger`(zastępuje`error_logger`) |
| 22,0 | 2019 | **Główne**: Ulepszenia dystrybucji, ulepszenia`ssl`|
| 23,0 | 2020 | **Główne**: ulepszenia `maps`, ulepszenia`ssl`|
| 24,0 | 2021 | **Główne**: ulepszenia `ssl`, ulepszenia`maps`|
| 25,0 | 2022 | **Główne**: ulepszenia `ssl`, ulepszenia`maps`|
| 26,0 | 2023 | **Główne**: ulepszenia `ssl`, ulepszenia`maps`|
| 27,0 | 2024 | **Główne**: ulepszenia `ssl`, ulepszenia`maps`|
## Oś czasu eliksiru
| Wersja | Rok | Kluczowy motyw |
|--------|------|-----------|
| 0,1 | 2011 | Pierwsze wydanie (José Valim) |
| 0,12 | 2013 | Pierwsza stabilna wersja sprzed wersji 1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Ulepszone komunikaty o błędach |
| 0,15 | 2014 |  Ulepszenia`Stream`,`Enum`|
| 1,0 | 2014 | **Pierwsza stabilna wersja** |
| 1.1 | 2015 |  Oświadczenie `with`, ulepszenia`Logger`|
| 1.2 | 2016 |  Serwer Generacji `Multi-call`,`MapSet`|
| 1.3 | 2016 |  Typy `Calendar`, ulepszenia`Mix`|
| 1,4 | 2017 |  Ulepszenia`Registry`,`Supervisor`|
| 1,5 | 2017 |  Ulepszenia `Calendar`, ulepszenia`Logger`|
| 1,6 | 2018 | **`mix format`** (formatowanie kodu), ulepszenia`Registry`|
| 1,7 | 2019 |  Ulepszenia `defstruct`, ulepszenia`mix`|
| 1,8 | 2019 |  Ulepszenia `Calendar`, ulepszenia`Logger`|
| 1,9 | 2019 | **`mix release`** (samodzielne wydania) |
| 1.10 | 2020 |  Ulepszenia `Calendar`, ulepszenia`Logger`|
| 1.11 | 2020 |  Ulepszenia `defdelegate`, ulepszenia`mix`|
| 1.12 | 2021 |  Ulepszenia `struct`, ulepszenia`mix`|
| 1.13 | 2021 |  Ulepszenia `mix`, ulepszenia`Logger`|
| 1.14 | 2022 |  Ulepszenia `def`, ulepszenia`mix`|
| 1,15 | 2023 |  Ulepszenia `mix`, ulepszenia`Logger`|
| 1.16 | 2024 |  Ulepszenia `mix`, ulepszenia`Logger`|
| 1,17 | 2024 | Ciągły rozwój |
## Główne kamienie milowe
### Erlang: Język telekomunikacyjny (1986–2000)
- **1986**: Joe Armstrong, Robert Virding, Mike Williams z firmy Ericsson tworzą Erlang
- **Cel**: Budowa niezawodnych systemów telekomunikacyjnych — filozofia „niech się zawiesi”.
- **Kluczowe cechy**: Model aktora, wymiana gorącego kodu, przetwarzanie rozproszone
- **1998**: Open source (R1) — Erlang wkracza w szerszy świat
- **Używany przez**: Przełącznik ATM Ericsson AXD301 (czas sprawności 99,9999999% — „dziewięć dziewiątek”)
### Dojrzałość Erlang/OTP (2000–2013)
- **OTP** (Open Telecom Platform) — frameworki, biblioteki, narzędzia
- **Mnesia** — rozproszona baza danych
- **Dializer** — analiza typu statycznego
- **R16B (2013)**: Mapy — struktura danych klucz-wartość
### Erlang Erlang Nowożytny (2014 – obecnie)
- **17,0 (2014)**: Mapy — główna funkcja językowa
- **18.0 (2015)**: Nowe API czasu, operacje na mapach
- **21.0 (2018)**: Nowy`logger`(zastępuje `error_logger`)
- **22,0–27,0**: Ciągłe ulepszenia protokołu SSL, dystrybucji i wydajności
### Elixir: Erlang dla społeczności Ruby (2011 – obecnie)
- **2011**: José Valim tworzy Elixir — kompiluje do Erlang BEAM
- **Cel**: Produktywność Ruby + niezawodność Erlanga
- **Kluczowe funkcje**: Metaprogramowanie, potoki `|>`, makra, narzędzie do kompilacji `mix`
- **1.0 (2014)**: Pierwsza stabilna wersja
- **1.6 (2018)**:`mix format`— wbudowany formater kodu
- **1.9 (2019)**:`mix release`— wydania samodzielne (nie wymaga Erlanga)
## Ewolucja składni
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

## Kluczowe zasady projektowania
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

## Rozwój ekosystemu
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
