---
# Metadata
title: "Haskell"
description: "Comprehensive reference for the Haskell programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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
# هاسکل
Haskell یک زبان برنامه نویسی کاملا کاربردی، تایپ ایستا و با تنبلی ارزیابی شده است. هاسکل برای اولین بار در سال 1990 استاندارد شد (Haskell 90) و از طریق چندین نسخه اصلاح شد (Haskell 2010 استاندارد فعلی است)، Haskell به دلیل دقت ریاضی، سیستم تایپ قدرتمند (با کلاس‌های نوع، مونادها و انواع داده‌های جبری) و تاکید بر صحت از طریق انواع شناخته شده است.
هاسکل یک زبان رایج نیست، اما تأثیر آن بسیار زیاد است. مفاهیمی مانند monads، ارزیابی تنبل و کلاس‌های نوع بر Rust، Swift، Kotlin، Scala و TypeScript تأثیر گذاشته‌اند. Haskell در امور مالی (Standard Chartered، Barclays)، کامپایلرها (GHC) و تأیید رسمی استفاده می شود.
---

## چرا هاسکل مهم است
- **توابع خالص**: بدون عوارض جانبی به طور پیش فرض - توابع همیشه خروجی یکسانی را برای ورودی یکسان برمی گرداند.
- **سیستم تایپ**: یکی از رساترین زبان ها است - اشکالاتی را در زمان کامپایل پیدا می کند که زبان های دیگر نمی توانند.
- **ارزیابی تنبل**: محاسبات تا زمانی که نیاز باشد به تعویق می افتد - ساختارهای داده بی نهایت و ترکیب کارآمد را فعال می کند.
- **مبنای ریاضی **: بر اساس حساب لامبدا و نظریه دسته - برنامه ها به اثبات های ریاضی نزدیک تر هستند.
- **تأثیر**: ایده های هاسکل بیشتر زبان های مدرن را شکل داده است.
- **همزمان**: حافظه تراکنش نرم افزاری (STM) برنامه نویسی همزمان زیبا را ارائه می دهد.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **منحنی یادگیری شیب دار** | مونادها، تابع‌ها، کلاس‌های نوع - بسیار متفاوت از زبان‌های امری | زمان سرمایه گذاری؛ مفاهیم قابل انتقال هستند |
| **سوپرایز ارزشیابی تنبل** | می تواند باعث استفاده غیرمنتظره از حافظه و مشکلات عملکرد شود | در صورت نیاز از ارزیابی دقیق (`!`) استفاده کنید |
| **اکوسیستم کوچکتر** | کتابخانه های کمتری نسبت به پایتون، جاوا یا جاوا اسکریپت | هک در حال رشد است. بسته های بسیار با کیفیت |
| **بازار کار** | طاقچه - بیشتر امور مالی، تحقیقاتی و کامپایلر | رشد در جوامع برنامه نویسی کاربردی |
| **سرعت تدوین** | GHC می تواند برای پروژه های بزرگ کند باشد | استفاده از GHCi برای توسعه تعاملی |
---

## اصول نحو
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

## نحو و الگوهای پیشرفته
### نوع خانواده - توابع سطح نوع
خانواده های نوع به شما امکان می دهند انواع را در سطح نوع محاسبه کنید، مشابه نحوه محاسبه توابع مقادیر در سطح ارزش.
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

### GADT - انواع داده های جبری تعمیم یافته
GADT ها به شما امکان می دهند نوع برگشتی هر سازنده را دقیقاً مشخص کنید و مفسرهای ایمن نوع و DSL های تعبیه شده را فعال می کند.
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

### ترانسفورماتور موناد
ترانسفورماتورهای موناد جلوه های مونادیک را روی هم قرار می دهند و به شما امکان می دهند IO، حالت، مدیریت خطا و موارد دیگر را ترکیب کنید.
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

### سلسله مراتب تابع، کاربردی و موناد
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

### تطبیق الگوی پیشرفته
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

### تنبل در مقابل ارزیابی دقیق
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

## همزمانی و موازی
### حافظه تراکنش نرم افزاری (STM)
STM تراکنش های قابل ترکیب را برای حالت اشتراکی فراهم می کند - مانند تراکنش های پایگاه داده اما برای حافظه.
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

### عملیات Async همزمان
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

### استراتژی های موازی
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه (Stack/Cabal)
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

### پیکربندی پشته (stack.yaml)
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

### توضیحات بسته (package.yaml برای hpack)
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

