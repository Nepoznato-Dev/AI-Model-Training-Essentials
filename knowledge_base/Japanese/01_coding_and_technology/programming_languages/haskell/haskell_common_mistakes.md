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
# Haskell — よくある間違いとアンチパターン
このドキュメントには、Haskell で最も一般的な間違い、罠、アンチパターンが修正付きでカタログ化されています。
---

## 1. 無限リストと怠惰の驚き
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

## 2. 部分的な関数
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

## 3. モナドの法則を理解していない
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

## 4. 文字列型の混乱
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

## 5. レコード構文が適切に使用されていない
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

## 6. 純粋関数における IO
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

## 7. アンチパターン:`IO`の使いすぎ
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

＃＃ まとめ
Haskell の純粋さと遅延は、遅延評価によるスペース リーク、実行時にクラッシュする部分関数、String/Text/ByteString 間の混乱、IO の過剰使用など、独特の落とし穴を生み出します。 Haskell の方法は次のとおりです。アキュムレータに厳密な評価を使用し (`foldl'`、 BangPatterns )、部分関数を回避し (`head`、`read`、`!!`)、エラー処理に`Maybe`/`Either`を使用し、テキストに`Text`を使用します。 IO を最小限に抑えます。コンパイラの型システムはあなたの最大の味方であり、完全な純粋な関数を目指してあなたを導いてくれるでしょう。