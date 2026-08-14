<!--
---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| K&R C | 1972–78 | Orijinal C (Kernighan ve Ritchie) |
| C89/C90 | 1989/90 | İlk ANSI/ISO standardı |
| C95 | 1995 | Değişiklik 1:`wchar.h`, digraflar |
| C99 | 1999 | `//`yorumları, `inline`, `bool`, VLA'lar, belirlenmiş başlatıcılar |
| C11 | 2011 | Atomikler, iplikler, `_Static_assert`, anonim yapılar/birleşimler |
| C17 | 2018 | Kusur düzeltmeleri (yeni özellik yok) |
| C23 | 2024 | `nullptr`,`typeof`,`constexpr`,`#embed`, nitelikler |
## Önemli Kilometre Taşları
### K&R C (1972–1989)
- **1972**: Dennis Ritchie, Unix için Bell Laboratuvarlarında C'yi yarattı
- **1978**: Kernighan ve Ritchie "C Programlama Dili"ni yayınladı
- Temel özellikler: `struct`, `int`, `char`, işaretçiler, işlevler,`#include`
-`void`yok,`enum`yok,`unsigned`yok,`const`yok
### C89/C90 — Standart (1989)
- İlk ANSI standardı (ANSI X3.159-1989)
- Eklendi:`void`,`enum`,`const`,`volatile`, fonksiyon prototipleri,`signed`
- "Altın çağ" — taşınabilir, yaygın olarak benimsenmiştir
- Hala birçok gömülü sistem için temel
### C99 — Modern C (1999)
-`//`tek satırlık yorumlar
-`inline`işlevleri
-`<stdbool.h>`aracılığıyla`bool`
- Değişken uzunluklu diziler (VLA'lar)
- Belirlenen başlatıcılar:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— döngüdeki bildirimler
-`<stdint.h>`:`int32_t`,`uint64_t`, vb.
-`restrict`anahtar kelimesi
- Değişken makrolar
- Bileşik değişmez değerler
### C11 — Güvenlik ve Eşzamanlılık (2011)
-`<stdatomic.h>`— atomik işlemler
-`<threads.h>`— iş parçacığı desteği
-`_Static_assert`— derleme zamanı iddiaları
- İç içe yapılarda anonim yapılar/birleşimler
-`_Alignof`,`_Alignas`— hizalama kontrolü
- Genel seçimler:`_Generic(x, int: ..., default: ...)`
- Unicode desteği:`<uchar.h>`
- İsteğe bağlı VLA desteği (yerleşik endişeler nedeniyle isteğe bağlı hale getirildi)
### C23 — Rönesans (2024)
-`nullptr`— boş işaretçi sabiti (`NULL` makrosunun yerine geçer)
-`typeof`— tür çıkarımı
-`constexpr`— sabit ifadeler
-`#embed`— ikili verileri derleme zamanında gömün
-`[[attribute]]`sözdizimi (C23 tarzı nitelikler)
- Anahtar kelime olarak`true`/`false`(artık `<stdbool.h>`'ye gerek yok)
-`auto`tipi çıkarım
-`static_assert`(alt çizgi olmadan)
-`alignof`(alt çizgi olmadan)
- Varsayılan`int`dönüşü kaldırıldı
## Standartlar Süreci
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## Uyumluluk Felsefesi
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## Ön İşlemci Gelişimi
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## Tür Sistem Gelişimi
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## Ekosistem Etkisi
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
