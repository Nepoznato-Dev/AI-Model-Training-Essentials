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
# हास्केल - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका हास्केल पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करती है।
---

## टूलचेन
| उपकरण | उद्देश्य |
|------|---------|
| **जीएचसी** | ग्लासगो हास्केल कंपाइलर (कंपाइलर) |
| **जीएचकप** | हास्केल टूलचेन इंस्टॉलर |
| **कैबल** | सिस्टम और पैकेज प्रारूप बनाएं |
| **स्टैक** | प्रतिलिपि प्रस्तुत करने योग्य निर्माण उपकरण |
| **कैबल-इंस्टॉल** | पैकेज मैनेजर |
| **हैस्केल-भाषा-सर्वर (एचएलएस)** | एलएसपी सर्वर |
| **ghcid** | तेजी से संकलन प्रतिक्रिया |
| **फोरमोलू** | कोड फ़ॉर्मेटर |
| **ओरमोलू** | कोड फ़ॉर्मेटर |
| **ह्लिंट** | लिंटर/सुझाव |
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

## पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **हैकेज** | केंद्रीय पैकेज भंडार (15,000+ पैकेज) |
| **स्टैकेज** | क्यूरेटेड, संगत पैकेज सेट |
| **कैबल** | पैकेज प्रारूप और निर्माण उपकरण |
| **स्टैक** | प्रतिलिपि प्रस्तुत करने योग्य बिल्ड (एलटीएस स्नैपशॉट) |
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

## वेब फ्रेमवर्क
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **नौकर** | प्रकार-स्तर | टाइप-सुरक्षित एपीआई |
| **यसोद** | फुल-स्टैक | टाइप-सुरक्षित वेब ऐप्स |
| **स्कॉटी** | हल्का वजन | सरल एपीआई (सिनात्रा-जैसी) |
| **स्पॉक** | हल्का वजन | वेब ऐप्स |
| **आईएचपी** | बैटरी-शामिल | रेल की तरह, हास्केल |
| **मिसो** | अग्रभाग | एल्म जैसा अग्रभाग |
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

