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
C++ là ngôn ngữ lập trình được biên dịch, có mục đích chung do Bjarne Stroustrup tạo ra, được phát hành lần đầu tiên vào năm 1985. Nó mở rộng C với các tính năng hướng đối tượng, khái quát và -- trong các phiên bản hiện đại (C++ 11 trở lên) -- các khái niệm trừu tượng cấp cao như lambdas, con trỏ thông minh và Thư viện mẫu tiêu chuẩn (STL). C++ tuân theo nguyên tắc "trừu tượng hóa không chi phí": bạn không nên trả tiền cho những tính năng mà bạn không sử dụng.
C++ là ngôn ngữ được lựa chọn khi bạn cần cả hiệu suất cao và khả năng biểu đạt. Nó hỗ trợ các công cụ trò chơi (Unreal Engine), trình duyệt (Chrome, Firefox), cơ sở dữ liệu (MongoDB), hệ điều hành (các bộ phận của Windows và macOS), hệ thống giao dịch tài chính và mô phỏng thời gian thực.
---

## Tại sao C++ lại quan trọng
- **Hiệu suất với tính biểu cảm**: Tốc độ gần bằng C với các lớp, mẫu và tính trừu tượng hiện đại.
- **Nguyên tắc không chi phí**: Các bản tóm tắt biên dịch theo cùng mã mà bạn sẽ viết bằng tay trong C.
- **Cơ sở mã khổng lồ**: Cơ sở hạ tầng quan trọng trong nhiều thập kỷ -- trò chơi, trình duyệt, cơ sở dữ liệu, hệ thống nhúng.
- **Đa mô hình**: Hỗ trợ các phong cách lập trình thủ tục, hướng đối tượng, chung và chức năng.
- **Sự hủy diệt xác định**: RAII đảm bảo các tài nguyên được dọn sạch có thể dự đoán được -- không có sự tạm dừng của trình thu gom rác.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Độ phức tạp** | The language is enormous -- even experts do not know all of it | Bám sát C++ hiện đại (C++ 17/20); tránh các khuôn mẫu cũ |
| **An toàn bộ nhớ** | Quản lý bộ nhớ thủ công; con trỏ lủng lẳng, rò rỉ, UB | Sử dụng con trỏ thông minh, RAII và std :: tùy chọn |
| **Số lần biên dịch** | Các dự án lớn có thể mất vài phút để biên dịch | Precompiled headers, modules (C++20), incremental builds |
| **Thông báo lỗi** | Lỗi mẫu có thể dài hàng trăm dòng | Use static_assert, concepts (C++20), better compilers |
| **Khả năng tương thích nhị phân** | Tính không ổn định của ABI trên các phiên bản trình biên dịch | Giao diện C ổn định cho các thư viện dùng chung |
---

##Cơ bản về cú pháp
###Cấu trúc cơ bản
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

### Lớp và lập trình hướng đối tượng
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

### Mẫu (Lập trình chung)
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

### Tính năng hiện đại của C++ (C++17/20)
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

## Thư viện chuẩn
### Thùng chứa
| Thùng chứa | Loại | Sử dụng Khi nào |
|----------|------|----------|
| std::vector | Mảng động | Lựa chọn mặc định cho dữ liệu tuần tự |
| std::deque | Hàng đợi hai đầu | Cần chèn/xóa nhanh ở cả hai đầu |
| std::list | Danh sách liên kết đôi | Thường xuyên chèn/xóa ở giữa |
| std::map | Sơ đồ cây đặt hàng | Cần sắp xếp khóa, tra cứu O(log n) |
| std::unordered_map | Bản đồ băm | Tra cứu trung bình O(1) nhanh |
| std::set | Đã đặt hàng | Các phần tử được sắp xếp độc đáo |
| std::mảng | Mảng có kích thước cố định | Kích thước được phân bổ theo ngăn xếp, đã biết tại thời điểm biên dịch |
| std::string | văn bản | Luôn sử dụng cái này, không bao giờ dùng raw char* |
### Con trỏ thông minh
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

