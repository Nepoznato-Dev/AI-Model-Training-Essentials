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
# C++
C++ est un langage de programmation compilé à usage général créé par Bjarne Stroustrup, publié pour la première fois en 1985. Il étend le C avec des fonctionnalités orientées objet, des génériques et - dans les versions modernes (C++ 11 et versions ultérieures) - des abstractions de haut niveau comme les lambdas, les pointeurs intelligents et la bibliothèque de modèles standard (STL). C++ suit le principe de « l'abstraction sans surcharge » : vous ne devez pas payer pour des fonctionnalités que vous n'utilisez pas.
C++ est le langage de choix lorsque vous avez besoin à la fois de hautes performances et de puissance d'expression. Il alimente les moteurs de jeu (Unreal Engine), les navigateurs (Chrome, Firefox), les bases de données (MongoDB), les systèmes d'exploitation (parties de Windows et macOS), les systèmes de trading financier et les simulations en temps réel.
---

## Pourquoi le C++ est important
- **Performance avec expressivité** : vitesse proche du C avec classes, modèles et abstractions modernes.
- **Principe de zéro surcharge** : les abstractions se compilent dans le même code que vous écririez à la main en C.
- **Base de code massive** : des décennies d'infrastructure critique : jeux, navigateurs, bases de données, systèmes embarqués.
- **Multi-paradigme** : prend en charge les styles de programmation procédurale, orientée objet, générique et fonctionnelle.
- **Destruction déterministe** : RAII garantit que les ressources sont nettoyées de manière prévisible – aucune pause du ramasse-miettes.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Complexité** | Le langage est énorme – même les experts ne le connaissent pas entièrement | S'en tenir au C++ moderne (C++17/20) ; éviter les modèles hérités |
| **Sécurité de la mémoire** | Gestion manuelle de la mémoire ; pointeurs pendants, fuites, UB | Utilisez des pointeurs intelligents, RAII et std::optional |
| **Temps de compilation** | La compilation des grands projets peut prendre quelques minutes | En-têtes précompilés, modules (C++20), builds incrémentielles |
| **Messages d'erreur** | Les erreurs de modèle peuvent comporter des centaines de lignes | Utilisez static_assert, concepts (C++20), meilleurs compilateurs |
| **Compatibilité binaire** | Instabilité ABI entre les versions du compilateur | Interfaces C stables pour bibliothèques partagées |
---

## Fondamentaux de la syntaxe
### Structure de base
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

### Classes et programmation orientée objet
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

### Modèles (programmation générique)
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

### Fonctionnalités C++ modernes (C++17/20)
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

## La bibliothèque standard
### Conteneurs
| Conteneur | Tapez | Utiliser quand |
|---------------|------|--------------|
| std::vecteur | Tableau dynamique | Choix par défaut pour les données séquentielles |
| std::deque | File d'attente à double extrémité | Besoin d'une insertion/effacement rapide aux deux extrémités |
| std :: liste | Liste doublement chaînée | Insertion/effacement fréquent au milieu |
| std::carte | Carte des arbres ordonnés | Besoin de clés triées, recherche O(log n) |
| std::unordered_map | Carte de hachage | Recherche moyenne rapide O(1) |
| std::set | Ensemble commandé | Éléments triés uniques |
| std :: tableau | Tableau de taille fixe | Allocation par pile, taille connue au moment de la compilation |
| std::chaîne | Texte | Utilisez toujours ceci, jamais de caractère brut* |
### Pointeurs intelligents
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

### Algorithmes
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

## Syntaxe et modèles avancés
###Concepts (C++20)
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

### Sémantique de déplacement et RAII
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

### Hiérarchie des exceptions personnalisées
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

## Concurrence et parallélisme
### std :: thread et synchronisation
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

### Async, Futures et Promesses
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

## Configuration du projet et système de construction
### Structure du projet
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

### Pipeline CI/CD (actions GitHub)
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

## Tests
### Exemple de test Google
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

## Interopérabilité
### C Interop (externe "C")
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

## Modèles de conception
### Modèle d'usine
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

### Modèle d'observateur
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

## Performances et optimisation
### Outils de profilage
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### Exemple de référence (Google Benchmark)
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

### Techniques d'optimisation
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

## Déploiement
### Déploiement de Docker
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

## Compilation et outillage
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

