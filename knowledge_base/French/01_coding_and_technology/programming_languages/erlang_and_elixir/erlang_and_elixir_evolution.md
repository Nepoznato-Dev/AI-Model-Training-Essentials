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
# Erlang & Elixir — Historique et évolution des versions
## Chronologie d'Erlang
| Version | Année | Thème clé |
|---------|------|-----------|
| Erlang 1 | 1986 | **Premier Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Première sortie publique |
| Erlang5 (R1) | 1998 | Version **Open source** |
| R9B | 2002 | Base de données Mnesia, performances améliorées |
| R12B | 2006 | Dialyseur (vérificateur de type) |
| R13B | 2008 | Améliorations des enregistrements, améliorations`fun`|
| R14B | 2010 | Compréhension binaire, GC amélioré |
| R15B | 2012 | Cartes (expérimentales) |
| R16B | 2013 | **Cartes** stables |
| 17,0 | 2014 | **Majeur** : Cartes, améliorations`receive`|
| 18,0 | 2015 | **Majeur** : API Time, opérations `maps`, améliorations`ssl`|
| 19,0 | 2016 |  Améliorations`try`/ `catch`, améliorations`binary`|
| 20,0 | 2017 | **Majeur** : améliorations `maps`, améliorations`ssl`|
| 21.0 | 2018 | **Majeur** : améliorations `ssl`,`logger`(remplace `error_logger`) |
| 22,0 | 2019 | **Majeur** : améliorations de la distribution, améliorations de`ssl`|
| 23,0 | 2020 | **Majeur** : améliorations `maps`, améliorations`ssl`|
| 24,0 | 2021 | **Majeur** : améliorations `ssl`, améliorations`maps`|
| 25,0 | 2022 | **Majeur** : améliorations `ssl`, améliorations`maps`|
| 26,0 | 2023 | **Majeur** : améliorations `ssl`, améliorations`maps`|
| 27,0 | 2024 | **Majeur** : améliorations `ssl`, améliorations`maps`|
## Chronologie de l'élixir
| Version | Année | Thème clé |
|---------|------|-----------|
| 0,1 | 2011 | Sortie initiale (José Valim) |
| 0,12 | 2013 | Premier stable pré-1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Messages d'erreur améliorés |
| 0,15 | 2014 |  Améliorations`Stream`,`Enum`|
| 1.0 | 2014 | **Première version stable** |
| 1.1 | 2015 |  Instruction `with`, améliorations`Logger`|
| 1.2 | 2016 |  Serveur générateur `Multi-call`,`MapSet`|
| 1.3 | 2016 |  Types `Calendar`, améliorations`Mix`|
| 1.4 | 2017 |  Améliorations`Registry`,`Supervisor`|
| 1.5 | 2017 |  Améliorations `Calendar`, améliorations`Logger`|
| 1.6 | 2018 | **`mix format`** (formateur de code), améliorations`Registry`|
| 1.7 | 2019 |  Améliorations `defstruct`, améliorations`mix`|
| 1.8 | 2019 |  Améliorations `Calendar`, améliorations`Logger`|
| 1.9 | 2019 | **`mix release`** (versions autonomes) |
| 1.10 | 2020 |  Améliorations `Calendar`, améliorations`Logger`|
| 1.11 | 2020 |  Améliorations `defdelegate`, améliorations`mix`|
| 1.12 | 2021 |  Améliorations `struct`, améliorations`mix`|
| 1.13 | 2021 |  Améliorations `mix`, améliorations`Logger`|
| 1.14 | 2022 |  Améliorations `def`, améliorations`mix`|
| 1.15 | 2023 |  Améliorations `mix`, améliorations`Logger`|
| 1.16 | 2024 |  Améliorations `mix`, améliorations`Logger`|
| 1.17 | 2024 | Développement en cours |
## Étapes majeures
### Erlang : le langage des télécommunications (1986-2000)
- **1986** : Joe Armstrong, Robert Virding, Mike Williams chez Ericsson créent Erlang
- **Objectif** : Construire des systèmes de télécommunications fiables – philosophie du "laissez-le planter"
- **Principales fonctionnalités** : modèle d'acteur, échange de code à chaud, informatique distribuée
- **1998** : Open source (R1) — Erlang entre dans le monde plus large
- **Utilisé par** : commutateur ATM Ericsson AXD301 (disponibilité de 99,9999999 % – "neuf neuf")
### Maturité Erlang/OTP (2000-2013)
- **OTP** (Open Telecom Platform) — frameworks, bibliothèques, outils
- **Mnesia** — base de données distribuée
- **Dialyseur** — analyse de type statique
- **R16B (2013)** : Cartes — structure de données clé-valeur
### Erlang Modern Era (2014-présent)
- **17.0 (2014)** : Cartes — fonctionnalité linguistique majeure
- **18.0 (2015)** : Nouvelle API temporelle, opérations sur les cartes
- **21.0 (2018)** : Nouveau`logger`(remplace `error_logger`)
- **22.0–27.0** : améliorations continues de SSL, de la distribution et des performances
### Elixir : Erlang pour la communauté Ruby (2011-présent)
- **2011** : José Valim crée Elixir — compile en Erlang BEAM
- **Objectif** : Productivité de Ruby + fiabilité d'Erlang
- **Principales fonctionnalités** : Métaprogrammation, tuyaux `|>`, macros, outil de construction `mix`
- **1.0 (2014)** : Première version stable
- **1.6 (2018)** :`mix format`— formateur de code intégré
- **1.9 (2019)** :`mix release`— versions autonomes (aucun Erlang requis)
## Évolution de la syntaxe
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

## Principes de conception clés
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

## Croissance de l'écosystème
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
