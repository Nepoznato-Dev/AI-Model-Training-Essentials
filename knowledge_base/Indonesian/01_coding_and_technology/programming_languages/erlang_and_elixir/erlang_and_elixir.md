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

#Erlang & Elixir
Erlang dibangun oleh Ericsson pada tahun 1986 untuk menggerakkan saklar telepon — yang menjelaskan mengapa Erlang menangani konkurensi, toleransi kesalahan, dan sistem terdistribusi lebih baik daripada apa pun. Proses Erlang ringan, terisolasi, dan berkomunikasi hanya melalui penyampaian pesan. Ketika suatu proses terhenti, supervisor memulai ulang proses tersebut. Filosofi “biarkan crash” ini menghasilkan sistem yang dapat berjalan bertahun-tahun tanpa downtime.
Elixir adalah bahasa modern yang dibangun di atas VM Erlang (BEAM) oleh Jose Valim pada tahun 2012. Elixir mempertahankan semua yang ditawarkan Erlang — konkurensi, toleransi kesalahan, distribusi — tetapi menambahkan sintaksis yang ramah, metaprogramming, dan perkakas yang sangat baik (Manajer paket campuran, registri paket Hex). Elixir banyak digunakan untuk aplikasi web (melalui kerangka Phoenix), sistem real-time, dan perangkat tertanam (melalui Saraf).
---

## Mengapa Erlang/Elixir Penting
- **Model konkurensi**: Proses ringan dengan penyampaian pesan — tanpa status bersama, tanpa kunci, tanpa kebuntuan.
- **Toleransi kesalahan**: Pohon supervisor secara otomatis memulai ulang proses yang mogok. Sistem pulih dari kesalahan dengan baik.
- **Didistribusikan berdasarkan desain**: Node Erlang berkomunikasi secara transparan antar mesin. Dibangun untuk cluster.
- **Pemuatan ulang kode panas**: Perbarui sistem yang berjalan tanpa waktu henti. Penting untuk telekomunikasi dan aplikasi real-time.
- **Waktu aktif sembilan sembilan**: Sistem Erlang telah mencapai keandalan 99,9999999% dalam produksi.
- **Kerangka Phoenix (Elixir)**: Salah satu kerangka web paling produktif, dengan saluran real-time bawaan.
- **LiveView (Elixir)**: Membangun UI web yang kaya dan real-time melalui koneksi WebSocket tanpa menulis JavaScript.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Hanya fungsional** | Tidak ada keadaan yang bisa berubah, tidak ada OOP — kurva pembelajaran yang curam | Rangkullah kekekalan; pencocokan pola menggantikan kondisional |
| **Sintaks Erlang** | Sintaks mirip prolog tidak biasa dan bertele-tele | Gunakan Elixir sebagai pengganti sintaksis modern |
| **Pasar kerja yang lebih kecil** | Niche dibandingkan dengan Python, Java, JavaScript | Permintaan yang tinggi di industri tertentu (telekomunikasi, fintech, game) |
| **Ukuran ekosistem** | Lebih sedikit perpustakaan dibandingkan ekosistem arus utama | Manfaatkan OTP Erlang; Hex terus berkembang |
| **Bukan untuk UI** | Tidak ada kerangka GUI asli | Gunakan untuk backend; berpasangan dengan kerangka kerja frontend |
| **Penanganan string** | String Erlang canggung (daftar karakter atau binari) | Elixir memiliki dukungan string yang sangat baik |
---

## Sintaks Ramuan
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

## Sintaks Erlang (untuk referensi)
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

## Komponen Ekosistem Utama
| Komponen | Deskripsi |
|-----------|-------------|
| **OTP** | Platform Telekomunikasi Terbuka — kerangka kerja yang telah teruji untuk membangun sistem yang terdistribusi dan toleran terhadap kesalahan |
| **Phoenix** | Kerangka web produktif dengan saluran real-time dan LiveView |
| **Ekto** | Pustaka database dan bahasa kueri (seperti ActiveRecord atau SQLAlchemy) |
| **Saraf** | Bangun sistem IoT tertanam dengan Elixir |
| **KelinciMQ** | Broker pesan yang ditulis dalam bahasa Erlang, digunakan oleh jutaan perusahaan |
| **CouchDB** | Basis data dokumen ditulis dalam Erlang |
| **WhatsApp** | Melayani miliaran pesan menggunakan model konkurensi Erlang |

---

## Sintaks & Pola Tingkat Lanjut
### Metaprogramming dengan Makro (Elixir)
Makro Elixir beroperasi pada waktu kompilasi, mengubah AST sebelum dieksekusi.
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

### Protokol (Kelas Tipe Elixir)
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

### Perilaku (Antarmuka Erlang/Elixir)
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

### Pemahaman dan Pemrosesan Aliran
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

## Konkurensi & Paralelisme
### Proses BEAM VM
BEAM VM (mesin virtual Erlang) menjalankan jutaan proses ringan, masing-masing dengan heapnya sendiri.
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