| Outil | Objectif |
|------|--------------|
| **GCC/Clang/MSVC** | Compilateurs |
| **CMake** | Générateur de système de construction (norme industrielle) |
| **GDB / LLDB** | Débogueurs |
| **Valgrind / AddressSanitizer** | Détection d'erreur de mémoire |
| **clang-bien rangé** | Peluchage et modernisation |
| **format clang** | Formatage des codes |
| **Conan / vcpkg** | Gestionnaires de paquets |
| **Google Test/Catch2** | Cadres de test |
---

## Quand utiliser C++
| Scénario | Pourquoi C++ | Meilleure alternative |
|--------------|---------|-------------------|
| Moteurs de jeu | Performance + contrôle en temps réel | -- |
| Navigateurs | Des décennies de code optimisé | Rust pour les nouveaux composants du navigateur |
| Trading haute fréquence | La latence en microsecondes est importante | -- |
| Systèmes embarqués (complexes) | Ensemble de fonctionnalités riches avec accès matériel | C pour plus simple, Rust pour la sécurité |
| Applications GUI (ordinateur de bureau) | Le framework Qt est mature | C# (Windows), Swift (macOS) |
| Développement d'applications générales | Trop complexe pour la plupart des applications | Python, Go, Java |
| Moteurs Web | Ce n'est pas le choix habituel | Allez, Rust, Node.js |
| Scripts / automatisation | Mauvais outil entièrement | Python, JavaScript |
---

## Évolution des normes C++
| Norme | Année | Principales fonctionnalités |
|--------------|------|-------------|
| C++98 | 1998 | La norme ISO originale ; STL, iostreams |
| C++11 | 2011 | **Début du C++ moderne** : auto, lambdas, pointeurs intelligents, sémantique de déplacement |
| C++14 | 2014 | Lambdas génériques, std::make_unique, déduction de type de retour |
| C++17 | 2017 | Liaisons structurées, std :: optionnel, std :: variante, std :: filesystem |
| C++20 | 2020 | **Version majeure** : concepts, plages, coroutines, modules |
| C++23 | 2023 | std::expected, std::print, en déduisant ceci |
Pour les nouveaux projets, ciblez au minimum C++20.
---

## Questions et réponses synthétiques
### Q1 : Quelle est la différence entre`std::unique_ptr`,`std::shared_ptr`et `std::weak_ptr` ?
**R :**`unique_ptr`représente la propriété exclusive : un seul pointeur peut posséder la ressource. Il n'a aucune surcharge (identique à un pointeur brut) et ne peut pas être copié, seulement déplacé. `shared_ptr`représente la propriété partagée : plusieurs pointeurs partagent la ressource, avec comptage de références. Lorsque le dernier`shared_ptr`est détruit, la ressource est libérée. `weak_ptr`est un observateur non propriétaire d'un`shared_ptr`— il n'augmente pas le nombre de références et est utilisé pour briser les références circulaires.
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

### Q2 : Qu'est-ce que la sémantique des mouvements et pourquoi est-elle importante ?
**R :** La sémantique de déplacement (C++11) permet de transférer des ressources (mémoire tas, descripteurs de fichiers, etc.) à partir d'un objet temporaire au lieu de les copier. Un constructeur/affectation de déplacement prend une référence rvalue (`T&&`) et "vole" les ressources de la source, la laissant dans un état valide mais non spécifié. Cela élimine les copies inutiles et c’est la raison pour laquelle la réallocation`std::vector`est efficace.
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

### Q3 : Quand dois-je utiliser`auto`et quand dois-je spécifier explicitement les types ?
**R :** Utilisez`auto`lorsque le type est évident d'après le contexte (boucles d'itérateur, appels`make_unique`/ `make_shared`, types lambda, types de modèles complexes). Spécifiez explicitement les types lorsque le type n'est pas évident, lorsque vous avez besoin de conversions implicites ou dans les signatures d'API publiques. Le style « Presque toujours automatique » (AAA) privilégie`auto`pour les variables locales ; le style « auto là où cela est utile » est plus conservateur.
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

### Q4 : Comment les concepts (C++20) améliorent-ils le code des modèles ?
**R :** Les concepts contraignent les paramètres du modèle avec des exigences nommées, produisant des messages d'erreur clairs et permettant une surcharge de fonctions sur les contraintes du modèle. Avant les concepts, SFINAE et`static_assert`étaient utilisés – tous deux produisaient des erreurs énigmatiques. Les concepts rendent le code du modèle lisible et composable.
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

