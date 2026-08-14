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
# Haskell
Ang Haskell ay isang purong functional, statically typed, tamad na sinusuri na programming language. Unang na-standardize noong 1990 (Haskell 90) at pino sa maraming bersyon (Haskell 2010 ang kasalukuyang pamantayan), kilala ang Haskell para sa kanyang mathematical rigour, malakas na sistema ng uri (na may mga uri ng klase, monad, at algebraic na uri ng data), at diin sa kawastuhan sa pamamagitan ng mga uri.
Ang Haskell ay hindi isang pangunahing wika, ngunit ang impluwensya nito ay napakalaki. Ang mga konsepto tulad ng monads, lazy evaluation, at type classes ay nakaimpluwensya sa Rust, Swift, Kotlin, Scala, at TypeScript. Ang Haskell ay ginagamit sa pananalapi (Standard Chartered, Barclays), compiler (GHC), at pormal na pag-verify.
---

## Bakit Mahalaga ang Haskell
- **Purong function**: Walang side effect bilang default — palaging ibinabalik ng mga function ang parehong output para sa parehong input.
- **Type system**: Kabilang sa mga pinaka-nagpapahayag ng anumang wika — nakakakuha ng mga bug sa oras ng pag-compile na hindi magagawa ng ibang mga wika.
- **Lazy evaluation**: Ang mga computations ay ipinagpaliban hanggang sa kinakailangan — nagbibigay-daan sa walang katapusang mga istruktura ng data at mahusay na komposisyon.
- **Mathematical foundation**: Batay sa lambda calculus at category theory — mas malapit ang mga program sa mathematical proofs.
- **Impluwensiya**: Ang mga ideya ni Haskell ay humubog sa karamihan sa mga modernong wika.
- **Concurrency**: Nagbibigay ang Software Transactional Memory (STM) ng eleganteng kasabay na programming.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Steep learning curve** | Monads, functors, type classes — ibang-iba sa mga imperative na wika | Mamuhunan ng oras; ang mga konsepto ay naililipat |
| **Lazy evaluation surprises** | Maaaring magdulot ng hindi inaasahang paggamit ng memorya at mga isyu sa pagganap | Gumamit ng mahigpit na pagsusuri (`!`) kung saan kinakailangan |
| **Mas maliit na ecosystem** | Mas kaunting mga aklatan kaysa sa Python, Java, o JavaScript | Ang hackage ay lumalaki; maraming kalidad na mga pakete |
| **Pamilihan ng trabaho** | Niche — karamihan sa pananalapi, pananaliksik, at gawain ng compiler | Lumalago sa mga functional na komunidad ng programming |
| **Bilis ng compilation** | Maaaring mabagal ang GHC para sa malalaking proyekto | Gamitin ang GHCi para sa interactive na pag-unlad |
---

## Syntax Fundamentals
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

## Advanced na Syntax at Mga Pattern
### Mga Uri ng Pamilya — Mga Function sa Antas ng Uri
Binibigyang-daan ka ng mga uri ng pamilya na mag-compute ng mga uri sa antas ng uri, katulad ng kung paano kino-compute ng mga function ang mga halaga sa antas ng halaga.
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

### GADT — Mga Pangkalahatan na Algebraic na Uri ng Data
Hinahayaan ka ng mga GADT na tukuyin ang uri ng pagbabalik ng bawat constructor nang tumpak, na nagpapagana ng mga uri-safe na interpreter at naka-embed na DSL.
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

### Mga Transformer ng Monad
Ang mga transformer ng Monad ay nagtataglay ng mga monadic effect, na nagpapahintulot sa iyong pagsamahin ang IO, estado, paghawak ng error, at higit pa.
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

### Functor, Applicative, at Monad Hierarchy
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

### Advanced na Pagtutugma ng Pattern
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

### Tamad vs Mahigpit na Pagsusuri
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

## Concurrency at Paralelismo
### Software Transactional Memory (STM)
Nagbibigay ang STM ng mga composable na transaksyon para sa shared state — tulad ng mga transaksyon sa database ngunit para sa memorya.
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

### Kasabay na Async Operations
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

### Mga Parallel na Istratehiya
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

## Project Configuration at Build System
### Istraktura ng Proyekto (Stack/Cabal)
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

### Stack Configuration (stack.yaml)
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

### Paglalarawan ng Package (package.yaml para sa hpack)
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

### Mga Key Build Command
| Utos | Paglalarawan |
|---------|-------------|
| `stack new my-project`| Lumikha ng bagong proyekto mula sa template |
| `stack build`| Buuin ang proyekto |
| `stack ghci`| Simulan ang interactive na REPL na may na-load na proyekto |
| `stack test`| Patakbuhin ang test suite |
| `stack bench`| Patakbuhin ang mga benchmark |
| `stack haddock`| Bumuo ng dokumentasyon |
| `stack exec my-app`| Patakbuhin ang executable |
| `stack clean`| Malinis na build artifacts |
| `stack update`| I-update ang index ng package |
| `stack freeze`| I-pin ang eksaktong dependency na bersyon |
### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### HSpec — Unit Testing Framework
Ang HSpec ay ang pinakasikat na balangkas ng pagsubok, na inspirasyon ng RSpec ni Ruby. Nagbibigay ito ng BDD-style syntax.
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

