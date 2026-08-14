<!--
---
# Metadata
title: "Haskell — Version History & Evolution"
description: "Comprehensive version history and evolution of Haskell from Haskell 1.0 to modern Haskell."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [haskell, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# हास्केल - संस्करण इतिहास और विकास
## समयरेखा
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| हास्केल 1.0 | 1990 | प्रारंभिक रिलीज़ (समिति प्रयास) |
| हास्केल 1.2 | 1992 | वस्तु प्रणाली प्रयोग |
| हास्केल 1.3 | 1996 | प्रकार की कक्षाएं शुरू की गईं |
| हास्केल 1.4 | 1997 | `IO`मोनड ने स्पष्ट किया |
| हास्केल 98 | 1998 | **पहला स्थिर मानक** |
| हास्केल 2010 | 2010 | **संशोधित मानक**, कैबल, मॉड्यूल |
| जीएचसी 7.0 | 2011 | परिवार प्रकार, डेटा प्रकार |
| जीएचसी 7.4 | 2012 | आवेदक-मोनाड प्रस्ताव शुरू होता है |
| जीएचसी 7.6 | 2013 | प्रकार परिवारों में सुधार |
| जीएचसी 7.8 | 2014 | पैटर्न समानार्थक शब्द,`NegativeLiterals`|
| जीएचसी 7.10 | 2015 | **आवेदक-मोनाड प्रस्ताव (एएमपी)**,`-XStrict`|
| जीएचसी 8.0 | 2016 | **प्रकारअनुप्रयोग**, `MonadFail`, कस्टम प्रकार की त्रुटियाँ |
| जीएचसी 8.2 | 2017 | अनबॉक्स्ड रकम, बैकपैक (मॉड्यूल सिस्टम) |
| जीएचसी 8.4 | 2018 | सार आधार पथ,`Semigroup`>>`Monoid`|
| जीएचसी 8.6 | 2018 | StarIsType,`DerivingVia`|
| जीएचसी 8.8 | 2019 | प्रस्तावना में मोनाडफेल |
| जीएचसी 8.10 | 2020 | एकीकृत`do`संकेतन, प्रकार बहुरूपता |
| जीएचसी 9.0 | 2021 | **लेविटी बहुरूपता**, रैखिक प्रकार |
| जीएचसी 9.2 | 2022 | योग्य `do`, त्रुटि संदेशों में सुधार |
| जीएचसी 9.4 | 2022 | **GHC2021** भाषा विस्तार सेट,`OverloadedRecordDot`|
| जीएचसी 9.6 | 2023 | आवश्यक प्रकार के तर्क,`TypeAbstractions`|
| जीएचसी 9.8 | 2024 | `TypeAbstractions`स्थिर, बेहतर त्रुटि संदेश |
| जीएचसी 9.10 | 2024 | आगे परिशोधन, प्रदर्शन |
| जीएचसी 9.12 | 2025 | निरंतर विकास |
## प्रमुख मील के पत्थर
### हास्केल 1.x - समिति वर्ष (1990-1998)
- **1990**: हास्केल 1.0 — समिति द्वारा डिज़ाइन की गई आलसी कार्यात्मक भाषा
- **1.3 (1996)**: प्रकार वर्ग - हास्केल की परिभाषित विशेषता
- **1.4 (1997)**:`IO`मोनैड ने स्पष्ट किया - साइड इफेक्ट्स को पूरी तरह से कैसे संभालें
- **हास्केल 98**: पहला स्थिर मानक; आज भी संदर्भित है
### हास्केल 2010 - आधुनिक मानक
- **2010**: संशोधित मानक - कैबल (पैकेज सिस्टम), मॉड्यूल सिस्टम में सुधार
- जीएचसी वास्तविक संकलक बन जाता है
- कैबल + हैकेज = हास्केल का पैकेज इकोसिस्टम
### जीएचसी 7.x — टाइप सिस्टम पावर (2011-2015)
- प्रकार परिवार, डेटा प्रकार, प्रकार बहुरूपता
- एप्लिकेटिव-मोनैड प्रस्ताव (एएमपी) - प्रकार वर्ग पदानुक्रम को ठीक करना
- पैटर्न पर्यायवाची,`Strict`एक्सटेंशन
### जीएचसी 8.x — मॉडर्न हास्केल (2016-2020)
-`TypeApplications`- कॉल साइटों पर स्पष्ट प्रकार के तर्क
- कस्टम प्रकार की त्रुटियाँ - बेहतर संकलक संदेश
- बैकपैक - घटक-आधारित डिज़ाइन के लिए मॉड्यूल सिस्टम
-`DerivingVia`- लचीली व्युत्पन्न रणनीतियाँ
### GHC 9.x — प्रयोज्य क्रांति (2021–वर्तमान)
- **9.0**: लेविटी बहुरूपता, रैखिक प्रकार (संसाधन सुरक्षा)
- **9.2**: योग्य `do`, बेहतर त्रुटि संदेश
- **9.4**: **जीएचसी2021** — आधुनिक डिफ़ॉल्ट एक्सटेंशन; `OverloadedRecordDot`(`.` के साथ फ़ील्ड एक्सेस)
- **9.6**: आवश्यक प्रकार के तर्क,`TypeAbstractions`
- **9.8–9.12**: त्रुटि संदेश में निरंतर सुधार, प्रदर्शन
## सिंटेक्स इवोल्यूशन
```haskell
-- Haskell 98: Basic type classes
class Eq a where
  (==) :: a -> a -> Bool

-- GHC extensions: Type applications (GHC 8.0)
-- Before:
read "[1,2,3]" :: [Int]
-- After:
read @[Int] "[1,2,3]"

-- GHC 9.4: OverloadedRecordDot
-- Before:
name (getPerson user)
-- After:
user.person.name

-- GHC 9.0: Linear types
-- Before:
processFile :: FilePath -> IO Result
-- After:
processFile :: FilePath %1 -> IO Result  -- file handle used exactly once

-- GHC 8.0: Custom type errors
type family ErrorMessage (a :: Type) :: ErrorMessage where
  ErrorMessage (NotSerializable a) =
    'Text "Cannot serialize type " ':<>: 'ShowType a
```

## टाइप सिस्टम इवोल्यूशन
```
Haskell 1.0:  Basic types, algebraic data types, pattern matching
Haskell 1.3:  Type classes
Haskell 98:   Multi-parameter type classes, functional dependencies
GHC 6.x:     GADTs, type families, rank-N types
GHC 7.0:     Data kinds, kind polymorphism
GHC 7.10:    Applicative-Monad Proposal
GHC 8.0:     TypeApplications, custom type errors
GHC 8.2:     Unboxed sums
GHC 9.0:     Levity polymorphism, linear types
GHC 9.4:     OverloadedRecordDot, GHC2021
GHC 9.6:     Required type arguments, TypeAbstractions
```

## समवर्ती एवं समांतरता
```
Haskell 98:  No standard concurrency model
2004: GHC 6.2 — Software Transactional Memory (STM)
2007: GHC 6.8 — lightweight threads (green threads)
2011: async library — structured concurrency
2018: io-streams, conduit — streaming I/O
2021: Linear types — resource-safe concurrency
2025: GHC + effect systems (Effectful, UnliftIO)
```

## मुख्य डिज़ाइन सिद्धांत
```
1. "Lazy by default" — non-strict evaluation
2. "Pure by default" — side effects explicit via monads
3. "Types are truth" — strong static typing
4. "Referential transparency" — same input → same output
5. "Composability" — small building blocks, compose freely
6. "Make illegal states unrepresentable" — type system as design tool
```

## पारिस्थितिकी तंत्र का विकास
```
1990: Haskell 1.0 — academic curiosity
1998: Haskell 98 — stable standard
2007: Cabal + Hackage — package ecosystem
2010: Haskell 2010 — revised standard
2012: Stack build tool — reproducible builds
2015: Haskell in industry — Facebook, Standard Chartered, Well-Typed
2021: GHC 9.0 — levity polymorphism, linear types
2023: GHC 9.6 — type abstractions
2025: Haskell used in finance, compilers, formal verification,
       blockchain (Cardano), and academic research
       GHC, Stack, Cabal; key libraries: lens, aeson, servant, yesod
```
