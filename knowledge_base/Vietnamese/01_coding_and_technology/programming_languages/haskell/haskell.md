<!--
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

-->
# Haskell
Haskell là một ngôn ngữ lập trình thuần túy về chức năng, được gõ tĩnh, được đánh giá một cách lười biếng. Được chuẩn hóa lần đầu tiên vào năm 1990 (Haskell 90) và được cải tiến qua nhiều phiên bản (Haskell 2010 là tiêu chuẩn hiện tại), Haskell được biết đến với tính chính xác về mặt toán học, hệ thống kiểu mạnh mẽ (với các lớp kiểu, đơn nguyên và kiểu dữ liệu đại số) và nhấn mạnh vào tính chính xác thông qua các kiểu.
Haskell không phải là ngôn ngữ chính thống nhưng sức ảnh hưởng của nó rất lớn. Các khái niệm như đơn nguyên, đánh giá lười biếng và các lớp loại đã ảnh hưởng đến Rust, Swift, Kotlin, Scala và TypeScript. Haskell được sử dụng trong tài chính (Standard Chartered, Barclays), biên dịch (GHC) và xác minh chính thức.
---

## Tại sao Haskell lại quan trọng
- **Hàm thuần túy**: Không có tác dụng phụ theo mặc định — các hàm luôn trả về cùng một đầu ra cho cùng một đầu vào.
- **Hệ thống gõ**: Một trong những ngôn ngữ có tính biểu cảm cao nhất — phát hiện các lỗi tại thời điểm biên dịch mà các ngôn ngữ khác không thể làm được.
- **Đánh giá lười biếng**: Việc tính toán được trì hoãn cho đến khi cần thiết — cho phép cấu trúc dữ liệu vô hạn và kết hợp hiệu quả.
- **Nền tảng toán học**: Dựa trên phép tính lambda và lý thuyết phạm trù — các chương trình gần với chứng minh toán học hơn.
- **Ảnh hưởng**: Ý tưởng của Haskell đã định hình hầu hết các ngôn ngữ hiện đại.
- **Đồng thời**: Bộ nhớ giao dịch phần mềm (STM) cung cấp khả năng lập trình đồng thời một cách tinh tế.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Đường cong học tập dốc** | Monads, functor, các lớp kiểu — rất khác với các ngôn ngữ mệnh lệnh | Đầu tư thời gian; các khái niệm có thể chuyển nhượng được |
| **Đánh giá lười biếng bất ngờ** | Có thể gây ra các vấn đề về hiệu suất và sử dụng bộ nhớ không mong muốn | Sử dụng đánh giá nghiêm ngặt (`!`) khi cần thiết |
| **Hệ sinh thái nhỏ hơn** | Ít thư viện hơn Python, Java hoặc JavaScript | Hacking đang gia tăng; nhiều gói chất lượng |
| **Thị trường việc làm** | Niche - chủ yếu là công việc tài chính, nghiên cứu và biên soạn | Phát triển trong cộng đồng lập trình chức năng |
| **Tốc độ biên dịch** | GHC có thể chậm đối với các dự án lớn | Sử dụng GHCi để phát triển tương tác |
---

##Cơ bản về cú pháp
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

## Cú pháp & Mẫu nâng cao
### Họ loại — Hàm cấp loại
Họ loại cho phép bạn tính toán các loại ở cấp độ loại, tương tự như cách các hàm tính toán các giá trị ở cấp độ giá trị.
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

### GADT - Các kiểu dữ liệu đại số tổng quát
GADT cho phép bạn chỉ định chính xác kiểu trả về của từng hàm tạo, cho phép trình thông dịch an toàn kiểu và DSL nhúng.
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

### Máy biến áp đơn nguyên
Biến áp đơn nguyên xếp chồng các hiệu ứng đơn âm, cho phép bạn kết hợp IO, trạng thái, xử lý lỗi, v.v.
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

### Functor, ứng dụng và phân cấp đơn nguyên
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

### So khớp mẫu nâng cao
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

### Đánh giá lười biếng và nghiêm ngặt
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

## Đồng thời & Song song
### Bộ nhớ giao dịch phần mềm (STM)
STM cung cấp các giao dịch có thể tổng hợp cho trạng thái chia sẻ — như giao dịch cơ sở dữ liệu nhưng dành cho bộ nhớ.
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

### Hoạt động không đồng bộ đồng thời
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

### Chiến lược song song
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án (Stack/Cabal)
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

### Cấu hình ngăn xếp (stack.yaml)
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

### Mô tả gói (pack.yaml cho hpack)
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