### دستورات ساخت کلید
| فرمان | توضیحات |
|---------|-------------|
| `stack new my-project`| ایجاد پروژه جدید از قالب |
| `stack build`| ساخت پروژه |
| `stack ghci`| شروع REPL تعاملی با پروژه بارگذاری شده |
| `stack test`| اجرای مجموعه تست |
| `stack bench`| اجرای معیارها |
| `stack haddock`| ایجاد مستندات |
| `stack exec my-app`| اجرای |
| `stack clean`| مصنوعات ساخت تمیز |
| `stack update`| به روز رسانی فهرست بسته |
| `stack freeze`| پین کردن نسخه های وابستگی دقیق |
### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### HSpec - چارچوب تست واحد
HSpec محبوب ترین چارچوب تست است که از RSpec الهام گرفته شده است. این یک نحو به سبک BDD ارائه می دهد.
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

### تست مبتنی بر ویژگی با QuickCheck
QuickCheck موارد آزمایشی تصادفی را برای تأیید ویژگی‌های کد شما ایجاد می‌کند.
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

### دستورات تست
| فرمان | توضیحات |
|---------|-------------|
| `stack test`| اجرای تمامی مجموعه های تست |
| `stack test --fast`| رد شدن از بهینه سازی برای ساخت های آزمایشی سریعتر |
| `stack build --test --test-arguments "--color"`| اجرای تست ها با خروجی رنگی |
| `stack ghci --test`| بارگذاری ماژول های تست در REPL |

---

## قابلیت همکاری
### C رابط عملکرد خارجی (FFI)
Haskell می تواند توابع C را مستقیماً فراخوانی کند و توابع Haskell را در معرض C قرار دهد.
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

### Python Interop (از طریق inline-c یا HPy)
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

## الگوهای طراحی
### نهایی بدون برچسب (DSL های تعبیه شده)
سبک نهایی بدون برچسب، DSL ها را با استفاده از کلاس های نوع رمزگذاری می کند و تفسیرهای متعدد را امکان پذیر می کند.
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

### موناد رایگان
مونادهای رایگان شرح افکت ها را از تفسیرشان جدا می کنند.
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

### الگوی ReaderT برای معماری کاربردی
الگوی ReaderT رویکرد مدرن Haskell برای تزریق وابستگی است.
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

## عملکرد و بهینه سازی
### ابزارهای پروفایل
| ابزار | هدف | فرمان |
|------|---------|---------|
| **پروفایلر GHC** | پروفایل زمان و تخصیص | `stack build --profile`سپس`./app +RTS -p`|
| **ThreadScope** | تجسم اجرای موازی | `./app +RTS -l`سپس`app.eventlog`|
| **ghc-events** | تجزیه و تحلیل گزارش رویداد | `ghc-events show app.eventlog`|
| **معیار** | معیارهای آماری | استفاده از بسته`criterion`|
| **hp2pretty** | تجسم پروفایل های پشته | `./app +RTS -h`سپس`hp2pretty app.hp`|
### محک زدن با معیار
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

### تکنیک های بهینه سازی
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

## استقرار
### باینری های انتشار ساختمان
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### استقرار داکر
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

### استقرار مبتنی بر Nix
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

## چه زمانی از Haskell استفاده کنیم
| سناریو | چرا هاسکل | جایگزین بهتر |
|----------|----------|------------------|
| تایید رسمی | سیستم نوع اثبات را فعال می کند | Agda، Coq |
| توسعه کامپایلر | عالی برای پیاده سازی زبان | OCaml، Rust |
| سیستم های مالی | صحت از طریق انواع | اسکالا، F# |
| یادگیری مفاهیم FP | ناب ترین زبان کاربردی | Scala (عملی تر)، Elm |
| توسعه برنامه عمومی | ممکن است اما طاقچه | پایتون، برو، جاوا |
| توسعه وب | Yesod/Servant وجود دارد اما محدود | جاوا اسکریپت/تایپ اسکریپت |
| علم داده | نه اکوسیستم | پایتون، R |
---

## پرسش و پاسخ مصنوعی
### Q1: ارزیابی تنبل Haskell چگونه بر عملکرد تأثیر می گذارد؟
**A:** ارزیابی تنبل به این معنی است که عبارات فقط در صورت نیاز محاسبه می شوند و ساختارهای داده بی نهایت و خطوط لوله قابل ترکیب را فعال می کنند. با این حال، در صورت انباشته شدن ضربات می تواند باعث نشت فضا شود:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

از`foldl'`(از`Data.List`) به جای`foldl`برای چین های عددی استفاده کنید. از الگوهای ضربه ای`!`یا`seq`برای ارزیابی در صورت نیاز استفاده کنید.
### Q2: تفاوت عملی بین `Functor`،`Applicative`و`Monad`چیست؟
**A:** هر کلاس تایپ قابلیتی را اضافه می کند:
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