### Property-Based Testing gamit ang QuickCheck
Ang QuickCheck ay bumubuo ng mga random na kaso ng pagsubok upang i-verify ang mga katangian ng iyong code.
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

### Mga Utos ng Pagsubok
| Utos | Paglalarawan |
|---------|-------------|
| `stack test`| Patakbuhin ang lahat ng test suite |
| `stack test --fast`| Laktawan ang mga pag-optimize para sa mas mabilis na mga pagsubok na build |
| `stack build --test --test-arguments "--color"`| Magpatakbo ng mga pagsubok na may kulay na output |
| `stack ghci --test`| I-load ang mga module ng pagsubok sa REPL |

---

## Interoperability
### C Foreign Function Interface (FFI)
Maaaring direktang tawagan ng Haskell ang mga function ng C at ilantad ang mga function ng Haskell sa C.
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

### Python Interop (sa pamamagitan ng inline-c o HPy)
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

## Mga Pattern ng Disenyo
### Tagless Final (Mga Naka-embed na DSL)
Ang panghuling istilo na walang tag ay nag-encode ng mga DSL gamit ang mga uri ng klase, na nagpapagana ng maraming interpretasyon.
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

### Libreng Monads
Ang mga libreng monad ay naghihiwalay sa paglalarawan ng mga epekto mula sa kanilang interpretasyon.
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

### ReaderT Pattern para sa Application Architecture
Ang ReaderT pattern ay ang modernong Haskell approach sa dependency injection.
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

## Pagganap at Pag-optimize
### Mga Tool sa Pag-profile
| Tool | Layunin | Utos |
|------|---------|---------|
| **GHC Profiler** | Pag-profile ng oras at alokasyon | `stack build --profile`pagkatapos ay`./app +RTS -p`|
| **ThreadScope** | I-visualize ang parallel execution | `./app +RTS -l`pagkatapos ay buksan ang`app.eventlog`|
| **ghc-events** | Suriin ang mga log ng kaganapan | `ghc-events show app.eventlog`|
| **Pamantayang** | Pagba-benchmark ng istatistika | Gamitin ang`criterion`package |
| **hp2pretty** | I-visualize ang mga profile ng heap | `./app +RTS -h`pagkatapos ay`hp2pretty app.hp`|
### Pag-benchmark gamit ang Criterion
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

### Mga Teknik sa Pag-optimize
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

## Deployment
### Building Release Binary
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### Docker Deployment
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

### Nix-Based Deployment
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

## Kailan Gamitin ang Haskell
| Sitwasyon | Bakit Haskell | Mas mahusay na Alternatibo |
|----------|-----------|-------------------|
| Pormal na pag-verify | Uri ng system ay nagbibigay-daan sa mga patunay | Agda, Coq |
| Pag-unlad ng compiler | Mahusay para sa pagpapatupad ng wika | OCaml, kalawang |
| Mga sistema ng pananalapi | Katumpakan sa pamamagitan ng mga uri | Scala, F# |
| Pag-aaral ng mga konsepto ng FP | Ang purest functional na wika | Scala (mas praktikal), Elm |
| Pangkalahatang pag-unlad ng application | Posible ngunit angkop na lugar | Python, Go, Java |
| Pagbuo ng web | Umiiral ang Yesod/Servant ngunit limitado | JavaScript/TypeScript |
| Agham ng datos | Hindi ang ecosystem | Python, R |
---

## Synthetic na Q&A
### Q1: Paano nakakaapekto sa pagganap ang tamad na pagsusuri ng Haskell?
**A:** Ang ibig sabihin ng tamad na pagsusuri ay ang mga expression ay kinukuwenta lamang kapag kinakailangan, na nagpapagana ng mga walang katapusang istruktura ng data at mga nabubuong pipeline. Gayunpaman, maaari itong maging sanhi ng pagtagas ng espasyo kung maipon ang mga thunks:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

Gamitin ang`foldl'`(mula sa`Data.List`) sa halip na`foldl`para sa mga numeric na fold. Gumamit ng`!`bang pattern o`seq`upang pilitin ang pagsusuri kapag kinakailangan.
### Q2: Ano ang praktikal na pagkakaiba sa pagitan ng`Functor`,`Applicative`, at`Monad`?
**A:** Ang bawat uri ng klase ay nagdaragdag ng kakayahan:
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

