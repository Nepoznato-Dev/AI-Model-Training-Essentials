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
# হাস্কেল — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি হাসকেল ইকোসিস্টেমের প্রয়োজনীয় টুলস, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## টুলচেইন
| টুল | উদ্দেশ্য |
|------|---------|
| **GHC** | গ্লাসগো হাসকেল কম্পাইলার (কম্পাইলার) |
| **GHCup** | Haskell টুলচেইন ইনস্টলার |
| **ক্যাবল** | সিস্টেম এবং প্যাকেজ বিন্যাস তৈরি করুন |
| **স্ট্যাক** | প্রজননযোগ্য বিল্ড টুল |
| **ক্যাবল-ইনস্টল** | প্যাকেজ ম্যানেজার |
| **হাস্কেল-ভাষা-সার্ভার (HLS)** | LSP সার্ভার |
| **ghcid** | দ্রুত কম্পাইল ফিডব্যাক |
| **চারমোলু** | কোড ফরম্যাটার |
| **অরমোলু** | কোড ফরম্যাটার |
| **হলিন্ট** | লিন্টার / পরামর্শ |
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

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **হ্যাকেজ** | কেন্দ্রীয় প্যাকেজ সংগ্রহস্থল (15,000+ প্যাকেজ) |
| **স্ট্যাকেজ** | কিউরেটেড, সামঞ্জস্যপূর্ণ প্যাকেজ সেট |
| **ক্যাবল** | প্যাকেজ ফরম্যাট এবং বিল্ড টুল |
| **স্ট্যাক** | প্রজননযোগ্য বিল্ড (LTS স্ন্যাপশট) |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **সেবক** | টাইপ-লেভেল | টাইপ-সেফ APIs |
| **হ্যাঁ** | ফুল-স্ট্যাক | টাইপ-নিরাপদ ওয়েব অ্যাপস |
| **স্কটি** | লাইটওয়েট | সরল API (সিনাট্রা-সদৃশ) |
| **স্পক** | লাইটওয়েট | ওয়েব অ্যাপস |
| **আইএইচপি** | ব্যাটারি-অন্তর্ভুক্ত | রেলের মতো, হাসকেল |
| **মিসো** | ফ্রন্টেন্ড | এলমের মত ফ্রন্টএন্ড |
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

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **অচল** | ওআরএম (ইয়েসোড ইকোসিস্টেম) |
| **hasql** | PostgreSQL (উচ্চ কর্মক্ষমতা) |
| **postgresql-সহজ** | PostgreSQL (সহজ) |
| **বিম** | টাইপ-নিরাপদ SQL |
| **এসকেলেটো** | টাইপ-নিরাপদ ESQL (অস্থায়ী) |
| **হেদিস** | Redis ক্লায়েন্ট |
| **মঙ্গোডিবি** | MongoDB ড্রাইভার |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **HUnit** | ইউনিট পরীক্ষা (xUnit-style) |
| **সুস্বাদু** | টেস্ট ফ্রেমওয়ার্ক (কম্পোজযোগ্য) |
| **সুস্বাদু-হুনিত** | সুস্বাদু জন্য HUnit ইন্টিগ্রেশন |
| **সুস্বাদু-দ্রুত চেক** | সম্পত্তি ভিত্তিক পরীক্ষা |
| **দ্রুত চেক** | সম্পত্তি ভিত্তিক পরীক্ষা |
| **হেজহগ** | সম্পত্তি ভিত্তিক (আধুনিক) |
| **hspec** | বিডিডি-স্টাইল পরীক্ষা |
| **ডক্টেস্ট** | হ্যাডক পরীক্ষা উদাহরণ |
| **সুস্বাদু-আবিষ্কার** | স্বয়ংক্রিয় আবিষ্কার পরীক্ষা |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **হলিন্ট** | পরামর্শ এবং linting |
| **ফোরমোলু / অরমোলু** | কোড ফরম্যাটিং |
| **আড়ম্বরপূর্ণ-হাস্কেল** | কোড ফরম্যাটিং |
| **আগাছা* | মৃত কোড সনাক্তকরণ |
| **স্ট্যান** | স্ট্যাটিক বিশ্লেষণ |
| **হাস্কেল-ভাষা-সার্ভার** | ডায়াগনস্টিকস, সমাপ্তি |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **ভিত্তি** | স্ট্যান্ডার্ড লাইব্রেরি (প্রিলিউড) |
| **পাঠ্য** | দক্ষ পাঠ্য প্রকার |
| **বাইটেস্ট্রিং** | বাইনারি ডেটা |
| **এসন** | JSON লাইব্রেরি |
| **পাত্র** | মানচিত্র, সেট, ক্রম |
| **অক্রমবিহীন পাত্র** | হ্যাশ মানচিত্র, হ্যাশ সেট |
| **ভেক্টর** | দক্ষ অ্যারে |
| **stm** | সফ্টওয়্যার লেনদেন মেমরি |
| **অসিঙ্ক** | Async গণনা |
| **অপ্টপার্স-প্রযোজ্য** | CLI যুক্তি পার্সিং |
| **অপ্টপার্স-জেনারিক** | স্বয়ংক্রিয়ভাবে প্রাপ্ত CLI |
| **ওয়ার্প** | HTTP সার্ভার |
| **http-ক্লায়েন্ট** | HTTP ক্লায়েন্ট |
| **নালী** | স্ট্রিমিং ডেটা |
| **পাইপ** | স্ট্রিমিং ডেটা |
| **স্ট্রিমিং** | স্ট্রিমিং ডেটা |
| **লেন্স** | অপটিক্স লাইব্রেরি |
| **মেগাপারসেক** | পার্সার কম্বিনেটর |
| **পার্সেক** | পার্সার কম্বিনেটর |
| **অবস্থান** | ভাল ভূমিকা |
| **অবস্থান** | বিকল্প ভূমিকা |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **VS কোড + HLS** | সেরা Haskell LSP সমর্থন |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **নিওভিম + এইচএলএস** | LSP সহ টার্মিনাল-ভিত্তিক |
| **Emacs + haskell-mode** | ক্লাসিক হাসকেল পরিবেশ |
| **ভিম + ভিম-হাস্কেল** | ভিম ইন্টিগ্রেশন |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **স্ট্যাটিক বাইনারি** | জিএইচসি স্ট্যাটিক বাইনারি তৈরি করে |
| **ডকার** | মাল্টি-স্টেজ বিল্ড (হাস্কেল ইমেজ) |
| **নিক্স** | প্রজননযোগ্য বিল্ড |
| **কুবারনেটস** | অর্কেস্ট্রেশন |
| **AWS Lambda** | সার্ভারহীন (হ্যাল মাধ্যমে) |
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

