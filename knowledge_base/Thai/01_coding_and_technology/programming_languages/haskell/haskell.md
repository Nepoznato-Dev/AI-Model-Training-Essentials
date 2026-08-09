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

#ฮาสเคลล์
Haskell เป็นภาษาโปรแกรมที่ใช้งานได้จริง มีการพิมพ์แบบคงที่ และมีการประเมินอย่างเกียจคร้าน มาตรฐานครั้งแรกในปี 1990 (Haskell 90) และปรับปรุงผ่านหลายเวอร์ชัน (Haskell 2010 เป็นมาตรฐานปัจจุบัน) Haskell เป็นที่รู้จักในด้านความแม่นยำทางคณิตศาสตร์ ระบบประเภทที่ทรงพลัง (พร้อมคลาสประเภท monads และประเภทข้อมูลพีชคณิต) และเน้นความถูกต้องผ่านประเภท
Haskell ไม่ใช่ภาษากระแสหลัก แต่มีอิทธิพลอย่างมาก แนวคิดเช่น monads การประเมินแบบขี้เกียจ และคลาสประเภทมีอิทธิพลต่อ Rust, Swift, Kotlin, Scala และ TypeScript Haskell ใช้ในด้านการเงิน (Standard Chartered, Barclays), ผู้เรียบเรียง (GHC) และการตรวจสอบอย่างเป็นทางการ
---

## ทำไม Haskell ถึงมีความสำคัญ
- **ฟังก์ชันล้วนๆ**: ไม่มีผลข้างเคียงตามค่าเริ่มต้น — ฟังก์ชันจะส่งคืนเอาต์พุตเดียวกันสำหรับอินพุตเดียวกันเสมอ
- **ระบบประเภท**: ในบรรดาภาษาที่สื่อความหมายได้ดีที่สุด — พบข้อบกพร่อง ณ เวลาคอมไพล์ ซึ่งภาษาอื่นไม่สามารถทำได้
- **การประเมินแบบ Lazy**: การคำนวณจะถูกเลื่อนออกไปจนกว่าจะจำเป็น ช่วยให้เกิดโครงสร้างข้อมูลที่ไม่มีที่สิ้นสุดและองค์ประกอบที่มีประสิทธิภาพ
- **พื้นฐานทางคณิตศาสตร์**: ขึ้นอยู่กับแคลคูลัสแลมบ์ดาและทฤษฎีหมวดหมู่ โปรแกรมต่างๆ มีความใกล้เคียงกับการพิสูจน์ทางคณิตศาสตร์มากกว่า
- **อิทธิพล**: แนวคิดของ Haskell ได้กำหนดรูปแบบภาษาสมัยใหม่ส่วนใหญ่
- **การทำงานพร้อมกัน**: Software Transactional Memory (STM) ให้การเขียนโปรแกรมพร้อมกันที่หรูหรา
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **เส้นโค้งการเรียนรู้ที่สูงชัน** | Monads, functors, คลาสประเภท — แตกต่างจากภาษาที่จำเป็นมาก | ลงทุนเวลา; แนวคิดสามารถถ่ายโอนได้ |
| **ขี้เกียจประเมินผล** | อาจทำให้เกิดปัญหาการใช้งานหน่วยความจำและประสิทธิภาพโดยไม่คาดคิด | ใช้การประเมินที่เข้มงวด (`!`) ในกรณีที่จำเป็น |
| **ระบบนิเวศเล็กลง** | ไลบรารีน้อยกว่า Python, Java หรือ JavaScript | แฮ็กเกอร์กำลังเติบโต แพ็คเกจคุณภาพมากมาย |
| **ตลาดงาน** | Niche — ส่วนใหญ่เป็นงานด้านการเงิน การวิจัย และงานคอมไพเลอร์ | เติบโตในชุมชนการเขียนโปรแกรมเชิงฟังก์ชัน |
| **ความเร็วในการเรียบเรียง** | GHC อาจช้าได้สำหรับโครงการขนาดใหญ่ | ใช้ GHCi เพื่อการพัฒนาเชิงโต้ตอบ |
---

