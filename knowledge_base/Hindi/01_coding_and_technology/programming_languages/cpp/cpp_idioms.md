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
# C++ - मुहावरेदार पैटर्न और सर्वोत्तम अभ्यास
यह मार्गदर्शिका स्वच्छ, आधुनिक C++ (20/23) कोड लिखने के लिए मुहावरेदार पैटर्न और सर्वोत्तम प्रथाओं को शामिल करती है।
---

## आरएआईआई और स्मार्ट पॉइंटर्स
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

## आधुनिक C++ प्रकार
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

## शब्दार्थ को स्थानांतरित करें
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

## रेंज और एल्गोरिदम (सी++20)
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

## अवधारणाएँ (सी++20)
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

## त्रुटि प्रबंधन
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

## क्लास डिज़ाइन
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

## समवर्ती
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

## सारांश
आधुनिक C++ मुहावरे जोर देते हैं: RAII और स्मार्ट पॉइंटर्स, मूव सेमेन्टिक्स, प्रकार कटौती के लिए `auto`, रेंज और एल्गोरिदम (C++20), टेम्पलेट बाधाओं के लिए अवधारणाएं, अनुपस्थिति/त्रुटियों के लिए`std::optional`/ `std::expected`, शून्य का नियम, और संकलन-समय गणना के लिए `constexpr`। फ़ॉर्मेटिंग के लिए `clang-format`, लाइनिंग के लिए`clang-tidy`का पालन करें और`-Wall -Wextra -Werror`के साथ संकलन करें। C++ समुदाय शून्य-लागत अमूर्तता को महत्व देता है और "जो आप उपयोग नहीं करते उसके लिए भुगतान न करें।"