---
# Metadata
title: "Ada — Version History & Evolution"
description: "Comprehensive version history and evolution of Ada from Ada 83 to modern Ada."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [ada, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# एडा - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| अदा 83 | 1983 | **प्रथम मानक** (MIL-STD-1815A) - एडा लवलेस के नाम पर |
| अदा 87 | 1987 | मामूली संशोधन (सटीकता, पहुंच नियम) |
| अदा 95 | 1995 | **प्रमुख**: ओओपी (टैग किए गए प्रकार), संरक्षित वस्तुएं, कार्य सुधार |
| एडा 2005 | 2005 | **इंटरफ़ेस**, अनाम एक्सेस प्रकार,`for`/`while`लूप सुधार |
| एडा 2012 | 2012 | **पहलू-उन्मुख प्रोग्रामिंग**, अनुबंध (पूर्व/बाद की शर्तें),`iterator`|
| एडा 2022 | 2022 | **`with ghost`**, समानांतर निर्माण, वास्तविक समय में सुधार |
## प्रमुख मील के पत्थर
### अदा 83 - द बर्थ (1983)
- **1983**: अमेरिकी रक्षा विभाग एम्बेडेड सिस्टम के लिए एक ही भाषा को अनिवार्य बनाता है
- जीन इचिबिया सीआईआई हनीवेल बुल (फ्रांस) में डिजाइन का नेतृत्व करते हैं।
- इसका नाम एडा लवलेस के नाम पर रखा गया - पहली कंप्यूटर प्रोग्रामर
- मुख्य विशेषताएं: मजबूत टाइपिंग, पैकेज, कार्य (संगामिति), जेनेरिक, अपवाद
- **लक्ष्य**: सुरक्षा-महत्वपूर्ण प्रणालियाँ - विमानन, रक्षा, अंतरिक्ष
### एडा 95 - ऑब्जेक्ट-ओरिएंटेड एडा (1995)
- **पहली आईएसओ-मानकीकृत OO भाषा** (जावा मानकीकृत होने से पहले)
- टैग किए गए प्रकार (वर्ग), वर्ग-व्यापी प्रकार, गतिशील प्रेषण
- संरक्षित वस्तुएं (सुरक्षित समवर्ती डेटा पहुंच)
- चाइल्ड पैकेज (पदानुक्रमित लाइब्रेरी)
- प्राग्मा-आधारित विन्यास
### एडा 2005 - रिफाइनमेंट्स (2005)
- इंटरफ़ेस (इंटरफ़ेस के एकाधिक वंशानुक्रम)
- अनाम पहुंच प्रकार (सरलीकृत सूचक)
-`for`लूप सुधार
- कंटेनर लाइब्रेरी (दोगुनी-लिंक की गई सूचियाँ, वैक्टर, मानचित्र)
- विस्तारित`return`कथन
### एडीए 2012 - अनुबंध और पहलू (2012)
- **पहलू-उन्मुख प्रोग्रामिंग**: घोषणाओं से जुड़े`aspect`खंड
- **अनुबंध**:`Pre`,`Post`,`Type_Invariant`- औपचारिक सत्यापन अंतर्निहित
- इटरेटर समर्थन (`for X of Container loop`)
-`overriding`संकेतक
- अभिव्यक्ति कार्य: `function F(X: Integer) return Integer is (X * 2);`
### एडा 2022 - पैरेलल एंड घोस्ट (2022)
- **`with ghost`**: सत्यापन के लिए भूत कोड (उत्पादन में संकलित)
- **समानांतर निर्माण**:`parallel`लूप,`parallel`ब्लॉक
- वास्तविक समय में सुधार
- कंटेनर सुधार
-`Iterator`पहलू परिशोधन
## सिंटेक्स इवोल्यूशन
```ada
-- Ada 83: Package-based design
package Stack is
   procedure Push(Item : in Integer);
   function Pop return Integer;
   Stack_Empty : exception;
end Stack;

package body Stack is
   Max : constant := 100;
   Data : array(1..Max) of Integer;
   Top : Integer range 0..Max := 0;

   procedure Push(Item : in Integer) is
   begin
      Top := Top + 1;
      Data(Top) := Item;
   end Push;

   function Pop return Integer is
      Result : Integer;
   begin
      if Top = 0 then raise Stack_Empty; end if;
      Result := Data(Top);
      Top := Top - 1;
      return Result;
   end Pop;
end Stack;

-- Ada 95: Object-oriented
type Shape is tagged record
   X, Y : Float;
end record;

function Area(S : Shape) return Float is
begin
   return 0.0;
end Area;

type Circle is new Shape with record
   Radius : Float;
end record;

function Area(C : Circle) return Float is
begin
   return 3.14159 * C.Radius ** 2;
end Area;

-- Ada 2012: Contracts and aspects
type Temperature is new Float
   with Dynamic_Predicate => Temperature >= -273.15;

procedure Set_Temp(T : in out Temperature)
   with Pre  => T >= -273.15,
        Post => T'Old < T;  -- temperature must increase

-- Expression functions (Ada 2012)
function Double(X : Integer) return Integer is (X * 2);

-- Ada 2022: Parallel constructs
parallel
   for I in Data'Range loop
      Data(I) := Compute(I);
   end loop;

-- Ada 2022: Ghost code for verification
procedure Process(X : in out Integer)
   with Ghost => True,
        Pre   => X > 0,
        Post  => X > X'Old;
```

## फ़ीचर इवोल्यूशन
```
Ada 83:   Packages, strong typing, tasks, generics, exceptions
Ada 95:   Tagged types (OOP), protected objects, child packages
Ada 2005: Interfaces, anonymous access, containers
Ada 2012: Aspects, contracts (Pre/Post), iterators, expression functions
Ada 2022: Ghost code, parallel constructs, real-time improvements
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Reliability first" — designed for safety-critical systems
2. "Strong typing" — catch errors at compile time
3. "Readability" — verbose but clear syntax
4. "Concurrency-safe" — protected objects, rendezvous, parallel
5. "Verifiable" — contracts, aspects, ghost code
6. "No hidden costs" — what you see is what you get (no GC required)
```

## पारिस्थितिकी तंत्र का विकास
```
1983: Ada 83 — DoD mandate, defense/aviation adoption
1987: Ada 87 — minor fixes
1995: Ada 95 — OOP, ISO standard
1995: GNAT (GNU NYU Ada Translator) — open source compiler
2005: Ada 2005 — interfaces, containers
2012: Ada 2012 — contracts, aspects
2015: SPARK 2014 — formal verification for Ada
2022: Ada 2022 — parallel, ghost code
2025: Ada used in: aviation (DO-178C), space (ESA), rail, defense
       Compilers: GNAT (open source), ObjectAda, AdaCore tools
       SPARK subset used for formal verification of critical code
```
