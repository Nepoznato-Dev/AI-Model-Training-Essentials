<!--
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

-->
#আদা
Ada হল একটি স্ট্যাটিকলি টাইপ করা, সংকলিত প্রোগ্রামিং ভাষা যা নিরাপত্তা-সমালোচনামূলক এবং উচ্চ-অখণ্ডতা সিস্টেমের জন্য ডিজাইন করা হয়েছে। মূলত 1980 এর দশকে মার্কিন প্রতিরক্ষা বিভাগের সাথে চুক্তির অধীনে বিকশিত হয়েছিল (এডা লাভলেসের নামে নামকরণ করা হয়েছে, প্রথম কম্পিউটার প্রোগ্রামার হিসাবে বিবেচিত), অ্যাডা নির্ভরযোগ্যতা, রক্ষণাবেক্ষণযোগ্যতা এবং সঠিকতার উপর জোর দেয়। এটি একটি একক, সুনির্দিষ্ট ভাষা দিয়ে DoD দ্বারা ব্যবহৃত শত শত প্রোগ্রামিং ভাষা প্রতিস্থাপন করার জন্য ডিজাইন করা হয়েছিল।
Ada বিমান চালনা (ফ্লাই-বাই-ওয়্যার সিস্টেম), স্পেস (ESA এবং NASA), প্রতিরক্ষা (ক্ষেপণাস্ত্র নির্দেশিকা, রাডার), রেল পরিবহন, এবং চিকিৎসা ডিভাইসে ব্যবহৃত হয় — যেখানে সফ্টওয়্যার ব্যর্থতার কারণে জীবন ব্যয় হতে পারে।
---

## কেন অ্যাডা ম্যাটারস
- **নিরাপত্তা-সমালোচনামূলক সিস্টেম**: এমন সিস্টেমের জন্য গ্রাউন্ড আপ থেকে ডিজাইন করা হয়েছে যেখানে ব্যর্থতা একটি বিকল্প নয়।
- **শক্তিশালী টাইপিং**: যেকোন মূলধারার ভাষার সবচেয়ে কঠোর টাইপ সিস্টেম — কম্পাইলের সময় ত্রুটি ধরা দেয় যা অন্যান্য ভাষা মিস করে।
- **বিল্ট-ইন কনকারেন্সি**: টাস্কিং (সমসাময়িক প্রোগ্রামিং) ভাষার অংশ, লাইব্রেরি নয়।
- **আনুষ্ঠানিক যাচাই**: প্রোগ্রামের সঠিকতা প্রমাণ করার জন্য আনুষ্ঠানিক পদ্ধতি সমর্থন করে।
- **নির্ভরযোগ্যতা বৈশিষ্ট্য**: অন্তর্নির্মিত ব্যতিক্রম, চুক্তি (পূর্ব/পরবর্তী শর্তাবলী), এবং রানটাইম চেক।
- **আধুনিক Ada**: Ada 2012 এবং Ada 2022 নিরাপত্তার নিশ্চয়তা বজায় রেখে আধুনিক বৈশিষ্ট্য যুক্ত করেছে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **কুলুঙ্গি সম্প্রদায়** | C, Java, বা Python | এর তুলনায় ছোট ডেভেলপার বেস বিশেষায়িত কিন্তু জ্ঞানী সম্প্রদায় |
| **ভার্বোস সিনট্যাক্স** | সি বা পাইথনের চেয়ে বেশি শব্দ সুরক্ষা-ভিত্তিক নকশার অংশ হিসাবে গ্রহণ করুন |
| **সীমিত ইকোসিস্টেম** | মূলধারার ভাষার তুলনায় কম লাইব্রেরি | কাস্টম কোড লিখুন; ব্যাপক স্ট্যান্ডার্ড লাইব্রেরি ব্যবহার করুন |
| **লার্নিং কার্ভ** | অনেক নিরাপত্তা বৈশিষ্ট্য সহ জটিল ভাষা | নিরাপত্তা-গুরুত্বপূর্ণ কাজের জন্য Ada এর "SPARK" উপসেট দিয়ে শুরু করুন |
| **কম্পাইলার উপলব্ধতা** | কম কম্পাইলার বিকল্প (GNAT হল প্রধান) | GNAT বিনামূল্যে এবং ভালভাবে রক্ষণাবেক্ষণ করা হয় |
---

