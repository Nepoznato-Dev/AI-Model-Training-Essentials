---
# Metadata
title: "Erlang & Elixir"
description: "Comprehensive reference for the Erlang and Elixir programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [erlang-and-elixir, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "38 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# এরলাং এবং এলিক্সির
Erlang 1986 সালে এরিকসন দ্বারা টেলিফোন সুইচ পাওয়ার জন্য তৈরি করা হয়েছিল - যা ব্যাখ্যা করে যে কেন এটি একযোগে, ত্রুটি সহনশীলতা, এবং বিতরণ সিস্টেমগুলিকে প্রায় অন্য যেকোনো কিছুর চেয়ে ভালভাবে পরিচালনা করে। Erlang প্রক্রিয়াগুলি হালকা, বিচ্ছিন্ন এবং শুধুমাত্র বার্তা পাসের মাধ্যমে যোগাযোগ করে। যখন একটি প্রক্রিয়া ক্র্যাশ হয়, তখন একজন সুপারভাইজার এটি পুনরায় চালু করেন। এই "এটি বিপর্যস্ত হতে দিন" দর্শন এমন সিস্টেম তৈরি করে যা ডাউনটাইম ছাড়াই বছরের পর বছর চলে।
এলিক্সির হল একটি আধুনিক ভাষা যা 2012 সালে জোসে ভ্যালিম দ্বারা Erlang-এর VM (BEAM)-এর উপরে তৈরি করা হয়েছে৷ এটি Erlang যা কিছু প্রস্তাব করে — একযোগে, ত্রুটি সহনশীলতা, বিতরণ — কিন্তু একটি বন্ধুত্বপূর্ণ বাক্য গঠন, মেটাপ্রোগ্রামিং এবং চমৎকার টুলিং (মিক্স প্যাকেজ ম্যানেজার, হেক্স প্যাকেজ রেজিস্ট্রি) যোগ করে৷ এলিক্সির ব্যাপকভাবে ওয়েব অ্যাপ্লিকেশনের জন্য ব্যবহৃত হয় (ফিনিক্স ফ্রেমওয়ার্কের মাধ্যমে), রিয়েল-টাইম সিস্টেম এবং এমবেডেড ডিভাইস (নার্ভের মাধ্যমে)।
---

## কেন এরলাং/এলিক্সির ব্যাপার
- **সঙ্গম মডেল**: বার্তা পাস করার সাথে হালকা প্রক্রিয়াগুলি — কোনও ভাগ করা অবস্থা, কোনও লক নেই, কোনও অচলাবস্থা নেই৷
- **ফল্ট টলারেন্স**: সুপারভাইজার ট্রি স্বয়ংক্রিয়ভাবে ক্র্যাশ হওয়া প্রসেস রিস্টার্ট করে। সিস্টেমগুলি ভালভাবে ত্রুটিগুলি থেকে পুনরুদ্ধার করে৷
- **ডিজাইন দ্বারা বিতরণ করা**: Erlang নোডগুলি মেশিন জুড়ে স্বচ্ছভাবে যোগাযোগ করে। ক্লাস্টার জন্য নির্মিত.
- **হট কোড রিলোডিং**: ডাউনটাইম ছাড়াই চলমান সিস্টেম আপডেট করুন। টেলিকম এবং রিয়েল-টাইম অ্যাপের জন্য গুরুত্বপূর্ণ।
- **নয় নাইন আপটাইম**: Erlang সিস্টেম উৎপাদনে 99.9999999% নির্ভরযোগ্যতা অর্জন করেছে।
- **ফিনিক্স ফ্রেমওয়ার্ক (এলিক্সির)**: রিয়েল-টাইম চ্যানেল বিল্ট ইন সহ সবচেয়ে উত্পাদনশীল ওয়েব ফ্রেমওয়ার্কগুলির মধ্যে একটি।
- **লাইভভিউ (এলিক্সির)**: জাভাস্ক্রিপ্ট না লিখেই ওয়েবসকেট সংযোগের মাধ্যমে সমৃদ্ধ, রিয়েল-টাইম ওয়েব UI তৈরি করুন।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **শুধুমাত্র কার্যকরী** | কোন পরিবর্তনশীল অবস্থা নেই, কোন OOP নেই — খাড়া শেখার বক্ররেখা | অপরিবর্তনীয়তা আলিঙ্গন; প্যাটার্ন ম্যাচিং শর্তাবলী প্রতিস্থাপন করে |
| **এরলাং সিনট্যাক্স** | প্রোলগ-এর মতো বাক্য গঠন অস্বাভাবিক এবং শব্দসমৃদ্ধ | আধুনিক সিনট্যাক্সের পরিবর্তে এলিক্সির ব্যবহার করুন |
| **ছোট চাকরীর বাজার** | পাইথন, জাভা, জাভাস্ক্রিপ্টের তুলনায় কুলুঙ্গি | নির্দিষ্ট শিল্পে উচ্চ চাহিদা (টেলিকম, ফিনটেক, গেমিং) |
| **ইকোসিস্টেমের আকার** | মূলধারার বাস্তুতন্ত্রের তুলনায় কম লাইব্রেরি | লিভারেজ Erlang এর OTP; হেক্স ক্রমাগত ক্রমবর্ধমান |
| **UI এর জন্য নয়** | কোনো নেটিভ GUI ফ্রেমওয়ার্ক নেই | ব্যাকএন্ডের জন্য ব্যবহার করুন; ফ্রন্টএন্ড ফ্রেমওয়ার্কের সাথে জোড়া |
| **স্ট্রিং হ্যান্ডলিং** | Erlang স্ট্রিংগুলি বিশ্রী (অক্ষর বা বাইনারিগুলির তালিকা) | এলিক্সির চমৎকার স্ট্রিং সমর্থন আছে |
---

