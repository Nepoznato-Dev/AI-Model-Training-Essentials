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
# সি++
C++ হল একটি সাধারণ-উদ্দেশ্য, সংকলিত প্রোগ্রামিং ভাষা যা Bjarne Stroustrup দ্বারা তৈরি করা হয়েছে, যা প্রথম 1985 সালে প্রকাশিত হয়েছিল। এটি C অবজেক্ট-ওরিয়েন্টেড বৈশিষ্ট্য, জেনেরিক, এবং -- আধুনিক সংস্করণে (C++11 এবং পরবর্তী) -- ল্যাম্বডাস, স্মার্ট পয়েন্টার এবং স্ট্যান্ডার্ড টেমপ্লেট (LSTbr Library) এর মতো উচ্চ-স্তরের বিমূর্ততা সহ C প্রসারিত করে। C++ "জিরো-ওভারহেড অ্যাবস্ট্রাকশন" নীতি অনুসরণ করে: আপনি ব্যবহার করেন না এমন বৈশিষ্ট্যগুলির জন্য আপনাকে অর্থ প্রদান করা উচিত নয়।
C++ হল পছন্দের ভাষা যখন আপনার উচ্চ কার্যক্ষমতা এবং অভিব্যক্তিপূর্ণ শক্তি উভয়েরই প্রয়োজন হয়। এটি গেম ইঞ্জিন (অবাস্তব ইঞ্জিন), ব্রাউজার (ক্রোম, ফায়ারফক্স), ডেটাবেস (মঙ্গোডিবি), অপারেটিং সিস্টেম (উইন্ডোজ এবং ম্যাকওএসের অংশ), আর্থিক ট্রেডিং সিস্টেম এবং রিয়েল-টাইম সিমুলেশনগুলিকে শক্তি দেয়৷
---

## কেন C++ ব্যাপার
- **অভিব্যক্তি সহ কর্মক্ষমতা**: ক্লাস, টেমপ্লেট এবং আধুনিক বিমূর্ততা সহ কাছাকাছি-সি গতি।
- **জিরো-ওভারহেড নীতি**: বিমূর্ততা একই কোডে কম্পাইল করে যা আপনি C এ হাতে লিখবেন।
- **ম্যাসিভ কোডবেস**: কয়েক দশকের গুরুত্বপূর্ণ অবকাঠামো -- গেম, ব্রাউজার, ডাটাবেস, এমবেডেড সিস্টেম।
- **মাল্টি-প্যারাডাইম**: পদ্ধতিগত, অবজেক্ট-ওরিয়েন্টেড, জেনেরিক এবং কার্যকরী প্রোগ্রামিং শৈলী সমর্থন করে।
- **নিয়ন্ত্রিক ধ্বংস**: RAII নিশ্চিত করে যে সংস্থানগুলি অনুমানযোগ্যভাবে পরিষ্কার করা হয়েছে -- কোনো আবর্জনা সংগ্রহকারী বিরতি দেয় না।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **জটিলতা** | ভাষাটি বিশাল -- এমনকি বিশেষজ্ঞরাও এর সব কিছুই জানেন না | আধুনিক C++ (C++17/20); উত্তরাধিকার নিদর্শন এড়িয়ে চলুন |
| **মেমরি নিরাপত্তা** | ম্যানুয়াল মেমরি ব্যবস্থাপনা; ঝুলন্ত পয়েন্টার, ফাঁস, UB | স্মার্ট পয়েন্টার, RAII, এবং std::optional | ব্যবহার করুন
| **সময় কম্পাইল** | বড় প্রকল্পগুলি কম্পাইল করতে মিনিট সময় নিতে পারে | প্রি-কম্পাইল করা হেডার, মডিউল (C++20), ইনক্রিমেন্টাল বিল্ডস |
| **ত্রুটি বার্তা** | টেমপ্লেট ত্রুটি শত শত লাইন দীর্ঘ হতে পারে | static_assert, ধারণা (C++20), আরও ভালো কম্পাইলার ব্যবহার করুন
| **বাইনারী সামঞ্জস্য** | কম্পাইলার সংস্করণ জুড়ে ABI অস্থিরতা | শেয়ার্ড লাইব্রেরির জন্য স্থিতিশীল সি ইন্টারফেস |
---

## সিনট্যাক্স মৌলিক
### মৌলিক কাঠামো
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

### ক্লাস এবং অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং
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

### টেমপ্লেট (জেনারিক প্রোগ্রামিং)
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

### আধুনিক C++ বৈশিষ্ট্য (C++17/20)
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

