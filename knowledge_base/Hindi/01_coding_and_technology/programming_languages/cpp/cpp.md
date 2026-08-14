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
# सी++
C++ एक सामान्य-उद्देश्यीय, संकलित प्रोग्रामिंग भाषा है, जो बर्जने स्ट्रॉस्ट्रुप द्वारा बनाई गई है, जिसे पहली बार 1985 में जारी किया गया था। यह C को ऑब्जेक्ट-ओरिएंटेड फीचर्स, जेनरिक और - आधुनिक संस्करणों (C++11 और बाद में) में - लैम्ब्डा, स्मार्ट पॉइंटर्स और स्टैंडर्ड टेम्पलेट लाइब्रेरी (STL) जैसे उच्च-स्तरीय अमूर्तता के साथ विस्तारित करता है। C++ "शून्य-ओवरहेड एब्स्ट्रैक्शन" सिद्धांत का पालन करता है: आपको उन सुविधाओं के लिए भुगतान नहीं करना चाहिए जिनका आप उपयोग नहीं करते हैं।
जब आपको उच्च प्रदर्शन और अभिव्यंजक शक्ति दोनों की आवश्यकता होती है तो C++ पसंदीदा भाषा है। यह गेम इंजन (अवास्तविक इंजन), ब्राउज़र (क्रोम, फ़ायरफ़ॉक्स), डेटाबेस (MongoDB), ऑपरेटिंग सिस्टम (विंडोज़ और macOS के हिस्से), वित्तीय ट्रेडिंग सिस्टम और वास्तविक समय सिमुलेशन को शक्ति प्रदान करता है।
---

## C++ क्यों मायने रखता है
- **अभिव्यंजना के साथ प्रदर्शन**: कक्षाओं, टेम्पलेट्स और आधुनिक अमूर्तताओं के साथ लगभग-सी गति।
- **शून्य-ओवरहेड सिद्धांत**: सार उसी कोड में संकलित होते हैं जिसे आप सी में हाथ से लिखेंगे।
- **विशाल कोडबेस**: दशकों का महत्वपूर्ण बुनियादी ढांचा - गेम, ब्राउज़र, डेटाबेस, एम्बेडेड सिस्टम।
- **बहु-प्रतिमान**: प्रक्रियात्मक, वस्तु-उन्मुख, सामान्य और कार्यात्मक प्रोग्रामिंग शैलियों का समर्थन करता है।
- **नियतात्मक विनाश**: आरएआईआई यह सुनिश्चित करता है कि संसाधनों को अनुमानित रूप से साफ किया जाए - कोई भी कचरा संग्रहकर्ता नहीं रुकता।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **जटिलता** | भाषा बहुत बड़ी है - यहां तक ​​कि विशेषज्ञ भी यह सब नहीं जानते हैं | आधुनिक C++ (C++17/20) पर टिके रहें; विरासत पैटर्न से बचें |
| **स्मृति सुरक्षा** | मैनुअल मेमोरी प्रबंधन; लटकते सूचक, लीक, यूबी | स्मार्ट पॉइंटर्स, RAII और std:: वैकल्पिक | का उपयोग करें
| **संकलन समय** | बड़ी परियोजनाओं को संकलित करने में कुछ मिनट लग सकते हैं | पूर्व संकलित हेडर, मॉड्यूल (सी++20), वृद्धिशील बिल्ड |
| **त्रुटि संदेश** | टेम्प्लेट त्रुटियाँ सैकड़ों पंक्तियाँ लंबी हो सकती हैं | static_assert, अवधारणाओं (C++20), बेहतर कंपाइलर्स का उपयोग करें |
| **बाइनरी अनुकूलता** | कंपाइलर संस्करणों में एबीआई अस्थिरता | साझा पुस्तकालयों के लिए स्थिर सी इंटरफेस |
---

## सिंटेक्स बुनियादी बातें
### बुनियादी संरचना
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

### कक्षाएं और ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग
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

