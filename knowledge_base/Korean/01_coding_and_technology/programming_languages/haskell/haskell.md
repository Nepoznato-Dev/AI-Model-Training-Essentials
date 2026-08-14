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
# 하스켈
Haskell은 순전히 기능적이며 정적으로 유형이 지정되고 느리게 평가되는 프로그래밍 언어입니다. 1990년에 처음 표준화(Haskell 90)되고 여러 버전(현재 표준은 Haskell 2010)을 통해 개선된 Haskell은 수학적 엄격함, 강력한 유형 시스템(유형 클래스, 모나드 및 대수 데이터 유형 포함), 유형을 통한 정확성 강조로 유명합니다.
하스켈은 주류 언어는 아니지만 그 영향력은 엄청납니다. 모나드, 지연 평가, 유형 클래스와 같은 개념은 Rust, Swift, Kotlin, Scala 및 TypeScript에 영향을 미쳤습니다. Haskell은 금융(Standard Chartered, Barclays), 컴파일러(GHC) 및 공식 검증에 사용됩니다.
---

## 하스켈이 중요한 이유
- **순수 함수**: 기본적으로 부작용이 없습니다. 함수는 항상 동일한 입력에 대해 동일한 출력을 반환합니다.
- **유형 시스템**: 모든 언어 중에서 가장 표현력이 뛰어난 언어 중 하나입니다. 다른 언어에서는 잡을 수 없는 버그를 컴파일 타임에 잡아냅니다.
- **지연 평가**: 필요할 때까지 계산이 연기되어 무한한 데이터 구조와 효율적인 구성이 가능합니다.
- **수학적 기초**: 람다 미적분학 및 범주 이론을 기반으로 하며 프로그램은 수학적 증명에 더 가깝습니다.
- **영향**: Haskell의 아이디어는 대부분의 현대 언어를 형성했습니다.
- **동시성**: 소프트웨어 트랜잭션 메모리(STM)는 우아한 동시 프로그래밍을 제공합니다.
## 절충안
| 제한사항 | 세부정보 | 일반적인 해결 방법 |
|------------|---------|------|
| **가파른 학습 곡선** | 모나드, 펑터, 유형 클래스 — 명령형 언어와 매우 다릅니다 | 시간을 투자하세요. 개념은 이전 가능합니다 |
| **게으른 평가로 인한 놀라움** | 예상치 못한 메모리 사용량 및 성능 문제가 발생할 수 있음 | 필요한 경우 엄격한 평가(`!`) 사용 |
| **더 작은 생태계** | Python, Java 또는 JavaScript보다 적은 라이브러리 | 해킹이 증가하고 있습니다. 많은 품질의 패키지 |
| **취업 시장** | 틈새 – 주로 금융, 연구 및 컴파일러 작업 | 함수형 프로그래밍 커뮤니티에서 성장 |
| **컴파일 속도** | 대규모 프로젝트에서는 GHC가 느려질 수 있습니다 | 대화형 개발을 위해 GHCi 사용 |
---

## 구문 기본 사항
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

## 고급 구문 및 패턴
### 유형군 - 유형 수준 함수
유형 패밀리를 사용하면 함수가 값 수준에서 값을 계산하는 방법과 유사하게 유형 수준에서 유형을 계산할 수 있습니다.
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

### GADT — 일반화된 대수 데이터 유형
GADT를 사용하면 각 생성자의 반환 유형을 정확하게 지정할 수 있으므로 유형이 안전한 인터프리터와 내장된 DSL을 사용할 수 있습니다.
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

### 모나드 트랜스포머
모나드 변환기는 모나드 효과를 스택하여 IO, 상태, 오류 처리 등을 결합할 수 있게 해줍니다.
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

### Functor, Applicative 및 Monad 계층 구조
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

### 고급 패턴 매칭
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

### 게으른 평가와 엄격한 평가
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

## 동시성 및 병렬성
### 소프트웨어 트랜잭션 메모리(STM)
STM은 데이터베이스 트랜잭션과 유사하지만 메모리를 위한 공유 상태에 대한 구성 가능한 트랜잭션을 제공합니다.
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

### 동시 비동기 작업
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

### 병렬 전략
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

## 프로젝트 구성 및 빌드 시스템
### 프로젝트 구조(스택/카발)
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

### 스택 구성(stack.yaml)
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

### 패키지 설명(hpack용 package.yaml)
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

