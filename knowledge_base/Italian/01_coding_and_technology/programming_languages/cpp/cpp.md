---
# Metadata
title: "C++"
description: "Comprehensive reference for the C++ programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [cpp, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "31 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#C++
C++ è un linguaggio di programmazione compilato di uso generale creato da Bjarne Stroustrup, rilasciato per la prima volta nel 1985. Estende il C con funzionalità orientate agli oggetti, generici e, nelle versioni moderne (C++11 e successive), astrazioni di alto livello come lambda, puntatori intelligenti e Standard Template Library (STL). Il C++ segue il principio dell'"astrazione zero-overhead": non dovresti pagare per le funzionalità che non usi.
C++ è il linguaggio da scegliere quando sono necessarie prestazioni elevate e potenza espressiva. Alimenta motori di gioco (Unreal Engine), browser (Chrome, Firefox), database (MongoDB), sistemi operativi (parti di Windows e macOS), sistemi di trading finanziario e simulazioni in tempo reale.
---

## Perché il C++ è importante
- **Prestazioni con espressività**: velocità quasi C con classi, modelli e astrazioni moderne.
- **Principio zero-overhead**: le astrazioni vengono compilate nello stesso codice che scriveresti a mano in C.
- **Enorme codebase**: decenni di infrastrutture critiche: giochi, browser, database, sistemi integrati.
- **Multiparadigma**: supporta stili di programmazione procedurali, orientati agli oggetti, generici e funzionali.
- **Distruzione deterministica**: RAII garantisce che le risorse vengano ripulite in modo prevedibile: nessuna pausa nel garbage collector.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Complessità** | Il linguaggio è enorme – nemmeno gli esperti lo conoscono tutto | Attenersi al moderno C++ (C++17/20); evitare modelli legacy |
| **Sicurezza della memoria** | Gestione manuale della memoria; puntatori pendenti, perdite, UB | Utilizza puntatori intelligenti, RAII e std::opzionale |
| **Tempi di compilazione** | La compilazione di progetti di grandi dimensioni può richiedere alcuni minuti | Intestazioni precompilate, moduli (C++20), build incrementali |
| **Messaggi di errore** | Gli errori del modello possono essere lunghi centinaia di righe | Utilizzare static_assert, concetti (C++20), compilatori migliori |
| **Compatibilità binaria** | Instabilità ABI tra le versioni del compilatore | Interfacce C stabili per librerie condivise |
---

## Fondamenti di sintassi
### Struttura di base
```cpp
#include <iostream>
#include <string>
#include <vector>

int add(int a, int b) { return a + b; }

int main() {
    std::string name = "World";
    std::cout << "Hello, " << name << "!\n";

    std::vector<int> numbers = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int n : numbers) { sum += n; }
    std::cout << "Sum: " << sum << "\n";
    return 0;
}
```

### Classi e programmazione orientata agli oggetti
```cpp
#include <iostream>
#include <string>
#include <memory>

class Animal {
public:
    explicit Animal(std::string name) : name_(std::move(name)) {}
    virtual ~Animal() = default;
    virtual std::string speak() const = 0;
    std::string name() const { return name_; }
private:
    std::string name_;
};

class Dog : public Animal {
public:
    explicit Dog(std::string name) : Animal(std::move(name)) {}
    std::string speak() const override { return name() + " says woof"; }
};

class Cat : public Animal {
public:
    explicit Cat(std::string name) : Animal(std::move(name)) {}
    std::string speak() const override { return name() + " says meow"; }
};

int main() {
    auto dog = std::make_unique<Dog>("Rex");
    auto cat = std::make_shared<Cat>("Whiskers");
    std::cout << dog->speak() << "\n";
    std::cout << cat->speak() << "\n";
    std::unique_ptr<Animal> animal = std::make_unique<Dog>("Buddy");
    std::cout << animal->speak() << "\n";
    return 0;
}
```

### Modelli (programmazione generica)
```cpp
template<typename T>
T maximum(T a, T b) { return (a > b) ? a : b; }

template<typename T, size_t N>
class Array {
public:
    T& operator[](size_t index) {
        if (index >= N) throw std::out_of_range("Out of bounds");
        return data_[index];
    }
    constexpr size_t size() const { return N; }
private:
    T data_[N];
};

int main() {
    std::cout << maximum(3, 7) << "\n";
    std::cout << maximum(3.14, 2.72) << "\n";
    Array<int, 5> arr;
    arr[0] = 42;
    return 0;
}
```