### टेम्प्लेट (जेनेरिक प्रोग्रामिंग)
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

### आधुनिक सी++ विशेषताएं (सी++17/20)
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

## मानक पुस्तकालय
### कंटेनर
| कंटेनर | प्रकार | कब उपयोग करें |
|--------|------|-------|
| std::वेक्टर | गतिशील सरणी | अनुक्रमिक डेटा के लिए डिफ़ॉल्ट विकल्प |
| std::deque | डबल-एंडेड कतार | दोनों सिरों पर तेजी से डालने/मिटाने की आवश्यकता है |
| std::सूची | डबल-लिंक्ड सूची | बीच में बार-बार डालना/मिटाना |
| एसटीडी::मानचित्र | पेड़ का नक्शा मंगवाया | क्रमबद्ध कुंजियों की आवश्यकता है, O(लॉग एन) लुकअप |
| std::unordered_map | हैश मैप | तेज़ O(1) औसत लुकअप |
| एसटीडी::सेट | ऑर्डर किया गया सेट | अद्वितीय क्रमबद्ध तत्व |
| std::सरणी | निश्चित-आकार सरणी | स्टैक-आवंटित, संकलन समय पर ज्ञात आकार |
| एसटीडी::स्ट्रिंग | पाठ | इसे हमेशा प्रयोग करें, कभी भी कच्चा चार* नहीं |
### स्मार्ट पॉइंटर्स
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

### एल्गोरिदम
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

## उन्नत सिंटैक्स और पैटर्न
### अवधारणाएँ (C++20)
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

### सिमेंटिक्स और RAII को स्थानांतरित करें
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

### कस्टम अपवाद पदानुक्रम
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

## समवर्ती एवं समांतरता
### std::थ्रेड और सिंक्रोनाइज़ेशन
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

### Async, वायदा, और वादे
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### गूगल टेस्ट उदाहरण
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

## अंतरसंचालनीयता
### सी इंटरऑप (बाहरी "सी")
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

## डिज़ाइन पैटर्न
### फ़ैक्टरी पैटर्न
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

### प्रेक्षक पैटर्न
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### बेंचमार्क उदाहरण (Google बेंचमार्क)
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

### अनुकूलन तकनीकें
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

## तैनाती
### डॉकर परिनियोजन
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

## संकलन और टूलींग
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| उपकरण | उद्देश्य |
|------|---------|
| **जीसीसी/क्लैंग/एमएसवीसी** | संकलक |
| **सीमेक** | सिस्टम जनरेटर बनाएं (उद्योग मानक) |
| **जीडीबी/एलएलडीबी** | डिबगर्स |
| **वालग्रिंड / एड्रेस सेनिटाइज़र** | मेमोरी त्रुटि का पता लगाना |
| **क्लैंग-साफ़** | लिंटिंग और आधुनिकीकरण |
| **क्लैंग-प्रारूप** | कोड फ़ॉर्मेटिंग |
| **कॉनन / वीसीपीकेजी** | पैकेज प्रबंधक |
| **गूगल टेस्ट/कैच2** | परीक्षण ढाँचे |
---

## C++ का उपयोग कब करें
| परिदृश्य | सी++ क्यों | बेहतर विकल्प |
|---|---|-----|
| गेम इंजन | प्रदर्शन + वास्तविक समय नियंत्रण | -- |
| ब्राउज़र्स | दशकों के अनुकूलित कोड | नए ब्राउज़र घटकों के लिए जंग |
| उच्च-आवृत्ति व्यापार | माइक्रोसेकंड विलंबता मायने रखती है | -- |
| एंबेडेड सिस्टम (जटिल) | हार्डवेयर एक्सेस के साथ समृद्ध सुविधा सेट | सी सरलता के लिए, जंग सुरक्षा के लिए |
| जीयूआई अनुप्रयोग (डेस्कटॉप) | क्यूटी ढांचा परिपक्व है | सी# (विंडोज़), स्विफ्ट (मैकओएस) |
| सामान्य अनुप्रयोग विकास | अधिकांश ऐप्स के लिए बहुत जटिल | पायथन, गो, जावा |
| वेब बैकएंड | सामान्य विकल्प नहीं | जाओ, जंग, Node.js |
| स्क्रिप्टिंग/स्वचालन | पूरी तरह से गलत उपकरण | पायथन, जावास्क्रिप्ट |
---

