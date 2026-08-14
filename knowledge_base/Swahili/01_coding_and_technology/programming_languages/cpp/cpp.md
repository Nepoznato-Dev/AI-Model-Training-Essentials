<!--
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

-->
#C++
C++ ni lugha ya kusudi la jumla, iliyokusanywa ya programu iliyoundwa na Bjarne Stroustrup, iliyotolewa kwa mara ya kwanza mwaka wa 1985. Inapanua C kwa vipengele vinavyolenga kitu, jeneriki, na -- katika matoleo ya kisasa (C++11 na matoleo mapya zaidi) -- vifupisho vya kiwango cha juu kama vile lambdas, viashiria mahiri na Maktaba ya Kiolezo cha STL (STL). C++ inafuata kanuni ya "kuondoa sifuri": hupaswi kulipia vipengele usivyotumia.
C++ ni lugha ya chaguo unapohitaji utendakazi wa hali ya juu na nguvu ya kujieleza. Inawezesha injini za mchezo (Injini isiyo ya kweli), vivinjari (Chrome, Firefox), hifadhidata (MongoDB), mifumo ya uendeshaji (sehemu za Windows na macOS), mifumo ya biashara ya kifedha, na maiga ya wakati halisi.
---

## Kwa nini C++ ni muhimu
- **Utendaji unaoeleweka**: Kasi ya Karibu-C yenye madarasa, violezo na vifupisho vya kisasa.
- **Kanuni ya sifuri ya juu zaidi**: Vifupisho hukusanya hadi nambari ile ile ambayo ungeandika kwa mkono katika C.
- **Codebase kubwa**: Miongo kadhaa ya miundombinu muhimu -- michezo, vivinjari, hifadhidata, mifumo iliyopachikwa.
- **Multi-paradigm**: Inaauni mitindo ya kiutaratibu, inayolenga kitu, ya kawaida na ya utendakazi.
- **Uharibifu dhahiri**: RAII inahakikisha kuwa rasilimali zinasafishwa kwa njia inayotabirika -- hakuna mkusanya takataka atasitishwa.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Utata** | Lugha ni kubwa sana -- hata wataalam hawajui yote | Shikilia C++ ya kisasa (C++17/20); epuka mifumo ya urithi |
| **Usalama wa kumbukumbu** | Usimamizi wa kumbukumbu ya mwongozo; viashiria vinavyoning'inia, uvujaji, UB | Tumia viashiria mahiri, RAII, na std::hiari |
| **Kukusanya nyakati** | Miradi mikubwa inaweza kuchukua dakika kutayarisha | Vijajuu vilivyokusanywa mapema, moduli (C++20), miundo ya ziada |
| **Ujumbe wa hitilafu** | Makosa ya kiolezo yanaweza kuwa mamia ya mistari | Tumia tuli_assert, dhana (C++20), vikusanyaji bora zaidi |
| **Upatanifu wa binary** | Kukosekana kwa uthabiti kwa ABI katika matoleo ya mkusanyaji | Miingiliano thabiti ya C ya maktaba zilizoshirikiwa |
---

## Misingi ya Sintaksia
### Muundo Msingi
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

### Madarasa na Upangaji Unaoelekezwa na Kitu
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

### Violezo (Utayarishaji wa Kawaida)
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

### Vipengele vya Kisasa vya C++ (C++17/20)
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

## Maktaba ya Kawaida
### Vyombo
| Chombo | Andika | Tumia Wakati |
|-----------|------|-----------|
| std::vekta | Safu inayobadilika | Chaguo-msingi la data mfuatano |
| std::deque | Foleni iliyokamilishwa mara mbili | Inahitaji kuingiza/kufuta haraka katika ncha zote mbili |
| std::orodha | Orodha iliyounganishwa maradufu | Ingiza/futa mara kwa mara katikati |
| std::ramani | Ramani ya mti iliyoagizwa | Unahitaji vitufe vilivyopangwa, utafutaji wa O(logi n) |
| std::map_isiyopangwa | Ramani ya hashi | Utafutaji wa haraka wa O(1) |
| std::weka | Seti iliyoagizwa | Vipengee vya kipekee vilivyopangwa |
| std::safu | Safu ya ukubwa usiobadilika | Rafu iliyogawiwa, saizi inayojulikana wakati wa kukusanya |
| std::kamba | Maandishi | Tumia hii kila wakati, usiwahi char ghafi* |
### Viashiria Mahiri
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