### Funzionalità moderne del C++ (C++17/20)
```cpp
#include <optional>
#include <variant>
#include <algorithm>
#include <numeric>

auto x = 42;              // int
auto pi = 3.14;           // double
auto greet = [](const std::string& name) { return "Hello, " + name; };

// Structured bindings (C++17)
std::map<std::string, int> ages = {{"Alice", 30}, {"Bob", 25}};
for (const auto& [name, age] : ages) {
    std::cout << name << " is " << age << "\n";
}

// std::optional
std::optional<int> find_index(const std::vector<int>& v, int target) {
    for (size_t i = 0; i < v.size(); i++)
        if (v[i] == target) return i;
    return std::nullopt;
}

// Lambda expressions
std::vector<int> nums = {5, 2, 8, 1, 9, 3};
std::sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });
auto sum = std::accumulate(nums.begin(), nums.end(), 0);
```

---

## La libreria standard
### Contenitori
| Contenitore | Digitare | Utilizzare quando |
|-----------|------|----------|
| std::vettore | Array dinamico | Scelta predefinita per dati sequenziali |
| std::deque | Coda a doppia estremità | È necessario inserire/cancellare rapidamente su entrambe le estremità |
| std::elenco | Elenco doppiamente collegato | Inserimento/cancellazione frequente al centro |
| std::mappa | Mappa dell'albero ordinata | Sono necessarie chiavi ordinate, ricerca O(log n) |
| std::unordered_map | Mappa hash | Ricerca media veloce O(1) |
| std::imposta | Set ordinato | Elementi ordinati unici |
| std::array | Array a dimensione fissa | Dimensione nota allocata nello stack in fase di compilazione |
| std::stringa | Testo | Usa sempre questo, mai raw char* |
### Puntatori intelligenti
```cpp
// unique_ptr -- exclusive ownership, zero overhead
auto resource = std::make_unique<DatabaseConnection>("localhost");

// shared_ptr -- shared ownership, reference counted
auto config = std::make_shared<AppConfig>();
auto copy = config;  // Both point to same object

// weak_ptr -- non-owning observer
std::weak_ptr<AppConfig> observer = config;
if (auto locked = observer.lock()) {
    // Object still alive
}
```

### Algoritmi
```cpp
std::vector<int> v = {5, 2, 8, 1, 9, 3, 7, 4, 6};
std::sort(v.begin(), v.end());
auto it = std::find(v.begin(), v.end(), 7);
bool exists = std::binary_search(v.begin(), v.end(), 7);

std::vector<int> doubled(v.size());
std::transform(v.begin(), v.end(), doubled.begin(), [](int x) { return x * 2; });

std::vector<int> evens;
std::copy_if(v.begin(), v.end(), std::back_inserter(evens),
             [](int x) { return x % 2 == 0; });
```

---

## Sintassi e modelli avanzati
### Concetti (C++20)
```cpp
#include <concepts>

// Define a concept
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

template<typename T>
concept Printable = requires(T t) {
    { std::cout << t } -> std::same_as<std::ostream&>;
};

// Constrained function template
Numeric auto add(Numeric auto a, Numeric auto b) {
    return a + b;
}

// Constrained class template
template<Printable T>
class Wrapper {
    T value;
public:
    explicit Wrapper(T v) : value(std::move(v)) {}
    void print() const { std::cout << value << "\n"; }
};
```

### Sposta la semantica e RAII
```cpp
class Buffer {
    std::unique_ptr<int[]> data_;
    size_t size_;
public:
    // Constructor
    explicit Buffer(size_t size) : data_(std::make_unique<int[]>(size)), size_(size) {}

    // Move constructor
    Buffer(Buffer&& other) noexcept : data_(std::move(other.data_)), size_(other.size_) {
        other.size_ = 0;
    }

    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        data_ = std::move(other.data_);
        size_ = other.size_;
        other.size_ = 0;
        return *this;
    }

    // Delete copy (exclusive ownership)
    Buffer(const Buffer&) = delete;
    Buffer& operator=(const Buffer&) = delete;

    ~Buffer() = default;  // unique_ptr handles cleanup
};

Buffer create_buffer() {
    return Buffer(1024);  // Move semantics, no copy
}
```

### Gerarchia delle eccezioni personalizzata
```cpp
#include <stdexcept>
#include <string>

class AppError : public std::runtime_error {
public:
    explicit AppError(const std::string& msg) : std::runtime_error(msg) {}
};

class NetworkError : public AppError {
    int status_code_;
public:
    NetworkError(int code, const std::string& msg)
        : AppError("Network " + std::to_string(code) + ": " + msg),
          status_code_(code) {}
    int status_code() const { return status_code_; }
};

class ValidationError : public AppError {
    std::string field_;
public:
    ValidationError(const std::string& field, const std::string& msg)
        : AppError(field + ": " + msg), field_(field) {}
    const std::string& field() const { return field_; }
};

// Usage
try {
    throw NetworkError(404, "Not Found");
} catch (const NetworkError& e) {
    std::cerr << "HTTP " << e.status_code() << ": " << e.what() << "\n";
} catch (const AppError& e) {
    std::cerr << "App error: " << e.what() << "\n";
}
```

