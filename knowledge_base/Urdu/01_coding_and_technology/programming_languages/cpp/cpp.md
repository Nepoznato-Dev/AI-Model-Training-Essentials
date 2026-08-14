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
C++ ایک عام مقصد کی، مرتب کردہ پروگرامنگ لینگویج ہے جسے Bjarne Stroustrup نے پہلی بار 1985 میں ریلیز کیا تھا۔ یہ C کو آبجیکٹ اورینٹڈ خصوصیات، جنرک، اور -- جدید ورژن (C++11 اور بعد میں) کے ساتھ پھیلاتا ہے -- اعلی سطحی تجریدات جیسے لیمبڈاس، سمارٹ پوائنٹرز، اور معیاری ٹیمپلیٹ (LSTbr)۔ C++ "zero-overhead abstraction" کے اصول کی پیروی کرتا ہے: آپ کو ان خصوصیات کے لیے ادائیگی نہیں کرنی چاہیے جو آپ استعمال نہیں کرتے ہیں۔
جب آپ کو اعلی کارکردگی اور اظہار کی طاقت دونوں کی ضرورت ہوتی ہے تو C++ انتخاب کی زبان ہوتی ہے۔ یہ گیم انجنز (غیر حقیقی انجن)، براؤزرز (کروم، فائر فاکس)، ڈیٹا بیسز (MongoDB)، آپریٹنگ سسٹمز (ونڈوز اور میک او ایس کے حصے)، مالیاتی تجارتی نظام، اور ریئل ٹائم سمولیشنز کو طاقت دیتا ہے۔
---

## کیوں C++ اہمیت رکھتا ہے۔
- **اظہار کے ساتھ کارکردگی**: کلاسز، ٹیمپلیٹس، اور جدید تجریدوں کے ساتھ قریب-C رفتار۔
- **زیرو-اوور ہیڈ اصول**: تجرید اسی کوڈ پر مرتب ہوتے ہیں جسے آپ C میں ہاتھ سے لکھیں گے۔
- **بڑے پیمانے پر کوڈبیس**: کئی دہائیوں کا اہم انفراسٹرکچر -- گیمز، براؤزرز، ڈیٹا بیس، ایمبیڈڈ سسٹمز۔
- **متعدد تمثیل**: طریقہ کار، آبجیکٹ پر مبنی، عام، اور فنکشنل پروگرامنگ اسٹائل کو سپورٹ کرتا ہے۔
- **ڈیٹرمنسٹک تباہی**: RAII یقینی بناتا ہے کہ وسائل کو پیش گوئی کے مطابق صاف کیا جاتا ہے -- کوئی کوڑا اٹھانے والا توقف نہیں کرتا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **پیچیدگی** | زبان بہت بڑی ہے -- یہاں تک کہ ماہرین بھی یہ سب نہیں جانتے | جدید C++ (C++17/20) پر قائم رہیں؛ میراثی نمونوں سے بچیں |
| **میموری سیفٹی** | دستی میموری کا انتظام؛ لٹکنے والے پوائنٹرز، لیک، UB | سمارٹ پوائنٹرز، RAII، اور std::optional | استعمال کریں۔
| ** مرتب اوقات** | بڑے منصوبوں کو مرتب کرنے میں منٹ لگ سکتے ہیں | پہلے سے مرتب کردہ ہیڈر، ماڈیولز (C++20)، انکریمنٹل بلڈز |
| **خرابی کے پیغامات** | ٹیمپلیٹ کی غلطیاں سینکڑوں لائنیں لمبی ہو سکتی ہیں | static_asssert، تصورات (C++20)، بہتر کمپائلرز استعمال کریں۔
| **بائنری مطابقت** | کمپائلر ورژن میں ABI عدم استحکام | مشترکہ لائبریریوں کے لیے مستحکم C انٹرفیس |
---

## نحوی بنیادی باتیں
### بنیادی ڈھانچہ
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