## এলিক্সির সিনট্যাক্স
```elixir
# Variables (immutable — rebinding creates a new binding)
name = "Alice"
age = 30
name = "Bob"  # Rebinding is allowed, but original value is unchanged

# Atoms (named constants — like symbols in Ruby)
status = :ok
error = :error

# Pattern matching (the core mechanism)
{status, message} = {:ok, "Success"}
# status => :ok, message => "Success"

# Functions
defmodule Math do
  def add(a, b), do: a + b

  def factorial(0), do: 1
  def factorial(n) when n > 0, do: n * factorial(n - 1)

  # Pattern matching in function heads
  def describe(:ok, result), do: "Success: #{result}"
  def describe(:error, reason), do: "Error: #{reason}"
end

Math.add(2, 3)        # 5
Math.factorial(5)     # 120

# Pipe operator (chain transformations)
"  Hello, World!  "
|> String.trim()
|> String.downcase()
|> String.replace("world", "elixir")
# "hello, elixir!"

# Collections
list = [1, 2, 3, 4, 5]
Enum.map(list, &(&1 * 2))          # [2, 4, 6, 8, 10]
Enum.filter(list, &(rem(&1, 2) == 0))  # [2, 4]
Enum.reduce(list, 0, &+/2)         # 15

# Maps
user = %{name: "Alice", age: 30, email: "alice@example.com"}
user.name                          # "Alice"
%{user | age: 31}                  # Update (creates new map)

# Process spawning (lightweight — you can spawn millions)
spawn(fn ->
  IO.puts("Hello from process #{self()}")
end)

# Message passing
defmodule Counter do
  def loop(count) do
    receive do
      {:increment} -> loop(count + 1)
      {:get, sender} -> send(sender, count); loop(count)
    end
  end
end

pid = spawn(Counter, :loop, [0])
send(pid, {:increment})
send(pid, {:get, self()})
receive do count -> IO.puts("Count: #{count}") end  # Count: 1

# Error handling with try/rescue
try do
  raise "Something went wrong"
rescue
  e in RuntimeError -> IO.puts("Caught: #{e.message}")
end

# With statement (clean error handling)
with {:ok, data} <- fetch_data(),
     {:ok, parsed} <- parse(data),
     {:ok, result} <- process(parsed) do
  {:ok, result}
else
  {:error, reason} -> {:error, reason}
end
```

## এরলাং সিনট্যাক্স (রেফারেন্সের জন্য)
```erlang
-module(hello).
-export([greet/1, factorial/1]).

% Function definition
greet(Name) ->
    io:format("Hello, ~s!~n", [Name]).

% Pattern matching and recursion
factorial(0) -> 1;
factorial(N) when N > 0 ->
    N * factorial(N - 1).

% Process spawning
start() ->
    Pid = spawn(fun loop/0),
    Pid ! {self(), hello},
    receive
        Response -> io:format("Got: ~p~n", [Response])
    end.

loop() ->
    receive
        {From, Msg} -> From ! {ack, Msg}, loop()
    end.
```

---

## বাস্তুতন্ত্রের মূল উপাদান
| উপাদান | বর্ণনা |
|------------|-------------|
| **OTP** | ওপেন টেলিকম প্ল্যাটফর্ম — বিতরণ করা, ত্রুটি-সহনশীল সিস্টেম তৈরির জন্য যুদ্ধ-পরীক্ষিত কাঠামো |
| **ফিনিক্স** | রিয়েল-টাইম চ্যানেল এবং লাইভভিউ সহ উত্পাদনশীল ওয়েব ফ্রেমওয়ার্ক |
| **ইক্টো** | ডেটাবেস লাইব্রেরি এবং ক্যোয়ারী ভাষা (যেমন ActiveRecord বা SQLAlchemy) |
| **স্নায়ু** | Elixir | এর সাথে এমবেডেড IoT সিস্টেম তৈরি করুন
| **র্যাবিটএমকিউ** | Erlang লেখা বার্তা ব্রোকার, মিলিয়ন কোম্পানি দ্বারা ব্যবহৃত |
| **কাউচডিবি** | এরলাং এ লেখা ডকুমেন্ট ডাটাবেস |
| **হোয়াটসঅ্যাপ** | এরল্যাং এর কনকারেন্সি মডেল ব্যবহার করে কোটি কোটি বার্তা পরিবেশন করে |

