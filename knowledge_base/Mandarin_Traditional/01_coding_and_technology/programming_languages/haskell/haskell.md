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

# 哈斯克爾
Haskell 是一種純函數式、靜態型別、延遲計算的程式語言。 Haskell 於 1990 年首次標準化（Haskell 90），並透過多個版本進行完善（Haskell 2010 是當前標準），Haskell 以其嚴謹性、強大的類型系統（具有類型類、單子和代數資料類型）以及對類型正確性的強調而聞名。
Haskell 不是主流語言，但其影響力卻是巨大的。諸如 monad、惰性求值和類型類之類的概念影響了 Rust、Swift、Kotlin、Scala 和 TypeScript。 Haskell 用於金融（渣打銀行、巴克萊銀行）、編譯器（GHC）和形式驗證。
---

## 為什麼 Haskell 很重要
- **純函數**：預設沒有副作用 - 函數始終為相同的輸入傳回相同的輸出。
- **類型系統**：是最具表現力的語言之一 - 在編譯時捕獲其他語言無法捕獲的錯誤。
- **惰性計算**：計算被推遲到需要時為止 - 實現無限的資料結構和高效的組合。
- **數學基礎**：基於 lambda 演算和範疇論 - 程式更接近數學證明。
- **影響**：哈斯克爾的思想塑造了大多數現代語言。
- **並發**：軟體事務記憶體（STM）提供優雅的並發程式設計。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **陡峭的學習曲線** | Monad、函子、型別類別－與命令式語言非常不同 |投入時間；這些概念是可以轉移的|
| **懶惰評價有驚喜** |可能會導致意外的記憶體使用和效能問題 |在需要時使用嚴格評估 (`!`) |
| **較小的生態系統** |比 Python、Java 或 JavaScript 更少的函式庫 | Hackage 正在成長；眾多優質方案|
| **就業市場** |利基市場－主要是金融、研究和編譯工作 |在函數式程式設計社群中成長 |
| **編譯速度** |對於大型項目，GHC 可能會很慢 |使用GHCi進行互動式開發 |
---

## 文法基礎知識
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

## 進階語法和模式
### 類型族 — 類型級函數
類型族允許您在類型層級計算類型，類似於函數在值層級計算值的方式。
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

### GADT — 廣義代數資料型
GADT 可讓您精確指定每個建構函式的傳回類型，從而啟用類型安全解釋器和嵌入式 DSL。
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

### 莫納德變形金剛
Monad 轉換器堆疊 Monadic 效果，讓您可以組合 IO、狀態、錯誤處理等。
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

### 函子、應用與 Monad 層次結構
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

### 進階模式匹配
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

### 惰性評估與嚴格評估
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

## 並發與平行
### 軟體事務記憶體 (STM)
STM 為共享狀態提供可組合事務－類似於資料庫事務，但用於記憶體。
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

### 並發非同步操作
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

### 平行策略
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

## 專案配置與建置系統
### 專案結構（堆疊/陰謀）
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

### 堆疊配置（stack.yaml）
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

### 套件描述（hpack 的 package.yaml）
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

### 關鍵建置命令
|命令 |描述 |
|---------|-------------|
|`stack new my-project`|從範本建立新專案 |
|`stack build`|建置專案|
|`stack ghci`|啟動互動式 REPL 並載入專案 |
|`stack test`|運行測試套件 |
|`stack bench`|執行基準測試 |
|`stack haddock`|產生文件 |
|`stack exec my-app`|執行執行檔 |
|`stack clean`|清理建置工件 |
|`stack update`|更新套件索引 |
|`stack freeze`|固定確切的依賴版本 |
### CI/CD 管道 (GitHub Actions)
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

## 測試
### HSpec — 單元測試框架
HSpec 是最受歡迎的測試框架，受到 Ruby 的 RSpec 的啟發。它提供了 BDD 風格的語法。
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

### 使用 QuickCheck 進行基於屬性的測試
QuickCheck 產生隨機測試用例來驗證程式碼的屬性。
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

### 測試命令
|命令 |描述 |
|---------|-------------|
|`stack test`|運行所有測試套件 |
|`stack test --fast`|跳過最佳化以獲得更快的測試建置 |
|`stack build --test --test-arguments "--color"`|使用彩色輸出運行測試 |
|`stack ghci --test`|在 REPL 中載入測試模組 |

---

## 互通性
### C 外部函數介面 (FFI)
Haskell 可以直接呼叫 C 函數，並將 Haskell 函數暴露給 C。
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

### Python 互通（透過 inline-c 或 HPy）
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

## 設計模式
### Tagless Final（嵌入式 DSL）
無標籤最終樣式使用類型類別對 DSL 進行編碼，從而實現多種解釋。
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

### 免費 Monad
自由單子將效果的描述與其解釋分開。
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

### 應用程式架構的 ReaderT 模式
ReaderT 模式是現代 Haskell 依賴注入法。
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

