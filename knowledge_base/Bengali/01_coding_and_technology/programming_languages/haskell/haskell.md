---
# Metadata
title: "Haskell"
description: "Comprehensive reference for the Haskell programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [haskell, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "39 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# হাস্কেল
Haskell একটি সম্পূর্ণরূপে কার্যকরী, স্ট্যাটিকালি টাইপ করা, অলসভাবে মূল্যায়ন করা প্রোগ্রামিং ভাষা। 1990 সালে প্রথম প্রমিত (Haskell 90) এবং একাধিক সংস্করণের মাধ্যমে পরিমার্জিত (Haskell 2010 হল বর্তমান মান), হাসকেল তার গাণিতিক কঠোরতা, শক্তিশালী টাইপ সিস্টেম (টাইপ ক্লাস, মোনাড এবং বীজগাণিতিক ডেটা টাইপ সহ), এবং প্রকারের মাধ্যমে সঠিকতার উপর জোর দেওয়ার জন্য পরিচিত।
হাসকেল একটি মূলধারার ভাষা নয়, তবে এর প্রভাব প্রচুর। মোনাড, অলস মূল্যায়ন এবং টাইপ ক্লাসের মত ধারণাগুলি রাস্ট, সুইফট, কোটলিন, স্কালা এবং টাইপস্ক্রিপ্টকে প্রভাবিত করেছে। হাসকেল অর্থায়নে ব্যবহৃত হয় (স্ট্যান্ডার্ড চার্টার্ড, বার্কলেস), কম্পাইলার (জিএইচসি), এবং আনুষ্ঠানিক যাচাইকরণে।
---

## কেন হাসকেল গুরুত্বপূর্ণ
- **বিশুদ্ধ ফাংশন**: ডিফল্টভাবে কোন পার্শ্ব প্রতিক্রিয়া নেই — ফাংশন সবসময় একই ইনপুটের জন্য একই আউটপুট ফেরত দেয়।
- **টাইপ সিস্টেম**: যেকোন ভাষার মধ্যে সবচেয়ে অভিব্যক্তিপূর্ণ - কম্পাইলের সময় বাগগুলি ধরে যা অন্য ভাষা করতে পারে না।
- **অলস মূল্যায়ন**: প্রয়োজন না হওয়া পর্যন্ত গণনা স্থগিত করা হয় — অসীম ডেটা স্ট্রাকচার এবং দক্ষ রচনা সক্ষম করে।
- **গাণিতিক ভিত্তি**: ল্যাম্বডা ক্যালকুলাস এবং বিভাগ তত্ত্বের উপর ভিত্তি করে — প্রোগ্রামগুলি গাণিতিক প্রমাণের কাছাকাছি।
- **প্রভাব**: হাসকেলের ধারণাগুলি বেশিরভাগ আধুনিক ভাষাকে রূপ দিয়েছে।
- **কনকারেন্সি**: সফটওয়্যার ট্রানজ্যাকশনাল মেমোরি (STM) মার্জিত সমসাময়িক প্রোগ্রামিং প্রদান করে।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **খাড়া শেখার বক্ররেখা** | Monads, functors, টাইপ ক্লাস — অপরিহার্য ভাষা থেকে খুব আলাদা | সময় বিনিয়োগ করুন; ধারণাগুলি হস্তান্তরযোগ্য |
| **অলস মূল্যায়ন বিস্ময়** | অপ্রত্যাশিত মেমরি ব্যবহার এবং কর্মক্ষমতা সমস্যা হতে পারে | যেখানে প্রয়োজন কঠোর মূল্যায়ন (`!`) ব্যবহার করুন |
| **ছোট ইকোসিস্টেম** | পাইথন, জাভা, বা জাভাস্ক্রিপ্টের চেয়ে কম লাইব্রেরি | হ্যাকেজ বাড়ছে; অনেক মানের প্যাকেজ |
| **চাকরীর বাজার** | কুলুঙ্গি — বেশিরভাগ অর্থ, গবেষণা, এবং কম্পাইলার কাজ | কার্যকরী প্রোগ্রামিং সম্প্রদায়ের মধ্যে ক্রমবর্ধমান |
| **সংকলনের গতি** | GHC বড় প্রকল্পের জন্য ধীর হতে পারে | ইন্টারেক্টিভ ডেভেলপমেন্টের জন্য GHCi ব্যবহার করুন |
---

## সিনট্যাক্স মৌলিক
```haskell
-- Basic types
name :: String
name = "Alice"

age :: Int
age = 30

-- Functions (no parentheses or commas needed)
add :: Int -> Int -> Int
add x y = x + y

-- Pattern matching
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- Algebraic data types
data Shape = Circle Double | Rectangle Double Double

area :: Shape -> Double
area (Circle r) = pi * r * r
area (Rectangle w h) = w * h

-- Type classes (like interfaces)
class Describable a where
    describe :: a -> String

instance Describable Shape where
    describe (Circle r) = "Circle with radius " ++ show r
    describe (Rectangle w h) = "Rectangle " ++ show w ++ "x" ++ show h

-- List operations (Haskell's strength)
numbers = [1, 2, 3, 4, 5]
doubled = map (*2) numbers
evens = filter even numbers
total = sum numbers

-- Monads (IO, Maybe, Either)
safeDivide :: Double -> Double -> Maybe Double
safeDivide _ 0 = Nothing
safeDivide x y = Just (x / y)

-- Do notation (syntactic sugar for monadic operations)
main :: IO ()
main = do
    putStrLn "What is your name?"
    name <- getLine
    putStrLn ("Hello, " ++ name ++ "!")

-- Lazy evaluation — infinite lists
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
first10 = take 10 fibs  -- [0,1,1,2,3,5,8,13,21,34]
```

