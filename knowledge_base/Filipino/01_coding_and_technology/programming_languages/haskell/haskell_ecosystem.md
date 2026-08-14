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
# Haskell — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa Haskell ecosystem.
---

## Toolchain
| Tool | Layunin |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (ang compiler) |
| **GHCup** | Haskell toolchain installer |
| **Cabal** | Bumuo ng system at format ng package |
| **Stack** | Reproducible build tool |
| **cabal-install** | Tagapamahala ng package |
| **haskell-language-server (HLS)** | LSP server |
| **ghcid** | Mabilis na mag-compile ng feedback |
| **formolu** | Taga-format ng code |
| **ormolu** | Taga-format ng code |
| **hlint** | Linter / mungkahi |
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

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **Hackage** | Central package repository (15,000+ packages) |
| **Stackage** | Na-curate, compatible na mga set ng package |
| **Cabal** | Format ng package at tool sa pagbuo |
| **Stack** | Reproducible build (LTS snapshots) |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Lingkod** | Antas ng uri | Mga API na ligtas sa uri |
| **Yesod** | Full-stack | Uri-safe na web apps |
| **Scotty** | Magaan | Mga Simpleng API (tulad ng Sinatra) |
| **Spock** | Magaan | Mga web app |
| **IHP** | Mga baterya-kasama | Parang riles, Haskell |
| **Miso** | Frontend | mala-Elm na frontend |
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
| Teknolohiya | Uri |
|------------|------|
| **persistent** | ORM (Yesod ecosystem) |
| **hasql** | PostgreSQL (mataas na pagganap) |
| **postgresql-simple** | PostgreSQL (simple) |
| **beam** | Ligtas sa uri ng SQL |
| **esqueleto** | Ligtas sa uri ng ESQL (sa patuloy na) |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **HUnit** | Pagsubok ng unit (estilo ng xUnit) |
| **masarap** | Test framework (composable) |
| **masarap-hunit** | HUnit integration para sa masarap |
| **tasty-quickcheck** | Pagsubok na nakabatay sa ari-arian |
| **QuickCheck** | Pagsubok na nakabatay sa ari-arian |
| **hedgehog** | Batay sa ari-arian (moderno) |
| **hspec** | BDD-style na pagsubok |
| **doctest** | Mga halimbawa ng pagsubok sa Haddock |
| **tasty-discover** | Mga pagsubok sa awtomatikong pagtuklas |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **hlint** | Mga mungkahi at linting |
| **formolu / ormolu** | Pag-format ng code |
| **naka-istilong-haskell** | Pag-format ng code |
| **manghahasik** | Dead code detection |
| **stan** | Static na pagsusuri |
| **haskell-language-server** | Diagnostics, mga pagkumpleto |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **base** | Karaniwang aklatan (Prelude) |
| **text** | Mahusay na mga uri ng teksto |
| **bytestring** | Binary data |
| **aeson** | JSON library |
| **mga lalagyan** | Mga mapa, set, sequence |
| **mga hindi ayos na lalagyan** | Hash na mga mapa, hash set |
| **vector** | Mahusay na array |
| **stm** | Software transactional memory |
| **async** | Async computations |
| **optparse-applicative** | CLI argument parsing |
| **optparse-generic** | Awtomatikong hinango na CLI |
| **warp** | HTTP server |
| **http-client** | HTTP client |
| **conduit** | Nag-stream ng data |
| **mga tubo** | Nag-stream ng data |
| **streaming** | Nag-stream ng data |
| **lens** | Optics library |
| **megaparsec** | Mga parser combinator |
| **parsec** | Mga parser combinator |
| **relude** | Better Prelude |
| **relude** | Alternatibong Prelude |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + HLS** | Pinakamahusay na suporta sa Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Nakabatay sa terminal sa LSP |
| **Emacs + haskell-mode** | Klasikong Haskell na kapaligiran |
| **Vim + vim-haskell** | Pagsasama ng Vim |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Static binary** | Gumagawa ang GHC ng mga static na binary |
| **Docker** | Multi-stage build (haskell image) |
| **Nix** | Reproducible build |
| **Kubernetes** | Orkestrasyon |
| **AWS Lambda** | Walang server (sa pamamagitan ng hal) |
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

## Buod
Ang ecosystem ng Haskell ay natatangi sa pagbibigay-diin nito sa kawastuhan at kaligtasan ng uri. Ang karaniwang toolchain ay: **GHC** bilang compiler, **GHCup** para sa pag-install, **Cabal** o **Stack** para sa mga build, **haskell-language-server** para sa suporta sa IDE, **hlint** para sa linting, **formolu** para sa pag-format, at **tasty + QuickCheck** para sa pagsubok. Kabilang sa mga pangunahing aklatan ang **aeson** para sa JSON, **text** para sa mga string, **servant** para sa mga type-safe na API, **lens** para sa optics, at **stm** para sa concurrency. Ang Haskell ay mahusay sa mga compiler, financial system, concurrent system, at kahit saan ang kawastuhan ay pinakamahalaga. Ang curve ng pag-aaral ay matarik, ngunit ang kabayaran ay software na gumagana nang tama sa pamamagitan ng pagtatayo.