### کلاسز اور آبجیکٹ اورینٹڈ پروگرامنگ
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

### ٹیمپلیٹس (عام پروگرامنگ)
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

### جدید C++ خصوصیات (C++17/20)
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

## معیاری لائبریری
### کنٹینرز
| کنٹینر | قسم | استعمال کریں جب |
|------------|------|---------|
| std::vector | متحرک صف | ترتیب وار ڈیٹا کے لیے پہلے سے طے شدہ انتخاب |
| std::deque | دوہری قطار | دونوں سروں پر تیزی سے داخل/مٹانے کی ضرورت ہے |
| std::list | دوہری منسلک فہرست | درمیان میں بار بار ڈالنا/مٹانا |
| std::map | آرڈر شدہ درخت کا نقشہ | ترتیب شدہ چابیاں کی ضرورت ہے، O(log n) تلاش |
| std::unordered_map | ہیش نقشہ | فاسٹ O(1) اوسط تلاش |
| std::set | آرڈر شدہ سیٹ | منفرد ترتیب شدہ عناصر |
| std::array | فکسڈ سائز کی صف | ڈھیر سے مختص، مرتب وقت پر معلوم سائز |
| std::string | متن | اسے ہمیشہ استعمال کریں، کبھی خام چار* |
### اسمارٹ پوائنٹرز
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

### الگورتھم
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

## اعلی درجے کی نحو اور نمونے۔
### تصورات (C++20)
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

### سیمنٹکس اور RAII کو منتقل کریں۔
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

### اپنی مرضی کے استثنائی درجہ بندی
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

## ہم آہنگی اور ہم آہنگی
### std::تھریڈ اور سنکرونائزیشن
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

### Async، مستقبل، اور وعدے
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ
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

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### گوگل ٹیسٹ کی مثال
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

## انٹرآپریبلٹی
### C انٹراپ (بیرونی "C")
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

## ڈیزائن پیٹرن
### فیکٹری پیٹرن
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

### مبصر پیٹرن
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### بینچ مارک کی مثال (گوگل بینچ مارک)
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### ڈاکر کی تعیناتی۔
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

## تالیف اور ٹولنگ
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| ٹول | مقصد |
|------|---------|
| **GCC / بجنا / MSVC** | مرتب کرنے والے |
| **CMake** | سسٹم جنریٹر بنائیں (صنعت کا معیار) |
| **GDB / LLDB** | ڈیبگرز |
| **والگرینڈ / ایڈریس سینیٹائزر** | میموری کی خرابی کا پتہ لگانا |
| **بنانا صاف** | لنٹنگ اور جدید کاری |
| **کلنگ فارمیٹ** | کوڈ فارمیٹنگ |
| **کانن / vcpkg** | پیکیج مینیجرز |
| **گوگل ٹیسٹ / کیچ 2** | جانچ کے فریم ورک |
---

## C++ کب استعمال کریں۔
| منظر نامہ | کیوں C++ | بہتر متبادل |
|------------|---------|-------------------|
| گیم انجن | کارکردگی + ریئل ٹائم کنٹرول | -- |
| براؤزرز | آپٹمائزڈ کوڈ کی دہائیاں | براؤزر کے نئے اجزاء کے لیے مورچا |
| اعلی تعدد ٹریڈنگ | مائیکرو سیکنڈ لیٹینسی کے معاملات | -- |
| ایمبیڈڈ سسٹمز (پیچیدہ) | ہارڈ ویئر تک رسائی کے ساتھ رچ فیچر سیٹ | سی آسان کے لیے، حفاظت کے لیے مورچا |
| GUI ایپلی کیشنز (ڈیسک ٹاپ) | Qt فریم ورک بالغ ہے | C# (ونڈوز)، سوئفٹ (macOS) |
| عام درخواست کی ترقی | زیادہ تر ایپس کے لیے بہت پیچیدہ | ازگر، گو، جاوا |
| ویب بیک اینڈز | عام انتخاب نہیں | Go, Rust, Node.js |
| سکرپٹ / آٹومیشن | غلط ٹول مکمل طور پر | Python, JavaScript |
---

