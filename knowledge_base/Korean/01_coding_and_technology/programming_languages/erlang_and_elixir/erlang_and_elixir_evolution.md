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

# Erlang & Elixir — 버전 기록 및 진화
## 얼랭 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 얼랭 1 | 1986 | **First Erlang** (조 암스트롱, 에릭슨) |
| 얼랭 4 | 1991 | 최초 공개 |
| 얼랭 5(R1) | 1998 | **오픈 소스** 출시 |
| R9B | 2002 | Mnesia 데이터베이스, 성능 향상 |
| R12B | 2006년 | 투석기(유형 검사기) |
| R13B | 2008 | 기록 개선,`fun`개선 |
| R14B | 2010 | 바이너리 이해력, 향상된 GC |
| R15B | 2012 | 지도(실험적) |
| R16B | 2013 | **지도** 안정적 |
| 17.0 | 2014 | **주요**: 지도,`receive`개선 |
| 18.0 | 2015 | **주요**: Time API,`maps`작업,`ssl`개선 |
| 19.0 | 2016 | `try`/`catch`개선,`binary`개선 |
| 20.0 | 2017 | **주요**:`maps`개선,`ssl`개선 |
| 21.0 | 2018 | **주요**:`ssl`개선 사항, `logger`(`error_logger`대체) |
| 22.0 | 2019 | **주요**: 배포 개선,`ssl`개선 |
| 23.0 | 2020 | **주요**:`maps`개선,`ssl`개선 |
| 24.0 | 2021 | **주요**:`ssl`개선,`maps`개선 |
| 25.0 | 2022 | **주요**:`ssl`개선,`maps`개선 |
| 26.0 | 2023년 | **주요**:`ssl`개선,`maps`개선 |
| 27.0 | 2024 | **주요**:`ssl`개선,`maps`개선 |
## 엘릭서 타임라인
| 버전 | 연도 | 주요 테마 |
|---------|------|------------|
| 0.1 | 2011 | 최초 출시(José Valim) |
| 0.12 | 2013 | 최초의 안정적인 1.0 이전 |
| 0.13 | 2014 |  `defprotocol`,`defimpl`|
| 0.14 | 2014 | 향상된 오류 메시지 |
| 0.15 | 2014 | `Stream`,`Enum`개선 |
| 1.0 | 2014 | **첫 번째 안정 릴리스** |
| 1.1 | 2015 | `with`문,`Logger`개선 |
| 1.2 | 2016 | `Multi-call`GenServer,`MapSet`|
| 1.3 | 2016 | `Calendar`유형,`Mix`개선 |
| 1.4 | 2017 | `Registry`,`Supervisor`개선 |
| 1.5 | 2017 | `Calendar`개선,`Logger`개선 |
| 1.6 | 2018 | **`mix format`** (코드 포맷터),`Registry`개선 |
| 1.7 | 2019 | `defstruct`개선,`mix`개선 |
| 1.8 | 2019 | `Calendar`개선,`Logger`개선 |
| 1.9 | 2019 | **`mix release`** (자체 포함 릴리스) |
| 1.10 | 2020 | `Calendar`개선,`Logger`개선 |
| 1.11 | 2020 | `defdelegate`개선,`mix`개선 |
| 1.12 | 2021 | `struct`개선,`mix`개선 |
| 1.13 | 2021 | `mix`개선,`Logger`개선 |
| 1.14 | 2022 | `def`개선,`mix`개선 |
| 1.15 | 2023년 | `mix`개선,`Logger`개선 |
| 1.16 | 2024 | `mix`개선,`Logger`개선 |
| 1.17 | 2024 | 지속적인 개발 |
## 주요 이정표
### 얼랭: 통신 언어(1986~2000)
- **1986**: Ericsson의 Joe Armstrong, Robert Virding, Mike Williams가 Erlang을 만들었습니다.
- **목표**: 안정적인 통신 시스템 구축 - "충돌되도록 놔두세요"라는 철학
- **주요 기능**: 액터 모델, 핫 코드 스와핑, 분산 컴퓨팅
- **1998**: 오픈 소스(R1) — Erlang이 더 넓은 세계로 진출
- **사용 대상**: Ericsson AXD301 ATM 스위치(99.9999999% 가동 시간 — "nine nines")
### 얼랭/OTP 성숙도(2000~2013)
- **OTP**(개방형 통신 플랫폼) — 프레임워크, 라이브러리, 도구
- **Mnesia** — 분산 데이터베이스
- **Dialyzer** — 정적 유형 분석
- **R16B(2013)**: 맵 — 키-값 데이터 구조
### 얼랑 현대 시대(2014~현재)
- **17.0 (2014)**: 지도 — 주요 언어 기능
- **18.0 (2015)**: 새로운 시간 API, 지도 작업
- **21.0(2018)**: 새로운 `logger`(`error_logger` 대체)
- **22.0–27.0**: SSL, 배포, 성능에 대한 지속적인 개선
### Elixir: Ruby 커뮤니티를 위한 Erlang(2011~현재)
- **2011**: José Valim이 Elixir를 만들고 Erlang BEAM으로 컴파일합니다.
- **목표**: Ruby의 생산성 + Erlang의 신뢰성
- **주요 기능**: 메타프로그래밍, 파이프 `|>`, 매크로,`mix`빌드 도구
- **1.0(2014)**: 첫 번째 안정 릴리스
- **1.6 (2018)**:`mix format`— 내장 코드 포맷터
- **1.9 (2019)**:`mix release`— 자체 포함 릴리스(Erlang 필요 없음)
## 구문 진화
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

## 주요 디자인 원칙
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

## 생태계 성장
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