---

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### টাইপ ফ্যামিলি — টাইপ-লেভেল ফাংশন
টাইপ ফ্যামিলি আপনাকে টাইপ লেভেলে টাইপ গণনা করার অনুমতি দেয়, যেভাবে ফাংশনগুলো মান লেভেলে মান গণনা করে।
```haskell
{-# LANGUAGE TypeFamilies, GADTs #-}

-- Associated type families
class Container c where
    type Item c
    insert :: Item c -> c -> c
    extract :: c -> Maybe (Item c)

instance Container [a] where
    type Item [a] = a
    insert x xs = x : xs
    extract [] = Nothing
    extract (x:_) = Just x

-- Closed type families (complete mapping)
type family Elem x where
    Elem Int = Bool
    Elem String = Char
    Elem [a] = a
```

### GADTs — সাধারণীকৃত বীজগণিত ডেটা প্রকার
GADTs আপনাকে প্রতিটি কনস্ট্রাক্টরের রিটার্ন টাইপ সুনির্দিষ্টভাবে নির্দিষ্ট করতে দেয়, টাইপ-সেফ ইন্টারপ্রেটার এবং এমবেডেড ডিএসএল সক্ষম করে।
```haskell
{-# LANGUAGE GADTs, RankNTypes #-}

-- A type-safe expression language
data Expr a where
    LitInt  :: Int -> Expr Int
    LitBool :: Bool -> Expr Bool
    Add     :: Expr Int -> Expr Int -> Expr Int
    If      :: Expr Bool -> Expr a -> Expr a -> Expr a
    IsZero  :: Expr Int -> Expr Bool

eval :: Expr a -> a
eval (LitInt n) = n
eval (LitBool b) = b
eval (Add a b) = eval a + eval b
eval (If cond t f) = if eval cond then eval t else eval f
eval (IsZero n) = eval n == 0

-- This is type-safe: eval (Add (LitInt 1) (LitInt 2)) == 3
-- This won't compile: Add (LitInt 1) (LitBool True)
```

### মোনাড ট্রান্সফরমার
মোনাড ট্রান্সফরমারগুলি মোনাডিক প্রভাবগুলিকে স্ট্যাক করে, আপনাকে IO, রাজ্য, ত্রুটি পরিচালনা এবং আরও অনেক কিছু একত্রিত করতে দেয়।
```haskell
{-# LANGUAGE OverloadedStrings #-}
import Control.Monad.Trans.Reader
import Control.Monad.Trans.State
import Control.Monad.Trans.Except
import Control.Monad.IO.Class

-- ReaderT for dependency injection
data AppConfig = AppConfig { dbHost :: String, dbPort :: Int }

type App a = ReaderT AppConfig IO a

runApp :: AppConfig -> App a -> IO a
runApp = runReaderT

getDbHost :: App String
getDbHost = do
    cfg <- ask
    return (dbHost cfg)

-- Stacking transformers: State + Error + IO
type AppM a = StateT Int (ExceptT String IO) a

processData :: AppM String
processData = do
    count <- get
    if count > 100
        then lift (throwE "Limit exceeded")
        else do
            put (count + 1)
            result <- lift (liftIO (putStrLn "Processing...") >> return "done")
            return result
```

### ফাংশন, অ্যাপ্লিকেটিভ এবং মোনাড হায়ারার্কি
```haskell
-- Functor: something you can map over
class Functor f where
    fmap :: (a -> b) -> f a -> f b

-- Applicative: functor with application
class Functor f => Applicative f where
    pure  :: a -> f a
    (<*>) :: f (a -> b) -> f a -> f b

-- Monad: applicative with sequencing
class Applicative m => Monad m where
    (>>=) :: m a -> (a -> m b) -> m b
    return :: a -> m a

-- Example: Maybe is Functor, Applicative, and Monad
-- fmap (+1) (Just 5)          == Just 6
-- pure 5 :: Maybe Int         == Just 5
-- Just (+1) <*> Just 5        == Just 6
-- Just 5 >>= \x -> Just (x+1) == Just 6
```

### উন্নত প্যাটার্ন ম্যাচিং
```haskell
{-# LANGUAGE ViewPatterns, PatternSynonyms #-}

-- View patterns: compute before matching
classify :: (Int -> Bool) -> Int -> String
classify isEven (isEven -> True) = "even"
classify _ _ = "odd"

-- Pattern synonyms: create patterns for existing types
pattern Email :: String -> String -> String
pattern Email user domain <- (break (== '@') -> (user, '@':domain))
    where Email user domain = user ++ "@" ++ domain

formatEmail :: String -> String
formatEmail (Email u d) = u ++ " at " ++ d

-- Guards with pattern matching
describe :: [Int] -> String
describe [] = "empty"
describe [x] | x < 0 = "single negative"
             | otherwise = "single positive"
describe (x:y:_) | x == y = "starts with duplicates"
describe _ = "multiple elements"
```

### অলস বনাম কঠোর মূল্যায়ন
```haskell
-- Lazy by default: thunks build up
lazySum :: [Int] -> Int
lazySum xs = foldl (+) 0 xs  -- Builds thunk chain, may stack overflow

-- Strict fold: forces evaluation at each step
strictSum :: [Int] -> Int
strictSum xs = foldl' (+) 0 xs  -- O(1) space

-- Bang patterns: force evaluation of arguments
strictPair :: (!Int, !Int) -> Int
strictPair (!x, !y) = x + y

-- Strict data fields
data StrictPoint = SP !Double !Double  -- Fields evaluated on construction

-- Using seq to force evaluation
strictApply :: (a -> b) -> a -> b
strictApply f x = x `seq` f x
```


