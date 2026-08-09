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
#C++
C++는 Bjarne Stroustrup이 만든 범용 컴파일 프로그래밍 언어로, 1985년에 처음 출시되었습니다. 이는 객체 지향 기능, 제네릭 및 최신 버전(C++11 이상)에서는 람다, 스마트 포인터 및 STL(표준 템플릿 라이브러리)과 같은 고급 추상화를 통해 C를 확장합니다. C++는 "제로 오버헤드 추상화" 원칙을 따릅니다. 즉, 사용하지 않는 기능에 대해 비용을 지불해서는 안 됩니다.
C++는 고성능과 표현력이 모두 필요할 때 선택하는 언어입니다. 게임 엔진(Unreal Engine), 브라우저(Chrome, Firefox), 데이터베이스(MongoDB), 운영 체제(Windows 및 macOS의 일부), 금융 거래 시스템 및 실시간 시뮬레이션을 지원합니다.
---

## C++가 중요한 이유
- **표현력이 뛰어난 성능**: 클래스, 템플릿 및 현대적인 추상화를 통해 C에 가까운 속도를 제공합니다.
- **제로 오버헤드 원칙**: 추상화는 C에서 직접 작성하는 것과 동일한 코드로 컴파일됩니다.
- **대규모 코드베이스**: 게임, 브라우저, 데이터베이스, 임베디드 시스템 등 수십 년에 걸친 중요 인프라.
- **다중 패러다임**: 절차적, 객체 지향적, 일반 및 함수형 프로그래밍 스타일을 지원합니다.
- **결정적 파괴**: RAII는 리소스가 예측 가능하게 정리되도록 보장하며 가비지 수집기가 일시 중지되지 않습니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **복잡성** | 언어는 엄청납니다. 심지어 전문가도 다 알지 못합니다 | 최신 C++(C++17/20)을 고수하세요. 레거시 패턴을 피하세요 |
| **메모리 안전** | 수동 메모리 관리; 매달린 포인터, 누수, UB | 스마트 포인터, RAII 및 std::Optional 사용 |
| **컴파일 시간** | 대규모 프로젝트는 컴파일하는 데 몇 분이 걸릴 수 있습니다 | 미리 컴파일된 헤더, 모듈(C++20), 증분 빌드 |
| **오류 메시지** | 템플릿 오류는 수백 줄에 달할 수 있습니다 | static_assert, 개념(C++20), 더 나은 컴파일러 사용 |
| **바이너리 호환성** | 컴파일러 버전 전반에 걸친 ABI 불안정성 | 공유 라이브러리를 위한 안정적인 C 인터페이스 |
---

## 구문 기본 사항
### 기본 구조
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

### 클래스와 객체지향 프로그래밍
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

### 템플릿(일반 프로그래밍)
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

### 최신 C++ 기능(C++17/20)
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

## 표준 라이브러리
### 컨테이너
| 컨테이너 | 유형 | 사용 시기 |
|------------|------|----------|
| 표준::벡터 | 동적 배열 | 순차 데이터에 대한 기본 선택 |
| 표준::데크 | 양방향 큐 | 양쪽 끝에서 빠른 삽입/삭제가 필요함 |
| 표준::목록 | 이중 연결 목록 | 중간에 잦은 삽입/삭제 |
| 표준::지도 | 주문형 트리 맵 | 정렬된 키 필요, O(log n) 조회 |
| 표준::순서가 없는_지도 | 해시 맵 | 빠른 O(1) 평균 조회 |
| 표준::설정 | 세트 주문 | 고유하게 정렬된 요소 |
| 표준::배열 | 고정 크기 배열 | 스택 할당, 컴파일 시 알려진 크기 |
| 표준::문자열 | 텍스트 | 항상 이것을 사용하고 절대 원시 char* |
### 스마트 포인터
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

### 알고리즘
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

## 고급 구문 및 패턴
### 개념(C++20)
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

### 이동 의미론 및 RAII
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

### 사용자 정의 예외 계층 구조
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

## 동시성 및 병렬성
### std::thread 및 동기화
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

### 비동기, 미래, 약속
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조
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

### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### Google 테스트 예
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

## 상호 운용성
### C Interop(외부 "C")
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

## 디자인 패턴
### 팩토리 패턴
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

### 관찰자 패턴
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

## 성능 및 최적화
### 프로파일링 도구
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### 벤치마크 예(Google 벤치마크)
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

### 최적화 기술
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

## 배포
### 도커 배포
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

## 컴파일 및 도구
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| 도구 | 목적 |
|------|---------|
| **GCC/Clang/MSVC** | 컴파일러 |
| **CMake** | 빌드 시스템 생성기(산업 표준) |
| **GDB / LLDB** | 디버거 |
| **Valgrind / AddressSanitizer** | 메모리 오류 감지 |
| **깔끔하게 정리** | 린팅 및 현대화 |
| ** 소리 형식 ** | 코드 서식 |
| **코난 / vcpkg** | 패키지 관리자 |
| **구글 테스트 / Catch2** | 테스트 프레임워크 |
---

## C++를 사용해야 하는 경우
| 시나리오 | 왜 C++인가 | 더 나은 대안 |
|----------|---------|------|
| 게임 엔진 | 성능 + 실시간 제어 | -- |
| 브라우저 | 수십 년에 걸친 최적화된 코드 | 새로운 브라우저 구성요소를 위한 Rust |
| 고주파 거래 | 마이크로초 대기 시간이 중요함 | -- |
| 임베디드 시스템(복합) | 하드웨어 액세스를 포함한 풍부한 기능 세트 | C는 더 간단하고 Rust는 안전을 위한 |
| GUI 애플리케이션(데스크탑) | Qt 프레임워크가 성숙해졌습니다 | C#(Windows), Swift(macOS) |
| 일반 애플리케이션 개발 | 대부분의 앱에 비해 너무 복잡함 | 파이썬, 바둑, 자바 |
| 웹 백엔드 | 일반적인 선택이 아님 | Go, 러스트, Node.js |
| 스크립팅/자동화 | 완전히 잘못된 도구 | 파이썬, 자바스크립트 |
---

## C++ 표준의 진화
| 표준 | 연도 | 주요 기능 |
|------------|------|-------------|
| C++98 | 1998 | 원래의 ISO 표준입니다. STL, 아이오스트림 |
| C++11 | 2011 | **최신 C++ 시작**: 자동, 람다, 스마트 포인터, 이동 의미론 |
| C++14 | 2014 | 일반 람다, std::make_unique, 반환 유형 추론 |
| C++17 | 2017 | 구조적 바인딩, std::옵션, std::variant, std::filesystem |
| C++20 | 2020 | **주요 릴리스**: 개념, 범위, 코루틴, 모듈 |
| C++23 | 2023 | std::expected, std::print, 이를 추론 |
새 프로젝트의 경우 최소한 C++20을 대상으로 하세요.
---

## 요약
C++는 프로그래밍에서 독특한 위치를 차지합니다. C++는 높은 수준의 추상화 표현력을 통해 C의 원시 성능을 제공합니다. 최신 C++(C++20/23)은 1990년대의 C++와는 매우 다른 언어입니다. 즉, 더 안전하고 표현력이 풍부하며 생산적입니다. 학습 곡선은 가파르고 언어는 규율을 보상합니다. 세밀한 제어가 필요한 성능이 중요한 애플리케이션의 경우 C++는 여전히 최고의 도구 중 하나입니다.