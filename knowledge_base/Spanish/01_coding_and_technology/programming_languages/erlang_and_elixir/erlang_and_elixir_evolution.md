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
# Erlang & Elixir - Historial de versiones y evolución
## Cronología de Erlang
| Versión | Año | Tema clave |
|---------|------|-----------|
| Erlang 1 | 1986 | **Primer Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Primer lanzamiento público |
| Erlang 5 (R1) | 1998 | **Código abierto** lanzamiento |
| R9B | 2002 | Base de datos Mnesia, rendimiento mejorado |
| R12B | 2006 | Dializador (verificador de tipo) |
| R13B | 2008 | Mejoras en registros, mejoras en`fun`|
| R14B | 2010 | Comprensión binaria, GC mejorado |
| R15B | 2012 | Mapas (experimentales) |
| R16B | 2013 | **Mapas** estable |
| 17.0 | 2014 | **Principal**: Mapas, mejoras`receive`|
| 18.0 | 2015 | **Principal**: API de tiempo, operaciones `maps`, mejoras en`ssl`|
| 19.0 | 2016 |  Mejoras`try`/ `catch`, mejoras`binary`|
| 20.0 | 2017 | **Principal**: mejoras en `maps`, mejoras en`ssl`|
| 21.0 | 2018 | **Principal**: mejoras en `ssl`,`logger`(reemplaza a `error_logger`) |
| 22.0 | 2019 | **Principal**: mejoras en la distribución, mejoras en`ssl`|
| 23.0 | 2020 | **Principal**: mejoras en `maps`, mejoras en`ssl`|
| 24.0 | 2021 | **Principal**: mejoras en `ssl`, mejoras en`maps`|
| 25.0 | 2022 | **Principal**: mejoras en `ssl`, mejoras en`maps`|
| 26.0 | 2023 | **Principal**: mejoras en `ssl`, mejoras en`maps`|
| 27.0 | 2024 | **Principal**: mejoras en `ssl`, mejoras en`maps`|
## Cronología del elixir
| Versión | Año | Tema clave |
|---------|------|-----------|
| 0,1 | 2011 | Liberación inicial (José Valim) |
| 0,12 | 2013 | Primer estable pre-1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Mensajes de error mejorados |
| 0,15 | 2014 |  Mejoras en `Stream`,`Enum`|
| 1.0 | 2014 | **Primera versión estable** |
| 1.1 | 2015 |  Declaración `with`, mejoras`Logger`|
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 |  Tipos `Calendar`, mejoras`Mix`|
| 1.4 | 2017 |  Mejoras en `Registry`,`Supervisor`|
| 1.5 | 2017 |  Mejoras `Calendar`, mejoras`Logger`|
| 1.6 | 2018 | **`mix format`** (formateador de código), mejoras en`Registry`|
| 1.7 | 2019 |  Mejoras `defstruct`, mejoras`mix`|
| 1.8 | 2019 |  Mejoras `Calendar`, mejoras`Logger`|
| 1.9 | 2019 | **`mix release`** (versiones autónomas) |
| 1.10 | 2020 |  Mejoras `Calendar`, mejoras`Logger`|
| 1.11 | 2020 |  Mejoras `defdelegate`, mejoras`mix`|
| 1.12 | 2021 |  Mejoras `struct`, mejoras`mix`|
| 1.13 | 2021 |  Mejoras `mix`, mejoras`Logger`|
| 1.14 | 2022 |  Mejoras `def`, mejoras`mix`|
| 1.15 | 2023 |  Mejoras `mix`, mejoras`Logger`|
| 1.16 | 2024 |  Mejoras `mix`, mejoras`Logger`|
| 1.17 | 2024 | Desarrollo continuo |
## Hitos importantes
### Erlang: el lenguaje de las telecomunicaciones (1986-2000)
- **1986**: Joe Armstrong, Robert Virding y Mike Williams en Ericsson crean Erlang
- **Objetivo**: construir sistemas de telecomunicaciones confiables: filosofía de "déjalo colapsar"
- **Características clave**: modelo de actor, intercambio de código activo, computación distribuida
- **1998**: Código abierto (R1): Erlang ingresa al resto del mundo
- **Usado por**: conmutador de cajero automático Ericsson AXD301 (99,9999999 % de tiempo de actividad: "nueve nueves")
### Madurez de Erlang/OTP (2000-2013)
- **OTP** (Plataforma Abierta de Telecomunicaciones): marcos, bibliotecas, herramientas
- **Mnesia** — base de datos distribuida
- **Dializador** — análisis de tipo estático
- **R16B (2013)**: Mapas: estructura de datos clave-valor
### Era moderna de Erlang (2014-presente)
- **17.0 (2014)**: Mapas: característica principal del idioma
- **18.0 (2015)**: Nueva API de tiempo, operaciones de mapas
- **21.0 (2018)**: Nuevo`logger`(reemplaza a `error_logger`)
- **22.0–27.0**: mejoras continuas en SSL, distribución y rendimiento
### Elixir: Erlang para la comunidad Ruby (2011-presente)
- **2011**: José Valim crea Elixir — compila en Erlang BEAM
- **Objetivo**: Productividad de Ruby + confiabilidad de Erlang
- **Características clave**: Metaprogramación, canalizaciones `|>`, macros, herramienta de compilación `mix`
- **1.0 (2014)**: primera versión estable
- **1.6 (2018)**:`mix format`— formateador de código incorporado
- **1.9 (2019)**: `mix release`: versiones independientes (no se necesita Erlang)
## Evolución de la sintaxis
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

## Principios clave de diseño
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

## Crecimiento del ecosistema
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
