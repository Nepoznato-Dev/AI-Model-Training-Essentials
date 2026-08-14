<!--
---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ada, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Ada — Sürüm Geçmişi ve Gelişimi
## Zaman Çizelgesi
| Sürüm | Yıl | Anahtar Tema |
|-----------|----------|-----------|
| Ada 83 | 1983 | **İlk standart** (MIL-STD-1815A) — Adını Ada Lovelace'den almıştır |
| Ada 87 | 1987 | Küçük revizyon (hassasiyet, erişilebilirlik kuralları) |
| Ada 95 | 1995 | **Ana**: OOP (etiketli türler), korunan nesneler, görevlendirme iyileştirmeleri |
| Ada 2005 | 2005 | **Arayüzler**, anonim erişim türleri,`for`/`while`döngü iyileştirmeleri |
| Ada 2012 | 2012 | **Görünüm odaklı programlama**, sözleşmeler (ön/son koşullar),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, paralel yapılar, gerçek zamanlı iyileştirmeler |
## Önemli Kilometre Taşları
### Ada 83 — Doğum (1983)
- **1983**: ABD Savunma Bakanlığı, gömülü sistemler için tek bir dilin kullanılmasını zorunlu kıldı
- Jean Ichbiah, CII Honeywell Bull'un (Fransa) tasarımına liderlik ediyor
- Adını ilk bilgisayar programcısı olan Ada Lovelace'den almıştır.
- Anahtar özellikler: güçlü yazma, paketler, görevler (eşzamanlılık), jenerikler, istisnalar
- **Hedef**: Güvenlik açısından kritik sistemler — havacılık, savunma, uzay
### Ada 95 — Nesneye Dayalı Ada (1995)
- **İlk ISO standartlı OO dili** (Java standartlaştırılmadan önce)
- Etiketli türler (sınıflar), sınıf çapında türler, dinamik dağıtım
- Korunan nesneler (güvenli eşzamanlı veri erişimi)
- Alt paketler (hiyerarşik kütüphane)
- Pragma tabanlı yapılandırma
### Ada 2005 — İyileştirmeler (2005)
- Arayüzler (çoklu arayüz kalıtımı)
- Anonim erişim türleri (basitleştirilmiş işaretçiler)
-`for`döngü iyileştirmeleri
- Konteyner kütüphaneleri (çift bağlantılı listeler, vektörler, haritalar)
- Genişletilmiş`return`beyanı
### Ada 2012 — Sözleşmeler ve Yönler (2012)
- **Görünüm odaklı programlama**: Bildirimlere eklenen`aspect`maddeleri
- **Sözleşmeler**:`Pre`,`Post`,`Type_Invariant`— yerleşik resmi doğrulama
- Yineleyici desteği (`for X of Container loop`)
-`overriding` göstergesi
- İfade işlevleri: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Paralel ve Hayalet (2022)
- **`with ghost`**: Doğrulama için hayalet kod (üretimde derlenmiştir)
- **Paralel yapılar**:`parallel`döngüleri,`parallel`blokları
- Gerçek zamanlı iyileştirmeler
- Konteyner iyileştirmeleri
-`Iterator`görünüm iyileştirmeleri
## Söz Dizimi Gelişimi
```ada
-- Ada 83: Package-based design
package Stack is
   procedure Push(Item : in Integer);
   function Pop return Integer;
   Stack_Empty : exception;
end Stack;

package body Stack is
   Max : constant := 100;
   Data : array(1..Max) of Integer;
   Top : Integer range 0..Max := 0;

   procedure Push(Item : in Integer) is
   begin
      Top := Top + 1;
      Data(Top) := Item;
   end Push;

   function Pop return Integer is
      Result : Integer;
   begin
      if Top = 0 then raise Stack_Empty; end if;
      Result := Data(Top);
      Top := Top - 1;
      return Result;
   end Pop;
end Stack;

-- Ada 95: Object-oriented
type Shape is tagged record
   X, Y : Float;
end record;

function Area(S : Shape) return Float is
begin
   return 0.0;
end Area;

type Circle is new Shape with record
   Radius : Float;
end record;

function Area(C : Circle) return Float is
begin
   return 3.14159 * C.Radius ** 2;
end Area;

-- Ada 2012: Contracts and aspects
type Temperature is new Float
   with Dynamic_Predicate => Temperature >= -273.15;

procedure Set_Temp(T : in out Temperature)
   with Pre  => T >= -273.15,
        Post => T'Old < T;  -- temperature must increase

-- Expression functions (Ada 2012)
function Double(X : Integer) return Integer is (X * 2);

-- Ada 2022: Parallel constructs
parallel
   for I in Data'Range loop
      Data(I) := Compute(I);
   end loop;

-- Ada 2022: Ghost code for verification
procedure Process(X : in out Integer)
   with Ghost => True,
        Pre   => X > 0,
        Post  => X > X'Old;
```

## Özellik Gelişimi
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Temel Tasarım İlkeleri
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Ekosistem Büyümesi
```
1983: Ada 83 — DoD mandate, defense/aviation adoption
1987: Ada 87 — minor fixes
1995: Ada 95 — OOP, ISO standard
1995: GNAT (GNU NYU Ada Translator) — open source compiler
2005: Ada 2005 — interfaces, containers
2012: Ada 2012 — contracts, aspects
2015: SPARK 2014 — formal verification for Ada
2022: Ada 2022 — parallel, ghost code
2025: Ada used in: aviation (DO-178C), space (ESA), rail, defense
       Compilers: GNAT (open source), ObjectAda, AdaCore tools
       SPARK subset used for formal verification of critical code
```
