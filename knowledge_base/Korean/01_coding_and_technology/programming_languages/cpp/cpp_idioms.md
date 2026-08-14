<!--
---
# Metadata
title: "C++ — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, modern C++ code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [cpp, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C++ — 관용적 패턴 및 모범 사례
이 가이드에서는 깔끔하고 현대적인 C++(20/23) 코드를 작성하기 위한 관용적 패턴과 모범 사례를 다룹니다.
---

## RAII 및 스마트 포인터
```cpp
// ✅ Use smart pointers, never raw new/delete
auto ptr = std::make_unique<Widget>();
auto shared = std::make_shared<Widget>();

// ✅ RAII for all resources
std::fstream file("data.txt");
std::lock_guard<std::mutex> lock(mtx);

// ✅ Custom deleters
auto conn = std::unique_ptr<Connection, decltype(&close_connection)>(
    open_connection("host"), &close_connection);
```

---

## 최신 C++ 유형
```cpp
// ✅ auto for type deduction
auto x = 42;
auto& ref = vec[0];
auto* ptr = obj.get();
auto it = map.begin();

// ✅ std::string_view for read-only strings
void print(std::string_view sv) {
    std::cout << sv << '\n';
}

// ✅ std::span for array views (C++20)
void process(std::span<const int> data) {
    for (auto val : data) { /* ... */ }
}

// ✅ std::optional for optional values
std::optional<User> find_user(int id);

if (auto user = find_user(1)) {
    std::cout << user->name() << '\n';
}

// ✅ std::variant for type-safe unions
using Value = std::variant<int, double, std::string>;

// ✅ std::expected for error handling (C++23)
std::expected<int, std::string> parse(std::string_view sv);
```

---

## 이동 의미론
```cpp
// ✅ Move when source is no longer needed
std::vector<int> data = {1, 2, 3};
auto moved = std::move(data);  // data is now empty

// ✅ Rule of Five (or Rule of Zero)
class Widget {
    std::string name_;
    std::vector<int> data_;
    // No custom copy/move/destructor needed — Rule of Zero
};

// ✅ Pass by value + move for sink parameters
class Builder {
    std::string name_;
public:
    void set_name(std::string name) {  // pass by value
        name_ = std::move(name);       // move into member
    }
};
```

---

## 범위 및 알고리즘(C++20)
```cpp
#include <ranges>
#include <algorithm>
#include <vector>

// ✅ Range adaptors
auto result = numbers
    | std::views::filter([](int n) { return n % 2 == 0; })
    | std::views::transform([](int n) { return n * n; })
    | std::views::take(5);

// ✅ Range-based for
for (const auto& item : container) {
    process(item);
}

// ✅ Algorithms with ranges
auto it = std::ranges::find(users, "Alice", &User::name);
std::ranges::sort(data, std::greater{});
auto [min_it, max_it] = std::ranges::minmax_element(data);
```

---

## 개념(C++20)
```cpp
// ✅ Define concepts
template<typename T>
concept Printable = requires(T t) {
    { std::cout << t } -> std::convertible_to<std::ostream&>;
};

template<typename T>
concept Numeric = std::integral<T> || std::floating_point<T>;

// ✅ Constrain templates
void print(Printable auto value) {
    std::cout << value << '\n';
}

auto square(Numeric auto x) {
    return x * x;
}
```

---

## 오류 처리
```cpp
// ✅ Exceptions for exceptional situations
try {
    auto result = risky_operation();
} catch (const std::invalid_argument& e) {
    std::cerr << "Invalid: " << e.what() << '\n';
} catch (const std::runtime_error& e) {
    std::cerr << "Runtime: " << e.what() << '\n';
}

// ✅ [[nodiscard]] for return values that shouldn't be ignored
[[nodiscard]] int calculate();

// ✅ std::expected (C++23) for expected failures
auto result = parse("42");
if (result) {
    use(*result);
} else {
    handle_error(result.error());
}
```

---

## 클래스 디자인
```cpp
// ✅ Prefer structs for plain data
struct Point {
    double x, y;
};

// ✅ Classes with invariants
class BankAccount {
    std::string owner_;
    double balance_{0.0};
    
public:
    explicit BankAccount(std::string owner) : owner_(std::move(owner)) {}
    
    void deposit(double amount) {
        if (amount <= 0) throw std::invalid_argument("amount must be positive");
        balance_ += amount;
    }
    
    [[nodiscard]] double balance() const noexcept { return balance_; }
};

// ✅ constexpr for compile-time computation
constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}
static_assert(factorial(5) == 120);
```

---

## 동시성
```cpp
// ✅ std::jthread (C++20) — auto-joining
std::jthread worker([](std::stop_token st) {
    while (!st.stop_requested()) {
        do_work();
    }
});
worker.request_stop();

// ✅ std::async for simple tasks
auto future = std::async(std::launch::async, [] {
    return expensive_computation();
});
auto result = future.get();

// ✅ Mutex with lock_guard
std::mutex mtx;
{
    std::lock_guard lock(mtx);
    shared_data.push_back(value);
}
```

---

## 요약
최신 C++ 관용구는 RAII 및 스마트 포인터, 이동 의미 체계, 유형 추론을 위한 `auto`, 범위 및 알고리즘(C++20), 템플릿 제약 조건에 대한 개념, 부재/오류를 위한`std::optional`/ `std::expected`, 0의 규칙 및 컴파일 시간 계산을 위한 `constexpr`를 강조합니다. 서식 지정을 위해서는 `clang-format`를 따르고 린팅을 위해서는 `clang-tidy`를 따르고 `-Wall -Wextra -Werror`로 컴파일합니다. C++ 커뮤니티는 비용이 들지 않는 추상화를 중요하게 생각하며 "사용하지 않는 것에 대해서는 비용을 지불하지 않습니다."