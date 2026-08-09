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

#ซี++
C++ เป็นภาษาโปรแกรมคอมไพล์สำหรับวัตถุประสงค์ทั่วไป สร้างขึ้นโดย Bjarne Stroustrup ซึ่งเปิดตัวครั้งแรกในปี 1985 โดยขยาย C ด้วยฟีเจอร์เชิงวัตถุ ภาษาทั่วไป และ -- ในเวอร์ชันสมัยใหม่ (C++ 11 และใหม่กว่า) -- นามธรรมระดับสูง เช่น lambdas, ตัวชี้อัจฉริยะ และ Standard Template Library (STL) C++ เป็นไปตามหลักการ "Zero-Overhead Abstraction": คุณไม่ควรจ่ายเงินสำหรับฟีเจอร์ที่คุณไม่ได้ใช้
C++ คือภาษาที่คุณเลือกเมื่อคุณต้องการทั้งประสิทธิภาพสูงและพลังในการแสดงออก มันขับเคลื่อนกลไกเกม (Unreal Engine), เบราว์เซอร์ (Chrome, Firefox), ฐานข้อมูล (MongoDB), ระบบปฏิบัติการ (ส่วนหนึ่งของ Windows และ macOS), ระบบการซื้อขายทางการเงิน และการจำลองแบบเรียลไทม์
---

## ทำไม C++ จึงมีความสำคัญ
- **ประสิทธิภาพพร้อมการแสดงออก**: ความเร็วเกือบ C พร้อมคลาส เทมเพลต และนามธรรมสมัยใหม่
- **หลักการไร้ค่าโสหุ้ย**: Abstractions คอมไพล์เป็นโค้ดเดียวกับที่คุณจะเขียนด้วยมือในภาษา C
- **ฐานโค้ดขนาดใหญ่**: ทศวรรษแห่งโครงสร้างพื้นฐานที่สำคัญ ไม่ว่าจะเป็นเกม เบราว์เซอร์ ฐานข้อมูล ระบบฝังตัว
- **หลายกระบวนทัศน์**: รองรับรูปแบบการเขียนโปรแกรมเชิงขั้นตอน เชิงวัตถุ ทั่วไป และเชิงฟังก์ชัน
- **การทำลายล้างตามกำหนด**: RAII ช่วยให้มั่นใจว่าทรัพยากรได้รับการทำความสะอาดอย่างคาดการณ์ได้ -- ไม่มีการหยุดเก็บขยะชั่วคราว
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ความซับซ้อน** | ภาษามีขนาดใหญ่มาก แม้แต่ผู้เชี่ยวชาญก็ยังไม่รู้ทั้งหมด | ยึดติดกับ C++ สมัยใหม่ (C++17/20); หลีกเลี่ยงรูปแบบเดิม |
| **ความปลอดภัยของหน่วยความจำ** | การจัดการหน่วยความจำด้วยตนเอง พอยน์เตอร์ห้อย, รอยรั่ว, UB | ใช้พอยน์เตอร์อัจฉริยะ RAII และ std::เป็นทางเลือก |
| **เวลาในการคอมไพล์** | โปรเจ็กต์ขนาดใหญ่อาจใช้เวลาไม่กี่นาทีในการคอมไพล์ | ส่วนหัวที่คอมไพล์แล้ว, โมดูล (C++20), บิวด์ส่วนเพิ่ม |
| **ข้อความแสดงข้อผิดพลาด** | ข้อผิดพลาดของเทมเพลตอาจมีความยาวได้หลายร้อยบรรทัด | ใช้ static_assert แนวคิด (C ++ 20) คอมไพเลอร์ที่ดีกว่า |
| **ความเข้ากันได้แบบไบนารี** | ความไม่เสถียรของ ABI ในเวอร์ชันคอมไพเลอร์ | อินเทอร์เฟซ C ที่เสถียรสำหรับไลบรารีที่แบ่งใช้ |
---

## พื้นฐานไวยากรณ์
### โครงสร้างพื้นฐาน
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

### คลาสและการเขียนโปรแกรมเชิงวัตถุ
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

### เทมเพลต (การเขียนโปรแกรมทั่วไป)
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

### คุณสมบัติ C ++ สมัยใหม่ (C ++ 17/20)
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

## ห้องสมุดมาตรฐาน
### คอนเทนเนอร์
| ตู้คอนเทนเนอร์ | พิมพ์ | ใช้เมื่อ |
|----------|-|----------|
| มาตรฐาน::เวกเตอร์ | อาร์เรย์แบบไดนามิก | ตัวเลือกเริ่มต้นสำหรับข้อมูลตามลำดับ |
| มาตรฐาน::deque | คิวปลายคู่ | ต้องการแทรก/ลบอย่างรวดเร็วที่ปลายทั้งสองข้าง |
| มาตรฐาน::รายการ | รายการเชื่อมโยงสองเท่า | แทรก/ลบตรงกลางบ่อยๆ |
| มาตรฐาน::แผนที่ | สั่งซื้อแผนที่ต้นไม้ | ต้องการคีย์ที่เรียงลำดับ O(log n) lookup |
| std::unordered_map | แผนที่แฮช | การค้นหาค่าเฉลี่ย O(1) อย่างรวดเร็ว |
| มาตรฐาน::ตั้งค่า | สั่งชุด | องค์ประกอบที่เรียงลำดับไม่ซ้ำกัน |
| มาตรฐาน::อาร์เรย์ | อาร์เรย์ขนาดคงที่ | จัดสรรสแต็ก ขนาดที่ทราบ ณ เวลารวบรวม |
| มาตรฐาน::สตริง | ข้อความ | ใช้สิ่งนี้เสมอ ห้ามใช้ถ่านดิบ* |
### ตัวชี้อัจฉริยะ
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

