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
# Erlang & Elixir — Version History & Evolution

## Erlang Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| Erlang 1 | 1986 | **First Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | First public release |
| Erlang 5 (R1) | 1998 | **Open source** release |
| R9B  | 2002 | Mnesia database, improved performance |
| R12B | 2006 | Dialyzer (type checker) |
| R13B | 2008 | Records improvements, `fun` improvements |
| R14B | 2010 | Binary comprehension, improved GC |
| R15B | 2012 | Maps (experimental) |
| R16B | 2013 | **Maps** stable |
| 17.0 | 2014 | **Major**: Maps, `receive` improvements |
| 18.0 | 2015 | **Major**: Time API, `maps` operations, `ssl` improvements |
| 19.0 | 2016 | `try`/`catch` improvements, `binary` improvements |
| 20.0 | 2017 | **Major**: `maps` improvements, `ssl` improvements |
| 21.0 | 2018 | **Major**: `ssl` improvements, `logger` (replaces `error_logger`) |
| 22.0 | 2019 | **Major**: Distribution improvements, `ssl` improvements |
| 23.0 | 2020 | **Major**: `maps` improvements, `ssl` improvements |
| 24.0 | 2021 | **Major**: `ssl` improvements, `maps` improvements |
| 25.0 | 2022 | **Major**: `ssl` improvements, `maps` improvements |
| 26.0 | 2023 | **Major**: `ssl` improvements, `maps` improvements |
| 27.0 | 2024 | **Major**: `ssl` improvements, `maps` improvements |

## Elixir Timeline

| Version | Year | Key Theme |
|---------|------|-----------|
| 0.1     | 2011 | Initial release (José Valim) |
| 0.12    | 2013 | First stable pre-1.0 |
| 0.13    | 2014 | `defprotocol`, `defimpl` |
| 0.14    | 2014 | Improved error messages |
| 0.15    | 2014 | `Stream`, `Enum` improvements |
| 1.0     | 2014 | **First stable release** |
| 1.1     | 2015 | `with` statement, `Logger` improvements |
| 1.2     | 2016 | `Multi-call` GenServer, `MapSet` |
| 1.3     | 2016 | `Calendar` types, `Mix` improvements |
| 1.4     | 2017 | `Registry`, `Supervisor` improvements |
| 1.5     | 2017 | `Calendar` improvements, `Logger` improvements |
| 1.6     | 2018 | **`mix format`** (code formatter), `Registry` improvements |
| 1.7     | 2019 | `defstruct` improvements, `mix` improvements |
| 1.8     | 2019 | `Calendar` improvements, `Logger` improvements |
| 1.9     | 2019 | **`mix release`** (self-contained releases) |
| 1.10    | 2020 | `Calendar` improvements, `Logger` improvements |
| 1.11    | 2020 | `defdelegate` improvements, `mix` improvements |
| 1.12    | 2021 | `struct` improvements, `mix` improvements |
| 1.13    | 2021 | `mix` improvements, `Logger` improvements |
| 1.14    | 2022 | `def` improvements, `mix` improvements |
| 1.15    | 2023 | `mix` improvements, `Logger` improvements |
| 1.16    | 2024 | `mix` improvements, `Logger` improvements |
| 1.17    | 2024 | Ongoing development |

## Major Milestones

### Erlang: The Telecom Language (1986–2000)
- **1986**: Joe Armstrong, Robert Virding, Mike Williams at Ericsson create Erlang
- **Goal**: Build reliable telecom systems — "let it crash" philosophy
- **Key features**: Actor model, hot code swapping, distributed computing
- **1998**: Open sourced (R1) — Erlang enters the wider world
- **Used by**: Ericsson AXD301 ATM switch (99.9999999% uptime — "nine nines")

### Erlang/OTP Maturity (2000–2013)
- **OTP** (Open Telecom Platform) — frameworks, libraries, tools
- **Mnesia** — distributed database
- **Dialyzer** — static type analysis
- **R16B (2013)**: Maps — key-value data structure

### Erlang Modern Era (2014–present)
- **17.0 (2014)**: Maps — major language feature
- **18.0 (2015)**: New time API, maps operations
- **21.0 (2018)**: New `logger` (replaces `error_logger`)
- **22.0–27.0**: Continuous improvements to SSL, distribution, performance

### Elixir: Erlang for the Ruby Community (2011–present)
- **2011**: José Valim creates Elixir — compiles to Erlang BEAM
- **Goal**: Productivity of Ruby + reliability of Erlang
- **Key features**: Metaprogramming, pipes `|>`, macros, `mix` build tool
- **1.0 (2014)**: First stable release
- **1.6 (2018)**: `mix format` — built-in code formatter
- **1.9 (2019)**: `mix release` — self-contained releases (no Erlang needed)

## Syntax Evolution

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

## Key Design Principles

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

## Ecosystem Growth

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
