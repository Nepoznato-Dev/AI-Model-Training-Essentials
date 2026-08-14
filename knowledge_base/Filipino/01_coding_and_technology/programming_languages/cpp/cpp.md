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
# C++
Ang C++ ay isang general-purpose, compiled programming language na nilikha ni Bjarne Stroustrup, na unang inilabas noong 1985. Pinapalawak nito ang C na may mga object-oriented na feature, generics, at -- sa mga modernong bersyon (C++11 at mas bago) -- high-level abstraction tulad ng lambdas, smart pointer, at Standard Template Library (STL). Ang C++ ay sumusunod sa prinsipyong "zero-overhead abstraction": hindi ka dapat magbayad para sa mga feature na hindi mo ginagamit.
Ang C++ ay ang wikang pipiliin kapag kailangan mo ng parehong mataas na pagganap at nagpapahayag na kapangyarihan. Pinapagana nito ang mga game engine (Unreal Engine), mga browser (Chrome, Firefox), mga database (MongoDB), mga operating system (mga bahagi ng Windows at macOS), mga financial trading system, at mga real-time na simulation.
---

## Bakit Mahalaga ang C++
- **Pagganap nang may pagpapahayag**: Malapit sa C na bilis na may mga klase, template, at modernong abstraction.
- **Zero-overhead na prinsipyo**: Ang mga abstraction ay pinagsama-sama sa parehong code na isusulat mo sa pamamagitan ng kamay sa C.
- **Malaking codebase**: Mga dekada ng kritikal na imprastraktura -- mga laro, browser, database, mga naka-embed na system.
- **Multi-paradigm**: Sinusuportahan ang procedural, object-oriented, generic, at functional na mga istilo ng programming.
- **Deterministikong pagkasira**: Tinitiyak ng RAII na nalilinis ang mga mapagkukunan nang mahuhulaan -- walang humihinto sa pagkolekta ng basura.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Pagiging kumplikado** | Napakalaki ng wika -- kahit ang mga eksperto ay hindi alam ang lahat ng ito | Manatili sa modernong C++ (C++17/20); iwasan ang mga legacy pattern |
| **Kaligtasan sa memorya** | Manu-manong pamamahala ng memorya; nakalawit na mga payo, tagas, UB | Gumamit ng mga matalinong pointer, RAII, at std::opsyonal |
| **Mga oras ng pag-compile** | Ang malalaking proyekto ay maaaring tumagal ng ilang minuto upang i-compile | Precompiled header, modules (C++20), incremental build |
| **Mga mensahe ng error** | Ang mga error sa template ay maaaring daan-daang linya ang haba | Gumamit ng static_assert, mga konsepto (C++20), mas mahusay na mga compiler |
| **Binary compatibility** | Kawalang-tatag ng ABI sa mga bersyon ng compiler | Stable C interface para sa mga shared library |
---

## Syntax Fundamentals
### Pangunahing Istruktura
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

### Mga Klase at Object-Oriented Programming
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

### Mga Template (Generic Programming)
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

### Mga Makabagong Tampok ng C++ (C++17/20)
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

## Ang Standard Library
### Mga lalagyan
| Lalagyan | Uri | Gamitin Kapag |
|-----------|------|----------|
| std::vector | Dynamic na array | Default na pagpipilian para sa sequential data |
| std::deque | Dalawang-natapos na pila | Kailangan ng mabilis na pagsingit/pagbura sa magkabilang dulo |
| std::listahan | Dobleng naka-link na listahan | Madalas ipasok/burahin sa gitna |
| std::mapa | Nag-order ng tree map | Kailangan ng mga pinagsunod-sunod na key, O(log n) lookup |
| std::unordered_map | Hash na mapa | Mabilis na O(1) average lookup |
| std::set | Naka-order na set | Mga natatanging pinagsunod-sunod na elemento |
| std::array | Fixed-size array | Ang stack-allocated, alam na laki sa oras ng pag-compile |
| std::string | Teksto | Palaging gamitin ito, hindi raw char* |
### Mga Smart Pointer
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

