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
# С++
C++ — это компилируемый язык программирования общего назначения, созданный Бьярном Страуструпом и впервые выпущенный в 1985 году. Он расширяет C объектно-ориентированными функциями, дженериками и — в современных версиях (C++11 и более поздних) — абстракциями высокого уровня, такими как лямбда-выражения, интеллектуальные указатели и стандартная библиотека шаблонов (STL). C++ следует принципу «абстракции с нулевыми издержками»: вам не следует платить за функции, которые вы не используете.
C++ — это язык выбора, когда вам нужна одновременно высокая производительность и выразительность. Он поддерживает игровые движки (Unreal Engine), браузеры (Chrome, Firefox), базы данных (MongoDB), операционные системы (части Windows и macOS), системы финансовой торговли и моделирование в реальном времени.
---

## Почему C++ важен
- **Производительность и выразительность**: скорость, близкая к C, с классами, шаблонами и современными абстракциями.
- **Принцип нулевых затрат**: абстракции компилируются в тот же код, который вы бы написали вручную на C.
- **Огромная база кода**: десятилетия критической инфраструктуры — игр, браузеров, баз данных, встроенных систем.
- **Мультипарадигма**: поддерживает процедурный, объектно-ориентированный, универсальный и функциональный стили программирования.
- **Детерминированное уничтожение**: RAII обеспечивает предсказуемую очистку ресурсов — сборщик мусора не приостанавливает работу.
## Компромиссы
| Ограничение | Подробности | Типичный обходной путь |
|-----------|---------|-------------------|
| **Сложность** | Язык огромен – даже эксперты не знают его всего | Придерживайтесь современного C++ (C++17/20); избегать устаревших шаблонов |
| **Безопасность памяти** | Ручное управление памятью; висящие указатели, утечки, УБ | Используйте интеллектуальные указатели, RAII и std::optional |
| **Время компиляции** | Компиляция больших проектов может занять несколько минут | Предварительно скомпилированные заголовки, модули (C++20), инкрементные сборки |
| **Сообщения об ошибках** | Ошибки шаблона могут занимать сотни строк | Используйте static_assert, концепции (C++20), лучшие компиляторы |
| **Двоичная совместимость** | Нестабильность ABI в разных версиях компилятора | Стабильные интерфейсы C для общих библиотек |
---

## Основы синтаксиса
### Базовая структура
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

### Классы и объектно-ориентированное программирование
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

### Шаблоны (общее программирование)
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

### Современные возможности C++ (C++17/20)
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

## Стандартная библиотека
### Контейнеры
| Контейнер | Тип | Используйте, когда |
|-----------|------|----------|
| станд::вектор | Динамический массив | Выбор по умолчанию для последовательных данных |
| станд::дек | Двусторонняя очередь | Требуется быстрая вставка/стирание на обоих концах |
| станд::список | Двусвязный список | Частая вставка/стирание посередине |
| станд::карта | Заказанная карта дерева | Нужны отсортированные ключи, поиск O(log n) |
| std::unordered_map | Хэш-карта | Быстрый поиск среднего значения O(1) |
| станд::установить | Заказал комплект | Уникальные отсортированные элементы |
| станд::массив | Массив фиксированного размера | Выделяется в стеке, размер известен во время компиляции |
| станд::строка | Текст | Всегда используйте это, а не необработанный char* |
### Умные указатели
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

### Алгоритмы
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

## Расширенный синтаксис и шаблоны
### Концепции (C++20)
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

### Семантика перемещения и RAII
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

### Пользовательская иерархия исключений
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

## Параллелизм и параллелизм
### std::thread и синхронизация
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

### Асинхронность, фьючерсы и обещания
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

## Конфигурация проекта и система сборки
### Структура проекта
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

### Конвейер CI/CD (действия GitHub)
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

## Тестирование
### Пример теста Google
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

## Совместимость
### C Interop (внешний "C")
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

## Шаблоны проектирования
### Фабричный шаблон
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

### Шаблон наблюдателя
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

## Производительность и оптимизация
### Инструменты профилирования
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Пример теста (Google Benchmark)
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

### Методы оптимизации
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

## Развертывание
### Развертывание Docker
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

## Компиляция и инструменты
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Инструмент | Цель |
|------|---------|
| **GCC/Clang/MSVC** | Составители |
| **CMake** | Генератор системы сборки (отраслевой стандарт) |
| **ГБД/БЛБД** | Отладчики |
| **Валгринд / АдресСанитайзер** | Обнаружение ошибок памяти |
| **аккуратно** | Линтинг и модернизация |
| **формат clang** | Форматирование кода |
| **Конан / vcpkg** | Менеджеры пакетов |
| **Тест Google/Catch2** | Платформы тестирования |
---

## Когда использовать C++
| Сценарий | Почему С++ | Лучшая альтернатива |
|----------|---------|-------------------|
| Игровые движки | Производительность + контроль в реальном времени | -- |
| Браузеры | Десятилетия оптимизированного кода | Rust для новых компонентов браузера |
| Высокочастотный трейдинг | Задержка в микросекундах имеет значение | -- |
| Встраиваемые системы (комплексные) | Богатый набор функций с аппаратным доступом | C — проще, Rust — безопасность |
| Приложения с графическим интерфейсом (настольный компьютер) | Платформа Qt является зрелой | C# (Windows), Swift (macOS) |
| Общая разработка приложений | Слишком сложно для большинства приложений | Питон, Го, Java |
| Веб-серверы | Нетипичный выбор | Go, Rust, Node.js |
| Скрипты/автоматизация | Совсем неправильный инструмент | Питон, JavaScript |
---

## Эволюция стандартов C++
| Стандарт | Год | Ключевые особенности |
|----------|------|-------------|
| С++98 | 1998 | Исходный стандарт ISO; STL, iostreams |
| С++11 | 2011 | **Начало современного C++**: авто, лямбда-выражения, интеллектуальные указатели, семантика перемещения |
| С++14 | 2014 | Общие лямбда-выражения, std::make_unique, вычисление типа возвращаемого значения |
| С++17 | 2017 | Структурированные привязки, std::optional, std::variant, std::filesystem |
| С++20 | 2020 | **Основной выпуск**: концепции, диапазоны, сопрограммы, модули |
| С++23 | 2023 | std::expected, std::print, вывод этого |
Для новых проектов ориентируйтесь как минимум на C++20.
---

## Краткое содержание
C++ занимает уникальную позицию в программировании: он дает вам чистую производительность C с выразительной мощью абстракций высокого уровня. Современный C++ (C++20/23) сильно отличается от C++ 1990-х годов: он более безопасный, более выразительный и более продуктивный. Кривая обучения крутая, а язык вознаграждает за дисциплину. Для приложений, критичных к производительности, где требуется детальный контроль, C++ остается одним из лучших доступных инструментов.