## सी++ मानक विकास
| मानक | वर्ष | प्रमुख विशेषताएँ |
|---|------|----|
| सी++98 | 1998 | मूल आईएसओ मानक; एसटीएल, iostreams |
| सी++11 | 2011 | **आधुनिक C++ प्रारंभ**: ऑटो, लैम्ब्डा, स्मार्ट पॉइंटर्स, मूव सिमेंटिक्स |
| सी++14 | 2014 | जेनेरिक लैम्ब्डा, std::make_unique, रिटर्न प्रकार कटौती |
| सी++17 | 2017 | संरचित बाइंडिंग, std::वैकल्पिक, std::variant, std::filesystem |
| सी++20 | 2020 | **प्रमुख रिलीज**: अवधारणाएं, श्रेणियां, कोरआउटाइन, मॉड्यूल |
| सी++23 | 2023 | std::अपेक्षित, std::प्रिंट, यह निष्कर्ष निकालना |
नई परियोजनाओं के लिए, न्यूनतम C++20 लक्ष्य रखें।
---

## सिंथेटिक प्रश्नोत्तर
### Q1:`std::unique_ptr`,`std::shared_ptr`और`std::weak_ptr`के बीच क्या अंतर है?
**ए:**`unique_ptr`विशेष स्वामित्व का प्रतिनिधित्व करता है - केवल एक सूचक ही संसाधन का स्वामी हो सकता है। इसमें शून्य ओवरहेड है (कच्चे पॉइंटर के समान) और इसे कॉपी नहीं किया जा सकता, केवल स्थानांतरित किया जा सकता है। `shared_ptr`साझा स्वामित्व का प्रतिनिधित्व करता है - एकाधिक पॉइंटर्स संदर्भ गणना के साथ संसाधन साझा करते हैं। जब अंतिम`shared_ptr`नष्ट हो जाता है, तो संसाधन मुक्त हो जाता है। `weak_ptr`एक`shared_ptr`का एक गैर-स्वामित्व वाला पर्यवेक्षक है - यह संदर्भ संख्या में वृद्धि नहीं करता है और इसका उपयोग परिपत्र संदर्भों को तोड़ने के लिए किया जाता है।
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

### प्रश्न2: चाल शब्दार्थ क्या हैं, और वे क्यों मायने रखते हैं?
**ए:** मूव सिमेंटिक्स (सी++11) संसाधनों (हीप मेमोरी, फ़ाइल हैंडल इत्यादि) को कॉपी करने के बजाय एक अस्थायी ऑब्जेक्ट से स्थानांतरित करने की अनुमति देता है। एक मूव कंस्ट्रक्टर/असाइनमेंट एक प्रतिद्वंद्विता संदर्भ (`T&&`) लेता है और स्रोत के संसाधनों को "चुरा लेता है", इसे वैध लेकिन अनिर्दिष्ट स्थिति में छोड़ देता है। यह अनावश्यक प्रतियों को समाप्त कर देता है और यही कारण है कि`std::vector`पुनर्आवंटन कुशल है।
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

### Q3: मुझे`auto`का उपयोग कब करना चाहिए, और कब मुझे स्पष्ट रूप से प्रकार निर्दिष्ट करना चाहिए?
**ए:** जब संदर्भ से प्रकार स्पष्ट हो तो`auto`का उपयोग करें (इटरेटर लूप,`make_unique`/`make_shared`कॉल, लैम्ब्डा प्रकार, जटिल टेम्पलेट प्रकार)। जब प्रकार स्पष्ट न हो, जब आपको अंतर्निहित रूपांतरणों की आवश्यकता हो, या सार्वजनिक एपीआई हस्ताक्षरों में स्पष्ट रूप से प्रकार निर्दिष्ट करें। "लगभग हमेशा ऑटो" (एएए) शैली स्थानीय चर के लिए`auto`का पक्ष लेती है; "ऑटो जहां सहायक" शैली अधिक रूढ़िवादी है।
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

