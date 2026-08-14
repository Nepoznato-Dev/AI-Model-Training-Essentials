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
# C++ – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Bibliotheken und Infrastruktur im C++-Ökosystem.
---

## Compiler
| Compiler | Plattform | Notizen |
|----------|----------|-------|
| **GCC (g++)** | Linux/Unix | GNU Compiler Collection, weit verbreitet |
| **Clang++** | Plattformübergreifend | LLVM-basierte, hervorragende Diagnostik |
| **MSVC** | Windows | Microsoft Visual C++-Compiler |
| **Intel oneAPI (icpx)** | Plattformübergreifend | Hochleistung, HPC-Fokus |
| **zig c++** | Plattformübergreifend | Tolle Cross-Compilation |
```bash
g++ -std=c++23 -O2 -Wall -Wextra -o app main.cpp
clang++ -std=c++23 -stdlib=libc++ -o app main.cpp
```

---

## Systeme erstellen
| Werkzeug | Geben Sie | ein Am besten für |
|------|------|----------|
| **CMake** | Plattformübergreifend | Industriestandard, die meisten Projekte |
| **Meson** | Modern | Schnelle, saubere Syntax, Ninja-Backend |
| **Bazel** | Maßstab | Monorepos, Google-Maßstab |
| **Conan + CMake** | Paketbewusst | C++-Paketverwaltung |
| **xmake** | Modern | Lua-basierter, integrierter Paketmanager |
| **Machen** | Klassisch | Einfache Unix-Projekte |
| **Ninja** | Schnell | Low-Level-Build-System |
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

## Paketmanager
| Werkzeug | Geben Sie | ein Notizen |
|------|------|-------|
| **Conan** | Dezentral | Python-basiert, am beliebtesten |
| **vcpkg** | Microsoft | CMake/VcpkgManifest-Integration |
| **Jäger** | CMake-nativ | CMake-gesteuerter Abhängigkeitsmanager |
| **xrepo** | Lua-basiert | Plattformübergreifend, über xmake |
```bash
# Conan 2.x
conan install . --output-folder=build --build=missing
cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

# vcpkg (manifest mode)
# vcpkg.json in project root
vcpkg install
```

---

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **Google-Test (gtest)** | Am beliebtesten ist Google |
| **Google Mock (gmock)** | Spott-Framework |
| **Catch2** | Single-Header, BDD-Stil |
| **doctest** | Leichter Single-Header |
| **Boost.Test** | Boost-basiertes Testen |
| **Google Benchmark** | Mikrobenchmarking |
| **Nanobank** | Leichtes Benchmarking |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **klirrend-ordentlich** | Linter, Modernisierung, fehleranfällige Prüfungen |
| **clang-format** | Codeformatierung |
| **cppcheck** | Statische Analyse |
| **PVS-Studio** | Kommerzielle statische Analyse |
| **Deckung** | Statische Unternehmensanalyse |
| **SonarQube** | Code-Qualitätsplattform |
| **include-what-you-use (IWYU)** | Header-Abhängigkeitsanalyse |
| **cppdep** | Abhängigkeitsanalyse |
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

## Debugging und Analyse
| Werkzeug | Zweck |
|------|---------|
| **GDB** | GNU-Debugger |
| **LLDB** | LLVM-Debugger |
| **Valgrind** | Speicherfehlererkennung |
| **AddressSanitizer (ASan)** | Schneller Speicherfehlerdetektor |
| **UndefinedBehaviorSanitizer (UBSan)** | UB-Erkennung |
| **ThreadSanitizer (TSan)** | Erkennung von Datenrennen |
| **MemorySanitizer (MSan)** | Nicht initialisierter Speicher |
| **LeakSanitizer (LSan)** | Erkennung von Speicherlecks |
| **perf** | Linux-Leistungsprofilierung |
| **Tracy** | Echtzeit-Frame-Profiler |
| **NVIDIA Nsight** | GPU-Profilerstellung |
```bash
# Compile with sanitizers
g++ -fsanitize=address,undefined -g -o app main.cpp
clang++ -fsanitize=thread -g -o app main.cpp
```

---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **STL** | Standardbibliothek (Container, Algorithmen) |
| **Boost** | Umfassende Utility-Bibliothek |
| **fmt** | Moderne Formatierung (Basis für std::format) |
| **nlohmann/json** | JSON-Analyse |
| **spdlog** | Schnelle Protokollierung |
| **Eigen** | Lineare Algebra |
| **OpenCV** | Computer Vision |
| **Qt** | Plattformübergreifendes GUI-Framework |
| **SDL2** | Multimedia/Spiele |
| **OpenGL/Vulkan/DirectX** | Grafik-APIs |
| **gRPC** | RPC-Framework |
| **Protobuf** | Serialisierung |
| **libcurl** | HTTP-Übertragungen |
| **OpenSSL** | Kryptographie, TLS |
| **SQLite** | Eingebettete Datenbank |
| **Poco** | Netzwerk- und Versorgungsbibliothek |
| **ASIO / Boost.Asio** | Asynchrone E/A, Netzwerk |
| **Bereiche (C++20)** | Lazy Evaluation, zusammensetzbare Algorithmen |
---

## Parallelität und Asynchronität
| Bibliothek | Zweck |
|---------|---------|
| **std::thread / std::jthread** | C++11/20-Threading |
| **std::async / std::future** | Aufgabenbasierte Parallelität |
| **std::execution** | Parallele Algorithmen (C++17) |
| **Boost.Asio** | Asynchrones Netzwerk |
| **libuv** | Asynchrone E/A |
| **OpenMP** | Direktivenbasierte Parallelität |
| **TBB** | Intel Threading-Bausteine ​​|
| **std::stop_token** | Kooperative Stornierung (C++20) |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **CLöwe** | Vollständige JetBrains C++ IDE, CMake-Integration |
| **VS-Code + clangd** | Leicht, LSP-basiert |
| **Visual Studio** | Beste Windows C++-IDE |
| **Qt Creator** | Qt-Entwicklung |
| **Neovim + clangd** | Terminalbasiert mit LSP |
| **Eclipse CDT** | Open-Source-C/C++ |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Statische Binärdatei** | `g++ -static`oder musl |
| **Docker** | Mehrstufige Builds |
| **Cross-Kompilierung** | GCC/Clang-übergreifende Toolchains |
| **Conan + CI** | Verpacken und verteilen |
| **vcpkg + CI** | Bereitstellung im Manifestmodus |
| **Eingebettet** | Bare-Metal, RTOS, Cross-Compile |
---

## Zusammenfassung
C++ verfügt über das reichhaltigste und komplexeste Ökosystem. Die Standard-Toolchain ist: **GCC** oder **Clang** für die Kompilierung, **CMake** für Builds, **Conan** oder **vcpkg** für Pakete, **Google Test** oder **Catch2** für Tests, **clang-tidy** für Linting, **GDB** für Debugging und **ASan/UBSan** für Sanitizer. Zu den wichtigsten Bibliotheken gehören **Boost** für Dienstprogramme, **fmt** für die Formatierung, **nlohmann/json** für JSON, **spdlog** für die Protokollierung, **Eigen** für Mathematik und **Qt** für die GUI. Modernes C++ (20/23) mit Konzepten, Bereichen, Coroutinen und Modulen verändert das Ökosystem. Kompilieren Sie immer mit`-Wall -Wextra -Werror`und verwenden Sie Desinfektionsmittel in CI.