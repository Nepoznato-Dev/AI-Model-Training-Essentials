<!--
---
# Metadata
title: "Haskell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Haskell ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [haskell, ecosystem, tooling, cabal, stack, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# ہاسکل - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ ہاسکل ایکو سسٹم میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## ٹول چین
| ٹول | مقصد |
|------|---------|
| **GHC** | گلاسگو ہاسکل کمپائلر (مرتب) |
| **GHCup** | ہاسکل ٹول چین انسٹالر |
| **کیبل** | سسٹم اور پیکیج کی شکل بنائیں |
| **اسٹیک** | تولیدی تعمیر کا آلہ |
| **کیبل-انسٹال** | پیکیج مینیجر |
| **ہاسکل-لینگویج-سرور (HLS)** | LSP سرور |
| **ghcid** | تیزی سے رائے مرتب کریں |
| **فورمولو** | کوڈ فارمیٹر |
| **اورمولو** | کوڈ فارمیٹر |
| **ہلنٹ** ​​| لنٹر / تجاویز |
```bash
ghcup install ghc latest    # install GHC
ghcup install cabal latest  # install Cabal
ghcup install stack latest  # install Stack

cabal init                  # new project
cabal build                 # build
cabal test                  # run tests
cabal run myapp             # run
cabal repl                  # interactive REPL

stack new myapp             # new project
stack build                 # build
stack test                  # run tests
stack exec myapp            # run
```

---

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **ہیکیج** | مرکزی پیکیج ریپوزٹری (15,000+ پیکجز) |
| **اسٹیکیج** | کیوریٹڈ، ہم آہنگ پیکیج سیٹ |
| **کیبل** | پیکیج کی شکل اور تعمیر کا آلہ |
| **اسٹیک** | دوبارہ پیدا کرنے کے قابل تعمیرات (LTS سنیپ شاٹس) |
```cabal
-- myapp.cabal
cabal-version: 3.0
name:          myapp
version:       0.1.0.0
build-type:    Simple

executable myapp
  main-is:          Main.hs
  hs-source-dirs:   app
  default-language:  Haskell2010
  build-depends:     base >=4.18
                   , text
                   , aeson
                   , http-types
                   , warp
  ghc-options:      -Wall -Werror
```

```yaml
# stack.yaml
resolver: lts-22.12
packages:
  - .
extra-deps:
  - some-package-1.0.0
```

---

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **خادم** | قسم کی سطح | ٹائپ سیف APIs |
| **یسود** | مکمل اسٹیک | ٹائپ سیف ویب ایپس |
| **سکوٹی** | ہلکا پھلکا | سادہ APIs (Sinatra-like) |
| **سپوک** | ہلکا پھلکا | ویب ایپس |
| **IHP** | بیٹریاں شامل | ریلوں کی طرح، ہاسکل |
| **Miso** | فرنٹ اینڈ | ایلم جیسا فرنٹ اینڈ |
```haskell
-- Servant API example
type UserAPI =
       "users" :> Get '[JSON] [User]
  :<|> "users" :> Capture "id" Int :> Get '[JSON] User
  :<|> "users" :> ReqBody '[JSON] User :> Post '[JSON] User

server :: Server UserAPI
server = listUsers :<|> getUser :<|> createUser

api :: Proxy UserAPI
api = Proxy

app :: Application
app = serve api server

main :: IO ()
main = run 8080 app
```

---

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **مستقل** | ORM (یسوڈ ماحولیاتی نظام) |
| **hasql** | PostgreSQL (اعلی کارکردگی) |
| **postgresql-simple** | PostgreSQL (سادہ) |
| **بیم** | ٹائپ سیف ایس کیو ایل |
| **esqueleto** | ٹائپ سیف ESQL (مسلسل پر) |
| **ہیڈیس** | Redis کلائنٹ |
| **mongoDB** | MongoDB ڈرائیور |
```haskell
-- postgresql-simple example
import Database.PostgreSQL.Simple

main :: IO ()
main = do
  conn <- connect defaultConnectInfo { connectDatabase = "mydb" }
  users <- query_ conn "SELECT id, name, email FROM users" :: IO [User]
  mapM_ print users
```

---

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **HUnit** | یونٹ ٹیسٹنگ (xUnit-style) |
| ** مزیدار** | ٹیسٹ فریم ورک (کمپوز ایبل) |
| **سوادج-ہونیت** | سوادج کے لئے HUnit انضمام |
| **سوادج-فوری چیک** | جائیداد کی بنیاد پر جانچ |
| **کوئیک چیک** | جائیداد کی بنیاد پر جانچ |
| **ہیج ہاگ** | پراپرٹی پر مبنی (جدید) |
| **hspec** | BDD طرز کی جانچ |
| **ڈاکٹسٹ** | Haddock میں ٹیسٹ کی مثالیں |
| **سوادج دریافت** | خودکار دریافت ٹیسٹ |
```haskell
-- hspec example
module UserServiceSpec (spec) where

import Test.Hspec
import UserService

spec :: Spec
spec = describe "UserService" $ do
  describe "find" $ do
    it "returns user when found" $ do
      let repo = mkRepo [(1, "Alice")]
          service = mkService repo
      findUser service 1 `shouldReturn` Just (User 1 "Alice")

    it "returns Nothing when not found" $ do
      let repo = mkRepo []
          service = mkService repo
      findUser service 999 `shouldReturn` Nothing

-- QuickCheck property
prop_reverse :: [Int] -> Bool
prop_reverse xs = reverse (reverse xs) == xs
```