### Lệnh xây dựng chính
| Lệnh | Mô tả |
|----------|-------------|
| `stack new my-project`| Tạo dự án mới từ mẫu |
| `stack build`| Xây dựng dự án |
| `stack ghci`| Bắt đầu REPL tương tác khi tải dự án |
| `stack test`| Chạy bộ thử nghiệm |
| `stack bench`| Chạy điểm chuẩn |
| `stack haddock`| Tạo tài liệu |
| `stack exec my-app`| Chạy tệp thực thi |
| `stack clean`| Tạo tác sạch sẽ |
| `stack update`| Cập nhật chỉ mục gói |
| `stack freeze`| Ghim các phiên bản phụ thuộc chính xác |
### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### HSpec — Khung kiểm tra đơn vị
HSpec là khung thử nghiệm phổ biến nhất, lấy cảm hứng từ RSpec của Ruby. Nó cung cấp cú pháp kiểu BDD.
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

### Kiểm tra dựa trên thuộc tính bằng QuickCheck
QuickCheck tạo các trường hợp kiểm thử ngẫu nhiên để xác minh các thuộc tính của mã của bạn.
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

### Lệnh kiểm tra
| Lệnh | Mô tả |
|----------|-------------|
| `stack test`| Chạy tất cả các bộ thử nghiệm |
| `stack test --fast`| Bỏ qua tối ưu hóa để xây dựng thử nghiệm nhanh hơn |
| `stack build --test --test-arguments "--color"`| Chạy thử nghiệm với đầu ra có màu |
| `stack ghci --test`| Tải các mô-đun kiểm tra trong REPL |

---

## Khả năng tương tác
###C Giao diện chức năng ngoại (FFI)
Haskell có thể gọi trực tiếp các hàm C và hiển thị các hàm Haskell cho C.
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

### Python Interop (thông qua inline-c hoặc HPy)
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

## Mẫu thiết kế
### Cuối cùng không gắn thẻ (DSL nhúng)
Kiểu cuối cùng không cần thẻ mã hóa DSL bằng cách sử dụng các lớp loại, cho phép nhiều cách diễn giải.
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

### Đơn nguyên miễn phí
Các đơn nguyên tự do tách biệt việc mô tả các hiệu ứng khỏi sự diễn giải của chúng.
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

### Mẫu ReaderT cho Kiến trúc ứng dụng
Mẫu ReaderT là cách tiếp cận Haskell hiện đại để chèn phần phụ thuộc.
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

## Hiệu suất & Tối ưu hóa
### Công cụ lập hồ sơ
| Công cụ | Mục đích | Lệnh |
|------|----------|----------|
| **Trình hồ sơ GHC** | Hồ sơ thời gian và phân bổ | `stack build --profile`rồi`./app +RTS -p`|
| **ThreadScope** | Trực quan hóa việc thực thi song song | `./app +RTS -l`thì mở`app.eventlog`|
| **ghc-sự kiện** | Phân tích nhật ký sự kiện | `ghc-events show app.eventlog`|
| **Tiêu chí** | Điểm chuẩn thống kê | Sử dụng gói`criterion`|
| **hp2pretty** | Trực quan hóa hồ sơ heap | `./app +RTS -h`rồi`hp2pretty app.hp`|
### Đo điểm chuẩn bằng tiêu chí
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

### Kỹ thuật tối ưu hóa
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

## Triển khai
### Xây dựng các bản phát hành nhị phân
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### Triển khai Docker
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

### Triển khai dựa trên Nix
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

## Khi nào nên sử dụng Haskell
| Kịch bản | Tại sao Haskell | Thay thế tốt hơn |
|----------|-------------|-------------------|
| Xác minh chính thức | Hệ thống loại cho phép chứng minh | Agda, Coq |
| Phát triển trình biên dịch | Tuyệt vời cho việc thực hiện ngôn ngữ | OCaml, Rust |
| Hệ thống tài chính | Tính đúng đắn thông qua các loại | Scala, F# |
| Học các khái niệm FP | Ngôn ngữ chức năng thuần túy nhất | Scala (thực tế hơn), Elm |
| Phát triển ứng dụng chung | Có thể nhưng thích hợp | Python, Go, Java |
| Phát triển web | Yesod/Servant tồn tại nhưng bị hạn chế | JavaScript/TypeScript |
| Khoa học dữ liệu | Không phải hệ sinh thái | Python, R |
---

## Hỏi đáp tổng hợp
### Câu 1: Đánh giá lười biếng của Haskell ảnh hưởng đến hiệu suất như thế nào?
**A:** Đánh giá lười biếng có nghĩa là các biểu thức chỉ được tính toán khi cần thiết, cho phép cấu trúc dữ liệu vô hạn và các quy trình có thể tổng hợp. Tuy nhiên, nó có thể gây rò rỉ không gian nếu thun tích tụ:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

Sử dụng`foldl'`(từ`Data.List`) thay vì`foldl`cho các nếp gấp số. Sử dụng các mẫu bang`!`hoặc`seq`để buộc đánh giá khi cần.
### Câu 2: Sự khác biệt thực tế giữa`Functor`,`Applicative`và`Monad`là gì?
**A:** Mỗi lớp kiểu chữ bổ sung thêm khả năng:
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

