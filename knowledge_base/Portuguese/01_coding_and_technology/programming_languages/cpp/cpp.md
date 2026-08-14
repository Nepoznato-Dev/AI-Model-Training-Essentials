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
C++ é uma linguagem de programação compilada de uso geral criada por Bjarne Stroustrup, lançada pela primeira vez em 1985. Ela estende C com recursos orientados a objetos, genéricos e - em versões modernas (C++ 11 e posteriores) - abstrações de alto nível como lambdas, ponteiros inteligentes e a Biblioteca de Modelos Padrão (STL). C++ segue o princípio da "abstração de sobrecarga zero": você não deve pagar por recursos que não usa.
C++ é a linguagem preferida quando você precisa de alto desempenho e poder expressivo. Ele alimenta motores de jogos (Unreal Engine), navegadores (Chrome, Firefox), bancos de dados (MongoDB), sistemas operacionais (partes do Windows e macOS), sistemas de negociação financeira e simulações em tempo real.
---

## Por que C++ é importante
- **Desempenho com expressividade**: Velocidade quase C com classes, modelos e abstrações modernas.
- **Princípio de sobrecarga zero**: as abstrações são compiladas no mesmo código que você escreveria manualmente em C.
- **Grande base de código**: Décadas de infraestrutura crítica – jogos, navegadores, bancos de dados, sistemas embarcados.
- **Multiparadigma**: Suporta estilos de programação processual, orientada a objetos, genérica e funcional.
- **Destruição determinística**: RAII garante que os recursos sejam limpos de forma previsível - sem pausas no coletor de lixo.
## As compensações
| Limitação | Detalhes | Solução alternativa típica |
|-------|---------|-------------------|
| **Complexidade** | A linguagem é enorme – mesmo os especialistas não sabem tudo | Atenha-se ao C++ moderno (C++17/20); evite padrões herdados |
| **Segurança de memória** | Gerenciamento manual de memória; ponteiros pendentes, vazamentos, UB | Use ponteiros inteligentes, RAII e std::optional |
| **Tempos de compilação** | Grandes projetos podem levar minutos para serem compilados | Cabeçalhos pré-compilados, módulos (C++20), compilações incrementais |
| **Mensagens de erro** | Erros de modelo podem ter centenas de linhas | Use static_assert, conceitos (C++20), melhores compiladores |
| **Compatibilidade binária** | Instabilidade da ABI nas versões do compilador | Interfaces C estáveis ​​para bibliotecas compartilhadas |
---

## Fundamentos de sintaxe
### Estrutura Básica
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

### Classes e Programação Orientada a Objetos
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

### Modelos (programação genérica)
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

### Recursos modernos do C++ (C++17/20)
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

## A Biblioteca Padrão
### Contêineres
| Recipiente | Tipo | Usar quando |
|-----------|------|----------|
| std::vetor | Matriz dinâmica | Escolha padrão para dados sequenciais |
| std::deque | Fila dupla | Precisa de inserção/apagamento rápido em ambas as extremidades |
| std::lista | Lista duplamente vinculada | Inserção/apagamento frequente no meio |
| std::mapa | Mapa de árvore ordenado | Precisa de chaves classificadas, pesquisa O (log n) |
| std::unordered_map | Mapa hash | Pesquisa rápida de média O(1) |
| std::definir | Conjunto encomendado | Elementos classificados exclusivos |
| std::matriz | Matriz de tamanho fixo | Tamanho conhecido e alocado na pilha em tempo de compilação |
| std::string | Texto | Sempre use isso, nunca char bruto* |
### Ponteiros inteligentes
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

## Sintaxe e padrões avançados
### Conceitos (C++20)
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

### Mover Semântica e RAII
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

### Hierarquia de exceções personalizadas
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

## Simultaneidade e paralelismo
### std::thread e sincronização
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

### Assíncrono, Futuros e Promessas
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

## Configuração do projeto e sistema de construção
### Estrutura do Projeto
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

###CMakeLists.txt
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

### Pipeline de CI/CD (ações do GitHub)
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

## Teste
### Exemplo de teste do Google
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

## Interoperabilidade
### Interoperabilidade C (externo "C")
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

## Padrões de Projeto
### Padrão de fábrica
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

### Padrão Observador
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

## Desempenho e otimização
### Ferramentas de criação de perfil
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Exemplo de benchmark (benchmark do Google)
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

### Técnicas de otimização
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

