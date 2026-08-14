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
C++ là ngôn ngữ lập trình được biên dịch, có mục đích chung do Bjarne Stroustrup tạo ra, được phát hành lần đầu tiên vào năm 1985. Nó mở rộng C với các tính năng hướng đối tượng, khái quát và -- trong các phiên bản hiện đại (C++ 11 trở lên) -- trừu tượng hóa cấp cao như lambdas, con trỏ thông minh và Thư viện mẫu tiêu chuẩn (STL). C++ tuân theo nguyên tắc "trừu tượng hóa không chi phí": bạn không nên trả tiền cho những tính năng mà bạn không sử dụng.
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
| **Độ phức tạp** | Ngôn ngữ rất lớn -- ngay cả các chuyên gia cũng không biết hết | Bám sát C++ hiện đại (C++ 17/20); tránh các khuôn mẫu cũ |
| **An toàn bộ nhớ** | Quản lý bộ nhớ thủ công; con trỏ lủng lẳng, rò rỉ, UB | Sử dụng con trỏ thông minh, RAII và std :: tùy chọn |
| **Số lần biên dịch** | Các dự án lớn có thể mất vài phút để biên dịch | Các tiêu đề, mô-đun được biên dịch sẵn (C++20), các bản dựng tăng dần |
| **Thông báo lỗi** | Lỗi mẫu có thể dài hàng trăm dòng | Sử dụng static_assert, khái niệm (C++20), trình biên dịch tốt hơn |
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

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`std::unique_ptr`,`std::shared_ptr`và`std::weak_ptr`là gì?
**A:**`unique_ptr`thể hiện quyền sở hữu độc quyền — chỉ một con trỏ có thể sở hữu tài nguyên. Nó không có chi phí hoạt động (giống như một con trỏ thô) và không thể sao chép mà chỉ di chuyển. `shared_ptr`thể hiện quyền sở hữu chung - nhiều con trỏ chia sẻ tài nguyên với tính năng tham chiếu. Khi`shared_ptr`cuối cùng bị phá hủy, tài nguyên sẽ được giải phóng. `weak_ptr`là trình quan sát không sở hữu`shared_ptr`- nó không làm tăng số lượng tham chiếu và được sử dụng để phá vỡ các tham chiếu vòng tròn.
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

### Câu 2: Ngữ nghĩa di chuyển là gì và tại sao chúng lại quan trọng?
**A:** Ngữ nghĩa di chuyển (C++11) cho phép truyền tài nguyên (bộ nhớ heap, bộ điều khiển tệp, v.v.) từ một đối tượng tạm thời thay vì sao chép chúng. Hàm tạo/gán di chuyển lấy tham chiếu giá trị (`T&&`) và "đánh cắp" tài nguyên của nguồn, để nó ở trạng thái hợp lệ nhưng không xác định. Điều này giúp loại bỏ các bản sao không cần thiết và là lý do khiến việc phân bổ lại`std::vector`có hiệu quả.
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

### Câu 3: Khi nào tôi nên sử dụng`auto`và khi nào tôi nên chỉ định rõ ràng các loại?
**A:** Sử dụng`auto`khi loại này rõ ràng trong ngữ cảnh (vòng lặp, lệnh gọi`make_unique`/ `make_shared`, loại lambda, loại mẫu phức tạp). Chỉ định loại rõ ràng khi loại đó không rõ ràng, khi bạn cần chuyển đổi ngầm định hoặc trong chữ ký API công khai. Kiểu "Hầu như luôn tự động" (AAA) ưu tiên`auto`cho các biến cục bộ; phong cách "tự động hữu ích" thận trọng hơn.
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

### Câu hỏi 4: Các khái niệm (C++20) cải thiện mã mẫu như thế nào?
**A:** Các khái niệm ràng buộc các tham số mẫu với các yêu cầu được đặt tên, tạo ra các thông báo lỗi rõ ràng và cho phép nạp chồng hàm trên các ràng buộc mẫu. Trước khi có khái niệm, SFINAE và`static_assert`đã được sử dụng — cả hai đều tạo ra lỗi khó hiểu. Các khái niệm làm cho mã mẫu có thể đọc được và có thể tổng hợp được.
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

