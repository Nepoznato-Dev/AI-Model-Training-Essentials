---
# Metadata
title: "Ada"
description: "Comprehensive reference for the Ada programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ada, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "35 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#اڈا
Ada ایک مستحکم طور پر ٹائپ شدہ، مرتب کردہ پروگرامنگ لینگویج ہے جسے حفاظت کے لیے اہم اور اعلیٰ سالمیت کے نظام کے لیے ڈیزائن کیا گیا ہے۔ اصل میں 1980 کی دہائی میں امریکی محکمہ دفاع کے ساتھ معاہدے کے تحت تیار کیا گیا (Ada Lovelace کے نام پر رکھا گیا، جسے پہلا کمپیوٹر پروگرامر سمجھا جاتا ہے)، Ada نے بھروسے، برقرار رکھنے اور درستگی پر زور دیا۔ اسے سیکڑوں پروگرامنگ زبانوں کو تبدیل کرنے کے لیے ڈیزائن کیا گیا تھا جس کے بعد DoD نے ایک واحد، اچھی طرح سے مخصوص زبان کے ساتھ استعمال کیا تھا۔
Ada کا استعمال ہوا بازی (فلائی بائی وائر سسٹمز)، اسپیس (ESA اور NASA)، دفاع (میزائل گائیڈنس، ریڈار)، ریل ٹرانسپورٹ، اور طبی آلات میں کیا جاتا ہے — جہاں کہیں بھی سافٹ ویئر کی ناکامی سے جانیں ضائع ہو سکتی ہیں۔
---

## ایڈا کیوں اہمیت رکھتی ہے۔
- **حفاظتی اہم نظام**: ایسے سسٹمز کے لیے زمین سے ڈیزائن کیا گیا ہے جہاں ناکامی کوئی آپشن نہیں ہے۔
- **مضبوط ٹائپنگ**: کسی بھی مرکزی دھارے کی زبان کا سب سے سخت قسم کا نظام — کمپائل کے وقت غلطیوں کو پکڑتا ہے جو دوسری زبانوں سے چھوٹ جاتی ہے۔
- **بلٹ ان کنکرنسی**: ٹاسکنگ (کنکرنٹ پروگرامنگ) زبان کا حصہ ہے، لائبریری نہیں۔
- **رسمی تصدیق**: پروگرام کی درستگی کو ثابت کرنے کے لیے رسمی طریقوں کی حمایت کرتا ہے۔
- **قابل اعتماد خصوصیات**: پہلے سے شامل مستثنیات، معاہدے (پہلے/پوسٹ کنڈیشنز)، اور رن ٹائم چیک۔
- **جدید Ada**: Ada 2012 اور Ada 2022 نے حفاظت کی ضمانتوں کو برقرار رکھتے ہوئے جدید خصوصیات کا اضافہ کیا ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **طاق برادری** | سی، جاوا، یا ازگر کے مقابلے میں چھوٹا ڈویلپر بیس | خصوصی لیکن باشعور کمیونٹی |
| **وربوز نحو** | C یا Python سے زیادہ لفظی | حفاظت پر مبنی ڈیزائن کے حصے کے طور پر قبول کریں |
| **محدود ماحولیاتی نظام** | مرکزی دھارے کی زبانوں سے کم لائبریریاں | حسب ضرورت کوڈ لکھیں؛ وسیع معیاری لائبریری کا استعمال کریں |
| **سیکھنے کا وکر** | بہت سی حفاظتی خصوصیات کے ساتھ پیچیدہ زبان | حفاظت کے لیے اہم کام کے لیے Ada کے "SPARK" سب سیٹ کے ساتھ شروع کریں |
| **کمپائلر کی دستیابی** | کم مرتب کرنے والے اختیارات (GNAT اہم ہے) | GNAT مفت اور اچھی طرح سے برقرار ہے |
---

