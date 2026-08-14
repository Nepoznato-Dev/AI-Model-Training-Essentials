---
# Metadata
title: "Haskell — Syntax Reference"
description: "Detailed syntax reference for Haskell covering type classes, monads, lazy evaluation, pattern matching, concurrency, and advanced type system features."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [haskell, syntax-reference, type-classes, monads, lazy-evaluation, pattern-matching, functional, coding-and-technology]
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

# হাসকেল - সিনট্যাক্স রেফারেন্স
এই নথিটি Haskell (GHC 9.x) এর জন্য একটি ব্যাপক, কাঠামোগত সিনট্যাক্স রেফারেন্স প্রদান করে। এটি সম্পূর্ণ সিনট্যাক্স প্যাটার্ন, টাইপ সিস্টেম, মোনাড, অলস মূল্যায়ন, এবং কার্যকরী প্রোগ্রামিং ইডিয়মগুলির উপর ফোকাস করে প্রধান হাসকেল রেফারেন্সের পরিপূরক।
---

## অপারেটর এবং এক্সপ্রেশন
### মূল অপারেটর
| অপারেটর | নাম | উদাহরণ | নোট |
|----------|------|---------|-------|
| `+``-``*``/` | পাটিগণিত | `x + y`| Num typeclass |
| `div``mod` | পূর্ণসংখ্যা বিভাজন | `7 \`div\` 2`| রিটার্নস 3 |
| `^``**` | শক্তি | `2 ^ 10`|  অবিচ্ছেদ্য জন্য `^`;  ভাসমান জন্য`**`|
| `==``/=` | সমতা | `x == y`| Eq typeclass |
| `<``>``<=``>=` | তুলনা | `x >= y`| অর্ডার টাইপক্লাস |
| `&&``\|\|``not`| যৌক্তিক | `a && b`| শর্ট সার্কিট |
| `.`| ফাংশন রচনা | `(f . g) x`| `f (g x)`|
| `$`| ফাংশন অ্যাপ্লিকেশন | `f $ x + 1`| `f (x + 1)`— কম অগ্রাধিকার |
| `<>`| মনোয়েড সংযোজন | `"hello" <> " world"`| সেমিগ্রুপ |
| `<$>`| ফাংশন fmap | `(+1) <$> Just 5`| `fmap (+1) (Just 5)`|
| `<*>`| প্রযোজ্য আবেদন | `pure (+) <*> Just 3`| |
| `>>=`| মোনাদ বাঁধা | `Just 5 >>= \x -> Just (x+1)`| |
| `>>`| মোনাড সিকোয়েন্স | `putStrLn "hi" >> putStrLn "bye"`| |
| `=<<`| বাঁধা (বিপরীত) | `f =<< mx`|`mx >>= f`|
| `++`| তালিকা সংযোজন | `[1,2] ++ [3,4]`| O(n) বাম তালিকায় |
| `:`| কনস | `1 : [2, 3]`| O(1) |
| `!!`| সূচক | `[1,2,3] !! 1`| O(n) — আংশিক ফাংশন |
| `\\`| তালিকার পার্থক্য | `[1,2,3] \\ [2]`| `[1,3]`|
### অপারেটর অগ্রাধিকার (নির্বাচিত)
| অগ্রাধিকার | অপারেটর |
|------------|------------|
| 7 (সর্বোচ্চ) | `*``/``div``mod` |
| 6 | `+``-` |
| 5 | `:``++``\\`|
| 4 | `==``/=``<``>``<=``>=` |
| 3 | `&&`|
| 2 | `\|\|`|
| 1 | `>>=``=<<` |
| 0 (সর্বনিম্ন) | `$``.` |
---

## নিয়ন্ত্রণ প্রবাহ
### প্যাটার্ন ম্যাচিং
```haskell
-- Case expression
describe :: Int -> String
describe n = case n of
  0 -> "zero"
  1 -> "one"
  2 -> "two"
  _ -> "many"

-- Function definition via pattern matching
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Tuple patterns
fst3 :: (a, b, c) -> a
fst3 (x, _, _) = x

-- List patterns
myHead :: [a] -> Maybe a
myHead []    = Nothing
myHead (x:_) = Just x

myTail :: [a] -> Maybe [a]
myTail []     = Nothing
myTail (_:xs) = Just xs

-- As-patterns (bind whole value + destructure)
firstTwo :: [a] -> Maybe [a]
firstTwo [] = Nothing
firstTwo xs@(x:_) = Just (take 2 xs)

-- Guard clauses
classify :: Int -> String
classify n
  | n < 0     = "negative"
  | n == 0    = "zero"
  | n <= 10   = "small"
  | n <= 100  = "medium"
  | otherwise = "large"

-- Where clauses
circleArea :: Double -> Double
circleArea r = pi * r^2
  where pi = 3.14159265  -- local binding

-- Let expressions
cylinderVolume :: Double -> Double -> Double
cylinderVolume r h =
  let baseArea = pi * r^2
  in baseArea * h
```

