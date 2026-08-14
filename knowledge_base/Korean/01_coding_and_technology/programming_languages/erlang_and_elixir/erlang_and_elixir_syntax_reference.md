---
# Metadata
title: "Erlang & Elixir — Syntax Reference"
description: "Detailed syntax reference for Erlang and Elixir covering pattern matching, processes, OTP, supervision trees, and fault-tolerant system patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [erlang, elixir, syntax-reference, pattern-matching, otp, processes, fault-tolerance, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Erlang & Elixir — 구문 참조
이 문서는 Erlang과 Elixir에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 패턴 일치, 프로세스 관리, OTP 동작 및 내결함성 시스템 패턴에 중점을 두어 기본 참조를 보완합니다.
---

## Erlang — 핵심 구문
```erlang
% Variables (uppercase)
X = 42.
Name = "Alice".
{ok, Value} = {ok, 42}.

% Atoms (lowercase identifiers)
hello.
ok.
error.
'complex atom'.

% Tuples and lists
Point = {1, 2}.
List = [1, 2, 3].
[H|T] = [1, 2, 3].  % H = 1, T = [2, 3]

% Pattern matching
case Status of
    ok    -> do_success();
    error -> do_failure();
    _     -> do_default()
end.

% Function clauses with pattern matching
factorial(0) -> 1;
factorial(N) -> N * factorial(N - 1).

% Guards
abs_val(X) when X >= 0 -> X;
abs_val(X) when X < 0  -> -X.

% List comprehensions
[X * 2 || X <- [1, 2, 3, 4, 5]].
[X || X <- List, X > 3].
```

---

## 엘릭서 — 핵심 구문
```elixir
# Variables (snake_case)
x = 42
name = "Alice"
{:ok, value} = {:ok, 42}

# Atoms
:hello
:ok
:error

# Pattern matching
case status do
  :ok    -> do_success()
  :error -> do_failure()
  _      -> do_default()
end

# Function with pattern matching
defmodule Math do
  def factorial(0), do: 1
  def factorial(n), do: n * factorial(n - 1)

  def abs_val(x) when x >= 0, do: x
  def abs_val(x) when x < 0, do: -x
end

# Pipe operator
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")

# Comprehensions
for x <- [1, 2, 3, 4, 5], x > 3, do: x * 2

# With (clean nested pattern matching)
with {:ok, user} <- find_user(id),
     {:ok, posts} <- fetch_posts(user),
     do: {:ok, {user, posts}}
```

---

## 프로세스 및 메시지 전달
```erlang
% Erlang — spawn and message passing
Pid = spawn(fun() ->
    receive
        {From, Msg} -> From ! {self(), Msg}
    end
end),
Pid ! {self(), hello},
receive
    {Pid, Response} -> io:format("~p~n", [Response])
end.
```

```elixir
# Elixir — spawn and message passing
pid = spawn(fn ->
  receive do
    {from, msg} -> send(from, {:ok, msg})
  end
end)

send(pid, {self(), :hello})
receive do
  {:ok, msg} -> IO.puts(msg)
end
```

---

## OTP 동작(Elixir)
```elixir
# GenServer
defmodule KeyValueStore do
  use GenServer

  # Client API
  def start_link(initial \\ %{}),
    do: GenServer.start_link(__MODULE__, initial, name: __MODULE__)

  def put(key, value), do: GenServer.cast(__MODULE__, {:put, key, value})
  def get(key), do: GenServer.call(__MODULE__, {:get, key})

  # Server callbacks
  def init(state), do: {:ok, state}

  def handle_cast({:put, key, value}, state),
    do: {:noreply, Map.put(state, key, value)}

  def handle_call({:get, key}, _from, state),
    do: {:reply, Map.get(state, key), state}
end

# Supervisor
defmodule App.Supervisor do
  use Supervisor

  def start_link(opts),
    do: Supervisor.start_link(__MODULE__, opts, name: __MODULE__)

  def init(_opts) do
    children = [
      {KeyValueStore, %{}},
      {Registry, keys: :unique, name: App.Registry}
    ]
    Supervisor.init(children, strategy: :one_for_one)
  end
end
```

---

## 오류 처리
```elixir
# try/rescue/catch
try do
  risky_operation()
rescue
  e in ArgumentError -> Logger.error("Bad arg: #{e.message}")
  e in RuntimeError  -> Logger.error("Runtime: #{e.message}")
catch
  :exit, reason -> Logger.error("Exit: #{reason}")
after
  cleanup()
end

# {:ok, result} | {:error, reason} pattern
case File.read("data.txt") do
  {:ok, content}    -> process(content)
  {:error, :enoent} -> Logger.warning("File not found")
  {:error, reason}  -> Logger.error("Failed: #{reason}")
end

# raise / Exception
raise ArgumentError, message: "invalid input"
raise "something went wrong"
```

---

## 요약
Erlang과 Elixir는 경량 프로세스, 메시지 전달, 내결함성 감독 트리 등 BEAM VM의 강력한 기능을 공유합니다. Erlang의 구문은 최소한이며 기능적입니다. Elixir는 파이프, 매크로, 프로토콜과 함께 현대적인 구문을 추가합니다. OTP 동작(GenServer, Supervisor, Application)은 안정적인 시스템 구축을 위해 검증된 패턴을 제공합니다. 실시간 분산 내결함성 애플리케이션의 경우 Erlang/Elixir는 타의 추종을 불허합니다.