---

## সামঞ্জস্য এবং সমান্তরালতা
### সফ্টওয়্যার লেনদেন মেমরি (STM)
STM শেয়ার্ড স্টেটের জন্য কম্পোজেবল লেনদেন প্রদান করে — যেমন ডাটাবেস লেনদেন কিন্তু মেমরির জন্য।
```haskell
import Control.Concurrent.STM
import Control.Concurrent
import Control.Monad

-- A shared bank account using STM
data Account = Account { balance :: TVar Int, owner :: String }

newAccount :: String -> Int -> IO Account
newAccount name initial = do
    bal <- newTVarIO initial
    return (Account bal name)

-- Transfer money atomically
transfer :: Account -> Account -> Int -> IO Bool
transfer from to amount = atomically $ do
    fromBal <- readTVar (balance from)
    if fromBal >= amount
        then do
            writeTVar (balance from) (fromBal - amount)
            toBal <- readTVar (balance to)
            writeTVar (balance to) (toBal + amount)
            return True
        else return False

-- STM composes naturally with retry and orElse
transferWithRetry :: Account -> Account -> Int -> IO ()
transferWithRetry from to amount = atomically $ do
    fromBal <- readTVar (balance from)
    check (fromBal >= amount)  -- retry if insufficient funds
    writeTVar (balance from) (fromBal - amount)
    toBal <- readTVar (balance to)
    writeTVar (balance to) (toBal + amount)
```

### সমসাময়িক অ্যাসিঙ্ক অপারেশন
```haskell
import Control.Concurrent.Async
import Network.HTTP.Simple

-- Run multiple IO actions concurrently
fetchUrls :: [String] -> IO [Response String]
fetchUrls urls = mapConcurrently (\url -> do
    request <- parseRequest url
    httpBS request
    ) urls

-- Race: first to complete wins
timeout :: Int -> IO a -> IO (Maybe a)
timeout micros action = race (threadDelay micros) action >>= \case
    Left () -> return Nothing
    Right a -> return (Just a)

-- Structured concurrency with async
concurrentPipeline :: IO ()
concurrentPipeline = do
    a1 <- async (computePart1)
    a2 <- async (computePart2)
    r1 <- wait a1
    r2 <- wait a2
    putStrLn $ "Results: " ++ show (r1, r2)
```

### সমান্তরাল কৌশল
```haskell
import Control.Parallel.Strategies

-- Parallel map using strategies
parMap' :: (a -> b) -> [a] -> Eval [b]
parMap' f xs = map f xs `using` parList rseq

-- Fibonacci: parallel computation
parFib :: Int -> Int
parFib 0 = 0
parFib 1 = 1
parFib n = parFib (n-1) + parFib (n-2)

-- Run with parallel strategies
fib :: Int -> Int
fib n = runEval $ do
    a <- rpar (parFib (n - 1))
    b <- rpar (parFib (n - 2))
    rseq a
    rseq b
    return (a + b)

-- Compile with: ghc -O2 -threaded -rtsopts
-- Run with: ./program +RTS -N4
```


---

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### প্রকল্পের কাঠামো (স্ট্যাক/ক্যাবল)
```
my-haskell-project/
├── app/
│   └── Main.hs              # Application entry point
├── src/
│   ├── Lib.hs               # Library root module
│   ├── MyProject/
│   │   ├── Types.hs         # Core type definitions
│   │   ├── Service.hs       # Business logic
│   │   └── Config.hs        # Configuration handling
├── test/
│   └── Spec.hs              # Test entry point
├── bench/
│   └── Bench.hs             # Benchmarks
├── package.yaml             # hpack project description
├── stack.yaml               # Stack resolver config
├── my-project.cabal         # Generated by hpack from package.yaml
└── README.md
```

### স্ট্যাক কনফিগারেশন (stack.yaml)
```yaml
# stack.yaml
resolver: lts-22.12            # GHC 9.4.x snapshot
packages:
  - .

extra-deps:
  - servant-0.20.1
  - servant-server-0.20

# Build options
build:
  haddock-arguments:
    haddock-args:
      - "--odir=docs"

# Docker support
docker:
  enable: false
  image: haskell:9.4

# Nix support (optional)
nix:
  enable: false
  packages: [zlib]
```

### প্যাকেজ বিবরণ (hpack এর জন্য package.yaml)
```yaml
# package.yaml
name:                my-haskell-project
version:             0.1.0.0
synopsis:            A sample Haskell project
license:             MIT
author:              Developer Name

ghc-options:
  - -Wall
  - -Wcompat
  - -Widentities
  - -Wincomplete-record-updates
  - -Wincomplete-uni-patterns
  - -Wredundant-constraints

dependencies:
  - base >= 4.7 && < 5
  - text
  - bytestring
  - containers
  - aeson
  - warp
  - servant-server

library:
  source-dirs: src

executables:
  my-app:
    main: Main.hs
    source-dirs: app
    dependencies:
      - my-haskell-project

tests:
  my-test:
    main: Spec.hs
    source-dirs: test
    dependencies:
      - my-haskell-project
      - hspec
      - QuickCheck
```

