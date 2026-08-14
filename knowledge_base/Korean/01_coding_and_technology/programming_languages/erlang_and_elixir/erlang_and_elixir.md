---
# Metadata
title: "Erlang & Elixir"
description: "Comprehensive reference for the Erlang and Elixir programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# 얼랭 & 엘릭서
Erlang은 1986년 Ericsson이 전화 스위치에 전원을 공급하기 위해 제작했습니다. 이는 Erlang이 다른 어떤 것보다 동시성, 내결함성 및 분산 시스템을 더 잘 처리하는 이유를 설명합니다. Erlang 프로세스는 가볍고 격리되어 있으며 메시지 전달을 통해서만 통신합니다. 프로세스가 충돌하면 감독자가 프로세스를 다시 시작합니다. 이러한 "충돌하자"라는 철학은 다운타임 없이 수년 동안 실행되는 시스템을 생산합니다.
Elixir는 2012년 Jose Valim이 Erlang의 VM(BEAM)을 기반으로 구축한 최신 언어입니다. 동시성, 내결함성, 배포 등 Erlang이 제공하는 모든 기능을 유지하면서도 친숙한 구문, 메타프로그래밍 및 뛰어난 도구(혼합 패키지 관리자, Hex 패키지 레지스트리)를 추가합니다. Elixir는 웹 애플리케이션(Phoenix 프레임워크를 통해), 실시간 시스템 및 임베디드 장치(Nerves를 통해)에 널리 사용됩니다.
---

## 얼랭/엘릭서가 중요한 이유
- **동시성 모델**: 메시지 전달이 포함된 경량 프로세스 — 공유 상태 없음, 잠금 없음, 교착 상태 없음.
- **내결함성**: 감독자 트리가 충돌이 발생한 프로세스를 자동으로 다시 시작합니다. 시스템은 오류로부터 정상적으로 복구됩니다.
- **설계에 따른 분산**: Erlang 노드는 시스템 간에 투명하게 통신합니다. 클러스터용으로 구축되었습니다.
- **핫 코드 다시 로드**: 가동 중지 시간 없이 실행 중인 시스템을 업데이트합니다. 통신 및 실시간 앱에 중요합니다.
- **9999999999%의 가동 시간**: Erlang 시스템은 생산에서 99.9999999%의 신뢰성을 달성했습니다.
- **Phoenix 프레임워크(Elixir)**: 실시간 채널이 내장되어 있어 가장 생산적인 웹 프레임워크 중 하나입니다.
- **LiveView(Elixir)**: JavaScript를 작성하지 않고도 WebSocket 연결을 통해 풍부한 실시간 웹 UI를 구축할 수 있습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **기능 전용** | 변경 가능한 상태 없음, OOP 없음 — 가파른 학습 곡선 | 불변성을 수용하십시오. 패턴 일치가 조건문을 대체합니다 |
| **Erlang 구문** | 프롤로그와 유사한 구문이 특이하고 장황합니다. | 현대적인 구문을 위해 대신 Elixir를 사용하세요 |
| **소규모 취업 시장** | Python, Java, JavaScript와 비교한 틈새 시장 | 특정 산업(통신, 핀테크, 게임)의 높은 수요 |
| **생태계 규모** | 주류 생태계보다 적은 수의 라이브러리 | Erlang의 OTP를 활용하세요. 꾸준히 성장하는 16진수 |
| **UI용 아님** | 기본 GUI 프레임워크 없음 | 백엔드에 사용합니다. 프론트엔드 프레임워크와 페어링 |
| **문자열 처리** | Erlang 문자열이 어색함(문자 또는 바이너리 목록) | Elixir는 탁월한 문자열 지원을 제공합니다 |
---

## 엘릭서 구문
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

## Erlang 구문(참고용)
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

## 주요 생태계 구성 요소
| 구성요소 | 설명 |
|------------|-------------|
| **OTP** | 개방형 통신 플랫폼 — 분산형 내결함성 시스템 구축을 위한 검증된 프레임워크 |
| **피닉스** | 실시간 채널과 LiveView를 갖춘 생산적인 웹 프레임워크 |
| **엑토** | 데이터베이스 라이브러리 및 쿼리 언어(예: ActiveRecord 또는 SQLAlchemy) |
| **신경** | Elixir로 임베디드 IoT 시스템 구축 |
| **RabbitMQ** | 수백만 개의 회사에서 사용되는 Erlang으로 작성된 메시지 브로커 |
| **카우치DB** | Erlang으로 작성된 문서 데이터베이스 |
| **왓츠앱** | Erlang의 동시성 모델을 사용하여 수십억 개의 메시지 제공 |

