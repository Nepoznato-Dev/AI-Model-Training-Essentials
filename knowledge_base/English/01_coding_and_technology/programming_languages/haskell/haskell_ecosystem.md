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
# Haskell — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Haskell ecosystem.

---

## Toolchain

| Tool | Purpose |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (the compiler) |
| **GHCup** | Haskell toolchain installer |
| **Cabal** | Build system and package format |
| **Stack** | Reproducible build tool |
| **cabal-install** | Package manager |
| **haskell-language-server (HLS)** | LSP server |
| **ghcid** | Fast compile feedback |
| **fourmolu** | Code formatter |
| **ormolu** | Code formatter |
| **hlint** | Linter / suggestions |

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

## Package Management

| Tool | Purpose |
|------|---------|
| **Hackage** | Central package repository (15,000+ packages) |
| **Stackage** | Curated, compatible package sets |
| **Cabal** | Package format and build tool |
| **Stack** | Reproducible builds (LTS snapshots) |

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

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **Servant** | Type-level | Type-safe APIs |
| **Yesod** | Full-stack | Type-safe web apps |
| **Scotty** | Lightweight | Simple APIs (Sinatra-like) |
| **Spock** | Lightweight | Web apps |
| **IHP** | Batteries-included | Rails-like, Haskell |
| **Miso** | Frontend | Elm-like frontend |

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

## Database

| Technology | Type |
|------------|------|
| **persistent** | ORM (Yesod ecosystem) |
| **hasql** | PostgreSQL (high-performance) |
| **postgresql-simple** | PostgreSQL (simple) |
| **beam** | Type-safe SQL |
| **esqueleto** | Type-safe ESQL (on persistent) |
| **hedis** | Redis client |
| **mongoDB** | MongoDB driver |

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

## Testing

| Framework | Purpose |
|-----------|---------|
| **HUnit** | Unit testing (xUnit-style) |
| **tasty** | Test framework (composable) |
| **tasty-hunit** | HUnit integration for tasty |
| **tasty-quickcheck** | Property-based testing |
| **QuickCheck** | Property-based testing |
| **hedgehog** | Property-based (modern) |
| **hspec** | BDD-style testing |
| **doctest** | Test examples in Haddock |
| **tasty-discover** | Auto-discover tests |

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

## Code Quality

| Tool | Purpose |
|------|---------|
| **hlint** | Suggestions and linting |
| **fourmolu / ormolu** | Code formatting |
| **stylish-haskell** | Code formatting |
| **weeder** | Dead code detection |
| **stan** | Static analysis |
| **haskell-language-server** | Diagnostics, completions |

```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Key Libraries

| Library | Purpose |
|---------|---------|
| **base** | Standard library (Prelude) |
| **text** | Efficient text types |
| **bytestring** | Binary data |
| **aeson** | JSON library |
| **containers** | Maps, sets, sequences |
| **unordered-containers** | Hash maps, hash sets |
| **vector** | Efficient arrays |
| **stm** | Software transactional memory |
| **async** | Async computations |
| **optparse-applicative** | CLI argument parsing |
| **optparse-generic** | Auto-derived CLI |
| **warp** | HTTP server |
| **http-client** | HTTP client |
| **conduit** | Streaming data |
| **pipes** | Streaming data |
| **streaming** | Streaming data |
| **lens** | Optics library |
| **megaparsec** | Parser combinators |
| **parsec** | Parser combinators |
| **relude** | Better Prelude |
| **relude** | Alternative Prelude |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + HLS** | Best Haskell LSP support |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Terminal-based with LSP |
| **Emacs + haskell-mode** | Classic Haskell environment |
| **Vim + vim-haskell** | Vim integration |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Static binary** | GHC produces static binaries |
| **Docker** | Multi-stage builds (haskell image) |
| **Nix** | Reproducible builds |
| **Kubernetes** | Orchestration |
| **AWS Lambda** | Serverless (via hal) |

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

## Summary

Haskell's ecosystem is unique in its emphasis on correctness and type safety. The standard toolchain is: **GHC** as compiler, **GHCup** for installation, **Cabal** or **Stack** for builds, **haskell-language-server** for IDE support, **hlint** for linting, **fourmolu** for formatting, and **tasty + QuickCheck** for testing. Key libraries include **aeson** for JSON, **text** for strings, **servant** for type-safe APIs, **lens** for optics, and **stm** for concurrency. Haskell excels at compilers, financial systems, concurrent systems, and anywhere correctness is paramount. The learning curve is steep, but the payoff is software that works correctly by construction.
