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

# ہاسکل
ہاسکل ایک مکمل طور پر فعال، مستحکم طور پر ٹائپ کی گئی، سستی سے تشخیص شدہ پروگرامنگ زبان ہے۔ سب سے پہلے 1990 میں معیاری بنایا گیا (Haskell 90) اور متعدد ورژنز کے ذریعے بہتر کیا گیا (Haskell 2010 موجودہ معیار ہے)، Haskell اپنی ریاضی کی سختی، طاقتور قسم کے نظام (ٹائپ کلاسز، مونڈز، اور الجبری ڈیٹا کی اقسام کے ساتھ)، اور اقسام کے ذریعے درستگی پر زور دینے کے لیے جانا جاتا ہے۔
ہاسکل مرکزی دھارے کی زبان نہیں ہے، لیکن اس کا اثر بہت زیادہ ہے۔ مونڈز، سست تشخیص، اور قسم کی کلاسوں جیسے تصورات نے Rust، Swift، Kotlin، Scala، اور TypeScript کو متاثر کیا ہے۔ ہاسکل فنانس (اسٹینڈرڈ چارٹرڈ، بارکلیز)، کمپائلرز (GHC) اور رسمی تصدیق میں استعمال ہوتا ہے۔
---

## ہاسکل کیوں اہمیت رکھتا ہے۔
- **خالص افعال**: ڈیفالٹ کے طور پر کوئی ضمنی اثرات نہیں - فنکشنز ہمیشہ ایک ہی ان پٹ کے لیے ایک ہی آؤٹ پٹ واپس کرتے ہیں۔
- **ٹائپ سسٹم**: کسی بھی زبان کا سب سے زیادہ اظہار کرنے والا - کمپائل کے وقت کیڑے پکڑتا ہے جو دوسری زبانیں نہیں کر سکتیں۔
- **سست تشخیص**: ضرورت کے مطابق حسابات کو موخر کر دیا جاتا ہے — ڈیٹا کے لامحدود ڈھانچے اور موثر کمپوزیشن کو قابل بناتا ہے۔
- **ریاضیاتی بنیاد**: لیمبڈا کیلکولس اور زمرہ تھیوری پر مبنی — پروگرام ریاضی کے ثبوت کے قریب ہوتے ہیں۔
- **اثر**: ہاسکل کے خیالات نے زیادہ تر جدید زبانوں کو تشکیل دیا ہے۔
- **کنکرنسی**: سافٹ ویئر ٹرانزیکشنل میموری (STM) خوبصورت سمورتی پروگرامنگ فراہم کرتی ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **کھڑا سیکھنے کا وکر** | مونڈز، فنیکٹرز، قسم کی کلاسز - لازمی زبانوں سے بہت مختلف | وقت کی سرمایہ کاری؛ تصورات قابل منتقلی ہیں |
| **سست تشخیص حیرت** | غیر متوقع طور پر میموری کے استعمال اور کارکردگی کے مسائل کا سبب بن سکتا ہے۔ جہاں ضرورت ہو سخت تشخیص (`!`) استعمال کریں۔
| **چھوٹا ماحولیاتی نظام** | Python، Java، یا JavaScript سے کم لائبریریاں | ہیکیج بڑھ رہا ہے؛ بہت سے معیار کے پیکجز |
| **ملازمت کی منڈی** | طاق - زیادہ تر فنانس، تحقیق، اور مرتب کرنے والا کام | فنکشنل پروگرامنگ کمیونٹیز میں بڑھنا |
| **تالیف کی رفتار** | GHC بڑے منصوبوں کے لیے سست ہو سکتا ہے | انٹرایکٹو ترقی کے لیے GHCi استعمال کریں |
---

## نحوی بنیادی باتیں
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

## اعلی درجے کی نحو اور نمونے۔
### خاندانوں کی قسم — قسم کی سطح کے افعال
قسم کے خاندان آپ کو قسم کی سطح پر اقسام کی گنتی کرنے کی اجازت دیتے ہیں، جیسا کہ فنکشنز قدر کی سطح پر اقدار کی گنتی کرتے ہیں۔
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

### GADTs — عام الجبری ڈیٹا کی اقسام
GADTs آپ کو ہر ایک کنسٹرکٹر کی واپسی کی قسم کو قطعی طور پر بتانے دیتا ہے، ٹائپ سیف انٹرپریٹرز اور ایمبیڈڈ DSLs کو فعال کرتے ہوئے۔
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

