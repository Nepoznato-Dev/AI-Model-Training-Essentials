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
# C++ - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، کتابخانه ها و زیرساخت های ضروری در اکوسیستم C++ را پوشش می دهد.
---

## کامپایلرها
| کامپایلر | پلت فرم | یادداشت ها |
|----------|----------|-------|
| **GCC (g++)** | لینوکس/یونیکس | مجموعه کامپایلر گنو، پرکاربرد |
| **کلنگ++** | کراس پلتفرم | مبتنی بر LLVM، تشخیص عالی |
| **MSVC** | ویندوز | کامپایلر Microsoft Visual C++ |
| **Intel oneAPI (icpx)** | کراس پلتفرم | کارایی بالا، فوکوس HPC |
| **zig c++** | کراس پلتفرم | تلفیقی عالی |
```bash
g++ -std=c++23 -O2 -Wall -Wextra -o app main.cpp
clang++ -std=c++23 -stdlib=libc++ -o app main.cpp
```

---

## ساخت سیستم
| ابزار | نوع | بهترین برای |
|------|------|----------|
| **CMake** | کراس پلتفرم | استاندارد صنعت، اکثر پروژه ها |
| **مزون** | مدرن | نحو سریع و تمیز، باطن نینجا |
| **بازل** | مقیاس | Monorepos، Google-scale |
| **Conan + CMake** | پکیج آگاه | مدیریت بسته C++ |
| **xmake** | مدرن | مبتنی بر Lua، مدیر بسته داخلی |
| **ساخت ** | کلاسیک | پروژه های ساده یونیکس |
| **نینجا** | سریع | سیستم ساخت سطح پایین |
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

## مدیران بسته
| ابزار | نوع | یادداشت ها |
|------|------|-------|
| **کونان** | غیر متمرکز | مبتنی بر پایتون، محبوب ترین |
| **vcpkg** | مایکروسافت | ادغام CMake/VcpkgManifest |
| **شکارچی** | CMake-native | مدیر وابستگی مبتنی بر CMake |
| **xrepo** | مبتنی بر Lua | کراس پلتفرم، از طریق xmake |
```bash
# Conan 2.x
conan install . --output-folder=build --build=missing
cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

# vcpkg (manifest mode)
# vcpkg.json in project root
vcpkg install
```

---

## تست
| چارچوب | هدف |
|-----------|---------|
| **تست گوگل (gtest)** | محبوب ترین، گوگل |
| **Google Mock (gmock)** | چارچوب تمسخر آمیز |
| **Catch2** | تک سر، به سبک BDD |
| **دکتر** | تک سر سبک |
| **Boost.Test** | تست مبتنی بر تقویت |
| **معیار گوگل** | Microbenchmarking |
| **نانو میز** | معیار سبک وزن |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **کلنگ و مرتب** | Linter، مدرنیزاسیون، بررسی های bugprone |
| **فرمت cang** | قالب بندی کد |
| **cppcheck** | تجزیه و تحلیل استاتیک |
| **PVS-Studio** | تحلیل استاتیک تجاری |
| **پوشش** | تجزیه و تحلیل استاتیک سازمانی |
| **SonarQube** | پلت فرم کیفیت کد |
| **شامل-چه استفاده می کنید (IWYU)** | تحلیل وابستگی سرصفحه |
| **cppdep** | تحلیل وابستگی |
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

## اشکال زدایی و تجزیه و تحلیل
| ابزار | هدف |
|------|---------|
| **GDB** | دیباگر گنو |
| **LLDB** | دیباگر LLVM |
| **والگریند** | تشخیص خطای حافظه |
| **AddressSanitizer (ASan)** | تشخیص خطای حافظه سریع |
| **DefinedBehaviorSanitizer (UBSan)** | تشخیص UB |
| **ThreadSanitizer (TSan)** | تشخیص نژاد داده |
| **MemorySanitizer (MSan)** | حافظه بدون مقدار اولیه |
| **LeakSanitizer (LSan)** | تشخیص نشت حافظه |
| **پرف** | پروفایل عملکرد لینوکس |
| **تریسی** | پروفایلر فریم بلادرنگ |
| **NVIDIA Nsight** | پروفایل GPU |
```bash
# Compile with sanitizers
g++ -fsanitize=address,undefined -g -o app main.cpp
clang++ -fsanitize=thread -g -o app main.cpp
```