## স্ট্যান্ডার্ড লাইব্রেরি
### ধারক
| ধারক | প্রকার | কখন ব্যবহার করুন |
|------------|------|----------|
| std::ভেক্টর | ডায়নামিক অ্যারে | ক্রমিক ডেটার জন্য ডিফল্ট পছন্দ |
| std::deque | ডবল-এন্ডেড সারি | উভয় প্রান্তে দ্রুত সন্নিবেশ/মুছে ফেলতে হবে |
| std::তালিকা | দ্বৈত-সংযুক্ত তালিকা | মাঝখানে ঘন ঘন সন্নিবেশ/মুছে ফেলুন |
| std::মানচিত্র | অর্ডার করা গাছের মানচিত্র | সাজানো কী দরকার, O(log n) লুকআপ |
| std::unordered_map | হ্যাশ মানচিত্র | দ্রুত O(1) গড় লুকআপ |
| std::set | অর্ডার করা সেট | অনন্য সাজানো উপাদান |
| std:: array | স্থির-আকার অ্যারে | স্ট্যাক-বরাদ্দ, কম্পাইলের সময় পরিচিত আকার |
| std::স্ট্রিং | পাঠ্য | সর্বদা এটি ব্যবহার করুন, কখনই কাঁচা চর* |
### স্মার্ট পয়েন্টার
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

### অ্যালগরিদম
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### ধারণা (C++20)
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

### শব্দার্থবিদ্যা এবং RAII সরান
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

### কাস্টম ব্যতিক্রম শ্রেণিবিন্যাস
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

## সামঞ্জস্য এবং সমান্তরালতা
### std::থ্রেড এবং সিঙ্ক্রোনাইজেশন
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

### অ্যাসিঙ্ক, ফিউচার এবং প্রতিশ্রুতি
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো
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

### CI/CD পাইপলাইন (GitHub অ্যাকশন)
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

## পরীক্ষা
### গুগল টেস্টের উদাহরণ
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

## ইন্টারঅপারেবিলিটি
### সি ইন্টারপ (বাহ্যিক "সি")
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

## ডিজাইন প্যাটার্ন
### কারখানার প্যাটার্ন
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

### পর্যবেক্ষক প্যাটার্ন
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### বেঞ্চমার্ক উদাহরণ (গুগল বেঞ্চমার্ক)
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

### অপ্টিমাইজেশন কৌশল
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

## স্থাপনা
### ডকার স্থাপনা
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

## সংকলন এবং টুলিং
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| টুল | উদ্দেশ্য |
|------|---------|
| **GCC / ক্ল্যাং / MSVC** | কম্পাইলার |
| **সিমেক** | সিস্টেম জেনারেটর তৈরি করুন (শিল্প মান) |
| **GDB / LLDB** | ডিবাগার |
| **ভালগ্রিন্ড/অ্যাড্রেস স্যানিটাইজার** | মেমরি ত্রুটি সনাক্তকরণ |
| **ঘনঘন-পরিপাটি** | লিন্টিং এবং আধুনিকীকরণ |
| **ক্ল্যাং-ফর্ম্যাট** | কোড ফরম্যাটিং |
| **কোনান / ভিসিপিকেজি** | প্যাকেজ ম্যানেজার |
| **গুগল টেস্ট / ক্যাচ২** | পরীক্ষার কাঠামো |
---

## কখন C++ ব্যবহার করবেন
| দৃশ্যকল্প | কেন C++ | ভাল বিকল্প |
|------------|---------|---------|
| গেম ইঞ্জিন | কর্মক্ষমতা + রিয়েল-টাইম নিয়ন্ত্রণ | -- |
| ব্রাউজার | অপ্টিমাইজড কোডের দশক | নতুন ব্রাউজার উপাদানের জন্য মরিচা |
| উচ্চ ফ্রিকোয়েন্সি ট্রেডিং | মাইক্রোসেকেন্ড লেটেন্সি ব্যাপার | -- |
| এমবেডেড সিস্টেম (জটিল) | হার্ডওয়্যার অ্যাক্সেস সহ সমৃদ্ধ বৈশিষ্ট্য সেট | সি সহজতর জন্য, নিরাপত্তার জন্য মরিচা |
| GUI অ্যাপ্লিকেশন (ডেস্কটপ) | Qt ফ্রেমওয়ার্ক পরিপক্ক | C# (উইন্ডোজ), সুইফট (macOS) |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | বেশিরভাগ অ্যাপের জন্য খুব জটিল | পাইথন, গো, জাভা |
| ওয়েব ব্যাকএন্ড | সাধারণ পছন্দ নয় | Go, Rust, Node.js |
| স্ক্রিপ্টিং / অটোমেশন | সম্পূর্ণরূপে ভুল টুল | পাইথন, জাভাস্ক্রিপ্ট |
---

