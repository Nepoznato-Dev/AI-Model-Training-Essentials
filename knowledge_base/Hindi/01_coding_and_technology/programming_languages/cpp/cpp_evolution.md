---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [cpp, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# C++ - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| सीफ्रंट | 1983 | "सी कक्षाओं के साथ" - कक्षाएं, विरासत |
| सी++98 | 1998 | पहला आईएसओ मानक; एसटीएल, टेम्प्लेट, अपवाद |
| सी++03 | 2003 | दोष सुधार |
| सी++11 | 2011 | **प्रमुख**: मूव सिमेंटिक्स, लैम्ब्डा, `auto`, स्मार्ट पॉइंटर्स,`nullptr`|
| सी++14 | 2014 | जेनेरिक लैम्ब्डा,`auto`रिटर्न,`std::make_unique`|
| सी++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, संरचित बाइंडिंग |
| सी++20 | 2020 | **प्रमुख**: अवधारणाएं, श्रेणियां, कोरआउटाइन, मॉड्यूल, `std::span`, तीन-तरफा तुलना |
| सी++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`,`this`|
| सी++26 | ~2026 | `std::execution`, प्रतिबिंब (अपेक्षित), अनुबंध |
## प्रमुख मील के पत्थर
### पूर्व-मानक युग (1983-1998)
- **1983**: बर्जने स्ट्रॉस्ट्रुप ने बेल लैब्स में "सी विद क्लासेस" बनाया
- **1985**: नाम बदला गया C++; "द C++ प्रोग्रामिंग लैंग्वेज" का पहला संस्करण
- **1989**: टेम्प्लेट, अपवाद, नामस्थान प्रस्तावित
- **1990**: अलेक्जेंडर स्टेपानोव द्वारा एसटीएल (स्टैंडर्ड टेम्प्लेट लाइब्रेरी)।
- **1991**: टेम्पलेट मानकीकृत; "एनोटेटेड सी++ संदर्भ मैनुअल"
### सी++98 - द फाउंडेशन (1998)
- कक्षाएं, विरासत, आभासी कार्य
- टेम्पलेट्स (कार्य, कक्षाएं, विशेषज्ञता)
- एसटीएल: `vector`, `map`, `set`, `algorithm`,`iterator`
- अपवाद (`try/catch/throw`)
-`namespace`,`bool`,`const_cast`,`dynamic_cast`
-`explicit`कंस्ट्रक्टर,`mutable`सदस्य
- आरटीटीआई (`typeid`, `dynamic_cast`)
### सी++11 - द रेनेसां (2011)
- **शब्दार्थ ले जाएँ**:`&&`प्रतिमूल्य संदर्भ,`std::move`
- **स्मार्ट पॉइंटर्स**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: प्रकार का अनुमान
- **`nullptr`**:`NULL`की जगह लेता है 
- **लैम्बडास**:`[](int x) { return x * 2; }`
- **रेंज-फॉर**:`for (auto& x : container)`
- **`constexpr`**: संकलन-समय गणना
- **`static_assert`**: संकलन-समय दावे
- **`using`**: उपनाम टाइप करें (`typedef` की जगह)
- **वेरिएडिक टेम्प्लेट**:`template<typename... Args>`
- **`enum class`**: दृढ़ता से टाइप की गई एनम
- **`override`/`final`**: वर्चुअल फ़ंक्शन नियंत्रण
- **`std::thread`**: देशी थ्रेडिंग
- **`std::atomic`**: लॉक-फ्री प्रोग्रामिंग
- **`std::function`/`std::bind`**: प्रथम श्रेणी के कार्य
### सी++17 — शोधन (2017)
-`std::optional<T>`,`std::variant<T...>`,`std::any`
-`if constexpr`- संकलन-समय शाखाकरण
- संरचित बाइंडिंग:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- समानांतर एल्गोरिदम:`std::execution::par`
- नेस्टेड नेमस्पेस:`namespace A::B::C {}`
-`[[nodiscard]]`,`[[maybe_unused]]`, `[[fallthrough]]`
### C++20 - आधुनिक भाषा (2020)
- **अवधारणाएँ**:`template<std::integral T>`- प्रतिबंधित टेम्पलेट्स
- **श्रेणियाँ**:`views::filter`,`views::transform`- आलसी पाइपलाइन
- **कोरआउट्स**:`co_await`,`co_yield`,`co_return`
- **मॉड्यूल**:`import`/`export`— तेज़ संकलन
- **`std::span`**: सन्निहित डेटा का गैर-स्वामित्व वाला दृश्य
- **तीन-तरफ़ा तुलना**:`<=>`(अंतरिक्ष यान ऑपरेटर)
- **`std::format`**: पायथन-शैली स्वरूपण
- **`consteval`/`constinit`**: संकलन-समय प्रवर्तन
- **नामित इनिशियलाइज़र**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: स्टॉप टोकन के साथ ऑटो-ज्वाइनिंग थ्रेड
### C++23 — व्यावहारिक सुधार (2024)
-`std::expected<T, E>`- जंग-प्रेरित त्रुटि प्रबंधन
-`std::print`/`std::println`- तेज़ स्वरूपित आउटपुट
-`std::flat_map`,`std::flat_set`
-`this`घटाना - स्पष्ट ऑब्जेक्ट पैरामीटर
-`std::mdspan`- बहुआयामी विस्तार
-`std::generator`- तुल्यकालिक जनरेटर
-`#include <debugging>`- ब्रेकप्वाइंट, डंप
## प्रमुख पैटर्न का विकास
```
Memory Management:
  1998: Raw pointers, manual new/delete
  2011: Smart pointers (unique_ptr, shared_ptr)
  2020: std::span, views (zero-copy abstractions)
  2023: std::expected (error without exceptions)

Error Handling:
  1998: Exceptions (try/catch)
  2011: noexcept, error codes
  2023: std::expected (Rust-inspired)
  2026: Contracts (expected)

Concurrency:
  1998: None (OS threads)
  2011: std::thread, std::mutex, std::atomic
  2017: Parallel algorithms
  2020: Coroutines, std::jthread

Abstraction:
  1998: Templates (unconstrained)
  2011: Move semantics, perfect forwarding
  2020: Concepts (constrained templates)
```

## मानक प्रक्रिया
```
1998: C++98 (ISO/IEC 14882:1998)
2003: C++03 (defect fixes)
2011: C++11 — "modern C++" begins
2014: C++14 — incremental
2017: C++17 — incremental
2020: C++20 — another revolution
2024: C++23 — practical improvements
2026: C++26 — reflection, contracts (expected)

3-year release cycle since C++11
```

## पारिस्थितिकी तंत्र पर प्रभाव
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
