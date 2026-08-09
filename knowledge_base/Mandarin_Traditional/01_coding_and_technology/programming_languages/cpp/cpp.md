---
# Metadata
title: "C++"
description: "Comprehensive reference for the C++ programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
C++ 是一種通用的編譯型程式語言，由 Bjarne Stroustrup 創建，於 1985 年首次發布。它透過物件導向的功能、泛型以及現代版本（C++11 及更高版本）中的高階抽象（如 lambda、智慧型指標和標準範本庫 (STL)）擴展了 C。 C++ 遵循「零開銷抽象」原則：您不應該為不使用的功能付費。
當您需要高效能和表達能力時，C++ 是首選語言。它為遊戲引擎（虛幻引擎）、瀏覽器（Chrome、Firefox）、資料庫（MongoDB）、作業系統（Windows 和 macOS 的一部分）、金融交易系統和即時模擬提供支援。
---

## 為什麼 C++ 很重要
- **具有表現力的表現**：類別、模板和現代抽象的接近 C 的速度。
- **零開銷原則**：抽象編譯為與您在 C 中手動編寫的程式碼相同的程式碼。
- **龐大的程式碼庫**：數十年的關鍵基礎設施－遊戲、瀏覽器、資料庫、嵌入式系統。
- **多範式**：支援過程式、物件導向、泛型和函數式程式設計風格。
- **確定性銷毀**：RAII 確保可預測地清理資源 - 垃圾收集器不會暫停。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **複雜性** |語言浩瀚，即使是專家也無法全部掌握 |堅持使用現代 C++ (C++17/20)；避免遺留模式|
| **記憶體安全** |手動記憶體管理；懸空指標、洩漏、UB |使用智慧型指標、RAII 和 std::可選 |
| **編譯時間** |大型專案可能需要幾分鐘的時間來編譯 |預編譯頭檔、模組 (C++20)、增量建置 |
| **錯誤訊息** |模板錯誤可能長達數百行 |使用 static_assert、概念 (C++20)、更好的編譯器 |
| **二進位相容性** |跨編譯器版本的 ABI 不穩定 |共用函式庫的穩定 C 介面 |
---

## 文法基礎知識
### 基本結構
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

### 類別和物件導向編程
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

### 模板（通用程式設計）
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

### 現代 C++ 功能 (C++17/20)
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

## 標準庫
### 容器
|貨櫃|類型 |使用時間 |
|------------|------|----------|
| std::向量 |動態數組 |順序資料的預設選擇 |
| std::雙端佇列 |雙端佇列|需要在兩端快速插入/擦除|
| std::清單 |雙向鍊錶|經常在中間插入/擦除 |
| std::地圖 |有序樹圖|需要排序鍵，O(log n) 尋找 |
| std::unordered_map | std::unordered_map |哈希圖 |快速 O(1) 平均查找 |
|標準::設定|訂購套裝 |獨特的排序元素 |
| std::數組 |固定大小數組 |堆疊分配，編譯時已知大小 |
| std::字串 |文字|總是使用它，切勿使用原始字元* |
### 智慧指針
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

### 演算法
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

## 進階語法和模式
### 概念 (C++20)
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

### 移動語意和 RAII
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

### 自訂異常層次結構
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

## 並發與平行
### std::thread 和同步
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

### 非同步、Futures 和 Promise
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

## 專案配置與建置系統
### 專案結構
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

### CI/CD 管道 (GitHub Actions)
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

## 測試
### 谷歌測試範例
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

## 互通性
### C 互通（外部「C」）
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

## 設計模式
### 工廠模式
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

### 觀察者模式
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

## 效能與最佳化
### 分析工具
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### 基準範例（Google 基準）
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

### 優化技術
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

## 部署
### Docker 部署
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

## 編譯和工具
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

|工具|目的|
|------|---------|
| **GCC / Clang / MSVC** |編譯器 |
| **CMake** |建置系統產生器（業界標準）|
| **GDB / LLDB** |偵錯器|
| **Valgrind / AddressSanitizer** |記憶體錯誤檢測|
| **整潔** | Linting 和現代化 |
| **clang 格式** |程式碼格式化 |
| **柯南/vcpkg** |套件管理器 |
| **Google測試/Catch2** |測試框架|
---

## 何時使用 C++
|場景 |為什麼選擇 C++ |更好的選擇|
|----------|---------|--------------------|
|遊戲引擎|效能+即時控制| --|
|瀏覽器 |數十年的最佳化程式碼 | Rust 用於新的瀏覽器元件 |
|高頻交易|微秒延遲很重要 | --|
|嵌入式系統（複雜）|具有硬體存取功能的豐富功能集 | C 更簡單，Rust 更安全 |
| GUI 應用程式（桌面）| Qt框架成熟| C# (Windows)、Swift (macOS) |
|通用應用程式開發|對於大多數應用程式來說太複雜 | Python、Go、Java |
|網路後端 |不是典型的選擇 | Go、Rust、Node.js |
|腳本/自動化 |完全錯誤的工具| Python、JavaScript |
---

## C++ 標準演進
|標準|年份|主要特點|
|----------|------|-------------|
| C++98 | C++98 1998 |原始ISO標準； STL、iostreams |
| C++11 | C++11 2011 | **現代 C++ 開始**：自動、lambda、智慧型指標、移動語意 |
| C++14 | C++14 2014 |通用 lambda、std::make_unique、回傳型別推導 |
| C++17 | C++17 2017 | 2017結構化綁定、std::可選、std::variant、std::filesystem |
| C++20 | C++20 2020 | **主要版本**：概念、範圍、協程、模組 |
| C++23 | C++23 2023 | std::expected，std::print，推導出這個 |
對於新項目，至少以 C++20 為目標。
---

＃＃ 概括
C++ 在程式設計中佔有獨特的地位：它為您提供 C 的原始效能以及高階抽象的表達能力。現代 C++ (C++20/23) 是一種與 20 世紀 90 年代的 C++ 截然不同的語言 — 它更安全、更具表現力、也更有效率。學習曲線陡峭，語言獎勵紀律。對於需要細粒度控制的效能關鍵型應用程序，C++ 仍然是最好的可用工具之一。