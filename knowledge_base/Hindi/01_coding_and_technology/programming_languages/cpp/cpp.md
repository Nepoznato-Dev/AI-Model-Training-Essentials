---
# मेटाडेटा
शीर्षक: "सी++"
विवरण: "C++ प्रोग्रामिंग भाषा के लिए व्यापक संदर्भ जिसमें अवलोकन, ट्रेड-ऑफ़, सिंटैक्स फंडामेंटल, इकोसिस्टम और इसका उपयोग कब करना है।"
श्रेणी: "कोडिंग और प्रौद्योगिकी"
संस्करण: "1.0.0"
स्थिति: "सक्रिय"
#योगदान
लेखक:
  - नाम: "एआई मॉडल ट्रेनिंग टीम"
    ईमेल: ""
    भूमिका: "मूल_लेखक"
योगदानकर्ता: []
चेंजलॉग:
  - संस्करण: "1.0.0"
    दिनांक: "2026-08-05"
    लेखक: "एआई मॉडल ट्रेनिंग टीम"
    परिवर्तन: "योगदानकर्ता ट्रैकिंग के लिए YAML फ्रंटमैटर मेटाडेटा जोड़ा गया"
#समीक्षा
बनाया गया: "2026-08-05"
अंतिम_संशोधित: "2026-08-05"
समीक्षा दिनांक: "2027-02-05"
इनके द्वारा समीक्षा: "कोडिंग और प्रौद्योगिकी ज्ञान आधार टीम"
अगली_समीक्षा: "2027-08-05"
#वर्गीकरण
टैग: [सीपीपी, प्रोग्रामिंग-भाषा, सिंटैक्स, पारिस्थितिकी तंत्र, कोडिंग-और-प्रौद्योगिकी]
कठिनाई_स्तर: "मध्यवर्ती"
पूर्वावश्यकताएँ: []
अनुमानित_पढ़ने_का_समय: "31 मिनट"
# योगदान मार्गदर्शिका
योगदान:
  लाइसेंस: "एमआईटी"
  फीडबैक_चैनल: "गिटहब मुद्दे"
  कैसे_तो_योगदान करें: "परिवर्तनों के साथ एक पीआर सबमिट करें और चेंजलॉग अपडेट करें"
  समीक्षा_प्रक्रिया: "विलय से पहले श्रेणी अनुरक्षकों द्वारा परिवर्तनों की समीक्षा की जाती है"
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
| **जटिलता** | भाषा बहुत बड़ी है - यहाँ तक कि विशेषज्ञ भी यह सब नहीं जानते हैं | आधुनिक C++ (C++17/20) पर टिके रहें; विरासत पैटर्न से बचें |
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

## सारांश
C++ प्रोग्रामिंग में एक अद्वितीय स्थान रखता है: यह आपको उच्च-स्तरीय अमूर्तता की अभिव्यंजक शक्ति के साथ C का कच्चा प्रदर्शन प्रदान करता है। आधुनिक C++ (C++20/23) 1990 के दशक की C++ से बहुत अलग भाषा है - यह अधिक सुरक्षित, अधिक अभिव्यंजक और अधिक उत्पादक है। सीखने की प्रक्रिया कठिन है और भाषा अनुशासन को पुरस्कृत करती है। प्रदर्शन-महत्वपूर्ण अनुप्रयोगों के लिए जहां आपको सूक्ष्म नियंत्रण की आवश्यकता होती है, C++ उपलब्ध सर्वोत्तम उपकरणों में से एक है।