**Functor** یک تابع خالص را روی یک زمینه ترسیم می کند. **کاربردی** توابعی را اعمال می کند که خودشان در یک زمینه هستند. **موناد** اجازه می دهد هر مرحله به نتیجه مرحله قبل بستگی داشته باشد. در عمل: از`fmap`/`<$>`برای تبدیل های ساده،`<*>`برای ترکیب افکت ها و`>>=`/`do`برای محاسبات وابسته متوالی استفاده کنید.
### Q3: چگونه عوارض جانبی را در کد Haskell خالص کنترل کنم؟
**A:** از سیستم نوع برای جداسازی کدهای خالص و موثر استفاده کنید:
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

منطق اصلی را خالص نگه دارید و جلوه ها را به لبه ها فشار دهید. از`ReaderT`برای پیکربندی،`ExceptT`برای خطاها و`StateT`برای حالت تغییرپذیر استفاده کنید.
### Q4: کلاس های نوع چیست و چه تفاوتی با رابط های OOP دارند؟
**A:** کلاس های نوع رفتاری را تعریف می کنند که انواع می توانند پیاده سازی کنند. برخلاف رابط های OOP، آنها باز هستند (هر نوع می تواند یک نمونه باشد) و از چند شکلی ad-hoc پشتیبانی می کنند:
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

### Q5: چگونه یک پروژه Haskell را برای استفاده در دنیای واقعی ساختار دهم؟
**A:** از Cabal یا Stack با یک چیدمان استاندارد استفاده کنید:
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

روش‌های کلیدی: IO را در`Main.hs`یا یک ماژول اختصاصی`IO`نگه دارید، منطق هسته را خالص و قابل آزمایش کنید، از پوشش‌های`newtype`برای انواع دامنه استفاده کنید.
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: اجرای یک تابع بخش ایمن با گزارش خطا
**مرحله 1: مشکل را درک کنید**
ما به تقسیمی نیاز داریم که تقسیم بر صفر را مدیریت کند و خطاهای معنی دار را گزارش کند، نه فقط خرابی ها.
**مرحله 2: رویکرد را شناسایی کنید**
از`Either`برای بازگرداندن پیام خطا یا نتیجه استفاده کنید. این باعث می شود که احتمال شکست در نوع صریح باشد.
**مرحله 3: پیاده سازی **```haskell
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

**مرحله 4: تایید **
سیستم نوع تضمین می‌کند که تماس‌گیرندگان باید مورد خطا را مدیریت کنند. تطبیق الگو یا`either`مدیریت صریح را مجبور می کند.
### مشکل 2: تجزیه یک زبان پیکربندی ساده
**مرحله 1: مشکل را درک کنید**
جفت‌های کلید-مقدار را از رشته‌ای مانند`name=Alice\nage=30`تجزیه کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از`Text.Parsec`یا بازگشت دستی استفاده کنید. برای سادگی، از`break`و`span`استفاده کنید.
**مرحله 3: پیاده سازی **```haskell
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

**مرحله 4: تمدید**
مدیریت نظر (`#`)، سرصفحه‌های بخش (`[section]`) را اضافه کنید و با استفاده از`Value`ADT، اجبار را تایپ کنید.
### مسئله 3: ساختن یک فیبوناچی یادداشت شده با تنبلی
**مرحله 1: مشکل را درک کنید**
اعداد فیبوناچی را به طور موثر محاسبه کنید. بازگشت ساده لوح نمایی است.
**مرحله 2: رویکرد را شناسایی کنید**
از ارزیابی تنبل Haskell برای ایجاد یک لیست بی نهایت استفاده کنید که در آن هر عنصر یک بار محاسبه شده و در حافظه پنهان ذخیره می شود.
**مرحله 3: پیاده سازی **```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**مرحله 4: بهینه سازی**
برای دسترسی تصادفی، از`Data.Array`با ساختار تنبل استفاده کنید. برای شاخص های بسیار بزرگ، از توان ماتریسی در O(log n) استفاده کنید.
### مسئله 4: پیاده سازی یک ماشین حالت ساده
**مرحله 1: مشکل را درک کنید**
یک چراغ راهنمایی که چرخه های قرمز -> سبز -> زرد -> قرمز را در می آورد مدل کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از یک نوع داده جبری برای حالت ها و یک تابع انتقال خالص استفاده کنید.
**مرحله 3: پیاده سازی **```haskell
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

**مرحله 4: تایید **
توابع خالص به طور ساده قابل آزمایش هستند:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## خلاصه
Haskell خالص ترین بیان برنامه نویسی تابعی در یک زبان رایج است. نوع سیستم آن یکی از قدرتمندترین ها است و تأکید آن بر توابع خالص کدی را تولید می کند که استدلال و آزمایش آن آسان تر است. در حالی که Haskell به طور گسترده در صنعت استفاده نمی شود، ایده های آن عمیقاً بر برنامه نویسی مدرن تأثیر گذاشته است. یادگیری Haskell طرز فکر شما را در مورد برنامه نویسی تغییر می دهد - حتی اگر هرگز به طور حرفه ای از آن استفاده نکنید.