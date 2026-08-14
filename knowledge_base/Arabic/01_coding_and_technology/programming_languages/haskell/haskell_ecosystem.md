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
# هاسكل - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في نظام هاسكل البيئي.
---

## سلسلة الأدوات
| أداة | الغرض |
|------|---------|
| ** جي اتش سي ** | مترجم غلاسكو هاسكل (المترجم) |
| **غكوب** | مثبت سلسلة أدوات هاسكل |
| **كابال** | بناء النظام وتنسيق الحزمة |
| **كومة** | أداة بناء قابلة للتكرار |
| **تثبيت الكابال** | مدير الحزم |
| **خادم لغة هاسكل (HLS)** | خادم LSP |
| **غسيد** | تجميع سريع للملاحظات |
| **فورمولو** | منسق الكود |
| **أورمولو** | منسق الكود |
| **هلينت** | لينتر / اقتراحات |
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

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| ** الاختراق ** | مستودع الحزم المركزي (+15000 حزمة) |
| **المكدس** | مجموعات حزم منسقة ومتوافقة |
| **كابال** | تنسيق الحزمة وأداة البناء |
| **كومة** | بنيات قابلة للتكرار (لقطات LTS) |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **الخادم** | مستوى النوع | واجهات برمجة التطبيقات الآمنة من النوع |
| **يسود** | مكدس كامل | تطبيقات الويب الآمنة من النوع |
| **سكوتي** | خفيف الوزن | واجهات برمجة التطبيقات البسيطة (مثل سيناترا) |
| **سبوك** | خفيف الوزن | تطبيقات الويب |
| ** آي إتش بي ** | البطاريات متضمنة | تشبه القضبان، هاسكل |
| **ميسو** | الواجهة الأمامية | واجهة أمامية تشبه الدردار |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| **مستمر** | ORM (النظام البيئي Yesod) |
| **حاسق** | PostgreSQL (عالي الأداء) |
| **postgresql-simple** | PostgreSQL (بسيط) |
| **شعاع** | نوع SQL آمن |
| ** إسكويليتو ** | ESQL من النوع الآمن (على المستمر) |
| **هديس** | عميل ريديس |
| ** مونغو دي بي ** | برنامج تشغيل MongoDB |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **وحدة** | اختبار الوحدة (نمط xUnit) |
| **لذيذ** | إطار الاختبار (قابل للتركيب) |
| **هونيت لذيذ** | التكامل HUnit لذيذ |
| **فحص سريع لذيذ** | الاختبار على أساس الملكية |
| **فحص سريع** | الاختبار على أساس الملكية |
| **القنفذ** | الملكية (الحديثة) |
| **المواصفات** | اختبار نمط BDD |
| **دوكتيست** | أمثلة اختبارية في الحدوق |
| **اكتشاف لذيذ** | اختبارات الاكتشاف التلقائي |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **هلينت** | الاقتراحات والفحص |
| ** فورمولو / أورمولو ** | تنسيق الكود |
| **أنيقة-هاسكل** | تنسيق الكود |
| **الاعشاب** | كشف الكود الميت |
| **ستان** | التحليل الساكن |
| **خادم لغة هاسكل** | التشخيص والإكمال |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **قاعدة** | المكتبة القياسية (مقدمة) |
| **نص** | أنواع النص الفعالة |
| ** سلسلة بايت ** | البيانات الثنائية |
| **إيسون** | مكتبة جيسون |
| **حاويات** | خرائط، مجموعات، تسلسلات |
| **حاويات غير مرتبة** | خرائط التجزئة، مجموعات التجزئة |
| **ناقل** | صفائف فعالة |
| **اس تي ام** | ذاكرة المعاملات البرمجية |
| **غير متزامن** | حسابات غير متزامنة |
| **optparse-applicative** | تحليل وسيطة CLI |
| **optparse-عام** | سطر الأوامر المشتق تلقائيًا |
| **الاعوجاج** | خادم HTTP |
| **http-client** | عميل HTTP |
| **القناة** | تدفق البيانات |
| **أنابيب** | تدفق البيانات |
| **البث** | تدفق البيانات |
| **عدسة** | مكتبة البصريات |
| **ميجا فرسخ فلكي** | مجمعات المحلل اللغوي |
| **بارسيك** | مجمعات المحلل اللغوي |
| **ريلود** | مقدمة أفضل |
| **ريلود** | مقدمة بديلة |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| **رمز VS + HLS** | أفضل دعم لهاسكل LSP |
| **IntelliJ + IntelliJ-Haskforce** | جيت براينز هاسكل |
| **نيوفيم + اتش ال اس** | يعتمد على المحطة مع LSP |
| ** إيماكس + وضع هاسكل ** | بيئة هاسكل الكلاسيكية |
| ** فيم + فيم-هاسكل** | تكامل فيم |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **ثنائي ثابت** | تنتج GHC ثنائيات ثابتة |
| ** عامل الميناء ** | بناء متعدد المراحل (صورة هاسكل) |
| ** نيكس ** | بنيات قابلة للتكرار |
| **كوبرنيتس** | تنسيق |
| **AWS لامدا** | بدون خادم (عبر هال) |
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

## ملخص
يعد نظام هاسكل البيئي فريدًا من نوعه في تركيزه على الصحة وسلامة الكتابة. سلسلة الأدوات القياسية هي: **GHC** كمترجم، **GHCup** للتثبيت، **Cabal** أو **Stack** للإنشاءات، **haskell-language-server** لدعم IDE، **hlint** للفحص، **fourmolu** للتنسيق، و **tasty + QuickCheck** للاختبار. تتضمن مكتبات المفاتيح **aeson** لـ JSON، و**text** للسلاسل، و**servant** لواجهات برمجة التطبيقات الآمنة للنوع، و**lens** للبصريات، و**stm** للتزامن. تتفوق هاسكل في المترجمين، والأنظمة المالية، والأنظمة المتزامنة، وفي أي مكان تكون الصحة أمرًا بالغ الأهمية. إن منحنى التعلم شديد الانحدار، ولكن المردود هو البرمجيات التي تعمل بشكل صحيح من خلال البناء.