Ang **Functor** ay nagmamapa ng isang purong function sa isang konteksto. Ang **Applicative** ay naglalapat ng mga function na mismong nasa isang konteksto. Hinahayaan ng **Monad** na depende ang bawat hakbang sa resulta ng nakaraang hakbang. Sa pagsasagawa: gamitin ang`fmap`/`<$>`para sa mga simpleng pagbabago,`<*>`para sa pagsasama-sama ng mga epekto, at`>>=`/`do`para sa sequential dependent computations.
### Q3: Paano ko hahawakan ang mga side effect sa purong Haskell code?
**A:** Gamitin ang uri ng system upang paghiwalayin ang dalisay at epektibong code:
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

Panatilihing dalisay ang pangunahing lohika at itulak ang mga epekto sa mga gilid. Gamitin ang`ReaderT`para sa configuration,`ExceptT`para sa mga error, at`StateT`para sa nababagong estado.
### Q4: Ano ang mga uri ng klase at paano sila naiiba sa mga interface ng OOP?
**A:** Tinutukoy ng mga uri ng klase ang gawi na maaaring ipatupad ng mga uri. Hindi tulad ng mga interface ng OOP, bukas ang mga ito (maaaring maging instance ang anumang uri) at sinusuportahan ang ad-hoc polymorphism:
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

### Q5: Paano ko ibubuo ang isang proyekto ng Haskell para sa paggamit sa totoong mundo?
**A:** Gumamit ng Cabal o Stack na may karaniwang layout:
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

Mga pangunahing kasanayan: panatilihin ang IO sa`Main.hs`o isang nakalaang`IO`module, gawing dalisay at masusubok ang core logic, gumamit ng`newtype`wrapper para sa mga uri ng domain.
---

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Pagpapatupad ng Safe Division Function na may Error Reporting
**Hakbang 1: Unawain ang Problema**
Kailangan namin ng dibisyon na humahawak sa paghahati sa pamamagitan ng zero at nag-uulat ng mga makabuluhang error, hindi lang mga pag-crash.
**Hakbang 2: Tukuyin ang Diskarte**
Gamitin ang`Either`upang ibalik ang alinman sa mensahe ng error o ang resulta. Ginagawa nitong tahasan ang posibilidad ng pagkabigo sa uri.
**Hakbang 3: Ipatupad**```haskell
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

**Hakbang 4: I-verify**
Ginagarantiyahan ng uri ng system na dapat pangasiwaan ng mga tumatawag ang kaso ng error. Pinipilit ng pagtutugma ng pattern o`either`ang tahasang paghawak.
### Problema 2: Pag-parse ng Simpleng Configuration Language
**Hakbang 1: Unawain ang Problema**
I-parse ang mga pares ng key-value mula sa isang string tulad ng`name=Alice\nage=30`.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng`Text.Parsec`o manu-manong recursion. Para sa pagiging simple, gamitin ang`break`at`span`.
**Hakbang 3: Ipatupad**```haskell
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

**Hakbang 4: Palawakin**
Magdagdag ng paghawak ng komento (`#`), mga header ng seksyon (`[section]`), at i-type ang pamimilit gamit ang isang`Value`ADT.
### Problema 3: Pagbuo ng Memoized Fibonacci na may Katamaran
**Hakbang 1: Unawain ang Problema**
Mahusay na mag-compute ng mga numero ng Fibonacci. Ang naive recursion ay exponential.
**Hakbang 2: Tukuyin ang Diskarte**
Gamitin ang tamad na pagsusuri ng Haskell upang lumikha ng isang walang katapusang listahan kung saan ang bawat elemento ay kinalkula nang isang beses at naka-cache.
**Hakbang 3: Ipatupad**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**Hakbang 4: I-optimize**
Para sa random na pag-access, gamitin ang`Data.Array`na may tamad na konstruksyon. Para sa napakalaking mga indeks, gumamit ng matrix exponentiation sa O(log n).
### Problema 4: Pagpapatupad ng Simple State Machine
**Hakbang 1: Unawain ang Problema**
Magmodelo ng traffic light na umiikot sa Pula -> Berde -> Dilaw -> Pula.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng algebraic na uri ng data para sa mga estado at isang purong transition function.
**Hakbang 3: Ipatupad**```haskell
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

**Hakbang 4: I-verify**
Ang mga dalisay na function ay trivially na nasusubok:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## Buod
Ang Haskell ay ang purong pagpapahayag ng functional programming sa isang pangunahing wika. Ang uri ng sistema nito ay kabilang sa pinakamakapangyarihan, at ang pagbibigay-diin nito sa mga purong function ay gumagawa ng code na mas madaling mangatuwiran at subukan. Habang ang Haskell ay hindi malawakang ginagamit sa industriya, ang mga ideya nito ay lubos na nakaimpluwensya sa modernong programming. Binabago ng Learning Haskell ang iyong iniisip tungkol sa programming — kahit na hindi mo ito ginagamit nang propesyonal.