## C++ معیارات کا ارتقا
| معیاری | سال | اہم خصوصیات |
|------------|------|------------|
| C++98 | 1998 | اصل ISO معیار؛ STL، iostreams |
| C++11 | 2011 | **جدید C++ شروع ہوتا ہے**: آٹو، لیمبڈاس، سمارٹ پوائنٹرز، موو سیمنٹکس |
| C++14 | 2014 | عام لیمبڈاس، std::make_unique، واپسی کی قسم کی کٹوتی |
| C++17 | 2017 | سٹرکچرڈ بائنڈنگز، std::optional, std::variant, std::filesystem |
| C++20 | 2020 | **بڑی ریلیز**: تصورات، رینجز، کوروٹینز، ماڈیولز |
| C++23 | 2023 | std::expected, std::print, deducing this |
نئے پروجیکٹس کے لیے، کم از کم C++20 کو ہدف بنائیں۔
---

## مصنوعی سوال و جواب
### Q1: `std::unique_ptr`، `std::shared_ptr`، اور`std::weak_ptr`میں کیا فرق ہے؟
**A:**`unique_ptr`خصوصی ملکیت کی نمائندگی کرتا ہے — صرف ایک پوائنٹر وسائل کا مالک ہوسکتا ہے۔ اس میں صفر اوور ہیڈ (ایک خام پوائنٹر کی طرح) ہے اور اسے کاپی نہیں کیا جا سکتا، صرف منتقل کیا جا سکتا ہے۔ `shared_ptr`مشترکہ ملکیت کی نمائندگی کرتا ہے - ایک سے زیادہ پوائنٹرز حوالہ شمار کے ساتھ وسائل کا اشتراک کرتے ہیں۔ جب آخری`shared_ptr`تباہ ہو جاتا ہے، تو وسائل کو آزاد کر دیا جاتا ہے۔ `weak_ptr`ایک`shared_ptr`کا غیر مالک مبصر ہے — یہ حوالہ کی تعداد میں اضافہ نہیں کرتا اور سرکلر حوالہ جات کو توڑنے کے لیے استعمال ہوتا ہے۔
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

### Q2: حرکت کے الفاظ کیا ہیں، اور وہ کیوں اہمیت رکھتے ہیں؟
**A:** Move semantics (C++11) وسائل (ہیپ میموری، فائل ہینڈلز وغیرہ) کو نقل کرنے کے بجائے کسی عارضی چیز سے منتقل کرنے کی اجازت دیتا ہے۔ ایک حرکت کنسٹرکٹر/اسائنمنٹ ایک rvalue حوالہ (`T&&` ) لیتا ہے اور ماخذ کے وسائل کو "چوری" کرتا ہے، اسے درست لیکن غیر متعینہ حالت میں چھوڑ دیتا ہے۔ اس سے غیر ضروری کاپیاں ختم ہو جاتی ہیں اور یہی وجہ ہے کہ`std::vector`ری لوکیشن موثر ہے۔
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

Q3
**A:** جب قسم سیاق و سباق سے واضح ہو تو`auto`استعمال کریں (اعتراف کرنے والے لوپس،`make_unique`/`make_shared`کالز، لیمبڈا کی اقسام، پیچیدہ ٹیمپلیٹ کی قسمیں)۔ جب قسم واضح نہ ہو، جب آپ کو مضمر تبادلوں کی ضرورت ہو، یا عوامی API دستخطوں میں واضح طور پر قسموں کی وضاحت کریں۔ "Almost Always Auto" (AAA) طرز مقامی متغیرات کے لیے`auto`کی حمایت کرتا ہے۔ "آٹو جہاں مددگار" انداز زیادہ قدامت پسند ہے۔
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

