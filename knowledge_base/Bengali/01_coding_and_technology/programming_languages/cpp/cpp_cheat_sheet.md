---
# Metadata
title: "C++ — Cheat Sheet"
description: "Quick-reference cheat sheet for C++ syntax, STL, and modern C++ patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [cpp, stl, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C++ — চিট শীট
## মৌলিক
```cpp
// Variables
int x = 42;
double pi = 3.14159;
std::string name = "Alice";
bool active = true;
auto inferred = 42;          // type deduced
const int MAX = 100;
constexpr double PI = 3.14159265358979;

// Type aliases
using String = std::string;
using Callback = std::function<void(int)>;

// String operations
std::string s = "Hello, World!";
s.length();          // or s.size()
s.substr(0, 5);      // "Hello"
s.find("World");     // 7
s.replace(7, 5, "C++");
s + " appended";
#include <format>
std::format("Hello, {}!", name);  // C++20
```

## ধারক (STL)
```cpp
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <array>

// vector
std::vector<int> v = {1, 2, 3};
v.push_back(4);
v[0]; v.at(0);
v.size();
v.begin(), v.end();
for (auto& x : v) { ... }

// array (fixed size)
std::array<int, 5> a = {1, 2, 3, 4, 5};

// map (ordered)
std::map<std::string, int> m;
m["alice"] = 90;
m.insert({"bob", 85});
m.contains("alice");  // C++20
for (auto& [key, val] : m) { ... }

// unordered_map (hash map)
std::unordered_map<std::string, int> um;

// set
std::set<int> s = {3, 1, 4, 1, 5};  // {1, 3, 4, 5}

// optional (C++17)
std::optional<int> find(std::string_view key);
auto result = find("alice");
if (result) { use(*result); }
result.value_or(0);

// span (C++20)
void process(std::span<int> data);
```

## স্মার্ট পয়েন্টার এবং মেমরি
```cpp
#include <memory>

// unique_ptr
auto p = std::make_unique<Point>(1, 2);
// p is automatically deleted; cannot be copied
auto p2 = std::move(p);  // transfer ownership

// shared_ptr
auto sp = std::make_shared<Point>(1, 2);
auto sp2 = sp;  // reference count = 2

// weak_ptr
std::weak_ptr<Point> wp = sp;
if (auto locked = wp.lock()) { use(*locked); }

// Raw pointers (avoid when possible)
int* raw = new int(42);
delete raw;
int* arr = new int[10];
delete[] arr;
```

## ক্লাস
```cpp
class Animal {
public:
    Animal(std::string name) : name_(std::move(name)) {}
    virtual ~Animal() = default;

    virtual std::string speak() const = 0;
    std::string name() const { return name_; }

private:
    std::string name_;
};

class Dog : public Animal {
public:
    using Animal::Animal;  // inherit constructors
    std::string speak() const override { return name() + " barks"; }
};

// Struct (default public)
struct Point {
    double x{}, y{};
    double distance_to(const Point& o) const {
        return std::sqrt((x-o.x)*(x-o.x) + (y-o.y)*(y-o.y));
    }
};
```

## টেমপ্লেট এবং জেনেরিক
```cpp
// Function template
template<typename T>
T max_val(T a, T b) { return (a > b) ? a : b; }

// Class template
template<typename T, size_t N>
class Buffer {
    std::array<T, N> data_;
public:
    T& operator[](size_t i) { return data_[i]; }
};

// Concepts (C++20)
template<typename T>
concept Printable = requires(T t) {
    { std::cout << t } -> std::same_as<std::ostream&>;
};

void print(const Printable auto& val) {
    std::cout << val << '\n';
}
```

## অ্যালগরিদম
```cpp
#include <algorithm>
#include <numeric>

std::vector<int> v = {5, 3, 1, 4, 2};

std::sort(v.begin(), v.end());
std::sort(v.begin(), v.end(), std::greater<>());

auto it = std::find(v.begin(), v.end(), 3);
bool exists = std::any_of(v.begin(), v.end(), [](int x){ return x > 3; });

std::transform(v.begin(), v.end(), v.begin(), [](int x){ return x * 2; });
int sum = std::accumulate(v.begin(), v.end(), 0);

// Ranges (C++20)
#include <ranges>
auto result = v | std::views::filter([](int x){ return x > 2; })
                | std::views::transform([](int x){ return x * x; });
```

## আধুনিক C++ বৈশিষ্ট্য
```cpp
// Structured bindings (C++17)
auto [x, y] = std::make_pair(1, 2);
auto [key, value] = *m.begin();

// if-init (C++17)
if (auto it = m.find("key"); it != m.end()) {
    use(it->second);
}

// Lambda
auto add = [](int a, int b) { return a + b; };
auto add_typed = [](int a, int b) -> int { return a + b; };
auto capture_val = [x](int a) { return a + x; };
auto capture_ref = [&x](int a) { x += a; };

// constexpr & consteval
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}
consteval int forced_compile_time(int n) { return n * n; }

// std::expected (C++23)
std::expected<int, std::string> divide(int a, int b) {
    if (b == 0) return std::unexpected("division by zero");
    return a / b;
}
```

## ত্রুটি হ্যান্ডলিং
```cpp
#include <stdexcept>

try {
    if (value < 0) throw std::invalid_argument("negative");
    auto result = risky_operation();
} catch (const std::invalid_argument& e) {
    std::cerr << "Bad arg: " << e.what() << '\n';
} catch (const std::exception& e) {
    std::cerr << "Error: " << e.what() << '\n';
}

// noexcept
void safe_function() noexcept { /* never throws */ }
```
