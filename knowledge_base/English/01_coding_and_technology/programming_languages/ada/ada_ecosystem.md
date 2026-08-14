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

# Ada — Ecosystem & Tooling Guide

This guide covers the essential tools, libraries, and infrastructure in the Ada ecosystem.

---

## Compilers & Implementations

| Compiler | Type | Notes |
|----------|------|-------|
| **GNAT** | Open-source | GCC-based, most widely used |
| **GNAT Community** | Free | AdaCore's free edition |
| **GNAT Pro** | Commercial | Safety-certified, AdaCore |
| **ObjectAda** | Commercial | Windows, safety-critical |
| **Janus/Ada** | Commercial | Embedded systems |

```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Build Systems & Package Management

| Tool | Purpose |
|------|---------|
| **Alire** | Modern package manager (recommended) |
| **GPRbuild** | Project build tool |
| **GPR (GNAT Project)** | Project file format |
| **Make** | Classic builds |

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

## Safety & Verification

| Tool | Purpose |
|------|---------|
| **GNATprove** | Formal verification |
| **SPARK** | Safety-critical subset |
| **CodePeer** | Static analysis |
| **Polyspace** | Runtime verification |
| **Coverity** | Static analysis |

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

## Testing

| Framework | Purpose |
|-----------|---------|
| **AUnit** | Unit testing framework |
| **Ahven** | Simple testing |
| **GNATtest** | Code-based testing |
| **gprbuild** | Build and test |

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

## Key Libraries

| Library | Purpose |
|---------|---------|
| **Ada.Containers** | Vectors, maps, sets |
| **Ada.Strings** | String handling |
| **Ada.Text_IO** | Console I/O |
| **Ada.Calendar** | Date/time |
| **GNATcoll** | GNAT utilities |
| **AWS** | Ada Web Server |
| **XML/Ada** | XML parsing |
| **GID** | Image decoding |
| **SDLAda** | SDL2 bindings |
| **GLFW** | OpenGL windowing |
| **Cortex GNAT Runtime** | Embedded (ARM) |

---

## Concurrency

| Feature | Purpose |
|---------|---------|
| **Tasks** | Concurrent threads |
| **Protected Objects** | Synchronized data |
| **Select statements** | Rendezvous |
| **Entry calls** | Synchronization |

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

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **GPS (GNAT Programming Studio)** | AdaCore's IDE |
| **VS Code + Ada** | Ada language support |
| **Emacs + ada-mode** | Classic Ada environment |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Static binary** | GNAT produces static binaries |
| **Cross-compile** | GNAT cross-compilation |
| **Embedded** | Bare-metal, RTOS (Ravenscar) |
| **Docker** | Containerized |
| **Safety certification** | DO-178C, IEC 61508, Common Criteria |

---

## Summary

Ada's ecosystem is purpose-built for safety-critical and high-reliability systems. The standard toolchain is: **GNAT** (GCC-based) for compilation, **Alire** for package management, **GPRbuild** for builds, **GNATprove** and **SPARK** for formal verification, and **AUnit** for testing. Ada excels in aerospace (DO-178C), defense, railway, medical devices, and any domain where correctness is paramount. Ada's strengths are strong typing, concurrency (tasks, protected objects), formal verification (SPARK), and safety certification. The ecosystem is essential for safety-critical embedded systems.
