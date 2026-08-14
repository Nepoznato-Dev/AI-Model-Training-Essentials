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
# Erlang & Elixir — Tham khảo cú pháp
Tài liệu này cung cấp tài liệu tham khảo cú pháp có cấu trúc, toàn diện cho Erlang và Elixir. Nó bổ sung cho tài liệu tham khảo chính bằng cách tập trung vào khớp mẫu, quản lý quy trình, hành vi OTP và các mẫu hệ thống có khả năng chịu lỗi.
---

## Erlang — Cú pháp cốt lõi
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

## Elixir — Cú pháp cốt lõi
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

## Quy trình & Truyền tin nhắn
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

## Hành vi OTP (Elixir)
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

## Xử lý lỗi
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

## Bản tóm tắt
Erlang và Elixir chia sẻ các siêu năng lực của BEAM VM: quy trình nhẹ, truyền tin nhắn và cây giám sát có khả năng chịu lỗi. Cú pháp của Erlang tối giản và đầy đủ chức năng. Elixir bổ sung thêm cú pháp hiện đại với các pipe, macro và giao thức. Hành vi OTP (GenServer, Người giám sát, Ứng dụng) cung cấp các mẫu đã được thử nghiệm trong thực tế để xây dựng các hệ thống đáng tin cậy. Đối với các ứng dụng thời gian thực, phân tán, có khả năng chịu lỗi cao, Erlang/Elixir vẫn chưa có đối thủ.