---

## Concorrenza e parallelismo
### std::thread e sincronizzazione
```cpp
#include <thread>
#include <mutex>
#include <shared_mutex>
#include <condition_variable>
#include <vector>
#include <iostream>

// Mutex-based thread safety
class ThreadSafeCounter {
    int count_ = 0;
    mutable std::mutex mtx_;
public:
    void increment() {
        std::lock_guard<std::mutex> lock(mtx_);
        count_++;
    }
    int get() const {
        std::lock_guard<std::mutex> lock(mtx_);
        return count_;
    }
};

int main() {
    ThreadSafeCounter counter;
    std::vector<std::thread> threads;

    for (int i = 0; i < 10; i++) {
        threads.emplace_back([&counter]() {
            for (int j = 0; j < 1000; j++) counter.increment();
        });
    }
    for (auto& t : threads) t.join();
    std::cout << "Count: " << counter.get() << "\n";  // 10000
}
```

### Asincrono, futuri e promesse
```cpp
#include <future>
#include <iostream>

// std::async -- launch asynchronous tasks
int compute(int x) {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return x * x;
}

int main() {
    auto future1 = std::async(std::launch::async, compute, 5);
    auto future2 = std::async(std::launch::async, compute, 10);

    // Do other work while tasks run...
    std::cout << "Result 1: " << future1.get() << "\n";  // 25
    std::cout << "Result 2: " << future2.get() << "\n";  // 100
}

// std::promise for custom async communication
void worker(std::promise<int> prom) {
    prom.set_value(42);
}

int main() {
    std::promise<int> prom;
    std::future<int> fut = prom.get_future();
    std::thread t(worker, std::move(prom));
    std::cout << "Value: " << fut.get() << "\n";  // 42
    t.join();
}
```

---

## Configurazione del progetto e sistema di creazione
### Struttura del progetto
```
my_project/
+-- CMakeLists.txt
+-- src/
|   +-- main.cpp
|   +-- app.cpp
|   +-- app.h
|   +-- utils/
|       +-- string_utils.cpp
|       +-- string_utils.h
+-- include/
|   +-- config.h
+-- tests/
|   +-- CMakeLists.txt
|   +-- test_app.cpp
|   +-- test_utils.cpp
+-- third_party/
|   +-- CMakeLists.txt
+-- .clang-format
+-- .clang-tidy
```

### CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.20)
project(my_project VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_compile_options(-Wall -Wextra -Wpedantic)

# Main executable
add_executable(my_app src/main.cpp src/app.cpp src/utils/string_utils.cpp)
target_include_directories(my_app PRIVATE include src)

# Testing with Google Test
include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.14.0
)
FetchContent_MakeAvailable(googletest)
enable_testing()
add_executable(tests tests/test_app.cpp tests/test_utils.cpp src/app.cpp)
target_link_libraries(tests GTest::gtest_main)
target_include_directories(tests PRIVATE src include)
add_test(NAME AllTests COMMAND tests)
```

### Pipeline CI/CD (azioni GitHub)
```yaml
name: C++ CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: cmake -B build -DCMAKE_BUILD_TYPE=Debug
      - run: cmake --build build
      - run: ctest --test-dir build --output-on-failure
```

---

## Test
### Esempio di test di Google
```cpp
// tests/test_app.cpp
#include <gtest/gtest.h>
#include "app.h"

TEST(CalculatorTest, Addition) {
    EXPECT_EQ(add(2, 3), 5);
    EXPECT_EQ(add(-1, 1), 0);
    EXPECT_EQ(add(0, 0), 0);
}

TEST(CalculatorTest, Division) {
    EXPECT_DOUBLE_EQ(divide(10.0, 3.0), 3.333333333);
    EXPECT_THROW(divide(1.0, 0.0), std::invalid_argument);
}

TEST(StringUtilTest, Trim) {
    EXPECT_EQ(trim("  hello  "), "hello");
    EXPECT_EQ(trim(""), "");
    EXPECT_EQ(trim("  "), "");
}

// Parameterised test
class MathTest : public testing::TestWithParam<std::tuple<int, int, int>> {};