### อัลกอริทึม
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

## ไวยากรณ์และรูปแบบขั้นสูง
### แนวคิด (C++20)
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

### ย้ายความหมายและ RAII
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

### ลำดับชั้นข้อยกเว้นที่กำหนดเอง
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### std::thread และการซิงโครไนซ์
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

### Async ฟิวเจอร์ส และคำมั่นสัญญา
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ
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

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### ตัวอย่างการทดสอบของ Google
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

## การทำงานร่วมกัน
### C Interop (ภายนอก "C")
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

## รูปแบบการออกแบบ
### ลายโรงงาน
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

### รูปแบบผู้สังเกตการณ์
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### ตัวอย่างการวัดประสิทธิภาพ (Google Benchmark)
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### การปรับใช้นักเทียบท่า
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

## การรวบรวมและการใช้เครื่องมือ
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **GCC / เสียงดังกราว / MSVC** | คอมไพเลอร์ |
| **ซีเมค** | สร้างระบบเครื่องกำเนิดไฟฟ้า (มาตรฐานอุตสาหกรรม) |
| **GDB / LLDB** | ดีบักเกอร์ |
| **Valgrind / AddressSanitizer** | การตรวจจับข้อผิดพลาดของหน่วยความจำ |
| **เสียงดังกราวเป็นระเบียบเรียบร้อย** | Linting และความทันสมัย ​​|
| **รูปแบบเสียงดังกราว** | การจัดรูปแบบโค้ด |
| **โคนัน / vcpkg** | ผู้จัดการแพ็คเกจ |
| **การทดสอบของ Google / Catch2** | กรอบการทดสอบ |
---

## เมื่อใดจึงควรใช้ C++
| สถานการณ์ | ทำไมต้อง C++ | ทางเลือกที่ดีกว่า |
|----------|---------|-------------------|
| เครื่องยนต์เกม | ประสิทธิภาพ + การควบคุมแบบเรียลไทม์ | -- |
| เบราว์เซอร์ | ทศวรรษของโค้ดที่ได้รับการปรับปรุง | Rust สำหรับส่วนประกอบเบราว์เซอร์ใหม่ |
| การซื้อขายความถี่สูง | เวลาแฝงระดับไมโครวินาทีมีความสำคัญ | -- |
| ระบบสมองกลฝังตัว (ซับซ้อน) | ชุดคุณลักษณะที่หลากหลายพร้อมการเข้าถึงฮาร์ดแวร์ | C เพื่อความเรียบง่าย สนิมเพื่อความปลอดภัย |
| แอปพลิเคชัน GUI (เดสก์ท็อป) | กรอบ Qt เป็นผู้ใหญ่แล้ว | C# (Windows), Swift (macOS) |
| การพัฒนาแอพพลิเคชั่นทั่วไป | ซับซ้อนเกินไปสำหรับแอปส่วนใหญ่ | Python, Go, Java |
| แบ็กเอนด์ของเว็บ | ไม่ใช่ตัวเลือกทั่วไป | ไป, สนิม, Node.js |
| การเขียนสคริปต์ / ระบบอัตโนมัติ | เครื่องมือผิดทั้งหมด | หลาม, จาวาสคริปต์ |
---

## วิวัฒนาการมาตรฐาน C ++
| มาตรฐาน | ปี | คุณสมบัติที่สำคัญ |
|----------|-|-------------|
| ค++98 | 1998 | มาตรฐาน ISO ดั้งเดิม STL, iostreams |
| ค++11 | 2554 | **Modern C++ เริ่มต้นขึ้น**: auto, lambdas, smart pointers, move semantics |
| ค++14 | 2014 | lambdas ทั่วไป, std::make_unique, การหักประเภทการส่งคืน |
| ค++17 | 2017 | การเชื่อมโยงแบบมีโครงสร้าง std::เป็นทางเลือก, std::variant, std::filesystem |
| ค++20 | 2020 | **รุ่นหลัก**: แนวคิด ช่วง โครูทีน โมดูล |
| ค++23 | 2023 | std::expected, std::print, อนุมานสิ่งนี้ |
สำหรับโปรเจ็กต์ใหม่ ให้กำหนดเป้าหมาย C++20 เป็นขั้นต่ำ
---

## สรุป
C++ ครองตำแหน่งที่ไม่เหมือนใครในการเขียนโปรแกรม: มันให้ประสิทธิภาพดิบของ C พร้อมพลังการแสดงออกของนามธรรมระดับสูง Modern C++ (C++20/23) เป็นภาษาที่แตกต่างจาก C++ ในยุค 1990 มาก -- ปลอดภัยกว่า แสดงออกได้มากกว่า และมีประสิทธิภาพมากกว่า เส้นโค้งการเรียนรู้นั้นสูงชัน และภาษาก็ให้รางวัลแก่ระเบียบวินัย สำหรับแอปพลิเคชันที่เน้นประสิทธิภาพการทำงานซึ่งคุณต้องการการควบคุมอย่างละเอียด C++ ยังคงเป็นหนึ่งในเครื่องมือที่ดีที่สุดที่มีอยู่