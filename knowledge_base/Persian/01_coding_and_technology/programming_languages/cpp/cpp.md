---
# فراداده
عنوان: "C++"
توضیحات: "مرجع جامع برای زبان برنامه نویسی C++ شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [cpp، زبان برنامه‌نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "31 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
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
| موتورهای بازی | عملکرد + کنترل زمان واقعی | -- |
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

## خلاصه
C++ جایگاه منحصر به فردی را در برنامه نویسی اشغال می کند: عملکرد خام C را با قدرت بیانی انتزاعات سطح بالا به شما می دهد. C++ مدرن (C++20/23) زبان بسیار متفاوتی با C++ دهه 1990 است -- ایمن تر، رساتر و سازنده تر است. منحنی یادگیری شیب دار است و زبان به نظم و انضباط پاداش می دهد. برای برنامه های کاربردی حیاتی که به کنترل دقیق نیاز دارید، C++ یکی از بهترین ابزارهای موجود باقی می ماند.