### مونڈ ٹرانسفارمرز
مونڈ ٹرانسفارمرز موناڈک اثرات کو اسٹیک کرتے ہیں، آپ کو IO، ریاست، غلطی سے نمٹنے اور مزید کو یکجا کرنے دیتے ہیں۔
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

### فنیکٹر، اطلاقی، اور مونڈ درجہ بندی
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

### ایڈوانس پیٹرن میچنگ
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

### سست بمقابلہ سخت تشخیص
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

## ہم آہنگی اور ہم آہنگی
### سافٹ ویئر ٹرانزیکشنل میموری (STM)
STM مشترکہ حالت کے لیے کمپوز ایبل ٹرانزیکشن فراہم کرتا ہے — جیسے ڈیٹا بیس ٹرانزیکشنز لیکن میموری کے لیے۔
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

### کنکرنٹ Async آپریشنز
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

### متوازی حکمت عملی
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ (اسٹیک/کیبل)
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

### اسٹیک کنفیگریشن (stack.yaml)
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

### پیکیج کی تفصیل (hpack کے لیے package.yaml)
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

### کلیدی بلڈ کمانڈز
| کمانڈ | تفصیل |
|---------|---------------|
| `stack new my-project`| ٹیمپلیٹ سے نیا پروجیکٹ بنائیں |
| `stack build`| منصوبے کی تعمیر |
| `stack ghci`| بھری ہوئی پروجیکٹ کے ساتھ انٹرایکٹو REPL شروع کریں |
| `stack test`| ٹیسٹ سویٹ چلائیں |
| `stack bench`| بینچ مارکس چلائیں |
| `stack haddock`| دستاویزات بنائیں |
| `stack exec my-app`| قابل عمل چلائیں |
| `stack clean`| تعمیراتی نمونے صاف کریں |
| `stack update`| پیکیج انڈیکس کو اپ ڈیٹ کریں |
| `stack freeze`| عین انحصاری ورژن پن |
### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### HSpec — یونٹ ٹیسٹنگ فریم ورک
HSpec سب سے مقبول ٹیسٹنگ فریم ورک ہے، جو روبی کے RSpec سے متاثر ہے۔ یہ BDD طرز کا نحو فراہم کرتا ہے۔
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

### QuickCheck کے ساتھ پراپرٹی پر مبنی جانچ
QuickCheck آپ کے کوڈ کی خصوصیات کی تصدیق کرنے کے لیے بے ترتیب ٹیسٹ کیسز تیار کرتا ہے۔
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

### ٹیسٹ کمانڈز
| کمانڈ | تفصیل |
|---------|---------------|
| `stack test`| تمام ٹیسٹ سویٹس چلائیں |
| `stack test --fast`| تیز تر ٹیسٹ بنانے کے لیے اصلاح کو چھوڑیں |
| `stack build --test --test-arguments "--color"`| رنگین آؤٹ پٹ کے ساتھ ٹیسٹ چلائیں |
| `stack ghci --test`| REPL میں ٹیسٹ ماڈیول لوڈ کریں |

---

## انٹرآپریبلٹی
### C غیر ملکی فنکشن انٹرفیس (FFI)
ہاسکل سی فنکشنز کو براہ راست کال کر سکتا ہے اور ہاسکل کے فنکشنز کو سی میں ظاہر کر سکتا ہے۔
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

### Python Interop (بذریعہ inline-c یا HPy)
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

## ڈیزائن پیٹرن
### ٹیگ لیس فائنل (ایمبیڈڈ DSLs)
ٹیگ لیس فائنل اسٹائل DSLs کو ٹائپ کلاسز کا استعمال کرتے ہوئے انکوڈ کرتا ہے، متعدد تشریحات کو فعال کرتا ہے۔
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

### مفت مونڈز
مفت مونڈز اثرات کی تفصیل کو ان کی تشریح سے الگ کرتے ہیں۔
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

### ایپلیکیشن آرکیٹیکچر کے لیے ریڈر ٹی پیٹرن
ریڈر ٹی پیٹرن انحصار انجیکشن کے لئے جدید ہاسکل نقطہ نظر ہے۔
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

