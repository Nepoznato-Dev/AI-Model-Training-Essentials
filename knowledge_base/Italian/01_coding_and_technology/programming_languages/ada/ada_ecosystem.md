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

# Ada: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, le librerie e le infrastrutture essenziali nell'ecosistema Ada.
---

## Compilatori e implementazioni
| Compilatore | Digitare | Note |
|----------|------|-------|
| **GNAT** | Open source | Basato su GCC, il più utilizzato |
| **Comunità GNAT** | Gratuito | Edizione gratuita di AdaCore |
| **GNAT Pro** | Commerciale | Certificato di sicurezza, AdaCore |
| **OggettoAda** | Commerciale | Finestre, critiche per la sicurezza |
| **Giano/Ada** | Commerciale | Sistemi integrati |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Costruisci sistemi e gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **Alire** | Gestore di pacchetti moderno (consigliato) |
| **GPRbuild** | Strumento di creazione del progetto |
| **GPR (Progetto GNAT)** | Formato file di progetto |
| **Fai** | Costruzioni classiche |
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

## Sicurezza e verifica
| Strumento | Scopo |
|------|---------|
| **GNATprovare** | Verifica formale |
| **SCINTILLA** | Sottoinsieme critico per la sicurezza |
| **CodicePeer** | Analisi statica |
| **Polispazio** | Verifica runtime |
| **Copertura** | Analisi statica |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **UNità** | Quadro di test unitario |
| **Ahven** | Test semplici |
| **GNATtest** | Test basati su codice |
| **gprbuild** | Costruisci e testa |
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

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **Ada.Contenitori** | Vettori, mappe, set |
| **Ada.Stringhe** | Gestione delle stringhe |
| **Ada.Text_IO** | I/O della console |
| **Ada.Calendario** | Data/ora |
| **GNATcoll** | Utilità GNAT |
| **AWS** | Ada WebServer |
| **XML/Ada** | Analisi XML |
| **GID** | Decodifica delle immagini |
| **SDLAda** | Attacchi SDL2 |
| **GLFW** | Finestre OpenGL |
| **Runtime Cortex GNAT** | Incorporato (ARM) |
---

## Concorrenza
| Caratteristica | Scopo |
|---------|---------|
| **Compiti** | Discussioni simultanee |
| **Oggetti protetti** | Dati sincronizzati |
| **Seleziona affermazioni** | Appuntamento |
| **Chiamate di ingresso** | Sincronizzazione |
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

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **GPS (Studio di programmazione GNAT)** | IDE di AdaCore |
| **Codice VS + Ada** | Supporto linguistico Ada |
| **Emacs + modalità ada** | Ambiente Ada classico |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Binario statico** | GNAT produce binari statici |
| **Compilazione incrociata** | Compilazione incrociata GNAT |
| **Incorporato** | Bare-metal, RTOS (Ravenscar) |
| **Docker** | Containerizzato |
| **Certificazione di sicurezza** | DO-178C, IEC 61508, Criteri comuni |
---

## Riepilogo
L'ecosistema di Ada è costruito appositamente per sistemi critici per la sicurezza e ad alta affidabilità. La toolchain standard è: **GNAT** (basata su GCC) per la compilazione, **Alire** per la gestione dei pacchetti, **GPRbuild** per le build, **GNATprove** e **SPARK** per la verifica formale e **AUnit** per i test. Ada eccelle nel settore aerospaziale (DO-178C), difesa, ferroviario, dispositivi medici e in qualsiasi settore in cui la correttezza è fondamentale. I punti di forza di Ada sono la tipizzazione forte, la concorrenza (attività, oggetti protetti), la verifica formale (SPARK) e la certificazione di sicurezza. L’ecosistema è essenziale per i sistemi integrati critici per la sicurezza.