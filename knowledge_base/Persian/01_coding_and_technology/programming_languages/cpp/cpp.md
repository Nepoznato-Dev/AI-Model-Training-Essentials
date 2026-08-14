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
C++ یک زبان برنامه نویسی همه منظوره و کامپایل شده است که توسط Bjarne Stroustrup ایجاد شد و اولین بار در سال 1985 منتشر شد. این زبان C را با ویژگی های شی گرا، ژنریک و -- در نسخه های مدرن (C++11 و جدیدتر) -- انتزاعات سطح بالا مانند لامبدا، اشاره گرهای هوشمند و کتابخانه قالب استاندارد (STL) گسترش می دهد. C++ از اصل "انتزاع سربار صفر" پیروی می کند: نباید برای ویژگی هایی که استفاده نمی کنید هزینه ای پرداخت کنید.
C++ زمانی که به عملکرد بالا و قدرت بیان نیاز دارید، زبان انتخابی است. موتورهای بازی (Unreal Engine)، مرورگرها (Chrome، Firefox)، پایگاه‌های داده (MongoDB)، سیستم‌های عامل (بخش‌هایی از Windows و macOS)، سیستم‌های معاملات مالی و شبیه‌سازی‌های بلادرنگ را نیرو می‌دهد.
---

## چرا C++ مهم است
- ** عملکرد با بیان **: سرعت نزدیک به C با کلاس ها، قالب ها و انتزاع های مدرن.
- ** اصل سربار صفر **: انتزاع ها به همان کدی که با دست در C می نویسید کامپایل می شوند.
- **پایه کد عظیم**: چندین دهه زیرساخت حیاتی -- بازی ها، مرورگرها، پایگاه های داده، سیستم های تعبیه شده.
- **چند پارادایم**: از سبک های برنامه نویسی رویه ای، شی گرا، عمومی و تابعی پشتیبانی می کند.
- **تخریب قطعی**: RAII تضمین می کند که منابع به طور قابل پیش بینی پاکسازی می شوند - بدون مکث جمع آوری زباله.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **پیچیدگی** | زبان بسیار زیاد است -- حتی کارشناسان هم همه آن را نمی دانند | به C++ مدرن (C++17/20) پایبند باشید. اجتناب از الگوهای میراث |
| **ایمنی حافظه** | مدیریت حافظه دستی؛ اشاره گر آویزان، نشت، UB | از اشاره گرهای هوشمند، RAII و std::optional | استفاده کنید
| **زمان کامپایل** | کامپایل پروژه های بزرگ چند دقیقه طول می کشد | هدرهای از پیش کامپایل شده، ماژول ها (C++20)، ساخت های افزایشی |
| **پیام های خطا** | خطاهای الگو می تواند صدها خط باشد | استفاده از static_assert، مفاهیم (C++20)، کامپایلرهای بهتر |
| **سازگاری باینری** | ناپایداری ABI در نسخه های کامپایلر | رابط های C پایدار برای کتابخانه های مشترک |
---

## اصول نحو
### ساختار اساسی
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

### کلاس ها و برنامه نویسی شی گرا
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

### قالب ها (برنامه نویسی عمومی)
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

### ویژگی های مدرن C++ (C++17/20)
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

## کتابخانه استاندارد
### ظروف
| کانتینر | نوع | استفاده از When |
|-----------|------|----------|
| std::vector | آرایه پویا | انتخاب پیش فرض برای داده های متوالی |
| std::deque | صف دو طرفه | نیاز به درج/پاک کردن سریع در هر دو انتها |
| std::list | لیست پیوندی دوگانه | درج/پاک کردن مکرر در وسط |
| std::map | نقشه درخت سفارشی | نیاز به کلیدهای مرتب شده، جستجوی O(log n) |
| std::unordered_map | نقشه هش | جستجوی متوسط ​​O(1) سریع |
| std::set | ست سفارشی | عناصر مرتب شده منحصر به فرد |
| std::array | آرایه با اندازه ثابت | تخصیص پشته، اندازه شناخته شده در زمان کامپایل |
| std::string | متن | همیشه از این استفاده کنید، هرگز کاراکتر خام* |
### اشاره گرهای هوشمند
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