## 效能與最佳化
### 分析工具
|工具|目的|命令 |
|------|---------|---------|
| **GHC 分析器** |時間與分配分析 |`stack build --profile`然後`./app +RTS -p`|
| **執行緒範圍** |視覺化並行執行 |`./app +RTS -l`然後開啟`app.eventlog`|
| **ghc-事件** |分析事件日誌 |`ghc-events show app.eventlog`|
| **標準** |統計標竿|使用`criterion`封裝|
| **hp2漂亮** |視覺化堆疊設定檔 |`./app +RTS -h`然後`hp2pretty app.hp`|
### 用標準進行基準測試
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

### 優化技術
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

## 部署
### 建置發布二進位文件
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### Docker 部署
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

### 基於 Nix 的部署
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

## 何時使用 Haskell
|場景|為什麼選擇 Haskell |更好的選擇|
|----------|----------|--------------------|
|形式驗證|型別支援證明 |阿格達、科克 |
|編譯器開發|非常適合語言實作 | OCaml、Rust |
|金融體系|類型的正確性 |斯卡拉、F# |
|學習 FP 概念 |最純粹的函數式語言 | Scala（更實用）、Elm |
|通用應用開發 |可能但利基| Python、Go、Java |
|網頁開發| Yesod/Servant 存在但有限 | JavaScript/TypeScript |
|資料科學|不是生態系| Python、R |
---

## 綜合問答
### Q1：Haskell 的惰性求值如何影響效能？
**答案：** 惰性求值意味著僅在需要時才計算表達式，從而實現無限資料結構和可組合管道。但是，如果 thunk 累積，可能會導致空間洩漏：
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

使用`foldl'`（來自`Data.List`）而不是`foldl`進行數位折疊。需要時使用`!`瀏海圖案或`seq`強制進行評估。
### Q2：`Functor`、`Applicative`和`Monad`之間的實際差異是什麼？
**A:** 每個類型類別都新增了功能：
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

**函子** 在上下文上映射纯函数。 **適用性** 應用本身位於上下文中的函數。 **Monad** 讓每一步都依賴上一步的結果。實務上：使用`fmap`/`<$>`進行簡單變換，使用`<*>`進行組合效果，使用`>>=`/`do`進行順序相關計算。
### Q3：如何處理純 Haskell 程式碼中的副作用？
**A:** 使用類型系統來分離純粹且有效的程式碼：
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

保持核心邏輯純粹，將效果推向邊緣。使用`ReaderT`進行配置，使用`ExceptT`進行錯誤，使用`StateT`進行可變狀態。
### Q4：什麼是型別類別以及它們與 OOP 介面有何不同？
**A:** 類型類別定義類型可以實現的行為。與 OOP 介面不同，它們是開放的（任何類型都可以是實例）並支援臨時多態性：
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

### Q5：如何建構一個供實際使用的 Haskell 專案？
**A:** 使用 Cabal 或 Stack 並採用標準佈局：
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

關鍵實務：將 IO 保留在`Main.hs`或專用的`IO`模組中，使核心邏輯純淨且可測試，對域類型使用`newtype`包裝器。
---

## 解決問題的思路
### 問題 1：實作帶​​有錯誤報告的安全除法函數
**第 1 步：了解問題**
我們需要除法來處理除以零並報告有意義的錯誤，而不僅僅是崩潰。
**第 2 步：確定方法**
使用`Either`傳回錯誤訊息或結果。這使得類型中明確出現故障的可能性。
**步驟 3：實施**```haskell
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

**第 4 步：驗證**
類型系統保證呼叫者必須處理錯誤情況。模式匹配或`either`強制明確處理。
### 問題 2：解析簡單的設定語言
**第 1 步：了解問題**
從`name=Alice\nage=30`等字串中解析鍵值對。
**第 2 步：確定方法**
使用`Text.Parsec`或手動遞歸。為簡單起見，請使用`break`和`span`。
**步驟 3：實施**```haskell
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

**第 4 步：擴充**
新增註釋處理 (`#`)、節標題 (`[section]`)，並使用`Value`ADT 進行型別強制轉換。
### 問題 3：用惰性建構記憶斐波那契
**第 1 步：了解問題**
高效率計算斐波那契數。樸素遞歸是指數級的。
**第 2 步：確定方法**
使用 Haskell 的惰性求值建立一個無限列表，其中每個元素都計算一次並快取。
**步驟 3：實施**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**第 4 步：優化**
對於隨機訪問，請使用具有惰性構造的 `Data.Array`。對於非常大的索引，請使用 O(log n) 矩陣求冪。
### 問題 4：實作簡單的狀態機
**第 1 步：了解問題**
模擬一個循環紅 -> 綠色 -> 黃 -> 紅的交通燈。
**第 2 步：確定方法**
使用狀態代數資料型別和純轉換函數。
**步驟 3：實施**```haskell
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

**第 4 步：驗證**
純函數是可以簡單測試的：```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

＃＃ 概括
Haskell 是主流語言中函數式程式設計最純粹的表達式。它的類型系統是最強大的類型系統之一，它對純函數的強調產生的程式碼更容易推理和測試。雖然 Haskell 在工業中應用並不廣泛，但它的想法卻深刻地影響了現代程式設計。學習 Haskell 會改變你對程式設計的看法——即使你從未專業地使用過它。