### 주요 빌드 명령
| 명령 | 설명 |
|---------|-------------|
| `stack new my-project`| 템플릿에서 새 프로젝트 만들기 |
| `stack build`| 프로젝트 빌드 |
| `stack ghci`| 프로젝트가 로드된 상태에서 대화형 REPL 시작 |
| `stack test`| 테스트 스위트 실행 |
| `stack bench`| 벤치마크 실행 |
| `stack haddock`| 문서 생성 |
| `stack exec my-app`| 실행 파일 실행 |
| `stack clean`| 빌드 아티팩트 정리 |
| `stack update`| 패키지 색인 업데이트 |
| `stack freeze`| 정확한 종속성 버전 고정 |
### CI/CD 파이프라인(GitHub 작업)
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

## 테스트
### HSpec — 단위 테스트 프레임워크
HSpec은 Ruby의 RSpec에서 영감을 받아 가장 널리 사용되는 테스트 프레임워크입니다. BDD 스타일 구문을 제공합니다.
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

### QuickCheck를 사용한 속성 기반 테스트
QuickCheck는 코드의 속성을 확인하기 위해 무작위 테스트 사례를 생성합니다.
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

### 테스트 명령
| 명령 | 설명 |
|---------|-------------|
| `stack test`| 모든 테스트 스위트 실행 |
| `stack test --fast`| 더 빠른 테스트 빌드를 위한 최적화 건너뛰기 |
| `stack build --test --test-arguments "--color"`| 컬러 출력으로 테스트 실행 |
| `stack ghci --test`| REPL의 로드 테스트 모듈 |

---

## 상호 운용성
### C FFI(외부 함수 인터페이스)
Haskell은 C 함수를 직접 호출하고 Haskell 함수를 C에 노출할 수 있습니다.
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

### Python Interop(inline-c 또는 HPy를 통해)
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

## 디자인 패턴
### 태그 없는 최종(내장형 DSL)
태그가 없는 최종 스타일은 유형 클래스를 사용하여 DSL을 인코딩하므로 다양한 해석이 가능합니다.
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

### 무료 모나드
무료 모나드는 효과 설명과 해석을 분리합니다.
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

### 애플리케이션 아키텍처를 위한 ReaderT 패턴
ReaderT 패턴은 종속성 주입에 대한 최신 Haskell 접근 방식입니다.
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

## 성능 및 최적화
### 프로파일링 도구
| 도구 | 목적 | 명령 |
|------|---------|---------|
| **GHC 프로파일러** | 시간 및 할당 프로파일링 | `stack build --profile`다음으로`./app +RTS -p`|
| **스레드스코프** | 병렬 실행 시각화 |  `./app +RTS -l`를 열고`app.eventlog`|
| **ghc-이벤트** | 이벤트 로그 분석 | `ghc-events show app.eventlog`|
| **기준** | 통계적 벤치마킹 |`criterion`패키지 사용 |
| **hp2예쁜** | 힙 프로필 시각화 | `./app +RTS -h`다음으로`hp2pretty app.hp`|
### 기준을 사용한 벤치마킹
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

### 최적화 기술
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

## 배포
### 릴리스 바이너리 빌드
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### 도커 배포
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

### Nix 기반 배포
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

## 하스켈을 사용해야 하는 경우
| 시나리오 | 왜 하스켈인가 | 더 나은 대안 |
|----------|------------|------|
| 정식 검증 | 유형 시스템을 통해 증명 가능 | 아그다, 콕 |
| 컴파일러 개발 | 언어 구현에 탁월 | OCaml, 러스트 |
| 금융 시스템 | 유형을 통한 정확성 | 스칼라, F# |
| FP 개념 학습 | 가장 순수한 기능적 언어 | Scala(더 실용적), Elm |
| 일반 애플리케이션 개발 | 가능하지만 틈새 시장 | 파이썬, 바둑, 자바 |
| 웹 개발 | Yesod/Servant가 존재하지만 제한적 | 자바스크립트/타입스크립트 |
| 데이터 과학 | 생태계가 아니다 | 파이썬, R |
---

## 종합 Q&A
### Q1: Haskell의 지연 평가는 성능에 어떤 영향을 미치나요?
**A:** 지연 평가는 필요할 때만 표현식이 계산되어 무한한 데이터 구조와 구성 가능한 파이프라인이 가능하다는 것을 의미합니다. 그러나 썽크가 누적되면 공간 누수가 발생할 수 있습니다.
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

숫자 접기에는`foldl`대신`foldl'`(`Data.List`)를 사용하십시오. 필요할 때 강제로 평가하려면`!`뱅 패턴 또는 `seq`를 사용하세요.
### Q2:`Functor`,`Applicative`,`Monad`의 실질적인 차이점은 무엇인가요?
**답:** 각 유형 클래스에는 다음 기능이 추가됩니다.
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

