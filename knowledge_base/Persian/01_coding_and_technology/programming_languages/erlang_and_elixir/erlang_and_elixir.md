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

#ارلنگ و اکسیر
Erlang توسط اریکسون در سال 1986 برای تامین برق سوئیچ های تلفن ساخته شد - که توضیح می دهد که چرا همزمان، تحمل خطا و سیستم های توزیع شده را تقریباً بهتر از هر چیز دیگری مدیریت می کند. فرآیندهای Erlang سبک وزن هستند، ایزوله هستند و فقط از طریق ارسال پیام ارتباط برقرار می کنند. هنگامی که یک فرآیند از کار می افتد، یک سرپرست آن را دوباره راه اندازی می کند. این فلسفه "بگذار خراب شود" سیستم هایی را تولید می کند که سال ها بدون توقف کار می کنند.
Elixir یک زبان مدرن است که بر روی ماشین مجازی Erlang (BEAM) توسط Jose Valim در سال 2012 ساخته شده است. این زبان همه چیزهایی را که Erlang ارائه می دهد حفظ می کند - همزمانی، تحمل خطا، توزیع - اما یک نحو دوستانه، فرابرنامه نویسی و ابزار عالی (Mix package manager، Hex Registry Package) را اضافه می کند. Elixir به طور گسترده برای برنامه های کاربردی وب (از طریق چارچوب Phoenix)، سیستم های بلادرنگ و دستگاه های تعبیه شده (از طریق Nerves) استفاده می شود.
---

## چرا Erlang/Elixir مهم است
- **مدل همزمان**: فرآیندهای سبک با ارسال پیام - بدون حالت مشترک، بدون قفل، بدون بن بست.
- **تحمل خطا**: درختان ناظر به طور خودکار فرآیندهای خراب شده را مجدداً راه اندازی می کنند. سیستم ها از خطاها به خوبی بازیابی می شوند.
- **توزیع بر اساس طراحی**: گره های Erlang به طور شفاف بین ماشین ها ارتباط برقرار می کنند. برای خوشه ها ساخته شده است.
- **بارگذاری مجدد کد داغ**: سیستم های در حال اجرا را بدون خرابی به روز رسانی کنید. برای برنامه های مخابراتی و بلادرنگ حیاتی است.
- **Nine nines uptime **: سیستم های Erlang به 99.9999999% قابلیت اطمینان در تولید دست یافته اند.
- **فریم ورک ققنوس (Elixir)**: یکی از پربازده ترین فریم ورک های وب، با کانال های بی درنگ داخلی.
- **LiveView (Elixir)**: ایجاد رابط های وب غنی و بی درنگ از طریق اتصالات WebSocket بدون نوشتن جاوا اسکریپت.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **فقط کاربردی** | بدون حالت قابل تغییر، بدون OOP — منحنی یادگیری شیب دار | تغییر ناپذیری را در آغوش بگیرید. تطبیق الگو جایگزین شرطی ها می شود |
| ** نحو ارلنگ ** | نحو پرولوگ مانند غیر معمول و پرمخاطب است | به جای آن از Elixir برای نحو مدرن استفاده کنید |
| **بازار کار کوچکتر** | طاقچه در مقایسه با پایتون، جاوا، جاوا اسکریپت | تقاضای بالا در صنایع خاص (تلکام، فین تک، بازی) |
| **اندازه اکوسیستم** | کتابخانه های کمتر از اکوسیستم های جریان اصلی | اهرم OTP Erlang. هگز به طور پیوسته در حال رشد |
| **برای رابط کاربری نیست** | بدون چارچوب بومی رابط کاربری گرافیکی | استفاده برای backends. جفت شدن با فریم ورک های فرانت اند |
| **دستکاری رشته** | رشته های Erlang بی دست و پا هستند (لیست کاراکترها یا باینری ها) | اکسیر دارای ساپورت رشته عالی است |
---

## نحو اکسیر
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

## نحو Erlang (برای مرجع)
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

## اجزای کلیدی اکوسیستم
| جزء | توضیحات |
|-----------|-------------|
| **OTP** | Open Telecom Platform — چارچوب آزمایش شده نبرد برای ساختن سیستم های توزیع شده و مقاوم در برابر خطا |
| **ققنوس** | چارچوب وب مولد با کانال های بلادرنگ و LiveView |
| **اکتو** | کتابخانه پایگاه داده و زبان پرس و جو (مانند ActiveRecord یا SQLAlchemy) |
| **اعصاب** | ساخت سیستم های اینترنت اشیا تعبیه شده با Elixir |
| **RabbitMQ** | کارگزار پیام نوشته شده در Erlang، مورد استفاده میلیون ها شرکت |
| **CouchDB** | پایگاه داده اسناد نوشته شده در Erlang |
| **واتس اپ** | میلیاردها پیام را با استفاده از مدل همزمانی ارلنگ ارائه می دهد