---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### ম্যাক্রোর সাথে মেটাপ্রোগ্রামিং (এলিক্সির)
এলিক্সির ম্যাক্রো কম্পাইলের সময়ে কাজ করে, কার্যকর করার আগে AST-কে রূপান্তরিত করে।
```elixir
defmodule MyMacros do
  # Simple macro: unless (opposite of if)
  defmacro unless(condition, do: block) do
    quote do
      if !unquote(condition), do: unquote(block)
    end
  end

  # Macro with multiple arguments
  defmacro assert_equal(left, right) do
    quote do
      left_val = unquote(left)
      right_val = unquote(right)
      if left_val != right_val do
        raise "Assertion failed: #{inspect(left_val)} != #{inspect(right_val)}"
      end
    end
  end

  # DSL-building macro
  defmacro route(method, path, do: block) do
    quote do
      def handle(unquote(method), unquote(path), conn) do
        _ = conn
        unquote(block)
      end
    end
  end
end

# Usage
require MyMacros

MyMacros.unless 1 == 2 do
  IO.puts("This runs because 1 != 2")
end

# DSL example
defmodule Router do
  require MyMacros
  MyMacros.route :get, "/users" do
    {:ok, list_users()}
  end
  MyMacros.route :post, "/users" do
    {:ok, create_user(conn)}
  end
end
```

### প্রোটোকল (এলিক্সির টাইপ ক্লাস)
```elixir
# Define a protocol
defprotocol Serializable do
  @doc "Convert a data structure to a serializable format"
  def serialize(data)
end

# Implement for multiple types
defimpl Serializable, for: Map do
  def serialize(map), do: Jason.encode!(map)
end

defimpl Serializable, for: List do
  def serialize(list), do: Jason.encode!(list)
end

defimpl Serializable, for: Atom do
  def serialize(nil), do: "null"
  def serialize(true), do: "true"
  def serialize(false), do: "false"
  def serialize(atom), do: Atom.to_string(atom)
end

# Usage
Serializable.serialize(%{name: "Alice"})  # JSON string
Serializable.serialize([1, 2, 3])         # JSON array
Serializable.serialize(:ok)               # "ok"

# Derive implementation for structs
defmodule User do
  @derive [Serializable]
  defstruct [:name, :age, :email]
end
```

### আচরণ (এরলাং/এলিক্সির ইন্টারফেস)
```elixir
# Define a behaviour (contract)
defmodule CacheBehaviour do
  @callback init(opts :: keyword()) :: {:ok, state :: term()} | {:error, term()}
  @callback get(key :: term(), state :: term()) :: {:ok, term()} | :miss
  @callback put(key :: term(), value :: term(), state :: term()) :: {:ok, term()}
  @callback delete(key :: term(), state :: term()) :: :ok
end

# Implement the behaviour
defmodule MemoryCache do
  @behaviour CacheBehaviour

  @impl true
  def init(_opts), do: {:ok, %{}}

  @impl true
  def get(key, state) do
    case Map.get(state, key) do
      nil -> :miss
      value -> {:ok, value}
    end
  end

  @impl true
  def put(key, value, state), do: {:ok, Map.put(state, key, value)}

  @impl true
  def delete(key, state), do: :ok
end
```

### বোধগম্যতা এবং স্ট্রীম প্রক্রিয়াকরণ
```elixir
# For-comprehensions with filters and generators
result = for x <- 1..100,
              rem(x, 3) == 0,
              x > 10,
              do: x * x

# Multiple generators (cartesian product)
pairs = for x <- [1, 2, 3],
            y <- [:a, :b, :c],
            do: {x, y}

# Streams for lazy evaluation of large datasets
"large_file.txt"
|> File.stream!()
|> Stream.map(&String.trim/1)
|> Stream.filter(&(String.length(&1) > 0))
|> Stream.chunk_every(100)
|> Enum.each(&process_batch/1)

# Stream.resource for custom data sources
stream = Stream.resource(
  fn -> File.open!("data.csv") end,
  fn file ->
    case IO.read(file, :line) do
      :eof -> {:halt, file}
      line -> {[parse_line(line)], file}
    end
  end,
  fn file -> File.close(file) end
)
```


---