### Algorithm
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

## Advanced na Syntax at Mga Pattern
### Mga Konsepto (C++20)
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

### Ilipat ang Semantics at RAII
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

### Custom Exception Hierarchy
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

## Concurrency at Paralelismo
### std::thread at Pag-synchronize
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

### Async, Futures, at Mga Pangako
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

## Project Configuration at Build System
### Istraktura ng Proyekto
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

### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### Halimbawa ng Google Test
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

## Interoperability
### C Interop (panlabas na "C")
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

## Mga Pattern ng Disenyo
### Pattern ng Pabrika
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

### Pattern ng Tagamasid
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Halimbawa ng Benchmark (Google Benchmark)
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

### Mga Teknik sa Pag-optimize
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

## Deployment
### Docker Deployment
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

## Compilation at Tooling
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Tool | Layunin |
|------|---------|
| **GCC / Clang / MSVC** | Mga Compiler |
| **CMake** | Bumuo ng system generator (standard sa industriya) |
| **GDB / LLDB** | Mga Debugger |
| **Valgrind / AddressSanitizer** | Pagtukoy ng error sa memorya |
| **clang-linis** | Linting at modernisasyon |
| **clang-format** | Pag-format ng code |
| **Conan / vcpkg** | Mga manager ng package |
| **Google Test / Catch2** | Mga balangkas ng pagsubok |
---

## Kailan Gamitin ang C++
| Sitwasyon | Bakit C++ | Mas mahusay na Alternatibo |
|----------|---------|-------------------|
| Mga makina ng laro | Pagganap + real-time na kontrol | -- |
| Mga Browser | Mga dekada ng na-optimize na code | kalawang para sa mga bagong bahagi ng browser |
| High-frequency na pangangalakal | Mahalaga ang microsecond latency | -- |
| Mga naka-embed na system (kumplikado) | Rich feature set na may access sa hardware | C para sa mas simple, kalawang para sa kaligtasan |
| Mga GUI application (desktop) | Mature na ang Qt framework | C# (Windows), Swift (macOS) |
| Pangkalahatang pag-unlad ng application | Masyadong kumplikado para sa karamihan ng mga app | Python, Go, Java |
| Mga backend sa web | Hindi ang karaniwang pagpipilian | Go, Rust, Node.js |
| Pag-script / automation | Ganap na maling tool | Python, JavaScript |
---

## C++ Standards Evolution
| Pamantayan | Taon | Mga Pangunahing Tampok |
|----------|------|-------------|
| C++98 | 1998 | Ang orihinal na pamantayan ng ISO; STL, mga iostream |
| C++11 | 2011 | **Nagsisimula ang modernong C++**: auto, lambdas, smart pointer, move semantics |
| C++14 | 2014 | Mga generic na lambdas, std::make_unique, return type deduction |
| C++17 | 2017 | Structured bindings, std::opsyonal, std::variant, std::filesystem |
| C++20 | 2020 | **Major release**: concepts, ranges, coroutines, modules |
| C++23 | 2023 | std::expected, std::print, deducing this |
Para sa mga bagong proyekto, i-target ang C++20 bilang pinakamababa.
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba ng`std::unique_ptr`,`std::shared_ptr`, at`std::weak_ptr`?
**A:** Kinakatawan ng`unique_ptr`ang eksklusibong pagmamay-ari — isang pointer lang ang maaaring magmay-ari ng mapagkukunan. Ito ay may zero overhead (katulad ng isang raw pointer) at hindi maaaring kopyahin, ilipat lamang.  Kinakatawan ng`shared_ptr`ang ibinahaging pagmamay-ari — maraming pointer ang nagbabahagi ng mapagkukunan, na may pagbibilang ng sanggunian. Kapag ang huling`shared_ptr`ay nawasak, ang mapagkukunan ay pinalaya.  Ang`weak_ptr`ay isang hindi nagmamay-ari na tagamasid ng isang`shared_ptr`— hindi nito pinapataas ang bilang ng sanggunian at ginagamit upang sirain ang mga pabilog na sanggunian.
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

