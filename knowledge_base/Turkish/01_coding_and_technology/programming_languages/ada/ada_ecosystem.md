<!--
---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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

-->
# Ada — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz Ada ekosistemindeki temel araçları, kütüphaneleri ve altyapıyı kapsar.
---

## Derleyiciler ve Uygulamalar
| Derleyici | Tür | Notlar |
|----------|------|----------|
| **TBMM** | Açık kaynak | GCC tabanlı, en yaygın kullanılan |
| **TBMM Topluluğu** | Ücretsiz | AdaCore'un ücretsiz sürümü |
| **TBMM Pro** | Ticari | Güvenlik sertifikalı, AdaCore |
| **ObjectAda** | Ticari | Güvenlik açısından kritik pencereler |
| **Janus/Ada** | Ticari | Gömülü sistemler |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Sistem Oluşturma ve Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **Alire** | Modern paket yöneticisi (önerilir) |
| **GPR yapısı** | Proje oluşturma aracı |
| **GPR (TBMM Projesi)** | Proje dosya formatı |
| **Yap** | Klasik yapılar |
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

## Güvenlik ve Doğrulama
| Araç | Amaç |
|------|------------|
| **TBMMKanıtla** | Resmi doğrulama |
| **KIVILCIM** | Güvenlik açısından kritik alt küme |
| **CodePeer** | Statik analiz |
| **Çokluuzay** | Çalışma zamanı doğrulaması |
| **Gizlilik** | Statik analiz |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **Birim** | Birim test çerçevesi |
| **Ahven** | Basit test |
| **TBMM testi** | Kod tabanlı test |
| **gprbuild** | Oluşturun ve test edin |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Ada.Konteynerler** | Vektörler, haritalar, setler |
| **Ada.Strings** | Dize işleme |
| **Ada.Text_IO** | Konsol G/Ç |
| **Ada.Takvim** | Tarih/saat |
| **TBMMColl** | TBMM hizmetleri |
| **AWS** | Ada Web Sunucusu |
| **XML/Ada** | XML ayrıştırma |
| **GID** | Görüntü kod çözme |
| **SDLAda** | SDL2 bağlamaları |
| **GLFW** | OpenGL pencereleme |
| **Cortex TBMM Çalışma Zamanı** | Gömülü (ARM) |
---

## Eşzamanlılık
| Özellik | Amaç |
|-----------|-----------|
| **Görevler** | Eşzamanlı konular |
| **Korunan Nesneler** | Senkronize veriler |
| **İfadeleri seçin** | Randevu |
| **Giriş çağrıları** | Senkronizasyon |
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

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **GPS (TBMM Programlama Stüdyosu)** | AdaCore'un IDE'si |
| **VS Kodu + Ada** | Ada dil desteği |
| **Emacs + ada modu** | Klasik Ada ortamı |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Statik ikili** | TBMM statik ikili dosyalar üretiyor |
| **Çapraz derleme** | TBMM çapraz derlemesi |
| **Gömülü** | Çıplak metal, RTOS (Ravenscar) |
| **Docker** | Konteynerde |
| **Güvenlik sertifikası** | DO-178C, IEC 61508, Ortak Kriterler |
---

## Özet
Ada'nın ekosistemi, güvenlik açısından kritik ve yüksek güvenilirliğe sahip sistemler için özel olarak tasarlanmıştır. Standart araç zinciri şu şekildedir: derleme için **TBMM** (GCC tabanlı), paket yönetimi için **Alire**, derlemeler için **GPRbuild**, resmi doğrulama için **GNATprove** ve **SPARK** ve test için **AUnit**. Ada, havacılık (DO-178C), savunma, demiryolu, tıbbi cihazlar ve doğruluğun en önemli olduğu her alanda üstün başarı göstermektedir. Ada'nın güçlü yönleri güçlü yazma, eşzamanlılık (görevler, korunan nesneler), resmi doğrulama (SPARK) ve güvenlik sertifikasıdır. Ekosistem, güvenlik açısından kritik gömülü sistemler için gereklidir.