TEST_P(MathTest, Addition) {
    auto [a, b, expected] = GetParam();
    EXPECT_EQ(add(a, b), expected);
}

INSTANTIATE_TEST_SUITE_P(
    Cases, MathTest,
    testing::Values(
        std::make_tuple(1, 2, 3),
        std::make_tuple(0, 0, 0),
        std::make_tuple(-1, -2, -3)
    ));
```

```bash
# Build and run tests
cmake -B build && cmake --build build
ctest --test-dir build --output-on-failure
```

---

## Interoperabilità
### Interoperabilità C (esterno "C")
```cpp
// Calling C code from C++
extern "C" {
    #include "legacy_c_library.h"
}

// Exposing C++ to C (via C interface)
// cpp_interface.h
#ifdef __cplusplus
extern "C" {
#endif

int cpp_add(int a, int b);
void cpp_process(const char* input, char* output, int max_len);

#ifdef __cplusplus
}
#endif

// cpp_interface.cpp
#include "cpp_interface.h"
#include <string>

extern "C" int cpp_add(int a, int b) {
    return a + b;  // Could use C++ features internally
}

extern "C" void cpp_process(const char* input, char* output, int max_len) {
    std::string result = std::string(input) + "_processed";
    strncpy(output, result.c_str(), max_len - 1);
    output[max_len - 1] = '\0';
}
```

---

## Modelli di progettazione
### Modello di fabbrica
```cpp
#include <memory>
#include <string>
#include <unordered_map>
#include <functional>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual std::string name() const = 0;
};

class Circle : public Shape {
    double radius_;
public:
    explicit Circle(double r) : radius_(r) {}
    double area() const override { return 3.14159 * radius_ * radius_; }
    std::string name() const override { return "Circle"; }
};

class Rectangle : public Shape {
    double w_, h_;
public:
    Rectangle(double w, double h) : w_(w), h_(h) {}
    double area() const override { return w_ * h_; }
    std::string name() const override { return "Rectangle"; }
};

// Factory using std::function
class ShapeFactory {
    using Creator = std::function<std::unique_ptr<Shape>()>;
    std::unordered_map<std::string, Creator> creators_;
public:
    void register_shape(const std::string& name, Creator creator) {
        creators_[name] = std::move(creator);
    }
    std::unique_ptr<Shape> create(const std::string& name) {
        return creators_.at(name)();
    }
};
```

### Modello dell'osservatore
```cpp
#include <functional>
#include <vector>
#include <string>

class Event {
    using Callback = std::function<void(const std::string&)>;
    std::vector<Callback> listeners_;
public:
    void subscribe(Callback cb) { listeners_.push_back(std::move(cb)); }
    void emit(const std::string& data) {
        for (auto& cb : listeners_) cb(data);
    }
};

// Usage
Event on_data;
on_data.subscribe([](const std::string& d) { std::cout << "Listener 1: " << d << "\n"; });
on_data.subscribe([](const std::string& d) { std::cout << "Listener 2: " << d << "\n"; });
on_data.emit("hello");
```

---

## Prestazioni e ottimizzazione
### Strumenti di profilazione
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Esempio di benchmark (Google Benchmark)
```cpp
#include <benchmark/benchmark.h>

static void BM_VectorPushBack(benchmark::State& state) {
    for (auto _ : state) {
        std::vector<int> v;
        for (int i = 0; i < state.range(0); i++) v.push_back(i);
    }
}
BENCHMARK(BM_VectorPushBack)->Arg(1000)->Arg(100000);
BENCHMARK_MAIN();
```

### Tecniche di ottimizzazione
```cpp
// Reserve vector capacity when size is known
std::vector<int> v;
v.reserve(10000);  // Avoid reallocations

// Use std::move for expensive objects
std::string s = "hello world";
std::string moved = std::move(s);

// Prefer pre-increment for iterators
for (auto it = v.begin(); it != v.end(); ++it) { }

// Likely/unlikely attributes (C++20)
if (x > 0) [[likely]] {
    // Fast path
} else [[unlikely]] {
    // Error path
}
```

---

## Distribuzione
### Distribuzione Docker
```dockerfile
FROM gcc:13 AS builder
WORKDIR /app
COPY src/ ./
RUN g++ -std=c++20 -O2 -o my_app main.cpp app.cpp

