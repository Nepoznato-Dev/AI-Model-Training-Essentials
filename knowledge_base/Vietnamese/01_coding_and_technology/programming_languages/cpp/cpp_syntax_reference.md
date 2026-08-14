---
# Metadata
title: "C++ — Syntax Reference"
description: "Detailed syntax reference for C++ covering operators, control flow, classes, templates, smart pointers, STL containers, concurrency, concepts, ranges, and modern C++ features."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [cpp, syntax-reference, operators, templates, stl, smart-pointers, concurrency, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# C++ — Tham chiếu cú ​​pháp
Tài liệu này cung cấp tham chiếu cú ​​pháp có cấu trúc, toàn diện cho Modern C++ (C++17/20/23). Nó bổ sung cho tham chiếu C++ chính bằng cách tập trung vào các mẫu cú pháp đầy đủ, bảng toán tử, cơ chế mẫu và các tính năng hiện đại.
---

## Toán tử & Biểu thức
### Toán tử số học và so sánh
| Nhà điều hành | Tên | Ví dụ | Ghi chú |
|----------|------|----------|-------|
| `+``-``*``/``%`| Số học | `a + b`| Tương tự như C |
| `++``--` | Tăng/Giảm | `++i`,`i++`| Ưu tiên tăng trước |
| `==``!=``<``>``<=``>=` | So sánh | `a <=> b`| `<=>`là so sánh ba chiều (C++20) |
| `&&``\|\|``!`| Hợp lý | `a && b`| Đoản mạch |
| `&``\|``^``~``<<``>>` | Theo chiều bit | `a & b`| Tương tự như C |
| `?:`| Đệ tam | `cond ? a : b`| |
### C++-Các toán tử cụ thể
| Nhà điều hành | Tên | Ví dụ | Ghi chú |
|----------|------|----------|-------|
| `::`| Độ phân giải phạm vi | `std::cout`| |
| `.*``->*` | Con trỏ tới thành viên | `obj.*pmf`| |
| `<=>`| Tàu vũ trụ (C++20) | `a <=> b`| Trả về`strong_ordering`|
| `co_await`| Đình chỉ coroutine | `co_await expr`| C++20 |
| `co_yield`| Sản lượng coroutine | `co_yield value`| C++20 |
| `co_return`| Coroutine trở lại | `co_return value`| C++20 |
### Quá tải toán tử
```cpp
class Vector2D {
    double x_, y_;
public:
    Vector2D(double x, double y) : x_(x), y_(y) {}

    // Member operator — left operand is *this
    Vector2D operator+(const Vector2D& rhs) const {
        return {x_ + rhs.x_, y_ + rhs.y_};
    }

    // Compound assignment — return *this by reference
    Vector2D& operator+=(const Vector2D& rhs) {
        x_ += rhs.x_; y_ += rhs.y_;
        return *this;
    }

    // Comparison (C++20: just define <=>)
    auto operator<=>(const Vector2D&) const = default;

    // Stream output — must be non-member (friend)
    friend std::ostream& operator<<(std::ostream& os, const Vector2D& v) {
        return os << "(" << v.x_ << ", " << v.y_ << ")";
    }

    // Subscript operator
    double operator[](int i) const { return i == 0 ? x_ : y_; }
    double& operator[](int i) { return i == 0 ? x_ : y_; }

    // Function call operator
    double operator()(double t) const { return x_ * t + y_; }
};

// Non-member operator for symmetry (allows 2.0 + vec)
Vector2D operator*(double s, const Vector2D& v) { return {s * v.x, s * v.y}; }
Vector2D operator*(const Vector2D& v, double s) { return s * v; }
```

---

## Luồng điều khiển
### Ràng buộc có cấu trúc & Mẫu hiện đại
```cpp
// Structured bindings (C++17)
auto [x, y] = std::pair{3.0, 4.0};
auto [name, age] = std::tuple{"Alice", 30};

// With maps
std::map<std::string, int> scores = {{"Alice", 95}, {"Bob", 87}};
for (const auto& [name, score] : scores) {
    std::cout << name << ": " << score << "\n";
}

// With if-init (C++17)
if (auto it = scores.find("Alice"); it != scores.end()) {
    std::cout << "Found: " << it->second << "\n";
}

// Switch with init (C++17)
switch (auto status = get_status(); status) {
    case Status::OK: break;
    case Status::Error: handle_error(); break;
}

// if constexpr — compile-time branching
template<typename T>
std::string to_string(const T& value) {
    if constexpr (std::is_arithmetic_v<T>) {
        return std::to_string(value);
    } else if constexpr (std::is_same_v<T, std::string>) {
        return "\"" + value + "\"";
    } else {
        return "[complex type]";
    }
}
```

---

## Hàm & Lambda
### Cú pháp hàm hiện đại
```cpp
// Trailing return type
auto add(int a, int b) -> int { return a + b; }

// Deduced return type (C++14)
auto multiply(auto a, auto b) { return a * b; }  // C++20 abbreviated template

// Constexpr function — evaluated at compile time
constexpr int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
constexpr int fact5 = factorial(5);  // Computed at compile time

// Consteval — MUST be evaluated at compile time (C++20)
consteval int forced_compile_time(int n) { return n * n; }

//nodiscard — warn if return value is ignored
[[nodiscard]] int compute() { return 42; }

// Immediately invoked lambda
const auto config = [&] {
    Config c;
    c.timeout = 30;
    c.retries = 3;
    return c;
}();
```

### Biểu thức Lambda
```cpp
// Basic lambda
auto square = [](int x) { return x * x; };

// Capture modes
int x = 10, y = 20;
auto by_value = [x, y]() { return x + y; };
auto by_ref = [&x, &y]() { x++; return y; };
auto all_by_value = [=]() { return x + y; };
auto all_by_ref = [&]() { x++; y++; };
auto mixed = [x, &y]() { y += x; };  // x by value, y by ref

// Generic lambda (C++14)
auto print = [](const auto& value) { std::cout << value << "\n"; };

// Lambda with explicit template parameters (C++20)
auto convert = []<typename T>(const std::vector<T>& v) {
    std::vector<std::string> result;
    for (const auto& item : v) result.push_back(std::to_string(item));
    return result;
};

// Mutable lambda — can modify captured-by-value variables
auto counter = [count = 0]() mutable { return ++count; };
counter();  // 1
counter();  // 2

// Recursive lambda
auto fib = [](auto& self, int n) -> int {
    return n <= 1 ? n : self(self, n - 1) + self(self, n - 2);
};
int result = fib(fib, 10);  // 55
```

---

## Lớp học & OOP
###Thiết kế đẳng cấp hiện đại
```cpp
// Class with modern features
class Widget {
    std::string name_;
    int value_ = 0;                          // Default member initializer
    static inline int count_ = 0;            // Inline static (C++17)

public:
    // Delegating constructor
    Widget() : Widget("default", 0) {}
    Widget(std::string name, int value = 0)
        : name_(std::move(name)), value_(value) { ++count_; }

    // Rule of zero — no custom destructor/copy/move needed

    // Explicit conversion operator
    explicit operator bool() const { return value_ != 0; }

    // Designated initializers support (aggregate or public members)
    std::string name() const { return name_; }
    int value() const { return value_; }

    static int instance_count() { return count_; }
};

// Aggregate with designated initializers (C++20)
struct Config {
    std::string host = "localhost";
    int port = 8080;
    int timeout = 30;
};

Config cfg{.host = "example.com", .port = 443};

// Enum class — scoped, strongly typed
enum class Color : uint8_t { Red, Green, Blue };
enum class [[nodiscard]] ErrorCode { OK = 0, NotFound = 1, Permission = 2 };

// Using enum (C++20)
using enum Color;
Color c = Red;
```

### Kế thừa & Đa hình
```cpp
// Abstract base class
class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual std::string name() const = 0;

    // Non-virtual interface pattern
    void describe() const {
        std::cout << name() << ": area = " << area() << "\n";
    }
};

// Override and final
class Circle final : public Shape {
    double radius_;
public:
    explicit Circle(double r) : radius_(r) {}
    double area() const override { return std::numbers::pi * radius_ * radius_; }
    std::string name() const override { return "Circle"; }
};

// Multiple inheritance
class Serializable {
public:
    virtual std::string serialize() const = 0;
    virtual void deserialize(std::string_view) = 0;
};

class PersistentCircle : public Circle, public Serializable {
public:
    using Circle::Circle;
    std::string serialize() const override { /* ... */ return ""; }
    void deserialize(std::string_view) override { /* ... */ }
};

// CRTP — static polymorphism (no vtable overhead)
template<typename Derived>
class Printable {
public:
    void print() const {
        std::cout << static_cast<const Derived*>(this)->to_string() << "\n";
    }
};

class MyType : public Printable<MyType> {
public:
    std::string to_string() const { return "MyType"; }
};
```

---

## Mẫu & Ý tưởng
### Nguyên tắc cơ bản về mẫu
```cpp
// Function template
template<typename T>
T max(T a, T b) { return (a > b) ? a : b; }

// Class template
template<typename T, size_t N>
class Array {
    T data_[N];
public:
    T& operator[](size_t i) { return data_[i]; }
    constexpr size_t size() const { return N; }
};

// Variable template (C++14)
template<typename T>
constexpr T pi = T(3.14159265358979323846);

double area = pi<double> * r * r;

// Template specialization
template<>
class Array<bool, 8> {
    uint8_t bits_ = 0;  // Specialized: pack 8 bools into 1 byte
public:
    bool operator[](size_t i) const { return (bits_ >> i) & 1; }
    void set(size_t i, bool v) {
        if (v) bits_ |= (1 << i);
        else bits_ &= ~(1 << i);
    }
};

// Variadic templates
template<typename... Args>
void log(const char* fmt, Args&&... args) {
    (std::cout << ... << std::forward<Args>(args)) << "\n";  // Fold expression
}

// Fold expressions (C++17)
template<typename... Args>
auto sum(Args... args) { return (args + ...); }

template<typename... Args>
bool all_true(Args... args) { return (args && ...); }
```

### Khái niệm (C++20)
```cpp
#include <concepts>

// Concept definition
template<typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<T>;
};

template<typename T>
concept Hashable = requires(T a) {
    { std::hash<T>{}(a) } -> std::convertible_to<std::size_t>;
};

// Constrained template
template<Addable T>
T add(T a, T b) { return a + b; }

// Abbreviated syntax
void print(const std::ranges::range auto& container) {
    for (const auto& item : container) std::cout << item << " ";
}

// Concept composition
template<typename T>
concept Number = std::integral<T> || std::floating_point<T>;

// Requires clause
template<typename T>
    requires std::copyable<T>
class Container {
    std::vector<T> data_;
};
```

---

## Bộ nhớ và con trỏ thông minh
```cpp
// unique_ptr — exclusive ownership
auto p = std::make_unique<int>(42);
auto arr = std::make_unique<int[]>(100);

// Custom deleter
auto file = std::unique_ptr<FILE, decltype(&fclose)>(
    fopen("data.txt", "r"), &fclose);

// shared_ptr — shared ownership
auto sp1 = std::make_shared<int>(42);
auto sp2 = sp1;  // Reference count = 2

// weak_ptr — non-owning observer
std::weak_ptr<int> wp = sp1;
if (auto locked = wp.lock()) {
    std::cout << *locked << "\n";
}

// enable_shared_from_this
class Session : public std::enable_shared_from_this<Session> {
public:
    std::shared_ptr<Session> get_shared() {
        return shared_from_this();
    }
};
```

---

## Thuật toán và vùng chứa STL
### Tổng quan về vùng chứa
| Thùng chứa | Tiêu đề | Đã đặt hàng | Tra cứu | Ghi chú |
|----------|--------|---------|--------|-------|
| `vector`| `<vector>`| Có | O(n) | Lựa chọn mặc định cho chuỗi |
| `deque`| `<deque>`| Có | O(n) | Đẩy/bật nhanh ở cả hai đầu |
| `list`| `<list>`| Có | O(n) | Danh sách liên kết đôi |
| `array`| `<array>`| Có | O(n) | Kích thước cố định, phân bổ theo ngăn xếp |
| `set`/`multiset`| `<set>`| Có | O(log n) | Cây đỏ đen |
| `map`/`multimap`| `<map>`| Có (bằng phím) | O(log n) | Khóa-giá trị, cây đỏ đen |
| `unordered_set`| `<unordered_set>`| Không | O(1) trung bình | Bảng băm |
| `unordered_map`| `<unordered_map>`| Không | O(1) trung bình | Bảng băm |
### Thuật toán chính
```cpp
#include <algorithm>
#include <numeric>
#include <ranges>

std::vector<int> v = {5, 2, 8, 1, 9, 3, 7, 4, 6};

// Sorting
std::sort(v.begin(), v.end());
std::sort(v.begin(), v.end(), std::greater<>());

// Searching
auto it = std::find(v.begin(), v.end(), 7);
auto it2 = std::lower_bound(v.begin(), v.end(), 5);
bool exists = std::binary_search(v.begin(), v.end(), 7);

// Transform
std::vector<int> doubled(v.size());
std::transform(v.begin(), v.end(), doubled.begin(), [](int x) { return x * 2; });

// Reduce
int sum = std::accumulate(v.begin(), v.end(), 0);
int product = std::accumulate(v.begin(), v.end(), 1, std::multiplies<>());

// C++20 Ranges — cleaner syntax, no begin/end
using namespace std::ranges;
auto result = v | views::filter([](int x) { return x > 3; })
                | views::transform([](int x) { return x * x; })
                | views::take(5);
for (int x : result) std::cout << x << " ";
```

---

## Đồng thời
```cpp
#include <thread>
#include <mutex>
#include <future>
#include <semaphore>

// Thread
std::thread t([] { std::cout << "Hello from thread\n"; });
t.join();

// async + future
auto result = std::async(std::launch::async, [] {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    return 42;
});
int value = result.get();  // Blocks until ready

// Mutex + lock_guard
std::mutex mtx;
std::lock_guard lock(mtx);  // RAII — unlocks on scope exit
std::unique_lock ulock(mtx); // More flexible (deferred, timed)

// Condition variable
std::condition_variable cv;
cv.wait(lock, [&] { return ready; });
cv.notify_one();

// C++20 Semaphore
std::counting_semaphore<10> sem(10);
sem.acquire();  // Decrement
sem.release();  // Increment

// C++20 Latch (one-shot barrier)
std::latch done(3);
done.count_down();
done.wait();

// C++20 atomic smart pointers
std::atomic<std::shared_ptr<int>> asp;
```

---

## Bản tóm tắt
Cú pháp C++ trải dài từ thao tác con trỏ cấp thấp đến siêu lập trình mẫu cấp cao và không đồng bộ dựa trên coroutine. Sự phát triển của ngôn ngữ thông qua C++17/20/23 đã cải thiện đáng kể tính an toàn (con trỏ thông minh,`std::optional`, khái niệm), tính biểu cảm (liên kết có cấu trúc, phạm vi,`std::format`) và hiệu suất (các khái niệm cho phép trừu tượng hóa với chi phí bằng 0, coroutine cho không đồng bộ mà không cần chi phí ngăn xếp). Triết lý cốt lõi vẫn không thay đổi: bạn không nên trả tiền cho những gì bạn không sử dụng và ngôn ngữ phải hỗ trợ mọi cấp độ trừu tượng từ ngôn ngữ cơ bản đến các ngôn ngữ theo miền cụ thể.