### অলস প্যাটার্ন
```haskell
-- Lazy pattern (~) — defers matching
let (a, b) = undefined in a  -- Exception: undefined
let ~(a, b) = undefined in a -- () — no error, pattern not forced

-- Useful in recursive definitions
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Bang patterns (strict evaluation — GHC extension)
{-# LANGUAGE BangPatterns #-}
strictSum :: [Int] -> Int
strictSum = go 0
  where go !acc []     = acc
        go !acc (x:xs) = go (acc + x) xs
```

---

## ফাংশন
```haskell
-- Function definition
add :: Int -> Int -> Int
add x y = x + y

-- Lambda
double = \x -> x * 2

-- Currying — all functions are curried
add' :: Int -> (Int -> Int)
add' = \x -> \y -> x + y

-- Partial application
add5 :: Int -> Int
add5 = add 5

-- Higher-order functions
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

-- Composition
composeExample :: [Int] -> [Int]
composeExample = filter (> 3) . map (* 2)

-- Point-free style
sumOfSquares :: [Int] -> Int
sumOfSquares = sum . map (^2)

-- Sections (partial operator application)
halve = (/ 2)
reciprocal = (1 /)
isPositive = (> 0)

-- flip — reverse argument order
flippedMap = flip map
flippedMap [1,2,3] (*2)  -- [2, 4, 6]

-- Uncurry / curry
uncurry (+) (3, 4)        -- 7
curry fst 3 4             -- 3
```

---

## বীজগণিতের তথ্য প্রকার
```haskell
-- Sum type (enum-like)
data Color = Red | Green | Blue
  deriving (Show, Eq, Ord, Enum, Bounded)

-- Product type
data Point = Point Double Double
  deriving (Show, Eq)

-- Record syntax
data Person = Person
  { personName  :: String
  , personAge   :: Int
  , personEmail :: String
  } deriving (Show, Eq)

-- Record update syntax
alice :: Person
alice = Person "Alice" 30 "alice@example.com"

olderAlice :: Person
olderAlice = alice { personAge = 31 }

-- Parameterized types
data Maybe a = Nothing | Just a
data Either e a = Left e | Right a
data List a = Nil | Cons a (List a)

-- Recursive types
data Tree a = Leaf | Node (Tree a) a (Tree a)
  deriving (Show, Eq)

insert :: Ord a => Tree a -> a -> Tree a
insert Leaf x = Node Leaf x Leaf
insert (Node l v r) x
  | x < v     = Node (insert l x) v r
  | x > v     = Node l v (insert r x)
  | otherwise = Node l v r

-- Newtype — zero-cost wrapper
newtype UserId = UserId Int deriving (Show, Eq)
newtype Name = Name String deriving (Show, Eq)

-- Type aliases
type Predicate a = a -> Bool
type Pair a = (a, a)
```

---

## টাইপ ক্লাস
```haskell
-- Type class declaration
class Eq a where
  (==) :: a -> a -> Bool
  (/=) :: a -> a -> Bool
  x /= y = not (x == y)  -- default implementation

-- Instance
data Color = Red | Green | Blue

instance Eq Color where
  Red   == Red   = True
  Green == Green = True
  Blue  == Blue  = True
  _     == _     = False

-- Multi-parameter type class
class Convertible a b where
  convert :: a -> b

-- Functional dependencies
class Collectible c a | c -> a where
  empty  :: c
  insert :: a -> c -> c
  toList :: c -> [a]

-- Deriving
data Status = Active | Inactive | Pending
  deriving (Show, Read, Eq, Ord, Enum, Bounded)

-- DerivingVia (GHC extension)
newtype Age = Age Int deriving (Eq, Ord, Show) via Int

-- Common type classes
-- Functor:   fmap  :: (a -> b) -> f a -> f b
-- Applicative: pure :: a -> f a; (<*>) :: f (a -> b) -> f a -> f b
-- Monad:     (>>=) :: f a -> (a -> f b) -> f b
-- Foldable:  foldr :: (a -> b -> b) -> b -> t a -> b
-- Traversable: traverse :: Applicative f => (a -> f b) -> t a -> f (t b)
```

---