### কী বিল্ড কমান্ড
| আদেশ | বর্ণনা |
|---------|---------------|
| `stack new my-project`| টেমপ্লেট থেকে নতুন প্রকল্প তৈরি করুন |
| `stack build`| প্রকল্প নির্মাণ |
| `stack ghci`| প্রজেক্ট লোড করে ইন্টারেক্টিভ REPL শুরু করুন |
| `stack test`| টেস্ট স্যুট চালান |
| `stack bench`| বেঞ্চমার্ক চালান |
| `stack haddock`| ডকুমেন্টেশন তৈরি করুন |
| `stack exec my-app`| এক্সিকিউটেবল চালান |
| `stack clean`| বিল্ড আর্টিফ্যাক্ট পরিষ্কার |
| `stack update`| প্যাকেজ সূচক আপডেট করুন |
| `stack freeze`| সঠিক নির্ভরতা সংস্করণগুলি পিন করুন |
### CI/CD পাইপলাইন (GitHub অ্যাকশন)
```yaml
# .github/workflows/haskell.yml
name: Haskell CI
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Stack
        uses: haskell-actions/setup@v2
        with:
          enable-stack: true
          stack-version: latest

      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.stack
          key: stack-${{ hashFiles('stack.yaml') }}

      - name: Build
        run: stack build --no-terminal --system-ghc

      - name: Test
        run: stack test --no-terminal --system-ghc

      - name: Haddock
        run: stack haddock --no-terminal --system-ghc
```


---

## পরীক্ষা
### HSpec — ইউনিট টেস্টিং ফ্রেমওয়ার্ক
HSpec হল সবচেয়ে জনপ্রিয় টেস্টিং ফ্রেমওয়ার্ক, রুবির RSpec দ্বারা অনুপ্রাণিত। এটি একটি BDD-শৈলী সিনট্যাক্স প্রদান করে।
```haskell
-- test/Spec.hs
import Test.Hspec
import Test.QuickCheck
import MyProject.Math (factorial, isPrime)

main :: IO ()
main = hspec $ do
    describe "factorial" $ do
        it "returns 1 for 0" $ do
            factorial 0 `shouldBe` (1 :: Integer)

        it "returns correct values for small inputs" $ do
            factorial 1 `shouldBe` 1
            factorial 5 `shouldBe` 120
            factorial 10 `shouldBe` 3628800

        it "is always positive for non-negative input" $
            property $ \n ->
                n >= 0 ==> factorial (abs n) > 0

    describe "isPrime" $ do
        it "identifies primes correctly" $ do
            isPrime 2 `shouldBe` True
            isPrime 3 `shouldBe` True
            isPrime 4 `shouldBe` False
            isPrime 17 `shouldBe` True

        it "returns False for numbers less than 2" $
            property $ \n ->
                n < 2 ==> isPrime n == False
```

### QuickCheck সহ সম্পত্তি-ভিত্তিক পরীক্ষা
QuickCheck আপনার কোডের বৈশিষ্ট্য যাচাই করতে এলোমেলো পরীক্ষার কেস তৈরি করে।
```haskell
import Test.QuickCheck

-- Define an Arbitrary instance for custom types
data Tree a = Leaf a | Branch (Tree a) (Tree a)
    deriving (Eq, Show)

instance Arbitrary a => Arbitrary (Tree a) where
    arbitrary = do
        depth <- choose (1, 3)
        genTree depth
      where
        genTree 1 = Leaf <$> arbitrary
        genTree n = frequency
            [ (1, Leaf <$> arbitrary)
            , (2, Branch <$> genTree (n-1) <*> genTree (n-1))
            ]

-- Properties to test
prop_reverseInvolutive :: [Int] -> Bool
prop_reverseInvolutive xs = reverse (reverse xs) == xs

prop_sortIdempotent :: [Int] -> Bool
prop_sortIdempotent xs = sort (sort xs) == sort xs

prop_lengthAfterMap :: [Int] -> Bool
prop_lengthAfterMap xs = length (map (*2) xs) == length xs

-- Custom generator with shrink
newtype PositiveInt = PositiveInt Int deriving (Show)

instance Arbitrary PositiveInt where
    arbitrary = PositiveInt <$> choose (1, 10000)
    shrink (PositiveInt n) = [ PositiveInt n' | n' <- shrink n, n' > 0 ]

-- Run with: quickCheckWith stdArgs { maxSuccess = 1000 } prop_name
```

### টেস্ট কমান্ড
| আদেশ | বর্ণনা |
|---------|---------------|
| `stack test`| সমস্ত পরীক্ষা স্যুট চালান |
| `stack test --fast`| দ্রুত পরীক্ষা তৈরির জন্য অপ্টিমাইজেশানগুলি এড়িয়ে যান |
| `stack build --test --test-arguments "--color"`| রঙিন আউটপুট দিয়ে পরীক্ষা চালান |
| `stack ghci --test`| REPL এ পরীক্ষা মডিউল লোড করুন |

---

## ইন্টারঅপারেবিলিটি
### সি ফরেন ফাংশন ইন্টারফেস (এফএফআই)
Haskell সরাসরি C ফাংশন কল করতে পারে এবং Haskell ফাংশন C-তে প্রকাশ করতে পারে।
```haskell
{-# LANGUAGE ForeignFunctionInterface #-}
import Foreign
import Foreign.C.Types
import Foreign.C.String

-- Calling C functions from Haskell
foreign import ccall "stdlib.h malloc"
    c_malloc :: CSize -> IO (Ptr a)

foreign import ccall "stdlib.h free"
    c_free :: Ptr a -> IO ()

foreign import ccall "string.h strlen"
    c_strlen :: CString -> IO CSize

-- Using the FFI safely
safeStrlen :: String -> IO Int
safeStrlen str = do
    let len = fromIntegral (length str)
    withCString str $ \cstr -> do
        n <- c_strlen cstr
        return (fromIntegral n)

-- Allocating and using C memory
withCArray :: Storable a => [a] -> (Ptr a -> IO b) -> IO b
withCArray xs f = do
    ptr <- mallocArray (length xs)
    zipWithM_ (pokeElemOff ptr) [0..] xs
    result <- f ptr
    free ptr
    return result

-- Exporting Haskell functions to C
foreign export ccall "hs_add"
    hsAdd :: CInt -> CInt -> CInt

hsAdd :: CInt -> CInt -> CInt
hsAdd a b = a + b
```

