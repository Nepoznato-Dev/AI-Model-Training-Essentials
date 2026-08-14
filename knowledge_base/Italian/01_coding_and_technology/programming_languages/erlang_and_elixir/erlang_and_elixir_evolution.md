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
# Erlang & Elixir - Storia ed evoluzione delle versioni
## Cronologia di Erlang
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| Erlang 1 | 1986 | **Primo Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Prima uscita pubblica |
| Erlang 5 (R1) | 1998 | Versione **Open source** |
| R9B | 2002| Database Mnesia, prestazioni migliorate |
| R12B| 2006| Dializzatore (controllo del tipo) |
| R13B | 2008| Miglioramenti ai record, miglioramenti`fun`|
| R14B| 2010| Comprensione binaria, GC migliorato |
| R15B| 2012| Mappe (sperimentali) |
| R16B| 2013| **Mappe** stabile |
| 17.0| 2014| **Maggiore**: Mappe, miglioramenti`receive`|
| 18.0| 2015| **Principale**: API Time, operazioni `maps`, miglioramenti`ssl`|
| 19.0| 2016|  Miglioramenti`try`/ `catch`, miglioramenti`binary`|
| 20.0| 2017 | **Principale**: miglioramenti `maps`, miglioramenti`ssl`|
| 21.0| 2018 | **Maggiore**: miglioramenti `ssl`,`logger`(sostituisce`error_logger`) |
| 22.0| 2019 | **Principale**: miglioramenti alla distribuzione, miglioramenti a`ssl`|
| 23.0| 2020 | **Principale**: miglioramenti `maps`, miglioramenti`ssl`|
| 24.0| 2021 | **Principale**: miglioramenti `ssl`, miglioramenti`maps`|
| 25.0| 2022 | **Principale**: miglioramenti `ssl`, miglioramenti`maps`|
| 26.0| 2023 | **Principale**: miglioramenti `ssl`, miglioramenti`maps`|
| 27.0| 2024 | **Principale**: miglioramenti `ssl`, miglioramenti`maps`|
## Cronologia dell'elisir
| Versione | Anno | Tema chiave |
|---------|------|-----------|
| 0,1 | 2011 | Versione iniziale (José Valim) |
| 0,12 | 2013| Primo pre-1.0 stabile |
| 0,13 | 2014| `defprotocol`,`defimpl`|
| 0,14 | 2014| Messaggi di errore migliorati |
| 0,15| 2014| `Stream`,`Enum`miglioramenti |
| 1.0 | 2014| **Prima versione stabile** |
| 1.1 | 2015|  Dichiarazione `with`, miglioramenti`Logger`|
| 1.2 | 2016| `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016|  Tipi `Calendar`, miglioramenti`Mix`|
| 1.4 | 2017 | `Registry`,`Supervisor`miglioramenti |
| 1,5 | 2017 |  Miglioramenti `Calendar`, miglioramenti`Logger`|
| 1.6 | 2018 | **`mix format`** (formattatore codice), miglioramenti`Registry`|
| 1.7 | 2019 |  Miglioramenti `defstruct`, miglioramenti`mix`|
| 1.8 | 2019 |  Miglioramenti `Calendar`, miglioramenti`Logger`|
| 1.9 | 2019 | **`mix release`** (versioni autonome) |
| 1.10| 2020 |  Miglioramenti `Calendar`, miglioramenti`Logger`|
| 1.11 | 2020 |  Miglioramenti `defdelegate`, miglioramenti`mix`|
| 1.12 | 2021 |  Miglioramenti `struct`, miglioramenti`mix`|
| 1.13 | 2021 |  Miglioramenti `mix`, miglioramenti`Logger`|
| 1.14 | 2022 |  Miglioramenti `def`, miglioramenti`mix`|
| 1.15| 2023 |  Miglioramenti `mix`, miglioramenti`Logger`|
| 1.16 | 2024 |  Miglioramenti `mix`, miglioramenti`Logger`|
| 1.17 | 2024 | Sviluppo continuo |
## Traguardi importanti
### Erlang: il linguaggio delle telecomunicazioni (1986-2000)
- **1986**: Joe Armstrong, Robert Virding e Mike Williams della Ericsson creano Erlang
- **Obiettivo**: costruire sistemi di telecomunicazioni affidabili — filosofia "lasciarlo crollare".
- **Caratteristiche principali**: modello ad attori, scambio di codici a caldo, calcolo distribuito
- **1998**: Open source (R1) — Erlang entra nel mondo più ampio
- **Utilizzato da**: switch ATM Ericsson AXD301 (tempo di attività del 99,9999999% — "nove nove")
### Maturità Erlang/OTP (2000–2013)
- **OTP** (Open Telecom Platform): framework, librerie, strumenti
- **Mnesia**: database distribuito
- **Dializzatore** — analisi di tipo statico
- **R16B (2013)**: Mappe: struttura dati chiave-valore
### Erlang Era moderna (2014-oggi)
- **17.0 (2014)**: Mappe: funzionalità linguistica principale
- **18.0 (2015)**: nuova API temporale, operazioni sulle mappe
- **21.0 (2018)**: Nuovo`logger`(sostituisce`error_logger`)
- **22.0–27.0**: miglioramenti continui a SSL, distribuzione e prestazioni
### Elisir: Erlang per la comunità Ruby (2011-oggi)
- **2011**: José Valim crea Elixir — compila in Erlang BEAM
- **Obiettivo**: produttività di Ruby + affidabilità di Erlang
- **Caratteristiche principali**: Metaprogrammazione, pipe `|>`, macro, strumento di creazione `mix`
- **1.0 (2014)**: prima versione stabile
- **1.6 (2018)**:`mix format`— formattatore di codice integrato
- **1.9 (2019)**:`mix release`— versioni autonome (non è necessario Erlang)
## Evoluzione della sintassi
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

## Principi chiave di progettazione
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

## Crescita dell'ecosistema
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
