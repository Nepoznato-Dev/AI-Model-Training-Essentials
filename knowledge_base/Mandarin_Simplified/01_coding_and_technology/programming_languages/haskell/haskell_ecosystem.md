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

# Haskell — 生态系统和工具指南
本指南涵盖了 Haskell 生态系统中的基本工具、框架和基础设施。
---

## 工具链
|工具|目的|
|------|---------|
| **GHC** | Glasgow Haskell Compiler（编译器）|
| **GHCup** | Haskell 工具链安装程序 |
| **阴谋集团** |构建系统和包格式|
| **堆栈** |可复制的构建工具 |
| **阴谋集团安装** |包管理器 |
| **haskell 语言服务器 (HLS)** | LSP服务器|
| **ghcid** |快速编译反馈|
| **弗莫鲁** |代码格式化程序|
| **奥尔莫鲁** |代码格式化程序|
| **林特** |短绒/建议 |
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

## 包管理
|工具|目的|
|------|---------|
| **黑客攻击** |中央包存储库（15,000+ 个包）|
| **堆栈** |精心策划的兼容套件 |
| **阴谋集团** |包格式和构建工具 |
| **堆栈** |可重现的构建（LTS 快照）|
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

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **仆人** |类型级别 |类型安全的 API |
| **是的** |全栈|类型安全的网络应用程序 |
| **斯科蒂** |轻量化|简单的 API（类似 Sinatra）|
| **斯波克** |轻量化|网络应用程序 |
| **国际水文计划** |含电池 |类似 Rails，Haskell |
| **味噌** |前端 |类似榆树的前端 |
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **持续** | ORM（Yesod 生态系统）|
| **hasql** | PostgreSQL（高性能）|
| **postgresql-简单** | PostgreSQL（简单）|
| **梁** |类型安全的 SQL |
| **esqueleto** |类型安全的 ESQL（持久性）|
| **赫迪斯** | Redis 客户端 |
| **mongoDB** | MongoDB 驱动程序 |
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

## 测试
|框架|目的|
|------------|---------|
| **HUnit** |单元测试（xUnit 风格）|
| **美味** |测试框架（可组合）|
| **美味的单位** | HUnit 集成带来美味 |
| **美味-快速检查** |基于属性的测试 |
| **快速检查** |基于属性的测试 |
| **刺猬** |以财产为基础（现代）|
| **hspec** | BDD 式测试 |
| **文档测试** | Haddock 中的测试示例 |
| **美味发现** |自动发现测试 |
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

## 代码质量
|工具|目的|
|------|---------|
| **林特** |建议和检查 |
| **弗尔莫鲁/奥尔莫鲁** |代码格式化 |
| **时尚的哈斯克尔** |代码格式化 |
| **除草机** |死代码检测 |
| **斯坦** |静态分析|
| **haskell-语言服务器** |诊断、完成 |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## 关键库
|图书馆 |目的|
|---------|---------|
| **基地** |标准库（前奏）|
| **文字** |高效的文本类型 |
| **字节串** |二进制数据|
| **艾森** | JSON 库 |
| **集装箱** |地图、集合、序列 |
| **无序容器** |哈希图、哈希集|
| **矢量** |高效阵列 |
| **stm** |软件事务内存|
| **异步** |异步计算 |
| **optparse-applicative** | CLI 参数解析 |
| **optparse-通用** |自动派生的 CLI |
| **扭曲** | HTTP 服务器 |
| **http 客户端** | HTTP 客户端 |
| **导管** |流数据|
| **管道** |流数据 |
| **流媒体** |流数据 |
| **镜头** |光学图书馆 |
| **兆秒差距** |解析器组合器 |
| **秒差距** |解析器组合器 |
| **拒绝** |更好的前奏 |
| **拒绝** |另类前奏 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS 代码 + HLS** |最佳 Haskell LSP 支持 |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell | JetBrains 哈斯克尔
| **Neovim + HLS** |基于终端的LSP |
| **Emacs + haskell 模式** |经典Haskell环境|
| **Vim + vim-haskell** | Vim 集成 |
---

## 部署
|方法|笔记|
|--------|--------|
| **静态二进制** | GHC 生成静态二进制文件 |
| **码头工人** |多阶段构建（haskell 图像）|
| **尼克斯** |可重复的构建 |
| **Kubernetes** |编排|
| **AWS Lambda** |无服务器（通过 hal）|
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
Haskell 的生态系统的独特之处在于它强调正确性和类型安全。标准工具链是：**GHC** 作为编译器，**GHCup** 用于安装，**Cabal** 或 **Stack** 用于构建，**haskell-language-server** 用于 IDE 支持，**hlint** 用于 linting，**fourmolu** 用于格式化，以及 **tasty + QuickCheck** 用于测试。主要库包括用于 JSON 的 **aeson**、用于字符串的 **text**、用于类型安全 API 的 **servant**、用于光学的 **lens** 以及用于并发的 **stm**。 Haskell 擅长编译器、金融系统、并发系统以及任何要求正确性的系统。学习曲线很陡峭，但回报是通过构建可以正确运行的软件。