---
# Metadata
title: "C++ — Common Mistakes & Anti-Patterns"
description: "Comprehensive guide to common pitfalls, traps, and anti-patterns in C++ that catch even experienced developers, with explanations and corrections."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial common mistakes document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [cpp, cplusplus, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# C++ — عام غلطیاں اور اینٹی پیٹرن
یہ دستاویز C++ میں سب سے عام غلطیوں، ٹریپس اور اینٹی پیٹرن کی فہرست بناتی ہے۔ ہر اندراج غلط نقطہ نظر کو ظاہر کرتا ہے، یہ بتاتا ہے کہ یہ کیوں ناکام ہوتا ہے، اور صحیح حل فراہم کرتا ہے۔ جدید C++ (C++ 11/14/17/20) زیادہ تر کلاسک خرابیوں سے بچنے کے لیے ٹولز فراہم کرتا ہے۔
---

## 1. تین/پانچ خلاف ورزیوں کا اصول
```cpp
// ❌ WRONG — missing copy/move semantics
class Resource {
    int* data;
public:
    Resource() : data(new int[100]) {}
    ~Resource() { delete[] data; }
    // Missing: copy constructor, copy assignment,
    // move constructor, move assignment
};

Resource a;
Resource b = a;       // shallow copy — double free on destruction!

// ✅ CORRECT — follow Rule of Five (or use Rule of Zero)
class Resource {
    std::vector<int> data;  // Rule of Zero: let compiler handle it
};

// ✅ CORRECT — explicit Rule of Five
class Resource {
    int* data;
public:
    Resource() : data(new int[100]) {}
    ~Resource() { delete[] data; }
    Resource(const Resource& other) : data(new int[100]) {
        std::copy(other.data, other.data + 100, data);
    }
    Resource& operator=(const Resource& other) {
        if (this != &other) {
            delete[] data;
            data = new int[100];
            std::copy(other.data, other.data + 100, data);
        }
        return *this;
    }
    Resource(Resource&&) noexcept = default;
    Resource& operator=(Resource&&) noexcept = default;
};
```

---

## 2. سمارٹ پوائنٹرز کے بجائے خام`new`/ `delete`
```cpp
// ❌ WRONG — manual memory management
void process() {
    Widget* w = new Widget();
    w->doSomething();
    delete w;  // skipped if doSomething() throws
}

// ✅ CORRECT — use smart pointers
void process() {
    auto w = std::make_unique<Widget>();
    w->doSomething();
}  // automatically deleted, even on exception
```

---

## 3. سلائسنگ کا مسئلہ
```cpp
// ❌ WRONG — object slicing
class Base { virtual void show() { cout << "Base"; } };
class Derived : public Base { void show() override { cout << "Derived"; } };

Base b = Derived();  // sliced! Derived part is lost
b.show();  // prints "Base"

// ✅ CORRECT — use pointers or references
std::unique_ptr<Base> b = std::make_unique<Derived>();
b->show();  // prints "Derived"

void process(const Base& b) {  // pass by reference
    b.show();  // polymorphic call
}
```

---

## 4. تکرار کرنے والا باطل
```cpp
// ❌ WRONG — erasing from vector while iterating
std::vector<int> v = {1, 2, 3, 4, 5};
for (auto it = v.begin(); it != v.end(); ++it) {
    if (*it % 2 == 0) {
        v.erase(it);  // invalidates iterator!
    }
}

// ✅ CORRECT — use erase-remove idiom
v.erase(std::remove_if(v.begin(), v.end(),
    [](int x) { return x % 2 == 0; }), v.end());

// ✅ CORRECT — C++20 std::erase_if
std::erase_if(v, [](int x) { return x % 2 == 0; });
```

---

## 5. لٹکتے ہوئے حوالہ جات
```cpp
// ❌ WRONG — returning reference to local
const std::string& getGreeting() {
    std::string s = "Hello";
    return s;  // s is destroyed, dangling reference!
}

// ✅ CORRECT — return by value (move semantics make it efficient)
std::string getGreeting() {
    return "Hello";  // NRVO or move
}
```

---

## 6.`std::move`کا صحیح استعمال نہیں کرنا
```cpp
// ❌ WRONG — move from const (prevents move)
class Widget {
    std::vector<int> data;
public:
    Widget(const Widget&& other) : data(std::move(other.data)) {}
    // other.data is const — std::move has no effect, copies instead
};

// ✅ CORRECT — non-const rvalue reference
Widget(Widget&& other) noexcept : data(std::move(other.data)) {}
```

---

## 7. اینٹی پیٹرن: ہیڈر میں`using namespace std;`کا استعمال
```cpp
// ❌ WRONG — pollutes global namespace for all includers
// widget.h
#include <vector>
using namespace std;  // forces this on everyone who includes widget.h

// ✅ CORRECT — use explicit qualification or local using
#include <vector>
class Widget {
    std::vector<int> data;
};
```

---

## 8. دستخط شدہ اوور فلو سے غیر متعینہ سلوک
```cpp
// ❌ WRONG — signed integer overflow is undefined
int a = INT_MAX;
int b = a + 1;  // undefined behavior!

// ✅ CORRECT — use unsigned for wrapping
unsigned a = UINT_MAX;
unsigned b = a + 1;  // well-defined: wraps to 0

// ✅ CORRECT — check before overflow
if (a > INT_MAX - 1) { /* handle overflow */ }
```

---

## 9. قدر کے زمرے کو نہ سمجھنا
```cpp
// ❌ WRONG — binding temporary to non-const lvalue reference
std::string& s = getTemporary();  // compile error

// ✅ CORRECT — const reference extends lifetime
const std::string& s = getTemporary();

// ✅ CORRECT — use rvalue reference
std::string&& s = getTemporary();

// ✅ CORRECT — just take ownership
auto s = getTemporary();
```

---

## 10. اینٹی پیٹرن: دستی وسائل کا انتظام (پری-RAII)
```cpp
// ❌ WRONG — C-style resource management
FILE* f = fopen("data.txt", "r");
if (!f) return;
// ... use f ...
fclose(f);  // missed on early return or exception

// ✅ CORRECT — RAII with std::unique_ptr or custom deleter
auto f = std::unique_ptr<FILE, decltype(&fclose)>(
    fopen("data.txt", "r"), &fclose);
if (!f) return;
// automatically closed
```

---

## 11. ٹیمپلیٹ بلوٹ اور لانگ کمپائل ٹائمز
```cpp
// ❌ WRONG — putting all template code in headers
// Every translation unit that includes the header instantiates the template

// ✅ CORRECT — explicit instantiation for common types
// widget.cpp
template class Widget<int>;
template class Widget<std::string>;

// ✅ CORRECT — use concepts (C++20) for clearer constraints
template <std::integral T>
T add(T a, T b) { return a + b; }
```

---

## 12.`[[nodiscard]]`اور`[[maybe_unused]]`استعمال نہیں کرنا
```cpp
// ❌ WRONG — ignoring error codes
int result = risky_operation();
// result ignored — potential bug

// ✅ CORRECT — mark functions that shouldn't be ignored
[[nodiscard]] int risky_operation();

// Compiler warns if return value is discarded
```

---

## خلاصہ
C++ کی پیچیدگی غلطیوں کے بہت سے مواقع پیدا کرتی ہے: پانچ کا قاعدہ، آبجیکٹ سلائسنگ، ایٹریٹر کی غلط کاری، لٹکتے ہوئے حوالہ جات، اور دستخط شدہ اوور فلو سے غیر متعینہ سلوک۔ جدید C++ تریاق ہے: خام`new`/`delete`کے بجائے سمارٹ پوائنٹرز استعمال کریں، تمام وسائل کے لیے RAII، خام صفوں کے بجائے`std::vector`اور `std::string`، کارکردگی کے لیے سیمنٹکس کو منتقل کریں، اور کیٹ کی قدر کو`new`پر واپس کریں۔ C++ بنیادی رہنما خطوط ایک وجہ سے موجود ہیں — ان کی پیروی کریں، اور جو کچھ آپ کھو رہے ہیں اسے پکڑنے کے لیے Clang-Tidy اور sanitizers جیسے ٹولز کا استعمال کریں۔