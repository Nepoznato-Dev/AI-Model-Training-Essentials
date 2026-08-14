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

# ہاسکل - نحوی حوالہ
یہ دستاویز ہاسکل (GHC 9.x) کے لیے ایک جامع، ساختی نحوی حوالہ فراہم کرتی ہے۔ یہ مکمل نحوی نمونوں، قسم کے نظام، مونڈس، سست تشخیص، اور فعال پروگرامنگ محاوروں پر توجہ مرکوز کرکے مرکزی ہاسکل حوالہ کی تکمیل کرتا ہے۔
---

## آپریٹرز اور اظہار
### کور آپریٹرز
| آپریٹر | نام | مثال | نوٹس |
|------------|------|---------|---------|
| `+``-``*``/` | ریاضی | `x + y`| Num typeclass |
| `div``mod` | عددی تقسیم | `7 \`div\` 2`| واپسی 3 |
| `^``**` | طاقت | `2 ^ 10`| `^`لازمی کے لیے؛  تیرنے کے لیے`**`|
| `==``/=` | مساوات | `x == y`| Eq typeclass |
| `<``>``<=``>=` | موازنہ | `x >= y`| آرڈر ٹائپ کلاس |
| `&&``\|\|``not`| منطقی | `a && b`| شارٹ سرکٹ |
| `.`| فنکشن کمپوزیشن | `(f . g) x`| `f (g x)`|
| `$`| فنکشن ایپلی کیشن | `f $ x + 1`| `f (x + 1)`— کم ترجیح |
| `<>`| Monoid ضمیمہ | `"hello" <> " world"`| نیم گروپ |
| `<$>`| فنیکٹر fmap | `(+1) <$> Just 5`| `fmap (+1) (Just 5)`|
| `<*>`| قابل اطلاق درخواست | `pure (+) <*> Just 3`| |
| `>>=`| موناد باندھ | `Just 5 >>= \x -> Just (x+1)`| |
| `>>`| موناد کی ترتیب | `putStrLn "hi" >> putStrLn "bye"`| |
| `=<<`| باندھ (الٹ) | `f =<< mx`| جیسا کہ`mx >>= f`|
| `++`| فہرست کنیکٹنیشن | `[1,2] ++ [3,4]`| O(n) بائیں فہرست میں |
| `:`| Cons | `1 : [2, 3]`| O(1) |
| `!!`| انڈیکس | `[1,2,3] !! 1`| O(n) — جزوی فعل |
| `\\`| فہرست میں فرق | `[1,2,3] \\ [2]`| `[1,3]`|
### آپریٹر کی ترجیح (منتخب)
| مقدم | آپریٹرز |
|------------|------------|
| 7 (سب سے زیادہ) | `*``/``div``mod` |
| 6 | `+``-` |
| 5 | `:``++``\\`|
| 4 | `==``/=``<``>``<=``>=` |
| 3 | `&&`|
| 2 | `\|\|`|
| 1 | `>>=``=<<` |
| 0 (سب سے کم) | `$``.` |
---

## کنٹرول فلو
### پیٹرن میچنگ
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

### سست پیٹرن
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

## افعال
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

## الجبری ڈیٹا کی اقسام
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

## قسم کی کلاسز
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

## پریکٹس میں مونڈز
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

## ماڈیولز اور درآمدات
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

## اعلی درجے کی خصوصیات
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

## خلاصہ
ہاسکل کا نحو کم سے کم ہے لیکن غیر معمولی طور پر اظہار خیال کرتا ہے۔ قسم کا نظام - الجبری ڈیٹا کی اقسام، قسم کی کلاسز، GADTs، اور قسم کے خاندانوں کے ساتھ - ایک تفصیلات اور تصدیقی ٹول دونوں کے طور پر کام کرتا ہے۔ پیٹرن کی مماثلت، سست تشخیص، اور مونڈز پیچیدہ مسائل کا خوبصورت حل فراہم کرتے ہیں۔ ہاسکل کی پاکیزگی (قسم میں کوئی مضر اثرات نہیں) کوڈ کے بارے میں استدلال، جانچ اور متوازی بنانا آسان بناتا ہے۔ اگرچہ سیکھنے کا منحنی خطوط بہت زیادہ ہے، ہاسکل کا اثر جدید زبانوں پر پھیلتا ہے — سوئفٹ کے آپشنز سے لے کر کوٹلن کی سیل شدہ کلاسز تک رسسٹ ٹائپ سسٹم تک۔ ہاسکل میں مہارت حاصل کرنا آپ کو ہر زبان میں ایک بہتر پروگرامر بناتا ہے۔