FROM debian:bookworm-slim
COPY --from=builder /app/my_app /usr/local/bin/my_app
CMD ["my_app"]
```

---

## Compilazione e strumenti
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Strumento | Scopo |
|------|---------|
| **GCC/Clang/MSVC** | Compilatori |
| **CMake** | Generatore di sistemi di costruzione (standard di settore) |
| **GDB/LLDB** | Debugger |
| **Valgrind / AddressSanitizer** | Rilevamento errori di memoria |
| **rumore ordinato** | Lining e ammodernamento |
| **formato clang** | Formattazione del codice |
| **Conan/vcpkg** | Gestori di pacchetti |
| **Test Google / Catch2** | Strutture di test |
---

## Quando utilizzare il C++
| Scenario | Perché C++ | Alternativa migliore |
|----------|---------|-------------|
| Motori di gioco | Prestazioni + controllo in tempo reale | -- |
| Browser | Decenni di codice ottimizzato | Rust per i nuovi componenti del browser |
| Trading ad alta frequenza | La latenza dei microsecondi è importante | -- |
| Sistemi integrati (complessi) | Ricco set di funzionalità con accesso hardware | C per più semplice, Rust per sicurezza |
| Applicazioni GUI (desktop) | Il framework Qt è maturo | C# (Windows), Swift (macOS) |
| Sviluppo di applicazioni generali | Troppo complesso per la maggior parte delle app | Python, Go, Java |
| Backend Web | Non è la scelta tipica | Vai, Rust, Node.js |
| Scripting/automazione | Strumento completamente sbagliato | Python, JavaScript |
---

## Evoluzione degli standard C++
| Norma | Anno | Caratteristiche principali |
|----------|------|-----|
| C++98 | 1998 | Lo standard ISO originale; STL, iostream |
| C++11 | 2011 | **Inizia il C++ moderno**: auto, lambda, puntatori intelligenti, semantica di spostamento |
| C++14 | 2014| Lambda generici, std::make_unique, deduzione del tipo restituito |
| C++17 | 2017 | Collegamenti strutturati, std::opzionale, std::variant, std::filesystem |
| C++20 | 2020 | **Rilascio principale**: concetti, intervalli, coroutine, moduli |
| C++23 | 2023 | std::expected, std::print, deducendo questo |
Per i nuovi progetti, scegliere come target minimo C++20.
---

## Domande e risposte sintetiche
### D1: Qual è la differenza tra`std::unique_ptr`,`std::shared_ptr`e`std::weak_ptr`?
**R:**`unique_ptr`rappresenta la proprietà esclusiva: solo un puntatore può possedere la risorsa. Ha zero spese generali (come un puntatore grezzo) e non può essere copiato, ma solo spostato. `shared_ptr`rappresenta la proprietà condivisa: più puntatori condividono la risorsa, con conteggio dei riferimenti. Quando l'ultimo`shared_ptr`viene distrutto, la risorsa viene liberata. `weak_ptr`è un osservatore non proprietario di un `shared_ptr`: non aumenta il conteggio dei riferimenti e viene utilizzato per interrompere i riferimenti circolari.
```cpp
// unique_ptr — exclusive ownership, zero overhead
auto file = std::make_unique<FileHandle>("data.txt");
// auto copy = file;              // Error: cannot copy
auto moved = std::move(file);     // OK: transfers ownership
// file is now nullptr

// shared_ptr — shared ownership, reference counted
auto config = std::make_shared<Config>("app.conf");
auto ref1 = config;               // ref count = 2
auto ref2 = config;               // ref count = 3
// Resource freed when last shared_ptr is destroyed

// weak_ptr — non-owning observer
std::weak_ptr<Config> observer = config;
if (auto locked = observer.lock()) {  // Promote to shared_ptr
    locked->reload();
}
// Break circular references:
// struct A { shared_ptr<B> b; };  // A → B
// struct B { shared_ptr<A> a; };  // B → A — memory leak!
// Fix: change one to weak_ptr<B>
```

### D2: Cos'è la semantica di spostamento e perché è importante?
**R:** La semantica di spostamento (C++11) consente di trasferire risorse (memoria heap, handle di file, ecc.) da un oggetto temporaneo invece di copiarli. Un costruttore/assegnazione di spostamento accetta un riferimento rvalue (`T&&`) e "ruba" le risorse dell'origine, lasciandola in uno stato valido ma non specificato. Ciò elimina le copie non necessarie ed è il motivo per cui la riallocazione`std::vector`è efficiente.
```cpp
class Buffer {
    std::unique_ptr<int[]> data_;
    size_t size_;
public:
    // Move constructor — steal resources
    Buffer(Buffer&& other) noexcept
        : data_(std::move(other.data_)), size_(other.size_) {
        other.size_ = 0;  // Leave source in valid empty state
    }

    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if (this != &other) {
            data_ = std::move(other.data_);
            size_ = other.size_;
            other.size_ = 0;
        }
        return *this;
    }
};