## অনুশীলনে Monads
```haskell
-- Maybe monad — computations that can fail
safeDiv :: Double -> Double -> Maybe Double
safeDiv _ 0 = Nothing
safeDiv x y = Just (x / y)

safeSqrt :: Double -> Maybe Double
safeSqrt x
  | x < 0     = Nothing
  | otherwise = Just (sqrt x)

-- Do notation
quadratic :: Double -> Double -> Double -> Maybe Double
quadratic a b c = do
  let disc = b*b - 4*a*c
  sqDisc <- safeSqrt disc
  result <- safeDiv (-b + sqDisc) (2 * a)
  return result

-- Either monad — errors with context
data AppError = NotFound String | ValidationError String
  deriving (Show)

type App a = Either AppError a

findUser :: Int -> App String
findUser 1 = Right "Alice"
findUser _ = Left (NotFound "User not found")

-- IO monad
main :: IO ()
main = do
  putStrLn "What is your name?"
  name <- getLine
  putStrLn $ "Hello, " ++ name ++ "!"

-- State monad
import Control.Monad.State

type Counter = State Int

tick :: Counter Int
tick = do
  n <- get
  put (n + 1)
  return n

runCounter :: Counter a -> (a, Int)
runCounter = flip runState 0

-- Reader monad — dependency injection
import Control.Monad.Reader

type AppConfig = Reader DatabaseConfig

getConnection :: AppConfig Connection
getConnection = do
  config <- ask
  return (connect config)
```

---

## মডিউল এবং আমদানি
```haskell
module Data.MyModule
  ( -- Exported types
    MyType(..)      -- export type and all constructors
  , MyOtherType     -- export type only (abstract)
    -- Exported functions
  , myFunction
  , myOtherFunction
  ) where

import Data.List (sort, group)          -- selective import
import Data.Map qualified as M          -- qualified import
import Data.Maybe (fromMaybe, isJust)   -- specific functions
import Prelude hiding (map, filter)     -- hide specific names

-- Re-export
module Data.Wrapper (module Data.Internal, wrapper) where
```

---

## উন্নত বৈশিষ্ট্য
```haskell
{-# LANGUAGE GADTs #-}
-- Generalized Algebraic Data Types
data Expr a where
  Num  :: Int -> Expr Int
  Bool :: Bool -> Expr Bool
  Add  :: Expr Int -> Expr Int -> Expr Int
  If   :: Expr Bool -> Expr a -> Expr a -> Expr a

eval :: Expr a -> a
eval (Num n)      = n
eval (Bool b)     = b
eval (Add a b)    = eval a + eval b
eval (If c t f)   = if eval c then eval t else eval f

{-# LANGUAGE TypeFamilies #-}
-- Type families
type family Elem c
type instance Elem [a] = a
type instance Elem String = Char

{-# LANGUAGE RankNTypes #-}
-- Rank-N types
runAction :: (forall m. MonadIO m => m ()) -> IO ()
runAction action = runAction' action

{-# LANGUAGE ExistentialQuantification #-}
-- Existential types
data Showable = forall a. Show a => MkShowable a

instance Show Showable where
  show (MkShowable x) = show x

-- Lens pattern (simplified)
data Lens s a = Lens
  { view :: s -> a
  , over :: (a -> a) -> s -> s
  , set  :: a -> s -> s
  }

-- Concurrent Haskell
import Control.Concurrent
import Control.Concurrent.Async

-- Fork IO
main = do
  tid <- forkIO $ replicateM_ 5 (putStrLn "worker" >> threadDelay 1000000)
  replicateM_ 3 (putStrLn "main" >> threadDelay 1000000)

-- Async
do
  result <- race (slowAction 1) (slowAction 2)
  case result of
    Left  a -> print a
    Right b -> print b

-- STM (Software Transactional Memory)
import Control.Concurrent.STM

transfer :: TVar Int -> TVar Int -> Int -> IO ()
transfer from to amount = atomically $ do
  balance <- readTVar from
  if balance >= amount
    then do
      writeTVar from (balance - amount)
      modifyTVar to (+ amount)
    else retry  -- block until condition met
```

---

## সারাংশ
হাসকেলের সিনট্যাক্স ন্যূনতম কিন্তু অসাধারণভাবে অভিব্যক্তিপূর্ণ। টাইপ সিস্টেম - বীজগাণিতিক ডেটা টাইপ, টাইপ ক্লাস, GADTs এবং টাইপ ফ্যামিলি সহ - একটি স্পেসিফিকেশন এবং একটি যাচাইকরণ টুল উভয় হিসাবে কাজ করে। প্যাটার্ন ম্যাচিং, অলস মূল্যায়ন এবং মোনাড জটিল সমস্যার মার্জিত সমাধান প্রদান করে। হাসকেলের বিশুদ্ধতা (প্রকারে কোন পার্শ্বপ্রতিক্রিয়া নেই) কোডটিকে যুক্তি, পরীক্ষা এবং সমান্তরাল করা সহজ করে তোলে। শেখার বক্ররেখা খাড়া হলেও, হাসকেলের প্রভাব আধুনিক ভাষাগুলিতে ছড়িয়ে পড়ে — সুইফটের বিকল্প থেকে কোটলিনের সিল করা ক্লাস থেকে রাস্টের টাইপ সিস্টেম পর্যন্ত। Haskell আয়ত্ত করা আপনাকে প্রতিটি ভাষায় একজন ভাল প্রোগ্রামার করে তোলে।