---

## نحو و الگوهای پیشرفته
### فرابرنامه‌نویسی با ماکرو (اکسیر)
ماکروهای اکسیر در زمان کامپایل عمل می کنند و AST را قبل از اجرا تغییر می دهند.
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

### پروتکل ها (کلاس های نوع اکسیر)
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

### رفتارها (رابط Erlang/Elixir)
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

### درک و پردازش جریان
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

## همزمانی و موازی
### فرآیندهای BEAM VM
BEAM VM (ماشین مجازی Erlang) میلیون ها فرآیند سبک وزن را اجرا می کند که هر کدام دارای پشته های خاص خود هستند.
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

### OTP Supervisor Trees
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

### Task و Async/Await
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

### ارلنگ/اکسیر توزیع شده
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (ترکیب)
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

### پیکربندی مخلوط (mix.exs)
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

### دستورات Key Mix
| فرمان | توضیحات |
|---------|-------------|
| `mix new my_app`| ایجاد پروژه جدید اکسیر |
| `mix phx.new my_app`| ایجاد اپلیکیشن وب جدید فونیکس |
| `mix deps.get`| واکشی وابستگی ها |
| `mix compile`| کامپایل پروژه |
| `mix test`| اجرای تست ها |
| `mix test --trace`| تست ها را با خروجی پرمخاطب اجرا کنید |
| `mix credo`| اجرای تجزیه و تحلیل استاتیک |
| `mix dialyzer`| اجرای بررسی نوع |
| `mix format`| کد قالب |
| `mix docs`| ایجاد مستندات |
| `mix release`| ساخت نسخه |
| `iex -S mix`| شروع REPL با پروژه بارگذاری شده |
### فرمتگر کد (.formatter.exs)
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### ExUnit - چارچوب تست داخلی
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

### StreamData - تست مبتنی بر ویژگی
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

### Mox - چارچوب تمسخر آمیز
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

## قابلیت همکاری
### درگاه Erlang و NIF (C Bindings)
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

### Elixir-Erlang Interop
```elixir
# Call any Erlang module directly from Elixir
:lists.sort([3, 1, 2])                      # [1, 2, 3]
:maps.merge(%{a: 1}, %{b: 2})               # %{a: 1, b: 2}
:erlang.system_time(:millisecond)            # current time in ms
:crypto.hash(:sha256, "secret") |> Base.encode16()
```

---

## الگوهای طراحی
### GenServer State Machine
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

### الگوی خط لوله با نوع نتیجه
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
| ابزار | هدف | استفاده |
|------|---------|-------|
| **:eprof** | پروفایل در سطح عملکرد | `:eprof.start()`سپس نمایه |
| **:fprof** | نمایه گراف فراخوان دقیق | `:fprof.profile(fn -> ... end)`|
| **:ناظر** | مانیتور سیستم بصری | `:observer.start()`در IEx |
| **بنچی** | کتابخانه معیار | افزودن به deps |
### محک زدن با Benchee
```elixir
list = Enum.to_list(1..100_000)

Benchee.run(%{
  "Enum.map" => fn -> Enum.map(list, &(&1 * 2)) end,
  "Stream.map" => fn -> list |> Stream.map(&(&1 * 2)) |> Enum.to_list() end,
  "for comprehension" => fn -> for x <- list, do: x * 2 end
}, time: 5, memory_time: 2)
```

### تکنیک های بهینه سازی
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

## استقرار
### انتشار مخلوط
```bash
MIX_ENV=prod mix release
_build/prod/rel/my_app/bin/my_app start
_build/prod/rel/my_app/bin/my_app daemon
_build/prod/rel/my_app/bin/my_app remote
```

### استقرار داکر
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

## چه زمانی از Erlang/Elixir استفاده کنیم
| سناریو | چرا ارلنگ/اکسیر | جایگزین بهتر |
|------------------------------------------------------------------|
| پیام رسانی بلادرنگ / چت | ساخته شده برای این - WhatsApp، Discord از Erlang | برو، Node.js برای موارد ساده تر |
| برنامه های وب با به روز رسانی زنده | Phoenix LiveView استثنایی است | Rails, Django برای برنامه های سنتی |
| سیستم های توزیع شده | توزیع بومی، بدون زیرساخت اضافی | برو، جاوا (Akka) |
| خدمات مقاوم در برابر خطا | درختان ناظر به طور خودکار خرابی ها را مدیریت می کنند | Kubernetes برای بازیابی در سطح زیرساخت |
| اینترنت اشیا / تعبیه شده (Elixir) | پلت فرم اعصاب عالی است | ج، زنگ برای دستگاه‌های با محدودیت منابع |
| سیستم های مخابراتی | Erlang به معنای واقعی کلمه برای این ساخته شد | — |
| علم داده / ML | نه اکوسیستم | پایتون، R |
| برنامه های موبایل | مناسب نیست | سویفت، کاتلین، دارت |
| API های REST ساده | ممکن است اما بیش از حد برای خدمات کوچک | برو، Node.js، پایتون |
---