## พื้นฐานไวยากรณ์
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

## ไวยากรณ์และรูปแบบขั้นสูง
### Type Families — ฟังก์ชันระดับประเภท
ตระกูลประเภทช่วยให้คุณสามารถคำนวณประเภทในระดับประเภทได้ คล้ายกับวิธีที่ฟังก์ชันคำนวณค่าในระดับค่า
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

### GADTs — ประเภทข้อมูลพีชคณิตทั่วไป
GADT ช่วยให้คุณระบุประเภทการส่งคืนของตัวสร้างแต่ละตัวได้อย่างแม่นยำ โดยเปิดใช้งานตัวแปลที่ปลอดภัยสำหรับประเภทและ DSL ที่ฝังไว้
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

### โมนาด ทรานส์ฟอร์มเมอร์ส
หม้อแปลง Monad ซ้อนเอฟเฟกต์แบบ Monadic ทำให้คุณสามารถรวม IO, สถานะ, การจัดการข้อผิดพลาด และอื่นๆ อีกมากมาย
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

### Functor, Applicative และ Monad Hierarchy
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

### การจับคู่รูปแบบขั้นสูง
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

### ขี้เกียจกับการประเมินที่เข้มงวด
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### หน่วยความจำธุรกรรมซอฟต์แวร์ (STM)
STM จัดทำธุรกรรมแบบประกอบได้สำหรับสถานะที่ใช้ร่วมกัน เช่น ธุรกรรมฐานข้อมูล แต่สำหรับหน่วยความจำ
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

### การดำเนินการ Async พร้อมกัน
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

### กลยุทธ์คู่ขนาน
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ (Stack/Cabal)
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

### การกำหนดค่าสแต็ก (stack.yaml)
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

### คำอธิบายแพ็คเกจ (package.yaml สำหรับ hpack)
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

### คำสั่งสร้างคีย์
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `stack new my-project`| สร้างโครงการใหม่จากเทมเพลต |
| `stack build`| สร้างโครงการ |
| `stack ghci`| เริ่ม REPL แบบโต้ตอบโดยโหลดโปรเจ็กต์ |
| `stack test`| เรียกใช้ชุดทดสอบ |
| `stack bench`| เรียกใช้การวัดประสิทธิภาพ |
| `stack haddock`| สร้างเอกสาร |
| `stack exec my-app`| เรียกใช้ไฟล์ปฏิบัติการ |
| `stack clean`| ทำความสะอาดสิ่งประดิษฐ์บิลด์ |
| `stack update`| อัพเดตดัชนีแพ็คเกจ |
| `stack freeze`| ปักหมุดเวอร์ชันการพึ่งพาที่แน่นอน |
### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### HSpec - กรอบการทดสอบหน่วย
HSpec เป็นเฟรมเวิร์กการทดสอบที่ได้รับความนิยมสูงสุด ซึ่งได้รับแรงบันดาลใจจาก RSpec ของ Ruby มันมีไวยากรณ์สไตล์ BDD
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

### การทดสอบตามคุณสมบัติด้วย QuickCheck
QuickCheck สร้างกรณีทดสอบแบบสุ่มเพื่อตรวจสอบคุณสมบัติของโค้ดของคุณ
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

### คำสั่งทดสอบ
| คำสั่ง | คำอธิบาย |
|---------|-------------|
| `stack test`| เรียกใช้ชุดทดสอบทั้งหมด |
| `stack test --fast`| ข้ามการเพิ่มประสิทธิภาพเพื่อการทดสอบบิลด์ที่เร็วขึ้น |
| `stack build --test --test-arguments "--color"`| รันการทดสอบด้วยเอาต์พุตสี |
| `stack ghci --test`| โหลดโมดูลทดสอบใน REPL |

---

## การทำงานร่วมกัน
### C อินเทอร์เฟซฟังก์ชันต่างประเทศ (FFI)
Haskell สามารถเรียกใช้ฟังก์ชัน C ได้โดยตรงและเปิดเผยฟังก์ชัน Haskell ไปที่ C
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

### Python Interop (ผ่าน inline-c หรือ HPy)
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