### পাইথন ইন্টারপ (ইনলাইন-সি বা HPy এর মাধ্যমে)
```haskell
-- Using inline-c to call C which wraps Python
{-# LANGUAGE QuasiQuotes #-}
import qualified Language.C.Inline as C

C.include "<Python.h>"

runPython :: String -> IO ()
runPython code = do
    C.withCString code $ \cstr -> do
        [C.block| void {
            Py_Initialize();
            PyRun_SimpleString($(char *cstr));
            Py_Finalize();
        } |]
        return ()
```


---

## ডিজাইন প্যাটার্ন
### ট্যাগলেস ফাইনাল (এমবেডেড ডিএসএল)
ট্যাগবিহীন চূড়ান্ত শৈলী DSL-কে টাইপ ক্লাস ব্যবহার করে এনকোড করে, একাধিক ব্যাখ্যা সক্ষম করে।
```haskell
{-# LANGUAGE FlexibleInstances #-}

-- Define the DSL as a type class
class ExprDSL repr where
    lit  :: Int -> repr Int
    add  :: repr Int -> repr Int -> repr Int
    mul  :: repr Int -> repr Int -> repr Int
    ifz  :: repr Int -> repr a -> repr a -> repr a

-- Interpretation 1: Direct evaluation
newtype Eval a = Eval { runEval :: a }

instance ExprDSL Eval where
    lit n = Eval n
    add (Eval a) (Eval b) = Eval (a + b)
    mul (Eval a) (Eval b) = Eval (a * b)
    ifz (Eval c) (Eval t) (Eval f) = Eval (if c == 0 then t else f)

-- Interpretation 2: Pretty printing
newtype Pretty a = Pretty { runPretty :: String }

instance ExprDSL Pretty where
    lit n = Pretty (show n)
    add (Pretty a) (Pretty b) = Pretty $ "(" ++ a ++ " + " ++ b ++ ")"
    mul (Pretty a) (Pretty b) = Pretty $ "(" ++ a ++ " * " ++ b ++ ")"
    ifz (Pretty c) (Pretty t) (Pretty f) =
        Pretty $ "(if " ++ c ++ " == 0 then " ++ t ++ " else " ++ f ++ ")"

-- Use the same DSL expression with different interpretations
example :: ExprDSL repr => repr Int
example = add (lit 3) (mul (lit 4) (lit 5))

-- runEval example  == 23
-- runPretty example == "(3 + (4 * 5))"
```

### বিনামূল্যে Monads
ফ্রি মোনাডগুলি তাদের ব্যাখ্যা থেকে প্রভাবের বর্ণনাকে আলাদা করে।
```haskell
{-# LANGUAGE DeriveFunctor #-}

-- Define a functor for your operations
data TeletypeF next
    = GetLine (String -> next)
    | PutLine String next
    deriving (Functor)

type Teletype = Free TeletypeF

-- Smart constructors
getLine' :: Teletype String
getLine' = liftF (GetLine id)

putLine' :: String -> Teletype ()
putLine' s = liftF (PutLine s ())

-- Build programs using the DSL
program :: Teletype ()
program = do
    name <- getLine'
    putLine' ("Hello, " ++ name ++ "!")

-- Interpret in IO
runTeletypeIO :: Teletype a -> IO a
runTeletypeIO (Pure a) = return a
runTeletypeIO (Free (GetLine f)) = getLine >>= runTeletypeIO . f
runTeletypeIO (Free (PutLine s next)) = putStrLn s >> runTeletypeIO next

-- Interpret as pure state (for testing)
runTeletypePure :: [String] -> Teletype a -> (a, [String])
runTeletypePure _ (Pure a) = (a, [])
runTeletypePure [] (Free (GetLine _)) = error "No more input"
runTeletypePure (i:is) (Free (GetLine f)) = runTeletypePure is (f i)
runTeletypePure is (Free (PutLine s next)) =
    let (a, out) = runTeletypePure is next
    in (a, s : out)
```

### অ্যাপ্লিকেশন আর্কিটেকচারের জন্য ReaderT প্যাটার্ন
রিডারটি প্যাটার্ন হল নির্ভরতা ইনজেকশনের আধুনিক হাস্কেল পদ্ধতি।
```haskell
{-# LANGUAGE OverloadedStrings #-}
import Control.Monad.Reader
import Data.IORef

-- Application environment
data AppEnv = AppEnv
    { appLogger   :: String -> IO ()
    , appDbPool   :: IORef Int  -- simplified pool
    , appConfig   :: AppConfig
    }

data AppConfig = AppConfig
    { cfgPort :: Int
    , cfgDebug :: Bool
    }

type App a = ReaderT AppEnv IO a

-- Logging with dependency injection
logMsg :: String -> App ()
logMsg msg = do
    env <- ask
    liftIO (appLogger env msg)

-- Application entry point
runApplication :: App ()
runApplication = do
    logMsg "Starting application"
    env <- ask
    liftIO $ putStrLn $ "Running on port " ++ show (cfgPort (appConfig env))
    logMsg "Application started"

main :: IO ()
main = do
    loggerRef <- newIORef 0
    let env = AppEnv
            { appLogger = \msg -> putStrLn ("[LOG] " ++ msg)
            , appDbPool = loggerRef
            , appConfig = AppConfig { cfgPort = 8080, cfgDebug = True }
            }
    runReaderT runApplication env
```


