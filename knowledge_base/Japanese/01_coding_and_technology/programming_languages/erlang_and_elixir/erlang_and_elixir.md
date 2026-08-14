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

# Erlang と Elixir
Erlang は、電話交換機に電力を供給するために 1986 年にエリクソンによって構築されました。これが、Erlang が他のほとんどの製品よりも並行性、フォールト トレランス、分散システムをうまく処理できる理由を説明しています。 Erlang プロセスは軽量で独立しており、メッセージ パッシングを通じてのみ通信します。プロセスがクラッシュすると、スーパーバイザがプロセスを再起動します。この「クラッシュさせる」という哲学により、ダウンタイムなしで何年も稼働するシステムが生み出されます。
Elixir は、2012 年に Jose Valim によって Erlang の VM (BEAM) 上に構築された最新言語です。Erlang が提供するすべてのもの (同時実行性、フォールト トレランス、分散) はそのままに、使いやすい構文、メタプログラミング、優れたツール (Mix パッケージ マネージャー、Hex パッケージ レジストリ) が追加されています。 Elixir は、Web アプリケーション (Phoenix フレームワーク経由)、リアルタイム システム、組み込みデバイス (Nerves 経由) に広く使用されています。
---

## Erlang/Elixir が重要な理由
- **同時実行モデル**: メッセージ パッシングを備えた軽量プロセス - 共有状態、ロック、デッドロックはありません。
- **フォールト トレランス**: スーパーバイザー ツリーは、クラッシュしたプロセスを自動的に再起動します。システムはエラーから正常に回復します。
- **設計により分散**: Erlang ノードはマシン間で透過的に通信します。クラスター用に構築されています。
- **ホットコードのリロード**: ダウンタイムなしで実行中のシステムを更新します。通信およびリアルタイム アプリにとって重要です。
- **ナインナインの稼働時間**: Erlang システムは、運用環境で 99.9999999% の信頼性を達成しました。
- **Phoenix フレームワーク (Elixir)**: リアルタイム チャネルが組み込まれた、最も生産的な Web フレームワークの 1 つ。
- **LiveView (Elixir)**: JavaScript を記述せずに、WebSocket 接続を介してリッチなリアルタイム Web UI を構築します。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **機能のみ** |変更可能な状態も OOP もありません — 急峻な学習曲線 |不変性を受け入れます。パターン マッチングで条件文を置き換える |
| **Erlang 構文** |プロローグのような構文は珍しく、冗長です。最新の構文には代わりに Elixir を使用してください。
| **小規模な雇用市場** | Python、Java、JavaScript と比較したニッチ |特定の業界 (テレコム、フィンテック、ゲーム) での高い需要 |
| **生態系のサイズ** |主流のエコシステムよりライブラリが少ない | Erlang の OTP を活用します。順調に成長するヘックス |
| **UI 用ではありません** |ネイティブ GUI フレームワークなし |バックエンドに使用します。フロントエンドフレームワークと組み合わせる |
| **文字列の処理** | Erlang の文字列は厄介です (文字またはバイナリのリスト)。 Elixir は優れた文字列サポートを備えています。
---

## エリクサーの構文
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

## Erlang 構文 (参考)
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

## 主要なエコシステムのコンポーネント
|コンポーネント |説明 |
|----------|---------------|
| **OTP** |オープンテレコムプラットフォーム — 分散型フォールトトレラントシステムを構築するための、歴戦のフレームワーク |
| **フェニックス** |リアルタイム チャネルと LiveView を備えた生産的な Web フレームワーク |
| **エクト** |データベース ライブラリとクエリ言語 (ActiveRecord や SQLAlchemy など) |
| **神経** | Elixir を使用して組み込み IoT システムを構築する |
| **ウサギMQ** | Erlang で書かれたメッセージ ブローカー。何百万もの企業で使用されています。
| **CouchDB** | Erlang で書かれたドキュメント データベース |
| **WhatsApp** | Erlang の同時実行モデルを使用して数十億のメッセージを処理 |

---

