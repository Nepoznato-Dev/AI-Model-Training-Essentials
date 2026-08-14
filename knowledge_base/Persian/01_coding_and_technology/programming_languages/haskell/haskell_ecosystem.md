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
# Haskell - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم Haskell را پوشش می‌دهد.
---

## زنجیره ابزار
| ابزار | هدف |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (کامپایلر) |
| **GHCup** | نصب کننده زنجیره ابزار Haskell |
| **کابال** | ساخت سیستم و فرمت پکیج |
| **پشته** | ابزار ساخت قابل تکرار |
| **کابال-نصب** | مدیر بسته |
| **سرور زبان-haskell (HLS)** | سرور LSP |
| **ghcid** | بازخورد کامپایل سریع |
| **فورمولو** | فرمت کننده کد |
| **اورمولو** | فرمت کننده کد |
| **هلنت** | لینتر / پیشنهادات |
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

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **هک ** | مخزن مرکزی بسته (15000+ بسته) |
| **پشته** | مجموعه های بسته بندی شده و سازگار |
| **کابال** | قالب بسته و ابزار ساخت |
| **پشته** | ساخت های قابل تکرار (تصاویر فوری LTS) |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **خدمت** | سطح نوع | APIهای نوع ایمن |
| **Yesod** | تمام پشته | برنامه های وب ایمن تایپ |
| **اسکاتی** | سبک | APIهای ساده (شبیه سیناترا) |
| **اسپاک** | سبک | برنامه های وب |
| **IHP** | دارای باتری | ریل مانند، هاسکل |
| **میسو** | Frontend | پیشانی نارون مانند |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **مداوم** | ORM (اکوسیستم Yesod) |
| **hasql** | PostgreSQL (با کارایی بالا) |
| **postgresql-ساده** | PostgreSQL (ساده) |
| **پرتو** | نوع ایمن SQL |
| **اسکلتو** | نوع ایمن ESQL (در حالت پایدار) |
| **هدیس** | مشتری Redis |
| **mongoDB** | درایور MongoDB |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **هونیت** | تست واحد (xUnit-style) |
| **خوشمزه** | چارچوب تست (قابل ترکیب) |
| **tasty-hunit** | ادغام HUnit برای خوشمزه |
| **خوشمزه-چک سریع** | تست مبتنی بر اموال |
| **بررسی سریع** | تست مبتنی بر اموال |
| **جوجه تیغی** | املاک محور (مدرن) |
| **hspec** | تست سبک BDD |
| **دکتر** | نمونه های تست در هادوک |
| **خوشمزه-کشف** | تست های کشف خودکار |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **هلنت** | پیشنهادات و لینتینگ |
| **فورمولو / اورمولو** | قالب بندی کد |
| **شیک-هشکل** | قالب بندی کد |
| **علف هرز** | تشخیص کد مرده |
| **ستان** | تجزیه و تحلیل استاتیک |
| **سرور-زبان-haskell** | تشخیص، تکمیل |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **پایه** | کتابخانه استاندارد (پرلود) |
| **متن** | انواع متن کارآمد |
| **بای تست** | داده های باینری |
| **آسون** | کتابخانه JSON |
| **ظروف** | نقشه ها، مجموعه ها، دنباله ها |
| **بدون سفارش-ظروف** | نقشه هاش، مجموعه هش |
| **وکتور** | آرایه های کارآمد |
| **stm** | حافظه تراکنشی نرم افزار |
| **ناهمگام** | محاسبات Async |
| **optparse-applicative** | تجزیه آرگومان CLI |
| **optparse-generic** | CLI مشتق از خودکار |
| **تار** | سرور HTTP |
| **http-client** | سرویس گیرنده HTTP |
| **مجری** | جریان داده |
| **لوله** | جریان داده |
| **جریان** | جریان داده |
| **لنز** | کتابخانه اپتیک |
| **مگاپارسک** | ترکیبات تجزیه کننده |
| **پارسک** | ترکیبات تجزیه کننده |
| **رلود** | پیش درآمد بهتر |
| **رلود** | پیش درآمد جایگزین |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + HLS** | بهترین پشتیبانی Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | مبتنی بر ترمینال با LSP |
| **Emacs + haskell-mode** | محیط کلاسیک Haskell |
| **Vim + vim-haskell** | ادغام Vim |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **باینری استاتیک** | GHC باینری های ثابت تولید می کند |
| **داکر** | ساخت های چند مرحله ای (تصویر هسکل) |
| **نیکس** | ساخت های تکرار شونده |
| **Kubernetes** | ارکستراسیون |
| **AWS Lambda** | بدون سرور (از طریق hal) |
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

## خلاصه
اکوسیستم Haskell در تاکید بر صحت و ایمنی نوع منحصر به فرد است. زنجیره ابزار استاندارد عبارتند از: **GHC** به عنوان کامپایلر، **GHCup** برای نصب، **Cabal** یا **Stack** برای ساخت‌ها، **haskell-language-server** برای پشتیبانی IDE، **hlint** برای linting، **fourmolu** برای قالب‌بندی، و **tasty + QuickCheck** برای تست. کتابخانه‌های کلیدی شامل **aeson** برای JSON، **text** برای رشته‌ها، **servant** برای APIهای ایمن نوع، **lens** برای اپتیک و **stm** برای همزمانی. Haskell در کامپایلرها، سیستم های مالی، سیستم های همزمان و هر جایی که صحت در اولویت است، برتری دارد. منحنی یادگیری شیب دار است، اما بازده آن نرم افزاری است که با ساخت به درستی کار می کند.