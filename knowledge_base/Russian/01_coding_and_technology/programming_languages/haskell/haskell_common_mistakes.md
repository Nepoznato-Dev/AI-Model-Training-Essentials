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
# Haskell — распространенные ошибки и антишаблоны
В этом документе перечислены наиболее распространенные ошибки, ловушки и антишаблоны в Haskell с исправлениями.
---

## 1. Бесконечные списки и сюрпризы от лени
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

## 2. Частичные функции
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

## 3. Непонимание законов монады
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

## 4. Путаница с типом строк
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

## 5. Неправильное использование синтаксиса записи
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

## 6. Ввод-вывод в чистых функциях
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

## 7. Антипаттерн: злоупотребление `IO`
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

## Краткое содержание
Чистота и ленивость Haskell создают уникальные ловушки: утечки пространства из-за ленивых вычислений, частичные функции, которые аварийно завершают работу во время выполнения, путаница между String/Text/ByteString и чрезмерное использование ввода-вывода. Способ Haskell: используйте строгую оценку для аккумуляторов (`foldl'`, BangPatterns), избегайте частичных функций (`head`,`read`,`!!`), используйте`Maybe`/`Either`для обработки ошибок, используйте`Text`для текста и сохраняйте ввод-вывод. минимальный. Система типов компилятора — ваш главный союзник. Пусть она приведет вас к полным, чистым функциям.