**Functor**는 컨텍스트에 순수 함수를 매핑합니다. **적용**은 컨텍스트에 있는 함수를 적용합니다. **모나드**는 각 단계가 이전 단계의 결과에 따라 달라지도록 합니다. 실제로: 단순 변환에는`fmap`/ `<$>`를 사용하고, 효과 결합에는 `<*>`를, 순차적 종속 계산에는`>>=`/ `do`를 사용합니다.
### Q3: 순수 하스켈 코드에서 부작용을 어떻게 처리하나요?
**답:** 유형 시스템을 사용하여 순수 코드와 효과적인 코드를 구분하세요.
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

핵심 로직을 순수하게 유지하고 효과를 가장자리까지 밀어 넣으세요. 구성에는 `ReaderT`를, 오류에는 `ExceptT`를, 변경 가능한 상태에는 `StateT`를 사용하세요.
### Q4: 유형 클래스란 무엇이며 OOP 인터페이스와 어떻게 다릅니까?
**A:** 유형 클래스는 유형이 구현할 수 있는 동작을 정의합니다. OOP 인터페이스와 달리 개방형(모든 유형이 인스턴스가 될 수 있음)이며 임시 다형성을 지원합니다.
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

### Q5: 실제 사용을 위해 Haskell 프로젝트를 어떻게 구성합니까?
**답변:** 표준 레이아웃으로 Cabal 또는 Stack을 사용하세요.
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

주요 사례:`Main.hs`또는 전용`IO`모듈에 IO를 유지하고, 핵심 논리를 순수하고 테스트 가능하게 만들고, 도메인 유형에`newtype`래퍼를 사용합니다.
---

## 사고 사슬 문제 해결
### 문제 1: 오류 보고를 통한 안전 분할 기능 구현
**1단계: 문제 이해**
0으로 나누기를 처리하고 단순한 충돌이 아닌 의미 있는 오류를 보고하는 나누기가 필요합니다.
**2단계: 접근 방식 파악**
오류 메시지나 결과를 반환하려면 `Either`를 사용하세요. 이는 유형에서 실패 가능성을 명시적으로 만듭니다.
**3단계: 구현**```haskell
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

**4단계: 확인**
유형 시스템은 호출자가 오류 사례를 처리해야 함을 보장합니다. 패턴 일치 또는 `either`는 명시적 처리를 강제합니다.
### 문제 2: 간단한 구성 언어 구문 분석
**1단계: 문제 이해**
`name=Alice\nage=30` 와 같은 문자열에서 키-값 쌍을 구문 분석합니다.
**2단계: 접근 방식 파악**
`Text.Parsec` 또는 수동 재귀를 사용하십시오. 단순화를 위해`break`및`span`를 사용합니다.
**3단계: 구현**```haskell
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

**4단계: 확장**
`Value` ADT를 사용하여 주석 처리(`#`), 섹션 헤더(`[section]`) 및 유형 강제를 추가합니다.
### 문제 3: 게으름을 활용하여 메모된 피보나치 만들기
**1단계: 문제 이해**
피보나치 수를 효율적으로 계산합니다. 순진한 재귀는 기하급수적입니다.
**2단계: 접근 방식 파악**
Haskell의 지연 평가를 사용하여 각 요소가 한 번 계산되고 캐시되는 무한 목록을 만듭니다.
**3단계: 구현**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**4단계: 최적화**
임의 액세스의 경우 지연 구성과 함께 `Data.Array`를 사용합니다. 매우 큰 인덱스의 경우 O(log n)의 행렬 지수화를 사용합니다.
### 문제 4: 간단한 상태 머신 구현
**1단계: 문제 이해**
빨간색 -> 녹색 -> 노란색 -> 빨간색으로 순환하는 신호등을 모델링합니다.
**2단계: 접근 방식 파악**
상태와 순수 전이 함수에는 대수적 데이터 유형을 사용합니다.
**3단계: 구현**```haskell
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

**4단계: 확인**
순수 함수는 간단하게 테스트 가능합니다.```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## 요약
하스켈은 주류 언어 중 함수형 프로그래밍의 가장 순수한 표현입니다. 유형 시스템은 가장 강력한 것 중 하나이며, 순수 함수에 중점을 두어 추론하고 테스트하기가 더 쉬운 코드를 생성합니다. Haskell은 업계에서 널리 사용되지는 않지만 그 아이디어는 현대 프로그래밍에 깊은 영향을 미쳤습니다. Haskell을 배우면 프로그래밍에 대한 생각이 바뀌게 됩니다. 전문적으로 사용하지 않더라도 말이죠.