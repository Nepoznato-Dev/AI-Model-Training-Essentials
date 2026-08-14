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

# हास्केल
हास्केल एक पूरी तरह कार्यात्मक, स्थिर रूप से टाइप की गई, आलसी मूल्यांकन वाली प्रोग्रामिंग भाषा है। पहली बार 1990 में मानकीकृत (हास्केल 90) और कई संस्करणों के माध्यम से परिष्कृत (हास्केल 2010 वर्तमान मानक है), हास्केल अपनी गणितीय कठोरता, शक्तिशाली प्रकार प्रणाली (प्रकार वर्गों, मोनैड और बीजगणितीय डेटा प्रकारों के साथ) और प्रकारों के माध्यम से शुद्धता पर जोर देने के लिए जाना जाता है।
हास्केल मुख्यधारा की भाषा नहीं है, लेकिन इसका प्रभाव बहुत बड़ा है। सन्यासी, आलसी मूल्यांकन और टाइप क्लास जैसी अवधारणाओं ने रस्ट, स्विफ्ट, कोटलिन, स्काला और टाइपस्क्रिप्ट को प्रभावित किया है। हास्केल का उपयोग वित्त (स्टैंडर्ड चार्टर्ड, बार्कलेज), कंपाइलर्स (जीएचसी), और औपचारिक सत्यापन में किया जाता है।
---

## हास्केल क्यों मायने रखता है
- **शुद्ध फ़ंक्शन**: डिफ़ॉल्ट रूप से कोई साइड इफेक्ट नहीं - फ़ंक्शन हमेशा समान इनपुट के लिए समान आउटपुट लौटाते हैं।
- **टाइप सिस्टम**: किसी भी भाषा में सबसे अधिक अभिव्यंजक - संकलन के समय बग पकड़ता है जिसे अन्य भाषाएं नहीं पकड़ सकतीं।
- **आलसी मूल्यांकन**: आवश्यकता पड़ने तक गणनाओं को स्थगित कर दिया जाता है - अनंत डेटा संरचनाओं और कुशल संरचना को सक्षम बनाता है।
- **गणितीय आधार**: लैम्ब्डा कैलकुलस और श्रेणी सिद्धांत पर आधारित - कार्यक्रम गणितीय प्रमाणों के करीब हैं।
- **प्रभाव**: हास्केल के विचारों ने अधिकांश आधुनिक भाषाओं को आकार दिया है।
- **कंकरेंसी**: सॉफ्टवेयर ट्रांजेक्शनल मेमोरी (एसटीएम) सुरुचिपूर्ण समवर्ती प्रोग्रामिंग प्रदान करता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **सीखने की तीव्र अवस्था** | मोनैड्स, फ़ंक्टर, टाइप क्लासेस - अनिवार्य भाषाओं से बहुत अलग | निवेश का समय; अवधारणाएँ हस्तांतरणीय हैं |
| **आलसी मूल्यांकन आश्चर्य** | अप्रत्याशित मेमोरी उपयोग और प्रदर्शन संबंधी समस्याएं पैदा हो सकती हैं | जहां आवश्यक हो वहां सख्त मूल्यांकन (`!`) का उपयोग करें |
| **छोटा पारिस्थितिकी तंत्र** | पायथन, जावा, या जावास्क्रिप्ट की तुलना में कम पुस्तकालय | हैकेज बढ़ रहा है; कई गुणवत्ता पैकेज |
| **नौकरी बाज़ार** | आला - ज्यादातर वित्त, अनुसंधान और संकलक कार्य | कार्यात्मक प्रोग्रामिंग समुदायों में वृद्धि |
| **संकलन गति** | बड़ी परियोजनाओं के लिए जीएचसी धीमी हो सकती है | इंटरैक्टिव विकास के लिए जीएचसीआई का उपयोग करें |
---

## सिंटेक्स बुनियादी बातें
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

## उन्नत सिंटैक्स और पैटर्न
### प्रकार के परिवार - प्रकार-स्तर के कार्य
प्रकार परिवार आपको प्रकार के स्तर पर प्रकारों की गणना करने की अनुमति देते हैं, ठीक उसी तरह जैसे फ़ंक्शन मूल्य स्तर पर मानों की गणना करते हैं।
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

### GADTs - सामान्यीकृत बीजगणितीय डेटा प्रकार
जीएडीटी आपको प्रत्येक कंस्ट्रक्टर के रिटर्न प्रकार को सटीक रूप से निर्दिष्ट करने देता है, जिससे टाइप-सुरक्षित दुभाषिए और एम्बेडेड डीएसएल सक्षम होते हैं।
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

