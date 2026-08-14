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
# Haskell — przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie Haskell.
---

## Łańcuch narzędzi
| Narzędzie | Cel |
|------|-------------|
| **GHC** | Glasgow Haskell Compiler (the compiler) |
| **GHCup** | Haskell toolchain installer |
| **Kabała** | Build system and package format |
| **Stos** | Reproducible build tool |
| **instalacja kabała** | Menedżer pakietów |
| **haskell-language-server (HLS)** | Serwer LSP |
| **ghcid** | Szybka kompilacja opinii |
| **czterymole** | Formater kodu |
| **ormolu** | Formater kodu |
| **hlint** | Linter / sugestie |
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

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **Hackage** | Central package repository (15,000+ packages) |
| **Stackage** | Curated, compatible package sets |
| **Kabała** | Package format and build tool |
| **Stos** | Reproducible builds (LTS snapshots) |
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

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Sługa** | Poziom typu | Interfejsy API bezpieczne dla typów |
| **Tak** | Pełny stos | Aplikacje internetowe bezpieczne dla typów |
| **Scotty** | Lekki | Proste API (podobne do Sinatry) |
| **Spock** | Lekki | aplikacje internetowe |
| **IHP** | Baterie w zestawie | Railsowy, Haskell |
| **Miso** | Interfejs | Nakładka przypominająca wiąz |
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

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **trwałe** | ORM (ekosystem Yesod) |
| **hasql** | PostgreSQL (wysoka wydajność) |
| **postgresql-prosty** | PostgreSQL (prosty) |
| **promień** | Bezpieczny typ SQL |
| **esqueleto** | Bezpieczny typ ESQL (na trwałym) |
| **hedis** | Klient Redisa |
| **mongoDB** | Sterownik MongoDB |
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

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **Jednostka HU** | Testowanie jednostkowe (w stylu xUnit) |
| **smaczne** | Struktura testowa (komponowalna) |
| **smaczna-hunit** | Integracja HUnit dla smacznego |
| **smaczne-szybkie sprawdzenie** | Testowanie oparte na właściwościach |
| **Szybkie sprawdzenie** | Testowanie oparte na właściwościach |
| **jeż** | Oparte na nieruchomościach (nowoczesne) |
| **hspec** | Testowanie w stylu BDD |
| **doktest** | Przykłady testów w Haddocku |
| **smaczne odkrycie** | Testy automatycznego wykrywania |
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

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **hlint** | Sugestie i linting |
| **czterymolu / ormolu** | Formatowanie kodu |
| **stylowy haskell** | Formatowanie kodu |
| **pielnik** | Wykrywanie martwego kodu |
| **stan** | Analiza statyczna |
| **serwer języka haskell** | Diagnostyka, uzupełnienia |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **podstawa** | Biblioteka standardowa (Prelude) |
| **tekst** | Wydajne typy tekstu |
| **ciąg znaków** | Dane binarne |
| **aezon** | Biblioteka JSON |
| **kontenery** | Mapy, zbiory, sekwencje |
| **nieuporządkowane-kontenery** | Mapy skrótów, zestawy skrótów |
| **wektor** | Wydajne tablice |
| **stm** | Oprogramowanie pamięci transakcyjnej |
| **asynchroniczny** | Obliczenia asynchroniczne |
| **optparse-aplikacyjny** | Analiza argumentów CLI |
| **optparse-ogólne** | Automatycznie wyprowadzony CLI |
| **wypaczenie** | Serwer HTTP |
| **klient http** | Klient HTTP |
| **przewód** | Dane strumieniowe |
| **rury** | Dane strumieniowe |
| **transmisja strumieniowa** | Dane strumieniowe |
| **obiektyw** | Biblioteka optyki |
| **megaparsek** | Kombinatory parserów |
| **parsek** | Kombinatory parserów |
| **reludium** | Lepsze Preludium |
| **reludium** | Alternatywne Preludium |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + HLS** | Najlepsza obsługa Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Oparta na terminalu z LSP |
| **Emacs + tryb haskell** | Klasyczne środowisko Haskell |
| **Vim + vim-haskell** | Integracja z Vimem |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Statyczny plik binarny** | GHC produkuje statyczne pliki binarne |
| **Doker** | Kompilacje wieloetapowe (obraz haskell) |
| **Nix** | Powtarzalne kompilacje |
| **Kubernetes** | Orkiestracja |
| **AWS Lambda** | Bezserwerowy (przez hal) |
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

## Streszczenie
Ekosystem Haskell jest wyjątkowy pod względem nacisku na poprawność i bezpieczeństwo typów. Standardowy zestaw narzędzi to: **GHC** jako kompilator, **GHCup** do instalacji, **Cabal** lub **Stack** do kompilacji, **haskell-language-server** do obsługi IDE, **hlint** do lintingu, **fourmolu** do formatowania i **tasty + QuickCheck** do testowania. Kluczowe biblioteki obejmują **aeson** dla JSON, **text** dla ciągów znaków, **servant** dla interfejsów API bezpiecznych typów, **lens** dla optyki i **stm** dla współbieżności. Haskell przoduje w kompilatorach, systemach finansowych, systemach współbieżnych i wszędzie tam, gdzie poprawność jest najważniejsza. Krzywa uczenia się jest stroma, ale nagrodą jest oprogramowanie, które działa poprawnie z założenia.