### الگوریتم ها
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

## نحو و الگوهای پیشرفته
### مفاهیم (C++20)
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

### Move Semantics و RAII
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

### سلسله مراتب استثنای سفارشی
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

## همزمانی و موازی
### std::thread و همگام سازی
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

### Async، Futures و Promises
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### نمونه تست گوگل
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

## قابلیت همکاری
### C Interop (خارجی "C")
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

## الگوهای طراحی
### الگوی کارخانه
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

### الگوی مشاهده گر
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### مثال بنچمارک (معیار گوگل)
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

### تکنیک های بهینه سازی
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

## استقرار
### استقرار داکر
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

## تالیف و ابزار
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| ابزار | هدف |
|------|---------|
| **GCC / Clang / MSVC ** | کامپایلر |
| **CMake** | ساخت سیستم ژنراتور (استاندارد صنعتی) |
| **GDB / LLDB** | اشکال زدا |
| **Valgrind / AddressSanitizer** | تشخیص خطای حافظه |
| **کلنگ و مرتب** | لینتینگ و نوسازی |
| **فرمت cang** | قالب بندی کد |
| **Conan / vcpkg** | مدیران بسته |
| **Google Test / Catch2** | تست چارچوب |
---

## چه زمانی از C++ استفاده کنیم
| سناریو | چرا C++ | جایگزین بهتر |
|----------|---------|-------------------|
| موتورهای بازی | عملکرد + کنترل بلادرنگ | -- |
| مرورگرها | چند دهه کد بهینه شده | زنگ برای اجزای جدید مرورگر |
| تجارت با فرکانس بالا | تأخیر میکروثانیه اهمیت دارد | -- |
| سیستم های تعبیه شده (پیچیده) | مجموعه ویژگی های غنی با دسترسی سخت افزاری | C برای ساده تر، زنگ برای ایمنی |
| برنامه های رابط کاربری گرافیکی (رومیزی) | فریمورک Qt بالغ است | سی شارپ (ویندوز)، سوئیفت (macOS) |
| توسعه برنامه عمومی | برای اکثر برنامه ها خیلی پیچیده است | پایتون، برو، جاوا |
| پشتیبان های وب | انتخاب معمولی نیست | برو، Rust، Node.js |
| اسکریپت / اتوماسیون | ابزار کاملا اشتباه | پایتون، جاوا اسکریپت |
---

## تکامل استانداردهای C++
| استاندارد | سال | ویژگی های کلیدی |
|----------|------|-------------|
| C++98 | 1998 | استاندارد ISO اصلی؛ STL، iostreams |
| C++11 | 2011 | **C++ مدرن شروع می شود**: خودکار، لامبدا، اشاره گرهای هوشمند، معناشناسی حرکت |
| C++14 | 2014 | لامبداهای عمومی، std::make_unique، نوع برگشتی کسر |
| C++17 | 2017 | اتصالات ساختاریافته، std::اختیاری، std::variant، std::فایل سیستم |
| C++20 | 2020 | **نسخه اصلی**: مفاهیم، ​​محدوده ها، روال ها، ماژول ها |
| C++23 | 2023 | std::expected، std::print، با استنباط این |
برای پروژه های جدید، حداقل C++20 را هدف قرار دهید.
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین `std::unique_ptr`،`std::shared_ptr`و`std::weak_ptr`چیست؟
**A:**`unique_ptr`مالکیت انحصاری را نشان می دهد - فقط یک اشاره گر می تواند مالک منبع باشد. سربار آن صفر است (همانند یک اشاره گر خام) و نمی توان آن را کپی کرد، فقط جابجا کرد. `shared_ptr`مالکیت مشترک را نشان می دهد - چندین اشاره گر منبع را با شمارش مرجع به اشتراک می گذارند. هنگامی که آخرین`shared_ptr`از بین می رود، منبع آزاد می شود. `weak_ptr`یک ناظر غیر مالک یک`shared_ptr`است - تعداد مراجع را افزایش نمی دهد و برای شکستن مراجع دایره ای استفاده می شود.
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

