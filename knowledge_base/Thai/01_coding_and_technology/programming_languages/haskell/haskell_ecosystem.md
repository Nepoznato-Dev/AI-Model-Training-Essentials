---
# Metadata
title: "Haskell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Haskell ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Haskell - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่สำคัญในระบบนิเวศของ Haskell
---

## ห่วงโซ่เครื่องมือ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (คอมไพเลอร์) |
| **จีเอชคัพ** | ตัวติดตั้ง Toolchain Haskell |
| **คาบาล** | สร้างระบบและรูปแบบแพ็คเกจ |
| **กองซ้อน** | เครื่องมือสร้างที่ทำซ้ำได้ |
| **ติดตั้ง cabal** | ผู้จัดการแพ็คเกจ |
| **เซิร์ฟเวอร์ภาษา haskell (HLS)** | เซิร์ฟเวอร์ LSP |
| **ghcid** | ข้อเสนอแนะการรวบรวมอย่างรวดเร็ว |
| **โฟร์โมลู** | ตัวจัดรูปแบบโค้ด |
| **ออร์โมลู** | ตัวจัดรูปแบบโค้ด |
| **คำราม** | Linter / ข้อเสนอแนะ |
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

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **แฮ็ค** | พื้นที่เก็บข้อมูลแพ็คเกจส่วนกลาง (15,000+ แพ็คเกจ) |
| **กองซ้อน** | ชุดแพ็คเกจที่ได้รับการดูแลจัดการและเข้ากันได้
| **คาบาล** | รูปแบบแพ็คเกจและเครื่องมือสร้าง |
| **กองซ้อน** | บิลด์ที่ทำซ้ำได้ (สแนปช็อต LTS) |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **คนรับใช้** | ระดับประเภท | API ที่ปลอดภัยสำหรับประเภท |
| **เยซด** | เต็มกอง | เว็บแอปที่ปลอดภัยต่อการพิมพ์ |
| **สก็อตตี้** | น้ำหนักเบา | API แบบง่าย (คล้าย Sinatra) |
| **สป็อค** | น้ำหนักเบา | เว็บแอป |
| **IHP** | รวมแบตเตอรี่ | คล้ายราง Haskell |
| **มิโซะ** | ส่วนหน้า | ส่วนหน้าเหมือนเอล์ม |
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

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **ถาวร** | ORM (ระบบนิเวศเยซอด) |
| **hasql** | PostgreSQL (ประสิทธิภาพสูง) |
| **postgresql-ง่าย** | PostgreSQL (แบบง่าย) |
| **คาน** | SQL แบบปลอดภัย |
| **ผลงาน** | ESQL แบบปลอดภัย (แบบถาวร) |
| **เฮดิส** | ลูกค้า Redis |
| **mongoDB** | ไดรเวอร์ MongoDB |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **หน่วย** | การทดสอบหน่วย (สไตล์ xUnit) |
| **อร่อย** | กรอบการทดสอบ (ประกอบได้) |
| **ล่าอร่อย** | บูรณาการ HUnit เพื่อความอร่อย |
| **อร่อย-เช็คด่วน** | การทดสอบตามคุณสมบัติ |
| **ตรวจสอบด่วน** | การทดสอบตามคุณสมบัติ |
| **เม่น** | ตามคุณสมบัติ (สมัยใหม่) |
| **สเป็ก** | การทดสอบแบบ BDD |
| **หมอ** | ตัวอย่างการทดสอบใน Haddock |
| **ค้นพบความอร่อย** | การทดสอบการค้นหาอัตโนมัติ |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **คำราม** | ข้อแนะนำและขุย |
| **fourmolu / ormolu** | การจัดรูปแบบโค้ด |
| **มีสไตล์-haskell** | การจัดรูปแบบโค้ด |
| **กำจัดวัชพืช** | การตรวจจับรหัสที่เสีย |
| **สแตน** | การวิเคราะห์แบบคงที่ |
| **เซิร์ฟเวอร์ภาษา haskell** | การวินิจฉัย ความสำเร็จ |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **ฐาน** | ไลบรารีมาตรฐาน (โหมโรง) |
| **ข้อความ** | ประเภทข้อความที่มีประสิทธิภาพ |
| **สตริงไบต์** | ข้อมูลไบนารี |
| **อีซัน** | ไลบรารี JSON |
| **ตู้คอนเทนเนอร์** | แผนที่ ชุด ลำดับ |
| **ตู้คอนเทนเนอร์ไม่เรียงลำดับ** | แผนที่แฮช ชุดแฮช |
| **เวกเตอร์** | อาร์เรย์ที่มีประสิทธิภาพ |
| **stm** | ซอฟต์แวร์หน่วยความจำทรานแซคชัน |
| **อะซิงโครนัส** | การคำนวณแบบอะซิงก์ |
| **optparse-ประยุกต์** | การแยกวิเคราะห์อาร์กิวเมนต์ CLI |
| **optparse-ทั่วไป** | CLI ที่ได้รับอัตโนมัติ |
| **วาร์ป** | เซิร์ฟเวอร์ HTTP |
| **http-ไคลเอนต์** | ไคลเอ็นต์ HTTP |
| **ท่อร้อยสาย** | สตรีมมิ่งข้อมูล |
| **ท่อ** | สตรีมมิ่งข้อมูล |
| **สตรีมมิ่ง** | สตรีมมิ่งข้อมูล |
| **เลนส์** | ห้องสมุดทัศนศาสตร์ |
| **เมกะพาร์เซก** | ตัวรวมพาร์เซอร์ |
| **พาร์เซก** | ตัวรวมพาร์เซอร์ |
| **เรลูด** | โหมโรงดีกว่า |
| **เรลูด** | อัลเทอร์เนทีฟโหมโรง |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **รหัส VS + HLS** | การสนับสนุน Haskell LSP ที่ดีที่สุด |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **นีโอวิม + HLS** | เทอร์มินัลที่ใช้ LSP |
| **Emacs + โหมด haskell** | สภาพแวดล้อม Haskell แบบคลาสสิก |
| **Vim + vim-haskell** | การรวมเป็นกลุ่ม |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ไบนารีแบบคงที่** | GHC สร้างไบนารีแบบคงที่ |
| **นักเทียบท่า** | การสร้างแบบหลายขั้นตอน (อิมเมจ haskell) |
| **ห้าม** | บิลด์ที่ทำซ้ำได้ |
| **Kubernetes** | การเรียบเรียง |
| **AWS แลมบ์ดา** | ไร้เซิร์ฟเวอร์ (ผ่าน hal) |
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

