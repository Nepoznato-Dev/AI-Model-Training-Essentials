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
# Haskell — Erreurs courantes et anti-modèles
Ce document répertorie les erreurs, pièges et anti-modèles les plus courants dans Haskell avec des corrections.
---

## 1. Listes infinies et surprises de paresse
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

## 2. Fonctions partielles
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

## 3. Ne pas comprendre les lois des monades
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

## 4. Confusion des types de chaînes
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

## 5. Ne pas utiliser correctement la syntaxe d'enregistrement
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

## 6. IO dans les fonctions pures
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

## 7. Anti-modèle : utilisation excessive de `IO`
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

## Résumé
La pureté et la paresse de Haskell créent des pièges uniques : fuites d'espace dues à une évaluation paresseuse, fonctions partielles qui plantent au moment de l'exécution, confusion entre String/Text/ByteString et utilisation excessive des E/S. La méthode Haskell est la suivante : utilisez une évaluation stricte pour les accumulateurs (`foldl'`, BangPatterns), évitez les fonctions partielles (`head`,`read`,`!!`), utilisez`Maybe`/`Either`pour la gestion des erreurs, utilisez`Text`pour le texte et gardez les E/S minimales. Le système de types du compilateur est votre meilleur allié : laissez-le vous guider vers des fonctions totales et pures.