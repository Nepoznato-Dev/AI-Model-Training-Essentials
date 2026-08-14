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
#Haskell
Haskell tamamen işlevsel, statik olarak yazılan, tembelce değerlendirilen bir programlama dilidir. İlk olarak 1990'da standartlaştırılan (Haskell 90) ve birden fazla versiyonla (Haskell 2010 mevcut standarttır) iyileştirilen Haskell, matematiksel titizliği, güçlü tip sistemi (tip sınıfları, monadlar ve cebirsel veri türleriyle) ve türler aracılığıyla doğruluğa verdiği önemle tanınır.
Haskell yaygın bir dil olmasa da etkisi çok büyüktür. Monadlar, tembel değerlendirme ve tip sınıfları gibi kavramlar Rust, Swift, Kotlin, Scala ve TypeScript'i etkilemiştir. Haskell finansta (Standard Chartered, Barclays), derleyicilerde (GHC) ve resmi doğrulamada kullanılır.
---

## Haskell Neden Önemlidir
- **Saf işlevler**: Varsayılan olarak yan etki yoktur — işlevler her zaman aynı giriş için aynı çıktıyı döndürür.
- **Yazım sistemi**: Tüm diller arasında en anlamlı dillerden biri — derleme zamanında diğer dillerin yakalayamadığı hataları yakalar.
- **Tembel değerlendirme**: Hesaplamalar ihtiyaç duyulana kadar ertelenir; sonsuz veri yapılarına ve verimli kompozisyona olanak tanır.
- **Matematiksel temel**: Lambda hesabı ve kategori teorisine dayalı — programlar matematiksel kanıtlara daha yakındır.
- **Etki**: Haskell'in fikirleri çoğu modern dili şekillendirmiştir.
- **Eşzamanlılık**: Yazılım İşlemsel Belleği (STM), zarif eşzamanlı programlama sağlar.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Dik öğrenme eğrisi** | Monad'lar, işlevler, tür sınıfları — emir dillerinden çok farklı | Zamana yatırım yapın; kavramlar aktarılabilir |
| **Tembel değerlendirme sürprizleri** | Beklenmedik bellek kullanımına ve performans sorunlarına neden olabilir | Gerektiğinde katı değerlendirme (`!`) kullanın |
| **Daha küçük ekosistem** | Python, Java veya JavaScript'ten daha az kitaplık | Hacking artıyor; birçok kaliteli paket |
| **İş piyasası** | Niş — çoğunlukla finans, araştırma ve derleyici işi | İşlevsel programlama topluluklarında büyümek |
| **Derleme hızı** | GHC büyük projeler için yavaş olabilir | Etkileşimli geliştirme için GHCi'yi kullanın |
---

## Söz Diziminin Temelleri
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

## Gelişmiş Sözdizimi ve Desenler
### Tür Aileleri — Tür Düzeyinde İşlevler
Tür aileleri, işlevlerin değer düzeyinde değerleri hesaplamasına benzer şekilde, türleri tür düzeyinde hesaplamanıza olanak tanır.
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

### GADT'ler — Genelleştirilmiş Cebirsel Veri Türleri
GADT'ler, her oluşturucunun dönüş türünü tam olarak belirtmenize olanak tanıyarak tür açısından güvenli yorumlayıcılara ve yerleşik DSL'lere olanak tanır.
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

### Monad Transformatörleri
Monad transformatörleri tekli efektleri bir araya getirerek GÇ, durum, hata işleme ve daha fazlasını birleştirmenize olanak tanır.
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

### İşlevsel, Uygulamalı ve Monad Hiyerarşisi
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

### Gelişmiş Desen Eşleştirme
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

### Tembel ve Katı Değerlendirme
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

## Eşzamanlılık ve Paralellik
### Yazılım İşlemsel Belleği (STM)
STM, paylaşılan durum için (veritabanı işlemleri gibi) ancak bellek için birleştirilebilir işlemler sağlar.
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

### Eşzamanlı Eşzamansız İşlemler
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

### Paralel Stratejiler
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı (Yığın/Kabal)
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

### Yığın Yapılandırması (stack.yaml)
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

### Paket Açıklaması (hpack için package.yaml)
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

### Anahtar Oluşturma Komutları
| Komut | Açıklama |
|-----------|------------|
| `stack new my-project`| Şablondan yeni proje oluştur |
| `stack build`| Projeyi oluşturun |
| `stack ghci`| Proje yüklüyken etkileşimli REPL'i başlatın |
| `stack test`| Test paketini çalıştırın |
| `stack bench`| Karşılaştırmaları çalıştırın |
| `stack haddock`| Dokümantasyon oluşturun |
| `stack exec my-app`| Yürütülebilir dosyayı çalıştırın |
| `stack clean`| Temiz yapı eserleri |
| `stack update`| Paket dizinini güncelle |
| `stack freeze`| Tam bağımlılık sürümlerini sabitleyin |
### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### HSpec — Birim Test Çerçevesi
HSpec, Ruby'nin RSpec'inden ilham alan en popüler test çerçevesidir. BDD tarzı bir sözdizimi sağlar.
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

