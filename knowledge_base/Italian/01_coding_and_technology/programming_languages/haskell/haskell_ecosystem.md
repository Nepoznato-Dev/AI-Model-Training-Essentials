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
# Haskell: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e le infrastrutture essenziali nell'ecosistema Haskell.
---

## Catena di strumenti
| Strumento | Scopo |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (il compilatore) |
| **GHCup** | Programma di installazione della toolchain Haskell |
| **Cabala** | Compila il sistema e il formato del pacchetto |
| **Pila** | Strumento di creazione riproducibile |
| **installazione cabala** | Gestore pacchetti |
| **server della lingua haskell (HLS)** | Server LSP |
| **ghcid** | Feedback di compilazione rapida |
| **quattromolu** | Formattatore di codice |
| **ormolu** | Formattatore di codice |
| **suggerimento** | Linter / suggerimenti |
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

## Gestione dei pacchetti
| Strumento | Scopo |
|------|---------|
| **Hackage** | Repository centrale dei pacchetti (oltre 15.000 pacchetti) |
| **Stackage** | Set di pacchetti curati e compatibili |
| **Cabala** | Formato del pacchetto e strumento di creazione |
| **Pila** | Build riproducibili (istantanee LTS) |
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

## Framework Web
| Quadro | Digitare | Ideale per |
|-----------|------|----------|
| **Servo** | Livello di tipo | API indipendenti dai tipi |
| **Sìod** | Stack completo | App Web indipendenti dai tipi |
| **Scotty** | Leggero | API semplici (simili a Sinatra) |
| **Spock** | Leggero | App Web |
| **IHP** | Batterie incluse | Simile a Rails, Haskell |
| **Miso** | Frontend | Frontend simile a Elm |
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

##Banca dati
| Tecnologia | Digitare |
|------------|------|
| **persistente** | ORM (ecosistema Yesod) |
| **hasql** | PostgreSQL (ad alte prestazioni) |
| **postgresql-simple** | PostgreSQL (semplice) |
| **fascio** | SQL indipendente dai tipi |
| **esqueletto** | ESQL indipendente dai tipi (su persistente) |
| **hedis** | Cliente Redis |
| **mongoDB** | Driver MongoDB |
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

## Test
| Quadro | Scopo |
|-----------|---------|
| **UnitàH** | Test unitario (stile xUnit) |
| **gustoso** | Quadro di test (componibile) |
| **tasty-hunit** | Integrazione HUnit per gustoso |
| **gustoso controllo rapido** | Test basati sulle proprietà |
| **Controllo rapido** | Test basati sulle proprietà |
| **riccio** | Basato sulla proprietà (moderno) |
| **hspec** | Test in stile BDD |
| **doctest** | Esempi di test in Haddock |
| **gustoso-scopri** | Test di individuazione automatica |
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

## Qualità del codice
| Strumento | Scopo |
|------|---------|
| **suggerimento** | Suggerimenti e lanugine |
| **fourmolu / ormolu** | Formattazione del codice |
| **haskell elegante** | Formattazione del codice |
| **sarchiatore** | Rilevamento del codice morto |
| **stan** | Analisi statica |
| **server-linguaggio-haskell** | Diagnostica, completamenti |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Biblioteche chiave
| Biblioteca | Scopo |
|---------|---------|
| **base** | Libreria standard (Preludio) |
| **testo** | Tipi di testo efficienti |
| **stringa di byte** | Dati binari |
| **aesone** | Libreria JSON |
| **contenitori** | Mappe, insiemi, sequenze |
| **contenitori-non ordinati** | Mappe hash, set di hash |
| **vettore** | Array efficienti |
| **stm** | Memoria transazionale del software |
| **asincrono** | Calcoli asincroni |
| **optparse-applicativo** | Analisi degli argomenti CLI |
| **optparse-generico** | CLI derivata automaticamente |
| **ordito** | ServerHTTP |
| **cliente http** | Client HTTP |
| **condotto** | Dati in streaming |
| **tubi** | Dati in streaming |
| **streaming** | Dati in streaming |
| **lente** | Libreria di ottica |
| **megaparsec** | Combinatori parser |
| **parsec** | Combinatori parser |
| **rinuncia** | Preludio migliore |
| **rinuncia** | Preludio alternativo |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + HLS** | Miglior supporto Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Basato su terminale con LSP |
| **Emacs + modalità haskell** | Ambiente Haskell classico |
| **Vim + vim-haskell** | Integrazione Vim |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Binario statico** | GHC produce binari statici |
| **Docker** | Build in più fasi (immagine haskell) |
| **Niente** | Build riproducibili |
| **Kubernetes** | Orchestrazione |
| **AWS Lambda** | Serverless (tramite hal) |
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

## Riepilogo
L'ecosistema di Haskell è unico nella sua enfasi sulla correttezza e sulla sicurezza del tipo. La toolchain standard è: **GHC** come compilatore, **GHCup** per l'installazione, **Cabal** o **Stack** per le build, **haskell-lingual-server** per il supporto IDE, **hlint** per linting, **fourmolu** per la formattazione e **tasty + QuickCheck** per i test. Le librerie di chiavi includono **aeson** per JSON, **text** per stringhe, **servant** per API indipendenti dai tipi, **lens** per ottica e **stm** per concorrenza. Haskell eccelle nei compilatori, nei sistemi finanziari, nei sistemi concorrenti e ovunque la correttezza sia fondamentale. La curva di apprendimento è ripida, ma il profitto è un software che funziona correttamente per costruzione.