### Q4: अवधारणाएँ (C++20) टेम्पलेट कोड को कैसे बेहतर बनाती हैं?
**ए:** अवधारणाएँ नामित आवश्यकताओं के साथ टेम्प्लेट मापदंडों को बाधित करती हैं, स्पष्ट त्रुटि संदेश उत्पन्न करती हैं और टेम्प्लेट बाधाओं पर फ़ंक्शन ओवरलोडिंग को सक्षम करती हैं। अवधारणाओं से पहले, SFINAE और`static_assert`का उपयोग किया गया था - दोनों गुप्त त्रुटियाँ उत्पन्न करते हैं। अवधारणाएँ टेम्प्लेट कोड को पढ़ने योग्य और लिखने योग्य बनाती हैं।
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

### प्रश्न5: पांच का नियम क्या है, और यह शून्य के नियम से कैसे संबंधित है?
**ए:** पांच का नियम: यदि आप डिस्ट्रक्टर, कॉपी कंस्ट्रक्टर, कॉपी असाइनमेंट, मूव कंस्ट्रक्टर, या मूव असाइनमेंट में से किसी एक को परिभाषित करते हैं, तो आपको सभी पांचों को परिभाषित करना चाहिए। शून्य का नियम (पसंदीदा): डिज़ाइन कक्षाएं ताकि उन्हें इनमें से किसी की भी आवश्यकता न हो - सदस्यों के रूप में RAII प्रकार (`std::string`, `std::vector`, `std::unique_ptr`) का उपयोग करें, और कंपाइलर-जनरेटेड स्पेशल स्वचालित रूप से सही काम करेंगे।
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

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: रेंज के साथ थ्रेड-सुरक्षित निर्माता-उपभोक्ता कतार लागू करें
**समस्या कथन:** उपभोक्ता पक्ष के लिए C++20 श्रेणियों का उपयोग करके एक सीमित, थ्रेड-सुरक्षित निर्माता-उपभोक्ता कतार बनाएं। कतार को पूर्ण होने पर उत्पादकों को और खाली होने पर उपभोक्ताओं को ब्लॉक करना चाहिए और ग्रेसफुल शटडाउन का समर्थन करना चाहिए।
**चरण 1 - समस्या को समझें:**
हमें चाहिए: (1) ब्लॉकिंग पुश/पॉप के साथ एक सीमित कतार, (2) म्यूटेक्स और कंडीशन वेरिएबल्स के माध्यम से थ्रेड सुरक्षा, (3) सिग्नल शटडाउन का एक तरीका, (4) सी++20 रेंज एकीकरण ताकि उपभोक्ता लूप के लिए रेंज-आधारित का उपयोग कर सकें।
**चरण 2 - दृष्टिकोण को पहचानें:**
- ब्लॉक करने के लिए`std::mutex`+`std::condition_variable`का उपयोग करें।
- अंतर्निहित कंटेनर के रूप में`std::queue<T>`का उपयोग करें।
- रिटर्न प्रकार के रूप में`std::optional<T>`का उपयोग करें -`std::nullopt`सिग्नल बंद हो जाता है।
- श्रेणियों के समर्थन के लिए एक प्रहरी-आधारित पुनरावर्तक लागू करें।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- थ्रेड सुरक्षा:`std::mutex`सभी कतार स्थिति की सुरक्षा करता है; स्थिति चर अवरोधन को संभालते हैं।
- शानदार शटडाउन:`shutdown()`ने सभी वेटरों को जगाया;  खाली और बंद होने पर`pop()``nullopt` लौटाता है।
- रेंज समर्थन: इटरेटर का प्रहरी (डिफ़ॉल्ट-निर्मित) किसी भी समाप्त इटरेटर के बराबर तुलना करता है।
- उत्पादन: लॉक-मुक्त एकल-निर्माता एकल-उपभोक्ता के लिए `boost::lockfree::spsc_queue`, या उच्च-थ्रूपुट परिदृश्यों के लिए`folly::ProducerConsumerQueue`का उपयोग करें।
### समस्या 2: किसी भी प्रकार का मिटाया गया प्रकार लागू करें
**समस्या कथन:**`std::any`(C++17) का एक सरलीकृत संस्करण स्क्रैच से लागू करें - किसी भी प्रकार के एकल मानों के लिए एक प्रकार-सुरक्षित कंटेनर,`any_cast`के माध्यम से कॉपी, मूव और टाइप-सुरक्षित पुनर्प्राप्ति का समर्थन करता है।
**चरण 1 - समस्या को समझें:**
`std::any`किसी भी प्रतिलिपि योग्य प्रकार का मान संग्रहीत करता है और प्रकार की जाँच के साथ इसे पुनर्प्राप्त करता है। आंतरिक रूप से, यह टाइप इरेज़र का उपयोग करता है: एक व्युत्पन्न टेम्पलेट के साथ एक बेस क्लास इंटरफ़ेस जो वास्तविक मान रखता है। `any_cast`रनटाइम पर संग्रहीत प्रकार की जांच करता है और बेमेल होने पर`bad_any_cast`फेंकता है।
**चरण 2 - दृष्टिकोण को पहचानें:**
- वर्चुअल`clone()`और`type()`के साथ बेस क्लास`HolderBase`का उपयोग करें।
- एक व्युत्पन्न टेम्पलेट`Holder<T>`का उपयोग करें जो वास्तविक मूल्य संग्रहीत करता है।
-`std::unique_ptr<HolderBase>`को`Any`क्लास में स्टोर करें।
-`any_cast<T>``typeid` की जांच करता है और एक`static_cast`निष्पादित करता है।
**चरण 3 - समाधान लागू करें:**
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

