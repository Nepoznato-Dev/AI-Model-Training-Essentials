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
C++ es un lenguaje de programación compilado de propósito general creado por Bjarne Stroustrup, lanzado por primera vez en 1985. Amplía C con características orientadas a objetos, genéricos y, en versiones modernas (C++11 y posteriores), abstracciones de alto nivel como lambdas, punteros inteligentes y la biblioteca de plantillas estándar (STL). C++ sigue el principio de "abstracción sin gastos generales": no debes pagar por funciones que no utilizas.
C++ es el lenguaje elegido cuando se necesita alto rendimiento y potencia expresiva. Impulsa motores de juegos (Unreal Engine), navegadores (Chrome, Firefox), bases de datos (MongoDB), sistemas operativos (partes de Windows y macOS), sistemas de comercio financiero y simulaciones en tiempo real.
---

## Por qué es importante C++
- **Rendimiento con expresividad**: Velocidad cercana a C con clases, plantillas y abstracciones modernas.
- **Principio de sobrecarga cero**: las abstracciones se compilan en el mismo código que escribirías a mano en C.
- **Base de código masiva**: Décadas de infraestructura crítica: juegos, navegadores, bases de datos, sistemas integrados.
- **Multiparadigma**: admite estilos de programación procedimental, orientada a objetos, genérica y funcional.
- **Destrucción determinista**: RAII garantiza que los recursos se limpien de manera predecible, sin pausas en el recolector de basura.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **Complejidad** | El lenguaje es enorme: ni siquiera los expertos lo saben todo | Cíñete al C++ moderno (C++17/20); evitar patrones heredados |
| **Seguridad de la memoria** | Gestión manual de la memoria; indicadores pendientes, fugas, UB | Utilice punteros inteligentes, RAII y std::optional |
| **Tiempos de compilación** | Los proyectos grandes pueden tardar unos minutos en compilarse | Encabezados precompilados, módulos (C++20), compilaciones incrementales |
| **Mensajes de error** | Los errores de plantilla pueden tener cientos de líneas | Utilice static_assert, conceptos (C++20), mejores compiladores |
| **Compatibilidad binaria** | Inestabilidad ABI entre versiones del compilador | Interfaces C estables para bibliotecas compartidas |
---

## Fundamentos de sintaxis
### Estructura básica
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

### Clases y programación orientada a objetos
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

### Plantillas (Programación genérica)
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

### Funciones modernas de C++ (C++17/20)
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

## La biblioteca estándar
### Contenedores
| Contenedor | Tipo | Usar cuando |
|-----------|------|----------|
| estándar::vector | Matriz dinámica | Elección predeterminada para datos secuenciales |
| std::deque | Cola de doble extremo | Necesita inserción/borrado rápido en ambos extremos |
| std::lista | Lista doblemente enlazada | Insertar/borrar frecuentemente en el medio |
| std::mapa | Mapa de árbol ordenado | Necesita claves ordenadas, búsqueda O (log n) |
| std::unordered_map | Mapa hash | Búsqueda rápida de promedio O (1) |
| estándar::conjunto | Conjunto ordenado | Elementos ordenados únicos |
| std::matriz | Matriz de tamaño fijo | Tamaño conocido y asignado por pila en el momento de la compilación |
| std::cadena | Texto | Utilice siempre esto, nunca char* sin formato |
### Punteros inteligentes
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

### Algoritmos
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

## Sintaxis y patrones avanzados
### Conceptos (C++20)
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

### Mover semántica y RAII
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

### Jerarquía de excepciones personalizada
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

## Concurrencia y paralelismo
### std::thread y sincronización
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

### Asíncrono, futuros y promesas
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

## Configuración del proyecto y sistema de construcción
### Estructura del proyecto
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

### Canalización de CI/CD (acciones de GitHub)
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

## Pruebas
### Ejemplo de prueba de Google
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

## Interoperabilidad
### C Interop (externo "C")
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

## Patrones de diseño
### Patrón de fábrica
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

### Patrón de observador
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

## Rendimiento y optimización
### Herramientas de creación de perfiles
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Ejemplo de punto de referencia (punto de referencia de Google)
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

### Técnicas de optimización
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

## Implementación
### Implementación de Docker
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

