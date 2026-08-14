<!--
---
# Metadata
title: "C++ — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the C++ ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [cpp, ecosystem, tooling, compilers, build-systems, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "18 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C++ — ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ C++ ماحولیاتی نظام میں ضروری ٹولز، لائبریریوں اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## مرتب کرنے والے
| مرتب کرنے والا | پلیٹ فارم | نوٹس |
|------------|---------|-------|
| **GCC (g++)** | لینکس/یونکس | GNU کمپائلر مجموعہ، وسیع پیمانے پر استعمال کیا جاتا ہے |
| **کلنگ++** | کراس پلیٹ فارم | LLVM پر مبنی، بہترین تشخیص |
| **MSVC** | ونڈوز | مائیکروسافٹ بصری C++ مرتب کرنے والا |
| **Intel oneAPI (icpx)** | کراس پلیٹ فارم | اعلی کارکردگی، HPC فوکس |
| **zig c++** | کراس پلیٹ فارم | عظیم کراس تالیف |
```bash
g++ -std=c++23 -O2 -Wall -Wextra -o app main.cpp
clang++ -std=c++23 -stdlib=libc++ -o app main.cpp
```

---

## سسٹمز بنائیں
| ٹول | قسم | کے لیے بہترین |
|------|------|---------|
| **CMake** | کراس پلیٹ فارم | صنعت کے معیار، سب سے زیادہ منصوبوں |
| **میسن** | جدید | تیز، صاف نحو، ننجا پسدید |
| **بیزل** | پیمانہ | Monorepos, Google-scale |
| **کانن + سی میک** | پیکیج سے آگاہ | C++ پیکیج مینجمنٹ |
| **xmake** | جدید | Lua پر مبنی، بلٹ ان پیکیج مینیجر |
| **بناؤ** | کلاسیکی | سادہ یونکس پروجیکٹس |
| **ننجا** | تیز | کم سطح کی تعمیر کا نظام |
```cmake
# CMakeLists.txt example
cmake_minimum_required(VERSION 3.24)
project(myapp LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(myapp src/main.cpp)
target_compile_features(myapp PRIVATE cxx_std_23)

# Find packages
find_package(fmt REQUIRED)
target_link_libraries(myapp PRIVATE fmt::fmt)
```

---

## پیکیج مینیجرز
| ٹول | قسم | نوٹس |
|------|------|------|
| **کانن** | وکندریقرت | ازگر پر مبنی، سب سے زیادہ مقبول |
| **vcpkg** | مائیکروسافٹ | CMake/VcpkgManifest انضمام |
| ** ہنٹر** | CMake-آبائی | CMake پر مبنی انحصار مینیجر |
| **xrepo** | Lua کی بنیاد پر | کراس پلیٹ فارم، xmake کے ذریعے |
```bash
# Conan 2.x
conan install . --output-folder=build --build=missing
cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

# vcpkg (manifest mode)
# vcpkg.json in project root
vcpkg install
```

---

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **گوگل ٹیسٹ (gtest)** | سب سے زیادہ مقبول، گوگل |
| **گوگل موک (gmock)** | طنزیہ فریم ورک |
| **کیچ2** | سنگل ہیڈر، BDD طرز |
| **ڈاکٹسٹ** | ہلکا پھلکا سنگل ہیڈر |
| **بوسٹ۔ٹیسٹ** | بوسٹ پر مبنی ٹیسٹنگ |
| **گوگل بینچ مارک** | مائیکرو بینچ مارکنگ |
| **نینو بینچ** | ہلکا پھلکا بینچ مارکنگ |
```cpp
// Catch2 example
#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>

TEST_CASE("vector operations") {
    std::vector<int> v = {1, 2, 3};
    REQUIRE(v.size() == 3);
    REQUIRE(v[0] == 1);
    SECTION("push_back") {
        v.push_back(4);
        REQUIRE(v.size() == 4);
    }
}
```

---

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **بنانا صاف** | لنٹر، ماڈرنائز، بگپرون چیکس |
| **کلنگ فارمیٹ** | کوڈ فارمیٹنگ |
| **سی پی پی چیک** | جامد تجزیہ |
| **PVS-Studio** | تجارتی جامد تجزیہ |
| **کوریت** | انٹرپرائز جامد تجزیہ |
| **سونار کیوب** | کوڈ کوالٹی پلیٹ فارم |
| **اس میں شامل ہے کہ آپ کیا استعمال کرتے ہیں (IWYU)** | ہیڈر انحصار تجزیہ |
| **cppdep** | انحصار تجزیہ |
```yaml
# .clang-tidy example
Checks: >
  -*,
  bugprone-*,
  modernize-*,
  performance-*,
  readability-*,
  -modernize-use-trailing-return-type
```

---