## সি++ স্ট্যান্ডার্ড বিবর্তন
| স্ট্যান্ডার্ড | বছর | মূল বৈশিষ্ট্য |
|----------|------|---------------|
| C++98 | 1998 | মূল ISO মান; STL, iostreams |
| C++11 | 2011 | **আধুনিক C++ শুরু হয়**: অটো, ল্যাম্বডাস, স্মার্ট পয়েন্টার, মুভ শব্দার্থবিদ্যা |
| C++14 | 2014 | জেনেরিক ল্যাম্বডাস, std::make_unique, রিটার্ন টাইপ ডিডাকশন |
| C++17 | 2017 | স্ট্রাকচার্ড বাইন্ডিং, std::optional, std::variant, std::filesystem |
| C++20 | 2020 | **প্রধান রিলিজ**: ধারণা, রেঞ্জ, কোরোটিন, মডিউল |
| C++23 | 2023 | std::প্রত্যাশিত, std::প্রিন্ট, এটি ডিডিউসিং |
নতুন প্রকল্পের জন্য, ন্যূনতম হিসাবে C++20 লক্ষ্য করুন।
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: `std::unique_ptr`,`std::shared_ptr`এবং`std::weak_ptr`এর মধ্যে পার্থক্য কী?
**A:**`unique_ptr`একচেটিয়া মালিকানার প্রতিনিধিত্ব করে — শুধুমাত্র একটি পয়েন্টার সম্পদের মালিক হতে পারে। এটিতে শূন্য ওভারহেড রয়েছে (একটি কাঁচা পয়েন্টারের মতো) এবং অনুলিপি করা যাবে না, শুধুমাত্র সরানো যাবে। `shared_ptr`শেয়ার করা মালিকানার প্রতিনিধিত্ব করে — একাধিক পয়েন্টার রেফারেন্স গণনা সহ সম্পদ ভাগ করে। যখন শেষ`shared_ptr`ধ্বংস হয়, সম্পদ মুক্ত হয়। `weak_ptr`হল একটি `shared_ptr`-এর মালিকানাহীন পর্যবেক্ষক — এটি রেফারেন্সের সংখ্যা বাড়ায় না এবং সার্কুলার রেফারেন্স ভাঙতে ব্যবহৃত হয়।
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

### প্রশ্ন 2: মুভ শব্দার্থবিদ্যা কি এবং কেন তারা গুরুত্বপূর্ণ?
**A:** মুভ শব্দার্থবিদ্যা (C++11) অনুলিপি করার পরিবর্তে একটি অস্থায়ী বস্তু থেকে সম্পদ স্থানান্তর করার অনুমতি দেয় (হিপ মেমরি, ফাইল হ্যান্ডেল, ইত্যাদি)। একটি মুভ কনস্ট্রাক্টর/অ্যাসাইনমেন্ট একটি rvalue রেফারেন্স (`T&&`) নেয় এবং উত্সের সংস্থানগুলিকে "চুরি" করে, এটি একটি বৈধ কিন্তু অনির্দিষ্ট অবস্থায় রেখে দেয়। এটি অপ্রয়োজনীয় অনুলিপিগুলিকে সরিয়ে দেয় এবং`std::vector`পুনঃঅবস্থান কার্যকর হওয়ার কারণ।
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

### প্রশ্ন 3: কখন আমার`auto`ব্যবহার করা উচিত, এবং কখন আমার প্রকারগুলি স্পষ্টভাবে উল্লেখ করা উচিত?
**A:**`auto`ব্যবহার করুন যখন ধরণটি প্রসঙ্গ থেকে স্পষ্ট হয় (ইটারেটর লুপ,`make_unique`/`make_shared`কল, ল্যাম্বডা প্রকার, জটিল টেমপ্লেট প্রকার)। যখন ধরনটি স্পষ্ট না হয়, যখন আপনার অন্তর্নিহিত রূপান্তর বা সর্বজনীন API স্বাক্ষরের প্রয়োজন হয় তখন স্পষ্টভাবে প্রকারগুলি নির্দিষ্ট করুন৷ "অলমোস্ট অলওয়েজ অটো" (AAA) স্টাইল স্থানীয় ভেরিয়েবলের জন্য`auto`এর পক্ষে; "স্বয়ংক্রিয় যেখানে সহায়ক" শৈলী আরও রক্ষণশীল।
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