### Thuật toán
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

## Cú pháp & Mẫu nâng cao
### Khái niệm (C++20)
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

### Di chuyển ngữ nghĩa và RAII
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

### Phân cấp ngoại lệ tùy chỉnh
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

## Đồng thời & Song song
### std::thread và Đồng bộ hóa
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

### Không đồng bộ, Tương lai và Lời hứa
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
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

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### Ví dụ kiểm tra Google
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

## Khả năng tương tác
### C Interop (bên ngoài "C")
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

## Mẫu thiết kế
### Mẫu nhà máy
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

### Mẫu người quan sát
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Ví dụ về điểm chuẩn (Điểm chuẩn của Google)
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
### Triển khai Docker
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

## Biên dịch và tạo công cụ
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Công cụ | Mục đích |
|------|----------|
| **GCC / Clang / MSVC** | Trình biên dịch |
| **CMake** | Xây dựng hệ thống máy phát điện (tiêu chuẩn ngành) |
| **GDB / LLDB** | Trình gỡ lỗi |
| **Valgrind / Trình khử trùng địa chỉ** | Phát hiện lỗi bộ nhớ |
| **clang-gọn gàng** | Linting và hiện đại hóa |
| **định dạng clang** | Định dạng mã |
| **Conan / vcpkg** | Quản lý gói |
| **Kiểm tra của Google / Catch2** | Khung kiểm tra |
---

## Khi nào nên sử dụng C++
| Kịch bản | Tại sao C++ | Thay thế tốt hơn |
|----------|----------|-------------------|
| Công cụ trò chơi | Hiệu suất + kiểm soát thời gian thực | -- |
| Trình duyệt | Hàng thập kỷ mã được tối ưu hóa | Rust cho các thành phần trình duyệt mới |
| Giao dịch tần số cao | Vấn đề về độ trễ micro giây | -- |
| Hệ thống nhúng (phức tạp) | Bộ tính năng phong phú với quyền truy cập phần cứng | C để đơn giản hơn, Rust để an toàn |
| Ứng dụng GUI (máy tính để bàn) | Khung Qt đã hoàn thiện | C# (Windows), Swift (macOS) |
| Phát triển ứng dụng chung | Quá phức tạp đối với hầu hết các ứng dụng | Python, Go, Java |
| Phụ trợ web | Không phải sự lựa chọn điển hình | Đi, Rust, Node.js |
| Viết kịch bản / tự động hóa | Công cụ sai hoàn toàn | Python, JavaScript |
---

## Sự phát triển của tiêu chuẩn C++
| Tiêu chuẩn | Năm | Các tính năng chính |
|----------|------|-------------|
| C++98 | 1998 | Tiêu chuẩn ISO gốc; STL, iostream |
| C++11 | 2011 | **C++ hiện đại bắt đầu**: tự động, lambdas, con trỏ thông minh, ngữ nghĩa di chuyển |
| C++14 | 2014 | Lambda chung, std::make_unique, khấu trừ kiểu trả về |
| C++17 | 2017 | Các ràng buộc có cấu trúc, std::Options, std::variant, std::filesystem |
| C++20 | 2020 | **Bản phát hành chính**: khái niệm, phạm vi, coroutine, mô-đun |
| C++23 | 2023 | std::expected, std::print, suy ra điều này |
Đối với các dự án mới, hãy nhắm mục tiêu tối thiểu là C++20.
---

## Bản tóm tắt
C++ chiếm một vị trí độc nhất trong lập trình: nó mang lại cho bạn hiệu suất thô của C với sức mạnh biểu đạt của sự trừu tượng hóa cấp cao. C++ hiện đại (C++20/23) là một ngôn ngữ rất khác so với C++ của những năm 1990 -- nó an toàn hơn, biểu cảm hơn và hiệu quả hơn. Đường cong học tập rất dốc và ngôn ngữ mang lại tính kỷ luật. Đối với các ứng dụng quan trọng về hiệu năng mà bạn cần kiểm soát chi tiết, C++ vẫn là một trong những công cụ tốt nhất hiện có.