## نحوی بنیادی باتیں
```ada
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Hello_World is
   Name : constant String := "Alice";
   Age  : Integer := 30;
begin
   Put_Line("Hello, " & Name & "! Age:" & Integer'Image(Age));
end Hello_World;

-- Strong typing
type Temperature is new Float range -273.15 .. 1000.0;
type Celsius is new Float range -273.15 .. 1000.0;

-- These are DIFFERENT types — cannot mix them
Temp : Temperature := 25.0;
-- Temp := Celsius(30.0);  -- Explicit conversion required

-- Arrays with bounds checking
type Day_Index is range 1 .. 7;
type Temperature_Array is array (Day_Index) of Temperature;

-- Records (structs)
type Point is record
   X : Float;
   Y : Float;
end record;

-- Subtypes with constraints
subtype Percentage is Float range 0.0 .. 100.0;

-- Protected objects (thread-safe)
protected type Counter is
   procedure Increment;
   function Value return Integer;
private
   Count : Integer := 0;
end Counter;

protected body Counter is
   procedure Increment is
   begin
      Count := Count + 1;
   end Increment;

   function Value return Integer is
   begin
      return Count;
   end Value;
end Counter;

-- Tasks (concurrency)
task type Worker is
   entry Start(Id : Integer);
end Worker;

task body Worker is
   My_Id : Integer;
begin
   accept Start(Id : Integer) do
      My_Id := Id;
   end Start;
   -- Do work...
end Worker;
```

---

## اعلی درجے کی نحو اور نمونے۔
### ٹیگ شدہ اقسام اور وراثت (OOP)
```ada
-- Abstract base type
package Shapes is
   type Shape is abstract tagged record
      Colour : String(1 .. 10) := ("green     ");
   end record;

   function Area(S : Shape) return Float is abstract;
   procedure Draw(S : Shape) is abstract;

   type Circle is new Shape with record
      Radius : Float := 0.0;
   end record;

   overriding function Area(S : Circle) return Float;
   overriding procedure Draw(S : Circle);

   type Rectangle is new Shape with record
      Width  : Float := 0.0;
      Height : Float := 0.0;
   end record;

   overriding function Area(S : Rectangle) return Float;
   overriding procedure Draw(S : Rectangle);

   -- Class-wide type for polymorphism
   procedure Print_Area(S : Shape'Class);
end Shapes;

package body Shapes is
   function Area(S : Circle) return Float is
   begin
      return 3.14159 * S.Radius ** 2;
   end Area;

   procedure Draw(S : Circle) is
   begin
      null; -- Draw circle
   end Draw;

   function Area(S : Rectangle) return Float is
   begin
      return S.Width * S.Height;
   end Area;

   procedure Draw(S : Rectangle) is
   begin
      null; -- Draw rectangle
   end Draw;

   procedure Print_Area(S : Shape'Class) is
   begin
      Put_Line("Area: " & Float'Image(Area(S)));
   end Print_Area;
end Shapes;
```

### آپریٹر اوورلوڈنگ
```ada
package Vector_Math is
   type Vec3 is record
      X, Y, Z : Float;
   end record;

   function "+" (A, B : Vec3) return Vec3;
   function "*" (A, B : Vec3) return Float;  -- dot product
   function "*" (S : Float; V : Vec3) return Vec3;
   function "=" (A, B : Vec3) return Boolean;
end Vector_Math;

package body Vector_Math is
   function "+" (A, B : Vec3) return Vec3 is
   begin
      return (A.X + B.X, A.Y + B.Y, A.Z + B.Z);
   end "+";

   function "*" (A, B : Vec3) return Float is
   begin
      return A.X * B.X + A.Y * B.Y + A.Z * B.Z;
   end "*";

   function "*" (S : Float; V : Vec3) return Vec3 is
   begin
      return (S * V.X, S * V.Y, S * V.Z);
   end "*";

   function "=" (A, B : Vec3) return Boolean is
   begin
      return A.X = B.X and A.Y = B.Y and A.Z = B.Z;
   end "=";
end Vector_Math;
```

