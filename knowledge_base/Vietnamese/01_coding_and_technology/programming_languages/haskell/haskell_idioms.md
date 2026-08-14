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
# Haskell — Các mẫu thành ngữ & các phương pháp hay nhất
Hướng dẫn này bao gồm các mẫu thành ngữ và các phương pháp thực hành tốt nhất để viết mã Haskell thuần túy, thuần túy.
---

## Loại & Dữ liệu
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

## Khớp mẫu
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

## Đơn nguyên & Hàm số
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

## Mẫu chức năng
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

## Xử lý lỗi
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

## Sự nghiêm khắc
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

## Bản tóm tắt
Thành ngữ Haskell nhấn mạnh: kiểu mạnh, khớp mẫu, đơn nguyên cho hiệu ứng, hàm thuần túy và đánh giá lười biếng (với mức độ nghiêm ngặt khi cần thiết). Làm theo Hướng dẫn về phong cách Haskell, sử dụng`hlint`để nhận đề xuất và`fourmolu`để định dạng. Haskell đánh giá cao tính đúng đắn và bố cục — "làm cho các trạng thái bất hợp pháp không thể đại diện được."