### Algorithms
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

## Sintaksia na Miundo ya Kina
### Dhana (C++20)
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

### Hoja Semantiki na RAII
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

### Ngazi Maalum ya Vighairi
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

## Concurrency & Usambamba
### std:: thread na Usawazishaji
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

### Async, Futures, na Ahadi
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Muundo wa Mradi
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

### CI/CD Bomba (Vitendo vya GitHub)
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

##Upimaji
### Mfano wa Jaribio la Google
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

## Kuingiliana
### C Interop (ya nje "C")
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

## Miundo ya Kubuni
### Muundo wa Kiwanda
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

### Muundo wa Mwangalizi
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

## Utendaji na Uboreshaji
### Zana za Kuweka Wasifu
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Mfano wa Alama (Kigezo cha Google)
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

### Mbinu za Kuboresha
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

## Usambazaji
### Usambazaji wa Docker
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

## Mkusanyiko na Vifaa
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Zana | Kusudi |
|------|----------|
| **GCC / Clang / MSVC** | Wakusanyaji |
| **CMake** | Jenereta ya mfumo wa kujenga (kiwango cha sekta) |
| **GDB / LLDB** | Watatuzi |
| **Valgrind / AnwaniSanitizer** | Utambuzi wa hitilafu ya kumbukumbu |
| **clang-tidy** | Linting na kisasa |
| **umbizo la kufoka** | Uumbizaji wa msimbo |
| **Conan / vcpkg** | Wasimamizi wa vifurushi |
| **Jaribio la Google / Catch2** | Mifumo ya majaribio |
---

## Wakati wa Kutumia C++
| Hali | Kwa nini C++ | Mbadala Bora |
|----------|---------|-------------------|
| Injini za mchezo | Utendaji + udhibiti wa wakati halisi | -- |
| Vivinjari | Miongo kadhaa ya nambari iliyoboreshwa | Kutu kwa vipengele vipya vya kivinjari |
| Biashara ya masafa ya juu | Mambo ya latency ya Microsecond | -- |
| Mifumo iliyopachikwa (tata) | Seti tajiri ya kipengele na ufikiaji wa maunzi | C kwa rahisi, Kutu kwa usalama |
| Programu za GUI (desktop) | Mfumo wa Qt umekomaa | C# (Windows), Swift (macOS) |
| Maendeleo ya maombi ya jumla | Changamano sana kwa programu nyingi | Python, Nenda, Java |
| Nyuma za wavuti | Sio chaguo la kawaida | Nenda, Rust, Node.js |
| Maandishi / otomatiki | Chombo kibaya kabisa | Python, JavaScript |
---

## Mageuzi ya Viwango vya C++
| Kawaida | Mwaka | Sifa Muhimu |
|----------|------|-------------|
| C++98 | 1998 | Kiwango cha asili cha ISO; STL, iostreams |
| C++11 | 2011 | **C++ ya kisasa huanza**: otomatiki, lambdas, viashiria mahiri, semantiki za kusonga |
| C++14 | 2014 | Lambdas za kawaida, std::make_unique, makato ya aina ya kurejesha |
| C++17 | 2017 | Vifungo vilivyopangwa, std::si lazima, std::lahaja, std::mfumo wa faili |
| C++20 | 2020 | **Toleo kuu**: dhana, safu, kanuni, moduli |
| C++23 | 2023 | std::inatarajiwa, std::print, ikionyesha hii |
Kwa miradi mipya, lenga C++20 kama kiwango cha chini zaidi.
---