---

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### প্রোফাইলিং টুল
| টুল | উদ্দেশ্য | আদেশ |
|------|---------|---------|
| **GHC প্রোফাইলার** | সময় এবং বরাদ্দ প্রোফাইলিং | `stack build --profile`তারপর`./app +RTS -p`|
| **থ্রেডস্কোপ** | সমান্তরাল মৃত্যুদন্ড কল্পনা করুন | `./app +RTS -l`তারপর`app.eventlog`| খুলুন
| **GHc-ইভেন্ট** | ইভেন্ট লগ বিশ্লেষণ করুন | `ghc-events show app.eventlog`|
| **মাপদণ্ড** | পরিসংখ্যানগত বেঞ্চমার্কিং |`criterion`প্যাকেজ ব্যবহার করুন |
| **hp2pretty** | হিপ প্রোফাইল ভিজ্যুয়ালাইজ করুন | `./app +RTS -h`তারপর`hp2pretty app.hp`|
### মানদণ্ড সহ বেঞ্চমার্কিং
```haskell
-- bench/Bench.hs
import Criterion.Main
import Data.List (sort)

-- Functions to benchmark
naiveSum :: [Int] -> Int
naiveSum = foldl (+) 0

strictSum :: [Int] -> Int
strictSum = foldl' (+) 0

main :: IO ()
main = defaultMain
    [ bgroup "sum 1M elements"
        [ bench "naive foldl" $ whnf naiveSum [1..1000000]
        , bench "strict foldl'" $ whnf strictSum [1..1000000]
        ]
    , bgroup "sorting"
        [ bench "sort 10k" $ whnf sort [10000, 9999..1]
        , bench "sort 100k" $ whnf sort [100000, 99999..1]
        ]
    ]

-- Run: stack bench
-- Output includes mean, std dev, throughput
```

### অপ্টিমাইজেশন কৌশল
```haskell
{-# LANGUAGE BangPatterns, StrictData #-}

-- 1. Strictness annotations prevent thunk buildup
data Point = Point !Double !Double !Double
    deriving (Show)

-- 2. Unboxed types for performance-critical code
import Data.Vector.Unboxed qualified as VU

fastDotProduct :: VU.Vector Double -> VU.Vector Double -> Double
fastDotProduct a b = VU.sum (VU.zipWith (*) a b)

-- 3. Fusion with rewrite rules (lists fuse automatically)
-- This runs in O(1) memory due to stream fusion:
processed :: [Int] -> [Int]
processed = filter odd . map (*2) . filter (> 5)

-- 4. Using ByteString/Text instead of String
import qualified Data.ByteString as BS
import qualified Data.Text as T

-- String: [Char] — linked list, terrible performance
-- ByteString: packed bytes, great for I/O
-- Text: packed Unicode text

-- 5. SPECIALIZE pragma for monomorphic optimization
{-# SPECIALIZE fastSum :: [Int] -> Int #-}
fastSum :: Num a => [a] -> a
fastSum = foldl' (+) 0

-- 6. Compile flags for maximum performance
-- ghc-options: -O2 -fllvm -funbox-strict-fields -rtsopts
```


---

## স্থাপনা
### বিল্ডিং রিলিজ বাইনারি
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### ডকার স্থাপনা
```dockerfile
# Multi-stage Dockerfile for minimal image
# Stage 1: Build
FROM haskell:9.4 AS builder
WORKDIR /app
COPY stack.yaml package.yaml ./
RUN stack install --system-ghc --only-dependencies
COPY . .
RUN stack build --system-ghc --copy-bins --local-bin-path /app/dist

# Stage 2: Runtime (minimal image)
FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y ca-certificates libgmp10 && rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/dist/my-app /usr/local/bin/my-app
EXPOSE 8080
CMD ["my-app"]
```

### নিক্স-ভিত্তিক স্থাপনা
```nix
# default.nix
{ pkgs ? import <nixpkgs> {} }:
pkgs.haskellPackages.developPackage {
  root = ./.;
  modifier = drv:
    pkgs.haskell.lib.addBuildFlags drv [
      "-O2"
      "-threaded"
      "-rtsopts"
    ];
}
```

---

## কখন Haskell ব্যবহার করবেন
| দৃশ্যকল্প | কেন হাসকেল | ভাল বিকল্প |
|------------|------------|---------|
| আনুষ্ঠানিক যাচাই | টাইপ সিস্টেম প্রমাণ সক্ষম করে | Agda, Coq |
| কম্পাইলার উন্নয়ন | ভাষা বাস্তবায়নের জন্য চমৎকার | OCaml, মরিচা |
| আর্থিক ব্যবস্থা | প্রকারের মাধ্যমে সঠিকতা | স্কালা, F# |
| FP ধারণা শেখা | বিশুদ্ধতম কার্যকরী ভাষা | স্কালা (আরো ব্যবহারিক), এলম |
| সাধারণ অ্যাপ্লিকেশন বিকাশ | সম্ভব কিন্তু কুলুঙ্গি | পাইথন, গো, জাভা |
| ওয়েব ডেভেলপমেন্ট | ইয়েসদ/সেবক বিদ্যমান কিন্তু সীমিত | জাভাস্ক্রিপ্ট/টাইপস্ক্রিপ্ট |
| তথ্য বিজ্ঞান | বাস্তুতন্ত্র নয় | পাইথন, আর |
---

## সিন্থেটিক প্রশ্নোত্তর
### প্রশ্ন 1: কীভাবে হাসকেলের অলস মূল্যায়ন কর্মক্ষমতা প্রভাবিত করে?
**A:** অলস মূল্যায়ন মানে এক্সপ্রেশনগুলি শুধুমাত্র প্রয়োজনের সময় গণনা করা হয়, অসীম ডেটা স্ট্রাকচার এবং কম্পোজেবল পাইপলাইন সক্ষম করে৷ যাইহোক, থঙ্কস জমা হলে এটি স্থান ফুটো করতে পারে:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

