<!--
---
# Metadata
title: "Ada — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, safe Ada code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [ada, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
#एडीए - मुहावरेदार पैटर्न और सर्वोत्तम अभ्यास
यह मार्गदर्शिका स्वच्छ, सुरक्षित एडीए कोड लिखने के लिए मुहावरेदार पैटर्न को कवर करती है।
---

## सुरक्षा टाइप करें
```ada
-- ✅ Strong typing with subtypes
type Age is range 0 .. 150;
type Percentage is delta 0.01 digits 5 range 0.0 .. 100.0;
type User_Id is new Integer range 1 .. Integer'Last;

-- ✅ Constrained types
type Name is new String (1 .. 64);
type Buffer_Size is range 1 .. 4096;

-- ✅ Enumerated types
type Color is (Red, Green, Blue);
type Status is (Active, Inactive, Pending);
```

---

## पैकेज और एनकैप्सुलेशन
```ada
-- ✅ Private types for encapsulation
package Users is
   type User is private;
   
   function Create (Name : String; Email : String) return User;
   function Get_Name (U : User) return String;
   function Get_Email (U : User) return String;
private
   type User is record
      Name  : String (1 .. 64);
      Email : String (1 .. 128);
   end record;
end Users;

-- ✅ Limited types (no assignment/copy)
type Connection is limited private;
```

---

## अनुबंध और दावे
```ada
-- ✅ Pre/postconditions
function Divide (A, B : Float) return Float
   with Pre  => B /= 0.0,
        Post => Divide'Result * B = A;

-- ✅ Assertions
pragma Assert (Index >= Low and Index <= High);

-- ✅ Type invariants
type Stack is record
   Data : array (1 .. 100) of Integer;
   Top  : Natural := 0;
end record
   with Type_Invariant => Stack.Top <= 100;
```

---

## सारांश
एडा मुहावरे जोर देते हैं: मजबूत टाइपिंग, एनकैप्सुलेशन के लिए निजी प्रकार, अनुबंध (पूर्व/बाद की शर्तें), और दावे। एडा स्टाइल गाइड का पालन करें, औपचारिक सत्यापन के लिए GNATprove का उपयोग करें। एडा सुरक्षा और शुद्धता को सर्वोपरि महत्व देता है।