// Move happens automatically with temporaries
Buffer createBuffer() {
    Buffer b(1000);
    return b;  // Moved, not copied (or elided via NRVO)
}

// Explicit move with std::move
Buffer a(500);
Buffer b = std::move(a);  // a's resources transferred to b
```

### D3: Quando dovrei utilizzare`auto`e quando dovrei specificare i tipi in modo esplicito?
**R:** Utilizza`auto`quando il tipo è ovvio dal contesto (loop iteratori, chiamate `make_unique`/`make_shared`, tipi lambda, tipi di template complessi). Specifica i tipi in modo esplicito quando il tipo non è ovvio, quando sono necessarie conversioni implicite o nelle firme API pubbliche. Lo stile "Almost Always Auto" (AAA) favorisce`auto`per le variabili locali; lo stile "auto dove utile" è più conservatore.
```cpp
// Good use of auto — type is obvious
auto ptr = std::make_unique<User>("Alice");   // unique_ptr<User>
auto it = map.find("key");                     // map::iterator
auto lambda = [](int x) { return x * 2; };    // closure type

// Good use of auto — avoids repetition
std::map<std::string, std::vector<int>>::iterator it2 = m.begin();  // Verbose
auto it3 = m.begin();  // Much cleaner

// Specify type explicitly — when conversion is needed
double result = computeInt() * 2.0;  // int → double conversion
// auto result = computeInt() * 2.0;  // Also double, but less clear

// Never use auto in function signatures (C++20 abbreviated functions are different)
auto process(std::string_view input) -> Result;  // OK: trailing return type
```

### D4: In che modo i concetti (C++20) migliorano il codice del modello?
**R:** I concetti vincolano i parametri del modello con requisiti denominati, producendo messaggi di errore chiari e consentendo l'overload delle funzioni sui vincoli del modello. Prima dei concetti venivano utilizzati SFINAE e `static_assert`: entrambi producono errori criptici. I concetti rendono il codice del modello leggibile e componibile.
```cpp
#include <concepts>

// Define a concept
template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

// Constrained function template
template<Numeric T>
T square(T x) { return x * x; }

// Abbreviated syntax (C++20)
void print(const std::ranges::range auto& container) {
    for (const auto& item : container) {
        std::cout << item << " ";
    }
}

// Concept composition
template<typename T>
concept Printable = requires(T t) {
    { std::cout << t } -> std::same_as<std::ostream&>;
};

// Overloading on concepts
template<std::integral T>
std::string format(T value) { return std::to_string(value); }

template<std::floating_point T>
std::string format(T value) {
    return std::format("{:.2f}", value);
}

format(42);      // Calls integral version: "42"
format(3.14);    // Calls floating_point version: "3.14"
```

### D5: Cos'è la Regola del Cinque e come si collega alla Regola dello Zero?
**R:** La regola del cinque: se definisci uno qualsiasi tra distruttore, costruttore di copia, assegnazione di copia, costruttore di spostamento o assegnazione di spostamento, devi definirli tutti e cinque. La regola dello zero (preferita): progettare classi in modo che non abbiano bisogno di nessuno di questi: utilizzare i tipi RAII (`std::string`,`std::vector`,`std::unique_ptr`) come membri e gli speciali generati dal compilatore faranno automaticamente la cosa giusta.
```cpp
// Rule of Zero — preferred approach
class User {
    std::string name_;              // Manages its own memory
    std::vector<int> scores_;       // Manages its own memory
    std::unique_ptr<Detail> detail_; // Manages its own memory
    // No destructor, copy/move constructors, or assignments needed
    // Compiler-generated versions do the right thing
};

// Rule of Five — when you manage resources directly
class FileHandle {
    FILE* file_;
public:
    ~FileHandle() { if (file_) fclose(file_); }
    FileHandle(const FileHandle&) = delete;            // Non-copyable
    FileHandle& operator=(const FileHandle&) = delete;
    FileHandle(FileHandle&& other) noexcept : file_(other.file_) {
        other.file_ = nullptr;
    }
    FileHandle& operator=(FileHandle&& other) noexcept {
        if (this != &other) {
            if (file_) fclose(file_);
            file_ = other.file_;
            other.file_ = nullptr;
        }
        return *this;
    }
};
```

---

## Risoluzione dei problemi basati sulla catena di pensiero
### Problema 1: implementare una coda produttore-consumatore thread-safe con intervalli
**Dichiarazione del problema:** crea una coda produttore-consumatore delimitata e thread-safe utilizzando intervalli C++20 per il lato consumatore. La coda dovrebbe bloccare i produttori quando sono pieni e i consumatori quando sono vuoti e supportare l'arresto regolare.
**Passaggio 1: comprendere il problema:**
Abbiamo bisogno di: (1) una coda delimitata con blocco push/pop, (2) sicurezza del thread tramite mutex e variabili di condizione, (3) un modo per segnalare l'arresto, (4) integrazione degli intervalli C++20 in modo che i consumatori possano utilizzare cicli for basati su intervalli.
**Passaggio 2: identificare l'approccio:**
- Utilizza`std::mutex`+`std::condition_variable`per bloccare.
- Utilizza`std::queue<T>`come contenitore sottostante.
- Utilizza`std::optional<T>`come tipo di ritorno:`std::nullopt`segnala lo spegnimento.
- Implementare un iteratore basato su sentinella per il supporto degli intervalli.
**Passaggio 3: implementa la soluzione:**
```cpp
#include <queue>
#include <mutex>
#include <condition_variable>
#include <optional>
#include <thread>
#include <vector>
#include <iostream>