### Q5 : Qu'est-ce que la règle de cinq et quel est son rapport avec la règle de zéro ?
**R :** La règle de cinq : si vous définissez l'un des éléments suivants : destructeur, constructeur de copie, affectation de copie, constructeur de déplacement ou affectation de déplacement, vous devez définir les cinq. La règle de zéro (préférée) : concevez les classes pour qu'elles n'en aient pas besoin - utilisez les types RAII (`std::string`,`std::vector`,`std::unique_ptr`) comme membres, et les spéciaux générés par le compilateur feront automatiquement la bonne chose.
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

## Résolution de problèmes en chaîne de pensée
### Problème 1 : implémenter une file d'attente producteur-consommateur Thread-Safe avec des plages
**Énoncé du problème :** Créez une file d'attente producteur-consommateur limitée et sécurisée pour les threads à l'aide de plages C++20 pour le côté consommateur. La file d'attente doit bloquer les producteurs lorsqu'ils sont pleins et les consommateurs lorsqu'ils sont vides, et permettre un arrêt progressif.
**Étape 1 — Comprendre le problème :**
Nous avons besoin de : (1) une file d'attente limitée avec blocage push/pop, (2) la sécurité des threads via des mutex et des variables de condition, (3) un moyen de signaler l'arrêt, (4) l'intégration des plages C++ 20 afin que les consommateurs puissent utiliser des boucles for basées sur des plages.
**Étape 2 — Identifiez l'approche :**
- Utilisez`std::mutex`+`std::condition_variable`pour le blocage.
- Utilisez`std::queue<T>`comme conteneur sous-jacent.
- Utilisez`std::optional<T>`comme type de retour —`std::nullopt`signale l'arrêt.
- Implémenter un itérateur basé sur sentinelle pour la prise en charge des plages.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Sécurité des threads :`std::mutex`protège tous les états de file d'attente ; les variables de condition gèrent le blocage.
- Arrêt progressif :`shutdown()`réveille tous les serveurs ; `pop()`renvoie`nullopt`lorsqu'il est vide et arrêté.
- Prise en charge de la plage : la sentinelle de l'itérateur (construite par défaut) est égale à n'importe quel itérateur épuisé.
- Production : utilisez`boost::lockfree::spsc_queue`pour un producteur unique et un consommateur unique sans verrouillage, ou`folly::ProducerConsumerQueue`pour les scénarios à haut débit.
### Problème 2 : implémenter un type quelconque effacé
**Énoncé du problème :** Implémentez une version simplifiée de`std::any`(C++17) à partir de zéro : un conteneur de type sécurisé pour les valeurs uniques de tout type, prenant en charge la copie, le déplacement et la récupération de type sécurisé via`any_cast`.
**Étape 1 — Comprendre le problème :**
`std::any`stocke une valeur de n'importe quel type copiable et la récupère avec vérification de type. En interne, il utilise l'effacement de type : une interface de classe de base avec un modèle dérivé qui contient la valeur réelle. `any_cast`vérifie le type stocké au moment de l'exécution et renvoie`bad_any_cast`en cas de non-concordance.
**Étape 2 — Identifiez l'approche :**
- Utilisez une classe de base`HolderBase`avec les`clone()`et`type()`virtuels.
- Utilisez un modèle dérivé`Holder<T>`qui stocke la valeur réelle.
- Stockez un`std::unique_ptr<HolderBase>`dans la classe `Any`.
-`any_cast<T>`vérifie`typeid`et effectue un`static_cast`.
**Étape 3 — Mettre en œuvre la solution :**
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

**Étape 4 – Vérifier et optimiser :**
- Sécurité du type :`any_cast`vérifie`typeid`au moment de l'exécution — un type incorrect lance`BadAnyCast`.
- Copier la sémantique : le virtuel`clone()`crée une copie complète de la valeur détenue.
- Sémantique de déplacement : le constructeur/affectation de déplacement par défaut transfère efficacement le `unique_ptr`.
- Optimisation des petits tampons (comme le vrai`std::any`) : stockez les petits types en ligne sans allocation de tas. Cela nécessite un`union`avec un tampon d'octets – beaucoup plus complexe.
- Production : utilisez`std::any`(C++17) — il est standard, bien testé et peut inclure SBO.
---

## Résumé
Le C++ occupe une position unique dans la programmation : il vous offre les performances brutes du C avec la puissance expressive des abstractions de haut niveau. Le C++ moderne (C++20/23) est un langage très différent du C++ des années 1990 : il est plus sûr, plus expressif et plus productif. La courbe d'apprentissage est abrupte et la langue récompense la discipline. Pour les applications critiques en termes de performances où vous avez besoin d’un contrôle précis, C++ reste l’un des meilleurs outils disponibles.