## کارکردگی اور اصلاح
### پروفائلنگ ٹولز
| ٹول | مقصد | کمانڈ |
|------|---------|---------|
| **GHC پروفائلر** | وقت اور مختص پروفائلنگ | `stack build --profile`پھر`./app +RTS -p`|
| **تھریڈ اسکوپ** | متوازی عمل درآمد کا تصور کریں | `./app +RTS -l`پھر`app.eventlog`| کھولیں۔
| **GHc-ایونٹس** | ایونٹ لاگز کا تجزیہ کریں | `ghc-events show app.eventlog`|
| **معیار** | شماریاتی بینچ مارکنگ |`criterion`پیکیج استعمال کریں۔
| **hp2pretty** | ہیپ پروفائلز کا تصور کریں | `./app +RTS -h`پھر`hp2pretty app.hp`|
### معیار کے ساتھ بینچ مارکنگ
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

### اصلاح کی تکنیک
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

## تعیناتی۔
### بلڈنگ ریلیز بائنریز
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### ڈاکر کی تعیناتی۔
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

### نکس پر مبنی تعیناتی۔
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

## ہاسکل کب استعمال کریں۔
| منظر نامہ | کیوں ہاسکل | بہتر متبادل |
|------------|------------|-------------------|
| رسمی تصدیق | ٹائپ سسٹم ثبوتوں کو قابل بناتا ہے | Agda، Coq |
| کمپائلر کی ترقی | زبان کے نفاذ کے لیے بہترین | OCaml، زنگ |
| مالیاتی نظام | اقسام کے ذریعے درستگی | Scala, F# |
| FP تصورات سیکھنا | خالص ترین فعال زبان | اسکالا (زیادہ عملی)، ایلم |
| عام درخواست کی ترقی | ممکن لیکن طاق | ازگر، گو، جاوا |
| ویب ڈویلپمنٹ | یسوڈ/خادم موجود ہیں لیکن محدود | JavaScript/TypeScript |
| ڈیٹا سائنس | ماحولیاتی نظام نہیں | ازگر، آر |
---

## مصنوعی سوال و جواب
### Q1: ہاسکل کی سست تشخیص کارکردگی کو کیسے متاثر کرتی ہے؟
**A:** سست تشخیص کا مطلب ہے کہ تاثرات کی گنتی صرف ضرورت کے وقت کی جاتی ہے، لامحدود ڈیٹا سٹرکچرز اور کمپوز ایبل پائپ لائنز کو فعال کرنا۔ تاہم، اگر تھنک جمع ہو جائیں تو یہ جگہ کے رساو کا سبب بن سکتا ہے:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

عددی تہوں کے لیے`foldl`کی بجائے`foldl'`(`Data.List` سے) استعمال کریں۔ ضرورت پڑنے پر تشخیص پر مجبور کرنے کے لیے`!`بینگ پیٹرن یا`seq`استعمال کریں۔
### Q2: `Functor`، `Applicative`، اور`Monad`کے درمیان کیا عملی فرق ہے؟
**A:** ہر قسم کی کلاس صلاحیت کا اضافہ کرتی ہے:
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

**فنٹر** ایک سیاق و سباق پر خالص فنکشن کا نقشہ بناتا ہے۔ **Applicative** ان افعال کا اطلاق کرتا ہے جو خود ایک سیاق و سباق میں ہوتے ہیں۔ **موناد** ہر قدم کو پچھلے مرحلے کے نتیجہ پر منحصر کرنے دیتا ہے۔ عملی طور پر: سادہ تبدیلیوں کے لیے`fmap`/ `<$>`، اثرات کو یکجا کرنے کے لیے `<*>`، اور ترتیب وار منحصر حسابات کے لیے`>>=`/`do`استعمال کریں۔
### Q3: میں خالص ہاسکل کوڈ میں ضمنی اثرات کو کیسے سنبھال سکتا ہوں؟
**A:** خالص اور مؤثر کوڈ کو الگ کرنے کے لیے ٹائپ سسٹم کا استعمال کریں:
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

بنیادی منطق کو خالص رکھیں اور اثرات کو کناروں تک دھکیلیں۔ ترتیب کے لیے `ReaderT`، غلطیوں کے لیے `ExceptT`، اور متغیر حالت کے لیے`StateT`استعمال کریں۔
### Q4: ٹائپ کلاسز کیا ہیں اور وہ OOP انٹرفیس سے کیسے مختلف ہیں؟
**A:** قسم کی کلاسیں رویے کی وضاحت کرتی ہیں جسے اقسام لاگو کر سکتی ہیں۔ OOP انٹرفیس کے برعکس، وہ کھلے ہیں (کسی بھی قسم کی مثال ہوسکتی ہے) اور ایڈہاک پولیمورفزم کی حمایت کرتے ہیں:
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

