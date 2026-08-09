---
# मेटाडेटा
शीर्षक: "एरलांग और अमृत"
विवरण: "एरलांग और एलिक्सिर प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है, शामिल है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [एरलैंग-एंड-एलिक्सिर, प्रोग्रामिंग-भाषा, सिंटैक्स, इकोसिस्टम, कोडिंग-एंड-टेक्नोलॉजी]
कठिनाई_स्तर: "उन्नत"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का समय: "38 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
---
# एरलांग और अमृत
एर्लैंग को 1986 में एरिक्सन द्वारा टेलीफोन स्विच को पावर देने के लिए बनाया गया था - जो बताता है कि यह समवर्ती, दोष सहिष्णुता और वितरित सिस्टम को लगभग किसी भी चीज़ से बेहतर क्यों संभालता है। एर्लैंग प्रक्रियाएं हल्की, अलग-थलग हैं और केवल संदेश भेजने के माध्यम से संचार करती हैं। जब कोई प्रक्रिया क्रैश हो जाती है, तो पर्यवेक्षक उसे पुनः आरंभ करता है। यह "इसे क्रैश होने दो" दर्शन ऐसे सिस्टम तैयार करता है जो बिना डाउनटाइम के वर्षों तक चलते हैं।
एलिक्सिर एक आधुनिक भाषा है जो 2012 में जोस वालिम द्वारा एर्लैंग के वीएम (बीईएएम) के शीर्ष पर बनाई गई है। यह एरलांग द्वारा प्रदान की जाने वाली हर चीज को बरकरार रखता है - समवर्तीता, गलती सहनशीलता, वितरण - लेकिन एक अनुकूल वाक्यविन्यास, मेटाप्रोग्रामिंग और उत्कृष्ट टूलींग (मिक्स पैकेज मैनेजर, हेक्स पैकेज रजिस्ट्री) जोड़ता है। एलिक्सिर का व्यापक रूप से वेब अनुप्रयोगों (फीनिक्स फ्रेमवर्क के माध्यम से), रीयल-टाइम सिस्टम और एम्बेडेड डिवाइस (नर्व्स के माध्यम से) के लिए उपयोग किया जाता है।
---

## एर्लांग/एलिक्सिर क्यों मायने रखता है
- **समवर्ती मॉडल**: संदेश भेजने के साथ हल्की प्रक्रियाएं - कोई साझा स्थिति नहीं, कोई लॉक नहीं, कोई गतिरोध नहीं।
- **दोष सहनशीलता**: पर्यवेक्षक पेड़ स्वचालित रूप से दुर्घटनाग्रस्त प्रक्रियाओं को पुनः आरंभ करते हैं। सिस्टम त्रुटियों से शालीनता से उबर जाता है।
- **डिज़ाइन द्वारा वितरित**: एरलांग नोड्स मशीनों में पारदर्शी रूप से संचार करते हैं। समूहों के लिए निर्मित.
- **हॉट कोड रीलोडिंग**: बिना डाउनटाइम के चल रहे सिस्टम को अपडेट करें। टेलीकॉम और रीयल-टाइम ऐप्स के लिए महत्वपूर्ण।
- **नाइन नाइन अपटाइम**: एरलांग सिस्टम ने उत्पादन में 99.9999999% विश्वसनीयता हासिल की है।
- **फीनिक्स फ्रेमवर्क (एलिक्सिर)**: सबसे अधिक उत्पादक वेब फ्रेमवर्क में से एक, जिसमें वास्तविक समय के चैनल अंतर्निहित हैं।
- **लाइवव्यू (एलिक्सिर)**: जावास्क्रिप्ट लिखे बिना वेबसॉकेट कनेक्शन पर समृद्ध, वास्तविक समय वेब यूआई बनाएं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **केवल कार्यात्मक** | कोई परिवर्तनशील स्थिति नहीं, कोई ओओपी नहीं - तीव्र सीखने की अवस्था | अपरिवर्तनीयता को गले लगाओ; पैटर्न मिलान सशर्तों को प्रतिस्थापित करता है |
| **एरलैंग सिंटैक्स** | प्रोलॉग जैसा वाक्यविन्यास असामान्य और क्रियात्मक है | आधुनिक वाक्यविन्यास के लिए इसके स्थान पर अमृत का प्रयोग करें |
| **छोटा नौकरी बाज़ार** | पायथन, जावा, जावास्क्रिप्ट की तुलना में आला | विशिष्ट उद्योगों (दूरसंचार, फिनटेक, गेमिंग) में उच्च मांग |
| **पारिस्थितिकी तंत्र का आकार** | मुख्यधारा के पारिस्थितिकी तंत्र की तुलना में कम पुस्तकालय | एर्लांग के ओटीपी का लाभ उठाएं; हेक्स लगातार बढ़ रहा है |
| **यूआई के लिए नहीं** | कोई मूल GUI ढाँचा नहीं | बैकएंड के लिए उपयोग करें; फ्रंटएंड फ्रेमवर्क के साथ जोड़ी |
| **स्ट्रिंग हैंडलिंग** | एरलांग तार अजीब हैं (वर्ण या बायनेरिज़ की सूची) | एलिक्सिर में उत्कृष्ट स्ट्रिंग समर्थन है |
---