## সামঞ্জস্য এবং সমান্তরালতা
### BEAM VM প্রসেস
BEAM VM (Erlang এর ভার্চুয়াল মেশিন) লক্ষ লক্ষ লাইটওয়েট প্রসেস চালায়, প্রতিটির নিজস্ব স্তূপ রয়েছে।
```elixir
# Spawning processes
pid = spawn(fn ->
  receive do
    {:hello, name} -> IO.puts("Hello, #{name}!")
    :stop -> IO.puts("Stopping...")
  end
end)

send(pid, {:hello, "World"})  # "Hello, World!"
send(pid, :stop)              # "Stopping..."

# GenServer — the standard process pattern
defmodule KeyValueStore do
  use GenServer

  # Client API
  def start_link(initial \\ %{}) do
    GenServer.start_link(__MODULE__, initial, name: __MODULE__)
  end

  def get(key), do: GenServer.call(__MODULE__, {:get, key})
  def put(key, value), do: GenServer.cast(__MODULE__, {:put, key, value})
  def delete(key), do: GenServer.call(__MODULE__, {:delete, key})

  # Server callbacks
  @impl true
  def init(state), do: {:ok, state}

  @impl true
  def handle_call({:get, key}, _from, state) do
    {:reply, Map.get(state, key), state}
  end

  @impl true
  def handle_cast({:put, key, value}, state) do
    {:noreply, Map.put(state, key, value)}
  end

  @impl true
  def handle_call({:delete, key}, _from, state) do
    {:reply, :ok, Map.delete(state, key)}
  end
end

# Usage
KeyValueStore.start_link()
KeyValueStore.put(:name, "Alice")
KeyValueStore.get(:name)  # "Alice"
```

### OTP সুপারভাইজার গাছ
```elixir
defmodule AppSupervisor do
  use Supervisor

  def start_link(init_arg) do
    Supervisor.start_link(__MODULE__, init_arg, name: __MODULE__)
  end

  @impl true
  def init(_init_arg) do
    children = [
      # Worker that restarts on any crash
      {KeyValueStore, %{}},

      # Worker with custom restart strategy
      {DatabasePool, [size: 10, timeout: 5000]},

      # Supervisor for a subtree of processes
      {TaskSupervisor, name: MyApp.TaskSupervisor},

      # Temporary worker (never restarted)
      {OneTimeJob, [run_immediately: true]}
    ]

    # Strategy: :one_for_one restarts only the crashed child
    # :one_for_all restarts all children when one crashes
    # :rest_for_one restarts the crashed child and all children started after it
    Supervisor.init(children, strategy: :one_for_one,
      max_restarts: 5, max_seconds: 60)
  end
end
```

### টাস্ক এবং অ্যাসিঙ্ক/অপেক্ষা করুন
```elixir
# Fire-and-forget tasks
Task.start(fn -> IO.puts("Running in background") end)

# Async/await for concurrent work with results
task1 = Task.async(fn -> fetch_from_api("/users") end)
task2 = Task.async(fn -> fetch_from_api("/orders") end)
task3 = Task.async(fn -> fetch_from_api("/products") end)

# Wait for all results
results = [task1, task2, task3]
|> Task.await_many(10_000)  # 10 second timeout

# Task.supervised with timeout and error handling
result = Task.await(task1, 5_000)  # 5 second timeout

# Parallel map
items = 1..1000
results = items
|> Task.async_stream(&process_item/1, max_concurrency: 10, timeout: 5_000)
|> Enum.map(fn {:ok, result} -> result end)
```

### বিতরণ করা Erlang/Elixir
```elixir
# Start nodes with names
# Terminal 1: iex --sname node1@localhost
# Terminal 2: iex --sname node2@localhost

# Connect nodes
Node.connect(:node1@localhost)
Node.list()  # [:node1@localhost]

# Spawn on remote node
remote_pid = Node.spawn(:node1@localhost, fn ->
  IO.puts("Running on #{node()}")
  self()
end)

# Send messages across nodes
send(remote_pid, :hello)

# Distributed GenServer
# Register a process globally across the cluster
defmodule DistributedCounter do
  use GenServer

  def start_link do
    GenServer.start_link(__MODULE__, 0, name: {:global, __MODULE__})
  end

  def increment do
    :global.trans({__MODULE__, fn ->
      GenServer.call({:global, __MODULE__}, :inc)
    end}, [node()])
  end

  def handle_call(:inc, _from, count) do
    {:reply, count + 1, count + 1}
  end
end
```


---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (মিক্স)
```
my_elixir_app/
├── config/
│   ├── config.exs           # Base configuration
│   ├── dev.exs              # Development overrides
│   ├── prod.exs             # Production overrides
│   └── test.exs             # Test overrides
├── lib/
│   └── my_elixir_app/
│       ├── application.ex   # OTP Application module
│       ├── models/
│       │   └── user.ex
│       ├── services/
│       │   └── auth.ex
│       └── web/
│           ├── router.ex
│           ├── controllers/
│           └── views/
├── test/
│   ├── test_helper.exs
│   └── my_elixir_app/
│       └── services/
│           └── auth_test.exs
├── priv/
│   └── repo/
│       └── migrations/      # Database migrations
├── mix.exs                  # Project configuration
├── .formatter.exs           # Code formatter config
└── README.md
```

