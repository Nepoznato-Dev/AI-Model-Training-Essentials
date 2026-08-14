<!--
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

-->
# Erlang 和 Elixir — 语法参考
本文档为 Erlang 和 Elixir 提供了全面、结构化的语法参考。它通过关注模式匹配、流程管理、OTP 行为和容错系统模式来补充主要参考。
---

## Erlang — 核心语法
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

## Elixir — 核心语法
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

## 进程和消息传递
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

## OTP 行为 (Elixir)
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

## 错误处理
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

＃＃ 概括
Erlang 和 Elixir 共享 BEAM VM 的超能力：轻量级进程、消息传递和容错监督树。 Erlang 的语法简洁且实用。 Elixir 添加了带有管道、宏和协议的现代语法。 OTP 行为（GenServer、Supervisor、应用程序）为构建可靠的系统提供了经过实战检验的模式。对于实时、分布式、容错应用程序，Erlang/Elixir 仍然是无与伦比的。