### Câu 5: Quy tắc số 5 là gì và nó liên quan thế nào đến Quy tắc số 0?
**A:** Quy tắc Năm: nếu bạn xác định bất kỳ một trong số hàm hủy, hàm tạo sao chép, phép gán sao chép, hàm tạo di chuyển hoặc phép gán di chuyển, bạn nên xác định cả năm hàm. Quy tắc số 0 (ưu tiên): thiết kế các lớp để chúng không cần bất kỳ loại nào trong số này - sử dụng các loại RAII (`std::string`,`std::vector`,`std::unique_ptr`) làm thành viên và các đặc biệt do trình biên dịch tạo sẽ tự động thực hiện điều đúng đắn.
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

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Triển khai Hàng đợi Nhà sản xuất-Người tiêu dùng An toàn theo Chủ đề với các Phạm vi
**Báo cáo vấn đề:** Xây dựng hàng đợi nhà sản xuất-người tiêu dùng có giới hạn, an toàn theo luồng bằng cách sử dụng phạm vi C++20 cho phía người tiêu dùng. Hàng đợi sẽ chặn nhà sản xuất khi đầy và người tiêu dùng khi trống, đồng thời hỗ trợ tắt máy một cách nhẹ nhàng.
**Bước 1 — Tìm hiểu vấn đề:**
Chúng tôi cần: (1) một hàng đợi có giới hạn với tính năng chặn push/pop, (2) an toàn luồng thông qua các biến điều kiện và mutex, (3) một cách tắt tín hiệu, (4) tích hợp phạm vi C++20 để người tiêu dùng có thể sử dụng các vòng lặp for dựa trên phạm vi.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng`std::mutex`+`std::condition_variable`để chặn.
- Sử dụng`std::queue<T>`làm vùng chứa bên dưới.
- Sử dụng`std::optional<T>`làm kiểu trả về —`std::nullopt`báo hiệu tắt máy.
- Triển khai trình vòng lặp dựa trên trọng điểm để hỗ trợ phạm vi.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- An toàn luồng:`std::mutex`bảo vệ tất cả trạng thái hàng đợi; biến điều kiện xử lý việc chặn.
- Tắt máy một cách duyên dáng:`shutdown()`đánh thức tất cả những người phục vụ; `pop()`trả về`nullopt`khi trống và tắt.
- Hỗ trợ phạm vi: trọng điểm của trình vòng lặp (được xây dựng mặc định) so sánh bằng với bất kỳ trình vòng lặp đã cạn kiệt nào.
- Sản xuất: sử dụng`boost::lockfree::spsc_queue`cho người tiêu dùng đơn lẻ một nhà sản xuất không khóa hoặc`folly::ProducerConsumerQueue`cho các kịch bản thông lượng cao.
### Vấn đề 2: Thực hiện một kiểu xóa bất kỳ kiểu nào
**Báo cáo sự cố:** Triển khai phiên bản đơn giản hóa của`std::any`(C++17) từ đầu — một vùng chứa an toàn loại cho các giá trị đơn lẻ thuộc bất kỳ loại nào, hỗ trợ sao chép, di chuyển và truy xuất an toàn loại thông qua`any_cast`.
**Bước 1 — Tìm hiểu vấn đề:**
`std::any`lưu trữ giá trị của bất kỳ loại có thể sao chép nào và truy xuất nó bằng cách kiểm tra loại. Trong nội bộ, nó sử dụng tính năng xóa kiểu: giao diện lớp cơ sở với mẫu dẫn xuất chứa giá trị thực. `any_cast`kiểm tra loại được lưu trữ trong thời gian chạy và đưa ra`bad_any_cast`khi không khớp.
**Bước 2 — Xác định phương pháp tiếp cận:**
- Sử dụng lớp cơ sở`HolderBase`với`clone()`ảo và`type()`.
- Sử dụng mẫu dẫn xuất`Holder<T>`để lưu trữ giá trị thực.
- Lưu trữ`std::unique_ptr<HolderBase>`trong lớp `Any`.
-`any_cast<T>`kiểm tra`typeid`và thực hiện`static_cast`.
**Bước 3 — Triển khai giải pháp:**
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

**Bước 4 — Xác minh và tối ưu hóa:**
- An toàn loại:`any_cast`kiểm tra`typeid`khi chạy — ném sai loại`BadAnyCast`.
- Ngữ nghĩa sao chép:`clone()`ảo tạo bản sao sâu của giá trị được giữ.
- Ngữ nghĩa di chuyển: hàm tạo/gán di chuyển mặc định chuyển`unique_ptr`một cách hiệu quả.
- Tối ưu hóa bộ đệm nhỏ (như`std::any`thực): lưu trữ các loại nội tuyến nhỏ mà không cần phân bổ heap. Điều này yêu cầu`union`có bộ đệm byte - phức tạp hơn đáng kể.
- Sản xuất: sử dụng`std::any`(C++17) — đây là tiêu chuẩn, đã được kiểm tra kỹ lưỡng và có thể bao gồm SBO.
---

## Bản tóm tắt
C++ chiếm một vị trí độc nhất trong lập trình: nó mang lại cho bạn hiệu suất thô của C với sức mạnh biểu đạt của sự trừu tượng hóa cấp cao. C++ hiện đại (C++20/23) là một ngôn ngữ rất khác so với C++ của những năm 1990 -- nó an toàn hơn, biểu cảm hơn và hiệu quả hơn. Đường cong học tập rất dốc và ngôn ngữ mang lại tính kỷ luật. Đối với các ứng dụng quan trọng về hiệu năng mà bạn cần kiểm soát chi tiết, C++ vẫn là một trong những công cụ tốt nhất hiện có.