template<typename T>
class BlockingQueue {
    std::queue<T> queue_;
    mutable std::mutex mutex_;
    std::condition_variable not_empty_;
    std::condition_variable not_full_;
    size_t capacity_;
    bool shutdown_ = false;

public:
    explicit BlockingQueue(size_t capacity) : capacity_(capacity) {}

    // Returns false if shutdown was requested
    bool push(T value) {
        std::unique_lock lock(mutex_);
        not_full_.wait(lock, [&] { return queue_.size() < capacity_ || shutdown_; });
        if (shutdown_) return false;
        queue_.push(std::move(value));
        not_empty_.notify_one();
        return true;
    }

    // Returns nullopt if shutdown was requested and queue is empty
    std::optional<T> pop() {
        std::unique_lock lock(mutex_);
        not_empty_.wait(lock, [&] { return !queue_.empty() || shutdown_; });
        if (queue_.empty()) return std::nullopt;
        T value = std::move(queue_.front());
        queue_.pop();
        not_full_.notify_one();
        return value;
    }

    void shutdown() {
        std::lock_guard lock(mutex_);
        shutdown_ = true;
        not_empty_.notify_all();
        not_full_.notify_all();
    }

    // Range support — iterator that reads until shutdown
    class Iterator {
        BlockingQueue* bq_;
        std::optional<T> current_;
    public:
        using iterator_category = std::input_iterator_tag;
        using value_type = T;
        using difference_type = std::ptrdiff_t;
        using pointer = T*;
        using reference = T&;

        Iterator() : bq_(nullptr) {}  // Sentinel (end)
        explicit Iterator(BlockingQueue* bq) : bq_(bq) { advance(); }

        void advance() { current_ = bq_ ? bq_->pop() : std::nullopt; }
        T& operator*() { return *current_; }
        Iterator& operator++() { advance(); return *this; }
        Iterator operator++(int) { auto tmp = *this; advance(); return tmp; }
        bool operator==(const Iterator& other) const {
            return !current_.has_value() && !other.current_.has_value();
        }
        bool operator!=(const Iterator& other) const { return !(*this == other); }
    };

    Iterator begin() { return Iterator(this); }
    Iterator end() { return Iterator(); }
};

// Usage with ranges
int main() {
    BlockingQueue<int> queue(10);

    // Producer
    std::thread producer([&] {
        for (int i = 0; i < 20; i++) {
            queue.push(i);
        }
        queue.shutdown();
    });

    // Consumer — using range-based for loop
    std::vector<int> results;
    for (int value : queue) {
        results.push_back(value);
    }

    producer.join();
    std::cout << "Received " << results.size() << " items\n";
}
```

**Passaggio 4: verifica e ottimizzazione:**
- Sicurezza del thread:`std::mutex`protegge tutto lo stato della coda; le variabili di condizione gestiscono il blocco.
- Spegnimento ordinato:`shutdown()`sveglia tutti i camerieri; `pop()`restituisce`nullopt`quando è vuoto e spento.
- Supporto dell'intervallo: la sentinella dell'iteratore (costruita per impostazione predefinita) è uguale a qualsiasi iteratore esaurito.
- Produzione: utilizzare`boost::lockfree::spsc_queue`per singolo produttore e singolo consumatore senza blocchi o`folly::ProducerConsumerQueue`per scenari ad alto rendimento.
### Problema 2: implementare un tipo qualsiasi cancellato dal tipo
**Dichiarazione del problema:** Implementa da zero una versione semplificata di`std::any`(C++17): un contenitore indipendente dai tipi per singoli valori di qualsiasi tipo, che supporta la copia, lo spostamento e il recupero indipendente dai tipi tramite`any_cast`.
**Passaggio 1: comprendere il problema:**
`std::any`memorizza un valore di qualsiasi tipo copiabile e lo recupera con il controllo del tipo. Internamente utilizza la cancellazione del tipo: un'interfaccia della classe base con un modello derivato che contiene il valore effettivo. `any_cast`controlla il tipo memorizzato in fase di esecuzione e genera`bad_any_cast`in caso di mancata corrispondenza.
**Passaggio 2: identificare l'approccio:**
- Utilizza una classe base`HolderBase`con`clone()`virtuale e`type()`.
- Utilizzare un modello derivato`Holder<T>`che memorizza il valore effettivo.
- Memorizza un`std::unique_ptr<HolderBase>`nella classe `Any`.
-`any_cast<T>`controlla`typeid`ed esegue un`static_cast`.
**Passaggio 3: implementa la soluzione:**
```cpp
#include <typeinfo>
#include <memory>
#include <stdexcept>
#include <utility>
#include <string>
#include <iostream>