## अमृत सिंटेक्स
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

## एर्लांग सिंटैक्स (संदर्भ के लिए)
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

## प्रमुख पारिस्थितिकी तंत्र घटक
| घटक | विवरण |
|----|----|
| **ओटीपी** | ओपन टेलीकॉम प्लेटफ़ॉर्म - वितरित, दोष-सहिष्णु प्रणालियों के निर्माण के लिए युद्ध-परीक्षित ढांचा |
| **फ़ीनिक्स** | वास्तविक समय चैनलों और लाइवव्यू के साथ उत्पादक वेब ढांचा |
| **एक्टो** | डेटाबेस लाइब्रेरी और क्वेरी भाषा (जैसे ActiveRecord या SQLAlchemy) |
| **नसें** | Elixir के साथ एम्बेडेड IoT सिस्टम बनाएं |
| **RabbitMQ** | एर्लांग में लिखा गया संदेश ब्रोकर, लाखों कंपनियों द्वारा उपयोग किया जाता है |
| **काउचडीबी** | एर्लांग में लिखा गया दस्तावेज़ डेटाबेस |
| **व्हाट्सएप** | एर्लांग के समवर्ती मॉडल का उपयोग करके अरबों संदेश परोसता है |

---

## उन्नत सिंटैक्स और पैटर्न
### मैक्रोज़ के साथ मेटाप्रोग्रामिंग (एलिक्सिर)
एलिक्सिर मैक्रोज़ संकलन समय पर काम करते हैं, निष्पादन से पहले एएसटी को बदलते हैं।
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

### प्रोटोकॉल (अमृत के प्रकार वर्ग)
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

### व्यवहार (एरलांग/एलिक्सिर इंटरफेस)
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

### समझ और स्ट्रीम प्रोसेसिंग
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

## समवर्ती एवं समांतरता
### बीम वीएम प्रक्रियाएं
BEAM VM (एरलैंग की वर्चुअल मशीन) लाखों हल्की प्रक्रियाएं चलाती है, प्रत्येक का अपना ढेर होता है।
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

### ओटीपी पर्यवेक्षक पेड़
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

### कार्य और Async/प्रतीक्षा
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

### एर्लांग/अमृत वितरित किया गया
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (मिश्रित)
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

### मिक्स कॉन्फ़िगरेशन (mix.exs)
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

### कुंजी मिश्रण आदेश
| आदेश | विवरण |
|---------|-----------------|
|  __संरक्षित_0__ | नया अमृत प्रोजेक्ट बनाएं |
|  __संरक्षित_1__ | नया फीनिक्स वेब ऐप बनाएं |
|  __संरक्षित_2__ | निर्भरताएँ प्राप्त करें |
|  __संरक्षित_3__ | प्रोजेक्ट संकलित करें |
|  __संरक्षित_4__ | परीक्षण चलाएँ |
|  __संरक्षित_5__ | वर्बोज़ आउटपुट के साथ परीक्षण चलाएँ |
|  __संरक्षित_6__ | स्थैतिक विश्लेषण चलाएँ |
|  __संरक्षित_7__ | टाइप चेकिंग चलाएँ |
|  __संरक्षित_8__ | प्रारूप कोड |
|  __संरक्षित_9__ | दस्तावेज़ तैयार करें |
|  __संरक्षित_10__ | एक रिलीज बनाएं |
|  __संरक्षित_11__ | लोड किए गए प्रोजेक्ट के साथ आरईपीएल प्रारंभ करें |
### कोड फ़ॉर्मेटर (.formatter.exs)
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### एक्सयूनिट - बिल्ट-इन टेस्ट फ्रेमवर्क
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

### स्ट्रीमडेटा - संपत्ति-आधारित परीक्षण
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

### मोक्स - मॉकिंग फ्रेमवर्क
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

## अंतरसंचालनीयता
### एर्लांग पोर्ट और एनआईएफ (सी बाइंडिंग्स)
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