### मोनाड ट्रांसफार्मर
मोनाड ट्रांसफॉर्मर मोनाडिक प्रभावों को ढेर कर देते हैं, जिससे आपको आईओ, स्थिति, त्रुटि प्रबंधन और बहुत कुछ संयोजित करने की सुविधा मिलती है।
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

### फ़ंक्टर, एप्लिकेटिव, और मोनाड पदानुक्रम
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

### उन्नत पैटर्न मिलान
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

### आलसी बनाम सख्त मूल्यांकन
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

## समवर्ती एवं समांतरता
### सॉफ्टवेयर ट्रांजेक्शनल मेमोरी (एसटीएम)
एसटीएम साझा स्थिति के लिए कंपोजेबल लेनदेन प्रदान करता है - जैसे डेटाबेस लेनदेन लेकिन मेमोरी के लिए।
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

### समवर्ती एसिंक संचालन
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

### समानांतर रणनीतियाँ
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना (स्टैक/कैबल)
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

### स्टैक कॉन्फ़िगरेशन (stack.yaml)
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

### पैकेज विवरण (hpack के लिए package.yaml)
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

### कुंजी निर्माण आदेश
| आदेश | विवरण |
|---------|-----------------|
| `stack new my-project`| टेम्पलेट से नया प्रोजेक्ट बनाएं |
| `stack build`| प्रोजेक्ट बनाएं |
| `stack ghci`| लोड किए गए प्रोजेक्ट के साथ इंटरैक्टिव आरईपीएल प्रारंभ करें |
| `stack test`| परीक्षण सुइट चलाएँ |
| `stack bench`| बेंचमार्क चलाएं |
| `stack haddock`| दस्तावेज़ तैयार करें |
| `stack exec my-app`| निष्पादन योग्य चलाएँ |
| `stack clean`| स्वच्छ निर्मित कलाकृतियाँ |
| `stack update`| पैकेज इंडेक्स अपडेट करें |
| `stack freeze`| सटीक निर्भरता संस्करण पिन करें |
### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### एचस्पेक - यूनिट टेस्टिंग फ्रेमवर्क
HSpec सबसे लोकप्रिय परीक्षण ढांचा है, जो रूबी के RSpec से प्रेरित है। यह BDD-शैली सिंटैक्स प्रदान करता है।
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

### क्विकचेक के साथ संपत्ति-आधारित परीक्षण
क्विकचेक आपके कोड के गुणों को सत्यापित करने के लिए यादृच्छिक परीक्षण मामले उत्पन्न करता है।
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

### टेस्ट कमांड
| आदेश | विवरण |
|---------|-----------------|
| `stack test`| सभी परीक्षण सुइट चलाएँ |
| `stack test --fast`| तेज़ परीक्षण बिल्ड के लिए अनुकूलन छोड़ें |
| `stack build --test --test-arguments "--color"`| रंगीन आउटपुट के साथ परीक्षण चलाएँ |
| `stack ghci --test`| आरईपीएल में परीक्षण मॉड्यूल लोड करें |

---

## अंतरसंचालनीयता
### सी फॉरेन फंक्शन इंटरफ़ेस (एफएफआई)
हास्केल सी फ़ंक्शंस को सीधे कॉल कर सकता है और हास्केल फ़ंक्शंस को सी में प्रदर्शित कर सकता है।
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

### पायथन इंटरऑप (इनलाइन-सी या एचपीवाई के माध्यम से)
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

## डिज़ाइन पैटर्न
### टैग रहित फ़ाइनल (एम्बेडेड डीएसएल)
टैग रहित अंतिम शैली कई व्याख्याओं को सक्षम करते हुए, प्रकार वर्गों का उपयोग करके डीएसएल को एन्कोड करती है।
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

### मुक्त भिक्षु
मुक्त सन्यासी प्रभावों के विवरण को उनकी व्याख्या से अलग करते हैं।
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

### एप्लीकेशन आर्किटेक्चर के लिए रीडरटी पैटर्न
रीडरटी पैटर्न निर्भरता इंजेक्शन के लिए आधुनिक हास्केल दृष्टिकोण है।
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

## प्रदर्शन एवं अनुकूलन
### प्रोफाइलिंग उपकरण
| उपकरण | उद्देश्य | आदेश |
|------|------|---------|
| **जीएचसी प्रोफाइलर** | समय और आवंटन प्रोफाइलिंग | `stack build --profile`फिर`./app +RTS -p`|
| **थ्रेडस्कोप** | समानांतर निष्पादन की कल्पना करें | `./app +RTS -l`फिर`app.eventlog`| खोलें
| **ghc-घटनाएँ** | इवेंट लॉग का विश्लेषण करें | `ghc-events show app.eventlog`|
| **मानदंड** | सांख्यिकीय बेंचमार्किंग |`criterion`पैकेज का उपयोग करें |
| **hp2सुन्दर** | ढेर प्रोफाइल विज़ुअलाइज़ करें | `./app +RTS -h`फिर`hp2pretty app.hp`|
### मानदंड के साथ बेंचमार्किंग
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