## Maswali na Majibu Yaliyoundwa
### Q1: Kuna tofauti gani kati ya`std::unique_ptr`,`std::shared_ptr`, na`std::weak_ptr`?
**J:**`unique_ptr`inawakilisha umiliki wa kipekee - kielekezi kimoja pekee kinaweza kumiliki rasilimali. Ina sehemu ya juu ya sifuri (sawa na kielekezi mbichi) na haiwezi kunakiliwa, inasogezwa tu. `shared_ptr`inawakilisha umiliki ulioshirikiwa - viashiria vingi hushiriki rasilimali, na kuhesabu marejeleo. Wakati`shared_ptr`ya mwisho inapoharibiwa, rasilimali huachiliwa. `weak_ptr`ni mwangalizi asiyemiliki`shared_ptr`— haiongezi hesabu ya marejeleo na hutumiwa kuvunja marejeleo ya duara.
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

### Q2: Semantiki za hoja ni nini, na kwa nini zina umuhimu?
**J:** Hamisha semantiki (C++11) ruhusu uhamishaji wa rasilimali (kumbukumbu rundo, vishikio vya faili, n.k.) kutoka kwa kitu cha muda badala ya kuvinakili. Kijenzi/mgawo wa kuhamisha huchukua rejeleo la rvalue (`T&&`) na "huiba" rasilimali za chanzo, na kuiacha katika hali halali lakini isiyobainishwa. Hii huondoa nakala zisizo za lazima na ndiyo sababu uwekaji upya wa`std::vector`ni mzuri.
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

### Q3: Je, ni lini nitumie`auto`, na ni lini ninapaswa kubainisha aina kwa uwazi?
**J:** Tumia`auto`wakati aina ni dhahiri kutoka kwa muktadha (misururu ya violezo, simu za`make_unique`/ `make_shared`, aina za lambda, aina changamano za violezo). Bainisha aina kwa uwazi wakati aina si dhahiri, unapohitaji ubadilishaji kamili, au katika sahihi za API za umma. Mtindo wa "Almost Always Auto" (AAA) unapendelea`auto`kwa vigeu vya ndani; mtindo wa "auto ambapo inasaidia" ni wa kihafidhina zaidi.
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

### Q4: Je, dhana (C++20) huboresha vipi msimbo wa violezo?
**J:** Dhana hubana vigezo vya violezo kwa mahitaji yaliyotajwa, kutoa ujumbe wazi wa hitilafu na kuwezesha upakiaji wa kitendakazi kwenye vizuizi vya violezo. Kabla ya dhana, SFINAE na`static_assert`zilitumika - zote mbili zilitoa makosa ya siri. Dhana hufanya msimbo wa kiolezo kusomeka na kutunga.
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

### Q5: Kanuni ya Tano ni ipi, na inahusiana vipi na Kanuni ya Sifuri?
**J:** Kanuni ya Tano: ukifafanua mojawapo ya kiharibifu, kijenzi cha nakala, kazi ya kunakili, kijenzi cha kuhamisha, au mgawo wa kuhamisha, unapaswa kufafanua yote matano. Kanuni ya Sifuri (inayopendekezwa): madarasa ya kubuni ili yasihitaji yoyote kati ya haya - tumia aina za RAII (`std::string`,`std::vector`,`std::unique_ptr`) kama wanachama, na maalum zinazozalishwa na mkusanyaji zitafanya jambo sahihi kiotomatiki.
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