### মিক্স কনফিগারেশন (mix.exs)
```elixir
defmodule MyElixirApp.MixProject do
  use Mix.Project

  def project do
    [
      app: :my_elixir_app,
      version: "0.1.0",
      elixir: "~> 1.15",
      start_permanent: Mix.env() == :prod,
      deps: deps(),
      aliases: aliases(),
      dialyzer: [plt_add_apps: [:mix]],
      preferred_cli_env: [
        "test.watch": :test
      ]
    ]
  end

  def application do
    [
      extra_applications: [:logger, :runtime_tools],
      mod: {MyElixirApp.Application, []}
    ]
  end

  defp deps do
    [
      {:phoenix, "~> 1.7"},
      {:phoenix_live_view, "~> 0.20"},
      {:plug_cowboy, "~> 2.7"},
      {:ecto_sql, "~> 3.11"},
      {:postgrex, "~> 0.17"},
      {:jason, "~> 1.4"},
      {:mox, "~> 1.1", only: :test},
      {:ex_machina, "~> 2.7", only: :test},
      {:credo, "~> 1.7", only: [:dev, :test], runtime: false},
      {:dialyxir, "~> 1.4", only: [:dev, :test], runtime: false},
      {:ex_doc, "~> 0.31", only: :dev, runtime: false}
    ]
  end

  defp aliases do
    [
      setup: ["deps.get", "ecto.setup"],
      "ecto.setup": ["ecto.create", "ecto.migrate", "run priv/repo/seeds.exs"],
      "ecto.reset": ["ecto.drop", "ecto.setup"],
      test: ["ecto.create --quiet", "ecto.migrate --quiet", "test"]
    ]
  end
end
```

### কী মিক্স কমান্ড
| আদেশ | বর্ণনা |
|---------|---------------|
| `mix new my_app`| নতুন এলিক্সির প্রকল্প তৈরি করুন |
| `mix phx.new my_app`| নতুন ফিনিক্স ওয়েব অ্যাপ তৈরি করুন |
| `mix deps.get`| নির্ভরতা আনয়ন |
| `mix compile`| প্রকল্প কম্পাইল |
| `mix test`| পরীক্ষা চালান |
| `mix test --trace`| ভার্বোস আউটপুট দিয়ে পরীক্ষা চালান |
| `mix credo`| স্ট্যাটিক বিশ্লেষণ চালান |
| `mix dialyzer`| টাইপ চেকিং চালান |
| `mix format`| ফরম্যাট কোড |
| `mix docs`| ডকুমেন্টেশন তৈরি করুন |
| `mix release`| একটি মুক্তি তৈরি করুন |
| `iex -S mix`| প্রজেক্ট লোড করে REPL শুরু করুন |
### কোড ফরম্যাটার (.formatter.exs)
```elixir
# .formatter.exs
[
  inputs: ["{mix,.formatter}.exs", "{config,lib,test}/**/*.{ex,exs}"],
  line_length: 100,
  locals_without_parens: [
    get: 2, post: 2, put: 2, delete: 2,
    pipe_through: 1, plug: 1
  ]
]
```

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
```yaml
name: Elixir CI
on: [push, pull_request]
env:
  MIX_ENV: test

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
        ports: ['5432:5432']
    steps:
      - uses: actions/checkout@v4
      - uses: erlef/setup-beam@v1
        with:
          elixir-version: '1.15'
          otp-version: '26'
      - name: Cache deps
        uses: actions/cache@v3
        with:
          path: |
            deps
            _build
          key: mix-${{ hashFiles('mix.lock') }}
      - run: mix deps.get
      - run: mix compile --warnings-as-errors
      - run: mix format --check-formatted
      - run: mix credo --strict
      - run: mix test
```


---

## পরীক্ষা
### ExUnit — বিল্ট-ইন টেস্ট ফ্রেমওয়ার্ক
```elixir
defmodule MyElixirApp.MathTest do
  use ExUnit.Case, async: true

  describe "add/2" do
    test "adds two positive numbers" do
      assert MyElixirApp.Math.add(2, 3) == 5
    end

    test "handles negative numbers" do
      assert MyElixirApp.Math.add(-1, -2) == -3
    end
  end

  test "key-value store operations" do
    {:ok, pid} = KeyValueStore.start_link()
    KeyValueStore.put(pid, :name, "Alice")
    assert KeyValueStore.get(pid, :name) == "Alice"
    KeyValueStore.delete(pid, :name)
    assert KeyValueStore.get(pid, :name) == nil
  end
end
```

### স্ট্রিমডেটা — সম্পত্তি-ভিত্তিক পরীক্ষা
```elixir
defmodule MyElixirApp.PropertyTest do
  use ExUnit.Case
  use StreamData

  property "reverse is involutive" do
    check all list <- list_of(integer()) do
      assert list |> Enum.reverse() |> Enum.reverse() == list
    end
  end

  property "sort preserves length" do
    check all list <- list_of(integer(), min_length: 1) do
      assert length(Enum.sort(list)) == length(list)
    end
  end

  def user_generator do
    gen all name <- string(:alphanumeric, min_length: 1),
            age <- integer(0..150) do
      %{name: name, age: age}
    end
  end

  property "users have valid ages" do
    check all user <- user_generator() do
      assert user.age >= 0 and user.age <= 150
    end
  end
end
```

