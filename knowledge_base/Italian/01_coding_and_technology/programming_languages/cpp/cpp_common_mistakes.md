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

# C++: errori comuni e anti-pattern
Questo documento cataloga gli errori, le trappole e gli anti-pattern più comuni in C++. Ogni voce mostra l'approccio errato, spiega perché fallisce e fornisce la soluzione corretta. Il C++ moderno (C++11/14/17/20) fornisce strumenti per evitare la maggior parte delle trappole classiche.
---

## 1. Regola delle tre/cinque violazioni
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

## 2.`new`/`delete`grezzi invece dei puntatori intelligenti
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

## 3. Problema di slicing
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

## 4. Invalidazione dell'iteratore
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

## 5. Riferimenti pendenti
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

## 6. Non utilizzare`std::move`correttamente
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

## 7. Anti-Pattern: utilizzo di`using namespace std;`nelle intestazioni
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

## 8. Comportamento indefinito dell'overflow firmato
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

## 9. Non comprendere le categorie di valori
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

## 10. Anti-Pattern: gestione manuale delle risorse (pre-RAII)
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

## 11. Template gonfio e tempi di compilazione lunghi
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

## 12. Non utilizzare`[[nodiscard]]`e `[[maybe_unused]]`
```cpp
// ❌ WRONG — ignoring error codes
int result = risky_operation();
// result ignored — potential bug

// ✅ CORRECT — mark functions that shouldn't be ignored
[[nodiscard]] int risky_operation();

// Compiler warns if return value is discarded
```

---

## Riepilogo
La complessità del C++ crea molte opportunità di errori: la regola del cinque, l'affettamento degli oggetti, l'invalidazione degli iteratori, i riferimenti pendenti e il comportamento indefinito derivante dall'overflow con segno. Il C++ moderno è l'antidoto: usa puntatori intelligenti invece di`new`/`delete`grezzi, RAII per tutte le risorse,`std::vector`e`std::string`invece di array grezzi, sposta la semantica per efficienza e`[[nodiscard]]`per catturare i valori restituiti ignorati. Le linee guida di base del C++ esistono per un motivo: seguile e utilizza strumenti come Clang-Tidy e disinfettanti per individuare ciò che ti manca.