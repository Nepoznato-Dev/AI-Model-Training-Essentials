---
# Metadata
title: "Haskell — Cheat Sheet"
description: "Quick-reference cheat sheet for Haskell syntax, types, and functional patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [haskell, functional, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Haskell — Lembar Cheat
## Dasar-dasar
```haskell
-- Variables (immutable by default)
name = "Alice"
age = 30 :: Int
pi = 3.14159 :: Double
active = True

-- Type annotations
greet :: String -> String
greet name = "Hello, " ++ name ++ "!"

-- Function application (no parentheses needed)
length "hello"          -- 5
max 3 5                 -- 5
succ 4                  -- 5

-- String (list of Char)
"Hello" ++ " World"     -- concatenation
head "hello"            -- 'h'
tail "hello"            -- "ello"
length "hello"          -- 5
'x' : "yz"              -- "xyz"

-- Tuples
pair = (1, "hello")
fst pair                -- 1
snd pair                -- "hello"
```

## Tipe & Tipe Kelas
```haskell
-- Basic types
42 :: Int
42 :: Integer           -- arbitrary precision
3.14 :: Float
3.14 :: Double
True :: Bool
'a' :: Char
"hello" :: String

-- Type constructors
data Color = Red | Green | Blue deriving (Show, Eq)
data Maybe a = Nothing | Just a
data Either e a = Left e | Right a

-- Type aliases
type Name = String
type Age = Int
type Person = (Name, Age)

-- Type classes
class Describable a where
    describe :: a -> String

instance Describable Color where
    describe Red   = "red"
    describe Green = "green"
    describe Blue  = "blue"

-- Common type classes: Show, Eq, Ord, Num, Functor, Monad
```

## Daftar & Pola
```haskell
-- List operations
let xs = [1, 2, 3, 4, 5]
head xs                 -- 1
tail xs                 -- [2,3,4,5]
last xs                 -- 5
init xs                 -- [1,2,3,4]
xs ++ [6]               -- append
0 : xs                  -- prepend
xs !! 2                 -- index: 3
length xs               -- 5
reverse xs              -- [5,4,3,2,1]
elem 3 xs               -- True
concat [[1,2],[3,4]]    -- [1,2,3,4]

-- List comprehensions
[x * 2 | x <- [1..10]]
[x * 2 | x <- [1..10], x > 3]
[(x, y) | x <- [1..3], y <- [1..3]]

-- Pattern matching
describe [] = "empty"
describe [x] = "one: " ++ show x
describe (x:xs) = "head: " ++ show x ++ ", rest: " ++ show (length xs)

-- Guards
classify n
    | n < 0     = "negative"
    | n == 0    = "zero"
    | otherwise = "positive"

-- Case expression
result = case value of
    Nothing -> "no value"
    Just x  -> "got " ++ show x
```

## Fungsi Tingkat Tinggi
```haskell
-- Map, filter, fold
map (* 2) [1, 2, 3]              -- [2, 4, 6]
filter (> 2) [1, 2, 3, 4]       -- [3, 4]
foldl (+) 0 [1, 2, 3]           -- 6
foldr (:) [] [1, 2, 3]          -- [1, 2, 3]
scanl (+) 0 [1, 2, 3]           -- [0, 1, 3, 6]

-- Lambda
\x -> x * 2
\x y -> x + y

-- Composition
(double . inc) 5    -- double (inc 5) = 12
(f . g . h) x       -- f (g (h x))

-- Partial application
add x y = x + y
add5 = add 5
add5 3               -- 8

-- $ operator (avoid parentheses)
f $ g $ h x          -- f (g (h x))

-- where clause
area r = pi * r ^ 2
    where pi = 3.14159

-- let expression
result = let x = 5; y = 10 in x + y
```

## Fungsi, Aplikatif & Monad
```haskell
-- Functor
fmap (* 2) (Just 5)       -- Just 10
(* 2) <$> [1, 2, 3]       -- [2, 4, 6]

-- Applicative
pure 5 :: Maybe Int        -- Just 5
Just (+) <*> Just 3 <*> Just 5  -- Just 8

-- Monad (Maybe)
Just 5 >>= \x -> Just (x * 2)   -- Just 10
Nothing >>= \x -> Just x        -- Nothing

-- do notation
result = do
    x <- Just 5
    y <- Just 10
    return (x + y)              -- Just 15

-- IO monad
main :: IO ()
main = do
    putStrLn "What's your name?"
    name <- getLine
    putStrLn ("Hello, " ++ name ++ "!")

-- IO operations
readFile "data.txt"
writeFile "out.txt" "content"
```

## Tipe & Catatan Data
```haskell
-- Record
data Person = Person
    { personName :: String
    , personAge  :: Int
    } deriving (Show, Eq)

alice = Person { personName = "Alice", personAge = 30 }
personName alice            -- "Alice"

-- Record update
olderAlice = alice { personAge = 31 }

-- Newtype (zero-cost wrapper)
newtype UserId = UserId Int deriving (Show, Eq)

-- Type class instance
instance Semigroup Color where
    Red <> _ = Red
    _ <> Red = Red
    Green <> _ = Green
    _ <> Green = Green
    Blue <> Blue = Blue
```

## Modul & Impor
```haskell
module MyModule (exported1, exported2) where

import Data.List (sort, nub)
import qualified Data.Map as Map
import Data.Maybe (fromMaybe, isJust)

-- Common modules
import Data.List
import Data.Map (Map)
import Data.Set (Set)
import Control.Monad
import Control.Applicative
import System.IO
import Text.Printf
```

## Penanganan Kesalahan
```haskell
-- Maybe for partial functions
safeDiv :: Double -> Double -> Maybe Double
safeDiv _ 0 = Nothing
safeDiv x y = Just (x / y)

-- Either for error messages
divide :: Double -> Double -> Either String Double
divide _ 0 = Left "Division by zero"
divide x y = Right (x / y)

-- error / undefined
error "this should never happen"
undefined  -- throws exception

-- Exception handling (IO)
import Control.Exception
main = do
    result <- try (readFile "nonexistent.txt") :: IO (Either IOException String)
    case result of
        Left err  -> putStrLn ("Error: " ++ show err)
        Right content -> putStrLn content
```