### মক্স — মকিং ফ্রেমওয়ার্ক
```elixir
defmodule WeatherBehaviour do
  @callback get_temperature(String.t()) :: {:ok, float()} | {:error, term()}
end

Mox.defmock(WeatherMock, for: WeatherBehaviour)

defmodule ForecastTest do
  use ExUnit.Case
  import Mox
  setup :verify_on_exit!

  test "displays temperature" do
    expect(WeatherMock, :get_temperature, fn "London" -> {:ok, 18.5} end)
    assert Forecast.display("London") == "Temperature: 18.5C"
  end
end
```


---

## ইন্টারঅপারেবিলিটি
### এরলাং পোর্ট এবং এনআইএফ (সি বাইন্ডিং)
```elixir
# NIF — call C from Elixir (compiled shared library)
defmodule ImageProcessor do
  @on_load :load_nif
  def load_nif do
    path = :filename.join(:code.priv_dir(:my_app), 'image_processor')
    :erlang.load_nif(path, 0)
  end
  def resize(_binary, _width, _height), do: :erlang.nif_error(:not_loaded)
  def compress(_binary, _quality), do: :erlang.nif_error(:not_loaded)
end

# Port — communicate with external process
defmodule ExternalWorker do
  def start do
    Port.open({:spawn, "python3 worker.py"}, [:binary, :exit_status])
  end
end
```

### Elixir-Erlang ইন্টারপ
```elixir
# Call any Erlang module directly from Elixir
:lists.sort([3, 1, 2])                      # [1, 2, 3]
:maps.merge(%{a: 1}, %{b: 2})               # %{a: 1, b: 2}
:erlang.system_time(:millisecond)            # current time in ms
:crypto.hash(:sha256, "secret") |> Base.encode16()
```

---

## ডিজাইন প্যাটার্ন
### জেনসার্ভার স্টেট মেশিন
```elixir
defmodule TrafficLight do
  use GenServer
  @transitions %{red: :green, green: :yellow, yellow: :red}
  @durations %{red: 30_000, green: 25_000, yellow: 5_000}

  def start_link(_opts), do: GenServer.start_link(__MODULE__, :red)
  def current_state(pid), do: GenServer.call(pid, :current)

  @impl true
  def init(state) do
    Process.send_after(self(), :transition, @durations[state])
    {:ok, state}
  end

  @impl true
  def handle_info(:transition, current) do
    next = @transitions[current]
    Process.send_after(self(), :transition, @durations[next])
    {:noreply, next}
  end

  @impl true
  def handle_call(:current, _from, state), do: {:reply, state, state}
end
```

### ফলাফলের ধরন সহ পাইপলাইন প্যাটার্ন
```elixir
defmodule OrderPipeline do
  def place_order(params) do
    {:ok, params}
    |> validate_items()
    |> validate_address()
    |> calculate_total()
    |> charge_payment()
    |> create_order_record()
  end

  defp validate_items({:ok, %{items: []}}), do: {:error, :validate, "No items"}
  defp validate_items({:ok, params}), do: {:ok, params}
  defp validate_items(err), do: err

  defp calculate_total({:ok, params}) do
    total = Enum.reduce(params.items, 0, fn item, acc ->
      acc + item.price * item.quantity
    end)
    {:ok, Map.put(params, :total, total)}
  end
  defp calculate_total(err), do: err

  defp charge_payment({:ok, %{total: total} = params}) do
    case Payment.charge(params.payment_method, total) do
      {:ok, tx_id} -> {:ok, Map.put(params, :transaction_id, tx_id)}
      {:error, reason} -> {:error, :payment, reason}
    end
  end
  defp charge_payment(err), do: err

  defp create_order_record({:ok, params}), do: {:ok, Orders.create(params)}
  defp create_order_record(err), do: err
end
```


---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
| টুল | উদ্দেশ্য | ব্যবহার |
|------|---------|-------|
| **:eprof** | ফাংশন-স্তরের প্রোফাইলিং | `:eprof.start()`তারপর প্রোফাইল |
| **:fprof** | বিস্তারিত কল গ্রাফ প্রোফাইলিং | `:fprof.profile(fn -> ... end)`|
| **:পর্যবেক্ষক** | ভিজ্যুয়াল সিস্টেম মনিটর |  IEx এ`:observer.start()`|
| **বেঞ্চি** | বেঞ্চমার্কিং লাইব্রেরি | deps যোগ করুন |
### বেঞ্চির সাথে বেঞ্চমার্কিং
```elixir
list = Enum.to_list(1..100_000)

Benchee.run(%{
  "Enum.map" => fn -> Enum.map(list, &(&1 * 2)) end,
  "Stream.map" => fn -> list |> Stream.map(&(&1 * 2)) |> Enum.to_list() end,
  "for comprehension" => fn -> for x <- list, do: x * 2 end
}, time: 5, memory_time: 2)
```