### Q2: معناشناسی حرکت چیست و چرا اهمیت دارد؟
**A:** Move semantics (C++11) امکان انتقال منابع (هپ حافظه، دسته فایل و غیره) را از یک شی موقت به جای کپی کردن آنها می دهد. یک سازنده/تخصیص حرکت یک مرجع rvalue (`T&&`) می گیرد و منابع منبع را "دزدیده" می کند و آن را در یک حالت معتبر اما نامشخص می گذارد. این کار کپی های غیر ضروری را حذف می کند و دلیل کارآمد بودن تخصیص مجدد`std::vector`است.
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

### Q3: چه زمانی باید از`auto`استفاده کنم، و چه زمانی باید به طور صریح انواع را مشخص کنم؟
**A:** از`auto`زمانی استفاده کنید که نوع از زمینه مشخص است (حلقه های تکرارکننده، فراخوانی های`make_unique`/ `make_shared`، انواع لامبدا، انواع الگوهای پیچیده). زمانی که نوع واضح نیست، زمانی که به تبدیل های ضمنی نیاز دارید یا در امضاهای عمومی API، انواع را به صراحت مشخص کنید. سبک "Almost Always Auto" (AAA)`auto`را برای متغیرهای محلی ترجیح می دهد. سبک "خودکار جایی که مفید است" محافظه کارانه تر است.
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

### Q4: چگونه مفاهیم (C++20) کد قالب را بهبود می بخشد؟
**الف:** مفاهیمی که پارامترهای قالب را با الزامات نامگذاری شده محدود می کند، پیام های خطای واضحی را تولید می کند و امکان بارگذاری بیش از حد تابع در محدودیت های الگو را فراهم می کند. قبل از مفاهیم، ​​از SFINAE و`static_assert`استفاده می شد - هر دو خطاهای مرموز ایجاد می کنند. مفاهیم، ​​کد قالب را قابل خواندن و ترکیب می کنند.
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

### Q5: قانون پنج چیست و چه ارتباطی با قانون صفر دارد؟
**الف:** قانون پنج: اگر هر کدام را از نوع تخریب کننده، سازنده کپی، تخصیص کپی، سازنده حرکت یا انتقال انتساب تعریف کنید، باید هر پنج را تعریف کنید. قانون صفر (ترجیحا): کلاس‌ها را طوری طراحی کنید که به هیچ یک از اینها نیاز نداشته باشند - از انواع RAII (`std::string`، `std::vector`، `std::unique_ptr`) به عنوان اعضا استفاده کنید، و ویژه‌های تولید شده توسط کامپایلر به طور خودکار کار درست را انجام می‌دهند.
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

