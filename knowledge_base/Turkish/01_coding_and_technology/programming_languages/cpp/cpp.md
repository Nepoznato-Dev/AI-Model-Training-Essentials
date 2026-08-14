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
#C++
C++, Bjarne Stroustrup tarafından oluşturulan ve ilk kez 1985'te piyasaya sürülen genel amaçlı, derlenmiş bir programlama dilidir. C'yi nesne yönelimli özellikler, jenerikler ve modern sürümlerde (C++ 11 ve sonrası) lambdalar, akıllı işaretçiler ve Standart Şablon Kitaplığı (STL) gibi yüksek düzeyli soyutlamalarla genişletir. C++ "sıfır genel gider soyutlaması" ilkesini izler: kullanmadığınız özellikler için ödeme yapmamalısınız.
Hem yüksek performansa hem de ifade gücüne ihtiyaç duyduğunuzda C++ tercih ettiğiniz dildir. Oyun motorlarına (Unreal Engine), tarayıcılara (Chrome, Firefox), veritabanlarına (MongoDB), işletim sistemlerine (Windows ve macOS'un parçaları), finansal ticaret sistemlerine ve gerçek zamanlı simülasyonlara güç sağlar.
---

## C++ Neden Önemlidir
- **Anlamlı performans**: Sınıflar, şablonlar ve modern soyutlamalarla C'ye yakın hız.
- **Sıfır genel gider ilkesi**: Soyutlamalar, C'de elle yazacağınız kodun aynısına göre derlenir.
- **Devasa kod tabanı**: Onlarca yıllık kritik altyapı (oyunlar, tarayıcılar, veritabanları, yerleşik sistemler).
- **Çoklu paradigma**: Prosedürel, nesne yönelimli, genel ve işlevsel programlama stillerini destekler.
- **Deterministik yıkım**: RAII, kaynakların tahmin edilebilir şekilde temizlenmesini sağlar; çöp toplayıcı duraklaması olmaz.
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

## Sentetik Soru-Cevap
### S1: `std::unique_ptr`,`std::shared_ptr`ve`std::weak_ptr`arasındaki fark nedir?
**C:**`unique_ptr`özel sahipliği temsil eder; yalnızca bir işaretçi kaynağa sahip olabilir. Sıfır yükü vardır (ham işaretçiyle aynı) ve kopyalanamaz, yalnızca taşınır.  `shared_ptr`, paylaşılan sahipliği temsil eder; birden fazla işaretçi, referans sayımıyla kaynağı paylaşır. Son`shared_ptr`yok edildiğinde kaynak serbest bırakılır.  `weak_ptr`, `shared_ptr`'nin sahibi olmayan bir gözlemcisidir; referans sayısını artırmaz ve döngüsel referansları kırmak için kullanılır.
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

### S2: Hareket anlambilimi nedir ve neden önemlidir?
**C:** Taşıma anlambilimi (C++11), kaynakları (yığın belleği, dosya tanıtıcıları vb.) kopyalamak yerine geçici bir nesneden aktarmaya olanak tanır. Bir taşıma oluşturucusu/atama, bir değer referansı (`T&&`) alır ve kaynağın kaynaklarını "çalarak" onu geçerli ancak belirtilmemiş bir durumda bırakır. Bu, gereksiz kopyaları ortadan kaldırır ve`std::vector`yeniden tahsisinin verimli olmasının nedeni budur.
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

### S3: Ne zaman`auto`kullanmalıyım ve türleri ne zaman açıkça belirtmeliyim?
**C:** Tür bağlamdan açıkça belli olduğunda`auto`kullanın (yineleyici döngüler,`make_unique`/`make_shared`çağrıları, lambda türleri, karmaşık şablon türleri). Tür açık olmadığında, örtülü dönüşümlere ihtiyaç duyduğunuzda veya genel API imzalarında türleri açıkça belirtin. "Neredeyse Her Zaman Otomatik" (AAA) stili, yerel değişkenler için `auto`'yi tercih eder; "yardımcı olduğu yerde otomatik" tarzı daha muhafazakardır.
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

### S4: Kavramlar (C++20) şablon kodunu nasıl geliştirir?
**C:** Kavramlar, şablon parametrelerini adlandırılmış gereksinimlerle sınırlandırır, net hata mesajları üretir ve şablon kısıtlamalarında işlevin aşırı yüklenmesini sağlar. Konseptlerden önce SFINAE ve`static_assert`kullanılıyordu; her ikisi de şifreli hatalar üretiyordu. Kavramlar şablon kodunu okunabilir ve oluşturulabilir hale getirir.
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

### S5: Beş Kuralı nedir ve Sıfır Kuralı ile ilişkisi nedir?
**C:** Beş Kuralı: Yıkıcı, kopya oluşturucu, kopya atama, taşıma oluşturucu veya taşıma atamasından herhangi birini tanımlarsanız, beşini de tanımlamanız gerekir. Sıfır Kuralı (tercih edilir): sınıfları bunlardan hiçbirine ihtiyaç duymayacak şekilde tasarlayın - üye olarak RAII türlerini (`std::string`,`std::vector`,`std::unique_ptr`) kullanın; derleyici tarafından oluşturulan özel öğeler otomatik olarak doğru olanı yapacaktır.
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

## Düşünce Zinciri Problem Çözme
### Sorun 1: Aralıklarla İş Parçacığı Güvenli Üretici-Tüketici Kuyruğu Uygulama
**Sorun Açıklaması:** Tüketici tarafı için C++20 aralıklarını kullanarak sınırlı, iş parçacığı açısından güvenli bir üretici-tüketici kuyruğu oluşturun. Kuyruk, dolduğunda üreticileri, boş olduğunda ise tüketicileri engellemeli ve otomatik kapanmayı desteklemelidir.
**1. Adım — Sorunu Anlayın:**
Şunlara ihtiyacımız var: (1) push/pop'u engelleyen sınırlı bir kuyruk, (2) mutex ve durum değişkenleri aracılığıyla iş parçacığı güvenliği, (3) kapatma sinyali vermenin bir yolu, (4) tüketicilerin aralık tabanlı for döngülerini kullanabilmesi için C++20 aralık entegrasyonu.
**2. Adım — Yaklaşımı Belirleyin:**
- Engelleme için`std::mutex`+`std::condition_variable`kullanın.
- Temel kapsayıcı olarak`std::queue<T>`kullanın.
- Dönüş türü olarak `std::optional<T>`'yi kullanın —`std::nullopt`kapanma sinyali verir.
- Aralık desteği için nöbetçi tabanlı bir yineleyici uygulayın.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- İş parçacığı güvenliği:`std::mutex`tüm kuyruk durumlarını korur; durum değişkenleri engellemeyi yönetir.
- Zarif kapatma:`shutdown()`tüm garsonları uyandırır; `pop()`boş olduğunda ve kapatıldığında`nullopt`değerini döndürür.
- Aralık desteği: yineleyicinin nöbetçisi (varsayılan olarak oluşturulmuş), tükenmiş herhangi bir yineleyiciyle eşit olarak karşılaştırılır.
- Üretim: Kilitsiz tek üretici tek tüketici için `boost::lockfree::spsc_queue`'yi veya yüksek verimli senaryolar için `folly::ProducerConsumerQueue`'yi kullanın.
### Sorun 2: Tür-Silinmiş Herhangi Bir Türü Uygulama
**Sorun Açıklaması:** `std::any`'nin (C++17) basitleştirilmiş bir sürümünü sıfırdan uygulayın;`any_cast`aracılığıyla kopyalamayı, taşımayı ve tür açısından güvenli almayı destekleyen, her türdeki tek değerler için tür açısından güvenli bir kapsayıcı.
**1. Adım — Sorunu Anlayın:**
 `std::any`, kopyalanabilir herhangi bir türün değerini saklar ve bunu tür denetimiyle alır. Dahili olarak, tür silmeyi kullanır: gerçek değeri tutan türetilmiş bir şablona sahip bir temel sınıf arayüzü.  `any_cast`, çalışma zamanında depolanan türü kontrol eder ve uyumsuzluk durumunda `bad_any_cast`'yi atar.
**2. Adım — Yaklaşımı Belirleyin:**
- Sanal`clone()`ve`type()`ile bir temel sınıf`HolderBase`kullanın.
- Gerçek değeri saklayan türetilmiş bir`Holder<T>`şablonu kullanın.
- Bir `std::unique_ptr<HolderBase>`'yi`Any`sınıfında saklayın.
- `any_cast<T>`, `typeid`'yi kontrol eder ve bir`static_cast`gerçekleştirir.
**3. Adım — Çözümü Uygulayın:**
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

**4. Adım — Doğrulayın ve Optimize Edin:**
- Tür güvenliği:`any_cast`çalışma zamanında `typeid`'yi kontrol eder — yanlış tür `BadAnyCast`'yi atar.
- Kopyalama semantiği: sanal `clone()`, tutulan değerin derin bir kopyasını oluşturur.
- Anlambilimi taşı: varsayılan olarak yapıcıyı/atamayı taşı, `unique_ptr`'yi verimli bir şekilde aktar.
- Küçük arabellek optimizasyonu (gerçek`std::any`gibi): küçük türleri yığın tahsisi olmadan satır içi olarak depolayın. Bunun için bayt tamponlu bir`union`gerekir; bu çok daha karmaşıktır.
- Üretim:`std::any`(C++17) kullanın — standarttır, iyi test edilmiştir ve SBO içerebilir.
---

## Özet
C++ programlamada benzersiz bir konuma sahiptir: C'nin ham performansını üst düzey soyutlamaların ifade gücüyle birlikte sunar. Modern C++ (C++20/23), 1990'ların C++'ından çok farklı bir dildir; daha güvenlidir, daha etkileyici ve daha üretkendir. Öğrenme eğrisi diktir ve dil disiplini ödüllendirir. Ayrıntılı kontrole ihtiyaç duyduğunuz, performansın kritik olduğu uygulamalar için C++ mevcut en iyi araçlardan biri olmaya devam ediyor.