## 高度な構文とパターン
### マクロを使用したメタプログラミング (Elixir)
Elixir マクロはコンパイル時に動作し、実行前に AST を変換します。
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

### プロトコル (Elixir の型クラス)
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

### 動作 (Erlang/Elixir インターフェイス)
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

### 内包表記とストリーム処理
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

## 同時実行性と並列処理
### BEAM VM プロセス
BEAM VM (Erlang の仮想マシン) は、それぞれが独自のヒープを持つ数百万の軽量プロセスを実行します。
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

### OTP スーパーバイザ ツリー
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

### タスクと非同期/待機
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

### 分散 Erlang/Elixir
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

## プロジェクトの構成とシステムの構築
### プロジェクト構造 (混合)
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

### ミックス構成 (mix.exs)
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

### キーミックスコマンド
|コマンド |説明 |
|----------|---------------|
| `mix new my_app`|新しい Elixir プロジェクトを作成する |
| `mix phx.new my_app`|新しい Phoenix Web アプリを作成する |
| `mix deps.get`|依存関係を取得する |
| `mix compile`|プロジェクトをコンパイルする |
| `mix test`|テストを実行する |
| `mix test --trace`|詳細な出力でテストを実行する |
| `mix credo`|静的解析を実行する |
| `mix dialyzer`|タイプチェックを実行する |
| `mix format`|フォーマットコード |
| `mix docs`|ドキュメントを生成する |
| `mix release`|リリースをビルドする |
| `iex -S mix`|プロジェクトがロードされた状態で REPL を開始 |
### コードフォーマッタ (.formatter.exs)
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

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### ExUnit — 組み込みテスト フレームワーク
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

### StreamData — プロパティベースのテスト
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

### Mox — モックフレームワーク
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

## 相互運用性
### Erlang ポートと NIF (C バインディング)
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

### Elixir-Erlang 相互運用性
```elixir
# Call any Erlang module directly from Elixir
:lists.sort([3, 1, 2])                      # [1, 2, 3]
:maps.merge(%{a: 1}, %{b: 2})               # %{a: 1, b: 2}
:erlang.system_time(:millisecond)            # current time in ms
:crypto.hash(:sha256, "secret") |> Base.encode16()
```

---

## デザインパターン
### GenServer ステート マシン
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

### 結果タイプを使用したパイプライン パターン
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

## パフォーマンスと最適化
### プロファイリングツール
|ツール |目的 |使い方 |
|------|-------|------|
| **:eprof** |機能レベルのプロファイリング | `:eprof.start()`プロフィール |
| **:fprof** |詳細なコールグラフプロファイリング | `:fprof.profile(fn -> ... end)`|
| **:観察者** |ビジュアルシステムモニター |  IEx の`:observer.start()`|
| **ベンチ** |ベンチマークライブラリ |デプスに追加 |
### Benchee によるベンチマーク
```elixir
list = Enum.to_list(1..100_000)

Benchee.run(%{
  "Enum.map" => fn -> Enum.map(list, &(&1 * 2)) end,
  "Stream.map" => fn -> list |> Stream.map(&(&1 * 2)) |> Enum.to_list() end,
  "for comprehension" => fn -> for x <- list, do: x * 2 end
}, time: 5, memory_time: 2)
```

### 最適化手法
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

## デプロイメント
### ミックスリリース
```bash
MIX_ENV=prod mix release
_build/prod/rel/my_app/bin/my_app start
_build/prod/rel/my_app/bin/my_app daemon
_build/prod/rel/my_app/bin/my_app remote
```

### Docker のデプロイメント
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