## ڈیبگنگ اور تجزیہ
| ٹول | مقصد |
|------|---------|
| **GDB** | GNU ڈیبگر |
| **LLDB** | LLVM ڈیبگر |
| **والگرینڈ** | میموری کی خرابی کا پتہ لگانا |
| **ایڈریس سینیٹائزر (آسن)** | تیز رفتار میموری کی خرابی کا پتہ لگانے والا |
| **غیر متعینہ سلوک سینیٹائزر (UBSan)** | UB کا پتہ لگانا |
| **تھریڈ سینیٹائزر (TSan)** | ڈیٹا ریس کا پتہ لگانا |
| **میموری سینیٹائزر (MSan)** | غیر شروع شدہ میموری |
| **لیک سینیٹائزر (LSan)** | میموری لیک کا پتہ لگانا |
| **perf** | لینکس کی کارکردگی کی پروفائلنگ |
| **ٹریسی** | ریئل ٹائم فریم پروفائلر |
| **NVIDIA Nsight** | GPU پروفائلنگ |
```bash
# Compile with sanitizers
g++ -fsanitize=address,undefined -g -o app main.cpp
clang++ -fsanitize=thread -g -o app main.cpp
```

---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **STL** | معیاری لائبریری (کنٹینرز، الگورتھم) |
| **بوسٹ** | جامع یوٹیلیٹی لائبریری |
| **fmt** | جدید فارمیٹنگ (std::format کی بنیاد) |
| **nlohmann/json** | JSON پارسنگ |
| **spdlog** | تیز لاگنگ |
| **ایگن** | لکیری الجبرا |
| **اوپن سی وی** | کمپیوٹر وژن |
| **Qt** | کراس پلیٹ فارم GUI فریم ورک |
| **SDL2** | ملٹی میڈیا/گیمز |
| **OpenGL/Vulkan/DirectX** | گرافکس APIs |
| **gRPC** | RPC فریم ورک |
| **پروٹوبف** | سیریلائزیشن |
| **libcurl** | HTTP منتقلی |
| **اوپن ایس ایس ایل** | خفیہ نگاری، TLS |
| **SQLite** | ایمبیڈڈ ڈیٹا بیس |
| **پوکو** | نیٹ ورک اور یوٹیلیٹی لائبریری |
| **ASIO / Boost.Asio** | Async I/O، نیٹ ورکنگ |
| **رینجز (C++20)** | سست تشخیص، کمپوز ایبل الگورتھم |
---

## ہم آہنگی اور اسینک
| لائبریری | مقصد |
|---------|---------|
| **std::thread / std::jthread** | C++ 11/20 تھریڈنگ |
| **std::async / std::future** | ٹاسک پر مبنی متوازی |
| **std::Execution** | متوازی الگورتھم (C++17) |
| **Boost.Asio** | Async نیٹ ورکنگ |
| **libuv** | Async I/O |
| **اوپن ایم پی** | ہدایت پر مبنی متوازی |
| **TBB** | انٹیل تھریڈنگ بلڈنگ بلاکس |
| **std::stop_token** | کوآپریٹو منسوخی (C++20) |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **کلیون** | مکمل JetBrains C++ IDE، CMake انضمام |
| **VS کوڈ + clangd** | ہلکا پھلکا، LSP پر مبنی |
| **بصری اسٹوڈیو** | بہترین ونڈوز C++ IDE |
| **Qt خالق** | Qt ترقی |
| **Neovim + clangd** | LSP کے ساتھ ٹرمینل پر مبنی |
| **گرہن CDT** | اوپن سورس C/C++ |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **جامد بائنری** | `g++ -static`یا musl |
| **ڈوکر** | ملٹی اسٹیج بناتا ہے |
| **کراس کمپائل** | GCC/Clang کراس ٹول چینز |
| **کانن + CI** | پیکیج اور تقسیم |
| **vcpkg + CI** | مینی فیسٹ موڈ کی تعیناتی |
| **ایمبیڈڈ** | ننگی دھات، RTOS، کراس کمپائل |
---

## خلاصہ
C++ میں سب سے امیر اور پیچیدہ ماحولیاتی نظام ہے۔ معیاری ٹول چین یہ ہے: تالیف کے لیے **GCC** یا **Clang**، **Cmake** تعمیرات کے لیے، **Conan** یا **vcpkg** پیکجز کے لیے، **گوگل ٹیسٹ** یا **Catch2** ٹیسٹنگ کے لیے، **کلنگ ٹائیڈی** لِنٹنگ کے لیے، **GDB** ڈیبگنگ کے لیے، اور ** izannit** کے لیے UBS. کلیدی لائبریریوں میں یوٹیلیٹیز کے لیے **بوسٹ**، فارمیٹنگ کے لیے **fmt**، JSON کے لیے **nlohmann/json**، لاگنگ کے لیے **spdlog**، ریاضی کے لیے **Eigen**، اور GUI کے لیے **Qt** شامل ہیں۔ جدید C++ (20/23) تصورات، حدود، کوروٹائنز اور ماڈیولز کے ساتھ ماحولیاتی نظام کو تبدیل کر رہا ہے۔ ہمیشہ`-Wall -Wextra -Werror`کے ساتھ مرتب کریں اور CI میں سینیٹائزر استعمال کریں۔