## সারাংশ
হাস্কেলের ইকোসিস্টেমটি সঠিকতা এবং টাইপ নিরাপত্তার উপর জোর দেওয়ার ক্ষেত্রে অনন্য। স্ট্যান্ডার্ড টুলচেন হল: কম্পাইলার হিসেবে **GHC**, ইনস্টলেশনের জন্য **GHCup**, বিল্ডের জন্য **ক্যাবল** বা **স্ট্যাক**, IDE সমর্থনের জন্য **হ্যাস্কেল-ভাষা-সার্ভার**, লিন্টিংয়ের জন্য **হলিন্ট**, বিন্যাসের জন্য **ফোরমোলু** এবং পরীক্ষার জন্য **সুস্বাদু + দ্রুত চেক**। মূল লাইব্রেরির মধ্যে রয়েছে JSON-এর জন্য **aeson**, স্ট্রিং-এর জন্য **টেক্সট**, টাইপ-সেফ API-এর জন্য **সার্ভেন্ট**, অপটিক্সের জন্য **লেন্স**, এবং কনকারেন্সির জন্য **stm**। হাস্কেল কম্পাইলার, আর্থিক ব্যবস্থা, সমসাময়িক সিস্টেম এবং যে কোনও জায়গায় শুদ্ধতা সর্বোত্তম। শেখার বক্ররেখা খাড়া, কিন্তু অর্থপ্রদান হল সফ্টওয়্যার যা নির্মাণের মাধ্যমে সঠিকভাবে কাজ করে।