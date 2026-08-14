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
# Ada – Leitfaden für Ökosysteme und Werkzeuge
Dieser Leitfaden behandelt die wesentlichen Tools, Bibliotheken und Infrastruktur im Ada-Ökosystem.
---

## Compiler und Implementierungen
| Compiler | Geben Sie | ein Notizen |
|----------|------|-------|
| **Mücke** | Open-Source | GCC-basiert, am weitesten verbreitet |
| **GNAT-Community** | Kostenlos | AdaCores kostenlose Edition |
| **GNAT Pro** | Kommerziell | Sicherheitszertifiziert, AdaCore |
| **ObjectAda** | Kommerziell | Fenster, sicherheitskritisch |
| **Janus/Ada** | Kommerziell | Eingebettete Systeme |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Build-Systeme und Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **Alire** | Moderner Paketmanager (empfohlen) |
| **GPRbuild** | Projekterstellungstool |
| **GPR (GNAT-Projekt)** | Projektdateiformat |
| **Machen** | Klassische Builds |
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

## Sicherheit und Überprüfung
| Werkzeug | Zweck |
|------|---------|
| **GNATprove** | Formale Verifizierung |
| **FUNKEN** | Sicherheitskritische Teilmenge |
| **CodePeer** | Statische Analyse |
| **Polyspace** | Laufzeitüberprüfung |
| **Deckung** | Statische Analyse |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **AUnit** | Unit-Test-Framework |
| **Ahven** | Einfaches Testen |
| **GNATtest** | Codebasiertes Testen |
| **gprbuild** | Erstellen und testen |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Ada.Containers** | Vektoren, Karten, Sets |
| **Ada.Strings** | String-Handhabung |
| **Ada.Text_IO** | Konsolen-E/A |
| **Ada.Calendar** | Datum/Uhrzeit |
| **GNATcoll** | GNAT-Dienstprogramme |
| **AWS** | Ada-Webserver |
| **XML/Ada** | XML-Analyse |
| **GID** | Bilddekodierung |
| **SDLAda** | SDL2-Bindungen |
| **GLFW** | OpenGL-Fensterung |
| **Cortex GNAT-Laufzeit** | Eingebettet (ARM) |
---

## Parallelität
| Funktion | Zweck |
|---------|---------|
| **Aufgaben** | Gleichzeitige Threads |
| **Geschützte Objekte** | Synchronisierte Daten |
| **Anweisungen auswählen** | Rendezvous |
| **Eintrittsaufrufe** | Synchronisierung |
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

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **GPS (GNAT Programming Studio)** | AdaCores IDE |
| **VS-Code + Ada** | Ada-Sprachunterstützung |
| **Emacs + ada-mode** | Klassische Ada-Umgebung |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Statische Binärdatei** | GNAT erzeugt statische Binärdateien |
| **Cross-Kompilierung** | GNAT-Kreuzkompilierung |
| **Eingebettet** | Bare-Metal, RTOS (Ravenscar) |
| **Docker** | Containerisiert |
| **Sicherheitszertifizierung** | DO-178C, IEC 61508, Common Criteria |
---

## Zusammenfassung
Das Ökosystem von Ada ist speziell für sicherheitskritische und hochzuverlässige Systeme konzipiert. Die Standard-Toolchain ist: **GNAT** (GCC-basiert) für die Kompilierung, **Alire** für die Paketverwaltung, **GPRbuild** für Builds, **GNATprove** und **SPARK** für die formale Verifizierung und **AUnit** für Tests. Ada zeichnet sich durch Luft- und Raumfahrt (DO-178C), Verteidigung, Eisenbahn, medizinische Geräte und alle Bereiche aus, in denen Korrektheit von größter Bedeutung ist. Adas Stärken sind starke Typisierung, Parallelität (Aufgaben, geschützte Objekte), formale Verifizierung (SPARK) und Sicherheitszertifizierung. Das Ökosystem ist für sicherheitskritische eingebettete Systeme unerlässlich.