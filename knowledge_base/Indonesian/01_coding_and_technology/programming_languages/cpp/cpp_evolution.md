---
# Metadata
title: "C++ — Version History & Evolution"
description: "Comprehensive version history and evolution of C++ from C with Classes to C++26."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# C++ — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Depan | 1983 | "C dengan Kelas" — kelas, warisan |
| C++98 | 1998 | Standar ISO pertama; STL, templat, pengecualian |
| C++03 | 2003 | Perbaikan cacat |
| C++11 | 2011 | **Mayor**: Memindahkan semantik, lambda,`auto`, smart pointer,`nullptr`|
| C++14 | 2014 | Lambda umum, pengembalian `auto`,`std::make_unique`|
| C++17 | 2017 | `std::optional`,`std::variant`,`if constexpr`, binding terstruktur |
| C++20 | 2020 | **Utama**: Konsep, rentang, coroutine, modul,`std::span`, perbandingan tiga arah |
| C++23 | 2024 | `std::expected`,`std::print`,`std::flat_map`, menyimpulkan`this`|
| C++26 | ~2026 | `std::execution`, refleksi (diharapkan), kontrak |
## Tonggak Penting
### Era Pra-Standar (1983–1998)
- **1983**: Bjarne Stroustrup menciptakan "C dengan Kelas" di Bell Labs
- **1985**: Berganti nama menjadi C++; edisi pertama "Bahasa Pemrograman C++"
- **1989**: Templat, pengecualian, namespace diusulkan
- **1990**: STL (Perpustakaan Templat Standar) oleh Alexander Stepanov
- **1991**: Templat distandarisasi; "Manual Referensi C++ Beranotasi"
### C++98 — Landasan (1998)
- Kelas, warisan, fungsi virtual
- Template (fungsi, kelas, spesialisasi)
- STL:`vector`,`map`,`set`,`algorithm`,`iterator`
- Pengecualian (`try/catch/throw`)
- `namespace`, `bool`, `const_cast`,`dynamic_cast`
- Konstruktor `explicit`, anggota `mutable`
- RTTI (`typeid`,`dynamic_cast`)
### C++11 — Renaisans (2011)
- **Pindahkan semantik**: referensi nilai `&&`,`std::move`
- **Petunjuk cerdas**:`unique_ptr`,`shared_ptr`,`weak_ptr`
- **`auto`**: ketik inferensi
- **`nullptr`**: menggantikan`NULL`
- **Lambdas**:`[](int x) { return x * 2; }`
- **Rentang-untuk**:`for (auto& x : container)`
- **`constexpr`**: komputasi waktu kompilasi
- **`static_assert`**: pernyataan waktu kompilasi
- **`using`** : ketik alias (menggantikan`typedef`)
- **Templat variadik**:`template<typename... Args>`
- **`enum class`**: enum yang diketik dengan kuat
- **`override`/`final`**: kontrol fungsi virtual
- **`std::thread`**: threading asli
- **`std::atomic`**: pemrograman bebas kunci
- **`std::function`/`std::bind`**: fungsi kelas satu
### C++17 — Penyempurnaan (2017)
- `std::optional<T>`, `std::variant<T...>`,`std::any`
-`if constexpr`— percabangan waktu kompilasi
- Binding terstruktur:`auto [x, y] = point;`
-`std::filesystem`
-`std::string_view`
- Algoritma paralel:`std::execution::par`
- Namespace bersarang:`namespace A::B::C {}`
-`[[nodiscard]]`, `[[maybe_unused]]`, `[[fallthrough]]`
### C++20 — Bahasa Modern (2020)
- **Konsep**:`template<std::integral T>`— templat terbatas
- **Rentang**:`views::filter`,`views::transform`— saluran pipa lambat
- **Coroutine**:`co_await`,`co_yield`,`co_return`
- **Modul**:`import`/`export`— kompilasi lebih cepat
- **`std::span`**: tidak memiliki tampilan data yang berdekatan
- **Perbandingan tiga arah**:`<=>`(operator pesawat luar angkasa)
- **`std::format`**: Pemformatan gaya Python
- **`consteval`/`constinit`**: penegakan waktu kompilasi
- **Inisialisasi yang ditunjuk**:`Point{.x = 1, .y = 2}`
- **`std::jthread`**: penggabungan otomatis thread dengan token stop
### C++23 — Peningkatan Praktis (2024)
-`std::expected<T, E>`— Penanganan kesalahan yang terinspirasi dari karat
-`std::print`/`std::println`— keluaran yang diformat dengan cepat
-`std::flat_map`,`std::flat_set`
- Menyimpulkan`this`— parameter objek eksplisit
-`std::mdspan`— rentang multidimensi
-`std::generator`— generator sinkron
-`#include <debugging>`— titik henti sementara, pembuangan
## Evolusi Pola Kunci
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

## Standar Proses
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

## Dampak Ekosistem
```
1998: C++ dominates systems, games, finance
2005: Boost library ecosystem grows
2011: Modern C++ makes C++ safer and more expressive
2020: C++20 concepts simplify template code
2025: C++ remains #4 most used language; dominant in games, embedded, HFT, OS kernels
```