সাংখ্যিক ভাঁজগুলির জন্য`foldl`এর পরিবর্তে`foldl'`(`Data.List` থেকে) ব্যবহার করুন৷ প্রয়োজনে জোর করে মূল্যায়ন করতে`!`ব্যাং প্যাটার্ন বা`seq`ব্যবহার করুন।
### প্রশ্ন 2: `Functor`,`Applicative`এবং`Monad`এর মধ্যে ব্যবহারিক পার্থক্য কী?
**A:** প্রতিটি টাইপক্লাস ক্ষমতা যোগ করে:
```haskell
-- Functor: apply a function inside a context
fmap (+1) (Just 5)            -- Just 6
(+1) <$> [1, 2, 3]            -- [2, 3, 4]

-- Applicative: apply functions with contexts to values with contexts
pure (+) <*> Just 3 <*> Just 5  -- Just 8
liftA2 (,) (Just 1) (Just 2)    -- Just (1,2)

-- Monad: chain computations with context
Just 5 >>= \x -> Just (x + 1)   -- Just 6
do { x <- Just 5; return (x+1) } -- Just 6
```

**Functor** একটি প্রসঙ্গে একটি বিশুদ্ধ ফাংশন ম্যাপ করে। **অ্যাপ্লিকেটিভ** এমন ফাংশনগুলিকে প্রয়োগ করে যেগুলি নিজেই একটি প্রসঙ্গে। **মোনাড** প্রতিটি ধাপকে পূর্ববর্তী ধাপের ফলাফলের উপর নির্ভর করতে দেয়। অনুশীলনে: সাধারণ রূপান্তরের জন্য`fmap`/ `<$>`, প্রভাব একত্রিত করার জন্য`<*>`এবং অনুক্রমিক নির্ভরশীল গণনার জন্য`>>=`/`do`ব্যবহার করুন৷
### প্রশ্ন 3: বিশুদ্ধ হাসকেল কোডে আমি কীভাবে পার্শ্ব প্রতিক্রিয়াগুলি পরিচালনা করব?
**A:** বিশুদ্ধ এবং কার্যকর কোড আলাদা করতে টাইপ সিস্টেম ব্যবহার করুন:
```haskell
-- Pure function — no side effects, always same output for same input
add :: Int -> Int -> Int
add x y = x + y

-- Effectful function — type signature declares the effect
readFile :: FilePath -> IO String
fetchUser :: UserId -> ExceptT ApiError IO User

-- Run effects at the boundary, keep core pure
main :: IO ()
main = do
  contents <- readFile "data.txt"
  let result = pureProcess contents  -- pure function
  putStrLn (show result)
```

মূল যুক্তি খাঁটি রাখুন এবং প্রভাবগুলি প্রান্তে ঠেলে দিন। কনফিগারেশনের জন্য `ReaderT`, ত্রুটির জন্য`ExceptT`এবং পরিবর্তনযোগ্য অবস্থার জন্য`StateT`ব্যবহার করুন৷
### প্রশ্ন 4: টাইপ ক্লাস কি এবং কিভাবে তারা OOP ইন্টারফেস থেকে আলাদা?
**A:** টাইপ ক্লাস এমন আচরণকে সংজ্ঞায়িত করে যা প্রকারগুলি প্রয়োগ করতে পারে। OOP ইন্টারফেসের বিপরীতে, এগুলি উন্মুক্ত (যেকোনো প্রকার একটি উদাহরণ হতে পারে) এবং অ্যাড-হক পলিমারফিজম সমর্থন করে:
```haskell
-- Type class declaration
class Eq a where
  (==) :: a -> a -> Bool

-- Instance for a type
instance Eq Color where
  Red   == Red   = True
  Green == Green = True
  Blue  == Blue  = True
  _     == _     = False

-- Derived instance (compiler generates it)
data Point = Point Int Int deriving (Eq, Show, Ord)

-- Constraint: function works for any type that is an instance of Eq
elem :: Eq a => a -> [a] -> Bool
```

### প্রশ্ন 5: বাস্তব-বিশ্ব ব্যবহারের জন্য আমি কীভাবে একটি হাসকেল প্রকল্প গঠন করব?
**A:** একটি স্ট্যান্ডার্ড লেআউট সহ ক্যাবল বা স্ট্যাক ব্যবহার করুন:
```
my-project/
├── app/Main.hs           -- Entry point
├── src/
│   ├── MyProject/
│   │   ├── Types.hs      -- Core data types
│   │   ├── Parser.hs     -- Pure parsing logic
│   │   ├── Service.hs    -- Business logic
│   │   └── Config.hs     -- Configuration types
├── test/
│   └── Spec.hs           -- Tests (use hspec or tasty)
├── my-project.cabal
└── stack.yaml
```

মূল অনুশীলন: IO কে`Main.hs`বা একটি ডেডিকেটেড`IO`মডিউলে রাখুন, মূল যুক্তিকে বিশুদ্ধ এবং পরীক্ষাযোগ্য করুন, ডোমেনের প্রকারের জন্য`newtype`র্যাপার ব্যবহার করুন৷
---