### अनुकूलन तकनीकें
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

## तैनाती
### बिल्डिंग रिलीज बायनेरिज़
```bash
# Build a static binary with Stack
stack build --copy-bins --local-bin-path ./dist

# Build a fully static binary (Linux) using Nix
stack build --docker --docker-image haskell:9.4

# Using cabal directly
cabal build all
cabal install --install-method=copy --overwrite-policy=always
```

### डॉकर परिनियोजन
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

### निक्स-आधारित परिनियोजन
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

## हास्केल का उपयोग कब करें
| परिदृश्य | हास्केल क्यों | बेहतर विकल्प |
|---|----|-----|
| औपचारिक सत्यापन | प्रकार प्रणाली प्रमाणों को सक्षम बनाती है | अगडा, कॉक |
| संकलक विकास | भाषा कार्यान्वयन के लिए उत्कृष्ट | ओकैमल, जंग |
| वित्तीय प्रणालियाँ | प्रकारों के माध्यम से शुद्धता | स्काला, एफ# |
| एफपी अवधारणाओं को सीखना | शुद्धतम कार्यात्मक भाषा | स्काला (अधिक व्यावहारिक), एल्म |
| सामान्य अनुप्रयोग विकास | संभव लेकिन आला | पायथन, गो, जावा |
| वेब विकास | यसोड/सेवक अस्तित्व में है लेकिन सीमित है | जावास्क्रिप्ट/टाइपस्क्रिप्ट |
| डेटा विज्ञान | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1: हास्केल का आलसी मूल्यांकन प्रदर्शन को कैसे प्रभावित करता है?
**ए:** आलसी मूल्यांकन का मतलब है कि अभिव्यक्ति की गणना केवल जरूरत पड़ने पर की जाती है, जिससे अनंत डेटा संरचनाएं और कंपोज़ेबल पाइपलाइन सक्षम हो जाती हैं। हालाँकि, यदि टुकड़े जमा हो जाते हैं तो यह स्थान रिसाव का कारण बन सकता है:
```haskell
-- Lazy: creates a chain of thunks, may leak space
sum' :: [Int] -> Int
sum' = foldl (+) 0

-- Strict: evaluates immediately, no thunk buildup
sumStrict :: [Int] -> Int
sumStrict = foldl' (+) 0  -- foldl' is strict in the accumulator
```

संख्यात्मक तहों के लिए`foldl`के बजाय`foldl'`(`Data.List` से) का उपयोग करें। आवश्यकता पड़ने पर मूल्यांकन को बाध्य करने के लिए`!`बैंग पैटर्न या`seq`का उपयोग करें।
### Q2:`Functor`,`Applicative`और`Monad`के बीच व्यावहारिक अंतर क्या है?
**ए:** प्रत्येक टाइपक्लास क्षमता जोड़ता है:
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

**फ़ंक्टर** एक संदर्भ पर एक शुद्ध फ़ंक्शन को मैप करता है। **एप्लिकेटिव** उन कार्यों को लागू करता है जो स्वयं एक संदर्भ में हैं। **मोनाड** प्रत्येक चरण को पिछले चरण के परिणाम पर निर्भर करता है। व्यवहार में: सरल परिवर्तनों के लिए`fmap`/ `<$>`, प्रभावों के संयोजन के लिए`<*>`और अनुक्रमिक निर्भर गणनाओं के लिए`>>=`/`do`का उपयोग करें।
### Q3: मैं शुद्ध हास्केल कोड में साइड इफेक्ट्स को कैसे संभाल सकता हूं?
**ए:** शुद्ध और प्रभावी कोड को अलग करने के लिए टाइप सिस्टम का उपयोग करें:
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

मूल तर्क को शुद्ध रखें और किनारों पर प्रभाव डालें। कॉन्फ़िगरेशन के लिए `ReaderT`, त्रुटियों के लिए`ExceptT`और परिवर्तनीय स्थिति के लिए`StateT`का उपयोग करें।
### Q4: प्रकार की कक्षाएं क्या हैं और वे OOP इंटरफेस से कैसे भिन्न हैं?
**ए:** प्रकार वर्ग उस व्यवहार को परिभाषित करते हैं जिसे प्रकार लागू कर सकते हैं। ओओपी इंटरफेस के विपरीत, वे खुले हैं (कोई भी प्रकार एक उदाहरण हो सकता है) और तदर्थ बहुरूपता का समर्थन करते हैं:
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

### Q5: मैं वास्तविक दुनिया में उपयोग के लिए हास्केल प्रोजेक्ट की संरचना कैसे करूं?
**ए:** मानक लेआउट के साथ कैबल या स्टैक का उपयोग करें:
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