### Q2: Ano ang move semantics, at bakit mahalaga ang mga ito?
**A:** Ang Move semantics (C++11) ay nagbibigay-daan sa paglilipat ng mga mapagkukunan (heap memory, file handle, atbp.) mula sa isang pansamantalang bagay sa halip na kopyahin ang mga ito. Ang isang move constructor/assignment ay tumatagal ng isang rvalue reference (`T&&`) at "nakawin" ang mga mapagkukunan ng source, na iniiwan ito sa isang wasto ngunit hindi natukoy na estado. Inaalis nito ang mga hindi kinakailangang kopya at ang dahilan kung bakit mahusay ang`std::vector`reallocation.
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

### Q3: Kailan ko dapat gamitin ang`auto`, at kailan ko dapat tahasang tukuyin ang mga uri?
**A:** Gamitin ang`auto`kapag ang uri ay halata mula sa konteksto (iterator loops,`make_unique`/`make_shared`na tawag, mga uri ng lambda, kumplikadong mga uri ng template). Tahasang tukuyin ang mga uri kapag hindi halata ang uri, kapag kailangan mo ng mga implicit na conversion, o sa mga pampublikong lagda ng API. Ang istilong "Almost Always Auto" (AAA) ay pinapaboran ang`auto`para sa mga lokal na variable; ang istilong "auto where helpful" ay mas konserbatibo.
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

### Q4: Paano pinapabuti ng mga konsepto (C++20) ang template code?
**A:** Pinipigilan ng mga konsepto ang mga parameter ng template na may pinangalanang mga kinakailangan, na gumagawa ng mga malinaw na mensahe ng error at pinapagana ang pag-overload ng function sa mga hadlang sa template. Bago ang mga konsepto, ginamit ang SFINAE at`static_assert`— parehong gumagawa ng mga misteryosong error. Ginagawa ng mga konsepto na nababasa at nabubuo ang code ng template.
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