### Q4: تصورات (C++20) ٹیمپلیٹ کوڈ کو کیسے بہتر بناتے ہیں؟
**A:** تصورات نامی تقاضوں کے ساتھ ٹیمپلیٹ کے پیرامیٹرز کو روکتے ہیں، واضح غلطی کے پیغامات تیار کرتے ہیں اور ٹیمپلیٹ کی رکاوٹوں پر فنکشن اوورلوڈنگ کو فعال کرتے ہیں۔ تصورات سے پہلے، SFINAE اور`static_assert`استعمال کیے جاتے تھے - دونوں خفیہ غلطیاں پیدا کرتے ہیں۔ تصورات ٹیمپلیٹ کوڈ کو پڑھنے کے قابل اور کمپوز ایبل بناتے ہیں۔
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

### Q5: پانچ کا قاعدہ کیا ہے، اور اس کا صفر کے اصول سے کیا تعلق ہے؟
**A:** پانچوں کا اصول: اگر آپ ڈسٹرکٹر، کاپی کنسٹرکٹر، کاپی اسائنمنٹ، موو کنسٹرکٹر، یا اسائنمنٹ میں سے کسی ایک کی وضاحت کرتے ہیں تو آپ کو پانچوں کی تعریف کرنی چاہیے۔ زیرو کا اصول (ترجیحی): کلاسز کو ڈیزائن کریں تاکہ انہیں ان میں سے کسی کی ضرورت نہ ہو — RAII اقسام (`std::string`,`std::vector`,`std::unique_ptr`) کو بطور ممبر استعمال کریں، اور مرتب کرنے والے کی طرف سے تیار کردہ خصوصی خود بخود صحیح کام کریں گے۔
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

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: رینج کے ساتھ ایک تھریڈ-محفوظ پروڈیوسر-صارف قطار لاگو کریں
**مسئلہ کا بیان:** صارفین کے لیے C++20 رینجز کا استعمال کرتے ہوئے دھاگے سے محفوظ پروڈیوسر صارفین کی قطار بنائیں۔ قطار کو پروڈیوسرز کو مکمل ہونے پر اور صارفین کو خالی ہونے پر بلاک کرنا چاہیے، اور خوبصورت بندش کی حمایت کرنا چاہیے۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
ہمیں ضرورت ہے: (1) بلاکنگ پش/پاپ کے ساتھ ایک باؤنڈڈ قطار، (2) میوٹیکس اور کنڈیشن ویری ایبلز کے ذریعے تھریڈ سیفٹی، (3) سگنل شٹ ڈاؤن کا طریقہ، (4) C++20 رینجز انضمام تاکہ صارفین لوپس کے لیے رینج پر مبنی استعمال کر سکیں۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- بلاک کرنے کے لیے`std::mutex`+`std::condition_variable`استعمال کریں۔
-`std::queue<T>`کو بنیادی کنٹینر کے طور پر استعمال کریں۔
-`std::optional<T>`کو واپسی کی قسم کے طور پر استعمال کریں -`std::nullopt`سگنل بند۔
- رینج سپورٹ کے لیے ایک سنٹینل پر مبنی ایٹریٹر کو لاگو کریں۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- تھریڈ سیفٹی:`std::mutex`تمام قطار کی حالت کی حفاظت کرتا ہے۔ حالت متغیر بلاکنگ کو ہینڈل کرتے ہیں۔
- شاندار شٹ ڈاؤن:`shutdown()`تمام ویٹروں کو جگا دیتا ہے۔ `pop()`خالی اور بند ہونے پر`nullopt`لوٹاتا ہے۔
- رینج سپورٹ: تکرار کرنے والے کا سینٹینل (پہلے سے طے شدہ) کسی بھی ختم ہونے والے تکرار کرنے والے کے برابر موازنہ کرتا ہے۔
- پیداوار: لاک فری سنگل پروڈیوسر سنگل کنزیومر کے لیے `boost::lockfree::spsc_queue`، یا`folly::ProducerConsumerQueue`ہائی تھرو پٹ منظرناموں کے لیے استعمال کریں۔
### مسئلہ 2: کسی بھی قسم کو مٹانے والی قسم کو لاگو کریں۔
**مسئلہ کا بیان:**`std::any`(C++17) کے ایک آسان ورژن کو شروع سے لاگو کریں — کسی بھی قسم کی واحد اقدار کے لیے ایک ٹائپ سیف کنٹینر،`any_cast`کے ذریعے کاپی، منتقل، اور ٹائپ سیف بازیافت۔
**مرحلہ 1 - مسئلہ کو سمجھیں:**
`std::any`کسی بھی قابل نقل قسم کی قدر کو ذخیرہ کرتا ہے اور اسے ٹائپ چیکنگ کے ساتھ بازیافت کرتا ہے۔ اندرونی طور پر، یہ ٹائپ ایریزر کا استعمال کرتا ہے: ایک اخذ کردہ ٹیمپلیٹ کے ساتھ ایک بیس کلاس انٹرفیس جو اصل قدر رکھتا ہے۔ `any_cast`رن ٹائم کے وقت ذخیرہ شدہ قسم کو چیک کرتا ہے اور`bad_any_cast`کو غیر مماثل ہونے پر پھینک دیتا ہے۔
**مرحلہ 2 — نقطہ نظر کی شناخت کریں:**
- ورچوئل`clone()`اور`type()`کے ساتھ بیس کلاس`HolderBase`استعمال کریں۔
- ایک اخذ کردہ ٹیمپلیٹ`Holder<T>`استعمال کریں جو اصل قیمت کو محفوظ کرتا ہے۔
-`std::unique_ptr<HolderBase>`کو`Any`کلاس میں اسٹور کریں۔
-`any_cast<T>``typeid` کو چیک کرتا ہے اور ایک`static_cast`انجام دیتا ہے۔
**مرحلہ 3 — حل کو نافذ کریں:**
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

