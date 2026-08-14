---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ada, ecosystem, tooling, compilers, safety-critical, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ada — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, perpustakaan, dan infrastruktur penting dalam ekosistem Ada.
---

## Kompiler & Implementasi
| Kompiler | Ketik | Catatan |
|----------|------|-------|
| **Agas** | Sumber terbuka | Berbasis GCC, paling banyak digunakan |
| **Komunitas AGNAT** | Gratis | Edisi gratis AdaCore |
| **GNAT Pro** | Komersial | Bersertifikat keamanan, AdaCore |
| **ObjekAda** | Komersial | Windows, kritis terhadap keselamatan |
| **Janus/Ada** | Komersial | Sistem tertanam |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Bangun Sistem & Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **Ali** | Manajer paket modern (disarankan) |
| **Pembangunan GPR** | Alat pembangunan proyek |
| **GPR (Proyek GNAT)** | Format file proyek |
| **Buat** | Bangunan klasik |
```toml
# alire.toml
name = "myapp"
description = "My Ada application"
version = "0.1.0"

[[depends-on]]
gnat = "^13"
gnatcoll = "^24"

[[pins]]
```

```bash
alr init --bin myapp      # create project
alr build                 # build
alr run                   # run
alr get --build gnatcoll  # get dependency
alr search                # search packages
alr index                 # update index
```

```gpr
-- myproject.gpr
project Myproject is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Main use ("main.adb");
   
   package Compiler is
      for Default_Switches ("Ada") use ("-gnatwa", "-gnatVa", "-O2");
   end Compiler;
   
   package Binder is
      for Default_Switches ("Ada") use ("-E");  -- store exceptions
   end Binder;
end Myproject;
```

---

## Keamanan & Verifikasi
| Alat | Tujuan |
|------|---------|
| **GNATbuktikan** | Verifikasi formal |
| **PERCIPTAAN** | Subset yang kritis terhadap keselamatan |
| **Rekan Kode** | Analisis statis |
| **Poliruang** | Verifikasi waktu proses |
| **Penutup** | Analisis statis |
```ada
-- SPARK example
package Stack with
   SPARK_Mode
is
   type Bounded_Stack (Capacity : Positive) is tagged private;
   
   procedure Push (S : in out Bounded_Stack; Element : Integer)
      with Pre  => not S.Is_Full,
           Post => not S.Is_Empty and S.Top = Element;
   
   function Is_Full (S : Bounded_Stack) return Boolean;
   function Is_Empty (S : Bounded_Stack) return Boolean;
   
private
   type Bounded_Stack (Capacity : Positive) is tagged record
      Data : array (1 .. Capacity) of Integer;
      Top_Index : Natural := 0;
   end record;
end Stack;
```

---

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Unit** | Kerangka pengujian unit |
| **Ahven** | Pengujian sederhana |
| **Ujian GNAT** | Pengujian berbasis kode |
| **gprbuild** | Bangun dan uji |
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Stack_Test is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;
   
   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Stack_Test;

package body Stack_Test is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("Stack Tests");
   end Name;
   
   procedure Run_Test (T : in out Test_Case) is
      S : Bounded_Stack (10);
   begin
      Push (S, 42);
      AUnit.Assertions.Assert (Top (S) = 42, "Top should be 42");
      AUnit.Assertions.Assert (not Is_Empty (S), "Should not be empty");
   end Run_Test;
end Stack_Test;
```

---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Ada.Kontainer** | Vektor, peta, set |
| **Ada.String** | Penanganan string |
| **Ada.Teks_IO** | Konsol I/O |
| **Ada.Kalender** | Tanggal/waktu |
| **GNATkol** | Utilitas GNAT |
| **AWS** | Ada Server Web |
| **XML/Ada** | Penguraian XML |
| **GID** | Penguraian gambar |
| **SDLAda** | Pengikatan SDL2 |
| **GLFW** | Jendela OpenGL |
| **Waktu Proses GNAT Korteks** | Tertanam (ARM) |
---

## Konkurensi
| Fitur | Tujuan |
|---------|---------|
| **Tugas** | Utas serentak |
| **Objek yang Dilindungi** | Data yang disinkronkan |
| **Pilih pernyataan** | Pertemuan |
| **Panggilan masuk** | Sinkronisasi |
```ada
task type Worker is
   entry Do_Work (Item : in Integer);
end Worker;

task body Worker is
   Value : Integer;
begin
   loop
      select
         accept Do_Work (Item : in Integer) do
            Value := Item;
         end Do_Work;
         Process (Value);
      or
         terminate;
      end select;
   end loop;
end Worker;
```

---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **GPS (Studio Pemrograman GNAT)** | IDE AdaCore |
| **Kode VS + Ada** | Ada dukungan bahasa |
| **Emacs + ada-mode** | Lingkungan Ada Klasik |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Biner statis** | GNAT menghasilkan biner statis |
| **Kompilasi silang** | kompilasi silang GNAT |
| **Tertanam** | Bare-metal, RTOS (Ravenscar) |
| **Buruh pelabuhan** | dalam kontainer |
| **Sertifikasi keselamatan** | DO-178C, IEC 61508, Kriteria Umum |
---

## Ringkasan
Ekosistem Ada dibangun khusus untuk sistem yang kritis terhadap keselamatan dan memiliki keandalan tinggi. Toolchain standarnya adalah: **GNAT** (berbasis GCC) untuk kompilasi, **Alire** untuk manajemen paket, **GPRbuild** untuk build, **GNATprove** dan **SPARK** untuk verifikasi formal, dan **AUnit** untuk pengujian. Ada unggul dalam bidang kedirgantaraan (DO-178C), pertahanan, perkeretaapian, peralatan medis, dan bidang apa pun yang mengutamakan kebenaran. Kekuatan Ada adalah pengetikan yang kuat, konkurensi (tugas, objek yang dilindungi), verifikasi formal (SPARK), dan sertifikasi keselamatan. Ekosistem sangat penting untuk sistem tertanam yang kritis terhadap keselamatan.