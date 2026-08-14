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
# Erlang & Elixir – Versionsgeschichte und Entwicklung
## Erlang-Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| Erlang 1 | 1986 | **First Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Erste öffentliche Veröffentlichung |
| Erlang 5 (R1) | 1998 | **Open Source**-Veröffentlichung |
| R9B | 2002 | Mnesia-Datenbank, verbesserte Leistung |
| R12B | 2006 | Dialysator (Typprüfer) |
| R13B | 2008 | Zeichnet Verbesserungen auf,`fun`Verbesserungen |
| R14B | 2010 | Binärverständnis, verbesserte GC |
| R15B | 2012 | Karten (experimentell) |
| R16B | 2013 | **Karten** stabil |
| 17,0 | 2014 | **Major**: Karten,`receive`Verbesserungen |
| 18,0 | 2015 | **Major**: Zeit-API, `maps`-Operationen, `ssl`-Verbesserungen |
| 19,0 | 2016 | `try`/`catch`Verbesserungen,`binary`Verbesserungen |
| 20,0 | 2017 | **Wichtig**: `maps`-Verbesserungen, `ssl`-Verbesserungen |
| 21,0 | 2018 | **Wichtig**: `ssl`-Verbesserungen,`logger`(ersetzt `error_logger`) |
| 22,0 | 2019 | **Major**: Verteilungsverbesserungen, `ssl`-Verbesserungen |
| 23,0 | 2020 | **Wichtig**: `maps`-Verbesserungen, `ssl`-Verbesserungen |
| 24,0 | 2021 | **Wichtig**: `ssl`-Verbesserungen, `maps`-Verbesserungen |
| 25,0 | 2022 | **Wichtig**: `ssl`-Verbesserungen, `maps`-Verbesserungen |
| 26,0 | 2023 | **Wichtig**: `ssl`-Verbesserungen, `maps`-Verbesserungen |
| 27,0 | 2024 | **Wichtig**: `ssl`-Verbesserungen, `maps`-Verbesserungen |
## Elixier-Zeitleiste
| Version | Jahr | Schlüsselthema |
|---------|------|-----------|
| 0,1 | 2011 | Erstveröffentlichung (José Valim) |
| 0,12 | 2013 | Erste stabile Version vor 1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Verbesserte Fehlermeldungen |
| 0,15 | 2014 | `Stream`,`Enum`Verbesserungen |
| 1,0 | 2014 | **Erste stabile Version** |
| 1.1 | 2015 |  `with`-Anweisung, `Logger`-Verbesserungen |
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1,3 | 2016 |  `Calendar`-Typen, `Mix`-Verbesserungen |
| 1,4 | 2017 | `Registry`,`Supervisor`Verbesserungen |
| 1,5 | 2017 |  `Calendar`-Verbesserungen, `Logger`-Verbesserungen |
| 1,6 | 2018 | **`mix format`** (Codeformatierer),`Registry`Verbesserungen |
| 1,7 | 2019 |  `defstruct`-Verbesserungen, `mix`-Verbesserungen |
| 1,8 | 2019 |  `Calendar`-Verbesserungen, `Logger`-Verbesserungen |
| 1,9 | 2019 | **`mix release`** (eigenständige Veröffentlichungen) |
| 1.10 | 2020 |  `Calendar`-Verbesserungen, `Logger`-Verbesserungen |
| 1.11 | 2020 |  `defdelegate`-Verbesserungen, `mix`-Verbesserungen |
| 1.12 | 2021 |  `struct`-Verbesserungen, `mix`-Verbesserungen |
| 1.13 | 2021 |  `mix`-Verbesserungen, `Logger`-Verbesserungen |
| 1,14 | 2022 |  `def`-Verbesserungen, `mix`-Verbesserungen |
| 1,15 | 2023 |  `mix`-Verbesserungen, `Logger`-Verbesserungen |
| 1,16 | 2024 |  `mix`-Verbesserungen, `Logger`-Verbesserungen |
| 1,17 | 2024 | Kontinuierliche Entwicklung |
## Wichtige Meilensteine
### Erlang: Die Telekommunikationssprache (1986–2000)
- **1986**: Joe Armstrong, Robert Virding und Mike Williams bei Ericsson gründen Erlang
- **Ziel**: Zuverlässige Telekommunikationssysteme aufbauen – „let it crash“-Philosophie
- **Hauptfunktionen**: Akteurmodell, Hot-Code-Austausch, verteiltes Rechnen
- **1998**: Open Source (R1) – Erlang dringt in die weite Welt vor
- **Verwendet von**: Ericsson AXD301 ATM Switch (99,9999999 % Betriebszeit – „nine nines“)
### Erlang/OTP-Reife (2000–2013)
- **OTP** (Open Telecom Platform) – Frameworks, Bibliotheken, Tools
- **Mnesia** – verteilte Datenbank
- **Dialysator** – statische Typanalyse
- **R16B (2013)**: Karten – Schlüsselwert-Datenstruktur
### Erlang Moderne Ära (2014–heute)
- **17.0 (2014)**: Karten – wichtige Sprachfunktion
- **18.0 (2015)**: Neue Zeit-API, Kartenoperationen
- **21.0 (2018)**: Neuer`logger`(ersetzt `error_logger`)
- **22.0–27.0**: Kontinuierliche Verbesserungen an SSL, Verteilung und Leistung
### Elixir: Erlang für die Ruby-Community (2011–heute)
- **2011**: José Valim erstellt Elixir – kompiliert zu Erlang BEAM
- **Ziel**: Produktivität von Ruby + Zuverlässigkeit von Erlang
- **Hauptfunktionen**: Metaprogrammierung, Pipes `|>`, Makros,`mix`Build-Tool
- **1.0 (2014)**: Erste stabile Version
- **1.6 (2018)**:`mix format`– integrierter Codeformatierer
- **1.9 (2019)**:`mix release`– eigenständige Veröffentlichungen (kein Erlang erforderlich)
## Syntaxentwicklung
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

## Wichtige Designprinzipien
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

## Ökosystemwachstum
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