**مرحلہ 4 — تصدیق کریں اور بہتر بنائیں:**
- قسم کی حفاظت:`any_cast`رن ٹائم پر`typeid`کو چیک کرتا ہے — غلط قسم پھینکتی ہے `BadAnyCast`۔
- کاپی سیمنٹکس: ورچوئل`clone()`رکھی ہوئی قدر کی گہری کاپی بناتا ہے۔
- سیمنٹکس کو منتقل کریں: ڈیفالٹ موو کنسٹرکٹر/اسائنمنٹ`unique_ptr`کو مؤثر طریقے سے منتقل کرتا ہے۔
- چھوٹی بفر آپٹیمائزیشن (جیسے اصلی `std::any`): ہیپ ایلوکیشن کے بغیر چھوٹی اقسام کو ان لائن اسٹور کریں۔ اس کے لیے بائٹ بفر کے ساتھ`union`کی ضرورت ہے — نمایاں طور پر زیادہ پیچیدہ۔
- پیداوار: استعمال کریں`std::any`(C++17) — یہ معیاری، اچھی طرح سے ٹیسٹ شدہ ہے، اور اس میں SBO شامل ہو سکتا ہے۔
---

## خلاصہ
C++ پروگرامنگ میں ایک منفرد مقام رکھتا ہے: یہ آپ کو اعلی سطحی تجرید کی اظہاری طاقت کے ساتھ C کی خام کارکردگی فراہم کرتا ہے۔ جدید C++ (C++ 20/23) 1990 کی دہائی کی C++ سے بہت مختلف زبان ہے -- یہ زیادہ محفوظ، زیادہ اظہار خیال اور زیادہ نتیجہ خیز ہے۔ سیکھنے کا منحنی خطوط کھڑا ہے، اور زبان نظم و ضبط کا بدلہ دیتی ہے۔ کارکردگی کے لحاظ سے اہم ایپلی کیشنز کے لیے جہاں آپ کو عمدہ کنٹرول کی ضرورت ہے، C++ دستیاب بہترین ٹولز میں سے ایک ہے۔