### প্রশ্ন 4: কিভাবে ধারণা (C++20) টেমপ্লেট কোড উন্নত করে?
**A:** ধারণাগুলি নামযুক্ত প্রয়োজনীয়তার সাথে টেমপ্লেট প্যারামিটারগুলিকে সীমাবদ্ধ করে, স্পষ্ট ত্রুটি বার্তা তৈরি করে এবং টেমপ্লেট সীমাবদ্ধতার উপর ফাংশন ওভারলোডিং সক্ষম করে৷ ধারণার আগে, SFINAE এবং`static_assert`ব্যবহার করা হয়েছিল - উভয়ই ক্রিপ্টিক ত্রুটি তৈরি করে। ধারণাগুলি টেমপ্লেট কোডকে পাঠযোগ্য এবং রচনাযোগ্য করে তোলে।
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

### প্রশ্ন 5: রুল অফ ফাইভ কী, এবং এটি কীভাবে শূন্যের নিয়মের সাথে সম্পর্কিত?
**A:** পাঁচটির নিয়ম: আপনি যদি ডেস্ট্রাক্টর, কপি কনস্ট্রাক্টর, কপি অ্যাসাইনমেন্ট, মুভ কনস্ট্রাক্টর বা অ্যাসাইনমেন্টের যেকোনো একটিকে সংজ্ঞায়িত করেন, তাহলে আপনার পাঁচটিই সংজ্ঞায়িত করা উচিত। শূন্যের নিয়ম (পছন্দের): ডিজাইন ক্লাস যাতে তাদের এগুলির কোনোটির প্রয়োজন না হয় — সদস্য হিসাবে RAII প্রকারগুলি (`std::string`,`std::vector`,`std::unique_ptr`) ব্যবহার করুন এবং কম্পাইলার-উত্পন্ন বিশেষগুলি স্বয়ংক্রিয়ভাবে সঠিক কাজ করবে৷
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

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: রেঞ্জ সহ একটি থ্রেড-নিরাপদ প্রযোজক-ভোক্তা সারি প্রয়োগ করুন
**সমস্যা বিবৃতি:** ভোক্তা পক্ষের জন্য C++20 রেঞ্জ ব্যবহার করে একটি আবদ্ধ, থ্রেড-নিরাপদ প্রযোজক-ভোক্তা সারি তৈরি করুন। সারিতে পূর্ণ হলে প্রযোজক এবং ভোক্তাদের খালি হলে ব্লক করা উচিত এবং আকর্ষণীয় শাটডাউন সমর্থন করা উচিত।
**ধাপ 1 — সমস্যাটি বুঝুন:**
আমাদের প্রয়োজন: (1) ব্লকিং পুশ/পপ সহ একটি আবদ্ধ সারি, (2) মিউটেক্স এবং কন্ডিশন ভেরিয়েবলের মাধ্যমে থ্রেড নিরাপত্তা, (3) শাটডাউন সংকেত দেওয়ার একটি উপায়, (4) C++20 রেঞ্জ ইন্টিগ্রেশন যাতে গ্রাহকরা লুপের জন্য রেঞ্জ-ভিত্তিক ব্যবহার করতে পারেন।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- ব্লক করার জন্য`std::mutex`+`std::condition_variable`ব্যবহার করুন।
- অন্তর্নিহিত ধারক হিসাবে`std::queue<T>`ব্যবহার করুন।
- রিটার্ন টাইপ হিসাবে`std::optional<T>`ব্যবহার করুন —`std::nullopt`সিগন্যাল শাটডাউন।
- রেঞ্জ সমর্থনের জন্য একটি সেন্টিনেল-ভিত্তিক পুনরাবৃত্তিকারী প্রয়োগ করুন।
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- থ্রেড নিরাপত্তা:`std::mutex`সমস্ত সারির অবস্থা রক্ষা করে; শর্ত ভেরিয়েবল ব্লকিং হ্যান্ডেল.
- সুন্দর শাটডাউন:`shutdown()`সমস্ত ওয়েটারকে জাগিয়ে তোলে; `pop()`খালি এবং বন্ধ হলে`nullopt`প্রদান করে।
- পরিসীমা সমর্থন: পুনরাবৃত্তিকারীর সেন্টিনেল (ডিফল্ট-নির্মিত) যে কোনও ক্লান্ত পুনরাবৃত্তিকারীর সমান তুলনা করে।
- উত্পাদন: লক-মুক্ত একক-প্রযোজক একক-ভোক্তার জন্য`boost::lockfree::spsc_queue`ব্যবহার করুন, বা উচ্চ-থ্রুপুট পরিস্থিতিগুলির জন্য`folly::ProducerConsumerQueue`ব্যবহার করুন৷
### সমস্যা 2: একটি টাইপ-ইরেজেড যেকোন প্রকার প্রয়োগ করুন
**সমস্যা বিবৃতি:** স্ক্র্যাচ থেকে`std::any`(C++17) এর একটি সরলীকৃত সংস্করণ প্রয়োগ করুন — যে কোনও ধরণের একক মানগুলির জন্য একটি টাইপ-নিরাপদ ধারক, সমর্থনকারী অনুলিপি, সরানো এবং`any_cast`এর মাধ্যমে টাইপ-নিরাপদ পুনরুদ্ধার।
**ধাপ 1 — সমস্যাটি বুঝুন:**
`std::any`যে কোনো অনুলিপিযোগ্য প্রকারের একটি মান সঞ্চয় করে এবং টাইপ চেকিংয়ের মাধ্যমে এটি পুনরুদ্ধার করে। অভ্যন্তরীণভাবে, এটি টাইপ ইরেজার ব্যবহার করে: একটি প্রাপ্ত টেমপ্লেট সহ একটি বেস ক্লাস ইন্টারফেস যা প্রকৃত মান ধারণ করে। `any_cast`রানটাইমে সঞ্চিত প্রকার পরীক্ষা করে এবং অমিল হলে`bad_any_cast`ছুড়ে দেয়।
**ধাপ 2 — পদ্ধতি সনাক্ত করুন:**
- ভার্চুয়াল`clone()`এবং`type()`সহ একটি বেস ক্লাস`HolderBase`ব্যবহার করুন৷
- একটি প্রাপ্ত টেমপ্লেট`Holder<T>`ব্যবহার করুন যা প্রকৃত মান সঞ্চয় করে৷
-`Any`ক্লাসে একটি`std::unique_ptr<HolderBase>`সংরক্ষণ করুন৷
-`any_cast<T>``typeid` চেক করে এবং একটি`static_cast`সম্পাদন করে৷
**ধাপ 3 — সমাধানটি বাস্তবায়ন করুন:**
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