### एलिक्सिर-एरलांग इंटरऑप
```elixir
# Call any Erlang module directly from Elixir
:lists.sort([3, 1, 2])                      # [1, 2, 3]
:maps.merge(%{a: 1}, %{b: 2})               # %{a: 1, b: 2}
:erlang.system_time(:millisecond)            # current time in ms
:crypto.hash(:sha256, "secret") |> Base.encode16()
```

---

## डिज़ाइन पैटर्न
### जेनसर्वर स्टेट मशीन
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

### परिणाम प्रकार के साथ पाइपलाइन पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
| उपकरण | उद्देश्य | उपयोग |
|------|------|-------|
| **:एप्रोफ़** | फ़ंक्शन-स्तरीय प्रोफ़ाइलिंग | `:eprof.start()`फिर प्रोफ़ाइल |
| **:fprof** | विस्तृत कॉल ग्राफ़ प्रोफ़ाइलिंग |  __संरक्षित_1__ |
| **:पर्यवेक्षक** | विजुअल सिस्टम मॉनिटर |  IEx में`:observer.start()`|
| **बेंची** | बेंचमार्किंग लाइब्रेरी | डिप्स में जोड़ें |
### बेंची के साथ बेंचमार्किंग
```elixir
list = Enum.to_list(1..100_000)

Benchee.run(%{
  "Enum.map" => fn -> Enum.map(list, &(&1 * 2)) end,
  "Stream.map" => fn -> list |> Stream.map(&(&1 * 2)) |> Enum.to_list() end,
  "for comprehension" => fn -> for x <- list, do: x * 2 end
}, time: 5, memory_time: 2)
```

### अनुकूलन तकनीकें
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

## तैनाती
### मिक्स रिलीज़
```bash
MIX_ENV=prod mix release
_build/prod/rel/my_app/bin/my_app start
_build/prod/rel/my_app/bin/my_app daemon
_build/prod/rel/my_app/bin/my_app remote
```

### डॉकर परिनियोजन
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

## एर्लांग/एलिक्सिर का उपयोग कब करें
| परिदृश्य | एर्लांग/एलिक्सिर क्यों | बेहतर विकल्प |
|---|-------------------|-----|
| वास्तविक समय संदेश/चैट | इसके लिए निर्मित - व्हाट्सएप, डिस्कॉर्ड एर्लैंग का उपयोग करते हैं | सरल मामलों के लिए Node.js पर जाएं |
| लाइव अपडेट के साथ वेब एप्लिकेशन | फीनिक्स लाइवव्यू असाधारण है | पारंपरिक ऐप्स के लिए रेल्स, Django |
| वितरित सिस्टम | मूल वितरण, कोई अतिरिक्त बुनियादी ढांचा नहीं | जाओ, जावा (अक्का) |
| दोष-सहिष्णु सेवाएँ | पर्यवेक्षक वृक्ष विफलताओं को स्वचालित रूप से संभालते हैं | बुनियादी ढांचे-स्तर की पुनर्प्राप्ति के लिए कुबेरनेट्स |
| IoT/एम्बेडेड (अमृत) | तंत्रिका मंच उत्कृष्ट है | सी, संसाधन-विवश उपकरणों के लिए जंग |
| दूरसंचार प्रणाली | एरलांग वस्तुतः इसी के लिए बनाया गया था | — |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
| मोबाइल ऐप्स | अनुकूल नहीं | स्विफ्ट, कोटलिन, डार्ट |
| सरल REST API | संभव लेकिन छोटी सेवाओं के लिए जरूरत से ज्यादा | जाओ, नोड.जेएस, पायथन |
---

## सारांश
एरलांग ने उस समस्या का समाधान किया जिससे अधिकांश भाषाएँ अभी भी जूझती हैं: ऐसी प्रणालियाँ बनाना जो कभी ख़राब न हों। इसका समवर्ती मॉडल - हल्की प्रक्रियाएं, संदेश भेजना, "इसे क्रैश होने दें" पर्यवेक्षण - मुख्यधारा की भाषाएं जो अब खोज रही हैं, उससे दशकों आगे है। एलिक्सिर एरलांग की महाशक्तियों को लेता है और उन्हें उत्कृष्ट डेवलपर अनुभव के साथ आधुनिक वाक्यविन्यास में लपेटता है। यदि आप वास्तविक समय, वितरित, या दोष-सहिष्णु प्रणाली का निर्माण कर रहे हैं, तो एर्लांग/एलिक्सिर निवेश के लायक है। सीखने की अवस्था वास्तविक है (कार्यात्मक प्रोग्रामिंग, पैटर्न मिलान, प्रक्रिया सोच), लेकिन भुगतान सॉफ्टवेयर है जो पूर्वानुमानित रूप से ऊपर रहता है और बढ़ता है।