## Mlolongo-wa-Kutatua Matatizo
### Tatizo la 1: Tekeleza Foleni ya Mtayarishaji-Mteja-Salama yenye Masafa
**Taarifa ya Tatizo:** Tengeneza foleni iliyo na mipaka ya mzalishaji na mtumiaji kwa kutumia safu za C++20 kwa upande wa watumiaji. Foleni inapaswa kuzuia wazalishaji ikiwa imejaa na watumiaji wakati tupu, na iauni kuzima kwa njia nzuri.
**Hatua ya 1 - Elewa Tatizo:**
Tunahitaji: (1) foleni iliyo na mipaka iliyo na msukumo wa kuzuia/pop, (2) usalama wa nyuzi kupitia vigeu vya mutex na hali, (3) njia ya kuashiria kuzimwa, (4) muunganisho wa safu za C++20 ili watumiaji waweze kutumia kulingana na anuwai kwa vitanzi.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia`std::mutex`+`std::condition_variable`kwa kuzuia.
- Tumia`std::queue<T>`kama chombo cha msingi.
- Tumia`std::optional<T>`kama aina ya kurejesha —`std::nullopt`huashiria kuzimwa.
- Tekeleza kirudia-msingi cha sentinel kwa usaidizi wa safu.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa nyuzi:`std::mutex`inalinda hali zote za foleni; vigezo vya hali hushughulikia kuzuia.
- Kuzima kwa neema:`shutdown()`huwaamsha wahudumu wote; `pop()`hurejesha`nullopt`wakati tupu na kuzima.
- Usaidizi wa masafa: mlinzi wa kiboreshaji (cha-msingi-iliyoundwa) hulinganishwa sawa na kiboreshaji chochote kilichochoka.
- Uzalishaji: tumia`boost::lockfree::spsc_queue`kwa mzalishaji mmoja bila kufuli bila kufuli, au`folly::ProducerConsumerQueue`kwa matukio ya utendakazi wa hali ya juu.
### Tatizo la 2: Tekeleza Aina Iliyofutwa Aina Yoyote
**Taarifa ya Tatizo:** Tekeleza toleo lililorahisishwa la`std::any`(C++17) kuanzia mwanzo - chombo cha aina-salama cha thamani moja za aina yoyote, kinachoauni nakala, kusogeza na urejeshaji wa aina salama kupitia`any_cast`.
**Hatua ya 1 - Elewa Tatizo:**
`std::any`huhifadhi thamani ya aina yoyote inayoweza kunakiliwa na kuirejesha kwa kuangalia aina. Kwa ndani, hutumia ufutaji wa aina: kiolesura cha darasa la msingi na kiolezo kilichotolewa ambacho kinashikilia thamani halisi. `any_cast`hukagua aina iliyohifadhiwa wakati wa utekelezaji na kutupa`bad_any_cast`kwenye kutolingana.
**Hatua ya 2 — Tambua Mbinu:**
- Tumia darasa la msingi`HolderBase`na`clone()`na`type()`.
- Tumia kiolezo kilichotolewa`Holder<T>`ambacho huhifadhi thamani halisi.
- Hifadhi`std::unique_ptr<HolderBase>`katika darasa la `Any`.
-`any_cast<T>`hukagua`typeid`na kutekeleza a`static_cast`.
**Hatua ya 3 - Tekeleza Suluhisho:**
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

**Hatua ya 4 - Thibitisha na Uboreshe:**
- Usalama wa aina:`any_cast`hukagua`typeid`wakati wa utekelezaji — aina isiyo sahihi inarusha`BadAnyCast`.
- Nakili semantiki: mtandaoni`clone()`huunda nakala ya kina ya thamani iliyoshikiliwa.
- Sogeza semantiki: kijenzi/mgawo chaguomsingi wa kusogeza hamisha`unique_ptr`kwa ufanisi.
- Uboreshaji wa bafa ndogo (kama`std::any`halisi ): hifadhi aina ndogo ndogo ndani ya mstari bila mgao wa lundo. Hii inahitaji`union`iliyo na bafa ya baiti - ngumu zaidi.
- Uzalishaji: tumia`std::any`(C++17) - ni ya kawaida, imejaribiwa vizuri, na inaweza kujumuisha SBO.
---

## Muhtasari
C++ inachukua nafasi ya kipekee katika upangaji programu: hukupa utendakazi ghafi wa C na uwezo wa kujieleza wa vifupisho vya kiwango cha juu. C++ ya kisasa (C++20/23) ni lugha tofauti sana na C++ ya miaka ya 1990 -- ni salama zaidi, inaeleza zaidi, na ina tija zaidi. Mtazamo wa kujifunza ni mwinuko, na lugha huthawabisha nidhamu. Kwa programu muhimu za utendaji ambapo unahitaji udhibiti mzuri, C++ inasalia kuwa mojawapo ya zana bora zaidi zinazopatikana.