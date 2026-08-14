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

# Haskell — 生態系與工具指南
本指南涵蓋了 Haskell 生態系統中的基本工具、框架和基礎設施。
---

## 工具鏈
|工具|目的|
|------|---------|
| **GHC** | Glasgow Haskell Compiler（編譯者）|
| **GHCup** | Haskell 工具鏈安裝程式 |
| **陰謀集團** |建置系統與包格式|
| **堆疊** |可複製的建置工具 |
| **陰謀集團安裝** |套件管理器 |
| **haskell 語言伺服器 (HLS)** | LSP伺服器|
| **ghcid** |快速編譯回饋|
| **弗莫魯** |程式碼格式化程式|
| **奧莫魯** |程式碼格式化程式|
| **林特** |短絨/建議 |
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

## 套件管理
|工具|目的|
|------|---------|
| **駭客攻擊** |中央套件儲存庫（15,000+ 個套件）|
| **堆疊** |精心策劃的兼容套件 |
| **陰謀集團** |包格式與建構工具 |
| **堆疊** |可重現的建置（LTS 快照）|
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **僕人** |類型等級 |類型安全的 API |
| **是的** |全端|型別安全的網路應用程式 |
| **斯科蒂** |輕量化|簡單的 API（類似 Sinatra）|
| **斯波克** |輕量化|網路應用程式 |
| **國際水文計畫** |含電池 |類似 Rails，Haskell |
| **味噌** |前端 |類似榆樹的前端 |
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

## 資料庫
|技術 |類型 |
|------------|------|
| **持續** | ORM（Yesod 生態系）|
| **hasql** | PostgreSQL（高性能）|
| **postgresql-簡單** | PostgreSQL（簡單）|
| **梁** |類型安全的 SQL |
| **esqueleto** |類型安全的 ESQL（持久性）|
| **赫迪斯** | Redis 客戶端 |
| **mongoDB** | MongoDB 驅動程式 |
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

## 測試
|框架|目的|
|------------|---------|
| **HUnit** |單元測試（xUnit 風格）|
| **美味** |測試框架（可組合）|
| **美味的單位** | HUnit 整合帶來美味 |
| **美味-快速檢查** |基於屬性的測試 |
| **快速檢查** |基於屬性的測試 |
| **刺蝟** |以財產為基礎（現代）|
| **hspec** | BDD 式測試 |
| **文檔測試** | Haddock 中的測試範例 |
| **美味發現** |自動發現測試 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **林特** |建議與檢查 |
| **弗爾莫魯 / 奧爾莫魯** |代碼格式化 |
| **時尚的哈斯克爾** |程式碼格式化 |
| **除草機** |死代碼檢測 |
| **史丹** |靜態分析|
| **haskell-語言伺服器** |診斷、完成 |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **基地** |標準庫（前奏）|
| **文字** |高效率的文字類型 |
| **位元組字串** |二進位資料|
| **艾森** | JSON 庫 |
| **貨櫃** |地圖、集合、序列 |
| **無序容器** |雜湊圖、雜湊集|
| **向量** |高效率陣列 |
| **stm** |軟體事務記憶體|
| **非同步** |非同步計算 |
| **optparse-applicative** | CLI 參數解析 |
| **optparse-通用** |自動派生的 CLI |
| **扭曲** | HTTP 伺服器 |
| **http 用戶端** | HTTP 客戶端 |
| **導管** |串流資料 |
| **管道** |串流資料 |
| **串流媒體** |串流資料 |
| **鏡頭** |光學圖書館 |
| **兆秒差距** |解析器組合器 |
| **秒差距** |解析器組合器 |
| **拒絕** |更好的前奏 |
| **拒絕** |另類前奏 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS 程式碼 + HLS** |最佳 Haskell LSP 支援 |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell | JetBrains 哈斯克爾
| **Neovim + HLS** |基於終端的LSP |
| **Emacs + haskell 模式** |經典Haskell環境|
| **Vim + vim-haskell** | Vim 整合 |
---

## 部署
|方法|筆記|
|--------|--------|
| **靜態二進位** | GHC 產生靜態二進位檔案 |
| **碼頭工人** |多階段建造（haskell 圖像）|
| **尼克斯** |可重複的構建 |
| **Kubernetes** |編排|
| **AWS Lambda** |無伺服器（透過 hal）|
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

＃＃ 概括
Haskell 的生態系統的獨特之處在於它強調正確性和類型安全。標準工具鍊是：**GHC** 作為編譯器，**GHCup** 用於安裝，**Cabal** 或 **Stack** 用於構建，**haskell-language-server** 用於 IDE 支持，**hlint** 用於 linting，**fourmolu** 用於格式化，以及 **tasty + QuickCheck** 用於測試。主要庫包括用於 JSON 的 **aeson**、用於字串的 **text**、用於類型安全 API 的 **servant**、用於光學的 **lens** 以及用於並發的 **stm**。 Haskell 擅長編譯器、金融系統、並發系統以及任何要求正確性的系統。學習曲線很陡峭，但回報是透過建立可以正確運行的軟體。