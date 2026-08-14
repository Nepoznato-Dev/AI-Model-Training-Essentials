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
# Erlang & Elixir — Riwayat Versi & Evolusi
## Garis Waktu Erlang
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Erlang 1 | 1986 | **Erlang Pertama** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | Rilis publik pertama |
| Erlang 5 (R1) | 1998 | **Sumber terbuka** rilis |
| R9B | 2002 | Basis data Mnesia, peningkatan kinerja |
| R12B | 2006 | Dialyzer (pemeriksa tipe) |
| R13B | 2008 | Mencatat peningkatan, peningkatan`fun`|
| R14B | 2010 | Pemahaman biner, peningkatan GC |
| R15B | 2012 | Peta (eksperimental) |
| R16B | 2013 | **Peta** stabil |
| 17.0 | 2014 | **Utama**: Peta, peningkatan`receive`|
| 18.0 | 2015 | **Utama**: API Waktu, operasi `maps`, peningkatan`ssl`|
| 19.0 | 2016 |  Peningkatan`try`/ `catch`, peningkatan`binary`|
| 20.0 | 2017 | **Utama**: peningkatan `maps`, peningkatan`ssl`|
| 21.0 | 2018 | **Utama**: Peningkatan `ssl`,`logger`(menggantikan`error_logger`) |
| 22.0 | 2019 | **Utama**: Peningkatan distribusi, peningkatan`ssl`|
| 23.0 | 2020 | **Utama**: Peningkatan `maps`, Peningkatan`ssl`|
| 24.0 | 2021 | **Utama**: Peningkatan `ssl`, Peningkatan`maps`|
| 25.0 | 2022 | **Utama**: Peningkatan `ssl`, Peningkatan`maps`|
| 26.0 | 2023 | **Utama**: Peningkatan `ssl`, Peningkatan`maps`|
| 27.0 | 2024 | **Utama**: Peningkatan `ssl`, Peningkatan`maps`|
## Garis Waktu Ramuan
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| 0,1 | 2011 | Rilis awal (José Valim) |
| 0,12 | 2013 | Stabil pertama sebelum 1.0 |
| 0,13 | 2014 | `defprotocol`,`defimpl`|
| 0,14 | 2014 | Pesan kesalahan yang ditingkatkan |
| 0,15 | 2014 |  Peningkatan `Stream`,`Enum`|
| 1.0 | 2014 | **Rilis stabil pertama** |
| 1.1 | 2015 |  Pernyataan `with`, peningkatan`Logger`|
| 1.2 | 2016 |  Server Gen `Multi-call`,`MapSet`|
| 1.3 | 2016 |  Tipe `Calendar`, peningkatan`Mix`|
| 1.4 | 2017 |  Peningkatan `Registry`,`Supervisor`|
| 1.5 | 2017 |  Peningkatan `Calendar`, peningkatan`Logger`|
| 1.6 | 2018 | **`mix format`** (pemformat kode), peningkatan`Registry`|
| 1.7 | 2019 |  Peningkatan `defstruct`, peningkatan`mix`|
| 1.8 | 2019 |  Peningkatan `Calendar`, peningkatan`Logger`|
| 1.9 | 2019 | **`mix release`** (rilis mandiri) |
| 1.10 | 2020 |  Peningkatan `Calendar`, peningkatan`Logger`|
| 1.11 | 2020 |  Peningkatan `defdelegate`, peningkatan`mix`|
| 1.12 | 2021 |  Peningkatan `struct`, peningkatan`mix`|
| 1.13 | 2021 |  Peningkatan `mix`, peningkatan`Logger`|
| 1.14 | 2022 |  Peningkatan `def`, peningkatan`mix`|
| 1.15 | 2023 |  Peningkatan `mix`, peningkatan`Logger`|
| 1.16 | 2024 |  Peningkatan `mix`, peningkatan`Logger`|
| 1.17 | 2024 | Pembangunan yang sedang berlangsung |
## Tonggak Penting
### Erlang: Bahasa Telekomunikasi (1986–2000)
- **1986**: Joe Armstrong, Robert Virding, Mike Williams di Ericsson menciptakan Erlang
- **Sasaran**: Membangun sistem telekomunikasi yang andal — filosofi "biarkan crash".
- **Fitur utama**: Model aktor, pertukaran kode panas, komputasi terdistribusi
- **1998**: Open source (R1) — Erlang memasuki dunia yang lebih luas
- **Digunakan oleh**: Switch ATM Ericsson AXD301 (waktu aktif 99,9999999% — "sembilan sembilan")
### Kedewasaan Erlang/OTP (2000–2013)
- **OTP** (Open Telecom Platform) — kerangka kerja, perpustakaan, alat
- **Mnesia** — basis data terdistribusi
- **Dialyzer** — analisis tipe statis
- **R16B (2013)**: Peta — struktur data nilai kunci
### Erlang Era Modern (2014–sekarang)
- **17.0 (2014)**: Peta — fitur bahasa utama
- **18.0 (2015)**: API waktu baru, operasi peta
- **21.0 (2018)**:`logger`baru (menggantikan`error_logger`)
- **22.0–27.0**: Peningkatan berkelanjutan pada SSL, distribusi, kinerja
### Elixir: Erlang untuk Komunitas Ruby (2011–sekarang)
- **2011**: José Valim membuat Elixir — mengkompilasi ke Erlang BEAM
- **Sasaran**: Produktivitas Ruby + keandalan Erlang
- **Fitur utama**: Pemrograman meta, pipa `|>`, makro, alat pembuatan `mix`
- **1.0 (2014)**: Rilis stabil pertama
- **1.6 (2018)**:`mix format`— pemformat kode bawaan
- **1.9 (2019)**:`mix release`— rilis mandiri (tidak diperlukan Erlang)
## Evolusi Sintaks
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

## Prinsip Desain Utama
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

## Pertumbuhan Ekosistem
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
