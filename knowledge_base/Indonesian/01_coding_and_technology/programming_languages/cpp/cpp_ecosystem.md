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
# C++ — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, perpustakaan, dan infrastruktur penting dalam ekosistem C++.
---

## Kompiler
| Kompiler | Peron | Catatan |
|----------|----------|-------|
| **GCC (g++)** | Linux/Unix | Koleksi Kompiler GNU, banyak digunakan |
| **Dentang++** | Lintas platform | Diagnostik luar biasa berbasis LLVM |
| **MSVC** | jendela | Kompiler Microsoft Visual C++ |
| **Intel oneAPI (icpx)** | Lintas platform | Performa tinggi, fokus HPC |
| **zig c++** | Lintas platform | Kompilasi silang yang hebat |
```bash
g++ -std=c++23 -O2 -Wall -Wextra -o app main.cpp
clang++ -std=c++23 -stdlib=libc++ -o app main.cpp
```

---

## Membangun Sistem
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **CMembuat** | Lintas platform | Standar industri, sebagian besar proyek |
| **Meson** | Modern | Sintaks yang cepat dan bersih, backend Ninja |
| **Bazel** | Skala | Monorepos, skala Google |
| **Conan + CMake** | Sadar paket | Manajemen paket C++ |
| **membuat** | Modern | Manajer paket bawaan berbasis Lua |
| **Buat** | Klasik | Proyek Unix sederhana |
| **Ninja** | Cepat | Sistem pembangunan tingkat rendah |
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

## Manajer Paket
| Alat | Ketik | Catatan |
|------|------|-------|
| **Conan** | Terdesentralisasi | Berbasis Python, paling populer |
| **vcpkg** | Microsoft | Integrasi CMake/VcpkgManifest |
| **Pemburu** | CMake-asli | Manajer ketergantungan berbasis CMake |
| **xrepo** | Berbasis Lua | Lintas platform, melalui xmake |
```bash
# Conan 2.x
conan install . --output-folder=build --build=missing
cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

# vcpkg (manifest mode)
# vcpkg.json in project root
vcpkg install
```

---

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Tes Google (gtest)** | Paling populer, Google |
| **Google Tiruan (gmock)** | Kerangka mengejek |
| **Tangkap2** | Header tunggal, gaya BDD |
| **tes dokter** | Header tunggal yang ringan |
| **Boost.Test** | Pengujian berbasis peningkatan |
| **Tolok Ukur Google** | Benchmarking Mikro |
| **nanobench** | Tolok ukur ringan |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **dentang-rapi** | Linter, modernisasi, pemeriksaan rawan bug |
| **format dentang** | Pemformatan kode |
| **cppperiksa** | Analisis statis |
| **PVS-Studio** | Analisis statis komersial |
| **Penutup** | Analisis statis perusahaan |
| **SonarQube** | Platform kualitas kode |
| **sertakan-apa-yang-Anda-gunakan (IWYU)** | Analisis ketergantungan header |
| **cppdep** | Analisis ketergantungan |
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

## Debugging & Analisis
| Alat | Tujuan |
|------|---------|
| **GDB** | Pendebug GNU |
| **LLDB** | debugger LLVM |
| **Valgrind** | Deteksi kesalahan memori |
| **AlamatSanitizer (ASan)** | Detektor kesalahan memori cepat |
| **BehaviorSanitizer Tidak Terdefinisi (UBSan)** | Deteksi UB |
| **Pembersih Benang (TSan)** | Deteksi perlombaan data |
| **Pembersih Memori (MSan)** | Memori yang tidak diinisialisasi |
| **LeakSanitizer (LSan)** | Deteksi kebocoran memori |
| **kinerja** | Profil kinerja Linux |
| **Tracy** | Profiler bingkai waktu nyata |
| **NVIDIA Nsight** | Pembuatan profil GPU |
```bash
# Compile with sanitizers
g++ -fsanitize=address,undefined -g -o app main.cpp
clang++ -fsanitize=thread -g -o app main.cpp
```

---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **STL** | Pustaka standar (wadah, algoritma) |
| **Peningkatan** | Perpustakaan utilitas yang komprehensif |
| **fmt** | Pemformatan modern (dasar untuk std::format) |
| **nlohmann/json** | Penguraian JSON |
| **spdlog** | Pencatatan cepat |
| **Eigen** | Aljabar linier |
| **OpenCV** | Visi komputer |
| **Qt** | Kerangka kerja GUI lintas platform |
| **SDL2** | Multimedia/permainan |
| **OpenGL/Vulkan/DirectX** | API Grafis |
| **gRPC** | Kerangka RPC |
| **Protobuf** | Serialisasi |
| **libcurl** | Transfer HTTP |
| **OpenSSL** | Kriptografi, TLS |
| **SQLite** | Basis data tertanam |
| **Poco** | Perpustakaan jaringan dan utilitas |
| **ASIO / Boost.Asio** | I/O asinkron, jaringan |
| **Rentang (C++20)** | Evaluasi malas, algoritma yang dapat disusun |
---

## Konkurensi & Asinkron
| Perpustakaan | Tujuan |
|---------|---------|
| **std::utas / std::jthread** | Utas C++11/20 |
| **std::async / std::masa depan** | Paralelisme berbasis tugas |
| **std::eksekusi** | Algoritma paralel (C++17) |
| **Meningkatkan.Asio** | Jaringan asinkron |
| **libuv** | I/O asinkron |
| **BukaMP** | Paralelisme berbasis direktif |
| **TBB** | Blok Penyusun Intel Threading |
| **std::stop_token** | Pembatalan kooperatif (C++20) |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **CLion** | IDE JetBrains C++ lengkap, integrasi CMake |
| **Kode VS + dentang** | Ringan, berbasis LSP |
| **Studio Visual** | IDE Windows C++ Terbaik |
| **Pembuat Qt** | Pengembangan Qt |
| **Neovim + dentang** | Berbasis terminal dengan LSP |
| **Gerhana CDT** | C/C++ sumber terbuka |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Biner statis** | `g++ -static`atau musl |
| **Buruh pelabuhan** | Pembangunan multi-tahap |
| **Kompilasi silang** | Rantai alat lintas GCC/Clang |
| **Conan + CI** | Kemas dan distribusikan |
| **vcpkg + CI** | Penerapan mode manifes |
| **Tertanam** | Bare-metal, RTOS, kompilasi silang |
---

## Ringkasan
C++ memiliki ekosistem terkaya dan paling kompleks. Toolchain standarnya adalah: **GCC** atau **Clang** untuk kompilasi, **CMake** untuk build, **Conan** atau **vcpkg** untuk paket, **Google Test** atau **Catch2** untuk pengujian, **clang-tidy** untuk linting, **GDB** untuk debugging, dan **ASan/UBSan** untuk sanitizer. Pustaka utama mencakup **Boost** untuk utilitas, **fmt** untuk pemformatan, **nlohmann/json** untuk JSON, **spdlog** untuk logging, **Eigen** untuk matematika, dan **Qt** untuk GUI. C++ modern (23/20) dengan konsep, rentang, coroutine, dan modul mengubah ekosistem. Selalu kompilasi dengan`-Wall -Wextra -Werror`dan gunakan pembersih di CI.