### অপ্টিমাইজেশন কৌশল
```elixir
# 1. Use iolists instead of string concatenation
good = ["Hello, ", name, "! You have ", Integer.to_string(count), " messages."]
IO.iodata_to_binary(good)

# 2. Use :ets for fast in-process key-value storage
:ets.new(:my_table, [:set, :public, :named_table])
:ets.insert(:my_table, {:key1, "value1"})
:ets.lookup(:my_table, :key1)

# 3. Prefer pattern matching over conditionals
# 4. Use binaries instead of charlists for strings
# 5. Use @compile inline for hot-path functions
```


---

## স্থাপনা
### মিক্স রিলিজ
```bash
MIX_ENV=prod mix release
_build/prod/rel/my_app/bin/my_app start
_build/prod/rel/my_app/bin/my_app daemon
_build/prod/rel/my_app/bin/my_app remote
```

### ডকার স্থাপনা
```dockerfile
FROM elixir:1.15-alpine AS builder
WORKDIR /app
RUN mix local.hex --force && mix local.rebar --force
COPY mix.exs mix.lock ./
RUN mix deps.get --only prod
COPY config config
COPY lib lib
COPY priv priv
RUN MIX_ENV=prod mix release

FROM alpine:3.18 AS app
RUN apk add --no-cache libstdc++ openssl ncurses-libs
WORKDIR /app
COPY --from=builder /app/_build/prod/rel/my_app ./
ENV PORT=4000
EXPOSE 4000
CMD ["bin/my_app", "start"]
```


---

## কখন Erlang/Elixir ব্যবহার করবেন
| দৃশ্যকল্প | কেন Erlang/Elexir | ভাল বিকল্প |
|------------|-------------------------------|
| রিয়েল-টাইম মেসেজিং / চ্যাট | এর জন্য তৈরি — WhatsApp, Discord use Erlang | যান, Node.js সহজ ক্ষেত্রে |
| লাইভ আপডেট সহ ওয়েব অ্যাপ্লিকেশন | ফিনিক্স লাইভভিউ ব্যতিক্রমী | ঐতিহ্যবাহী অ্যাপের জন্য রেল, জ্যাঙ্গো |
| বিতরণ ব্যবস্থা | স্থানীয় বন্টন, কোন অতিরিক্ত পরিকাঠামো নেই | যান, জাভা (আক্কা) |
| দোষ-সহনশীল সেবা | সুপারভাইজার গাছ স্বয়ংক্রিয়ভাবে ব্যর্থতা পরিচালনা করে | অবকাঠামো-স্তরের পুনরুদ্ধারের জন্য কুবারনেটস |
| IoT / এমবেডেড (এলিক্সির) | স্নায়ু প্ল্যাটফর্ম চমৎকার | সি, রিসোর্স সীমাবদ্ধ ডিভাইসের জন্য মরিচা |
| টেলিকম সিস্টেম | Erlang আক্ষরিক এই জন্য নির্মিত হয়েছিল | — |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
| মোবাইল অ্যাপস | উপযুক্ত নয় | সুইফট, কোটলিন, ডার্ট |
| সরল REST APIs | ছোট পরিষেবার জন্য সম্ভাব্য কিন্তু অতিমাত্রায় | Go, Node.js, Python |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: এরল্যাং এর "লেট ইট ক্র্যাশ" দর্শন কিভাবে কাজ করে?
**A:** প্রতিরক্ষামূলক প্রোগ্রামিংয়ের পরিবর্তে, Erlang প্রক্রিয়াগুলি ক্র্যাশ করতে দেয় এবং সুপারভাইজারদের মাধ্যমে সেগুলি পুনরায় চালু করতে দেয়:
```erlang
% Supervisor restarts crashed workers
{ok, Pid} = supervisor:start_link(my_sup, []),
% If a worker crashes, the supervisor restarts it automatically
% This is MORE reliable than trying to handle every error
```

### প্রশ্ন 2: এলিক্সির পাইপলাইন কিভাবে কাজ করে?
**A:**`|>`অপারেটর একটি ফাংশনের ফলাফলকে প্রথম আর্গুমেন্ট হিসেবে পরেরটিতে পাস করে:
```elixir
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
# "Hello World"
```

