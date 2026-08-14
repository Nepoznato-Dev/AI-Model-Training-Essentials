---
# Metadata
title: "Ada — Cheat Sheet"
description: "Quick-reference cheat sheet for Ada syntax, types, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [ada, safety-critical, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# اڈا - دھوکہ دہی کی شیٹ
## بنیادی باتیں
```ada
-- Variables
Name : constant String := "Alice";
Age  : Integer := 30;
Pi   : constant Float := 3.14159;
Active : Boolean := True;

-- Type declarations
type Day_Type is (Mon, Tue, Wed, Thu, Fri, Sat, Sun);
type Temperature is range -273 .. 1000;
type Percentage is delta 0.01 range 0.0 .. 100.0;

-- Subtypes
subtype Natural is Integer range 0 .. Integer'Last;
subtype Positive is Integer range 1 .. Integer'Last;
subtype Short_String is String (1 .. 80);

-- String operations
Name'Length                    -- 5
Name (1 .. 3)                  -- "Ali"
Name & " Smith"                -- concatenation
Ada.Strings.Fixed.Index (Name, "lic")
Ada.Strings.Fixed.Trim (Name, Ada.Strings.Both)
Ada.Strings.Unbounded.To_Unbounded_String ("hello")
```

## اقسام اور ریکارڈز
```ada
-- Record
type Point is record
    X : Float;
    Y : Float;
end record;

P : Point := (X => 1.0, Y => 2.0);
P.X := 3.0;

-- Tagged type (class)
type Animal is tagged record
    Name : Unbounded_String;
end record;

type Dog is new Animal with record
    Breed : Unbounded_String;
end record;

-- Variant record
type Shape_Kind is (Circle, Rectangle);
type Shape (Kind : Shape_Kind) is record
    case Kind is
        when Circle =>
            Radius : Float;
        when Rectangle =>
            Width, Height : Float;
    end case;
end record;

-- Access type (pointer)
type Node;
type Node_Ptr is access Node;
type Node is record
    Value : Integer;
    Next  : Node_Ptr;
end record;

-- Array type
type Vector is array (Positive range <>) of Float;
V : Vector (1 .. 10);
```

## کنٹرول فلو
```ada
-- If
if Condition then
    Do_Something;
elsif Other then
    Do_Other;
else
    Do_Default;
end if;

-- Case
case Day is
    when Mon .. Fri => Put_Line ("Weekday");
    when Sat | Sun  => Put_Line ("Weekend");
end case;

-- Case expression
Label : constant String :=
    (case Status is
        when Active   => "Active",
        when Inactive => "Inactive");

-- Loops
for I in 1 .. 10 loop
    Put (Integer'Image (I));
end loop;

for Item of Collection loop
    Process (Item);
end loop;

while Condition loop
    Do_Something;
end loop;

loop
    Do_Something;
    exit when Done;
end loop;

-- For with reverse
for I in reverse 1 .. 10 loop
    Put (Integer'Image (I));
end loop;
```

## ذیلی پروگرام
```ada
-- Procedure
procedure Greet (Name : in String;
                 Greeting : in String := "Hello") is
begin
    Put_Line (Greeting & ", " & Name & "!");
end Greet;

Greet ("Alice");
Greet ("Alice", "Hi");

-- Function
function Add (A, B : Integer) return Integer is
begin
    return A + B;
end Add;

-- Function with pre/postconditions
function Divide (A, B : Float) return Float
    with Pre  => B /= 0.0,
         Post => Divide'Result * B = A;

-- Generic
generic
    type Element_Type is private;
package Stack_Pkg is
    procedure Push (Item : Element_Type);
    function Pop return Element_Type;
    function Is_Empty return Boolean;
end Stack_Pkg;

-- Instantiation
package Int_Stack is new Stack_Pkg (Integer);
```

## پیکیجز اور او او پی
```ada
-- Package spec
package Shapes is
    type Shape is tagged private;
    procedure Set_Name (S : in out Shape; Name : String);
    function Get_Name (S : Shape) return String;
    function Area (S : Shape) return Float is abstract;
private
    type Shape is tagged record
        Name : Unbounded_String;
    end record;
end Shapes;

-- Dispatching
procedure Print_Area (S : Shape'Class) is
begin
    Put_Line (Float'Image (S.Area));
end Print_Area;

-- Exception handling
begin
    Risky_Operation;
exception
    when Constraint_Error =>
        Put_Line ("Constraint violated");
    when others =>
        Put_Line ("Unknown error");
end;
```

## معاہدے اور عمل
```ada
-- Pre/postconditions
function Sqrt (X : Float) return Float
    with Pre  => X >= 0.0,
         Post => Sqrt'Result >= 0.0;

-- Type invariants
type Bounded_Buffer is record
    Data : array (1 .. 100) of Integer;
    Count : Natural;
end record
    with Type_Invariant => Bounded_Buffer.Count <= 100;

-- Pragmas
pragma Assert (X > 0, "X must be positive");
pragma Preelaborate;
pragma Pure;
```
