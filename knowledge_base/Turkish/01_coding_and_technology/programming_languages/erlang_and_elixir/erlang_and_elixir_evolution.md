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
# Erlang ve İksir — Sürüm Geçmişi ve Gelişimi
## Erlang Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Erlang 1 | 1986 | **İlk Erlang** (Joe Armstrong, Ericsson) |
| Erlang 4 | 1991 | İlk halka açık yayın |
| Erlang 5 (R1) | 1998 | **Açık kaynak** sürümü |
| R9B | 2002 | Mnesia veritabanı, geliştirilmiş performans |
| R12B | 2006 | Diyalizör (tip denetleyici) |
| R13B | 2008 | Kayıt iyileştirmeleri,`fun`iyileştirmeleri |
| R14B | 2010 | İkili anlama, geliştirilmiş GC |
| R15B | 2012 | Haritalar (deneysel) |
| R16B | 2013 | **Haritalar** kararlı |
| 17.0 | 2014 | **Önemli**: Haritalar,`receive`iyileştirmeleri |
| 18.0 | 2015 | **Ana**: Time API,`maps`işlemleri,`ssl`iyileştirmeleri |
| 19.0 | 2016 | `try`/`catch`iyileştirmeleri,`binary`iyileştirmeleri |
| 20.0 | 2017 | **Önemli**:`maps`iyileştirmeleri,`ssl`iyileştirmeleri |
| 21.0 | 2018 | **Önemli**:`ssl`iyileştirmeleri,`logger`(`error_logger`'nin yerine geçer) |
| 22.0 | 2019 | **Önemli**: Dağıtım iyileştirmeleri,`ssl`iyileştirmeleri |
| 23.0 | 2020 | **Önemli**:`maps`iyileştirmeleri,`ssl`iyileştirmeleri |
| 24.0 | 2021 | **Önemli**:`ssl`iyileştirmeleri,`maps`iyileştirmeleri |
| 25.0 | 2022 | **Önemli**:`ssl`iyileştirmeleri,`maps`iyileştirmeleri |
| 26.0 | 2023 | **Önemli**:`ssl`iyileştirmeleri,`maps`iyileştirmeleri |
| 27.0 | 2024 | **Önemli**:`ssl`iyileştirmeleri,`maps`iyileştirmeleri |
## İksir Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| 0.1 | 2011 | İlk sürüm (José Valim) |
| 0.12 | 2013 | 1.0 öncesi ilk kararlı |
| 0.13 | 2014 | `defprotocol`,`defimpl`|
| 0.14 | 2014 | Geliştirilmiş hata mesajları |
| 0.15 | 2014 | `Stream`,`Enum`iyileştirmeleri |
| 1.0 | 2014 | **İlk kararlı sürüm** |
| 1.1 | 2015 | `with`bildirimi,`Logger`iyileştirmeleri |
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 | `Calendar`türleri,`Mix`iyileştirmeleri |
| 1.4 | 2017 | `Registry`,`Supervisor`iyileştirmeleri |
| 1.5 | 2017 | `Calendar`iyileştirmeleri,`Logger`iyileştirmeleri |
| 1.6 | 2018 | **`mix format`** (kod formatlayıcı),`Registry`iyileştirmeleri |
| 1.7 | 2019 | `defstruct`iyileştirmeleri,`mix`iyileştirmeleri |
| 1.8 | 2019 | `Calendar`iyileştirmeleri,`Logger`iyileştirmeleri |
| 1.9 | 2019 | **`mix release`** (bağımsız sürümler) |
| 1.10 | 2020 | `Calendar`iyileştirmeleri,`Logger`iyileştirmeleri |
| 1.11 | 2020 | `defdelegate`iyileştirmeleri,`mix`iyileştirmeleri |
| 1.12 | 2021 | `struct`iyileştirmeleri,`mix`iyileştirmeleri |
| 1.13 | 2021 | `mix`iyileştirmeleri,`Logger`iyileştirmeleri |
| 1.14 | 2022 | `def`iyileştirmeleri,`mix`iyileştirmeleri |
| 1.15 | 2023 | `mix`iyileştirmeleri,`Logger`iyileştirmeleri |
| 1.16 | 2024 | `mix`iyileştirmeleri,`Logger`iyileştirmeleri |
| 1.17 | 2024 | Devam eden geliştirme |
## Önemli Kilometre Taşları
### Erlang: Telekom Dili (1986–2000)
- **1986**: Ericsson'dan Joe Armstrong, Robert Virding, Mike Williams Erlang'ı yarattı
- **Hedef**: Güvenilir telekomünikasyon sistemleri oluşturmak — "bırakın çöksün" felsefesi
- **Temel özellikler**: Aktör modeli, çalışırken kod değiştirme, dağıtılmış bilgi işlem
- **1998**: Açık kaynaklı (R1) — Erlang daha geniş bir dünyaya açılıyor
- **Kullanılan**: Ericsson AXD301 ATM anahtarı (%99,9999999 çalışma süresi — "dokuz dokuzlu")
### Erlang/OTP Olgunluğu (2000–2013)
- **OTP** (Açık Telekom Platformu) — çerçeveler, kitaplıklar, araçlar
- **Mnesia** — dağıtılmış veritabanı
- **Diyalizör** — statik tür analizi
- **R16B (2013)**: Haritalar — anahtar/değer veri yapısı
### Erlang Modern Çağı (2014 – günümüz)
- **17.0 (2014)**: Haritalar — önemli dil özelliği
- **18.0 (2015)**: Yeni zaman API'si, harita işlemleri
- **21.0 (2018)**: Yeni`logger`(`error_logger`'nin yerine geçer)
- **22.0–27.0**: SSL, dağıtım ve performansta sürekli iyileştirmeler
### İksir: Ruby Topluluğu için Erlang (2011-günümüz)
- **2011**: José Valim İksir'i yaratıyor — Erlang BEAM'e derliyor
- **Hedef**: Ruby'nin üretkenliği + Erlang'ın güvenilirliği
- **Temel özellikler**: Metaprogramlama,`|>`kanalları, makrolar,`mix`derleme aracı
- **1.0 (2014)**: İlk kararlı sürüm
- **1.6 (2018)**:`mix format`— yerleşik kod biçimlendirici
- **1.9 (2019)**:`mix release`— bağımsız sürümler (Erlang'a gerek yok)
## Söz Dizimi Gelişimi
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

## Temel Tasarım İlkeleri
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

## Ekosistem Büyümesi
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
