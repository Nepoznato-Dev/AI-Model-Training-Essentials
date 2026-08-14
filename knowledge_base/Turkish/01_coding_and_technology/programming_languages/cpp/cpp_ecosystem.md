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
# C++ — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz, C++ ekosistemindeki temel araçları, kitaplıkları ve altyapıyı kapsar.
---

## Derleyiciler
| Derleyici | Platformu | Notlar |
|----------|----------|----------|
| **GCC (g++)** | Linux/Unix | Yaygın olarak kullanılan GNU Derleyici Koleksiyonu |
| **Tang++** | Çapraz platform | LLVM tabanlı, mükemmel teşhis |
| **MSVC** | Windows | Microsoft Visual C++ derleyicisi |
| **Intel oneAPI (icpx)** | Çapraz platform | Yüksek performanslı, HPC odaklı |
| **zig c++** | Çapraz platform | Harika çapraz derleme |
```bash
g++ -std=c++23 -O2 -Wall -Wextra -o app main.cpp
clang++ -std=c++23 -stdlib=libc++ -o app main.cpp
```

---

## Sistem Oluştur
| Araç | Tür | En İyisi |
|------|----------|----------|
| **CMake** | Çapraz platform | Endüstri standardı, çoğu proje |
| **Mezon** | Modern | Hızlı, temiz sözdizimi, Ninja arka ucu |
| **Bazel** | Ölçek | Monorepos, Google ölçeğinde |
| **Conan + CMake** | Paket uyumlu | C++ paket yönetimi |
| **xmake** | Modern | Lua tabanlı, yerleşik paket yöneticisi |
| **Yap** | Klasik | Basit Unix projeleri |
| **Ninja** | Hızlı | Düşük seviyeli yapı sistemi |
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

## Paket Yöneticileri
| Araç | Tür | Notlar |
|------|------|----------|
| **Conan** | Merkezi Olmayan | Python tabanlı, en popüler |
| **vcpkg** | Microsoft | CMake/VcpkgManifest entegrasyonu |
| **Avcı** | CMake-yerel | CMake odaklı bağımlılık yöneticisi |
| **xrepo** | Lua tabanlı | Çapraz platform, xmake aracılığıyla |
```bash
# Conan 2.x
conan install . --output-folder=build --build=missing
cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake

# vcpkg (manifest mode)
# vcpkg.json in project root
vcpkg install
```

---

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **Google Testi (gtest)** | En popüler, Google |
| **Google Mock (gmock)** | Alaycı çerçeve |
| **Yakala2** | Tek başlıklı, BDD tarzı |
| **doktor testi** | Hafif tek başlıklı |
| **Artırma.Test** | Boost tabanlı test |
| **Google Karşılaştırması** | Mikro kıyaslama |
| **nano tezgah** | Hafif kıyaslama |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **tıngırdayan-düzenli** | Linter, modernleştirme, hataya açık kontroller |
| **clang-formatı** | Kod biçimlendirme |
| **cppcheck** | Statik analiz |
| **PVS-Stüdyo** | Ticari statik analiz |
| **Gizlilik** | Kurumsal statik analiz |
| **SonarQube** | Kod kalitesi platformu |
| **ne kullandığınızı dahil edin (IWYU)** | Başlık bağımlılığı analizi |
| **cppdep** | Bağımlılık analizi |
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

## Hata Ayıklama ve Analiz
| Araç | Amaç |
|------|------------|
| **GDB** | GNU hata ayıklayıcı |
| **LLDB** | LLVM hata ayıklayıcı |
| **Valgrind** | Bellek hatası tespiti |
| **AdresSanitizer (ASan)** | Hızlı bellek hatası dedektörü |
| **UnDefinitionBehaviorSanitizer (UBSan)** | UB tespiti |
| **ThreadSanitizer (TSan)** | Veri yarışı tespiti |
| **Bellek Temizleyici (MSan)** | Başlatılmamış bellek |
| **Sızıntı Temizleyici (LSan)** | Bellek sızıntısı tespiti |
| **mükemmel** | Linux performans profili oluşturma |
| **Tracy** | Gerçek zamanlı çerçeve profili oluşturucu |
| **NVIDIA Nsight** | GPU profili oluşturma |
```bash
# Compile with sanitizers
g++ -fsanitize=address,undefined -g -o app main.cpp
clang++ -fsanitize=thread -g -o app main.cpp
```

