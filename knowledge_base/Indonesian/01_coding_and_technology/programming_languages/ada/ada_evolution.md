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
# Ada — Riwayat Versi & Evolusi
## Garis Waktu
| Versi | Tahun | Tema Utama |
|---------|------|-----------|
| Ada 83 | 1983 | **Standar pertama** (MIL-STD-1815A) — dinamai Ada Lovelace |
| Ada 87 | 1987 | Revisi kecil (presisi, aturan aksesibilitas) |
| Ada 95 | 1995 | **Utama**: OOP (tipe yang diberi tag), objek yang dilindungi, peningkatan tugas |
| Ada 2005 | 2005 | **Antarmuka**, jenis akses anonim, penyempurnaan loop`for`/`while`|
| Ada 2012 | 2012 | **Pemrograman berorientasi aspek**, kontrak (pra/pascakondisi),`iterator`|
| Ada 2022 | 2022 | **`with ghost`**, konstruksi paralel, peningkatan waktu nyata |
## Tonggak Penting
### Ada 83 — Kelahiran (1983)
- **1983**: Departemen Pertahanan AS mengamanatkan satu bahasa untuk sistem tertanam
- Jean Ichbiah memimpin desain di CII Honeywell Bull (Prancis)
- Dinamakan setelah Ada Lovelace — programmer komputer pertama
- Fitur utama: pengetikan yang kuat, paket, tugas (konkurensi), generik, pengecualian
- **Sasaran**: Sistem yang sangat penting bagi keselamatan — penerbangan, pertahanan, luar angkasa
### Ada 95 — Ada Berorientasi Objek (1995)
- **Bahasa OO berstandar ISO pertama** (sebelum Java distandarisasi)
- Tipe yang diberi tag (kelas), tipe seluruh kelas, pengiriman dinamis
- Objek yang dilindungi (akses data bersamaan yang aman)
- Paket anak (perpustakaan hierarki)
- Konfigurasi berbasis Pragma
### Ada 2005 — Penyempurnaan (2005)
- Antarmuka (berbagai warisan antarmuka)
- Jenis akses anonim (petunjuk yang disederhanakan)
- Peningkatan lingkaran `for`
- Pustaka kontainer (daftar tertaut ganda, vektor, peta)
- Pernyataan`return`yang diperluas
### Ada 2012 — Kontrak & Aspek (2012)
- **Pemrograman berorientasi aspek**: Klausul`aspect`dilampirkan pada deklarasi
- **Kontrak**:`Pre`,`Post`,`Type_Invariant`— verifikasi formal sudah ada di dalamnya
- Dukungan Iterator (`for X of Container loop`)
- Indikator `overriding`
- Fungsi ekspresi: `function F(X: Integer) return Integer is (X * 2);`
### Ada 2022 — Paralel & Hantu (2022)
- **`with ghost`**: Kode hantu untuk verifikasi (dikompilasi dalam produksi)
- **Konstruksi paralel**: loop `parallel`, blok `parallel`
- Peningkatan waktu nyata
- Perbaikan kontainer
- Penyempurnaan aspek `Iterator`
## Evolusi Sintaks
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

## Evolusi Fitur
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## Prinsip Desain Utama
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## Pertumbuhan Ekosistem
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