## সিনট্যাক্স মৌলিক
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### ট্যাগড টাইপস এবং ইনহেরিটেন্স (OOP)
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

### অপারেটর ওভারলোডিং
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

### জেনেরিক (কম্পাইল-টাইম পলিমরফিজম)
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

### চুক্তি এবং দিক (Ada 2012)
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

## সামঞ্জস্য এবং সমান্তরালতা
### টাস্ক এবং মিলন
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

### সুরক্ষিত বস্তু (থ্রেড-নিরাপদ শেয়ার করা ডেটা)
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

### সমান্তরাল কম্পিউটিং (Ada 2022)
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### GPR (GNAT প্রকল্প) ফাইল
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

### প্রকল্পের কাঠামো
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

### কমান্ড তৈরি করুন
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

### গিটহাব অ্যাকশন সহ CI/CD
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

## পরীক্ষা
### AUnit টেস্টিং ফ্রেমওয়ার্ক
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

## ইন্টারঅপারেবিলিটি
### সি ইন্টারঅপারেবিলিটি (ইন্টারফেস)
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

### মিশ্র-ভাষা প্রোগ্রামিং
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: সুরক্ষিত বস্তু সহ পর্যবেক্ষক
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

### প্যাটার্ন 2: বৈষম্যমূলক প্রকারের সাথে স্টেট মেশিন
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

### প্যাটার্ন 3: নিয়ন্ত্রিত প্রকার সহ RAII
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
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

### কম্পাইলার অপ্টিমাইজেশান
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

### জিরো-ওভারহেড অ্যাবস্ট্রাকশন
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

## স্থাপনা
### নিরাপত্তা-গুরুত্বপূর্ণ শংসাপত্রের জন্য স্পার্ক
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

### স্বতন্ত্র স্থাপনা
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

### এমবেডেড স্থাপনা
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

## কখন অ্যাডা ব্যবহার করবেন
| দৃশ্যকল্প | কেন অ্যাডা | ভাল বিকল্প |
|------------|---------|---------|
| নিরাপত্তা-সমালোচনা ব্যবস্থা | এই জন্য ডিজাইন; আনুষ্ঠানিক যাচাই সমর্থন | — |
| বিমান চলাচল / মহাকাশ | প্রত্যয়িত কম্পাইলার; DO-178C সম্মতি | — |
| প্রতিরক্ষা ব্যবস্থা | DoD ঐতিহ্য; নিরাপত্তা বৈশিষ্ট্য | — |
| রেলওয়ে / চিকিৎসা ডিভাইস | উচ্চ-সততার প্রয়োজনীয়তা | — |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | অ-গুরুত্বপূর্ণ সিস্টেমের জন্য ওভারকিল | Python, Java, Go |
| ওয়েব ডেভেলপমেন্ট | উপযুক্ত নয় | জাভাস্ক্রিপ্ট, পাইথন |
| ডেটা সায়েন্স / এমএল | বাস্তুতন্ত্র নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: Ada এর টাইপ সিস্টেম কিভাবে কম্পাইলের সময় বাগ প্রতিরোধ করে?
**A:** Ada এর টাইপ সিস্টেম যেকোনো ভাষার মধ্যে সবচেয়ে কঠোর। এটি অন্য ভাষাগুলি মিস করে এমন ত্রুটিগুলি ধরে:
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

### প্রশ্ন 2: অ্যাডা-এর টাস্কিং মডেল কী এবং এটি অন্যান্য কনকারেন্সি মডেলের সাথে কীভাবে তুলনা করে?
**A:** Ada সুরক্ষিত বস্তু এবং কাজগুলির সাথে অন্তর্নির্মিত একযোগে রয়েছে:
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

### প্রশ্ন 3: আমি কীভাবে অ্যাডা-এ জেনেরিক ব্যবহার করব?
**A:** অ্যাডা জেনেরিকগুলি স্পষ্ট এবং টাইপ-নিরাপদ:
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