मुख्य अभ्यास: IO को`Main.hs`या एक समर्पित`IO`मॉड्यूल में रखें, कोर लॉजिक को शुद्ध और परीक्षण योग्य बनाएं, डोमेन प्रकारों के लिए`newtype`रैपर का उपयोग करें।
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: त्रुटि रिपोर्टिंग के साथ एक सुरक्षित डिवीजन फ़ंक्शन को कार्यान्वित करना
**चरण 1: समस्या को समझें**
हमें ऐसे विभाजन की आवश्यकता है जो शून्य से विभाजन को संभाल सके और सार्थक त्रुटियों की रिपोर्ट करे, न कि केवल क्रैश की।
**चरण 2: दृष्टिकोण को पहचानें**
त्रुटि संदेश या परिणाम वापस करने के लिए`Either`का उपयोग करें। इससे प्रकार में विफलता की संभावना स्पष्ट हो जाती है।
**चरण 3: कार्यान्वयन**```haskell
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

**चरण 4: सत्यापित करें**
टाइप सिस्टम गारंटी देता है कि कॉल करने वालों को त्रुटि मामले को संभालना होगा। पैटर्न मिलान या`either`स्पष्ट हैंडलिंग को बाध्य करता है।
### समस्या 2: एक सरल कॉन्फ़िगरेशन भाषा को पार्स करना
**चरण 1: समस्या को समझें**
`name=Alice\nage=30` जैसी स्ट्रिंग से कुंजी-मान जोड़े को पार्स करें।
**चरण 2: दृष्टिकोण को पहचानें**
`Text.Parsec` या मैन्युअल रिकर्सन का उपयोग करें। सरलता के लिए,`break`और`span`का उपयोग करें।
**चरण 3: कार्यान्वयन**```haskell
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

**चरण 4: विस्तार करें**
टिप्पणी प्रबंधन (`#`), अनुभाग शीर्षलेख (`[section]`) जोड़ें, और`Value`ADT का उपयोग करके जबरदस्ती टाइप करें।
### समस्या 3: आलस्य के साथ एक मेमोइज़्ड फाइबोनैचि का निर्माण
**चरण 1: समस्या को समझें**
फाइबोनैचि संख्याओं की कुशलतापूर्वक गणना करें। अनुभवहीन प्रत्यावर्तन घातांकीय है।
**चरण 2: दृष्टिकोण को पहचानें**
एक अनंत सूची बनाने के लिए हास्केल के आलसी मूल्यांकन का उपयोग करें जहां प्रत्येक तत्व की एक बार गणना की जाती है और कैश किया जाता है।
**चरण 3: कार्यान्वयन**```haskell
-- Lazy infinite list — each value computed once
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- Access any element in O(n)
fib :: Int -> Integer
fib n = fibs !! n

-- Take first 20
-- take 20 fibs  -- [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
```

**चरण 4: अनुकूलन करें**
रैंडम एक्सेस के लिए, आलसी निर्माण के साथ`Data.Array`का उपयोग करें। बहुत बड़े सूचकांकों के लिए, O(log n) में मैट्रिक्स घातांक का उपयोग करें।
### समस्या 4: एक सरल राज्य मशीन लागू करना
**चरण 1: समस्या को समझें**
एक ट्रैफिक लाइट का मॉडल बनाएं जो लाल -> हरा -> पीला -> लाल चक्र करती हो।
**चरण 2: दृष्टिकोण को पहचानें**
राज्यों और शुद्ध संक्रमण फ़ंक्शन के लिए बीजगणितीय डेटा प्रकार का उपयोग करें।
**चरण 3: कार्यान्वयन**```haskell
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

**चरण 4: सत्यापित करें**
शुद्ध कार्य तुच्छ रूप से परीक्षण योग्य हैं:```haskell
prop_cycle :: Bool
prop_cycle = transition (transition (transition Red)) == Red
```

---

## सारांश
हास्केल मुख्यधारा की भाषा में कार्यात्मक प्रोग्रामिंग की सबसे शुद्ध अभिव्यक्ति है। इसका प्रकार सिस्टम सबसे शक्तिशाली में से एक है, और शुद्ध कार्यों पर इसका जोर ऐसे कोड का उत्पादन करता है जिसके बारे में तर्क करना और परीक्षण करना आसान है। जबकि हास्केल का उद्योग में व्यापक रूप से उपयोग नहीं किया जाता है, इसके विचारों ने आधुनिक प्रोग्रामिंग को गहराई से प्रभावित किया है। हास्केल सीखने से प्रोग्रामिंग के बारे में आपकी सोच बदल जाती है - भले ही आपने इसे कभी भी पेशेवर रूप से उपयोग नहीं किया हो।