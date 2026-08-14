<!--
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

-->
# Haskell — 惯用模式和最佳实践
本指南涵盖了编写干净、惯用的 Haskell 代码的惯用模式和最佳实践。
---

## 类型和数据
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

## 模式匹配
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

## 单子和函子
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

## 函数式模式
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

## 错误处理
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

## 严格性
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

＃＃ 概括
Haskell 习语强调：强类型、模式匹配、效果单子、纯函数和惰性求值（需要时严格执行）。遵循 Haskell 风格指南，使用`hlint`获取建议，使用`fourmolu`进行格式化。哈斯克尔重视正确性和组合——“让非法国家无法代表”。