**चरण 4 - सत्यापित करें और अनुकूलित करें:**
- प्रकार की सुरक्षा:`any_cast`रनटाइम पर`typeid`की जांच करता है - गलत प्रकार`BadAnyCast`फेंकता है।
- कॉपी सिमेंटिक्स: वर्चुअल`clone()`धारित मान की एक गहरी प्रतिलिपि बनाता है।
- मूव सिमेंटिक्स: डिफॉल्ट मूव कंस्ट्रक्टर/असाइनमेंट`unique_ptr`को कुशलतापूर्वक ट्रांसफर करता है।
- छोटे बफर अनुकूलन (वास्तविक`std::any`की तरह): ढेर आवंटन के बिना छोटे प्रकार के इनलाइन को स्टोर करें। इसके लिए बाइट बफर के साथ`union`की आवश्यकता होती है - जो काफी अधिक जटिल है।
- उत्पादन:`std::any`(C++17) का उपयोग करें - यह मानक है, अच्छी तरह से परीक्षण किया गया है, और इसमें एसबीओ शामिल हो सकता है।
---

## सारांश
C++ प्रोग्रामिंग में एक अद्वितीय स्थान रखता है: यह आपको उच्च-स्तरीय अमूर्तता की अभिव्यंजक शक्ति के साथ C का कच्चा प्रदर्शन प्रदान करता है। आधुनिक C++ (C++20/23) 1990 के दशक की C++ से बहुत अलग भाषा है - यह अधिक सुरक्षित, अधिक अभिव्यंजक और अधिक उत्पादक है। सीखने की प्रक्रिया कठिन है और भाषा अनुशासन को पुरस्कृत करती है। प्रदर्शन-महत्वपूर्ण अनुप्रयोगों के लिए जहां आपको सूक्ष्म नियंत्रण की आवश्यकता होती है, C++ उपलब्ध सर्वोत्तम उपकरणों में से एक है।