### Pohon Pengawas OTP
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

### Tugas dan Async/Menunggu
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

### Mendistribusikan Erlang/Elixir
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

## Konfigurasi Proyek & Sistem Pembangunan
### Struktur Proyek (Campuran)
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

### Konfigurasi Campuran (mix.exs)
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

### Perintah Campuran Kunci
| Perintah | Deskripsi |
|---------|-------------|
| `mix new my_app`| Buat proyek Elixir baru |
| `mix phx.new my_app`| Buat aplikasi web Phoenix baru |
| `mix deps.get`| Ambil dependensi |
| `mix compile`| Kompilasi proyek |
| `mix test`| Jalankan tes |
| `mix test --trace`| Jalankan pengujian dengan keluaran verbose |
| `mix credo`| Jalankan analisis statis |
| `mix dialyzer`| Jalankan pemeriksaan tipe |
| `mix format`| Kode format |
| `mix docs`| Hasilkan dokumentasi |
| `mix release`| Buat rilis |
| `iex -S mix`| Mulai REPL dengan proyek dimuat |
### Pemformat Kode (.formatter.exs)
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

### Saluran CI/CD (Tindakan GitHub)
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

## Pengujian
### ExUnit — Kerangka Uji Bawaan
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

### StreamData — Pengujian Berbasis Properti
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

### Mox — Kerangka Mengejek
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

## Interoperabilitas
### Port Erlang dan NIF (Pengikatan C)
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

## Pola Desain
### Mesin Status GenServer
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

### Pola Alur dengan Tipe Hasil
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

## Kinerja & Optimasi
### Alat Pembuatan Profil
| Alat | Tujuan | Penggunaan |
|------|---------|-------|
| **:eprof** | Pembuatan profil tingkat fungsi | `:eprof.start()`lalu profil |
| **:fprof** | Pembuatan profil grafik panggilan terperinci | `:fprof.profile(fn -> ... end)`|
| **:pengamat** | Monitor sistem visual | `:observer.start()`di IEx |
| **Meja** | Pustaka pembandingan | Tambahkan ke deps |
### Membandingkan dengan Benchee
```elixir
list = Enum.to_list(1..100_000)

Benchee.run(%{
  "Enum.map" => fn -> Enum.map(list, &(&1 * 2)) end,
  "Stream.map" => fn -> list |> Stream.map(&(&1 * 2)) |> Enum.to_list() end,
  "for comprehension" => fn -> for x <- list, do: x * 2 end
}, time: 5, memory_time: 2)
```

### Teknik Optimasi
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

## Penerapan
### Rilis Campuran
```bash
MIX_ENV=prod mix release
_build/prod/rel/my_app/bin/my_app start
_build/prod/rel/my_app/bin/my_app daemon
_build/prod/rel/my_app/bin/my_app remote
```

### Penerapan Docker
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

## Kapan Menggunakan Erlang/Elixir
| Skenario | Mengapa Erlang/Elixir | Alternatif Lebih Baik |
|----------|-------------------|-------------------|
| Pesan / obrolan waktu nyata | Dibuat untuk ini — WhatsApp, Discord menggunakan Erlang | Buka, Node.js untuk kasus yang lebih sederhana |
| Aplikasi web dengan pembaruan langsung | Phoenix LiveView luar biasa | Rails, Django untuk aplikasi tradisional |
| Sistem terdistribusi | Distribusi asli, tanpa infrastruktur tambahan | Pergi, Jawa (Akka) |
| Layanan toleransi kesalahan | Pohon supervisor menangani kegagalan secara otomatis | Kubernetes untuk pemulihan tingkat infrastruktur |
| IoT / tertanam (Elixir) | Platform saraf sangat bagus | C, Rust untuk perangkat dengan sumber daya terbatas |
| Sistem telekomunikasi | Erlang benar-benar dibangun untuk ini | — |
| Ilmu data / ML | Bukan ekosistem | Piton, R |
| Aplikasi seluler | Tidak cocok | Cepat, Kotlin, Dart |
| API REST Sederhana | Mungkin tapi berlebihan untuk layanan kecil | Buka, Node.js, Python |
---

## Ringkasan
Erlang memecahkan masalah yang masih dihadapi sebagian besar bahasa: membangun sistem yang tidak pernah mati. Model konkurensinya — proses yang ringan, penyampaian pesan, pengawasan "biarkan crash" — berpuluh-puluh tahun lebih maju dari apa yang baru ditemukan oleh bahasa-bahasa umum saat ini. Elixir mengambil kekuatan super Erlang dan membungkusnya dalam sintaksis modern dengan pengalaman pengembang yang luar biasa. Jika Anda membangun sistem real-time, terdistribusi, atau sistem yang toleran terhadap kesalahan, Erlang/Elixir layak untuk diinvestasikan. Kurva pembelajarannya nyata (pemrograman fungsional, pencocokan pola, proses berpikir), namun imbalannya adalah perangkat lunak yang tetap bertahan dan berkembang dengan skala yang dapat diprediksi.