### جنرک (مرتب وقت پولیمورفزم)
```ada
-- Generic package for type-safe containers
generic
   type Element_Type is private;
   with function "=" (A, B : Element_Type) return Boolean is <>;
package Generic_Stack is
   type Stack is limited private;
   procedure Push(S : in out Stack; E : Element_Type);
   procedure Pop(S : in out Stack; E : out Element_Type);
   function Is_Empty(S : Stack) return Boolean;
private
   Max_Size : constant := 1000;
   type Index_Type is range 1 .. Max_Size;
   type Array_Type is array (Index_Type range <>) of Element_Type;
   type Stack is record
      Data : Array_Type(1 .. Max_Size);
      Top  : Natural := 0;
   end record;
end Generic_Stack;

package body Generic_Stack is
   procedure Push(S : in out Stack; E : Element_Type) is
   begin
      if S.Top = Max_Size then
         raise Constraint_Error with "Stack overflow";
      end if;
      S.Top := S.Top + 1;
      S.Data(S.Top) := E;
   end Push;

   procedure Pop(S : in out Stack; E : out Element_Type) is
   begin
      if S.Top = 0 then
         raise Constraint_Error with "Stack underflow";
      end if;
      E := S.Data(S.Top);
      S.Top := S.Top - 1;
   end Pop;

   function Is_Empty(S : Stack) return Boolean is
   begin
      return S.Top = 0;
   end Is_Empty;
end Generic_Stack;

-- Instantiate for Integer
with Generic_Stack;
package Int_Stack is new Generic_Stack(Element_Type => Integer);
```

### معاہدے اور پہلو (Ada 2012)
```ada
function Square_Root(X : Float) return Float
   with Pre  => X >= 0.0,
        Post => Square_Root'Result >= 0.0
             and then abs (Square_Root'Result ** 2 - X) < 0.001;

procedure Swap(A, B : in out Integer)
   with Pre  => A /= B,
        Post => A = B'Old and B = A'Old;

-- Type invariants
type Bounded_Buffer is record
   Data : array (1 .. 100) of Integer := (others => 0);
   Head : Integer range 0 .. 100 := 0;
end record
   with Type_Invariant => Bounded_Buffer.Head <= 100;

-- Predicates
subtype Even_Integer is Integer
   with Static_Predicate => Even_Integer in Integer => Even_Integer mod 2 = 0;
```

---

## ہم آہنگی اور ہم آہنگی
### کام اور ملاقات
```ada
-- Task with entry (rendezvous communication)
task type Server is
   entry Request(Data : in Integer; Result : out Integer);
   entry Stop;
end Server;

task body Server is
   Running : Boolean := True;
begin
   while Running loop
      select
         accept Request(Data : in Integer; Result : out Integer) do
            Result := Data * Data;  -- Process request
         end Request;
      or
         accept Stop do
            Running := False;
         end Stop;
      end select;
   end loop;
end Server;

-- Usage
S : Server;
Answer : Integer;
S.Request(5, Answer);  -- Answer = 25
S.Stop;
```

### محفوظ آبجیکٹ (تھریڈ سے محفوظ مشترکہ ڈیٹا)
```ada
-- Protected object with internal mutual exclusion
protected type Shared_Buffer is
   procedure Put(Item : Integer);
   entry Get(Item : out Integer);
   function Count return Natural;
private
   Data    : array (1 .. 100) of Integer;
   Head    : Positive := 1;
   Tail    : Positive := 1;
   Num     : Natural := 0;
end Shared_Buffer;

protected body Shared_Buffer is
   procedure Put(Item : Integer) is
   begin
      if Num < 100 then
         Data(Tail) := Item;
         Tail := Tail mod 100 + 1;
         Num := Num + 1;
      end if;
   end Put;

   entry Get(Item : out Integer) when Num > 0 is
   begin
      Item := Data(Head);
      Head := Head mod 100 + 1;
      Num := Num - 1;
   end Get;

   function Count return Natural is
   begin
      return Num;
   end Count;
end Shared_Buffer;

-- Usage from multiple tasks (automatically synchronised)
Buf : Shared_Buffer;
```

