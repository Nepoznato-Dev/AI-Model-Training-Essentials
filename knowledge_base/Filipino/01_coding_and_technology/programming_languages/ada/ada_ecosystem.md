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

# Ada — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang kasangkapan, aklatan, at imprastraktura sa Ada ecosystem.
---

## Mga Compiler at Pagpapatupad
| Compiler | Uri | Mga Tala |
|----------|------|-------|
| **GNAT** | Open-source | Nakabatay sa GCC, pinakamalawak na ginagamit |
| **GNAT Community** | Libre | Ang libreng edisyon ng AdaCore |
| **GNAT Pro** | Komersyal | Na-certify sa kaligtasan, AdaCore |
| **ObjectAda** | Komersyal | Windows, kritikal sa kaligtasan |
| **Janus/Ada** | Komersyal | Mga naka-embed na system |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## Bumuo ng Mga Sistema at Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **Aire** | Modern package manager (inirerekomenda) |
| **GPRbuild** | Tool sa pagbuo ng proyekto |
| **GPR (GNAT Project)** | Format ng file ng proyekto |
| **Gumawa** | Mga klasikong build |
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

## Kaligtasan at Pag-verify
| Tool | Layunin |
|------|---------|
| **GNATprove** | Pormal na pag-verify |
| **SPARK** | Subset na kritikal sa kaligtasan |
| **CodePeer** | Static na pagsusuri |
| **Polyspace** | Runtime na pag-verify |
| **Pagtatakpan** | Static na pagsusuri |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **AUnit** | Unit testing framework |
| **Ahven** | Simpleng pagsubok |
| **GNATtest** | Pagsubok na nakabatay sa code |
| **gprbuild** | Bumuo at subukan |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **Ada.Containers** | Mga vector, mapa, set |
| **Ada.Strings** | Paghawak ng string |
| **Ada.Text_IO** | Console I/O |
| **Ada.Calendar** | Petsa/oras |
| **GNATcoll** | Mga utility ng GNAT |
| **AWS** | Ada Web Server |
| **XML/Ada** | XML parsing |
| **GID** | Pag-decode ng larawan |
| **SDLAda** | SDL2 bindings |
| **GLFW** | OpenGL windowing |
| **Cortex GNAT Runtime** | Naka-embed (ARM) |
---

## Kasabay
| Tampok | Layunin |
|---------|---------|
| **Mga Gawain** | Kasabay na mga thread |
| **Mga Protektadong Bagay** | Naka-synchronize na data |
| **Pumili ng mga pahayag** | Rendezvous |
| **Mga tawag sa pagpasok** | Pag-synchronize |
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

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **GPS (GNAT Programming Studio)** | IDE ng AdaCore |
| **VS Code + Ada** | Suporta sa wika ng Ada |
| **Emacs + ada-mode** | Klasikong kapaligiran ng Ada |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Static binary** | Gumagawa ang GNAT ng mga static na binary |
| **Cross-compile** | GNAT cross-compilation |
| **Naka-embed** | Bare-metal, RTOS (Ravenscar) |
| **Docker** | Naka-container |
| **Certification sa kaligtasan** | DO-178C, IEC 61508, Mga Karaniwang Pamantayan |
---

## Buod
Ang ecosystem ng Ada ay sadyang binuo para sa mga sistemang kritikal sa kaligtasan at mataas ang pagiging maaasahan. Ang karaniwang toolchain ay: **GNAT** (GCC-based) para sa compilation, **Alire** para sa pamamahala ng package, **GPRbuild** para sa mga build, **GNATprove** at **SPARK** para sa pormal na pag-verify, at **AUnit** para sa pagsubok. Ang Ada ay mahusay sa aerospace (DO-178C), depensa, railway, mga medikal na device, at anumang domain kung saan ang kawastuhan ay pinakamahalaga. Ang mga lakas ni Ada ay malakas na pag-type, concurrency (mga gawain, mga protektadong bagay), pormal na pag-verify (SPARK), at sertipikasyon sa kaligtasan. Ang ecosystem ay mahalaga para sa mga kritikal na kaligtasan na naka-embed na mga system.