## Compilación y herramientas
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Herramienta | Propósito |
|------|---------|
| **CCG/Clang/MSVC** | Compiladores |
| **CMake** | Generador de sistema de construcción (estándar de la industria) |
| **BGF / LLDB** | Depuradores |
| **Valgrind / AddressSanitizer** | Detección de errores de memoria |
| **sonido ordenado** | Linting y modernización |
| **formato clang** | Formato de código |
| **Conan/vcpkg** | Gestores de paquetes |
| **Prueba de Google / Catch2** | Marcos de prueba |
---

## Cuándo usar C++
| Escenario | ¿Por qué C++? Mejor alternativa |
|----------|---------|-------------------|
| Motores de juego | Rendimiento + control en tiempo real | -- |
| Navegadores | Décadas de código optimizado | Rust para nuevos componentes del navegador |
| Comercio de alta frecuencia | La latencia de microsegundos importa | -- |
| Sistemas integrados (complejos) | Amplio conjunto de funciones con acceso al hardware | C para más simple, Rust para seguridad |
| Aplicaciones GUI (escritorio) | El marco Qt está maduro | C# (Windows), Swift (macOS) |
| Desarrollo de aplicaciones generales | Demasiado complejo para la mayoría de las aplicaciones | Python, Ir, Java |
| Servidores web | No es la elección típica | Vaya, Rust, Node.js |
| Scripting / automatización | Herramienta totalmente equivocada | Python, JavaScript |
---

## Evolución de los estándares C++
| Estándar | Año | Características clave |
|----------|------|-------------|
| C++98 | 1998 | El estándar ISO original; STL, iostreams |
| C++11 | 2011 | **Comienza el C++ moderno**: auto, lambdas, punteros inteligentes, semántica de movimiento |
| C++14 | 2014 | Lambdas genéricas, std::make_unique, deducción por tipo de retorno |
| C++17 | 2017 | Enlaces estructurados, std::opcional, std::variant, std::filesystem |
| C++20 | 2020 | **Lanzamiento principal**: conceptos, rangos, corrutinas, módulos |
| C++23 | 2023 | std::expected, std::print, deduciendo esto |
Para proyectos nuevos, apunte a C++20 como mínimo.
---

## Preguntas y respuestas sintéticas
### P1: ¿Cuál es la diferencia entre `std::unique_ptr`,`std::shared_ptr`y `std::weak_ptr`?
**R:**`unique_ptr`representa propiedad exclusiva: solo un puntero puede poseer el recurso. No tiene sobrecarga (igual que un puntero sin formato) y no se puede copiar, solo mover. `shared_ptr`representa propiedad compartida: varios punteros comparten el recurso, con recuento de referencias. Cuando se destruye el último `shared_ptr`, el recurso se libera. `weak_ptr`es un observador no propietario de `shared_ptr`: no aumenta el recuento de referencias y se utiliza para romper referencias circulares.
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

### P2: ¿Qué es la semántica de movimientos y por qué son importantes?
**R:** La semántica de movimiento (C++11) permite transferir recursos (memoria dinámica, identificadores de archivos, etc.) desde un objeto temporal en lugar de copiarlos. Un constructor/asignación de movimiento toma una referencia de valor (`T&&`) y "roba" los recursos de la fuente, dejándola en un estado válido pero no especificado. Esto elimina copias innecesarias y es la razón por la que la reasignación de`std::vector`es eficiente.
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

### P3: ¿Cuándo debo usar`auto`y cuándo debo especificar los tipos explícitamente?
**R:** Utilice`auto`cuando el tipo sea obvio por el contexto (bucles de iterador, llamadas `make_unique`/`make_shared`, tipos lambda, tipos de plantillas complejas). Especifique tipos explícitamente cuando el tipo no sea obvio, cuando necesite conversiones implícitas o en firmas de API públicas. El estilo "Casi siempre automático" (AAA) favorece`auto`para variables locales; el estilo "automático cuando sea útil" es más conservador.
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

### P4: ¿Cómo mejoran los conceptos (C++20) el código de la plantilla?
**R:** Los conceptos restringen los parámetros de la plantilla con requisitos nombrados, lo que produce mensajes de error claros y permite la sobrecarga de funciones en las restricciones de la plantilla. Antes de los conceptos, se usaban SFINAE y `static_assert`; ambos producen errores crípticos. Los conceptos hacen que el código de plantilla sea legible y componible.
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