### Q5: میں حقیقی دنیا کے استعمال کے لیے ہاسکل پروجیکٹ کیسے بناؤں؟
**A:** معیاری ترتیب کے ساتھ کیبل یا اسٹیک استعمال کریں:
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

کلیدی طرز عمل: IO کو`Main.hs`یا ایک وقف شدہ`IO`ماڈیول میں رکھیں، بنیادی منطق کو خالص اور قابل آزمائش بنائیں، ڈومین کی اقسام کے لیے`newtype`ریپرز کا استعمال کریں۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: ایرر رپورٹنگ کے ساتھ سیف ڈویژن فنکشن کو نافذ کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
ہمیں ایسی تقسیم کی ضرورت ہے جو صفر کے حساب سے تقسیم کو ہینڈل کرے اور بامعنی غلطیوں کی اطلاع دے، نہ کہ کریش۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
غلطی کا پیغام یا نتیجہ واپس کرنے کے لیے`Either`استعمال کریں۔ یہ قسم میں ناکامی کے امکان کو واضح کرتا ہے۔
**مرحلہ 3: نافذ کریں**```haskell
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

**مرحلہ 4: تصدیق کریں**
قسم کا نظام اس بات کی ضمانت دیتا ہے کہ کال کرنے والوں کو غلطی کے معاملے کو ہینڈل کرنا چاہیے۔ پیٹرن میچنگ یا`either`واضح ہینڈلنگ پر مجبور کرتا ہے۔
### مسئلہ 2: ایک سادہ کنفیگریشن زبان کو پارس کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
`name=Alice\nage=30` جیسے سٹرنگ سے کلیدی قدر کے جوڑے پارس کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
`Text.Parsec` یا دستی تکرار کا استعمال کریں۔ سادگی کے لیے،`break`اور`span`استعمال کریں۔
**مرحلہ 3: نافذ کریں**```haskell
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

**مرحلہ 4: توسیع کریں**
تبصرہ ہینڈلنگ (`#`)، سیکشن ہیڈر ( `[section]`) شامل کریں، اور`Value`ADT کا استعمال کرتے ہوئے جبر ٹائپ کریں۔
### مسئلہ 3: سستی کے ساتھ میموائزڈ فبونیکی بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
فبونیکی نمبروں کی مؤثر طریقے سے گنتی کریں۔ بولی تکرار کفایتی ہے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
ایک لامحدود فہرست بنانے کے لیے ہاسکل کی سست تشخیص کا استعمال کریں جہاں ہر عنصر کو ایک بار شمار کیا جاتا ہے اور کیش کیا جاتا ہے۔
**مرحلہ 3: نافذ کریں**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**مرحلہ 4: بہتر بنائیں**
بے ترتیب رسائی کے لیے، سست تعمیر کے ساتھ`Data.Array`استعمال کریں۔ بہت بڑے اشاریہ جات کے لیے، O(log n) میں میٹرکس کی شرح کا استعمال کریں۔
### مسئلہ 4: ایک سادہ ریاستی مشین کا نفاذ
**مرحلہ 1: مسئلہ کو سمجھیں**
ایک ٹریفک لائٹ کا ماڈل بنائیں جو سرخ -> سبز -> پیلا -> سرخ چکر لگاتی ہے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
ریاستوں اور خالص منتقلی کے فنکشن کے لیے الجبری ڈیٹا کی قسم کا استعمال کریں۔
**مرحلہ 3: نافذ کریں**```haskell
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

**مرحلہ 4: تصدیق کریں**
خالص افعال معمولی طور پر قابل آزمائش ہیں:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## خلاصہ
ہاسکل مرکزی دھارے کی زبان میں فنکشنل پروگرامنگ کا خالص ترین اظہار ہے۔ اس کا قسم کا نظام سب سے زیادہ طاقتور ہے، اور خالص افعال پر اس کا زور ایسا کوڈ تیار کرتا ہے جس کے بارے میں استدلال اور جانچ کرنا آسان ہے۔ اگرچہ ہاسکل صنعت میں بڑے پیمانے پر استعمال نہیں ہوتا ہے، لیکن اس کے خیالات نے جدید پروگرامنگ پر گہرا اثر ڈالا ہے۔ ہاسکل سیکھنا پروگرامنگ کے بارے میں آپ کے سوچنے کے انداز کو بدل دیتا ہے — چاہے آپ اسے پیشہ ورانہ طور پر کبھی استعمال نہ کریں۔