**Functor** ánh xạ một hàm thuần túy lên một ngữ cảnh. **Áp dụng** áp dụng chính các hàm trong một ngữ cảnh. **Monad** cho phép mỗi bước phụ thuộc vào kết quả của bước trước đó. Trong thực tế: sử dụng`fmap`/`<$>`cho các phép biến đổi đơn giản,`<*>`để kết hợp các hiệu ứng và`>>=`/`do`cho các phép tính phụ thuộc tuần tự.
### Câu 3: Làm cách nào để xử lý các tác dụng phụ trong mã Haskell thuần túy?
**A:** Sử dụng hệ thống loại để phân tách mã thuần túy và hiệu quả:
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

Giữ logic cốt lõi thuần túy và đẩy các hiệu ứng ra rìa. Sử dụng`ReaderT`để định cấu hình,`ExceptT`cho lỗi và`StateT`cho trạng thái có thể thay đổi.
### Q4: Loại lớp là gì và chúng khác với giao diện OOP như thế nào?
**A:** Các lớp loại xác định hành vi mà các loại có thể triển khai. Không giống như giao diện OOP, chúng mở (bất kỳ loại nào cũng có thể là một phiên bản) và hỗ trợ đa hình đặc biệt:
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

### Câu hỏi 5: Làm cách nào để cấu trúc một dự án Haskell để sử dụng trong thực tế?
**A:** Sử dụng Cabal hoặc Stack với bố cục chuẩn:
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

Các phương pháp chính: giữ IO trong`Main.hs`hoặc mô-đun`IO`chuyên dụng, làm cho logic cốt lõi trở nên thuần túy và có thể kiểm tra được, sử dụng trình bao bọc`newtype`cho các loại miền.
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Thực hiện chức năng phân chia an toàn với báo cáo lỗi
**Bước 1: Tìm hiểu vấn đề**
Chúng ta cần phép chia xử lý phép chia cho 0 và báo cáo các lỗi có ý nghĩa chứ không chỉ gặp sự cố.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`Either`để trả về thông báo lỗi hoặc kết quả. Điều này làm cho khả năng thất bại trở nên rõ ràng trong loại này.
**Bước 3: Thực hiện**```haskell
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

**Bước 4: Xác minh**
Hệ thống loại đảm bảo người gọi phải xử lý trường hợp lỗi. Khớp mẫu hoặc`either`buộc phải xử lý rõ ràng.
### Vấn đề 2: Phân tích ngôn ngữ cấu hình đơn giản
**Bước 1: Tìm hiểu vấn đề**
Phân tích các cặp khóa-giá trị từ một chuỗi như`name=Alice\nage=30`.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`Text.Parsec`hoặc đệ quy thủ công. Để đơn giản, hãy sử dụng`break`và`span`.
**Bước 3: Thực hiện**```haskell
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

**Bước 4: Gia hạn**
Thêm xử lý nhận xét (`#`), tiêu đề phần (`[section]`) và nhập ép buộc bằng cách sử dụng`Value`ADT.
### Vấn đề 3: Xây dựng Fibonacci được ghi nhớ bằng sự lười biếng
**Bước 1: Tìm hiểu vấn đề**
Tính toán số Fibonacci một cách hiệu quả. Đệ quy ngây thơ là theo cấp số nhân.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng đánh giá lười biếng của Haskell để tạo danh sách vô hạn trong đó mỗi phần tử được tính toán một lần và được lưu vào bộ nhớ đệm.
**Bước 3: Thực hiện**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**Bước 4: Tối ưu hóa**
Để truy cập ngẫu nhiên, hãy sử dụng`Data.Array`với cấu trúc lười biếng. Đối với các chỉ số rất lớn, hãy sử dụng lũy ​​thừa ma trận trong O(log n).
### Bài toán 4: Triển khai một máy trạng thái đơn giản
**Bước 1: Tìm hiểu vấn đề**
Mô hình đèn giao thông có chu kỳ Đỏ -> Xanh -> Vàng -> Đỏ.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng kiểu dữ liệu đại số cho các trạng thái và hàm chuyển đổi thuần túy.
**Bước 3: Thực hiện**```haskell
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

**Bước 4: Xác minh**
Các hàm thuần túy có thể kiểm tra được một cách tầm thường:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## Bản tóm tắt
Haskell là sự thể hiện thuần túy nhất của lập trình hàm trong ngôn ngữ chính thống. Hệ thống kiểu của nó là một trong những hệ thống mạnh mẽ nhất và sự nhấn mạnh của nó vào các hàm thuần túy tạo ra mã dễ suy luận và kiểm tra hơn. Mặc dù Haskell không được sử dụng rộng rãi trong công nghiệp nhưng những ý tưởng của nó đã ảnh hưởng sâu sắc đến ngành lập trình hiện đại. Học Haskell sẽ thay đổi cách bạn nghĩ về lập trình — ngay cả khi bạn chưa bao giờ sử dụng nó một cách chuyên nghiệp.