---

## 고급 구문 및 패턴
### 매크로를 사용한 메타프로그래밍(Elixir)
Elixir 매크로는 컴파일 타임에 작동하여 실행 전에 AST를 변환합니다.
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

### 프로토콜 (Elixir의 유형 클래스)
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

### 동작(Erlang/Elixir 인터페이스)
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

### 이해 및 스트림 처리
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

## 동시성 및 병렬성
### BEAM VM 프로세스
BEAM VM(Erlang의 가상 머신)은 각각 자체 힙이 있는 수백만 개의 경량 프로세스를 실행합니다.
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

### OTP 감독자 트리
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

### 작업 및 비동기/대기
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

### 분산 얼랭/엘릭서
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조(혼합)
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

### 믹스 구성(mix.exs)
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

### 키 혼합 명령
| 명령 | 설명 |
|---------|-------------|
| `mix new my_app`| 새로운 Elixir 프로젝트 생성 |
| `mix phx.new my_app`| 새로운 Phoenix 웹 앱 만들기 |
| `mix deps.get`| 종속성 가져오기 |
| `mix compile`| 프로젝트 컴파일 |
| `mix test`| 테스트 실행 |
| `mix test --trace`| 자세한 출력으로 테스트 실행 |
| `mix credo`| 정적 분석 실행 |
| `mix dialyzer`| 유형 검사 실행 |
| `mix format`| 형식 코드 |
| `mix docs`| 문서 생성 |
| `mix release`| 릴리스 빌드 |
| `iex -S mix`| 프로젝트가 로드된 상태에서 REPL 시작 |
### 코드 포맷터(.formatter.exs)
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

### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### ExUnit — 내장 테스트 프레임워크
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

### StreamData - 속성 기반 테스트
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

### Mox — 모의 프레임워크
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

## 상호 운용성
### Erlang 포트 및 NIF(C 바인딩)
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

### Elixir-Erlang 상호 운용성
```elixir
# Call any Erlang module directly from Elixir
:lists.sort([3, 1, 2])                      # [1, 2, 3]
:maps.merge(%{a: 1}, %{b: 2})               # %{a: 1, b: 2}
:erlang.system_time(:millisecond)            # current time in ms
:crypto.hash(:sha256, "secret") |> Base.encode16()
```

---

## 디자인 패턴
### GenServer 상태 머신
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

### 결과 유형이 있는 파이프라인 패턴
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

## 성능 및 최적화
### 프로파일링 도구
| 도구 | 목적 | 사용법 |
|------|---------|-------|
| **:eprof** | 기능 수준 프로파일링 | `:eprof.start()`후 프로필 |
| **:fprof** | 상세한 호출 그래프 프로파일링 | `:fprof.profile(fn -> ... end)`|
| **:관찰자** | 시각적 시스템 모니터 |  IEx의`:observer.start()`|
| **벤치** | 벤치마킹 라이브러리 | 뎁스에 추가 |
### Benchee를 사용한 벤치마킹
```elixir
list = Enum.to_list(1..100_000)

Benchee.run(%{
  "Enum.map" => fn -> Enum.map(list, &(&1 * 2)) end,
  "Stream.map" => fn -> list |> Stream.map(&(&1 * 2)) |> Enum.to_list() end,
  "for comprehension" => fn -> for x <- list, do: x * 2 end
}, time: 5, memory_time: 2)
```

### 최적화 기술
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

## 배포
### 믹스 릴리스
```bash
MIX_ENV=prod mix release
_build/prod/rel/my_app/bin/my_app start
_build/prod/rel/my_app/bin/my_app daemon
_build/prod/rel/my_app/bin/my_app remote
```

### 도커 배포
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