## Erlang/Elixir を使用する場合
|シナリオ | Erlang/Elixir を選ぶ理由 |より良い代替案 |
|----------|-------------------|--------|
|リアルタイムメッセージング/チャット |このために構築 — WhatsApp、Discord は Erlang を使用 |簡単な場合は Node.js を使用してください |
|ライブアップデートを備えた Web アプリケーション | Phoenix LiveView は格別です |従来のアプリ用の Rails、Django |
|分散システム |ネイティブ配布、追加のインフラストラクチャは不要 |ゴー、ジャワ (アッカ) |
|フォールトトレラントサービス |スーパーバイザ ツリーは障害を自動的に処理します。インフラストラクチャレベルのリカバリのための Kubernetes |
| IoT / 組み込み (Elixir) |神経プラットフォームは優れています | C、リソースに制約のあるデバイス向けの Rust |
|通信システム | Erlang は文字通りこのために構築されました。 — |
|データ サイエンス / ML |エコシステムではありません |パイソン、R |
|モバイルアプリ |適さない | Swift、Kotlin、Dart |
|シンプルな REST API |可能ですが、小規模なサービスには過剰です | Go、Node.js、Python |
---

## 総合的な Q&A
### Q1: Erlang の「クラッシュさせる」哲学はどのように機能しますか?
**A:** Erlang は防御的なプログラミングの代わりに、プロセスをクラッシュさせ、スーパーバイザ経由で再起動させます。
```erlang
% Supervisor restarts crashed workers
{ok, Pid} = supervisor:start_link(my_sup, []),
% If a worker crashes, the supervisor restarts it automatically
% This is MORE reliable than trying to handle every error
```

### Q2: Elixir パイプラインはどのように機能しますか?
**A:**`|>`演算子は、ある関数の結果を最初の引数として次の関数に渡します。
```elixir
"hello world"
|> String.split()
|> Enum.map(&String.capitalize/1)
|> Enum.join(" ")
# "Hello World"
```

### Q3: Erlang と Elixir の違いは何ですか?
**A:** Elixir は、最新の構文を使用して Erlang VM (BEAM) 上で実行されます。
- Elixir: パイプ演算子、マクロ、プロトコル、文字列補間
- Erlang: よりシンプルな構文、OTP ビルトイン、より実戦テスト済み
- どちらも同じ同時実行モデル、VM、エコシステムを共有します
### Q4: GenServer は Elixir でどのように動作しますか?
**A:** GenServer はステートフル プロセスの標準抽象化です。
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

### Q5: Elixir でのエラーはどのように処理すればよいですか?
**A:** 例外には`try/rescue`を使用し、予想される失敗には`{:ok, result} | {:error, reason}`を使用します。
```elixir
case File.read("data.txt") do
  {:ok, content} -> process(content)
  {:error, :enoent} -> Logger.warning("File not found")
  {:error, reason} -> Logger.error("Failed: #{reason}")
end
```

---

## 思考連鎖による問題解決
### 問題 1: フォールトトレラントなキー/値ストアの構築
**ステップ 1: 問題を理解する**
プロセスがクラッシュしても存続するキーと値のストアを作成します。
**ステップ 2: アプローチを特定する**
スーパーバイザとともに GenServer を使用します。
**ステップ 3: 実装**```elixir
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

**ステップ 4: 確認**
プロセスを強制終了し、新しい状態で再起動することを確認します。
### 問題 2: 同時 Web スクレイパー
**ステップ 1: 問題を理解する**
複数の URL を同時にフェッチし、結果を収集します。
**ステップ 2: アプローチを特定する**
同時実行には Elixir タスクを使用します。
**ステップ 3: 実装**```elixir
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

**ステップ 4: 最適化**
大規模な URL リストに対してレート制限、再試行、ストリーミングを追加します。
---

＃＃ まとめ
Erlang は、ほとんどの言語が依然として抱えている、ダウンしないシステムの構築という問題を解決しました。その同時実行モデル (軽量プロセス、メッセージ パッシング、「クラッシュさせる」監視) は、主流の言語が現在発見し始めているものよりも数十年先を行っています。 Elixir は Erlang のスーパーパワーを利用し、優れた開発者エクスペリエンスを備えた最新の構文でラップします。リアルタイム システム、分散システム、またはフォールト トレラント システムを構築している場合、Erlang/Elixir は投資する価値があります。学習曲線は現実のもの (関数型プログラミング、パターン マッチング、プロセス思考) ですが、その見返りはソフトウェアが稼働し続け、予測どおりに拡張できることです。