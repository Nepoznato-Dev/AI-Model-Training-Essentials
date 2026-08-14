<!--
---
# Metadata
title: "Haskell — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Haskell with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [haskell, common-mistakes, anti-patterns, pitfalls, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# হাসকেল — সাধারণ ভুল এবং অ্যান্টি-প্যাটার্নস
এই নথিটি সংশোধন সহ Haskell-এ সবচেয়ে সাধারণ ভুল, ফাঁদ, এবং অ্যান্টি-প্যাটার্ন ক্যাটালগ করে।
---

## 1. অসীম তালিকা এবং অলসতা বিস্ময়
```haskell
-- ❌ WRONG — space leak from lazy accumulation
let nums = [1..1000000]
let doubled = map (*2) nums
let filtered = filter even doubled
-- All three lists exist in memory simultaneously!

-- ✅ CORRECT — use strict evaluation or streaming
import Data.List (foldl')
foldl' (+) 0 [1..1000000]  -- strict fold

-- ✅ CORRECT — use BangPatterns
{-# LANGUAGE BangPatterns #-}
sumStrict !acc [] = acc
sumStrict acc (x:xs) = sumStrict (acc + x) xs
```

---

## 2. আংশিক ফাংশন
```haskell
-- ❌ WRONG — crashes on empty list
firstElement :: [a] -> a
firstElement xs = head xs  -- runtime error on []

-- ✅ CORRECT — use Maybe
firstElement :: [a] -> Maybe a
firstElement [] = Nothing
firstElement (x:_) = Just x

-- ❌ WRONG — using `read` without validation
let x = read "not_a_number" :: Int  -- runtime error

-- ✅ CORRECT — use Text.Read.readMaybe
import Text.Read (readMaybe)
let x = readMaybe "42" :: Maybe Int  -- Just 42
let x = readMaybe "abc" :: Maybe Int  -- Nothing
```

---

## 3. মোনাড আইন না বোঝা
```haskell
-- ❌ WRONG — sequencing effects incorrectly
do
  x <- getLine
  return x
-- Same as just: getLine (violates left identity if not careful)

-- ✅ CORRECT — understand the three monad laws
-- 1. return a >>= f  ≡  f a          (left identity)
-- 2. m >>= return    ≡  m             (right identity)
-- 3. (m >>= f) >>= g ≡ m >>= (\x -> f x >>= g)  (associativity)
```

---

## 4. স্ট্রিং টাইপ কনফিউশন
```haskell
-- ❌ WRONG — using String ([Char]) for everything
-- Slow for concatenation, wrong for Unicode text
processText :: String -> String
processText = map toUpper

-- ✅ CORRECT — use Text for text, ByteString for binary
import qualified Data.Text as T
import qualified Data.Text.IO as TIO

processText :: T.Text -> T.Text
processText = T.toUpper
```

---

## 5. রেকর্ড সিনট্যাক্স সঠিকভাবে ব্যবহার না করা
```haskell
-- ❌ WRONG — positional access (fragile)
data Person = Person String Int String
getName (Person n _ _) = n

-- ✅ CORRECT — record syntax
data Person = Person
  { personName :: String
  , personAge :: Int
  , personEmail :: String
  }
getName :: Person -> String
getName = personName
```

---

## 6. বিশুদ্ধ ফাংশনে IO
```haskell
-- ❌ WRONG — trying to use IO in pure context
pureFunction :: Int -> Int
pureFunction x =
  let result = unsafePerformIO getLine  -- NEVER do this
  in x + read result

-- ✅ CORRECT — keep IO in IO monad
processInput :: IO ()
processInput = do
  line <- getLine
  let result = pureFunction (read line)
  print result

pureFunction :: Int -> Int
pureFunction x = x * 2
```

---

## 7. অ্যান্টি-প্যাটার্ন:`IO`অতিরিক্ত ব্যবহার করা
```haskell
-- ❌ WRONG — everything in IO
main :: IO ()
main = do
  x <- return 5
  y <- return 10
  let z = x + y
  print z

-- ✅ CORRECT — minimize IO, maximize pure code
main :: IO ()
main = do
  let z = computePurely 5 10
  print z

computePurely :: Int -> Int -> Int
computePurely x y = x + y
```

---

## সারাংশ
Haskell এর বিশুদ্ধতা এবং অলসতা অনন্য অসুবিধা তৈরি করে: অলস মূল্যায়ন থেকে স্থান ফাঁস, রানটাইমে ক্র্যাশ হওয়া আংশিক ফাংশন, স্ট্রিং/টেক্সট/বাইটস্ট্রিং-এর মধ্যে বিভ্রান্তি এবং আইও-এর অতিরিক্ত ব্যবহার। Haskell উপায় হল: সঞ্চয়কারীদের জন্য কঠোর মূল্যায়ন ব্যবহার করুন (`foldl'`, BangPatterns), আংশিক ফাংশনগুলি এড়িয়ে চলুন (`head`,`read`,`!!`),`Maybe`/`Maybe`/`Maybe`/ ত্রুটির জন্য ব্যবহার করুন পাঠ্যের জন্য `Text`, এবং IO ন্যূনতম রাখুন। কম্পাইলারের টাইপ সিস্টেম হল আপনার সর্বশ্রেষ্ঠ সহযোগী — এটি আপনাকে মোট, বিশুদ্ধ ফাংশনের দিকে নির্দেশনা দেয়।