## Erlang/Elixir를 사용해야 하는 경우
| 시나리오 | 왜 얼랭/엘릭서인가 | 더 나은 대안 |
|----------|------|------|
| 실시간 메시징/채팅 | 이를 위해 제작됨 — WhatsApp, Discord는 Erlang | 더 간단한 경우에는 Go, Node.js |
| 실시간 업데이트가 포함된 웹 애플리케이션 | Phoenix LiveView는 예외적입니다 | 기존 앱을 위한 Rails, Django |
| 분산 시스템 | 기본 배포, 추가 인프라 없음 | 자바(아카) |
| 내결함성 서비스 | 감독자 트리는 오류를 자동으로 처리합니다 | 인프라 수준 복구를 위한 Kubernetes |
| IoT/임베디드(Elixir) | Nerves 플랫폼은 훌륭합니다 | C, 리소스가 제한된 장치를 위한 Rust |
| 통신 시스템 | Erlang은 말 그대로 이를 위해 만들어졌습니다 | — |
| 데이터 과학 / ML | 생태계가 아니다 | 파이썬, R |
| 모바일 앱 | 적합하지 않음 | 스위프트, 코틀린, 다트 |
| 간단한 REST API | 소규모 서비스에는 가능하지만 과잉 | Go, Node.js, Python |
---

## 종합 Q&A
### Q1: Erlang의 "Let it crash" 철학은 어떻게 작동하나요?
**답:** 방어적인 프로그래밍 대신 Erlang은 프로세스가 충돌하고 감독자를 통해 다시 시작되도록 합니다.
```erlang
% Supervisor restarts crashed workers
{ok, Pid} = supervisor:start_link(my_sup, []),
% If a worker crashes, the supervisor restarts it automatically
% This is MORE reliable than trying to handle every error
```

### Q2: Elixir 파이프라인은 어떻게 작동하나요?
**A:**`|>`연산자는 한 함수의 결과를 다음 인수의 첫 번째 인수로 전달합니다.
```elixir
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
# "Hello World"
```

### Q3: 얼랭과 엘릭서의 차이점은 무엇인가요?
**답:** Elixir는 최신 구문을 사용하여 Erlang VM(BEAM)에서 실행됩니다.
- Elixir: 파이프 연산자, 매크로, 프로토콜, 문자열 보간
- Erlang: 더 간단한 구문, OTP 내장, 더 많은 전투 테스트를 거침
- 둘 다 동일한 동시성 모델, VM 및 생태계를 공유합니다.
### Q4: GenServer는 Elixir에서 어떻게 작동하나요?
**답:** GenServer는 상태 저장 프로세스에 대한 표준 추상화입니다.
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

### Q5: Elixir에서 오류를 어떻게 처리하나요?
**A:** 예외에는 `try/rescue`를 사용하고, 예상되는 오류에는 `{:ok, result} | {:error, reason}`를 사용하세요.
```elixir
case File.read("data.txt") do
  {:ok, content} -> process(content)
  {:error, :enoent} -> Logger.warning("File not found")
  {:error, reason} -> Logger.error("Failed: #{reason}")
end
```

---

## 사고 사슬 문제 해결
### 문제 1: 내결함성 키-값 저장소 구축
**1단계: 문제 이해**
프로세스 충돌에도 살아남는 키-값 저장소를 만듭니다.
**2단계: 접근 방식 파악**
감독자와 함께 GenServer를 사용하십시오.
**3단계: 구현**```elixir
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

**4단계: 확인**
프로세스를 종료하고 새로운 상태로 다시 시작되는지 확인합니다.
### 문제 2: 동시 웹 스크레이퍼
**1단계: 문제 이해**
여러 URL을 동시에 가져오고 결과를 수집합니다.
**2단계: 접근 방식 파악**
동시 실행을 위해 Elixir Tasks를 사용하세요.
**3단계: 구현**```elixir
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

**4단계: 최적화**
대규모 URL 목록에 대한 속도 제한, 재시도 및 스트리밍을 추가합니다.
---

## 요약
Erlang은 대부분의 언어가 여전히 어려움을 겪고 있는 문제, 즉 절대 다운되지 않는 시스템 구축 문제를 해결했습니다. 동시성 모델(경량 프로세스, 메시지 전달, "충돌 허용" 감독)은 주류 언어가 이제서야 발견한 것보다 수십 년 앞서 있습니다. Elixir는 Erlang의 초능력을 뛰어난 개발자 경험과 함께 현대적인 구문으로 포장합니다. 실시간, 분산 또는 내결함성 시스템을 구축하는 경우 Erlang/Elixir는 투자할 가치가 있습니다. 학습 곡선은 실제적이지만(기능적 프로그래밍, 패턴 일치, 프로세스 사고), 그에 따른 보상은 유지되고 예측 가능하게 확장되는 소프트웨어입니다.