---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **STL** | کتابخانه استاندارد (ظروف، الگوریتم ها) |
| **تقویت ** | کتابخانه ابزار جامع |
| **fmt** | قالب بندی مدرن (مبنای std::format) |
| **nlohmann/json** | تجزیه JSON |
| **spdlog** | ثبت سریع |
| **ویجن** | جبر خطی |
| **OpenCV** | بینایی کامپیوتر |
| **Qt** | چارچوب رابط کاربری گرافیکی کراس پلتفرم |
| **SDL2** | چند رسانه ای/بازی |
| **OpenGL/Vulkan/DirectX** | API های گرافیکی |
| **gRPC** | چارچوب RPC |
| **پروتوبوف** | سریال سازی |
| **libcurl** | انتقال HTTP |
| **OpenSSL** | رمزنگاری، TLS |
| **SQLite** | پایگاه داده تعبیه شده |
| **پوکو** | کتابخانه شبکه و ابزار |
| **ASIO / Boost.Asio** | Async I/O، شبکه |
| **محدوده (C++20)** | ارزیابی تنبل، الگوریتم های ترکیبی |
---

## همزمانی و ناهمگام
| کتابخانه | هدف |
|---------|---------|
| **std::thread / std::jthread** | C++11/20 threading |
| **std::async / std::future** | توازی مبتنی بر وظیفه |
| **std::execution** | الگوریتم های موازی (C++17) |
| **Boost.Asio** | شبکه Async |
| **لیبوو** | ورودی/خروجی غیرهمگام |
| **OpenMP** | موازی سازی مبتنی بر دستورالعمل |
| **TBB** | بلوک های ساختمان اینتل Threading |
| **std::stop_token** | لغو تعاونی (C++20) |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **CLion** | Full JetBrains C++ IDE، CMake ادغام |
| **VS Code + clangd** | سبک وزن مبتنی بر LSP |
| **ویژوال استودیو** | بهترین Windows C++ IDE |
| **Qt Creator** | توسعه Qt |
| **Neovim + clangd** | مبتنی بر ترمینال با LSP |
| **Eclipse CDT** | متن باز C/C++ |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **باینری استاتیک** | `g++ -static`یا musl |
| **داکر** | ساخت های چند مرحله ای |
| **تقاطع کامپایل** | زنجیره ابزار متقابل GCC/Clang |
| **Conan + CI** | بسته بندی و توزیع |
| **vcpkg + CI** | استقرار حالت مانیفست |
| **جاسازی شده** | بره متال، RTOS، متقابل کامپایل |
---

## خلاصه
C++ غنی ترین و پیچیده ترین اکوسیستم را دارد. زنجیره ابزار استاندارد عبارتند از: **GCC** یا **Clang** برای کامپایل، **CMake** برای ساخت‌ها، **Conan** یا **vcpkg** برای بسته‌ها، **Google Test** یا **Catch2** برای آزمایش، **clang-tidy** برای linting، **GDB** برای اشکال زدایی، **GDB**. کتابخانه های کلیدی شامل **Boost** برای ابزارهای کاربردی، **fmt** برای قالب بندی، **nlohmann/json** برای JSON، **spdlog** برای ورود به سیستم، **Eigen** برای ریاضی و **Qt** برای رابط کاربری گرافیکی. C++ مدرن (20/23) با مفاهیم، ​​محدوده‌ها، روتین‌ها و ماژول‌ها در حال تغییر اکوسیستم است. همیشه با`-Wall -Wextra -Werror`کامپایل کنید و از ضدعفونی کننده ها در CI استفاده کنید.