class BadAnyCast : public std::bad_cast {
public:
    const char* what() const noexcept override { return "bad any_cast"; }
};

class Any {
    struct HolderBase {
        virtual ~HolderBase() = default;
        virtual std::unique_ptr<HolderBase> clone() const = 0;
        virtual const std::type_info& type() const = 0;
    };

    template<typename T>
    struct Holder : HolderBase {
        T value;
        template<typename U>
        explicit Holder(U&& v) : value(std::forward<U>(v)) {}
        std::unique_ptr<HolderBase> clone() const override {
            return std::make_unique<Holder>(value);
        }
        const std::type_info& type() const override { return typeid(T); }
    };

    std::unique_ptr<HolderBase> holder_;

public:
    Any() = default;

    template<typename T>
    Any(T&& value) requires(!std::same_as<std::decay_t<T>, Any>)
        : holder_(std::make_unique<Holder<std::decay_t<T>>>(std::forward<T>(value))) {}

    // Copy
    Any(const Any& other) : holder_(other.holder_ ? other.holder_->clone() : nullptr) {}
    Any& operator=(const Any& other) {
        if (this != &other) { holder_ = other.holder_ ? other.holder_->clone() : nullptr; }
        return *this;
    }

    // Move
    Any(Any&&) = default;
    Any& operator=(Any&&) = default;

    // Check if empty
    bool has_value() const noexcept { return holder_ != nullptr; }
    const std::type_info& type() const {
        return holder_ ? holder_->type() : typeid(void);
    }
    void reset() noexcept { holder_.reset(); }

    // Type-safe cast
    template<typename T>
    friend T& any_cast(Any& a) {
        if (!a.holder_ || a.holder_->type() != typeid(T))
            throw BadAnyCast{};
        return static_cast<Holder<T>*>(a.holder_.get())->value;
    }

    template<typename T>
    friend const T& any_cast(const Any& a) {
        if (!a.holder_ || a.holder_->type() != typeid(T))
            throw BadAnyCast{};
        return static_cast<const Holder<T>*>(a.holder_.get())->value;
    }
};

// Usage
Any a = 42;
Any b = std::string("hello");
Any c = a;  // Copy

std::cout << any_cast<int>(a) << "\n";           // 42
std::cout << any_cast<std::string>(b) << "\n";   // hello
// any_cast<double>(a);                            // Throws BadAnyCast
```

**Passaggio 4: verifica e ottimizzazione:**
- Sicurezza del tipo:`any_cast`controlla`typeid`in fase di esecuzione: il tipo errato genera`BadAnyCast`.
- Copia semantica:`clone()`virtuale crea una copia profonda del valore mantenuto.
- Semantica di spostamento: il costruttore/assegnazione di spostamento predefinito trasferisce`unique_ptr`in modo efficiente.
- Ottimizzazione del buffer ridotto (come il vero `std::any`): memorizza piccoli tipi in linea senza allocazione dell'heap. Ciò richiede un`union`con un buffer di byte, molto più complesso.
- Produzione: utilizza`std::any`(C++17): è standard, ben testato e può includere SBO.
---

## Riepilogo
Il C++ occupa una posizione unica nella programmazione: offre le prestazioni grezze del C con la potenza espressiva delle astrazioni di alto livello. Il C++ moderno (C++20/23) è un linguaggio molto diverso dal C++ degli anni '90: è più sicuro, più espressivo e più produttivo. La curva di apprendimento è ripida e la lingua premia la disciplina. Per le applicazioni critiche per le prestazioni in cui è necessario un controllo granulare, C++ rimane uno dei migliori strumenti disponibili.