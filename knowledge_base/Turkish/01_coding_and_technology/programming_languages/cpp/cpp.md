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
C++, Bjarne Stroustrup tarafından oluşturulan ve ilk olarak 1985'te piyasaya sürülen genel amaçlı, derlenmiş bir programlama dilidir. C'yi nesne yönelimli özellikler, jenerikler ve modern sürümlerde (C++ 11 ve sonrası) lambdalar, akıllı işaretçiler ve Standart Şablon Kitaplığı (STL) gibi yüksek düzey soyutlamalarla genişletir. C++ "sıfır genel gider soyutlaması" ilkesini izler: kullanmadığınız özellikler için ödeme yapmamalısınız.
Hem yüksek performansa hem de ifade gücüne ihtiyaç duyduğunuzda C++ tercih edilen dildir. Oyun motorlarına (Unreal Engine), tarayıcılara (Chrome, Firefox), veritabanlarına (MongoDB), işletim sistemlerine (Windows ve macOS'un parçaları), finansal ticaret sistemlerine ve gerçek zamanlı simülasyonlara güç sağlar.
---

## C++ Neden Önemlidir
- **Anlamlı performans**: Sınıflar, şablonlar ve modern soyutlamalarla C'ye yakın hız.
- **Sıfır genel gider ilkesi**: Soyutlamalar, C'de elle yazacağınız kodun aynısına göre derlenir.
- **Devasa kod tabanı**: Onlarca yıllık kritik altyapı (oyunlar, tarayıcılar, veritabanları, yerleşik sistemler).
- **Çoklu paradigma**: Prosedürel, nesne yönelimli, genel ve işlevsel programlama stillerini destekler.
- **Deterministik imha**: RAII, kaynakların tahmin edilebilir şekilde temizlenmesini sağlar; çöp toplayıcı duraklaması olmaz.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Karmaşıklık** | Dil muazzam; uzmanlar bile tamamını bilmiyor | Modern C++'a (C++17/20) sadık kalın; eski kalıplardan kaçının |
| **Bellek güvenliği** | Manuel bellek yönetimi; sarkan işaretçiler, sızıntılar, UB | Akıllı işaretçileri, RAII'yi ve std::isteğe bağlı kullanın |
| **Derleme zamanları** | Büyük projelerin derlenmesi birkaç dakika sürebilir | Önceden derlenmiş başlıklar, modüller (C++20), artımlı yapılar |
| **Hata mesajları** | Şablon hataları yüzlerce satır uzunluğunda olabilir | static_assert, kavramlar (C++20), daha iyi derleyiciler kullanın |
| **İkili uyumluluk** | Derleyici sürümlerinde ABI kararsızlığı | Paylaşılan kütüphaneler için kararlı C arayüzleri |
---

## Söz Diziminin Temelleri
### Temel Yapı
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

### Sınıflar ve Nesneye Yönelik Programlama
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

### Şablonlar (Genel Programlama)
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

### Modern C++ Özellikleri (C++17/20)
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

## Standart Kütüphane
### Konteynerler
| Konteyner | Tür | Ne Zaman Kullan |
|-----------|----------|----------|
| std::vektör | Dinamik dizi | Sıralı veriler için varsayılan seçim |
| std::deque | Çift uçlu kuyruk | Her iki uçta da hızlı ekleme/silme gerekiyor |
| std::liste | Çift bağlantılı liste | Ortada sık ekleme/silme |
| std::harita | Sıralı ağaç haritası | Sıralanmış anahtarlara ihtiyacınız var, O(log n) araması |
| std::unordered_map | Haş haritası | Hızlı O(1) ortalama arama |
| std::set | Sipariş edilen set | Benzersiz sıralanmış öğeler |
| std::dizi | Sabit boyutlu dizi | Yığına ayrılmış, derleme zamanında bilinen boyut |
| std::string | Metin | Her zaman bunu kullanın, asla raw char* |
### Akıllı İşaretçiler
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

### Algoritmalar
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

## Gelişmiş Sözdizimi ve Desenler
### Kavramlar (C++20)
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

### Anlambilimi ve RAII'yi taşıma
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

### Özel İstisna Hiyerarşisi
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

## Eşzamanlılık ve Paralellik
### std::thread ve Senkronizasyon
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

### Eşzamansız İşlemler, Vadeli İşlemler ve Vaatler
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
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

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### Google Test Örneği
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

## Birlikte Çalışabilirlik
### C Birlikte Çalışma (harici "C")
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

## Tasarım Desenleri
### Fabrika Modeli
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

### Gözlemci Deseni
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Karşılaştırma Örneği (Google Karşılaştırması)
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

### Optimizasyon Teknikleri
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

## Dağıtım
### Docker Dağıtımı
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

## Derleme ve Araç Oluşturma
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Araç | Amaç |
|------|------------|
| **GCC / Clang / MSVC** | Derleyiciler |
| **CMake** | Sistem oluşturucuyu oluşturun (endüstri standardı) |
| **GDB / LLDB** | Hata ayıklayıcılar |
| **Valgrind / AdresSanitizer** | Bellek hatası tespiti |
| **tıngırdayan-düzenli** | Linting ve modernizasyon |
| **clang-formatı** | Kod biçimlendirme |
| **Conan / vcpkg** | Paket yöneticileri |
| **Google Testi / Yakalama2** | Çerçevelerin test edilmesi |
---

## C++ Ne Zaman Kullanılmalı?
| Senaryo | Neden C++ | Daha İyi Alternatif |
|----------|------------|-----------|
| Oyun motorları | Performans + gerçek zamanlı kontrol | -- |
| Tarayıcılar | Onlarca yıllık optimize edilmiş kod | Yeni tarayıcı bileşenleri için Rust |
| Yüksek frekanslı ticaret | Mikrosaniye gecikmesi önemlidir | -- |
| Gömülü sistemler (karmaşık) | Donanım erişimine sahip zengin özellik seti | Daha basit için C, güvenlik için pas |
| GUI uygulamaları (masaüstü) | Qt çerçevesi olgunlaştı | C# (Windows), Swift (macOS) |
| Genel uygulama geliştirme | Çoğu uygulama için fazla karmaşık | Python, Git, Java |
| Web arka uçları | Tipik bir seçim değil | Git, Rust, Node.js |
| Komut dosyası oluşturma / otomasyon | Tamamen yanlış araç | Python, JavaScript |
---

## C++ Standartlarının Gelişimi
| Standart | Yıl | Temel Özellikler |
|----------|------|------------|
| C++98 | 1998 | Orijinal ISO standardı; STL, io akışları |
| C++11 | 2011 | **Modern C++ başlıyor**: otomatik, lambdalar, akıllı işaretçiler, hareket semantiği |
| C++14 | 2014 | Genel lambdalar, std::make_unique, dönüş tipi kesinti |
| C++17 | 2017 | Yapılandırılmış bağlamalar, std::isteğe bağlı, std::variant, std::filesystem |
| C++20 | 2020 | **Büyük sürüm**: kavramlar, aralıklar, eşyordamlar, modüller |
| C++23 | 2023 | std::expected, std::print, bunu çıkarıyoruz |
Yeni projeler için minimum olarak C++20'yi hedefleyin.
---

## Özet
C++ programlamada benzersiz bir konuma sahiptir: C'nin ham performansını üst düzey soyutlamaların ifade gücüyle birlikte sunar. Modern C++ (C++20/23), 1990'ların C++'ından çok farklı bir dildir; daha güvenlidir, daha etkileyici ve daha üretkendir. Öğrenme eğrisi diktir ve dil disiplini ödüllendirir. Ayrıntılı kontrole ihtiyaç duyduğunuz, performansın kritik olduğu uygulamalar için C++ mevcut en iyi araçlardan biri olmaya devam ediyor.