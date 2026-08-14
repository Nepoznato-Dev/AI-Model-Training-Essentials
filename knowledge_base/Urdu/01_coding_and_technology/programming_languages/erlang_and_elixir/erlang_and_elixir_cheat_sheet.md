<!--
---
# Metadata
title: "Erlang & Elixir — Cheat Sheet"
description: "Quick-reference cheat sheet for Erlang and Elixir syntax and BEAM patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [erlang, elixir, beam, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# ایرلنگ اور ایلیکسیر - دھوکہ دہی کی شیٹ
## ایلیکسیر کی بنیادی باتیں
```elixir
# Variables (immutable)
name = "Alice"
age = 30
pi = 3.14159
active = true
nothing = nil

# Types
is_binary(name)     # true
is_integer(42)      # true
is_float(3.14)      # true
is_boolean(true)    # true
is_atom(:hello)     # true
is_nil(nil)         # true
is_list([1,2])      # true
is_map(%{})         # true

# String (binary) operations
String.length(name)
String.upcase(name)
String.downcase(name)
String.trim("  hi  ")
String.contains?(name, "lic")
String.replace(name, "Alice", "Bob")
String.slice(name, 0, 3)
"Hello, #{name}!"
to_string(42)
String.to_integer("42")
```

## ایلیکسیر کلیکشنز
```elixir
# List
[1, 2, 3]
[0 | [1, 2, 3]]           # prepend: [0, 1, 2, 3]
hd([1, 2, 3])              # 1
tl([1, 2, 3])              # [2, 3]
length([1, 2, 3])           # 3
Enum.map([1,2,3], &(&1 * 2))
Enum.filter([1,2,3,4], &(rem(&1, 2) == 0))
Enum.reduce([1,2,3], 0, &+/2)
Enum.each([1,2,3], &IO.inspect/1)
Enum.sort([3,1,2])
Enum.reverse([1,2,3])

# Tuple
{:ok, "value"}
elem({:ok, "value"}, 0)    # :ok
{:error, reason} = result  # pattern match
put_elem(tuple, 0, :error)

# Map
%{name: "Alice", age: 30}
map = %{name: "Alice"}
map[:name]                 # "Alice"
map.name                   # "Alice"
Map.get(map, :name)
Map.put(map, :email, "a@b.com")
Map.merge(m1, m2)
Map.keys(map)
Map.values(map)

# Keyword list (list of tuples)
[name: "Alice", age: 30]
opts = [timeout: 5000, retry: true]
opts[:timeout]             # 5000

# Pattern matching
{:ok, value} = {:ok, 42}
%{name: name} = %{name: "Alice", age: 30}
[a, b, c] = [1, 2, 3]
```

## ایلیکسیر کنٹرول فلو
```elixir
# if/else
if condition do
  "yes"
else
  "no"
end

# case
case value do
  0 -> "zero"
  n when n > 0 -> "positive"
  _ -> "other"
end

# cond
cond do
  score >= 90 -> "A"
  score >= 80 -> "B"
  true -> "C"
end

# with
with {:ok, user} <- find_user(id),
     {:ok, orders} <- get_orders(user) do
  {:ok, {user, orders}}
end

# Loops (recursion / Enum)
Enum.each(1..10, &IO.puts/1)
for x <- 1..10, do: x * x
for x <- 1..10, rem(x, 2) == 0, do: x
```

## ایرلنگ کی بنیادی باتیں
```erlang
%% Variables (uppercase, single assignment)
Name = "Alice",
Age = 30,
Pi = 3.14159,
Active = true.

%% Pattern matching
{ok, Value} = {ok, 42},
#{name := Name} = #{name => "Alice"}.

%% Atoms
hello, world, ok, error, undefined.

%% Tuples
{ok, Value}
{error, Reason}
element(1, {ok, 42}).     %% ok

%% Lists
[1, 2, 3]
[H | T] = [1, 2, 3],     %% H=1, T=[2,3]
lists:map(fun(X) -> X * 2 end, [1,2,3]).
lists:filter(fun(X) -> X > 2 end, [1,2,3,4]).
lists:foldl(fun(X, Acc) -> X + Acc end, 0, [1,2,3]).
length([1,2,3]).           %% 3
lists:reverse([1,2,3]).

%% Maps
#{name => "Alice", age => 30}
maps:get(name, Map).
maps:put(email, "a@b.com", Map).
```

## ایرلنگ کنٹرول فلو
```erlang
%% case
case Value of
    0 -> "zero";
    N when N > 0 -> "positive";
    _ -> "other"
end.

%% if
if
    X > 0 -> positive;
    X =:= 0 -> zero;
    X < 0 -> negative
end.

%% List comprehension
[ X * 2 || X <- [1,2,3,4]].
[ X || X <- [1,2,3,4,5], X > 2].

%% receive (message passing)
receive
    {hello, From} -> From ! {hi, self()};
    stop -> ok
after 5000 ->
    timeout
end.
```

## ہم آہنگی۔
```elixir
# Spawn
pid = spawn(fn -> IO.puts("running") end)
send(pid, {:hello, self()})
receive do
  {:hello, from} -> IO.inspect(from)
after 5000 -> :timeout
end

# Task
task = Task.async(fn -> expensive_op() end)
result = Task.await(task)

# GenServer pattern
defmodule Counter do
  use GenServer

  def start_link(init \\ 0), do: GenServer.start_link(__MODULE__, init)
  def increment(pid), do: GenServer.cast(pid, :increment)
  def get(pid), do: GenServer.call(pid, :get)

  @impl true
  def init(init), do: {:ok, init}
  @impl true
  def handle_cast(:increment, state), do: {:noreply, state + 1}
  @impl true
  def handle_call(:get, _from, state), do: {:reply, state, state}
end
```

## ہینڈلنگ کی خرابی۔
```elixir
# try/rescue
try do
  risky_operation()
rescue
  e in ArithmeticError -> "math error"
  e in RuntimeError -> "runtime: #{e.message}"
end

# raise
raise "Something failed"
raise ArgumentError, message: "invalid"

# Result pattern (idiomatic)
case Repo.get(User, id) do
  nil -> {:error, :not_found}
  user -> {:ok, user}
end
```

```erlang
%% try/catch
try
    risky_operation()
catch
    error:Reason -> {error, Reason};
    throw:Term -> {error, Term}
end.

%% error
error(badarg).
throw(some_value).
```
