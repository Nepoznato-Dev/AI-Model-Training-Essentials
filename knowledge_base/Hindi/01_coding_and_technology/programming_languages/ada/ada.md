---
# Metadata
title: "Ada"
description: "Comprehensive reference for the Ada programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

#अदा
Ada एक सांख्यिकीय रूप से टाइप की गई, संकलित प्रोग्रामिंग भाषा है जिसे सुरक्षा-महत्वपूर्ण और उच्च-अखंडता प्रणालियों के लिए डिज़ाइन किया गया है। मूल रूप से 1980 के दशक में अमेरिकी रक्षा विभाग (एडीए लवलेस के नाम पर, जिसे पहला कंप्यूटर प्रोग्रामर माना जाता है) के साथ अनुबंध के तहत विकसित किया गया, एडा विश्वसनीयता, रखरखाव और शुद्धता पर जोर देता है। इसे DoD द्वारा उपयोग की जाने वाली सैकड़ों प्रोग्रामिंग भाषाओं को एक एकल, अच्छी तरह से निर्दिष्ट भाषा से बदलने के लिए डिज़ाइन किया गया था।
एडीए का उपयोग विमानन (फ्लाई-बाय-वायर सिस्टम), अंतरिक्ष (ईएसए और नासा), रक्षा (मिसाइल मार्गदर्शन, रडार), रेल परिवहन और चिकित्सा उपकरणों में किया जाता है - जहां भी सॉफ्टवेयर विफलता से लोगों की जान जा सकती है।
---

## एडा क्यों मायने रखती है
- **सुरक्षा-महत्वपूर्ण सिस्टम**: उन सिस्टमों के लिए शुरू से ही डिज़ाइन किया गया है जहां विफलता कोई विकल्प नहीं है।
- **मजबूत टाइपिंग**: किसी भी मुख्यधारा की भाषा की सबसे सख्त प्रकार की प्रणाली - संकलन के समय त्रुटियों को पकड़ती है जो अन्य भाषाएँ चूक जाती हैं।
- **अंतर्निहित समवर्ती**: टास्किंग (समवर्ती प्रोग्रामिंग) भाषा का हिस्सा है, लाइब्रेरी का नहीं।
- **औपचारिक सत्यापन**: कार्यक्रम की शुद्धता साबित करने के लिए औपचारिक तरीकों का समर्थन करता है।
- **विश्वसनीयता विशेषताएं**: अंतर्निहित अपवाद, अनुबंध (पूर्व/बाद की शर्तें), और रनटाइम जांच।
- **आधुनिक Ada**: Ada 2012 और Ada 2022 ने सुरक्षा गारंटी बनाए रखते हुए आधुनिक सुविधाएँ जोड़ी हैं।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **आला समुदाय** | सी, जावा, या पायथन की तुलना में छोटा डेवलपर आधार | विशिष्ट लेकिन जानकार समुदाय |
| **वर्बोज़ सिंटैक्स** | सी या पायथन से अधिक वर्बोज़ | सुरक्षा-उन्मुख डिज़ाइन के भाग के रूप में स्वीकार करें |
| **सीमित पारिस्थितिकी तंत्र** | मुख्यधारा की भाषाओं की तुलना में कम पुस्तकालय | कस्टम कोड लिखें; व्यापक मानक पुस्तकालय का उपयोग करें |
| **सीखने की अवस्था** | कई सुरक्षा सुविधाओं के साथ जटिल भाषा | सुरक्षा-महत्वपूर्ण कार्य के लिए एडा के "स्पार्क" उपसमुच्चय से शुरुआत करें |
| **संकलक उपलब्धता** | कम कंपाइलर विकल्प (जीएनएटी मुख्य है) | GNAT निःशुल्क और सुव्यवस्थित है |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### टैग किए गए प्रकार और वंशानुक्रम (ओओपी)
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

### ऑपरेटर ओवरलोडिंग
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

### जेनरिक (संकलन-समय बहुरूपता)
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

### अनुबंध और पहलू (एडीए 2012)
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

## समवर्ती एवं समांतरता
### कार्य और मुलाकात
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

### संरक्षित वस्तुएं (थ्रेड-सुरक्षित साझा डेटा)
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

### समानांतर कंप्यूटिंग (एडीए 2022)
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### जीपीआर (जीएनएटी प्रोजेक्ट) फ़ाइलें
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

### परियोजना संरचना
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

### कमांड बनाएं
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

### GitHub क्रियाओं के साथ CI/CD
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

## परीक्षण
### एयूनिट परीक्षण ढांचा
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

## अंतरसंचालनीयता
### सी इंटरऑपरेबिलिटी (इंटरफ़ेस)
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

### मिश्रित भाषा प्रोग्रामिंग
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

## डिज़ाइन पैटर्न
### पैटर्न 1: संरक्षित वस्तुओं के साथ पर्यवेक्षक
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

### पैटर्न 2: भेदभावपूर्ण प्रकार वाली राज्य मशीन
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

### पैटर्न 3: नियंत्रित प्रकारों के साथ आरएआईआई
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
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

### कंपाइलर अनुकूलन
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

### शून्य-ओवरहेड अमूर्तन
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

## तैनाती
### सुरक्षा-महत्वपूर्ण प्रमाणन के लिए स्पार्क
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

### स्टैंडअलोन परिनियोजन
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