### P5: ¿Qué es la Regla de Cinco y cómo se relaciona con la Regla de Cero?
**R:** La regla de los cinco: si define cualquiera de los siguientes: destructor, constructor de copia, asignación de copia, constructor de movimiento o asignación de movimiento, debe definir los cinco. La regla del cero (preferida): diseñe clases para que no necesiten ninguno de estos; use tipos RAII (`std::string`,`std::vector`,`std::unique_ptr`) como miembros, y los especiales generados por el compilador harán lo correcto automáticamente.
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

## Resolución de problemas mediante cadena de pensamiento
### Problema 1: implementar una cola de productor-consumidor segura para subprocesos con rangos
**Declaración del problema:** Cree una cola de productor-consumidor limitada y segura para subprocesos utilizando rangos de C++20 para el lado del consumidor. La cola debería bloquear a los productores cuando estén llenas y a los consumidores cuando estén vacías, y admitir un cierre ordenado.
**Paso 1: comprenda el problema:**
Necesitamos: (1) una cola limitada con bloqueo push/pop, (2) seguridad de subprocesos mediante mutex y variables de condición, (3) una forma de señalar el apagado, (4) integración de rangos C++20 para que los consumidores puedan usar bucles for basados en rangos.
**Paso 2: Identifique el enfoque:**
- Utilice`std::mutex`+`std::condition_variable`para bloquear.
- Utilice`std::queue<T>`como contenedor subyacente.
- Utilice`std::optional<T>`como tipo de retorno:`std::nullopt`indica apagado.
- Implementar un iterador basado en centinela para soporte de rangos.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Seguridad de subprocesos:`std::mutex`protege todos los estados de la cola; las variables de condición manejan el bloqueo.
- Apagado elegante:`shutdown()`despierta a todos los camareros; `pop()`devuelve`nullopt`cuando está vacío y apagado.
- Soporte de rango: el centinela del iterador (construido por defecto) se compara con cualquier iterador agotado.
- Producción: utilice`boost::lockfree::spsc_queue`para un solo productor y un solo consumidor sin bloqueo, o`folly::ProducerConsumerQueue`para escenarios de alto rendimiento.
### Problema 2: implementar cualquier tipo borrado de tipo
**Declaración del problema:** Implemente una versión simplificada de`std::any`(C++17) desde cero: un contenedor con seguridad de tipos para valores únicos de cualquier tipo, que admite copia, movimiento y recuperación con seguridad de tipos a través de `any_cast`.
**Paso 1: comprenda el problema:**
`std::any`almacena un valor de cualquier tipo copiable y lo recupera con verificación de tipo. Internamente, utiliza borrado de tipos: una interfaz de clase base con una plantilla derivada que contiene el valor real. `any_cast`comprueba el tipo almacenado en tiempo de ejecución y genera`bad_any_cast`si no coincide.
**Paso 2: Identifique el enfoque:**
- Utilice una clase base`HolderBase`con`clone()`y`type()`virtuales.
- Utilice una plantilla derivada`Holder<T>`que almacene el valor real.
- Almacenar un`std::unique_ptr<HolderBase>`en la clase `Any`.
-`any_cast<T>`comprueba`typeid`y realiza un `static_cast`.
**Paso 3: Implementar la solución:**
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

**Paso 4: Verificar y optimizar:**
- Seguridad de tipos:`any_cast`comprueba`typeid`en tiempo de ejecución; el tipo incorrecto arroja `BadAnyCast`.
- Copiar semántica: virtual`clone()`crea una copia profunda del valor retenido.
- Semántica de movimiento: el constructor/asignación de movimiento predeterminado transfiere el`unique_ptr`de manera eficiente.
- Optimización de búfer pequeño (como`std::any`real): almacena tipos pequeños en línea sin asignación de montón. Esto requiere un`union`con un búfer de bytes, significativamente más complejo.
- Producción: use`std::any`(C++17): es estándar, está bien probado y puede incluir SBO.
---

## Resumen
C++ ocupa una posición única en programación: le brinda el rendimiento puro de C con el poder expresivo de las abstracciones de alto nivel. El C++ moderno (C++ 20/23) es un lenguaje muy diferente del C++ de la década de 1990: es más seguro, más expresivo y más productivo. La curva de aprendizaje es pronunciada y el idioma recompensa la disciplina. Para aplicaciones críticas para el rendimiento en las que necesita un control detallado, C++ sigue siendo una de las mejores herramientas disponibles.