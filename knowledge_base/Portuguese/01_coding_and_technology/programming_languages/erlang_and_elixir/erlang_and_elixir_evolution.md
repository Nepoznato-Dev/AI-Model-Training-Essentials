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
# Erlang & Elixir – Histórico de versões e evolução
## Linha do tempo de Erlang
| Versão | Ano | Tema principal |
|--------|------|-----------|
| Erlang 1 | 1986 | **Primeiro Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Primeiro lançamento público |
| Erlang 5 (R1) | 1998 | **Código aberto** lançamento |
| R9B | 2002 | Banco de dados Mnesia, melhor desempenho |
| R12B | 2006 | Dialisador (verificador de tipo) |
| R13B | 2008 | Melhorias de registros, melhorias`fun`|
| R14B | 2010 | Compreensão binária, GC aprimorado |
| R15B | 2012 | Mapas (experimentais) |
| R16B | 2013 | **Mapas** estável |
| 17,0 | 2014 | **Principais**: Mapas, melhorias no`receive`|
| 18,0 | 2015 | **Principal**: API Time, operações `maps`, melhorias`ssl`|
| 19,0 | 2016 |  Melhorias`try`/ `catch`, melhorias`binary`|
| 20,0 | 2017 | **Principais**: melhorias em `maps`, melhorias em`ssl`|
| 21,0 | 2018 | **Principais**: melhorias em `ssl`,`logger`(substitui`error_logger`) |
| 22,0 | 2019 | **Principais**: Melhorias na distribuição, melhorias no`ssl`|
| 23,0 | 2020 | **Principais**: melhorias em `maps`, melhorias em`ssl`|
| 24,0 | 2021 | **Principais**: melhorias em `ssl`, melhorias em`maps`|
| 25,0 | 2022 | **Principais**: melhorias em `ssl`, melhorias em`maps`|
| 26,0 | 2023 | **Principais**: melhorias em `ssl`, melhorias em`maps`|
| 27,0 | 2024 | **Principais**: melhorias no `ssl`, melhorias no`maps`|
## Linha do tempo do Elixir
| Versão | Ano | Tema principal |
|--------|------|-----------|
| 0,1 | 2011 | Lançamento inicial (José Valim) |
| 0,12 | 2013 | Primeiro estável pré-1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Mensagens de erro aprimoradas |
| 0,15 | 2014 |  Melhorias em `Stream`,`Enum`|
| 1,0 | 2014 | **Primeira versão estável** |
| 1.1 | 2015 |  Instrução `with`, melhorias`Logger`|
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 |  Tipos `Calendar`, melhorias`Mix`|
| 1.4 | 2017 |  Melhorias`Registry`,`Supervisor`|
| 1,5 | 2017 |  Melhorias `Calendar`, melhorias`Logger`|
| 1.6 | 2018 | **`mix format`** (formatador de código), melhorias`Registry`|
| 1.7 | 2019 |  Melhorias `defstruct`, melhorias`mix`|
| 1.8 | 2019 |  Melhorias `Calendar`, melhorias`Logger`|
| 1,9 | 2019 | **`mix release`** (lançamentos independentes) |
| 1.10 | 2020 |  Melhorias `Calendar`, melhorias`Logger`|
| 1.11 | 2020 |  Melhorias `defdelegate`, melhorias`mix`|
| 1.12 | 2021 |  Melhorias `struct`, melhorias`mix`|
| 1.13 | 2021 |  Melhorias `mix`, melhorias`Logger`|
| 1.14 | 2022 |  Melhorias `def`, melhorias`mix`|
| 1,15 | 2023 |  Melhorias `mix`, melhorias`Logger`|
| 1.16 | 2024 |  Melhorias `mix`, melhorias`Logger`|
| 1.17 | 2024 | Desenvolvimento contínuo |
## Marcos importantes
### Erlang: a linguagem das telecomunicações (1986–2000)
- **1986**: Joe Armstrong, Robert Virding, Mike Williams da Ericsson criam Erlang
- **Objetivo**: Construir sistemas de telecomunicações confiáveis — filosofia "deixe travar"
- **Principais recursos**: modelo de ator, troca dinâmica de código, computação distribuída
- **1998**: Código aberto (R1) — Erlang entra no mundo mais amplo
- **Usado por**: switch ATM Ericsson AXD301 (99,9999999% de tempo de atividade - "nove noves")
### Maturidade Erlang/OTP (2000–2013)
- **OTP** (Open Telecom Platform) — frameworks, bibliotecas, ferramentas
- **Mnesia** — banco de dados distribuído
- **Dialisador** — análise de tipo estático
- **R16B (2013)**: Mapas — estrutura de dados de valor-chave
### Era Moderna de Erlang (2014-presente)
- **17.0 (2014)**: Mapas — principal recurso de idioma
- **18.0 (2015)**: API do novo horário, operações de mapas
- **21.0 (2018)**: Novo`logger`(substitui`error_logger`)
- **22,0–27,0**: Melhorias contínuas em SSL, distribuição, desempenho
### Elixir: Erlang para a comunidade Ruby (2011-presente)
- **2011**: José Valim cria Elixir — compila para Erlang BEAM
- **Meta**: Produtividade de Ruby + confiabilidade de Erlang
- **Principais recursos**: Metaprogramação, pipes `|>`, macros, ferramenta de construção `mix`
- **1.0 (2014)**: Primeira versão estável
- **1.6 (2018)**:`mix format`— formatador de código integrado
- **1.9 (2019)**:`mix release`— versões independentes (sem necessidade de Erlang)
## Evolução da Sintaxe
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

## Princípios-chave de design
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

## Crescimento do Ecossistema
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
