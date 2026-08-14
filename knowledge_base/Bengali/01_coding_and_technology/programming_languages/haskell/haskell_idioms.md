---
# Metadata
title: "Haskell — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, idiomatic Haskell code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [haskell, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# হাসকেল — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অনুশীলন
এই নির্দেশিকাটি পরিচ্ছন্ন, ইডিওম্যাটিক হাসকেল কোড লেখার জন্য ইডিওম্যাটিক প্যাটার্ন এবং সর্বোত্তম অনুশীলনগুলি কভার করে।
---

## প্রকার ও ডেটা
```haskell
-- ✅ Use newtype for single-field wrappers
newtype UserId = UserId Int deriving (Eq, Show)
newtype Email = Email Text deriving (Eq, Show)

-- ✅ Algebraic data types
data User = User
  { userName  :: Text
  , userEmail :: Email
  , userAge   :: Int
  } deriving (Show, Eq)

-- ✅ Smart constructors
mkUser :: Text -> Text -> Int -> Either Text User
mkUser name email age
  | Text.null name = Left "Name required"
  | age < 0        = Left "Invalid age"
  | otherwise      = Right $ User name (Email email) age

-- ✅ Type aliases for readability
type UserName = Text
type Handler = Request -> IO Response
```

---

## প্যাটার্ন ম্যাচিং
```haskell
-- ✅ Exhaustive pattern matching
describe :: Maybe Int -> String
describe Nothing  = "Nothing"
describe (Just 0) = "Zero"
describe (Just n)
  | n > 0     = "Positive"
  | otherwise = "Negative"

-- ✅ Case expressions
result = case lookup key env of
  Just val -> process val
  Nothing  -> defaultValue

-- ✅ View patterns
-- ✅ Pattern guards
classify n
  | n < 0     = "negative"
  | n == 0    = "zero"
  | otherwise = "positive"
```

---

## Monads এবং Functors
```haskell
-- ✅ fmap / <$> for mapping
nameLength = length <$> getName user

-- ✅ Applicative for combining
result = pure User
  <*> parseName input
  <*> parseEmail input
  <*> parseAge input

-- ✅ Monad for sequencing
do
  user <- findUser userId
  orders <- findOrders (userId user)
  pure (user, orders)

-- ✅ Maybe monad
result = do
  user <- findUser 1
  addr <- userAddress user
  city <- addressCity addr
  pure city

-- ✅ Either for errors
parseConfig :: Text -> Either ConfigError Config
parseConfig input = do
  host <- parseHost input
  port <- parsePort input
  pure Config { host, port }
```

---

## কার্যকরী নিদর্শন
```haskell
-- ✅ Point-free style (when clearer)
totalLength = sum . map Text.length

-- ✅ Function composition
process = validate . normalize . parse

-- ✅ fold for accumulation
total = foldl' (+) 0 numbers

-- ✅ traverse for effects
results = traverse validateItem items

-- ✅ mapM / forM (less preferred, use traverse)
mapM_ print items

-- ✅ Lens for nested data
-- user ^. address . city
-- address . city .~ "NYC" $ user
```

---

## ত্রুটি হ্যান্ডলিং
```haskell
-- ✅ Either for expected errors
type AppError = Text
findUser :: UserId -> IO (Either AppError User)

-- ✅ ExceptT for monadic error handling
type App a = ExceptT AppError IO a

-- ✅ Custom exceptions (for truly exceptional cases)
data AppException = DatabaseError Text | NotFound Text
  deriving (Show, Typeable)
instance Exception AppException

-- ✅ Maybe for absence
findUser :: UserId -> IO (Maybe User)
```

---

## কঠোরতা
```haskell
-- ✅ Bang patterns for strict evaluation
factorial :: Int -> Integer -> Integer
factorial !0 !acc = acc
factorial !n !acc = factorial (n - 1) (acc * n)

-- ✅ Strict data types
data StrictPair a b = StrictPair !a !b

-- ✅ seq for evaluation
let !result = expensiveComputation x
in result + 1
```

---

## সারাংশ
হাসকেল ইডিয়মগুলি জোর দেয়: শক্তিশালী প্রকার, প্যাটার্ন ম্যাচিং, প্রভাবের জন্য মোনাড, বিশুদ্ধ ফাংশন এবং অলস মূল্যায়ন (প্রয়োজনে কঠোরতার সাথে)। Haskell শৈলী নির্দেশিকা অনুসরণ করুন, পরামর্শের জন্য`hlint`এবং বিন্যাসের জন্য`fourmolu`ব্যবহার করুন৷ হাস্কেল সঠিকতা এবং রচনাকে মূল্য দেয় - "অবৈধ রাষ্ট্রগুলিকে অপ্রতিরোধ্য করে তোলে।"