### প্রশ্ন 4: কী Ada-কে নিরাপত্তা-সমালোচনামূলক সিস্টেমের জন্য উপযুক্ত করে তোলে?
**A:** Ada প্রদান করে:
- আনুষ্ঠানিক যাচাইয়ের জন্য স্পার্ক উপসেট (শুদ্ধতার গাণিতিক প্রমাণ)
- চুক্তি ভিত্তিক প্রোগ্রামিং (প্রাক/পরবর্তী শর্তাবলী, প্রকার পরিবর্তন)
- স্পার্ক-এ কোনো অন্তর্নিহিত মেমরি বরাদ্দ নেই
- নির্ধারক টাস্কিং এবং সময়সূচী
- উচ্চ-সততা রিয়েল-টাইম সিস্টেমের জন্য Ravenscar প্রোফাইল
- টুলচেন যোগ্যতা (এভিওনিক্সের জন্য DO-178C)
### প্রশ্ন 5: আমি কীভাবে অ্যাডা প্রকল্পগুলি তৈরি করব?
**A:** GPR প্রকল্প ফাইলের সাথে GPRBuild ব্যবহার করুন:
```bash
gprbuild -P my_project.gpr
gprclean -P my_project.gpr
```

---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: একটি টাইপ-সেফ কিউ বাস্তবায়ন করা
**ধাপ 1: সমস্যাটি বুঝুন**
কম্পাইল-টাইম সাইজ চেকিং সহ একটি আবদ্ধ, থ্রেড-নিরাপদ সারি তৈরি করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
একটি আবদ্ধ বাফার সহ একটি সুরক্ষিত বস্তু ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```ada
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

**পদক্ষেপ 4: যাচাই করুন**
সুরক্ষিত বস্তু পারস্পরিক বর্জনের গ্যারান্টি দেয়। প্রবেশের বাধাগুলি ওভারফ্লো/আন্ডারফ্লো প্রতিরোধ করে।
### সমস্যা 2: চুক্তি ভিত্তিক বৈধতা
**ধাপ 1: সমস্যাটি বুঝুন**
আনুষ্ঠানিক চুক্তির সাথে একটি বর্গমূল ফাংশন প্রয়োগ করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
Ada 2012 চুক্তি ব্যবহার করুন (পূর্ব/পরবর্তী শর্তাবলী)।
**ধাপ 3: প্রয়োগ করুন**```ada
function Safe_Sqrt(X : Float) return Float
   with Pre  => X >= 0.0,
        Post => Safe_Sqrt'Result >= 0.0
              and then abs(Safe_Sqrt'Result**2 - X) < 0.001;

function Safe_Sqrt(X : Float) return Float is
begin
   return Float'Sqrt(X);
end Safe_Sqrt;
```

**পদক্ষেপ 4: যাচাই করুন**
রানটাইম চেক (আবেদন) লঙ্ঘন ধরা. স্পার্ক-এ, এগুলো প্রমাণের বাধ্যবাধকতা হয়ে যায়।
---

## সারাংশ
অ্যাডা হল সঠিকতার জন্য নির্মিত একটি ভাষা। এর কঠোর টাইপ সিস্টেম, বিল্ট-ইন কনকারেন্সি, এবং আনুষ্ঠানিক যাচাই সমর্থন এটিকে এমন সিস্টেমের জন্য পছন্দ করে যেখানে ব্যর্থতা গ্রহণযোগ্য নয়। যদিও এর সম্প্রদায়টি মূলধারার ভাষার তুলনায় ছোট, তবে বিমান চলাচল, প্রতিরক্ষা, স্থান এবং অন্যান্য নিরাপত্তা-সমালোচনামূলক ডোমেনে অ্যাডা অপরিহার্য। এই অ্যাপ্লিকেশনগুলির জন্য, সফ্টওয়্যার প্রকৌশলে অ্যাডা-এর কঠোর পদ্ধতির কোনও সীমাবদ্ধতা নয় - এটিই মূল বিষয়।