### متوازی کمپیوٹنگ (Ada 2022)
```ada
-- Parallel arrays (Ada 2022)
with Ada.Containers.Parallel;

-- Parallel iteration
for I in 1 .. 1_000_000 loop
   pragma Parallel_Loop;
   Results(I) := Compute(Data(I));
end loop;

-- Task pool pattern
task type Worker_Task(Id : Integer) is
   entry Work(Job : in Integer);
end Worker_Task;

task body Worker_Task is
   Current_Job : Integer;
begin
   loop
      accept Work(Job : in Integer) do
         Current_Job := Job;
      end Work;
      -- Process Current_Job
      Process(Current_Job, Id);
   end loop;
end Worker_Task;

-- Create pool of workers
Workers : array (1 .. 4) of Worker_Task;
```

---

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### GPR (GNAT پروجیکٹ) فائلیں۔
```
-- my_project.gpr
project My_Project is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Exec_Dir use "bin";
   for Main use ("main.adb");

   type Build_Mode is ("Debug", "Release", "Profile");
   Mode : Build_Mode := external("BUILD", "Debug");

   package Compiler is
      case Mode is
         when "Debug" =>
            for Default_Switches ("Ada") use
               ("-g", "-O0", "-gnata", "-gnatwa", "-gnatVa");
         when "Release" =>
            for Default_Switches ("Ada") use
               ("-O2", "-gnatp");
         when "Profile" =>
            for Default_Switches ("Ada") use
               ("-O2", "-pg", "-gnatn");
      end case;
   end Compiler;

   package Binder is
      for Switches ("Ada") use ("-E");  -- Runtime symbolization
   end Binder;

   package Linker is
      for Linker_Options use ("-lpthread");
   end Linker;
end My_Project;
```

### پروجیکٹ کا ڈھانچہ
```
my-ada-project/
+-- my_project.gpr         # GNAT project file
+-- src/
|   +-- main.adb           # Main program
|   +-- main.ads           # Main spec (if needed)
|   +-- my_package.ads     # Package specification
|   +-- my_package.adb     # Package body
|   +-- types.ads          # Shared type definitions
+-- tests/
|   +-- test_runner.adb
|   +-- test_my_package.ads
|   +-- test_my_package.adb
+-- lib/                   # External dependencies
+-- obj/                   # Object files (generated)
+-- bin/                   # Executables (generated)
+-- doc/
|   +-- design.md
```

### کمانڈز بنائیں
```bash
# Build with gnatmake (simple)
gnatmake -P my_project.gpr

# Build with gprbuild (recommended)
gprbuild -P my_project.gpr

# Build in release mode
gprbuild -P my_project.gpr -XBUILD=Release

# Clean build
gprclean -P my_project.gpr

# Run
./bin/main
```

### CI/CD GitHub ایکشن کے ساتھ
```yaml
name: Ada CI
on:
  push: {branches: [main]}
  pull_request: {branches: [main]}
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: sudo apt-get install -y gnat
      - run: gprbuild -P my_project.gpr
      - run: ./bin/run_tests
```

---

## ٹیسٹنگ
### AUnit ٹیسٹنگ فریم ورک
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Test_My_Package is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;

   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Test_My_Package;

package body Test_My_Package is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("My_Package Tests");
   end Name;

   procedure Run_Test (T : in out Test_Case) is
      use AUnit.Assertions;
   begin
      -- Test addition
      Assert (2 + 2 = 4, "Basic addition failed");

      -- Test custom function
      declare
         Result : constant Integer := My_Function(5);
      begin
         Assert (Result = 25, "My_Function(5) should be 25");
      end;

      -- Test exception
      begin
         Danger(0);
         Assert (False, "Should have raised exception");
      exception
         when Constraint_Error => null; -- Expected
      end;
   end Run_Test;
end Test_My_Package;

-- Test runner
with AUnit.Run;
with AUnit.Reporter.Text;
with AUnit.Test_Suites;
procedure Run_All_Tests is
   use AUnit.Test_Suites;
   Suite : constant Access_Test_Suite := new Test_Suite;
   TC    : aliased Test_My_Package.Test_Case;