### एंबेडेड परिनियोजन
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

## एडा का उपयोग कब करें
| परिदृश्य | अदा क्यों | बेहतर विकल्प |
|---|---|-----|
| सुरक्षा-महत्वपूर्ण प्रणालियाँ | इसके लिए डिज़ाइन किया गया; औपचारिक सत्यापन समर्थन | — |
| विमानन/एयरोस्पेस | प्रमाणित संकलक; DO-178C अनुपालन | — |
| रक्षा प्रणालियाँ | डीओडी विरासत; सुरक्षा सुविधाएँ | — |
| रेलवे/चिकित्सा उपकरण | उच्च-अखंडता आवश्यकताएँ | — |
| सामान्य अनुप्रयोग विकास | गैर-महत्वपूर्ण प्रणालियों के लिए ओवरकिल | पायथन, जावा, गो |
| वेब विकास | अनुकूल नहीं | जावास्क्रिप्ट, पायथन |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: एडा का प्रकार सिस्टम संकलन समय पर बग को कैसे रोकता है?
**ए:** एडा की टाइप प्रणाली किसी भी भाषा की तुलना में सबसे सख्त है। यह उन त्रुटियों को पकड़ता है जो अन्य भाषाएँ चूक जाती हैं:
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

### Q2: एडा का टास्किंग मॉडल क्या है और इसकी तुलना अन्य समवर्ती मॉडल से कैसे की जाती है?
**ए:** एडा में संरक्षित वस्तुओं और कार्यों के साथ अंतर्निहित समवर्तीता है:
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

### Q3: मैं Ada में जेनरिक का उपयोग कैसे करूँ?
**ए:** एडा जेनेरिक स्पष्ट और प्रकार-सुरक्षित हैं:
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

### Q4: क्या बात Ada को सुरक्षा-महत्वपूर्ण प्रणालियों के लिए उपयुक्त बनाती है?
**ए:** एडा प्रदान करता है:
- औपचारिक सत्यापन के लिए स्पार्क उपसमुच्चय (शुद्धता का गणितीय प्रमाण)
- अनुबंध-आधारित प्रोग्रामिंग (पूर्व/उत्तर शर्ते, प्रकार अपरिवर्तनीय)
- स्पार्क में कोई अंतर्निहित मेमोरी आवंटन नहीं
- नियतात्मक कार्य और शेड्यूलिंग
- उच्च-अखंडता वास्तविक समय प्रणालियों के लिए रेवेन्सकर प्रोफ़ाइल
- टूलचेन योग्यता (एवियोनिक्स के लिए DO-178C)
### Q5: मैं Ada प्रोजेक्ट कैसे बनाऊं?
**ए:** जीपीआर प्रोजेक्ट फ़ाइलों के साथ जीपीआरबिल्ड का उपयोग करें:
```bash
gprbuild -P my_project.gpr
gprclean -P my_project.gpr
```

---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: एक प्रकार-सुरक्षित कतार लागू करना
**चरण 1: समस्या को समझें**
संकलन-समय आकार जांच के साथ एक सीमित, थ्रेड-सुरक्षित कतार बनाएं।
**चरण 2: दृष्टिकोण को पहचानें**
बाउंड बफ़र के साथ संरक्षित ऑब्जेक्ट का उपयोग करें।
**चरण 3: कार्यान्वयन**```ada
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

**चरण 4: सत्यापित करें**
संरक्षित वस्तु पारस्परिक बहिष्कार की गारंटी देती है। प्रवेश बाधाएं अतिप्रवाह/अंडरफ्लो को रोकती हैं।
### समस्या 2: अनुबंध-आधारित सत्यापन
**चरण 1: समस्या को समझें**
औपचारिक अनुबंधों के साथ वर्गमूल फ़ंक्शन लागू करें।
**चरण 2: दृष्टिकोण को पहचानें**
Ada 2012 अनुबंधों (पूर्व/बाद की शर्तों) का उपयोग करें।
**चरण 3: कार्यान्वयन**```ada
function Safe_Sqrt(X : Float) return Float
   with Pre  => X >= 0.0,
        Post => Safe_Sqrt'Result >= 0.0
              and then abs(Safe_Sqrt'Result**2 - X) < 0.001;

function Safe_Sqrt(X : Float) return Float is
begin
   return Float'Sqrt(X);
end Safe_Sqrt;
```

**चरण 4: सत्यापित करें**
रनटाइम जांच (दावा) उल्लंघन पकड़ती है। स्पार्क में, ये प्रमाण दायित्व बन जाते हैं।
---

## सारांश
एडा शुद्धता के लिए बनाई गई भाषा है। इसकी सख्त प्रकार की प्रणाली, अंतर्निहित समवर्तीता और औपचारिक सत्यापन समर्थन इसे उन प्रणालियों के लिए विकल्प बनाता है जहां विफलता स्वीकार्य नहीं है। हालाँकि इसका समुदाय मुख्यधारा की भाषाओं की तुलना में छोटा है, फिर भी Ada विमानन, रक्षा, अंतरिक्ष और अन्य सुरक्षा-महत्वपूर्ण क्षेत्रों में आवश्यक बना हुआ है। इन अनुप्रयोगों के लिए, सॉफ़्टवेयर इंजीनियरिंग के प्रति Ada का कठोर दृष्टिकोण कोई सीमा नहीं है - यही बात है।