## حل مسئله زنجیره ای از فکر
### مشکل 1: یک صف تولیدکننده-مصرف کننده ایمن رشته ای را با محدوده اجرا کنید
**بیانیه مشکل:** با استفاده از محدوده های C++20 برای طرف مصرف کننده، یک صف تولیدکننده-مصرف کننده محدود و ایمن بسازید. صف باید تولیدکنندگان را در مواقع پر و مصرف کنندگان را در حالت خالی مسدود کند و از تعطیلی دلپذیر پشتیبانی کند.
** مرحله 1 - مشکل را درک کنید:**
ما نیاز داریم: (1) یک صف محدود با مسدود کردن فشار/پاپ، (2) ایمنی رشته از طریق متغیرهای mutex و شرط، (3) راهی برای خاموش شدن سیگنال، (4) یکپارچه‌سازی محدوده‌های C++20 تا مصرف‌کنندگان بتوانند از حلقه‌های مبتنی بر محدوده استفاده کنند.
** مرحله 2 - شناسایی رویکرد: **
- برای مسدود کردن از`std::mutex`+`std::condition_variable`استفاده کنید.
- از`std::queue<T>`به عنوان ظرف زیرین استفاده کنید.
- از`std::optional<T>`به عنوان نوع برگشتی استفاده کنید — خاموش شدن سیگنال های `std::nullopt`.
- یک تکرار کننده مبتنی بر نگهبان برای پشتیبانی از محدوده ها پیاده سازی کنید.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی موضوع:`std::mutex`از تمام وضعیت صف محافظت می کند. متغیرهای شرط بلوک را کنترل می کنند.
- خاموش شدن برازنده:`shutdown()`همه پیشخدمت ها را بیدار می کند. `pop()``nullopt` را در صورت خالی و خاموش شدن برمی گرداند.
- پشتیبانی از محدوده: نگهبان تکرار کننده (ساخت پیش فرض) با هر تکرار کننده خسته مقایسه می شود.
- تولید: از`boost::lockfree::spsc_queue`برای تک‌مصرف‌کننده تک‌تولیدکننده بدون قفل یا`folly::ProducerConsumerQueue`برای سناریوهای پرتوان استفاده کنید.
### مشکل 2: یک Type-Erased Any Type را اجرا کنید
**بیانیه مشکل:** یک نسخه ساده شده از`std::any`(C++17) را از ابتدا اجرا کنید - یک محفظه ایمن برای مقادیر تکی از هر نوع، پشتیبانی از کپی، جابجایی و بازیابی ایمن نوع از طریق `any_cast`.
** مرحله 1 - مشکل را درک کنید:**
`std::any`یک مقدار از هر نوع قابل کپی را ذخیره می کند و با بررسی نوع آن را بازیابی می کند. در داخل، از نوع پاک کردن استفاده می کند: یک رابط کلاس پایه با یک الگوی مشتق شده که مقدار واقعی را نگه می دارد. `any_cast`نوع ذخیره شده را در زمان اجرا بررسی می کند و`bad_any_cast`را در عدم تطابق می اندازد.
** مرحله 2 - شناسایی رویکرد: **
- از کلاس پایه`HolderBase`با`clone()`و`type()`مجازی استفاده کنید.
- از یک الگوی مشتق شده`Holder<T>`استفاده کنید که مقدار واقعی را ذخیره می کند.
- یک`std::unique_ptr<HolderBase>`را در کلاس`Any`ذخیره کنید.
-`any_cast<T>``typeid` را بررسی می کند و`static_cast`را انجام می دهد.
**مرحله 3 - راه حل را اجرا کنید:**
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

** مرحله 4 - تأیید و بهینه سازی: **
- ایمنی نوع:`any_cast``typeid` را در زمان اجرا بررسی می کند - نوع اشتباه`BadAnyCast`را پرتاب می کند.
- معناشناسی کپی: مجازی`clone()`یک کپی عمیق از مقدار نگهداری شده ایجاد می کند.
- معناشناسی حرکت: سازنده/تخصیص حرکت پیش‌فرض`unique_ptr`را به طور موثر منتقل می‌کند.
- بهینه سازی بافر کوچک (مانند`std::any`واقعی): انواع کوچک را به صورت درون خطی و بدون تخصیص پشته ذخیره کنید. این به یک`union`با بافر بایت نیاز دارد - بسیار پیچیده تر.
- تولید: از`std::any`(C++17) استفاده کنید - استاندارد، به خوبی آزمایش شده است و ممکن است شامل SBO باشد.
---

## خلاصه
C++ جایگاه منحصر به فردی را در برنامه نویسی اشغال می کند: عملکرد خام C را با قدرت بیانی انتزاعات سطح بالا به شما می دهد. C++ مدرن (C++20/23) زبان بسیار متفاوتی با C++ دهه 1990 است -- ایمن تر، رساتر و سازنده تر است. منحنی یادگیری شیب دار است و زبان به نظم و انضباط پاداش می دهد. برای برنامه های کاربردی حیاتی که به کنترل دقیق نیاز دارید، C++ یکی از بهترین ابزارهای موجود باقی می ماند.