### প্রশ্ন 3: Erlang এবং Elixir এর মধ্যে পার্থক্য কি?
**A:** এলিক্সির আধুনিক সিনট্যাক্স সহ Erlang VM (BEAM) এ চলে:
- এলিক্সির: পাইপ অপারেটর, ম্যাক্রো, প্রোটোকল, স্ট্রিং ইন্টারপোলেশন
- Erlang: সহজ সিনট্যাক্স, OTP বিল্ট-ইন, আরও যুদ্ধ-পরীক্ষিত
- উভয়ই একই সঙ্গতি মডেল, VM এবং ইকোসিস্টেম ভাগ করে
### প্রশ্ন 4: জেনসার্ভার কিভাবে এলিক্সিরে কাজ করে?
**A:** GenServer হল স্টেটফুল প্রসেসের জন্য আদর্শ বিমূর্ততা:
```elixir
defmodule Counter do
  use GenServer
  def start_link(init), do: GenServer.start_link(__MODULE__, init, name: __MODULE__)
  def increment, do: GenServer.cast(__MODULE__, :inc)
  def value, do: GenServer.call(__MODULE__, :get)
  def init(val), do: {:ok, val}
  def handle_cast(:inc, n), do: {:noreply, n + 1}
  def handle_call(:get, _, n), do: {:reply, n, n}
end
```

### প্রশ্ন 5: আমি কীভাবে এলিক্সিরে ত্রুটিগুলি পরিচালনা করব?
**A:** ব্যতিক্রমের জন্য `try/rescue`, প্রত্যাশিত ব্যর্থতার জন্য`{:ok, result} | {:error, reason}`ব্যবহার করুন:
```elixir
case File.read("data.txt") do
  {:ok, content} -> process(content)
  {:error, :enoent} -> Logger.warning("File not found")
  {:error, reason} -> Logger.error("Failed: #{reason}")
end
```

---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি ত্রুটি-সহনশীল কী-ভ্যালু স্টোর তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি মূল-মূল্যের দোকান তৈরি করুন যা প্রক্রিয়া ক্র্যাশ থেকে বেঁচে যায়।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
একজন সুপারভাইজারের সাথে একটি GenServer ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```elixir
defmodule KVStore do
  use GenServer
  def start_link, do: GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  def put(key, val), do: GenServer.cast(__MODULE__, {:put, key, val})
  def get(key), do: GenServer.call(__MODULE__, {:get, key})
  def init(state), do: {:ok, state}
  def handle_cast({:put, k, v}, state), do: {:noreply, Map.put(state, k, v)}
  def handle_call({:get, k}, _, state), do: {:reply, Map.get(state, k), state}
end

# Supervisor
children = [{KVStore, []}]
Supervisor.start_link(children, strategy: :one_for_one)
```

**পদক্ষেপ 4: যাচাই করুন**
প্রক্রিয়াটি মেরে ফেলুন এবং যাচাই করুন যে এটি নতুন অবস্থায় পুনরায় আরম্ভ হয়েছে।
### সমস্যা 2: সমবর্তী ওয়েব স্ক্র্যাপার
**ধাপ 1: সমস্যাটি বুঝুন**
একযোগে একাধিক URL আনুন এবং ফলাফল সংগ্রহ করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
সমসাময়িক সম্পাদনের জন্য এলিক্সির টাস্ক ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```elixir
urls = ["https://example.com", "https://example.org", "https://example.net"]

tasks = Enum.map(urls, fn url ->
  Task.async(fn ->
    case HTTPoison.get(url) do
      {:ok, %HTTPoison.Response{status_code: 200, body: body}} ->
        {url, :ok, String.length(body)}
      {:ok, %HTTPoison.Response{status_code: code}} ->
        {url, :error, code}
      {:error, %HTTPoison.Error{reason: reason}} ->
        {url, :error, reason}
    end
  end)
end)

results = Task.await_many(tasks, 10_000)
```

**ধাপ ৪: অপ্টিমাইজ**
বড় ইউআরএল তালিকার জন্য হার সীমিত করা, পুনরায় চেষ্টা করা এবং স্ট্রিমিং যোগ করুন।
---

## সারাংশ
এরলাং এমন একটি সমস্যার সমাধান করেছে যা বেশিরভাগ ভাষা এখনও লড়াই করে: বিল্ডিং সিস্টেম যা কখনই নিচে পড়ে না। এর সমসাময়িক মডেল — লাইটওয়েট প্রসেস, মেসেজ পাসিং, "লেট ইট ক্র্যাশ" তত্ত্বাবধান — মূলধারার ভাষাগুলি এখন যা আবিষ্কার করছে তার থেকে কয়েক দশক এগিয়ে৷ এলিক্সির এরল্যাং-এর পরাশক্তিগুলি গ্রহণ করে এবং চমৎকার বিকাশকারী অভিজ্ঞতার সাথে আধুনিক সিনট্যাক্সে মোড়ানো। আপনি যদি রিয়েল-টাইম, ডিস্ট্রিবিউটেড, বা ত্রুটি-সহনশীল সিস্টেম তৈরি করেন, তাহলে Erlang/Elixir বিনিয়োগের যোগ্য। শেখার বক্ররেখাটি বাস্তব (কার্যকরী প্রোগ্রামিং, প্যাটার্ন ম্যাচিং, প্রক্রিয়া চিন্তা), কিন্তু অর্থপ্রদান হল এমন সফ্টওয়্যার যা থাকে এবং অনুমানযোগ্যভাবে স্কেল করে।