## สรุป
ระบบนิเวศของ Haskell มีเอกลักษณ์เฉพาะตัวโดยเน้นความถูกต้องและความปลอดภัยของประเภท Toolchain มาตรฐานคือ: **GHC** ในฐานะคอมไพเลอร์, **GHCup** สำหรับการติดตั้ง, **Cabal** หรือ **Stack** สำหรับบิลด์, **haskell-Language-server** สำหรับการรองรับ IDE, **hlint** สำหรับ Linting, **fourmolu** สำหรับการจัดรูปแบบ และ **tasty + QuickCheck** สำหรับการทดสอบ ไลบรารีหลักประกอบด้วย **aeson** สำหรับ JSON, **text** สำหรับสตริง, **servant** สำหรับ API ที่ปลอดภัยสำหรับประเภท, **lens** สำหรับ optics และ **stm** สำหรับการทำงานพร้อมกัน Haskell เชี่ยวชาญด้านคอมไพเลอร์ ระบบการเงิน ระบบที่ทำงานพร้อมกัน และความถูกต้องเป็นสิ่งสำคัญยิ่ง เส้นโค้งการเรียนรู้นั้นสูงชัน แต่ผลตอบแทนที่ได้คือซอฟต์แวร์ที่ทำงานได้อย่างถูกต้องจากการก่อสร้าง