begin
   Add_Test (Suite, TC'Unchecked_Access);
   declare
      Runner : AUnit.Run.Test_Runner := AUnit.Run.Run_Suite (Suite);
      Reporter : AUnit.Reporter.Text.Text_Reporter;
   begin
      Reporter.Report (Runner);
   end;
end Run_All_Tests;
```

---

## انٹرآپریبلٹی
### C انٹرآپریبلٹی (انٹرفیس)
```ada
with Interfaces.C;
with Interfaces.C.Strings;

package C_Bridge is
   use Interfaces.C;

   -- Import C function
   function C_Malloc(Size : size_t) return System.Address;
   pragma Import(C, C_Malloc, "malloc");

   procedure C_Free(Ptr : System.Address);
   pragma Import(C, C_Free, "free");

   -- Export Ada function for C
   function Ada_Compute(X : double) return double;
   pragma Export(C, Ada_Compute, "compute");

   -- Struct interoperability
   type C_Point is record
      X : double;
      Y : double;
   end record
   with Convention => C;

   -- Call C library
   function C_Sqrt(X : double) return double;
   pragma Import(C, C_Sqrt, "sqrt");
end C_Bridge;
```

### مخلوط زبان کی پروگرامنگ
```ada
-- Ada calling C library (e.g., BLAS)
with Interfaces.C; use Interfaces.C;

package BLAS_Interface is
   type Matrix is array (Positive range <>, Positive range <>) of double;

   -- DGEMM: C = alpha * A * B + beta * C
   procedure DGEMM(
      Transa, Transb : Character;
      M, N, K         : int;
      Alpha           : double;
      A               : in double;
      LDA             : int;
      B               : in double;
      LDB             : int;
      Beta            : double;
      C               : in out double;
      LDC             : int
   );
   pragma Import(C, DGEMM, "dgemm_");
end BLAS_Interface;
```

---

## ڈیزائن پیٹرن
### پیٹرن 1: محفوظ آبجیکٹ کے ساتھ مبصر
```ada
protected type Event_Bus is
   procedure Subscribe(Handler_Id : Positive);
   procedure Notify(Event : String);
   function Subscriber_Count return Natural;
private
   type Handler_Array is array (1 .. 100) of Boolean;
   Active   : Handler_Array := (others => False);
   Count    : Natural := 0;
end Event_Bus;

protected body Event_Bus is
   procedure Subscribe(Handler_Id : Positive) is
   begin
      if not Active(Handler_Id) then
         Active(Handler_Id) := True;
         Count := Count + 1;
      end if;
   end Subscribe;

   procedure Notify(Event : String) is
   begin
      for I in 1 .. 100 loop
         if Active(I) then
            Dispatch(I, Event);
         end if;
      end loop;
   end Notify;

   function Subscriber_Count return Natural is
   begin
      return Count;
   end Subscriber_Count;
end Event_Bus;
```

### پیٹرن 2: امتیازی اقسام کے ساتھ ریاستی مشین
```ada
type Traffic_Light_State is (Red, Yellow, Green);

type Traffic_Light(State : Traffic_Light_State := Red) is record
   case State is
      when Red    => Timer : Natural := 30;
      when Yellow => Timer : Natural := 5;
      when Green  => Timer : Natural := 25;
   end case;
end record;

procedure Advance(L : in out Traffic_Light) is
begin
   case L.State is
      when Red    => L := (State => Green,  Timer => 25);
      when Green  => L := (State => Yellow, Timer => 5);
      when Yellow => L := (State => Red,    Timer => 30);
   end case;
end Advance;
```

### پیٹرن 3: کنٹرول شدہ اقسام کے ساتھ RAII
```ada
with Ada.Finalization;

type File_Handle is new Ada.Finalization.Controlled with record
   FD : Integer := -1;
end record;

overriding procedure Initialize(F : in out File_Handle) is
begin
   F.FD := Open_File("data.txt");
end Initialize;

overriding procedure Finalize(F : in out File_Handle) is
begin
   if F.FD >= 0 then
      Close_File(F.FD);
      F.FD := -1;
   end if;
end Finalize;

-- Usage: file is automatically closed when it goes out of scope
procedure Process is
   F : File_Handle;  -- Opens on creation
begin
   Read_Data(F);
end Process;  -- Automatically calls Finalize (closes file)
```

---

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
```bash
# GNAT profiling with gprof
gnatmake -g -pg my_program.adb
./my_program
gprof my_program gmon.out > profile.txt

# GNAT coverage analysis
gnatmake -fprofile-arcs -ftest-coverage my_program.adb
./my_program
gcov my_program.adb

# GNAT stack usage analysis
gnatstack -P my_project.gpr

# Valgrind for memory checking
valgrind --tool=memcheck ./my_program
```

### کمپائلر آپٹیمائزیشن
```bash
# GNAT optimisation flags
# Debug build (with runtime checks)
gprbuild -P my_project.gpr -XBUILD=Debug
# Flags: -g -O0 -gnata (assertions) -gnatwa (warnings) -gnatVa (validity)

# Release build (maximum performance)
gprbuild -P my_project.gpr -XBUILD=Release
# Flags: -O2 -gnatp (suppress all checks)

# Key GNAT flags:
# -gnatp      : Suppress all runtime checks (fastest)
# -gnata      : Enable assertions
# -gnatwa     : Enable all warnings
# -gnatVa     : Validity checks
# -gnateE     : Exception tracebacks
# -O2 / -O3   : Optimisation levels
# -march=native: CPU-specific optimisations
```

### زیرو-اوور ہیڈ خلاصہ
```ada
-- Ada's type system adds safety at compile time with zero runtime cost
type Altitude is new Float range 0.0 .. 100_000.0;
type Speed is new Float range 0.0 .. 2_000.0;

-- These checks happen at compile time or at boundaries
-- No runtime overhead for type-safe code
procedure Fly(A : Altitude; V : Speed) is
begin
   -- A and V are just Floats at runtime
   -- But the compiler prevents mixing Altitude and Speed
   null;
end Fly;

-- Inline procedures for hot paths
procedure Fast_Add(A, B : in out Integer) is
begin
   A := A + B;
end Fast_Add;
pragma Inline(Fast_Add);
```

---

## تعیناتی۔
### سیفٹی-کریٹیکل سرٹیفیکیشن کے لیے سپارک
```ada
-- SPARK subset: provably correct code
-- @SPARK_MODE ON

package Safety_Critical is
   procedure Compute_Output
     (Input : Float; Output : out Float)
   with
     Pre  => Input >= 0.0 and Input <= 100.0,
     Post => Output >= 0.0 and Output <= 1.0;
end Safety_Critical;

-- SPARK Prover verifies:
-- 1. No runtime errors possible
-- 2. Preconditions always satisfied at call sites
-- 3. Postconditions always hold on return
-- 4. No integer overflow, division by zero, etc.

-- Certification standards supported:
-- DO-178C (avionics) - Level A
-- IEC 61508 (functional safety) - SIL 4
-- ISO 26262 (automotive) - ASIL D
-- EN 50128 (railway) - SIL 4
```

### اسٹینڈ تنہا تعیناتی۔
```bash
# Static linking (no runtime dependencies)
gprbuild -P my_project.gpr -largs -static

# Create minimal runtime
gnatmake my_program.adb -bargs -static

# Cross-compilation (e.g., for embedded target)
gprbuild -P my_project.gpr --target=arm-eabi

# Docker deployment
# FROM debian:bullseye-slim
# RUN apt-get install -y libgnat-9
# COPY bin/my_app /usr/local/bin/
# ENTRYPOINT ["my_app"]
```

### ایمبیڈڈ تعیناتی۔
```ada
-- Bare-metal Ada for microcontrollers
-- No OS, no runtime, direct hardware access

procedure Main is
   -- Map to hardware registers
   GPIO_PORTA : array (0 .. 15) of Unsigned_32
      with Address => System'To_Address(16#4800_0000#);
begin
   -- Configure pin as output
   GPIO_PORTA(0) := 1;  -- Set LED on

   loop
      GPIO_PORTA(0) := not GPIO_PORTA(0);  -- Toggle LED
      Delay_Ms(500);
   end loop;
end Main;
```

---

## اڈا کب استعمال کریں۔
| منظر نامہ | کیوں اڈا | بہتر متبادل |
|------------|---------|-------------------|
| حفاظتی اہم نظام | اس کے لیے ڈیزائن کیا گیا ہے؛ رسمی تصدیق کی حمایت | - |
| ایوی ایشن / ایرو اسپیس | مصدقہ مرتب کرنے والے؛ DO-178C تعمیل | - |
| دفاعی نظام | DoD ورثہ؛ سیکورٹی خصوصیات | - |
| ریلوے / طبی آلات | اعلی سالمیت کی ضروریات | - |
| عام درخواست کی ترقی | غیر اہم نظاموں کے لیے اوور کِل | Python, Java, Go |
| ویب ڈویلپمنٹ | مناسب نہیں | جاوا اسکرپٹ، ازگر |
| ڈیٹا سائنس / ایم ایل | ماحولیاتی نظام نہیں | ازگر، آر |
---

## مصنوعی سوال و جواب
### Q1: Ada کا ٹائپ سسٹم کمپائل کے وقت کیڑے کو کیسے روکتا ہے؟
**A:** Ada کا ٹائپ سسٹم کسی بھی زبان میں سخت ترین ہے۔ یہ ایسی غلطیاں پکڑتا ہے جو دوسری زبانوں سے چھوٹ جاتی ہیں:
```ada
-- Subtypes with range constraints
type Temperature is range -273 .. 1000;  -- Celsius, absolute zero limit
type Percentage is range 0 .. 100;

-- The compiler rejects invalid values at compile time
T : Temperature := 2000;  -- Compile error!
P : Percentage := 150;    -- Compile error!

-- Modular types (wrap-around arithmetic)
type Byte is mod 256;
type Port is range 0 .. 65535;

-- Enumerated types with explicit values
type Traffic_Light is (Red, Yellow, Green);
-- Ada guarantees exhaustive case analysis
```

### Q2: Ada کا ٹاسکنگ ماڈل کیا ہے اور یہ دوسرے کنکرنسی ماڈلز سے کیسے موازنہ کرتا ہے؟
**A:** Ada کے پاس محفوظ اشیاء اور کاموں کے ساتھ بلٹ ان کنکرنسی ہے:
```ada
-- Protected object — safe shared state
protected type Counter is
   procedure Increment;
   function Value return Integer;
private
   Count : Integer := 0;
end Counter;

protected body Counter is
   procedure Increment is begin Count := Count + 1; end;
   function Value return Integer is (Count);
end Counter;

-- Task — concurrent execution
task type Worker is
   entry Start(Job_ID : Integer);
end Worker;

task body Worker is
   ID : Integer;
begin
   accept Start(Job_ID : Integer) do
      ID := Job_ID;
   end Start;
   -- Process job...
end Worker;
```

### Q3: میں Ada میں جنرک کیسے استعمال کروں؟
**A:** Ada generics واضح اور ٹائپ سیف ہیں:
```ada
generic
   type Element_Type is private;
   type Index_Type is range <>;
package Generic_Stack is
   procedure Push(Item : in Element_Type);
   function Pop return Element_Type;
   function Is_Empty return Boolean;
end Generic_Stack;
```

### Q4: Ada کو حفاظتی اہم نظاموں کے لیے کیا موزوں بناتا ہے؟
**A:** Ada فراہم کرتا ہے:
- رسمی تصدیق کے لیے سپارک سب سیٹ (صحیح ہونے کا ریاضیاتی ثبوت)
- معاہدہ پر مبنی پروگرامنگ (پہلے/پوسٹ کنڈیشنز، ٹائپ انویرینٹس)
- SPARK میں کوئی واضح میموری مختص نہیں ہے۔
- ڈیٹرمنسٹک ٹاسکنگ اور شیڈولنگ
- اعلی سالمیت والے ریئل ٹائم سسٹمز کے لیے ریوینسکر پروفائل
- ٹول چین کی اہلیت (DO-178C برائے ایویونکس)
### Q5: میں Ada پروجیکٹ کیسے بناؤں؟
**A:** GPR پروجیکٹ فائلوں کے ساتھ GPRBuild استعمال کریں:
```bash
gprbuild -P my_project.gpr
gprclean -P my_project.gpr
```

---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ٹائپ سیف قطار کو لاگو کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
کمپائل ٹائم سائز چیکنگ کے ساتھ ایک پابند، دھاگے سے محفوظ قطار بنائیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
باؤنڈڈ بفر کے ساتھ ایک محفوظ آبجیکٹ استعمال کریں۔
**مرحلہ 3: نافذ کریں**```ada
protected type Bounded_Queue(Capacity : Positive := 100) is
   entry Enqueue(Item : Integer);
   entry Dequeue(Item : out Integer);
   function Count return Natural;
private
   Buffer : array(1 .. Capacity) of Integer;
   Head, Tail : Positive := 1;
   Size : Natural := 0;
end Bounded_Queue;

protected body Bounded_Queue is
   entry Enqueue(Item : Integer) when Size < Capacity is
   begin
      Buffer(Tail) := Item;
      Tail := (Tail mod Capacity) + 1;
      Size := Size + 1;
   end;

   entry Dequeue(Item : out Integer) when Size > 0 is
   begin
      Item := Buffer(Head);
      Head := (Head mod Capacity) + 1;
      Size := Size - 1;
   end;

   function Count return Natural is (Size);
end Bounded_Queue;
```

**مرحلہ 4: تصدیق کریں**
محفوظ آبجیکٹ باہمی اخراج کی ضمانت دیتا ہے۔ داخلے کی رکاوٹیں اوور فلو/زیر بہاؤ کو روکتی ہیں۔
### مسئلہ 2: معاہدہ کی بنیاد پر توثیق
**مرحلہ 1: مسئلہ کو سمجھیں**
رسمی معاہدوں کے ساتھ مربع جڑ کی تقریب کو نافذ کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
Ada 2012 کے معاہدوں کا استعمال کریں (پہلے/پوسٹ کنڈیشنز)۔
**مرحلہ 3: نافذ کریں**```ada
function Safe_Sqrt(X : Float) return Float
   with Pre  => X >= 0.0,
        Post => Safe_Sqrt'Result >= 0.0
              and then abs(Safe_Sqrt'Result**2 - X) < 0.001;

function Safe_Sqrt(X : Float) return Float is
begin
   return Float'Sqrt(X);
end Safe_Sqrt;
```

**مرحلہ 4: تصدیق کریں**
رن ٹائم چیکس (دعویٰ) خلاف ورزیوں کو پکڑتے ہیں۔ سپارک میں، یہ ثبوت کی ذمہ داریاں بن جاتی ہیں۔
---

## خلاصہ
اڈا ایک زبان ہے جو درستگی کے لیے بنائی گئی ہے۔ اس کا سخت قسم کا نظام، بلٹ ان کنکرنسی، اور باضابطہ تصدیق کی حمایت اسے ایسے نظاموں کے لیے انتخاب بناتی ہے جہاں ناکامی قابل قبول نہیں ہوتی۔ اگرچہ اس کی کمیونٹی مرکزی دھارے کی زبانوں کے مقابلے میں چھوٹی ہے، Ada ایوی ایشن، دفاع، خلائی اور دیگر حفاظتی اہم ڈومینز میں ضروری ہے۔ ان ایپلی کیشنز کے لیے، سافٹ ویئر انجینئرنگ کے لیے اڈا کا سخت نقطہ نظر کوئی حد نہیں ہے - یہ نقطہ ہے۔