---

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **ہلنٹ** ​​| تجاویز اور linting |
| **فورمولو / اورمولو** | کوڈ فارمیٹنگ |
| **اسٹائلش-ہاسکل** | کوڈ فارمیٹنگ |
| **گھاس لگانے والا** | ڈیڈ کوڈ کا پتہ لگانا |
| **اسٹین** | جامد تجزیہ |
| **ہاسکل-لینگویج-سرور** | تشخیص، تکمیلات |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| **بنیاد** | معیاری لائبریری (مشاہدہ) |
| **متن** | متن کی موثر اقسام |
| **بائٹسٹرنگ** | بائنری ڈیٹا |
| **aeson** | JSON لائبریری |
| **کنٹینرز** | نقشے، سیٹ، ترتیب |
| **غیر ترتیب شدہ کنٹینرز** | ہیش نقشے، ہیش سیٹ |
| **ویکٹر** | موثر صفیں |
| **stm** | سافٹ ویئر ٹرانزیکشنل میموری |
| **async** | Async کمپیوٹیشنز |
| **آپٹ پارس اطلاقی** | CLI دلیل کی تجزیہ |
| **آپٹ پارس-جنرک** | خود کار طریقے سے حاصل کردہ CLI |
| **وارپ** | HTTP سرور |
| **http-کلائنٹ** | HTTP کلائنٹ |
| **نلی** | سٹریمنگ ڈیٹا |
| **پائپ** | سٹریمنگ ڈیٹا |
| **سٹریمنگ** | سٹریمنگ ڈیٹا |
| **عینک** | آپٹکس لائبریری |
| **میگا پارسیک** | پارسر کمبینیٹرز |
| **پارسیک** | پارسر کمبینیٹرز |
| **ریلوڈ** | بہتر پیش کش |
| **ریلوڈ** | متبادل پیش کش |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + HLS** | بہترین ہاسکل ایل ایس پی سپورٹ |
| **IntelliJ + IntelliJ-Haskforce** | جیٹ برینز ہاسکل |
| **Neovim + HLS** | LSP کے ساتھ ٹرمینل پر مبنی |
| **Emacs + haskell-mode** | کلاسک ہاسکل ماحول |
| **Vim + vim-haskell** | Vim انضمام |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **جامد بائنری** | GHC جامد بائنریز تیار کرتا ہے |
| **ڈوکر** | ملٹی اسٹیج بناتا ہے (ہاسکل امیج) |
| **نکس** | دوبارہ پیدا کرنے کے قابل تعمیرات |
| **Kubernetes** | آرکیسٹریشن |
| **AWS Lambda** | سرور لیس (بذریعہ ہال) |
```dockerfile
# Multi-stage Docker build
FROM haskell:9.6 AS builder
WORKDIR /app
COPY . .
RUN cabal build --only-dependencies
RUN cabal build

FROM debian:bookworm-slim
COPY --from=builder /app/dist-newstyle/build/*/myapp /usr/local/bin/
CMD ["myapp"]
```

---

## خلاصہ
ہاسکل کا ماحولیاتی نظام درستگی اور قسم کی حفاظت پر زور دینے میں منفرد ہے۔ معیاری ٹول چین یہ ہے: **GHC** بطور کمپائلر، **GHCup** تنصیب کے لیے، **Cabal** یا **Stack** تعمیرات کے لیے، **haskell-language-server** IDE سپورٹ کے لیے، **hlint** linting کے لیے، **formolu** فارمیٹنگ کے لیے، اور **tasty + QuickCheck** ٹیسٹنگ کے لیے۔ کلیدی لائبریریوں میں JSON کے لیے **aeson**، سٹرنگز کے لیے **text**، ٹائپ سیف APIs کے لیے **نوکر**، آپٹکس کے لیے **لینس**، اور کنکرنسی کے لیے **stm** شامل ہیں۔ کمپائلرز، فنانشل سسٹمز، کنکرنٹ سسٹمز، اور کہیں بھی درستگی سب سے اہم ہے۔ سیکھنے کا منحنی خطوط ہے، لیکن ادائیگی سافٹ ویئر ہے جو تعمیر کے ذریعہ صحیح طریقے سے کام کرتا ہے۔