## Implantação
### Implantação do Docker
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

## Compilação e ferramentas
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Ferramenta | Finalidade |
|------|---------|
| **GCC/Clang/MSVC** | Compiladores |
| **CMake** | Gerador de sistema de construção (padrão da indústria) |
| **GDB/LLDB** | Depuradores |
| **Valgrind / AddressSanitizer** | Detecção de erro de memória |
| **clang-arrumado** | Linting e modernização |
| **formato clang** | Formatação de código |
| **Conan/vcpkg** | Gerenciadores de pacotes |
| **Teste Google/Catch2** | Estruturas de teste |
---

## Quando usar C++
| Cenário | Por que C++ | Melhor Alternativa |
|----------|---------|-------------------|
| Motores de jogo | Desempenho + controle em tempo real | -- |
| Navegadores | Décadas de código otimizado | Rust para novos componentes do navegador |
| Negociação de alta frequência | A latência de microssegundos é importante | -- |
| Sistemas embarcados (complexos) | Rico conjunto de recursos com acesso a hardware | C para mais simples, Rust para segurança |
| Aplicativos GUI (desktop) | A estrutura Qt está madura | C# (Windows), Swift (macOS) |
| Desenvolvimento geral de aplicações | Muito complexo para a maioria dos aplicativos | Python, Go, Java |
| Back-ends da Web | Não é a escolha típica | Vá, Ferrugem, Node.js |
| Scripting/automação | Ferramenta totalmente errada | Python, JavaScript |
---

## Evolução dos padrões C++
| Padrão | Ano | Principais recursos |
|----------|------|------------|
| C++98 | 1998 | O padrão ISO original; STL, iostreams |
| C++11 | 2011 | **Começa o C++ moderno**: automático, lambdas, ponteiros inteligentes, semântica de movimentação |
| C++14 | 2014 | Lambdas genéricos, std::make_unique, dedução do tipo de retorno |
| C++17 | 2017 | Ligações estruturadas, std::optional, std::variant, std::filesystem |
| C++20 | 2020 | **Lançamento principal**: conceitos, intervalos, corrotinas, módulos |
| C++23 | 2023 | std::esperado, std::print, deduzindo isso |
Para novos projetos, direcione o C++20 no mínimo.
---

## Perguntas e respostas sintéticas
### Q1: Qual é a diferença entre`std::unique_ptr`,`std::shared_ptr`e`std::weak_ptr`?
**R:**`unique_ptr`representa propriedade exclusiva — apenas um ponteiro pode possuir o recurso. Ele tem sobrecarga zero (o mesmo que um ponteiro bruto) e não pode ser copiado, apenas movido. `shared_ptr`representa propriedade compartilhada — vários ponteiros compartilham o recurso, com contagem de referência. Quando o último`shared_ptr`for destruído, o recurso será liberado. `weak_ptr`é um observador não proprietário de um`shared_ptr`— ele não aumenta a contagem de referências e é usado para quebrar referências circulares.
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

### Q2: O que é semântica de movimento e por que ela é importante?
**R:** A semântica de movimentação (C++11) permite a transferência de recursos (memória heap, identificadores de arquivo etc.) de um objeto temporário em vez de copiá-los. Um construtor/atribuição de movimento pega uma referência de valor (`T&&`) e "rouba" os recursos da fonte, deixando-a em um estado válido, mas não especificado. Isso elimina cópias desnecessárias e é o motivo pelo qual a realocação de`std::vector`é eficiente.
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

### Q3: Quando devo usar`auto`e quando devo especificar os tipos explicitamente?
**R:** Use`auto`quando o tipo for óbvio no contexto (loops de iterador, chamadas `make_unique`/`make_shared`, tipos lambda, tipos de modelos complexos). Especifique os tipos explicitamente quando o tipo não for óbvio, quando você precisar de conversões implícitas ou em assinaturas de API públicas. O estilo "Almost Always Auto" (AAA) favorece`auto`para variáveis ​​locais; o estilo "automático onde útil" é mais conservador.
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

### Q4: Como os conceitos (C++20) melhoram o código do modelo?
**R:** Os conceitos restringem os parâmetros do modelo com requisitos nomeados, produzindo mensagens de erro claras e permitindo a sobrecarga de funções nas restrições do modelo. Antes dos conceitos, SFINAE e`static_assert`eram usados ​​– ambos produziam erros crípticos. Os conceitos tornam o código do modelo legível e combinável.
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