---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **STL** | Standart kütüphane (kapsayıcılar, algoritmalar) |
| **Artırma** | Kapsamlı yardımcı program kitaplığı |
| **fmt** | Modern biçimlendirme (std::format'ın temeli) |
| **nlohmann/json** | JSON ayrıştırma |
| **spdlog** | Hızlı kayıt |
| **Eigen** | Doğrusal cebir |
| **AçıkCV** | Bilgisayarlı görme |
| **Qt** | Platformlar arası GUI çerçevesi |
| **SDL2** | Multimedya/oyunlar |
| **OpenGL/Vulkan/DirectX** | Grafik API'leri |
| **gRPC** | RPC çerçevesi |
| **Protobuf** | Serileştirme |
| **libcurl** | HTTP aktarımları |
| **AçıkSSL** | Kriptografi, TLS |
| **SQLite** | Gömülü veritabanı |
| **Poco** | Ağ ve yardımcı program kitaplığı |
| **ASIO / Boost.Asio** | Zaman uyumsuz G/Ç, ağ iletişimi |
| **Aralıklar (C++20)** | Tembel değerlendirme, şekillendirilebilir algoritmalar |
---

## Eşzamanlılık ve Eşzamansız
| Kütüphane | Amaç |
|-----------|-----------|
| **std::thread / std::jthread** | C++11/20 iş parçacığı |
| **std::async / std::future** | Görev tabanlı paralellik |
| **std::yürütme** | Paralel algoritmalar (C++17) |
| **Boost.Asio** | Eşzamansız ağ iletişimi |
| **libuv** | Zaman uyumsuz G/Ç |
| **OpenMP** | Yönerge tabanlı paralellik |
| **TBB** | Intel İş Parçacığı Oluşturma Yapı Taşları |
| **std::stop_token** | Kooperatif iptali (C++20) |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **CLion** | Tam JetBrains C++ IDE, CMake entegrasyonu |
| **VS Kodu + clangd** | Hafif, LSP tabanlı |
| **Görsel Stüdyo** | En İyi Windows C++ IDE'si |
| **Qt Oluşturucu** | Qt geliştirme |
| **Neovim + clangd** | LSP ile terminal tabanlı |
| **Eclipse CDT** | Açık kaynak C/C++ |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Statik ikili** | `g++ -static`veya musl |
| **Docker** | Çok aşamalı yapılar |
| **Çapraz derleme** | GCC/Clang çapraz takım zincirleri |
| **Conan + CI** | Paketleyin ve dağıtın |
| **vcpkg + CI** | Bildirim modu dağıtımı |
| **Gömülü** | Çıplak metal, RTOS, çapraz derleme |
---

## Özet
C++ en zengin ve en karmaşık ekosisteme sahiptir. Standart araç zinciri şöyledir: derleme için **GCC** veya **Clang**, derlemeler için **CMake**, paketler için **Conan** veya **vcpkg**, test için **Google Test** veya **Catch2**, linting için **clang-tidy**, hata ayıklama için **GDB** ve temizleyiciler için **ASan/UBSan**. Anahtar kitaplıklar arasında yardımcı programlar için **Boost**, biçimlendirme için **fmt**, JSON için **nlohmann/json**, günlük kaydı için **spdlog**, matematik için **Eigen** ve GUI için **Qt** yer alır. Kavramlar, aralıklar, eşyordamlar ve modüllerle modern C++ (20/23) ekosistemi dönüştürüyor. Her zaman`-Wall -Wextra -Werror`ile derleyin ve CI'da temizleyiciler kullanın.