**পদক্ষেপ 4 — যাচাই করুন এবং অপ্টিমাইজ করুন:**
- টাইপ নিরাপত্তা:`any_cast`রানটাইমে`typeid`চেক করে — ভুল টাইপ`BadAnyCast`নিক্ষেপ করে৷
- অনুলিপি শব্দার্থবিদ্যা: ভার্চুয়াল`clone()`ধরে রাখা মানের একটি গভীর অনুলিপি তৈরি করে।
- শব্দার্থবিদ্যা সরান: ডিফল্ট মুভ কনস্ট্রাক্টর/অ্যাসাইনমেন্ট`unique_ptr`দক্ষতার সাথে স্থানান্তর করুন।
- ছোট বাফার অপ্টিমাইজেশান (যেমন বাস্তব `std::any`): হিপ অ্যালোকেশন ছাড়াই ইনলাইনে ছোট ধরনের স্টোর করুন। এর জন্য একটি বাইট বাফার সহ একটি`union`প্রয়োজন - উল্লেখযোগ্যভাবে আরও জটিল৷
- উত্পাদন:`std::any`(C++17) ব্যবহার করুন — এটি আদর্শ, ভাল-পরীক্ষিত, এবং এতে SBO অন্তর্ভুক্ত থাকতে পারে।
---

## সারাংশ
C++ প্রোগ্রামিং-এ একটি অনন্য অবস্থান দখল করে: এটি আপনাকে উচ্চ-স্তরের বিমূর্তকরণের অভিব্যক্তিপূর্ণ শক্তি সহ C-এর কাঁচা কর্মক্ষমতা দেয়। আধুনিক C++ (C++20/23) হল 1990-এর দশকের C++ থেকে একেবারেই আলাদা একটি ভাষা -- এটি নিরাপদ, আরও অভিব্যক্তিপূর্ণ এবং আরও উৎপাদনশীল। শেখার বক্ররেখা খাড়া, এবং ভাষা শৃঙ্খলা পুরস্কৃত করে। কর্মক্ষমতা-সমালোচনামূলক অ্যাপ্লিকেশনগুলির জন্য যেখানে আপনার সূক্ষ্ম নিয়ন্ত্রণের প্রয়োজন, C++ উপলব্ধ সেরা সরঞ্জামগুলির মধ্যে একটি।