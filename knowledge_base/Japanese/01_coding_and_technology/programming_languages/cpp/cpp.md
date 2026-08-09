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
C++ は、Bjarne Stroustrup によって作成された汎用のコンパイル済みプログラミング言語で、1985 年に初めてリリースされました。C++ は、オブジェクト指向機能、ジェネリックス、および最新バージョン (C++11 以降) では、ラムダ、スマート ポインター、標準テンプレート ライブラリ (STL) などの高レベルの抽象化によって C を拡張します。 C++ は、「ゼロオーバーヘッド抽象化」の原則に従います。つまり、使用しない機能に対して料金を支払うべきではありません。
C++ は、高いパフォーマンスと表現力の両方が必要な場合に最適な言語です。ゲーム エンジン (Unreal Engine)、ブラウザ (Chrome、Firefox)、データベース (MongoDB)、オペレーティング システム (Windows および macOS の一部)、金融取引システム、およびリアルタイム シミュレーションを強化します。
---

## C++ が重要な理由
- **表現力豊かなパフォーマンス**: クラス、テンプレート、最新の抽象化による C に近い速度。
- **オーバーヘッドゼロの原則**: 抽象化は、C で手動で作成するのと同じコードにコンパイルされます。
- **大規模なコードベース**: ゲーム、ブラウザ、データベース、組み込みシステムなど、数十年にわたる重要なインフラストラクチャ。
- **マルチパラダイム**: 手続き型、オブジェクト指向、汎用、および関数型プログラミング スタイルをサポートします。
- **決定的破壊**: RAII は、リソースが予測どおりにクリーンアップされることを保証します。ガベージ コレクターは停止しません。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **複雑さ** |この言語は膨大であり、専門家でもすべてを知っているわけではありません。最新の C++ (C++17/20) に固執します。レガシーパターンを避ける |
| **メモリの安全性** |手動メモリ管理。未解決ポインタ、リーク、UB |スマート ポインター、RAII、および std::optional を使用する |
| **コンパイル時間** |大規模なプロジェクトのコンパイルには数分かかることがあります。プリコンパイル済みヘッダー、モジュール (C++20)、インクリメンタル ビルド |
| **エラー メッセージ** |テンプレート エラーは数百行に及ぶ場合があります。 static_assert、概念 (C++20)、より優れたコンパイラを使用する |
| **バイナリ互換性** |コンパイラのバージョン間での ABI の不安定性 |共有ライブラリ用の安定した C インターフェイス |
---

## 構文の基礎
### 基本構造
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

### クラスとオブジェクト指向プログラミング
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

### テンプレート (汎用プログラミング)
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

### 最新の C++ 機能 (C++17/20)
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

## 標準ライブラリ
### コンテナ
|コンテナ |タイプ |いつ使用する |
|----------|------|----------|
| std::vector |動的配列 |順次データのデフォルトの選択 |
| std::deque |両端キュー |両端での高速な挿入/消去が必要 |
| std::リスト |二重リンクリスト |頻繁に途中で挿入/消去する |
| std::マップ |順序付きツリーマップ |ソートされたキーが必要です。O(log n) ルックアップ |
| std::unordered_map |ハッシュマップ |高速 O(1) 平均ルックアップ |
| std::set |オーダーセット |ユニークにソートされた要素 |
| std::配列 |固定サイズの配列 |スタックに割り当てられ、コンパイル時に既知のサイズ |
| std::文字列 |テキスト |常にこれを使用し、生の char* は使用しないでください。
### スマート ポインター
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

### アルゴリズム
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

## 高度な構文とパターン
### 概念 (C++20)
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

### 移動セマンティクスと RAII
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

### カスタム例外階層
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

## 同時実行性と並列処理
### std::thread と同期
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

### 非同期、先物、および約束
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

## プロジェクトの構成とシステムの構築
### プロジェクトの構造
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

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### Google テストの例
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

## 相互運用性
### C 相互運用性 (外部 "C")
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

## デザインパターン
### ファクトリーパターン
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

### オブザーバーパターン
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

## パフォーマンスと最適化
### プロファイリングツール
```bash
perf record -g ./my_app
perf report
valgrind --tool=callgrind ./my_app
valgrind --tool=massif ./my_app
```

### ベンチマークの例 (Google ベンチマーク)
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

### 最適化手法
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

## デプロイメント
### Docker のデプロイメント
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

## コンパイルとツール
```bash
g++ -std=c++20 -Wall -Wextra -o myprogram main.cpp
g++ -std=c++20 -O2 -o myprogram main.cpp
cmake -B build -S .
cmake --build build
```

|ツール |目的 |
|-----|----------|
| **GCC / Clang / MSVC** |コンパイラ |
| **CMake** |ビルド システム ジェネレーター (業界標準) |
| **GDB / LLDB** |デバッガー |
| **Valgrind / AddressSanitizer** |メモリエラー検出 |
| **カチャカチャ整頓** |リンティングと最新化 |
| **clang 形式** |コードのフォーマット |
| **コナン / vcpkg** |パッケージマネージャー |
| **Google テスト / Catch2** |テストフレームワーク |
---

## C++ を使用する場合
|シナリオ |なぜ C++ なのか |より良い代替案 |
|----------|----------|----------|
|ゲームエンジン |パフォーマンス + リアルタイム制御 | -- |
|ブラウザ |数十年にわたる最適化されたコード |新しいブラウザコンポーネント用のRust |
|高頻度取引 |マイクロ秒のレイテンシーが重要 | -- |
|組み込みシステム (複合) |ハードウェアアクセスを備えた豊富な機能セット | C はシンプル、Rust は安全 |
| GUI アプリケーション (デスクトップ) | Qt フレームワークは成熟しています | C# (Windows)、Swift (macOS) |
|一般的なアプリケーション開発 |ほとんどのアプリには複雑すぎる | Python、Go、Java |
| Web バックエンド |一般的な選択ではありません | Go、Rust、Node.js |
|スクリプト作成 / 自動化 |完全に間違ったツール | Python、JavaScript |
---

## C++ 標準の進化
|標準 |年 |主な機能 |
|----------|------|---------------|
| C++98 | 1998年 |オリジナルの ISO 規格。 STL、iostream |
| C++11 | 2011年 | **モダン C++ の始まり**: 自動、ラムダ、スマート ポインター、移動セマンティクス |
| C++14 | 2014年 |汎用ラムダ、std::make_unique、戻り値の型の推定 |
| C++17 | 2017年 |構造化バインディング、std::optional、std::variant、std::filesystem |
| C++20 | 2020年 | **メジャー リリース**: 概念、範囲、コルーチン、モジュール |
| C++23 | 2023年 | std::expected、std::print、これを推定する |
新しいプロジェクトの場合は、少なくとも C++20 をターゲットにしてください。
---

＃＃ まとめ
C++ はプログラミングにおいて独特の位置を占めており、高レベルの抽象化の表現力を備えた C のそのままのパフォーマンスを提供します。最新の C++ (C++20/23) は、1990 年代の C++ とは大きく異なる言語であり、より安全で、表現力が豊かで、生産性が高くなります。学習曲線は急勾配であり、この言語は規律に報います。きめ細かい制御が必要なパフォーマンスが重要なアプリケーションにとって、C++ は依然として利用可能な最良のツールの 1 つです。