### QuickCheck ile Özellik Tabanlı Test
QuickCheck, kodunuzun özelliklerini doğrulamak için rastgele test senaryoları oluşturur.
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

### Test Komutları
| Komut | Açıklama |
|-----------|------------|
| `stack test`| Tüm test paketlerini çalıştırın |
| `stack test --fast`| Daha hızlı test derlemeleri için optimizasyonları atlayın |
| `stack build --test --test-arguments "--color"`| Testleri renkli çıktıyla çalıştırın |
| `stack ghci --test`| REPL'de test modüllerini yükleyin |

---

## Birlikte Çalışabilirlik
### C Yabancı Fonksiyon Arayüzü (FFI)
Haskell, C işlevlerini doğrudan arayabilir ve Haskell işlevlerini C'ye gösterebilir.
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

### Python Birlikte Çalışma (satır içi-c veya HPy aracılığıyla)
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

## Tasarım Desenleri
### Etiketsiz Final (Yerleşik DSL'ler)
Etiketsiz son stil, DSL'leri tür sınıflarını kullanarak kodlayarak birden fazla yorumlamaya olanak tanır.
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

### Ücretsiz Monadlar
Serbest monadlar, etkilerin tanımını yorumlarından ayırır.
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

### Uygulama Mimarisi için ReaderT Modeli
ReaderT modeli, bağımlılık enjeksiyonuna yönelik modern Haskell yaklaşımıdır.
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

## Performans ve Optimizasyon
### Profil Oluşturma Araçları
| Araç | Amaç | Komut |
|------|---------|--------|
| **GHC Profil Oluşturucu** | Zaman ve tahsis profili oluşturma | `stack build --profile`ardından`./app +RTS -p`|
| **ThreadScope** | Paralel yürütmeyi görselleştirin | `./app +RTS -l`ardından `app.eventlog`'yi açın |
| **ghc-olayları** | Olay günlüklerini analiz edin | `ghc-events show app.eventlog`|
| **Kriter** | İstatistiksel kıyaslama |`criterion`paketini kullanın |
| **hp2güzel** | Yığın profillerini görselleştirin | `./app +RTS -h`ardından`hp2pretty app.hp`|
### Kriterle Karşılaştırma
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

### Optimizasyon Teknikleri
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

## Dağıtım
### Yapı Sürümü İkili Dosyaları
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### Docker Dağıtımı
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

### Nix Tabanlı Dağıtım
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

## Haskell Ne Zaman Kullanılmalı
| Senaryo | Neden Haskell | Daha İyi Alternatif |
|----------|-----------|-----------|
| Resmi doğrulama | Tip sistemi kanıtları mümkün kılar | Ağda, Coq |
| Derleyici geliştirme | Dil uygulaması için mükemmel | OCaml, Pas |
| Finansal sistemler | Türlere göre doğruluk | Scala, F# |
| FP kavramlarını öğrenme | En saf işlevsel dil | Scala (daha pratik), Karaağaç |
| Genel uygulama geliştirme | Mümkün ama niş | Python, Git, Java |
| Web geliştirme | Yesod/Hizmetçi var ama sınırlı | JavaScript/TypeScript |
| Veri bilimi | Ekosistem değil | Python, R |
---

## Sentetik Soru-Cevap
### S1: Haskell'in tembel değerlendirmesi performansı nasıl etkiler?
**C:** Tembel değerlendirme, ifadelerin yalnızca ihtiyaç duyulduğunda hesaplanması anlamına gelir; bu da sonsuz veri yapılarına ve şekillendirilebilir işlem hatlarına olanak tanır. Ancak, eğer yığınlar birikirse alan sızıntılarına neden olabilir:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

