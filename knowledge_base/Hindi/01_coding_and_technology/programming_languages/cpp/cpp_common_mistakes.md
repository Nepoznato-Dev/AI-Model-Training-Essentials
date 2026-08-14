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

# C++ - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ C++ में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है। प्रत्येक प्रविष्टि गलत दृष्टिकोण दिखाती है, बताती है कि यह विफल क्यों होता है, और सही समाधान प्रदान करती है। आधुनिक C++ (C++11/14/17/20) अधिकांश क्लासिक नुकसानों से बचने के लिए उपकरण प्रदान करता है।
---

## 1. तीन/पांच उल्लंघनों का नियम
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

## 2. स्मार्ट पॉइंटर्स के बजाय रॉ`new`/ `delete`
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

## 3. स्लाइसिंग समस्या
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

## 4. पुनरावर्तक अमान्यकरण
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

## 5. लटकते सन्दर्भ
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

## 6.`std::move`का सही ढंग से उपयोग न करना
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

## 7. एंटी-पैटर्न: हेडर में`using namespace std;`का उपयोग करना
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

## 8. हस्ताक्षरित अतिप्रवाह से अपरिभाषित व्यवहार
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

## 9. मूल्य श्रेणियों को न समझना
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

## 10. एंटी-पैटर्न: मैनुअल रिसोर्स मैनेजमेंट (प्री-आरएआईआई)
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

## 11. टेम्प्लेट ब्लोट और लंबा संकलन समय
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

## 12.`[[nodiscard]]`और`[[maybe_unused]]`का उपयोग नहीं करना
```cpp
// ❌ WRONG — ignoring error codes
int result = risky_operation();
// result ignored — potential bug

// ✅ CORRECT — mark functions that shouldn't be ignored
[[nodiscard]] int risky_operation();

// Compiler warns if return value is discarded
```

---

## सारांश
C++ की जटिलता गलतियों के लिए कई अवसर पैदा करती है: पांच का नियम, ऑब्जेक्ट स्लाइसिंग, इटरेटर अमान्यकरण, लटकते संदर्भ, और हस्ताक्षरित अतिप्रवाह से अपरिभाषित व्यवहार। आधुनिक C++ मारक है: कच्चे`new`/`delete`के बजाय स्मार्ट पॉइंटर्स का उपयोग करें, सभी संसाधनों के लिए RAII, कच्चे सरणियों के बजाय`std::vector`और `std::string`, दक्षता के लिए शब्दार्थ को स्थानांतरित करें, और नजरअंदाज किए गए रिटर्न मानों को पकड़ने के लिए`[[nodiscard]]`का उपयोग करें। C++ कोर दिशानिर्देश एक कारण से मौजूद हैं - उनका पालन करें, और जो आप चूक गए हैं उसे पकड़ने के लिए क्लैंग-टिडी और सैनिटाइज़र जैसे टूल का उपयोग करें।