### Q5: O que é a Regra dos Cinco e como ela se relaciona com a Regra do Zero?
**R:** A regra dos cinco: se você definir qualquer um entre destruidor, construtor de cópia, atribuição de cópia, construtor de movimento ou atribuição de movimento, deverá definir todos os cinco. A Regra de Zero (preferencial): projete classes para que não precisem de nenhuma delas - use tipos RAII (`std::string`,`std::vector`,`std::unique_ptr`) como membros, e os especiais gerados pelo compilador farão a coisa certa automaticamente.
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

## Resolução de problemas por cadeia de pensamento
### Problema 1: Implementar uma fila produtor-consumidor thread-safe com intervalos
**Declaração do problema:** Crie uma fila produtor-consumidor limitada e segura para threads usando intervalos C++20 para o lado do consumidor. A fila deve bloquear os produtores quando estiver cheia e os consumidores quando estiver vazia e suportar o desligamento normal.
**Etapa 1 — Entenda o problema:**
Precisamos de: (1) uma fila limitada com bloqueio push/pop, (2) segurança de thread via mutex e variáveis de condição, (3) uma maneira de sinalizar o desligamento, (4) integração de intervalos C++20 para que os consumidores possam usar loops for baseados em intervalo.
**Etapa 2 — Identifique a abordagem:**
- Use`std::mutex`+`std::condition_variable`para bloqueio.
- Use`std::queue<T>`como contêiner subjacente.
- Use`std::optional<T>`como tipo de retorno -`std::nullopt`sinaliza desligamento.
- Implementar um iterador baseado em sentinela para suporte de intervalos.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Segurança de thread:`std::mutex`protege todos os estados da fila; variáveis ​​de condição controlam o bloqueio.
- Desligamento normal:`shutdown()`acorda todos os garçons; `pop()`retorna`nullopt`quando vazio e desligado.
- Suporte de intervalo: a sentinela do iterador (construída por padrão) compara-se igual a qualquer iterador esgotado.
- Produção: use`boost::lockfree::spsc_queue`para produtor único e consumidor único sem bloqueio ou`folly::ProducerConsumerQueue`para cenários de alto rendimento.
### Problema 2: Implementar qualquer tipo apagado por tipo
**Declaração do problema:** Implemente uma versão simplificada de`std::any`(C++17) do zero — um contêiner de tipo seguro para valores únicos de qualquer tipo, com suporte para cópia, movimentação e recuperação de tipo seguro por meio de`any_cast`.
**Etapa 1 — Entenda o problema:**
`std::any`armazena um valor de qualquer tipo copiável e o recupera com verificação de tipo. Internamente, ele usa apagamento de tipo: uma interface de classe base com um modelo derivado que contém o valor real. `any_cast`verifica o tipo armazenado em tempo de execução e lança`bad_any_cast`em caso de incompatibilidade.
**Etapa 2 — Identifique a abordagem:**
- Use uma classe base`HolderBase`com`clone()`e`type()`virtuais.
- Use um modelo derivado`Holder<T>`que armazena o valor real.
- Armazene um`std::unique_ptr<HolderBase>`na classe `Any`.
-`any_cast<T>`verifica`typeid`e executa um`static_cast`.
**Etapa 3 — Implementar a solução:**
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

**Etapa 4 — Verificar e otimizar:**
- Segurança de tipo:`any_cast`verifica`typeid`em tempo de execução - o tipo errado gera`BadAnyCast`.
- Semântica de cópia: o`clone()`virtual cria uma cópia profunda do valor retido.
- Semântica de movimentação: o construtor/atribuição de movimentação padrão transfere o`unique_ptr`de forma eficiente.
- Otimização de buffer pequeno (como`std::any`real): armazena pequenos tipos inline sem alocação de heap. Isso requer um`union`com um buffer de bytes – significativamente mais complexo.
- Produção: use`std::any`(C++17) — é padrão, bem testado e pode incluir SBO.
---

## Resumo
C++ ocupa uma posição única na programação: oferece o desempenho bruto de C com o poder expressivo de abstrações de alto nível. O C++ moderno (C++20/23) é uma linguagem muito diferente do C++ da década de 1990 – é mais seguro, mais expressivo e mais produtivo. A curva de aprendizado é íngreme e o idioma recompensa a disciplina. Para aplicativos de desempenho crítico onde você precisa de controle refinado, C++ continua sendo uma das melhores ferramentas disponíveis.