Sayısal katlamalar için`foldl`yerine`foldl'`(`Data.List`'den) kullanın. Gerektiğinde değerlendirmeyi zorlamak için`!`patlama desenlerini veya `seq`'yi kullanın.
### S2: `Functor`,`Applicative`ve`Monad`arasındaki pratik fark nedir?
**A:** Her tür sınıfı aşağıdaki yetenekleri ekler:
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

**Functor** saf bir işlevi bir bağlam üzerinde eşler. **Uygulayıcı** kendileri bir bağlamda olan işlevleri uygular. **Monad** her adımın bir önceki adımın sonucuna bağlı olmasını sağlar. Uygulamada: basit dönüşümler için`fmap`/ `<$>`, efektleri birleştirmek için`<*>`ve sıralı bağımlı hesaplamalar için`>>=`/`do`kullanın.
### S3: Saf Haskell kodundaki yan etkileri nasıl ele alabilirim?
**A:** Saf ve etkili kodu ayırmak için tür sistemini kullanın:
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

Temel mantığı saf tutun ve efektleri kenarlara doğru itin. Yapılandırma için `ReaderT`'yi, hatalar için `ExceptT`'yi ve değiştirilebilir durum için `StateT`'yi kullanın.
### S4: Tür sınıfları nelerdir ve bunların OOP arayüzlerinden farkı nedir?
**C:** Tür sınıfları, türlerin uygulayabileceği davranışı tanımlar. OOP arayüzlerinin aksine, açıktırlar (herhangi bir tür örnek olabilir) ve geçici polimorfizmi destekler:
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

### S5: Bir Haskell projesini gerçek dünyada kullanım için nasıl yapılandırabilirim?
**C:** Cabal veya Stack'i standart bir düzende kullanın:
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

Temel uygulamalar: GÇ'yi `Main.hs`'de veya özel bir`IO`modülünde tutun, çekirdek mantığı saf ve test edilebilir hale getirin, etki alanı türleri için`newtype`sarmalayıcıları kullanın.
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Hata Raporlamayla Güvenli Bölme Fonksiyonunun Uygulanması
**1. Adım: Sorunu Anlayın**
Sıfıra bölme işlemini gerçekleştiren ve yalnızca çökmeleri değil, anlamlı hataları da bildiren bölmeye ihtiyacımız var.
**2. Adım: Yaklaşımı Belirleyin**
Bir hata mesajı veya sonuç döndürmek için `Either`'yi kullanın. Bu, başarısızlık olasılığını türde açıkça ortaya koyar.
**3. Adım: Uygulama**```haskell
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

**4. Adım: Doğrulayın**
Tip sistemi, arayanların hata durumunu ele alması gerektiğini garanti eder. Desen eşleştirme veya`either`açık işlemeyi zorlar.
### Sorun 2: Basit Yapılandırma Dilini Ayrıştırma
**1. Adım: Sorunu Anlayın**
Anahtar/değer çiftlerini`name=Alice\nage=30`gibi bir dizeden ayrıştırın.
**2. Adım: Yaklaşımı Belirleyin**
`Text.Parsec` veya manuel yinelemeyi kullanın. Basit olması açısından`break`ve`span`kullanın.
**3. Adım: Uygulama**```haskell
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

**4. Adım: Genişletin**
Yorum işleme (`#`), bölüm başlıkları (`[section]`) ekleyin ve`Value`ADT kullanarak zorlama yazın.
### Problem 3: Tembellikle Notlandırılmış Fibonacci Oluşturmak
**1. Adım: Sorunu Anlayın**
Fibonacci sayılarını verimli bir şekilde hesaplayın. Saf özyineleme üsteldir.
**2. Adım: Yaklaşımı Belirleyin**
Her öğenin bir kez hesaplandığı ve önbelleğe alındığı sonsuz bir liste oluşturmak için Haskell'in tembel değerlendirmesini kullanın.
**3. Adım: Uygulama**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**4. Adım: Optimize edin**
Rastgele erişim için tembel yapıyla`Data.Array`kullanın. Çok büyük indeksler için O(log n) cinsinden matris üssünü kullanın.
### Problem 4: Basit Durum Makinesinin Uygulanması
**1. Adım: Sorunu Anlayın**
Kırmızı -> Yeşil -> Sarı -> Kırmızı şeklinde dönen bir trafik ışığı modelleyin.
**2. Adım: Yaklaşımı Belirleyin**
Durumlar için cebirsel bir veri türü ve saf bir geçiş fonksiyonu kullanın.
**3. Adım: Uygulama**```haskell
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

**4. Adım: Doğrulayın**
Saf işlevler önemsiz bir şekilde test edilebilir:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## Özet
Haskell, işlevsel programlamanın ana dildeki en saf ifadesidir. Tip sistemi en güçlüleri arasındadır ve saf işlevlere yaptığı vurgu, üzerinde düşünmesi ve test etmesi daha kolay kod üretir. Haskell endüstride yaygın olarak kullanılmasa da fikirleri modern programlamayı derinden etkilemiştir. Haskell'i öğrenmek, programlama hakkındaki düşüncelerinizi değiştirir - onu asla profesyonelce kullanmasanız bile.