## डेटाबेस
| प्रौद्योगिकी | प्रकार |
|------|------|
| **लगातार** | ओआरएम (यसोड इकोसिस्टम) |
| **हैस्क्ल** | PostgreSQL (उच्च-प्रदर्शन) |
| **पोस्टग्रेस्क्ल-सिंपल** | PostgreSQL (सरल) |
| **बीम** | टाइप-सुरक्षित एसक्यूएल |
| **एस्क्वेलेटो** | टाइप-सुरक्षित ESQL (लगातार पर) |
| **हेडिस** | रेडिस क्लाइंट |
| **mongoDB** | MongoDB ड्राइवर |
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

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **हयूनिट** | यूनिट परीक्षण (xUnit-शैली) |
| **स्वादिष्ट** | टेस्ट फ्रेमवर्क (रचनात्मक) |
| **स्वादिष्ट-हनिट** | स्वादिष्ट के लिए HUnit एकीकरण |
| **स्वादिष्ट-क्विकचेक** | संपत्ति आधारित परीक्षण |
| **त्वरित जांच** | संपत्ति आधारित परीक्षण |
| **हेजहोग** | संपत्ति आधारित (आधुनिक) |
| **hspec** | बीडीडी-शैली परीक्षण |
| **सर्वोत्तम** | हैडॉक में परीक्षण उदाहरण |
| **स्वादिष्ट-खोज** | स्वतः-खोज परीक्षण |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **ह्लिंट** | सुझाव और लाइनिंग |
| **फोरमोलू/ओरमोलू** | कोड फ़ॉर्मेटिंग |
| **स्टाइलिश-हास्केल** | कोड फ़ॉर्मेटिंग |
| **खरपतवार** | डेड कोड का पता लगाना |
| **स्टेन** | स्थैतिक विश्लेषण |
| **हैस्केल-भाषा-सर्वर** | निदान, पूर्णताएँ |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **आधार** | मानक पुस्तकालय (प्रस्तावना) |
| **पाठ** | कुशल पाठ प्रकार |
| **बाइटस्ट्रिंग** | बाइनरी डेटा |
| **ऐसन** | JSON लाइब्रेरी |
| **कंटेनर** | मानचित्र, सेट, क्रम |
| **अनियंत्रित-कंटेनर** | हैश मैप, हैश सेट |
| **वेक्टर** | कुशल सरणियाँ |
| **एसटीएम** | सॉफ्टवेयर ट्रांसेक्शनल मेमोरी |
| **async** | एसिंक गणना |
| **optparse-आवेदक** | सीएलआई तर्क विश्लेषण |
| **ऑप्टपर्स-जेनेरिक** | स्वतः व्युत्पन्न सीएलआई |
| **ताना** | HTTP सर्वर |
| **http-क्लाइंट** | HTTP क्लाइंट |
| **नाली** | स्ट्रीमिंग डेटा |
| **पाइप** | स्ट्रीमिंग डेटा |
| **स्ट्रीमिंग** | स्ट्रीमिंग डेटा |
| **लेंस** | प्रकाशिकी पुस्तकालय |
| **मेगापारसेक** | पार्सर कॉम्बिनेटर |
| **पारसेक** | पार्सर कॉम्बिनेटर |
| **विरोध** | बेहतर प्रस्तावना |
| **विरोध** | वैकल्पिक प्रस्तावना |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **वीएस कोड + एचएलएस** | सर्वश्रेष्ठ हास्केल एलएसपी समर्थन |
| **इंटेलिजे + इंटेलीजे-हास्कफोर्स** | जेटब्रेन्स हास्केल |
| **नियोविम + एचएलएस** | एलएसपी के साथ टर्मिनल-आधारित |
| **Emacs + haskell-mode** | क्लासिक हास्केल वातावरण |
| **विम + विम-हास्केल** | विम एकीकरण |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **स्टेटिक बाइनरी** | जीएचसी स्थैतिक बायनेरिज़ उत्पन्न करता है |
| **डॉकर** | मल्टी-स्टेज बिल्ड (हैस्केल इमेज) |
| **निक्स** | प्रतिलिपि प्रस्तुत करने योग्य निर्माण |
| **कुबेरनेट्स** | आर्केस्ट्रा |
| **एडब्ल्यूएस लैम्ब्डा** | सर्वर रहित (एचएएल के माध्यम से) |
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

## सारांश
हास्केल का पारिस्थितिकी तंत्र शुद्धता और प्रकार की सुरक्षा पर जोर देने में अद्वितीय है। मानक टूलचेन है: कंपाइलर के रूप में **जीएचसी**, इंस्टॉलेशन के लिए **जीएचसीअप**, बिल्ड के लिए **कैबल** या **स्टैक**, आईडीई सपोर्ट के लिए **हैस्केल-लैंग्वेज-सर्वर**, लिंटिंग के लिए **एचलिंट**, फ़ॉर्मेटिंग के लिए **फोरमोलु** और परीक्षण के लिए **टेस्टी + क्विकचेक**। प्रमुख पुस्तकालयों में JSON के लिए **एसन**, स्ट्रिंग्स के लिए **टेक्स्ट**, टाइप-सुरक्षित एपीआई के लिए **सर्वेंट**, ऑप्टिक्स के लिए **लेंस** और समवर्ती के लिए **stm** शामिल हैं। हास्केल कंपाइलरों, वित्तीय प्रणालियों, समवर्ती प्रणालियों में उत्कृष्टता प्राप्त करता है, और कहीं भी शुद्धता सर्वोपरि है। सीखने की अवस्था कठिन है, लेकिन इसका लाभ वह सॉफ़्टवेयर है जो निर्माण द्वारा सही ढंग से काम करता है।