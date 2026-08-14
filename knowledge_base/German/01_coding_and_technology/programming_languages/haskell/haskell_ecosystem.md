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
# Haskell – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Haskell-Ökosystem.
---

## Werkzeugkette
| Werkzeug | Zweck |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (der Compiler) |
| **GHCup** | Haskell-Toolchain-Installationsprogramm |
| **Kabale** | Build-System und Paketformat |
| **Stapel** | Reproduzierbares Build-Tool |
| **cabal-install** | Paketmanager |
| **Haskell-Sprachserver (HLS)** | LSP-Server |
| **ghcid** | Schnelles Kompilieren von Feedback |
| **viermol** | Codeformatierer |
| **Ormolu** | Codeformatierer |
| **hlint** | Linter / Vorschläge |
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

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **Hackage** | Zentrales Paket-Repository (über 15.000 Pakete) |
| **Stapel** | Kuratierte, kompatible Paketsets |
| **Kabale** | Paketformat und Build-Tool |
| **Stapel** | Reproduzierbare Builds (LTS-Snapshots) |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **Diener** | Typebene | Typsichere APIs |
| **Jasod** | Full-Stack | Typsichere Web-Apps |
| **Scotty** | Leicht | Einfache APIs (Sinatra-ähnlich) |
| **Spock** | Leicht | Web-Apps |
| **IHP** | Batterien im Lieferumfang enthalten | Schienenartig, Haskell |
| **Miso** | Frontend | Ulmenartiges Frontend |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **persistent** | ORM (Yesod-Ökosystem) |
| **hasql** | PostgreSQL (hochleistungsfähig) |
| **postgresql-simple** | PostgreSQL (einfach) |
| **Balken** | Typsicheres SQL |
| **esqueleto** | Typsicheres ESQL (persistent) |
| **hedis** | Redis-Client |
| **mongoDB** | MongoDB-Treiber |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **HUnit** | Unit-Tests (xUnit-Stil) |
| **lecker** | Testframework (zusammensetzbar) |
| **lecker-hunit** | HUnit-Integration für leckeres |
| **lecker-quickcheck** | Eigenschaftsbasiertes Testen |
| **QuickCheck** | Eigenschaftsbasiertes Testen |
| **Igel** | Immobilienbasiert (modern) |
| **hspec** | Tests im BDD-Stil |
| **doctest** | Testbeispiele in Haddock |
| **lecker-entdecken** | Automatische Erkennungstests |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **hlint** | Vorschläge und Linting |
| **Fourmolu / Ormolu** | Codeformatierung |
| **stylish-haskell** | Codeformatierung |
| **Unkrautjäter** | Erkennung von totem Code |
| **stan** | Statische Analyse |
| **haskell-Sprachserver** | Diagnostik, Abschluss |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Basis** | Standardbibliothek (Prelude) |
| **Text** | Effiziente Textarten |
| **Bytestring** | Binärdaten |
| **aeson** | JSON-Bibliothek |
| **Behälter** | Karten, Mengen, Sequenzen |
| **ungeordnete-Container** | Hash-Maps, Hash-Sets |
| **Vektor** | Effiziente Arrays |
| **stm** | Software-Transaktionsspeicher |
| **asynchron** | Asynchrone Berechnungen |
| **optparse-applicative** | CLI-Argumentanalyse |
| **optparse-generic** | Automatisch abgeleitete CLI |
| **Verzerrung** | HTTP-Server |
| **http-Client** | HTTP-Client |
| **Leitung** | Streaming-Daten |
| **Rohre** | Streaming-Daten |
| **Streaming** | Streaming-Daten |
| **Objektiv** | Optikbibliothek |
| **Megaparsec** | Parser-Kombinatoren |
| **Parsec** | Parser-Kombinatoren |
| **Entspannen** | Besseres Vorspiel |
| **Entspannen** | Alternatives Vorspiel |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + HLS** | Beste Haskell LSP-Unterstützung |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Terminalbasiert mit LSP |
| **Emacs + Haskell-Modus** | Klassische Haskell-Umgebung |
| **Vim + vim-haskell** | Vim-Integration |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Statische Binärdatei** | GHC erzeugt statische Binärdateien |
| **Docker** | Mehrstufige Builds (Haskell-Image) |
| **Nix** | Reproduzierbare Builds |
| **Kubernetes** | Orchestrierung |
| **AWS Lambda** | Serverlos (über hal) |
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

## Zusammenfassung
Das Ökosystem von Haskell ist einzigartig in seiner Betonung von Korrektheit und Typsicherheit. Die Standard-Toolchain ist: **GHC** als Compiler, **GHCup** für die Installation, **Cabal** oder **Stack** für Builds, **haskell-lingual-server** für IDE-Unterstützung, **hlint** für Linting, **fourmolu** für die Formatierung und **tasty + QuickCheck** für Tests. Zu den Schlüsselbibliotheken gehören **aeson** für JSON, **text** für Strings, **servant** für typsichere APIs, **lens** für Optics und **stm** für Parallelität. Haskell zeichnet sich durch Compiler, Finanzsysteme, nebenläufige Systeme und überall dort aus, wo Korrektheit von größter Bedeutung ist. Die Lernkurve ist steil, aber der Lohn ist Software, die von Anfang an korrekt funktioniert.