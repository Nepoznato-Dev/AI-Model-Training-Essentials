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

# Ada — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, biblioteki i infrastrukturę w ekosystemie Ada.
---

## Kompilatory i implementacje
| Kompilator | Wpisz | Notatki |
|---------|------|-------|
| **GNAT** | Otwarte oprogramowanie | Oparte na GCC, najczęściej używane |
| **Społeczność GNAT** | Bezpłatne | Bezpłatna edycja AdaCore |
| **GNAT Pro** | Komercyjne | Certyfikat bezpieczeństwa, AdaCore |
| **Ada obiektu** | Komercyjne | Okna, krytyczne dla bezpieczeństwa |
| **Janus/Ada** | Komercyjne | Systemy wbudowane |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Tworzenie systemów i zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **Alicja** | Nowoczesny menedżer pakietów (zalecane) |
| **GPRbuild** | Narzędzie do tworzenia projektów |
| **GPR (Projekt GNAT)** | Format pliku projektu |
| **Zrób** | Klasyczne konstrukcje |
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

## Bezpieczeństwo i weryfikacja
| Narzędzie | Cel |
|------|-------------|
| **GNATdowód** | Weryfikacja formalna |
| **ISKRA** | Podzbiór krytyczny dla bezpieczeństwa |
| **CodePeer** | Analiza statyczna |
| **Polika** | Weryfikacja środowiska wykonawczego |
| **Zakrycie** | Analiza statyczna |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **Jednostka** | Struktura testów jednostkowych |
| **Aven** | Proste testowanie |
| **GNATtest** | Testowanie oparte na kodzie |
| **gprbuild** | Kompiluj i testuj |
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

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Ada.Kontenery** | wektory, mapy, zestawy |
| **Ada.Stringi** | Obsługa ciągów |
| **Ada.Text_IO** | We/wy konsoli |
| **Ada.Kalendarz** | Data/godzina |
| **GNATcoll** | narzędzia GNAT |
| **AWS** | Serwer WWW Ada |
| **XML/Ada** | Analiza XML |
| **GID** | Dekodowanie obrazu |
| **SDLAda** | Wiązania SDL2 |
| **GLFW** | Okna OpenGL |
| **Środowisko wykonawcze Cortex GNAT** | Wbudowany (ARM) |
---

## Współbieżność
| Funkcja | Cel |
|--------|---------|
| **Zadania** | Równoległe wątki |
| **Obiekty chronione** | Zsynchronizowane dane |
| **Wybierz stwierdzenia** | Spotkanie |
| **Zaproszenia wejściowe** | Synchronizacja |
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

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **GPS (Studio programowania GNAT)** | IDE AdaCore |
| **Kod VS + Ada** | Obsługa języka Ada |
| **Emacs + tryb ada** | Klasyczne środowisko Ada |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Statyczny plik binarny** | GNAT tworzy statyczne pliki binarne |
| **Kompilacja krzyżowa** | Kompilacja krzyżowa GNAT |
| **Wbudowany** | Bare-metal, RTOS (Ravenscar) |
| **Doker** | Kontenerowy |
| **Certyfikat bezpieczeństwa** | DO-178C, IEC 61508, Wspólne kryteria |
---

## Streszczenie
Ekosystem Ady został stworzony specjalnie dla systemów o krytycznym znaczeniu dla bezpieczeństwa i charakteryzujących się wysoką niezawodnością. Standardowy zestaw narzędzi to: **GNAT** (oparty na GCC) do kompilacji, **Alire** do zarządzania pakietami, **GPRbuild** do kompilacji, **GNATprove** i **SPARK** do formalnej weryfikacji oraz **AUnit** do testowania. Ada specjalizuje się w lotnictwie i kosmonautyce (DO-178C), obronności, kolejnictwie, urządzeniach medycznych i każdej dziedzinie, w której poprawność jest najważniejsza. Mocne strony Ady to silne pisanie na klawiaturze, współbieżność (zadania, obiekty chronione), weryfikacja formalna (SPARK) i certyfikacja bezpieczeństwa. Ekosystem jest niezbędny dla systemów wbudowanych o krytycznym znaczeniu dla bezpieczeństwa.