### Q5: Ano ang Rule of Five, at paano ito nauugnay sa Rule of Zero?
**A:** The Rule of Five: kung tutukuyin mo ang alinman sa destructor, copy constructor, copy assignment, move constructor, o ilipat assignment, dapat mong tukuyin ang lahat ng lima. The Rule of Zero (preferred): design classes para hindi na nila kailangan ang alinman sa mga ito — gamitin ang mga uri ng RAII (`std::string`,`std::vector`,`std::unique_ptr`) bilang mga miyembro, at awtomatikong gagawin ng mga compiler-generated specials ang tamang bagay.
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

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Magpatupad ng Thread-Safe Producer-Consumer Queue na may Mga Saklaw
**Pahayag ng Problema:** Bumuo ng bounded, thread-safe na pila ng producer-consumer gamit ang mga hanay ng C++20 para sa consumer side. Dapat harangan ng pila ang mga producer kapag puno at ang mga consumer kapag walang laman, at suportahan ang magandang pagsara.
**Hakbang 1 — Unawain ang Problema:**
Kailangan namin ng: (1) isang bounded queue na may nakaharang na push/pop, (2) thread safety sa pamamagitan ng mutex at condition variable, (3) isang paraan para magsenyas ng shutdown, (4) C++20 range integration para magamit ng mga consumer ang range-based para sa mga loop.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gamitin ang`std::mutex`+`std::condition_variable`para sa pagharang.
- Gamitin ang`std::queue<T>`bilang pinagbabatayan na lalagyan.
- Gamitin ang`std::optional<T>`bilang uri ng pagbabalik —`std::nullopt`ang nagsasara ng mga signal.
- Magpatupad ng iterator na nakabatay sa sentinel para sa suporta sa mga hanay.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Kaligtasan ng thread: Pinoprotektahan ng`std::mutex`ang lahat ng estado ng pila; ang mga variable ng kondisyon ay humahawak ng pagharang.
- Magagandang shutdown:`shutdown()`gumising sa lahat ng waiter;  Ibinabalik ng`pop()`ang`nullopt`kapag walang laman at isinara.
- Suporta sa hanay: ang sentinel ng iterator (default-constructed) ay naghahambing ng katumbas sa anumang naubos na iterator.
- Produksyon: gumamit ng`boost::lockfree::spsc_queue`para sa single-producer na single-consumer na walang lock, o`folly::ProducerConsumerQueue`para sa mga high-throughput na sitwasyon.
### Problema 2: Magpatupad ng Uri-Erased Anumang Uri
**Pahayag ng Problema:** Magpatupad ng pinasimpleng bersyon ng`std::any`(C++17) mula sa simula — isang lalagyan na ligtas sa uri para sa mga solong halaga ng anumang uri, sumusuporta sa kopya, paglipat, at pagkuha ng ligtas sa uri sa pamamagitan ng`any_cast`.
**Hakbang 1 — Unawain ang Problema:**
 Ang`std::any`ay nag-iimbak ng isang halaga ng anumang maaaring kopyahin na uri at kinukuha ito sa pamamagitan ng pagsuri ng uri. Sa panloob, gumagamit ito ng uri ng erasure: isang base class interface na may nagmula na template na nagtataglay ng aktwal na halaga.  Sinusuri ng`any_cast`ang nakaimbak na uri sa runtime at inihagis ang`bad_any_cast`sa mismatch.
**Hakbang 2 — Tukuyin ang Diskarte:**
- Gumamit ng base class na`HolderBase`na may virtual na`clone()`at`type()`.
- Gumamit ng hinangong template na`Holder<T>`na nag-iimbak ng aktwal na halaga.
- Mag-imbak ng`std::unique_ptr<HolderBase>`sa`Any`na klase.
- Sinusuri ng`any_cast<T>`ang`typeid`at nagsasagawa ng`static_cast`.
**Hakbang 3 — Ipatupad ang Solusyon:**
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

**Hakbang 4 — I-verify at I-optimize:**
- Kaligtasan ng uri: Sinusuri ng`any_cast`ang`typeid`sa runtime — ang maling uri ay naghagis ng`BadAnyCast`.
- Kopyahin ang mga semantika: ang virtual na`clone()`ay lumilikha ng malalim na kopya ng hawak na halaga.
- Ilipat ang mga semantika: ang default na paglipat ng constructor/assignment ay naglilipat ng`unique_ptr`nang mahusay.
- Maliit na buffer optimization (tulad ng tunay na`std::any`): mag-imbak ng maliliit na uri nang inline nang walang heap allocation. Nangangailangan ito ng`union`na may byte buffer — na mas kumplikado.
- Produksyon: gumamit ng`std::any`(C++17) — ito ay karaniwan, mahusay na nasubok, at maaaring may kasamang SBO.
---

## Buod
Sinasakop ng C++ ang isang natatanging posisyon sa programming: binibigyan ka nito ng hilaw na pagganap ng C na may nagpapahayag na kapangyarihan ng mga abstraction na may mataas na antas. Ang modernong C++ (C++20/23) ay isang ibang-iba na wika mula sa C++ noong 1990s -- ito ay mas ligtas, mas makahulugan, at mas produktibo. Ang kurba ng pagkatuto ay matarik, at ginagantimpalaan ng wika ang disiplina. Para sa mga application na kritikal sa pagganap kung saan kailangan mo ng mahusay na kontrol, ang C++ ay nananatiling isa sa mga pinakamahusay na tool na magagamit.