## รูปแบบการออกแบบ
### รอบชิงชนะเลิศแบบไร้แท็ก (DSL แบบฝัง)
รูปแบบสุดท้ายแบบไม่มีแท็กจะเข้ารหัส DSL โดยใช้คลาสประเภท ทำให้สามารถตีความได้หลากหลาย
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

### Monads ฟรี
พระสงฆ์อิสระแยกคำอธิบายของเอฟเฟกต์ออกจากการตีความ
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

### รูปแบบ ReaderT สำหรับสถาปัตยกรรมแอปพลิเคชัน
รูปแบบ ReaderT เป็นวิธี Haskell ที่ทันสมัยในการฉีดการพึ่งพา
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### เครื่องมือสร้างโปรไฟล์
| เครื่องมือ | วัตถุประสงค์ | คำสั่ง |
|------|---------|---------|
| **ตัวสร้างโปรไฟล์ GHC** | การทำโปรไฟล์เวลาและการจัดสรร | `stack build --profile`แล้วก็`./app +RTS -p`|
| **ขอบเขตเธรด** | แสดงภาพการดำเนินการแบบขนาน | `./app +RTS -l`จากนั้นเปิด`app.eventlog`|
| **ghc-เหตุการณ์** | วิเคราะห์บันทึกเหตุการณ์ | `ghc-events show app.eventlog`|
| **เกณฑ์** | การเปรียบเทียบทางสถิติ | ใช้แพ็คเกจ`criterion`|
| **hp2pretty** | แสดงภาพโปรไฟล์ฮีป | `./app +RTS -h`แล้วก็`hp2pretty app.hp`|
### การเปรียบเทียบด้วยเกณฑ์
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

### เทคนิคการเพิ่มประสิทธิภาพ
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

## การปรับใช้
### ไบนารี่รีลีสอาคาร
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### การปรับใช้นักเทียบท่า
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

### การปรับใช้ตาม Nix
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

## เมื่อใดควรใช้ Haskell
| สถานการณ์ | ทำไมต้อง Haskell | ทางเลือกที่ดีกว่า |
|----------|-----------|-------------------|
| การตรวจสอบอย่างเป็นทางการ | ระบบพิมพ์ช่วยให้การพิสูจน์อักษร | อักด้า, โคค |
| การพัฒนาคอมไพเลอร์ | ยอดเยี่ยมสำหรับการใช้งานภาษา | OCaml, สนิม |
| ระบบการเงิน | ความถูกต้องผ่านประเภท | สกาลา F# |
| การเรียนรู้แนวคิด FP | ภาษาการทำงานที่บริสุทธิ์ที่สุด | Scala (ใช้งานได้จริงมากกว่า), Elm |
| การพัฒนาแอพพลิเคชั่นทั่วไป | เป็นไปได้แต่เฉพาะกลุ่ม | Python, Go, Java |
| การพัฒนาเว็บ | Yesod/Servant มีอยู่แต่จำกัด | จาวาสคริปต์/ไทป์สคริปต์ |
| วิทยาศาสตร์ข้อมูล | ไม่ใช่ระบบนิเวศ | หลาม, อาร์ |
---

## สรุป
Haskell เป็นการแสดงออกที่แท้จริงของการเขียนโปรแกรมเชิงฟังก์ชันในภาษากระแสหลัก ระบบประเภทของระบบเป็นหนึ่งในระบบที่ทรงพลังที่สุด และการเน้นไปที่ฟังก์ชันล้วนๆ จะสร้างโค้ดที่ง่ายต่อการให้เหตุผลและทดสอบ แม้ว่า Haskell จะไม่ได้ใช้กันอย่างแพร่หลายในอุตสาหกรรม แต่แนวคิดของ Haskell ก็มีอิทธิพลอย่างมากต่อการเขียนโปรแกรมสมัยใหม่ การเรียนรู้ Haskell เปลี่ยนวิธีคิดเกี่ยวกับการเขียนโปรแกรม แม้ว่าคุณจะไม่เคยใช้มันอย่างมืออาชีพก็ตาม