## پرسش و پاسخ مصنوعی
### Q1: فلسفه ارلنگ "بگذار خراب شود" چگونه کار می کند؟
**A:** به جای برنامه نویسی تدافعی، Erlang اجازه می دهد تا پردازش ها از کار بیفتند و آنها را از طریق سرپرستان راه اندازی مجدد کند:
```erlang
% Supervisor restarts crashed workers
{ok, Pid} = supervisor:start_link(my_sup, []),
% If a worker crashes, the supervisor restarts it automatically
% This is MORE reliable than trying to handle every error
```

### Q2: خطوط لوله اکسیر چگونه کار می کنند؟
**A:** عملگر`|>`نتیجه یک تابع را به عنوان اولین آرگومان به آرگومان بعدی منتقل می کند:
```elixir
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
# "Hello World"
```

### Q3: تفاوت ارلنگ و اکسیر چیست؟
**A:** Elixir روی Erlang VM (BEAM) با نحو مدرن اجرا می شود:
- اکسیر: اپراتور لوله، ماکروها، پروتکل ها، درون یابی رشته ها
- Erlang: نحو ساده تر، OTP داخلی، بیشتر آزمایش شده در نبرد
- هر دو مدل همزمان، VM و اکوسیستم یکسانی دارند
### Q4: GenServers چگونه در Elixir کار می کند؟
**A:** GenServer انتزاع استاندارد برای فرآیندهای حالت است:
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

### Q5: چگونه خطاهای اکسیر را کنترل کنم؟
**A:** از`try/rescue`برای استثناء، از`{:ok, result} | {:error, reason}`برای خرابی های مورد انتظار استفاده کنید:
```elixir
case File.read("data.txt") do
  {:ok, content} -> process(content)
  {:error, :enoent} -> Logger.warning("File not found")
  {:error, reason} -> Logger.error("Failed: #{reason}")
end
```

---

## حل مسئله زنجیره ای از فکر
### مشکل 1: ساختن فروشگاهی با ارزش کلیدی مقاوم به خطا
**مرحله 1: مشکل را درک کنید**
یک فروشگاه با ارزش کلیدی ایجاد کنید که از خرابی فرآیندها جان سالم به در ببرد.
**مرحله 2: رویکرد را شناسایی کنید**
از GenServer با سرپرست استفاده کنید.
**مرحله 3: پیاده سازی **```elixir
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

**مرحله 4: تایید **
روند را بکشید و بررسی کنید که با حالت تازه شروع مجدد شود.
### مشکل 2: اسکراپر همزمان وب
**مرحله 1: مشکل را درک کنید**
چندین URL را به طور همزمان واکشی کنید و نتایج را جمع آوری کنید.
**مرحله 2: رویکرد را شناسایی کنید**
برای اجرای همزمان از Elixir Tasks استفاده کنید.
**مرحله 3: پیاده سازی **```elixir
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

**مرحله 4: بهینه سازی**
برای فهرست‌های URL بزرگ، محدودیت نرخ، تلاش‌های مجدد و پخش را اضافه کنید.
---

## خلاصه
Erlang مشکلی را حل کرد که بیشتر زبان ها هنوز با آن دست و پنجه نرم می کنند: ساختن سیستم هایی که هرگز از بین نمی روند. مدل همزمانی آن - فرآیندهای سبک، ارسال پیام، نظارت "بگذار خراب شود" - دهه ها جلوتر از آنچه زبان های جریان اصلی اکنون کشف می کنند است. Elixir قدرت‌های فوق‌العاده Erlang را می‌گیرد و آنها را در نحو مدرن با تجربه توسعه‌دهنده عالی قرار می‌دهد. اگر در حال ساختن سیستم های بلادرنگ، توزیع شده یا مقاوم در برابر خطا هستید، Erlang/Elixir ارزش سرمایه گذاری را دارد. منحنی یادگیری واقعی است (برنامه نویسی عملکردی، تطبیق الگو، تفکر فرآیند)، اما بازده آن نرم افزاری است که بالا می ماند و به طور قابل پیش بینی مقیاس می شود.