## চেইন-অফ-থট সমস্যা সমাধান
### সমস্যা 1: ত্রুটি রিপোর্টিং সহ একটি নিরাপদ বিভাগ ফাংশন বাস্তবায়ন
**ধাপ 1: সমস্যাটি বুঝুন**
আমাদের এমন বিভাজন দরকার যা শূন্য দ্বারা বিভাজন পরিচালনা করে এবং অর্থপূর্ণ ত্রুটির রিপোর্ট করে, শুধু ক্র্যাশ নয়।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
একটি ত্রুটি বার্তা বা ফলাফল ফেরত দিতে`Either`ব্যবহার করুন৷ এটি টাইপের ক্ষেত্রে ব্যর্থতার সম্ভাবনাকে স্পষ্ট করে তোলে।
**ধাপ 3: প্রয়োগ করুন**```haskell
safeDiv :: Double -> Double -> Either String Double
safeDiv _ 0 = Left "Division by zero"
safeDiv x y = Right (x / y)

-- Chain multiple operations
calc :: Double -> Double -> Double -> Either String Double
calc a b c = do
  ab <- safeDiv a b
  safeDiv ab c

-- Usage
calc 10 2 3   -- Right 1.666...
calc 10 0 3   -- Left "Division by zero"
```

**পদক্ষেপ 4: যাচাই করুন**
টাইপ সিস্টেম গ্যারান্টি দেয় যে কলকারীদের অবশ্যই ত্রুটির ক্ষেত্রে পরিচালনা করতে হবে। প্যাটার্ন ম্যাচিং বা`either`সুস্পষ্ট হ্যান্ডলিং জোর করে।
### সমস্যা 2: একটি সাধারণ কনফিগারেশন ভাষা পার্সিং
**ধাপ 1: সমস্যাটি বুঝুন**
`name=Alice\nage=30` এর মত একটি স্ট্রিং থেকে কী-মান জোড়া পার্স করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
`Text.Parsec` বা ম্যানুয়াল পুনরাবৃত্তি ব্যবহার করুন। সরলতার জন্য,`break`এবং`span`ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```haskell
import Data.Char (isSpace)
import Data.List (stripPrefix)

type Config = [(String, String)]

parseLine :: String -> Maybe (String, String)
parseLine line =
  case break (== '=') (trim line) of
    (key, '=':val) -> Just (trim key, trim val)
    _               -> Nothing
  where trim = reverse . dropWhile isSpace . reverse . dropWhile isSpace

parseConfig :: String -> Config
parseConfig = mapMaybe parseLine . lines

-- Usage
sample = "name = Alice\nage = 30\ncity = Paris"
parseConfig sample
-- [("name","Alice"),("age","30"),("city","Paris")]
```

**ধাপ 4: প্রসারিত করুন**
মন্তব্য পরিচালনা যোগ করুন (`#`), বিভাগ শিরোনাম (`[section]`), এবং`Value`ADT ব্যবহার করে জবরদস্তি টাইপ করুন।
### সমস্যা 3: অলসতার সাথে একটি মেমোাইজড ফিবোনাচি তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
ফিবোনাচি সংখ্যা দক্ষতার সাথে গণনা করুন। নিষ্পাপ পুনরাবৃত্তি সূচকীয়।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
একটি অসীম তালিকা তৈরি করতে হাসকেলের অলস মূল্যায়ন ব্যবহার করুন যেখানে প্রতিটি উপাদান একবার গণনা করা হয় এবং ক্যাশে করা হয়।
**ধাপ 3: প্রয়োগ করুন**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**ধাপ ৪: অপ্টিমাইজ**
র্যান্ডম অ্যাক্সেসের জন্য, অলস নির্মাণের সাথে`Data.Array`ব্যবহার করুন। খুব বড় সূচকের জন্য, O(log n) এ ম্যাট্রিক্স সূচক ব্যবহার করুন।
### সমস্যা 4: একটি সাধারণ স্টেট মেশিন প্রয়োগ করা
**ধাপ 1: সমস্যাটি বুঝুন**
লাল -> সবুজ -> হলুদ -> লাল সাইকেল করে এমন একটি ট্রাফিক লাইট মডেল করুন৷
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
রাজ্যের জন্য একটি বীজগণিত ডেটা টাইপ এবং একটি বিশুদ্ধ রূপান্তর ফাংশন ব্যবহার করুন।
**ধাপ 3: প্রয়োগ করুন**```haskell
data Light = Red | Green | Yellow deriving (Show, Eq)

transition :: Light -> Light
transition Red    = Green
transition Green  = Yellow
transition Yellow = Red

-- Run for n steps
runLight :: Light -> Int -> [Light]
runLight start n = take n (iterate transition start)

-- runLight Red 6  -- [Red,Green,Yellow,Red,Green,Yellow]

-- With state monad for complex state
import Control.Monad.State
type LightState = State Light

tick :: LightState Light
tick = do
  current <- get
  let next = transition current
  put next
  return next
```

**পদক্ষেপ 4: যাচাই করুন**
বিশুদ্ধ ফাংশন তুচ্ছভাবে পরীক্ষাযোগ্য:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## সারাংশ
হাসকেল হল একটি মূলধারার ভাষায় কার্যকরী প্রোগ্রামিংয়ের বিশুদ্ধতম অভিব্যক্তি। এর টাইপ সিস্টেম সবচেয়ে শক্তিশালী, এবং বিশুদ্ধ ফাংশনগুলির উপর এর জোর এমন কোড তৈরি করে যা সম্পর্কে যুক্তি এবং পরীক্ষা করা সহজ। যদিও হাস্কেল শিল্পে ব্যাপকভাবে ব্যবহৃত হয় না, তবে এর ধারণাগুলি আধুনিক প্রোগ্রামিংকে গভীরভাবে প্রভাবিত করেছে। হাস্কেল শেখা আপনি প্রোগ্রামিং সম্পর্কে কীভাবে চিন্তা করেন তা পরিবর্তন করে — এমনকি যদি আপনি এটি পেশাদারভাবে ব্যবহার করেন না।